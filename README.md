# Claude Prompt Library — Demos

Hands-on demos built from prompts in the [Anthropic Claude Prompt Library](https://platform.claude.com/docs/en/resources/prompt-library/library). Each folder contains the original prompt(s) and the output Claude generated from them.

## Project Structure

```
claude-prompt-library/
├── CosmicKeystrokes/       # Side-scrolling typing game (HTML)
├── CodeConsultant/         # Python performance optimization analysis
├── CulinaryCreator/        # Personalized gluten-free recipe ideas
├── DreamInterpreter/       # Dream symbolism analysis
├── EthicalDilemmaNavigator/ # Multi-framework ethical dilemma analysis
├── ExcelFormulaExpert/     # Advanced Excel formula generation
├── FunctionFabricator/     # Python Sudoku solver
├── GitGud/                 # Git commands guide for saving changes
├── GoogleAppsScriper/      # Google Slides translation via Apps Script
├── HalTheHumorousHelper/   # Sarcastic yet helpful AI assistant
├── IdiomIlluminator/       # Idiom meaning and origin explanation
├── LatexLegend/            # LaTeX table creation guide
├── MoodColorizer/          # Mood-to-color converter (HTML)
├── PortmanteauPoet/        # Creative portmanteau word blending
├── PunDit/                 # Pun and wordplay generator
├── SimileSavant/           # Creative similes for joyful laughter
├── SqlSorcerer/            # Natural language to SQL query
├── StorytellingSidekick/   # Collaborative storytelling with plot twists
└── WebsiteWizard/          # One-page website generator (HTML)
```

## Demos

### CodeConsultant

Performance analysis of a Python Fibonacci function with five optimization strategies ranging from pre-allocation to O(log n) matrix exponentiation.

**Files:**
- `prompt.md` — the system + user prompt
- `fibonacci-optimization.md` — five Fibonacci optimization strategies with comparison table

---

### CosmicKeystrokes

A fully self-contained side-scrolling typing game in a single HTML file. The player moves through a world using WASD, encounters random words, and must type them as fast as possible to earn points. Styled with Tailwind CSS.

**Files:**
- `prompt.md` — the user prompt sent to Claude
- [`typing-game.html`](CosmicKeystrokes/typing-game.html) — the generated game, open directly in a browser
- **Live demo:** https://mikewangmax.github.io/claude-prompt-library/CosmicKeystrokes/typing-game.html

---

### CulinaryCreator

Demonstrates Claude as a personalized recipe generator. Given a list of available ingredients (chicken breast, broccoli, carrots, onion, garlic, olive oil, rice, gluten-free soy sauce, honey) and a gluten-free dietary preference, Claude suggests three complete recipes — a honey garlic stir-fry, a one-pan rice bake, and fried rice — each with ingredient lists, step-by-step instructions, and practical tips.

**Files:**
- `prompt.md` — the system + user prompt
- `recipes.md` — the generated recipes

---

### DreamInterpreter

Demonstrates Claude as a dream interpretation assistant. Given a dream about walking through a dark forest, encountering a white stag that transforms into a wise old man, and receiving a golden key, Claude provides a detailed symbol-by-symbol analysis drawing on Jungian archetypes, mythological traditions, and narrative structure — with reflective questions for the dreamer.

**Files:**
- `prompt.md` — the system + user prompt
- `interpretation.md` — the generated dream analysis

---

### EthicalDilemmaNavigator

A comprehensive multi-framework ethical analysis of a journalist's dilemma about publishing a government corruption story versus accepting a bribe.

**Files:**
- `prompt.md` — the system + user prompt
- `ethical-dilemma-analysis.md` — multi-framework ethical analysis with consequence mapping and reflective questions

---

### ExcelFormulaExpert

Demonstrates Claude acting as an Excel formula expert. Given a sales data table (salesperson, product category, amount, date), Claude generates an advanced `SUMPRODUCT` formula to total sales filtered by category ("Electronics") and month (January), with a full explanation of each component.

**Files:**
- `prompt.md` — the system + user prompt
- `formula.md` — the generated formula and explanation

---

### HalTheHumorousHelper

A sarcastic yet helpful cooking advice response from Hal, featuring tiered meal suggestions ranked by effort level with witty commentary throughout.

**Files:**
- `prompt.md` — the system + user prompt
- `hal-cooking-advice.md` — Hal's sarcastic cooking advice with tiered meal suggestions

---

### FunctionFabricator

A Python Sudoku solver using backtracking with input validation, edge case handling, and comprehensive documentation.

**Files:**
- `prompt.md` — the system + user prompt
- `sudoku-solver.py` — Python Sudoku solver with backtracking algorithm

---

### GitGud

A comprehensive guide explaining Git commands for saving local changes, covering git add, git commit, useful variations, and recommended workflow practices.

**Files:**
- `prompt.md` — the user prompt
- `git-save-changes.md` — guide to saving changes with Git

---

### GoogleAppsScriper

A Google Apps Script that iterates over every slide and text element in a Google Slides presentation and translates all content to Korean using the `LanguageApp` service.

**Files:**
- `prompt.md` — the user prompt
- `translateToKorean.gs` — the generated Apps Script (paste into Google Apps Script editor)

---

### IdiomIlluminator

A comprehensive explanation of the meaning and origin of the idiom "Break a leg," covering six historical theories and cross-cultural parallels.

**Files:**
- `prompt.md` — the system + user prompt
- `idiom-explanation.md` — meaning, origin theories, and cross-cultural parallels for "Break a leg"

---

### LatexLegend

A comprehensive LaTeX table creation guide with basic code, line-by-line explanations, five style variations (alignment, booktabs, colored headers, multi-column/multi-row), a compilable minimal working example, and a quick reference of common table commands.

**Files:**
- `prompt.md` — the system + user prompt
- `latex-table-guide.md` — the generated LaTeX table guide

---

### MoodColorizer

Interactive mood-to-color converter using color psychology principles with keyword analysis, color harmonies, history tracking, and ambient visual feedback.

**Files:**
- `prompt.md` — the system + user prompt
- [`mood-colorizer.html`](MoodColorizer/mood-colorizer.html) — interactive mood-to-color app, open directly in a browser
- **Live demo:** https://mikewangmax.github.io/claude-prompt-library/MoodColorizer/mood-colorizer.html

---

### PortmanteauPoet

Demonstrates Claude as a creative portmanteau generator. Given the words "music" and "therapy," Claude produces a curated collection of innovative word blends — from "Musitherapy" to "Rhythmedy" — each with pronunciation guides, etymological breakdowns, and context suggestions for when to use them.

**Files:**
- `prompt.md` — the system + user prompt
- `portmanteaus.md` — the generated portmanteau options

---

### PunDit

Demonstrates Claude as a pun and wordplay generator. Given the topic "Fishing," Claude produces a categorized collection of original fish-themed puns, plays on words, and humorous phrases — from "reel talk" to "o-fish-ally on vacation" — organized into themed sections with witty commentary.

**Files:**
- `prompt.md` — the system + user prompt
- `puns.md` — the generated puns and wordplay

---

### SimileSavant

A collection of 15 vivid similes describing joyful and contagious laughter, using imagery like silver bells, champagne, popcorn, and carnival drums.

**Files:**
- `prompt.md` — the user prompt
- `joyful-laughter-similes.md` — creative similes for contagious laughter

---

### SqlSorcerer

Demonstrates Claude transforming a natural language request into a valid SQL query. Given a multi-table e-commerce database schema (Customers, Products, Orders, Order_Items, Reviews, Employees), Claude generates a query to find customers who have placed orders but never left a review, along with their total spend — complete with a step-by-step explanation of each clause.

**Files:**
- `prompt.md` — the system + user prompt
- `query.md` — the generated SQL query and explanation

---

### StorytellingSidekick

Demonstrates Claude as a collaborative storytelling partner. Given a premise about a young woman named Lila who discovers she can control the weather, Claude builds an engaging multi-chapter narrative with vivid characters, plot twists, and interactive story direction options for the reader to shape what happens next.

**Files:**
- `prompt.md` — the system + user prompt
- `story.md` — the generated collaborative story

---

### WebsiteWizard

A one-page website for a fictional online learning platform called **EduQuest**, generated from a detailed specification prompt. Features include a fixed nav bar, a hero section with a rotating tagline, featured course cards, an interactive learning-path quiz, student testimonials, and a contact modal. All HTML, CSS, and JavaScript are embedded in a single file.

**Files:**
- `prompt.md` — the system + user prompt
- [`eduquest.html`](WebsiteWizard/eduquest.html) — the generated website, open directly in a browser
- **Live demo:** https://mikewangmax.github.io/claude-prompt-library/WebsiteWizard/eduquest.html

## How to Use

1. Browse a folder to see the prompt that was used.
2. Open `.html` files directly in a browser, or use the **Live demo** links above to run the web demos online.
3. Paste `.gs` files into the [Google Apps Script editor](https://script.google.com) to run the script demo.
4. Reference `formula.md` for the Excel formula and copy it into your spreadsheet.

## Reference

- [Claude Prompt Library](https://platform.claude.com/docs/en/resources/prompt-library/library)
- [Anthropic Documentation](https://docs.anthropic.com)
