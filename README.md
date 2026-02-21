# Claude Prompt Library — Demos

Hands-on demos built from prompts in the [Anthropic Claude Prompt Library](https://platform.claude.com/docs/en/resources/prompt-library/library). Each folder contains the original prompt(s) and the output Claude generated from them.

## Project Structure

```
claude-prompt-library/
├── CosmicKeystrokes/       # Side-scrolling typing game (HTML)
├── ExcelFormulaExpert/     # Advanced Excel formula generation
├── GoogleAppsScriper/      # Google Slides translation via Apps Script
├── SqlSorcerer/            # Natural language to SQL query
├── StorytellingSidekick/   # Collaborative storytelling with plot twists
└── WebsiteWizard/          # One-page website generator (HTML)
```

## Demos

### CosmicKeystrokes

A fully self-contained side-scrolling typing game in a single HTML file. The player moves through a world using WASD, encounters random words, and must type them as fast as possible to earn points. Styled with Tailwind CSS.

**Files:**
- `prompt.md` — the user prompt sent to Claude
- [`typing-game.html`](CosmicKeystrokes/typing-game.html) — the generated game, open directly in a browser
- **Live demo:** https://mikewangmax.github.io/claude-prompt-library/CosmicKeystrokes/typing-game.html

---

### ExcelFormulaExpert

Demonstrates Claude acting as an Excel formula expert. Given a sales data table (salesperson, product category, amount, date), Claude generates an advanced `SUMPRODUCT` formula to total sales filtered by category ("Electronics") and month (January), with a full explanation of each component.

**Files:**
- `prompt.md` — the system + user prompt
- `formula.md` — the generated formula and explanation

---

### GoogleAppsScriper

A Google Apps Script that iterates over every slide and text element in a Google Slides presentation and translates all content to Korean using the `LanguageApp` service.

**Files:**
- `prompt.md` — the user prompt
- `translateToKorean.gs` — the generated Apps Script (paste into Google Apps Script editor)

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
