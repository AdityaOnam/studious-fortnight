# Task: clean + classify interview questions (questions only)

You are helping build a questions-only interview-prep corpus (ML, AI/LLM, system design, CS fundamentals) for a RAG store.
You get ONE batch file of raw candidate lines harvested from GitHub interview repos. Many are noise. Your job: for EVERY input line, either DROP it or output a cleaned question assigned to exactly one target topic file.

## Input
A TSV file, one candidate per line: `ID<TAB>raw text<TAB>[source-repo|nearest heading]`.
The bracket part is context only (helps you decide the topic); never copy it into the question.

## Target topics
Read `D:\COURSE\ITW_QUES\_tools\taxonomy_brief.txt` first. Use ONLY the KEYs listed there (e.g. RAG03, SD02, CS04). Pick the single best fit by reading each KEY's scope text. If a question is clearly relevant to the interview domains but fits no key well, choose the closest key.

## KEEP (and clean) when the line is
- a genuine interview question / prompt on: classical ML, statistics & probability for DS, deep learning, NLP, CV, LLMs/transformers, fine-tuning/alignment, RAG/retrieval, agents/GenAI apps, MLOps, ML/GenAI/system design (HLD and LLD "Design X" prompts), OS, networks, DBMS/SQL, NoSQL, OOP, design patterns, concurrency, security basics, Git/Docker/Linux/DevOps basics, Python/Java/C++ language-internals concept questions;
- an "implement X from scratch" ML/LLM coding task (key CODE01), e.g. "Implement multi-head attention in PyTorch". Keep only the task title as a question.

## DROP when the line is
- not a question/prompt (table-of-contents entry, section title like "Overview", sentence from an answer, rhetorical question inside an explanation, instructions, marketing, link text);
- a pure DSA/LeetCode algorithm problem ("reverse a linked list", "two-sum") — out of scope;
- behavioural/HR ("tell me about a time...", salary), career advice;
- frontend/web-framework/mobile specifics (React, Angular, CSS, Spring annotations, Android...), or niche vendor/product trivia that is not a transferable concept;
- unintelligible or impossible to repair into a standalone question;
- an exact or near duplicate of another line IN THIS BATCH (keep the best-phrased one, drop the other with reason `dup`).

## CLEAN rules for kept lines
1. Self-contained: no "above", "this", "the following", "the given code", "in the article" unless you can repair it by adding the missing context from the heading/source tag. If it can't be repaired, DROP it.
2. Keep the original meaning and wording as much as possible; fix grammar, remove markdown emphasis (`_x_`, `**x**`, backticks), numbering, emojis, "Q:" prefixes.
3. REMOVE any leaked answer / hint / explanation (e.g. "...? (Answer: X)", "...? Hint: ..."). Questions only.
4. If one line holds 2+ clearly separate questions, split into separate output lines using IDs with suffixes a, b, c (`Q000123a`, `Q000123b`). Do not split a question into trivial fragments.
5. Non-English input: translate to natural English interview phrasing.
6. Do not invent new questions. Do not add answers.
7. Difficulty D: `E` (basic definition/recall), `M` (needs understanding/tradeoffs), `H` (deep/advanced/design/open-ended). Judge from wording.

## Output
Write ONE file with the Write tool to the output path given in your task. TSV, one line per input ID (plus suffix lines), no header:
- kept: `ID<TAB>KEY<TAB>D<TAB>cleaned question`
- dropped: `ID<TAB>DROP<TAB>-<TAB>reason` where reason is one of: `notq`, `dsa`, `hr`, `frontend`, `unfixable`, `dup`, `offtopic`

Coverage rule: EVERY input ID must appear in your output at least once. Read the whole input file (use offset/limit if it is long). Work through it carefully; do not skim or stop early.

When done, reply with ONE short line: `kept N, dropped M, file written`. No other commentary.
