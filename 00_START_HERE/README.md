# ITW_QUES — interview questions corpus for RAG

Questions only, no answers, split into small topic files so retrieval stays precise and context stays small.

- `INDEX.md` — every file with question counts.
- `SOURCES.md` — where the questions came from (repos, stars, licences) and the licence caveat.
- `DAILY_SESSION_PROMPT.md` — ready-made system prompt for a daily mock-interview session.
- Domain folders `01_…` to `10_…` — the RAG files. **Only these ten folders should be ingested.**
- `_meta/` (provenance, difficulty, audit lists), `_raw/` (cloned sources), `_tools/` (scripts), `_work/` (intermediate data) are **not** for RAG — exclude them.

## File format
```md
---
domain: rag
topic: chunking_and_document_processing
title: Chunking and document processing
tags: [rag, chunking, parsing, ingestion]
count: 74
---
# Chunking and document processing
## Chunk size and overlap
- [RAG02-001] How do you choose chunk size and overlap …?
```
- One question per line, self-contained, stable ID `<TOPICKEY>-<number>`.
- Each `##` section holds ≤ 25 questions — a natural retrieval chunk. Large topics are split into `_part1`, `_part2`, … files (≈100 questions each).
- Difficulty (E/M/H), provenance and "generated vs harvested" live in `_meta/questions.jsonl`, keyed by the same ID.

## Ingesting into a RAG tool
- Chunk by markdown heading (`##`) — or just by file; every file is ≈ 3–6k tokens.
- Keep the YAML front-matter as metadata (`domain`, `topic`, `tags`) so you can filter ("only `domain: rag`").
- Put `DAILY_SESSION_PROMPT.md` in the system prompt / project instructions, not in the retrieval store.

## Using it daily
Start a chat, paste the daily prompt, say e.g. "45 minutes, focus RAG + system design, hard". Or "drill LoRA" / "mock design interview: rate limiter".
