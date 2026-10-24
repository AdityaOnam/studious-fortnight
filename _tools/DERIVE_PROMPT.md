# Task: derive interview QUESTIONS from note-style repos (questions only, no answers)

We are building a questions-only interview-prep corpus (ML, AI/LLM, system design, CS fundamentals) for a RAG store.
Some GitHub repos are study NOTES, not question lists. You turn their topic structure into good interview questions.

## Inputs
- Outline file(s): headings per file of the cloned repo, in `D:\COURSE\ITW_QUES\_work\outlines\<repo>.md`. Each `## FILE <path>` is a file in `D:\COURSE\ITW_QUES\_raw\<repo>\<path>`; `-` bullets are its headings.
- Target topics: `D:\COURSE\ITW_QUES\_tools\taxonomy_brief.txt` (use ONLY those KEYs).
- You may open the actual source files (Read) when a heading is cryptic or the file is rich enough that you want to see which concepts it covers. Don't read everything; prioritise the files that match your assigned scope.

## What to produce
For each meaningful technical concept covered, write 1–3 interview-style questions a strong interviewer would ask: definition/why, how it works internally, compare/contrast, trade-offs, failure modes, scenario-based ("what happens when…", "how would you debug…"), and for system-design material concrete "Design X" prompts. Vary the types. Prefer the question styles used in real interviews at big tech.
Targets: quality over volume, but cover the whole assigned scope — typically 250–600 questions for your assignment.

## Rules
- QUESTIONS ONLY. No answers, hints, or parenthetical explanations.
- English, self-contained, one question per line, natural interview phrasing. No references to "the article", "this repo", "the document".
- Do not copy sentences from the notes; write fresh questions. Keep each ≤ 220 characters.
- Skip: vendor/framework trivia not transferable (Spring annotations, MyBatis, Netty, Chinese-cloud specifics, WeChat, Alibaba tool names), DSA/LeetCode problems, HR/behavioural, pure book/course/resource lists, repo meta (contributing, about-author, roadmap, ads).
- Java-specific content: keep only when the concept is general (concurrency, memory model, GC concepts, hash-map internals, JVM basics) and phrase it so it stands alone.
- Assign each question exactly one target KEY from the taxonomy brief (best fit by scope) and difficulty `E` (recall), `M` (understanding/tradeoffs), `H` (deep/open-ended/design).
- Avoid near-duplicate questions within your output.

## Output
Write ONE TSV file with the Write tool (path given in your task), one line per question, no header:
`KEY<TAB>D<TAB>question<TAB>source` where source = `<repo>:<file path or topic heading>` (short).
You may write the file in several chunks: write the first part, then append more by re-reading and re-writing the full file content (or write `_partN.tsv` files — then also list them in your final reply).

When done, reply with ONE short line: `N questions written to <path(s)>`. No other commentary.
