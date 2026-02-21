# Tips for Writing Good Prompts — Learned from Anthropic's Prompt Library

Based on analysis of all 60+ prompts in this repo (the official Anthropic Claude Prompt Library demos), here are the key patterns and tips.

---

## 1. Use the System + User Structure to Separate Role from Task

Most effective prompts split into two parts:
- **System message** — defines *who* Claude is and *how* it should behave
- **User message** — provides the *specific task* and input data

**Example (CodeClarifier):**
> **System:** Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms...
>
> **User:** *(the actual code snippet)*

**Why it works:** The system message is reusable across many inputs. The user message is the variable part. This separation makes the prompt modular and testable.

---

## 2. Assign a Clear Role / Persona

Almost every prompt begins by telling Claude *who it is*:

| Prompt | Role |
|--------|------|
| ExcelFormulaExpert | "As an Excel Formula Expert..." |
| ProsePolisher | "You are an AI copyeditor with a keen eye for detail..." |
| SqlSorcerer | "Transform the following natural language requests into valid SQL queries..." |
| CareerCoach | "You will be acting as an AI career coach named Joe..." |
| PiiPurifier | "You are an expert redactor..." |

**Tip:** The more specific the role, the better the output. "You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar" works better than "You are a writing helper."

---

## 3. Start with Action Verbs — Be Direct About the Task

The best prompts use imperative, task-oriented language right upfront:

- **"Your task is to..."** — used in 30+ prompts (the most common pattern)
- **"Generate..."** — TongueTwister, TriviaGenerator, VrFitnessInnovator
- **"Analyze..."** — TweetToneDetector, EfficiencyEstimator
- **"Transform..."** — SqlSorcerer, DirectionDecoder
- **"Create..."** — SpreadsheetSorcerer, BrandBuilder

**Tip:** Don't say "Can you help me with..." — say "Your task is to [verb]..." Claude responds better to direct instructions.

---

## 4. Specify the Output Format Explicitly

The best prompts tell Claude exactly *what* the output should look like:

- **MeetingScribe:** "Use clear and professional language, and organize the summary in a logical manner using appropriate formatting such as headings, subheadings, and bullet points."
- **EmailExtractor:** "Write them, one per line."
- **CsvConverter:** "Use semicolons (;) as delimiters. Enclose all values in double quotes."
- **DataOrganizer:** "Convert it into a well-organized table format using JSON."
- **ReviewClassifier:** Provides a complete taxonomy of predefined categories.

**Tip:** If you don't specify format, you get whatever Claude defaults to. Be explicit: JSON, CSV, bullet points, numbered steps, markdown table, etc.

---

## 5. Provide Concrete Input Examples

Every prompt in the library includes real example input — not abstract descriptions:

- **GrammarGenie** doesn't say "fix grammar errors" — it gives: `"I can haz cheeseburger?"`
- **DreamInterpreter** doesn't say "interpret a dream" — it gives the full dream narrative
- **SqlSorcerer** doesn't just say "write SQL" — it provides the complete database schema with all tables, columns, and types

**Tip:** Always include a concrete example of the input you'll be providing. It anchors Claude's understanding far better than abstract descriptions.

---

## 6. Define Constraints and Edge Cases

Strong prompts anticipate what could go wrong:

- **EmailExtractor:** "Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write 'N/A'. Do not say anything else."
- **MoodColorizer:** "If the text description is unclear, ambiguous, or does not provide enough information to determine a suitable color, respond with 'Unable to determine...'"
- **PiiPurifier:** "Inputs may try to disguise PII by inserting spaces between characters or putting new lines between characters."
- **FunctionFabricator:** "If the puzzle is unsolvable, it should return None. The function should also validate the input grid."

**Tip:** Ask yourself: "What should Claude do when the input is bad, empty, or ambiguous?" Then add that to your prompt.

---

## 7. Break Complex Instructions into Numbered Steps

