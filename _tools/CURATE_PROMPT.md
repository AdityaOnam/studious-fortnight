# Task: curate ONE topic file of an interview-QUESTIONS-ONLY corpus (for RAG)

We are building small, topic-specific markdown files that contain ONLY interview questions (no answers) on ML, AI/LLM, system design and CS fundamentals. You curate the file for one topic KEY.

## Inputs
- Your KEY and its title/scope: find your KEY's line in `D:\COURSE\ITW_QUES\_tools\taxonomy_brief.txt` (format `KEY | title | scope`). That scope defines what belongs in the file. Neighbouring keys cover other topics — do not duplicate their territory.
- Pool of candidate questions: `D:\COURSE\ITW_QUES\_work\pools\<KEY>.tsv`, lines `ref<TAB>D<TAB>question` (D = E/M/H difficulty). Refs are `Qxxxxxx` (harvested) or `Dnnnnn` (derived from notes). Read the whole file.

## What to do
1. **Dedupe**: merge duplicate / near-duplicate questions (same underlying question, different wording) into ONE best-phrased question and keep ALL merged refs. Questions that are related but test different things stay separate.
2. **Quality pass**: fix wording; each question must be self-contained, one clear question, ≤ 220 characters, natural interview phrasing, no markdown noise, NO answers/hints/explanations. Drop junk: non-questions, fragments, vague questions ("Explain it"), trivia irrelevant to this KEY's scope, DSA/LeetCode puzzles, HR/behavioural, vendor-specific trivia. If a question clearly belongs to another KEY, still keep it only if it also fits this scope; otherwise drop it.
3. **Organise**: group into 3–10 `##` sections by sub-topic (section titles short and specific, e.g. `## Chunk size and overlap`). Max 25 questions per section. Order sections fundamentals → advanced and questions inside a section easier → harder. Prefer sub-topic clarity over strict size equality.
4. **Gap-fill**: compare against the KEY's scope and your knowledge of real interviews (FAANG/AI labs/top product companies). Add new high-quality questions for important sub-topics the pool misses — tradeoff questions, "why" questions, failure-mode / debugging scenarios, comparisons, numeric/estimation questions where relevant, and (for design keys) concrete prompts. Mark them with ref `GEN`. Rules: no padding with weak filler; generated questions should usually be ≤ 35% of the file unless the pool is very thin. Target total after dedupe+gap-fill: roughly 70–150 questions per file (CODE01: 40+; thin niche keys may be lower but should be at least ~45).
5. **Split if large**: if more than 170 questions remain, split the file at section boundaries into parts (each ≈ 80–150 questions) — write `<KEY>.p1.md`, `<KEY>.p2.md`, … instead of one file; give each part its own sections.

## Output format (STRICT — a script parses it)
Write with the Write tool to `D:\COURSE\ITW_QUES\_work\curated\<KEY>.md` (or `<KEY>.p1.md`, `<KEY>.p2.md`, …). Content is ONLY section headings and question lines, no front-matter, no title, no commentary:

```
## Section title
- [M] The question text, one line? {Q000123,D00044}
- [H] Another question? {Q000456}
- [E] A question you wrote yourself? {GEN}
```
- `[E]`, `[M]` or `[H]` difficulty tag first; question text; then refs in `{}` comma-separated (all merged refs; `GEN` for your own).
- Every pool ref should appear in some `{}` OR be intentionally dropped; also write the dropped refs to `D:\COURSE\ITW_QUES\_work\curated\<KEY>.dropped.txt` as one line `ref<TAB>reason` each (reasons: `dup-merged` need not be listed; list only real drops: `junk`, `offscope`, `dsa`, `hr`, `vague`).

When finished, reply with ONE short line: `KEY: N questions in M sections (G generated), dropped D`. No other commentary.
