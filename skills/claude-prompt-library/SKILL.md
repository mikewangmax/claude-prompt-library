---
name: claude-prompt-library
description: Workflow skill for managing the claude-prompt-library showcase repo at /Users/wangxin/Documents/claude/deep.learning.courses/claude-prompt-library. Use when the user provides an Anthropic Prompt Library URL to add as a new demo, or when adding demos, generating Claude outputs, updating the README, publishing to GitHub Pages, or any repo housekeeping. Triggers on tasks like "add this demo [url]", "add a new demo", "generate output for this prompt", "update the README", "commit and push", "consolidate settings", or "maintain the repo structure".
---

# claude-prompt-library

Showcases Claude-generated outputs from the [Anthropic Claude Prompt Library](https://platform.claude.com/docs/en/resources/prompt-library/library).
GitHub Pages root: `https://mikewangmax.github.io/claude-prompt-library/`
Repo path: `/Users/wangxin/Documents/claude/deep.learning.courses/claude-prompt-library`

## Core Structure

Every demo = one PascalCase folder:

```
DemoName/
├── prompt.md      # Verbatim prompt extracted from the library page — never modify after creation
└── <output>       # Claude-generated file(s): .html, .md, .py, .gs, etc.
```

## Primary Workflow: Add a Demo from a URL

When the user provides a URL like `https://platform.claude.com/docs/en/resources/prompt-library/website-wizard`:

**Step 1 — Derive the folder name**
Convert the URL slug to PascalCase: split on `-`, capitalise each word, join.
- `website-wizard` → `WebsiteWizard`
- `python-bug-buster` → `PythonBugBuster`
- `excel-formula-expert` → `ExcelFormulaExpert`

**Step 2 — Fetch the prompt**
Use WebFetch on the URL. Extract the **System** and **User** prompt text from the page table. Ignore the example output and API request sections.

**Step 3 — Create `DemoName/prompt.md`**
Write the prompts verbatim using the format in `references/conventions.md`. Do not paraphrase or trim.

**Step 4 — Execute the prompt**
Run the System + User prompt in the current Claude session. Generate the full output.

**Step 5 — Choose the output filename**
Pick a descriptive kebab-case name based on what was generated:

| Output type        | Extension | Example                |
|--------------------|-----------|------------------------|
| Web app / game     | `.html`   | `typing-game.html`     |
| Formula / docs     | `.md`     | `formula.md`           |
| Google Apps Script | `.gs`     | `translateToKorean.gs` |
| Python code        | `.py`     | `solution.py`          |

**Step 6 — Save the output**
Write the generated content to `DemoName/<output-file>`.

**Step 7 — Update README.md**
Add an entry under `## Demos` and update the `## Project Structure` block.
See `references/conventions.md` for the exact README entry template.

**Step 8 — Commit and push**

```bash
git add <files>
git commit -m "$(cat <<'EOF'
Add <DemoName> demo

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
git push
```

## Repo Maintenance

- **settings.local.json**: Always consolidated at `.claude/settings.local.json` — never create sub-folder copies
- **README structure block**: Keep `## Project Structure` in sync with actual demo folders
- **Live demo links**: Only `.html` files get a `**Live demo:**` line in README

## Other Git Operations

Common commit verbs: `Add`, `Update`, `Fix`, `Remove`
