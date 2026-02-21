# Claude Prompt Library — Demos

Hands-on demos built from prompts in the [Anthropic Claude Prompt Library](https://platform.claude.com/docs/en/resources/prompt-library/library). Each folder contains the original prompt(s) and the output Claude generated from them.

## Project Structure

```
claude-prompt-library/
├── CosmicKeystrokes/       # Side-scrolling typing game (HTML)
├── AdaptiveEditor/         # Style-adapted text rewriting
├── AirportCodeAnalyst/     # IATA airport code extraction
├── AlienAnthropologist/    # Alien field report on human behavior
├── AlliterationAlchemist/  # Alliterative phrase generation
├── BabelsBroadcasts/       # Multilingual product announcements
├── BrandBuilder/           # Brand identity design brief
├── CareerCoach/            # AI career transition roadmap
├── CodeClarifier/          # Plain-language code explanation
├── CodeConsultant/         # Python performance optimization analysis
├── CsvConverter/            # JSON to CSV data conversion
├── DataOrganizer/          # Unstructured text to JSON
├── DirectionDecoder/       # Natural language to step-by-step directions
├── CulinaryCreator/        # Personalized gluten-free recipe ideas
├── DreamInterpreter/       # Dream symbolism analysis
├── EfficiencyEstimator/    # Big O complexity analysis
├── EmailExtractor/         # Email address extraction from text
├── EmojiEncoder/           # Text-to-emoji message encoding
├── EthicalDilemmaNavigator/ # Multi-framework ethical dilemma analysis
├── ExcelFormulaExpert/     # Advanced Excel formula generation
├── FunctionFabricator/     # Python Sudoku solver
├── FuturisticFashionAdvisor/ # Avant-garde outfit suggestions
├── GitGud/
├── GradingGuru/            # Text quality evaluation
├── GrammarGenie/           # Grammar correction                 # Git commands guide for saving changes
├── GoogleAppsScriper/      # Google Slides translation via Apps Script
├── HalTheHumorousHelper/   # Sarcastic yet helpful AI assistant
├── IdiomIlluminator/       # Idiom meaning and origin explanation
├── InterviewQuestionCrafter/ # Interview question generation       # Idiom meaning and origin explanation
├── LatexLegend/            # LaTeX table creation guide
├── LessonPlanner/          # Comprehensive lesson plan creation
├── MasterModerator/        # Content moderation classifier
├── MeetingScribe/          # Meeting notes to structured summary
├── MemoMaestro/            # Professional company memo drafting
├── MindfulnessMentor/      # Guided mindfulness meditation
├── MoodColorizer/          # Mood-to-color converter (HTML)
├── MotivationalMuse/       # Personalized motivational messages          # Mood-to-color converter (HTML)
├── NeologismCreator/       # Creative neologism invention
├── PerspectivesPonderer/   # Multi-perspective analysis
├── PhilosophicalMusings/   # Philosophical discussion and analysis
├── PiiPurifier/            # PII redaction from text
├── PolyglotSuperpowers/    # Multilingual translation            # PII redaction from text
├── PortmanteauPoet/        # Creative portmanteau word blending
├── ProductNamingPro/       # Creative product name suggestions
├── ProsePolisher/          # Copyediting and prose improvement
├── PunDit/                 # Pun and wordplay generator
├── ReviewClassifier/       # Feedback categorization with sentiment
├── RiddleMeThis/           # Creative riddle generation
├── SciFiScenarioSimulator/ # Sci-fi scenario exploration
├── SecondGradeSimplifier/  # Complex topics simplified for kids
├── SimileSavant/           # Creative similes for joyful laughter
├── SocraticSage/           # Socratic dialogue and questioning
├── SpreadsheetSorcerer/    # CSV spreadsheet data generation
├── SqlSorcerer/            # Natural language to SQL query
├── TongueTwister/          # Creative tongue twister collection
├── TriviaGenerator/        # Trivia questions with progressive hints
├── TweetToneDetector/      # Tweet tone and sentiment analysis
├── StorytellingSidekick/   # Collaborative storytelling with plot twists
├── VrFitnessInnovator/     # VR fitness game concepts
└── WebsiteWizard/          # One-page website generator (HTML)
```

## Demos

### AdaptiveEditor

A pirate-style rewrite of a paragraph about Carl Linnaeus and his binomial nomenclature system from Systema Naturae.

**Files:**
- `prompt.md` — the user prompt
- `output.md` — pirate-style rewrite of a scientific paragraph

---

### AlienAnthropologist

An alien anthropologist's detailed field report analyzing human social interactions and relationships, covering bonding types, communication systems, rituals, conflict patterns, and evolutionary hypotheses.

**Files:**
- `prompt.md` — the system + user prompt
- `output.md` — alien field report on human social behavior

---

### AlliterationAlchemist

Twenty alliterative phrases and sentences evoking ocean imagery, marine life, and coastal landscapes.

**Files:**
- `prompt.md` — the system + user prompt
- `output.md` — alliterative ocean-themed phrases

---

### AirportCodeAnalyst

Identifies and lists IATA airport codes (SEA, AMS, CDG, FCO) extracted from a travel itinerary text.

**Files:**
- `prompt.md` — the system + user prompt
- `output.md` — extracted airport codes from travel text

---

### BabelsBroadcasts

Product announcement tweets for AI-powered binoculars in the 10 most commonly spoken languages.

**Files:**
- `prompt.md` — the user prompt
- `output.md` — multilingual product announcement tweets

---

### BrandBuilder

A comprehensive holistic brand identity design brief for an eco-friendly fashion brand called Verdana Collective, covering name, logo, colors, typography, visual style, tone of voice, and brand personality.

**Files:**
- `prompt.md` — the system + user prompt
- `brand-identity-brief.md` — complete brand identity design brief

---

### CareerCoach

AI career coach provides a comprehensive roadmap for transitioning into an AI career, covering skill assessment, learning paths, career options, practical experience, networking, and a realistic timeline.

**Files:**
- `prompt.md` — the system + user prompt
- `output.md` — AI career transition roadmap and advice

---

### CodeClarifier

A plain-language explanation of a Python bubble sort code snippet, broken into digestible parts with analogies and a summary table.

**Files:**
- `prompt.md` — the system + user prompt
- `output.md` — beginner-friendly code explanation with analogies

---

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

### CsvConverter

Converts a JSON array of contact records into a semicolon-delimited CSV with double-quoted values, plus saving and import instructions.

**Files:**
- `prompt.md` — the system + user prompt
- `json-to-csv-conversion.md` — JSON to semicolon-delimited CSV conversion with instructions

---

### CulinaryCreator

Demonstrates Claude as a personalized recipe generator. Given a list of available ingredients (chicken breast, broccoli, carrots, onion, garlic, olive oil, rice, gluten-free soy sauce, honey) and a gluten-free dietary preference, Claude suggests three complete recipes — a honey garlic stir-fry, a one-pan rice bake, and fried rice — each with ingredient lists, step-by-step instructions, and practical tips.

**Files:**
- `prompt.md` — the system + user prompt
- `recipes.md` — the generated recipes

---

### DataOrganizer

Converts unstructured text about notable residents into a structured JSON array with fields for name, age, profession, education, accomplishments, and village.

**Files:**
- `prompt.md` — the system + user prompt
- `output.json` — structured JSON data from unstructured text

---

### DirectionDecoder

Step-by-step directions for making a cup of tea, transformed from a natural language description into clear, sequential, imperative instructions.

**Files:**
- `prompt.md` — the system + user prompt
- `output.md` — step-by-step directions extracted from prose

---

### DreamInterpreter

Demonstrates Claude as a dream interpretation assistant. Given a dream about walking through a dark forest, encountering a white stag that transforms into a wise old man, and receiving a golden key, Claude provides a detailed symbol-by-symbol analysis drawing on Jungian archetypes, mythological traditions, and narrative structure — with reflective questions for the dreamer.

**Files:**
- `prompt.md` — the system + user prompt
- `interpretation.md` — the generated dream analysis

---

### EmojiEncoder

Shakespeare's "All the world's a stage" quote converted into an expressive emoji-rich message with key words replaced by relevant emojis.

**Files:**
- `prompt.md` — the system + user prompt
- `emoji-encoded-message.md` — emoji-encoded Shakespeare quote

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

### MeetingScribe

A concise, professionally formatted meeting summary distilling notes from a Verona reconciliation meeting into key takeaways, action items by responsible party, and next steps.

**Files:**
- `prompt.md` — the system + user prompt
- `meeting-summary.md` — structured meeting summary with action items and next steps

---

### MemoMaestro

A comprehensive, professionally formatted company memo announcing the Fit4Success employee wellness program with objectives, components, incentives, and enrollment details.

**Files:**
- `prompt.md` — the system + user prompt
- `company-wellness-memo.md` — professional company memo for a wellness program launch

---

### MindfulnessMentor

A comprehensive guided mindfulness meditation practice with breath awareness, body scan, tips for sustainability, and a quick stress reset technique.

**Files:**
- `prompt.md` — the system + user prompt
- `mindfulness-meditation-guide.md` — guided meditation with breath awareness and body scan

---

### MoodColorizer

Interactive mood-to-color converter using color psychology principles with keyword analysis, color harmonies, history tracking, and ambient visual feedback.

**Files:**
- `prompt.md` — the system + user prompt
- [`mood-colorizer.html`](MoodColorizer/mood-colorizer.html) — interactive mood-to-color app, open directly in a browser
- **Live demo:** https://mikewangmax.github.io/claude-prompt-library/MoodColorizer/mood-colorizer.html

---

### NeologismCreator

A creative neologism "cognoscamoflage" with full definition, etymology, related forms, usage examples, and synonyms for the act of pretending to understand something to avoid looking uninformed.

**Files:**
- `prompt.md` — the user prompt
- `neologism-output.md` — invented word with definition, etymology, and usage examples

---

### PerspectivesPonderer

A comprehensive pros-and-cons analysis of implementing a four-day workweek as a standard corporate practice, covering productivity, well-being, costs, equity, and regulatory considerations.

**Files:**
- `prompt.md` — the user prompt
- `four-day-workweek-analysis.md` — multi-perspective analysis of the four-day workweek

---

### PiiPurifier

A redacted version of a conversation where all personally identifiable information (names and address) has been replaced with XXX.

**Files:**
- `prompt.md` — the system + user prompt
- `redacted-conversation.md` — PII-redacted conversation text

---

### PortmanteauPoet

Demonstrates Claude as a creative portmanteau generator. Given the words "music" and "therapy," Claude produces a curated collection of innovative word blends — from "Musitherapy" to "Rhythmedy" — each with pronunciation guides, etymological breakdowns, and context suggestions for when to use them.

**Files:**
- `prompt.md` — the system + user prompt
- `portmanteaus.md` — the generated portmanteau options

---

### ProsePolisher

A detailed copyediting analysis of a short narrative passage about Jane's walk in nature, with specific suggestions for grammar, word choice, tone, and flow, plus a fully rewritten version.

**Files:**
- `prompt.md` — the system + user prompt
- `prose-polishing-analysis.md` — copyediting analysis with rewritten prose

---

### PunDit

Demonstrates Claude as a pun and wordplay generator. Given the topic "Fishing," Claude produces a categorized collection of original fish-themed puns, plays on words, and humorous phrases — from "reel talk" to "o-fish-ally on vacation" — organized into themed sections with witty commentary.

**Files:**
- `prompt.md` — the system + user prompt
- `puns.md` — the generated puns and wordplay

---

### SecondGradeSimplifier

A simplified explanation of mitochondria and ATP rewritten for grades 3–5 readers using kid-friendly analogies.

**Files:**
- `prompt.md` — the system + user prompt
- `simplified-explanation.md` — mitochondria explained for kids with battery and power plant analogies

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

### TriviaGenerator

A collection of 10 challenging trivia questions across diverse categories with three progressive hints each.

**Files:**
- `prompt.md` — the user prompt
- `trivia-questions.md` — 10 trivia questions with progressive hints and answers

---

### StorytellingSidekick

Demonstrates Claude as a collaborative storytelling partner. Given a premise about a young woman named Lila who discovers she can control the weather, Claude builds an engaging multi-chapter narrative with vivid characters, plot twists, and interactive story direction options for the reader to shape what happens next.

**Files:**
- `prompt.md` — the system + user prompt
- `story.md` — the generated collaborative story

---

### VrFitnessInnovator

A list of 12 innovative VR fitness game concepts spanning diverse genres, each with descriptions, key features, and fitness benefits.

**Files:**
- `prompt.md` — the user prompt
- `vr-fitness-game-ideas.md` — 12 VR fitness game concepts with features and fitness aspects

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
