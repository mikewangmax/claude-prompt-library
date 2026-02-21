---
name: batch-generate-demos
description: Batch-process multiple Anthropic Prompt Library URLs into demos for the claude-prompt-library repo. Accepts URLs as arguments or from a file. Generates all demos in parallel using sub-agents, then commits each demo individually for clean git history. Use when adding multiple demos at once, e.g. "batch generate these demos", "add all these URLs", or when providing a list of prompt library URLs.
---

# Batch Demo Generator

Processes multiple Anthropic Prompt Library URLs in parallel, creating demo folders with `prompt.md` and generated output for each, then committing each demo individually for clean git history.

Repo path: `/Users/wangxin/Documents/claude/deep.learning.courses/claude-prompt-library`
GitHub Pages root: `https://mikewangmax.github.io/claude-prompt-library/`

## Invocation

```
/batch-generate-demos <url1> <url2> <url3> ...
/batch-generate-demos --file <path-to-urls.txt>
```

When `--file` is the first argument, read the specified file (one URL per line, blank lines and `#` comments ignored). Otherwise treat all arguments as space-separated URLs.

---

## Phase 1 — Validate & Plan

1. **Parse the URL list** from arguments or file.
2. **Validate each URL** matches `https://platform.claude.com/docs/en/resources/prompt-library/<slug>`. Reject invalid URLs with a warning.
3. **Derive folder names**: split slug on `-`, capitalise each word, join → PascalCase (e.g. `sql-sorcerer` → `SqlSorcerer`).
4. **Check for existing folders** in the repo. Skip any URL whose folder already exists — report as "already exists, skipping".
5. **Report the plan** to the user:
   ```
   Will generate N demos: FolderA, FolderB, FolderC, ...
   Skipping M already-existing: FolderX, FolderY
   ```

---

## Phase 2 — Parallel Content Generation

Process URLs in **waves of up to 50 concurrent sub-agents**. For each wave:

1. Take the next batch of up to 50 URLs from the queue.
2. Launch one `Task` tool call per URL **in a single message** (this makes them run in parallel). Use `subagent_type: "general-purpose"`.
3. Each sub-agent receives this prompt (fill in the `<placeholders>`):

````
You are generating a demo for the claude-prompt-library repo.

**URL:** <url>
**Folder name:** <PascalCaseName>
**Repo path:** /Users/wangxin/Documents/claude/deep.learning.courses/claude-prompt-library

## Instructions

### Step 1 — Fetch the prompt
Use WebFetch on the URL. The page has a table with rows labeled "System", "User", and sometimes "Assistant (Prefill)" or additional "User" turns.
Extract **all** rows from the table (System, User, Assistant Prefill, etc.). Some pages only have a User row (no System).
Ignore the "Example output" and "API request" sections entirely.

### Step 2 — Create prompt.md
Write the file `<PascalCaseName>/prompt.md` at the repo path.

Format — include ALL turns from the page table, in order, using **bold labels** with colons:

For a simple System + User prompt:
```
**System:**
<system prompt text verbatim>

**User:**
<user prompt text verbatim>
```

For multi-turn prompts (with Assistant Prefill and/or multiple User turns):
```
**System:**
<system prompt text verbatim>

**User:**
<first user message verbatim>

**Assistant (Prefill):**
<assistant prefill text verbatim>

**User:**
<second user message verbatim>
```

If only a User prompt (no System row), write the raw text with no labels.

Do NOT paraphrase or trim the prompt text.

### Step 3 — Execute the prompt
Use the System prompt as your system instructions. If there are prior User + Assistant turns, treat them as conversation context. Generate a response to the **final User message**.

### Step 4 — Choose output filename
Pick a descriptive kebab-case filename:
- `.html` for web apps, games, or interactive pages
- `.md` for text, stories, formulas, analyses, explanations
- `.py` for Python code
- `.gs` for Google Apps Script

### Step 5 — Save the output
Write the generated content to `<PascalCaseName>/<chosen-filename>` at the repo path.

### Step 6 — Return result
At the very end of your response, output EXACTLY this block (no extra text after it):

RESULT_JSON:
{"folderName":"<PascalCaseName>","outputFile":"<chosen-filename>","description":"<one-sentence description of what was generated>","isHtml":<true or false>,"status":"success"}

If you encounter an error at any step, still output the block but with `"status":"failed"` and add an `"error":"<what went wrong>"` field.
````

4. Wait for all sub-agents in the wave to complete.
5. Parse the `RESULT_JSON:` line from each sub-agent's response. Collect results into a list.
6. Report wave progress: `Wave N complete: X/Y succeeded.`
7. Repeat until all URLs are processed.

---

## Phase 3 — Commit Each Demo Individually

After all waves complete, collect the successful results sorted alphabetically by `folderName`. Then **for each result**, perform these steps sequentially:

### 3a. Update README.md for this demo

1. Read the current `README.md`.
2. **Insert a new entry** into the `## Demos` section in alphabetical order among existing entries. Use the template from `references/conventions.md`:

   For non-HTML output:
   ```markdown
   ### <folderName>

   <description>

   **Files:**
   - `prompt.md` — the system + user prompt
   - `<outputFile>` — <brief description>

   ---
   ```

   For HTML output (add live demo link):
   ```markdown
   ### <folderName>

   <description>

   **Files:**
   - `prompt.md` — the system + user prompt
   - [`<outputFile>`](<folderName>/<outputFile>) — <brief description>, open directly in a browser
   - **Live demo:** https://mikewangmax.github.io/claude-prompt-library/<folderName>/<outputFile>

   ---
   ```

3. Update the `## Project Structure` tree block to include the new folder in alphabetical order. Use `├──` for all entries except the last which uses `└──`. Add a short `# comment`.

### 3b. Commit this demo

```bash
git add <FolderName>/ README.md
git commit -m "$(cat <<'EOF'
Add <FolderName> demo

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

Repeat steps 3a–3b for each successful demo before moving to the next.

### 3c. Push and report

After all individual commits are created, push once:

```bash
git push
```

Then print the final report:

```
Done! Added N demos (N individual commits).
Failed: [list any failures, or "none"]
```

---

## Error Handling

| Failure | Action |
|---------|--------|
| Invalid URL format | Skip with warning in Phase 1 |
| Folder already exists | Skip with note in Phase 1 |
| WebFetch fails | Sub-agent returns `status: "failed"`. Excluded from README. Reported at end. |
| Sub-agent fails to generate output | Same as above. Partial folder (prompt.md only) left in place. |
| git push fails | Report error, suggest manual resolution |

Failed URLs can be retried individually with `/generate-claude-prompt-demo <url>`.
