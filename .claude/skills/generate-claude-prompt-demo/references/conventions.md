# Conventions & Templates

## Folder Naming

- PascalCase, no spaces, no hyphens: `CosmicKeystrokes`, `PythonBugBuster`, `ExcelFormulaExpert`
- The folder name becomes the demo name in README headings

## Output File Naming

- Lowercase or kebab-case: `typing-game.html`, `formula.md`, `solution.py`
- Name should reflect the content, not just the folder name

## README Demo Entry Template

```markdown
### DemoName

<One-sentence description of what Claude generated and what it does.>

**Files:**
- `prompt.md` — <brief description of the prompt>
- [`output-file.html`](DemoName/output-file.html) — <what it does; open directly in a browser>
- **Live demo:** https://mikewangmax.github.io/claude-prompt-library/DemoName/output-file.html

---
```

**Rules:**
- Add `**Live demo:**` only for `.html` files served via GitHub Pages
- Use a markdown link `[filename](path)` only for `.html` files (directly openable in a browser)
- Non-HTML files (`.md`, `.gs`, `.py`) use plain text: `` - `formula.md` — the generated formula and explanation ``
- End each demo section with `---`

## README Project Structure Block

Keep this block in sync whenever a demo is added or removed:

```markdown
## Project Structure

```
claude-prompt-library/
├── CosmicKeystrokes/       # Side-scrolling typing game (HTML)
├── ExcelFormulaExpert/     # Advanced Excel formula generation
├── GoogleAppsScriper/      # Google Slides translation via Apps Script
├── PythonBugBuster/        # Python bug analysis and fix
└── WebsiteWizard/          # One-page website generator (HTML)
```
```

## GitHub Pages URL Pattern

```
https://mikewangmax.github.io/claude-prompt-library/<FolderName>/<output-file.html>
```

Only `.html` files are browsable via GitHub Pages. Markdown, scripts, and other files are not served.

## prompt.md Format

Preserve the prompt text **exactly** as extracted from the library page — no paraphrasing, trimming, or reformatting.

If the page has both System and User sections:

```
**System:**
<system prompt text>

**User:**
<user prompt text>
```

If the page has a multi-turn conversation (System, User, Assistant Prefill, and/or additional User turns):

```
**System:**
<system prompt text>

**User:**
<first user message>

**Assistant (Prefill):**
<assistant prefill text>

**User:**
<second user message>
```

Include every turn from the table in order. Use **bold labels** matching the row headers on the page.

If only a User prompt (no System row on the page), just write the raw text with no labels.

## URL Slug → Folder Name

URL pattern: `https://platform.claude.com/docs/en/resources/prompt-library/<slug>`

Conversion: split slug on `-`, capitalise each word, join with no separator.

| Slug                  | Folder name           |
|-----------------------|-----------------------|
| `website-wizard`      | `WebsiteWizard`       |
| `python-bug-buster`   | `PythonBugBuster`     |
| `excel-formula-expert`| `ExcelFormulaExpert`  |
| `cosmic-keystrokes`   | `CosmicKeystrokes`    |