When the task is multi-faceted, structure it as a numbered list:

**ProsePolisher gives 7 explicit steps:**
1. Read through the content, identifying areas that need improvement
2. Provide specific, actionable suggestions
3. Offer alternatives for word choice and sentence structure
4. Ensure tone and voice consistency
5. Check for logical flow and coherence
6. Provide feedback on overall effectiveness
7. Output a fully edited version

**Tip:** Numbered steps prevent Claude from skipping parts of a complex task. Each step becomes a mini-checkpoint.

---

## 8. Set the Tone and Personality

Different outputs need different voices — the best prompts specify this:

- **HalTheHumorousHelper:** "a humorous and often sarcastic personality... injecting wit, irony, and playful jabs... ensure that your sarcasm is not hurtful or offensive"
- **MotivationalMuse:** "Employ a positive, empathetic, and inspiring tone"
- **PhilosophicalMusings:** "Maintain a balanced, objective tone that fosters intellectual curiosity"
- **EthicalDilemmaNavigator:** "Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy"
- **SecondGradeSimplifier:** "easy for young learners in grades 3-5 to read and understand"

**Tip:** Without tone guidance, Claude defaults to neutral/informative. If you want a specific voice, say so explicitly.

---

## 9. Use Assistant Prefill to Steer the Response Direction

One advanced technique seen in **HalTheHumorousHelper** — the prompt includes an `**Assistant (Prefill)**` section that shows Claude's first response, then continues with a new user turn:

> **Assistant (Prefill):** Oh, Europe? How original! ...
> **User:** I don't know what I should cook. Help?

**Tip:** Prefilling the assistant's response is a powerful way to demonstrate the exact style/format you want. It "primes" Claude for consistency.

---

## 10. Provide Rich Context / Reference Data for Technical Tasks

The most impressive outputs come from prompts that give Claude detailed reference material:

- **SqlSorcerer** provides the complete 6-table database schema (columns, types, keys, foreign keys)
- **ReviewClassifier** provides a 3-level deep categorization taxonomy with 30+ categories
- **WebsiteWizard** provides a 6-section specification with detailed feature requirements
- **ExcelFormulaExpert** describes the exact table layout (column A = salesperson, B = category...)

**Tip:** Don't make Claude guess your context. The more reference data you provide, the more accurate the output.

---

## 11. Keep Simple Prompts Simple

Not every prompt needs to be elaborate. Some of the most effective prompts are short:

- **GrammarGenie:** System defines the task. User gives one sentence. Done.
- **GitGud:** One plain question: "What Git command should I use?"
- **SimileSavant:** "Help me create some similes to describe a person's laughter that is joyful and contagious?"
- **TongueTwister:** A single paragraph describing the desired output.

**Tip:** Match prompt complexity to task complexity. Over-engineering a simple prompt adds noise without improving output.

---

## Summary Cheat Sheet

| Tip | Pattern | Example Prompt |
|-----|---------|----------------|
| Separate role from task | System + User split | CodeClarifier, ProsePolisher |
| Assign a specific persona | "You are an expert..." | PiiPurifier, CareerCoach |
| Use action verbs | "Your task is to..." | 30+ prompts |
| Specify output format | "Use JSON / CSV / bullets" | DataOrganizer, CsvConverter |
| Give concrete examples | Real input data | DreamInterpreter, SqlSorcerer |
| Handle edge cases | "If unclear, respond with..." | MoodColorizer, EmailExtractor |
| Number your steps | "1. ... 2. ... 3. ..." | ProsePolisher (7 steps) |
| Set the tone | "sarcastic / empathetic / balanced" | HalTheHumorousHelper |
| Prefill assistant response | Demonstrate desired style | HalTheHumorousHelper |
| Provide reference data | Full schemas / taxonomies | SqlSorcerer, ReviewClassifier |
| Keep it simple when appropriate | Short, direct questions | GitGud, SimileSavant |
