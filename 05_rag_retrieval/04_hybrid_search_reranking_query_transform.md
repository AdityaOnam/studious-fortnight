---
domain: rag
topic: hybrid_search_reranking_query_transform
title: Hybrid search, reranking, query transformation
tags: [hybrid-search, reranking, bm25, hyde]
count: 164
---
# Hybrid search, reranking, query transformation

## BM25, sparse and dense retrieval
- [RAG04-001] What are the common retrieval approaches used in RAG systems, and how do they differ?
- [RAG04-002] Why does a RAG system need very high-quality search?
- [RAG04-003] Explain how keyword-based retrieval works and what an inverted index provides.
- [RAG04-004] What does BM25 compute? Walk through the moving parts of the formula.
- [RAG04-005] Why does BM25 saturate term frequency and normalize by document length, and what would go wrong without those two terms?
- [RAG04-006] Why does BM25 still matter next to dense embeddings, and why does it remain a strong baseline?
- [RAG04-007] Why does BM25 need no training while a dense retriever does?
- [RAG04-008] How would you tune k1 and b in BM25 for a corpus of very short documents like support ticket titles?
- [RAG04-009] How do tokenization, stemming, and stopword handling change BM25 results, for example on code, product SKUs, or non-English text?
- [RAG04-010] How does multi-tenant keyword scoring distort BM25 statistics such as IDF, and how do you avoid it?
- [RAG04-011] How do sparse embeddings differ from dense embeddings in keyword matching and interpretability?
- [RAG04-012] Why are sparse text representations often cheaper to store and search than dense embeddings?
- [RAG04-013] How do sparse vectors (BM25, SPLADE) differ from dense embedding vectors, and when should you use each?
- [RAG04-014] What is the vocabulary mismatch problem, and which retriever families address it?
- [RAG04-015] When does BM25 beat dense embeddings on enterprise data, and how would you combine them?
- [RAG04-016] Give a query distribution where you would weight BM25 above dense retrieval.
- [RAG04-017] Your enterprise RAG assistant retrieves well on conceptual questions but fails on exact error codes and SKU IDs. What is the fix?
- [RAG04-018] Why do dense retrievers struggle with rare entities, identifiers, and out-of-domain jargon?
- [RAG04-019] What is learned sparse retrieval (SPLADE-style), and when would you pick it over BM25 or a dense retriever?
- [RAG04-020] SPLADE's term expansion lengthens postings lists. What would you tune to keep query latency acceptable?
- [RAG04-021] Would you fuse SPLADE with dense retrieval, or does the expansion make dense retrieval redundant?

## Hybrid search
- [RAG04-022] What is hybrid search, and how does it work in RAG retrieval?
- [RAG04-023] Why is hybrid search better than pure vector search, and why does pure vector search fail on some queries?
- [RAG04-024] When would you use hybrid search instead of pure dense or semantic search?
- [RAG04-025] When is hybrid retrieval unnecessary? Queries are paraphrased natural language over a small clean FAQ and a teammate wants to add BM25 and RRF.
- [RAG04-026] Why do production systems fuse BM25 and dense retrieval and then run a cross-encoder, instead of doing one bigger vector search?
- [RAG04-027] Walk me through hybrid retrieval: keyword, vector, and reranking. When does each stage earn its cost?
- [RAG04-028] You turned on hybrid search, but searches for part numbers like "ACME-X200" still miss although the docs contain them. What is the likely cause?
- [RAG04-029] What problems do chunking strategy, metadata, hybrid search, query rewriting, and reranking each solve in RAG retrieval, and when does each help?
- [RAG04-030] What are the main architecture patterns for retrieval and semantic search in LLM systems?
- [RAG04-031] How do you achieve efficient and accurate search over large-scale corpora?
- [RAG04-032] What techniques can improve retrieval, and how do you improve recall when retrieval results look irrelevant?
- [RAG04-033] Should BM25 and the ANN search run in parallel or sequentially in hybrid search, and how does that affect latency?
- [RAG04-034] How would you show that hybrid search actually beats dense-only retrieval on your own data?
- [RAG04-035] Would you run hybrid search inside one engine (Elasticsearch, OpenSearch, pgvector) or across separate systems? What are the tradeoffs?
- [RAG04-036] Where do document ACL filters go in a hybrid retrieval pipeline, and what do they do to recall?
- [RAG04-037] How do you balance dense versus sparse weight in hybrid search, including query-adaptive weights?
- [RAG04-038] How do you tune the lexical/dense balance in hybrid search per tenant without per-tenant training data?

## Fusion and merging ranked lists
- [RAG04-039] If you have results from several retrievers, how would you merge them into a single homogeneous ranking?
- [RAG04-040] How does reciprocal rank fusion work, and why fuse by rank instead of by score?
- [RAG04-041] Why is score-based fusion between BM25 and cosine similarity problematic, and why is RRF safer than adding raw scores?
- [RAG04-042] What does the constant k in RRF control, and what changes if it is very small or very large?
- [RAG04-043] If a document appears only in the dense result list, what is its ceiling in the fused RRF ranking?
- [RAG04-044] When would weighted fusion beat RRF, and what data do you need to tune it?
- [RAG04-045] A teammate wants to replace RRF with a tuned weighted fusion (alpha*bm25 + (1-alpha)*dense) for a few NDCG points. What is the senior caveat?
- [RAG04-046] If you normalize scores (min-max, z-score) before weighted fusion, what failure modes appear?
- [RAG04-047] How many results should you pull from each retriever before fusing, and how would you choose?
- [RAG04-048] How does reciprocal rank fusion interact with multi-query expansion?
- [RAG04-049] When merging ranked results from N shards whose scores are not comparable (different BM25 statistics), how do you merge them?
- [RAG04-050] When merging ranked results from N shards, how does the approach change with pagination, for example fetching results 90-100?
- [RAG04-051] How do you make relevance scores comparable when fusing results across different corpora?

## Cross-encoder reranking fundamentals
- [RAG04-052] What is re-ranking, and why add it after initial vector retrieval in RAG?
- [RAG04-053] How does re-ranking differ from the initial retrieval step?
- [RAG04-054] Explain the difference between a cross-encoder and a bi-encoder.
- [RAG04-055] Why is a cross-encoder fundamentally more accurate than a bi-encoder, and why is it used as the re-ranker?
- [RAG04-056] Why can't cross-encoders pre-compute text representations like bi-encoders can, and what does that mean for storage and serving?
- [RAG04-057] Why can't you run a cross-encoder for first-stage retrieval over a 10M-document corpus, or over the whole corpus?
- [RAG04-058] A RAG system retrieves 20 chunks but only 5 fit in the context window. How does skipping re-ranking hurt, and what does a re-ranker fix?
- [RAG04-059] Describe a scenario where BM25 returns relevant chunks in poor order. How does a neural re-ranker address that?
- [RAG04-060] What are the different types of re-ranker models used in RAG?
- [RAG04-061] Compare re-rankers against simply raising the similarity threshold in initial retrieval for reducing noise. When is each more appropriate?
- [RAG04-062] Recall@50 is poor because the gold chunk is often never retrieved, and a teammate adds a cross-encoder reranker. Will it help?
- [RAG04-063] Recall@20 is healthy, answers are vague, and precision@5 is 0.55. What is the best first move?
- [RAG04-064] The correct document enters the candidate pool but always ranks outside the top K. Should you adjust recall or add reranking?
- [RAG04-065] How are reranking models trained, and how do you fine-tune one for a new domain?
- [RAG04-066] How do you mine hard negatives when training a reranker, and what goes wrong with false negatives?
- [RAG04-067] Why not fine-tune the bi-encoder instead of adding a reranker?
- [RAG04-068] You have an embedding model and a reranker. Design the two-stage retrieval pipeline and explain when the reranker earns its latency.

## Reranker latency, depth, and tuning
- [RAG04-069] What challenges do re-rankers face in computational overhead and latency?
- [RAG04-070] How do you choose a reranking model, tune it, and decide whether a cross-encoder cost is worth it?
- [RAG04-071] How do you decide how many candidates to rerank, and how would you pick candidate depth (top-100 vs top-1000) empirically?
- [RAG04-072] Your reranker adds 250ms of latency and the product manager objects. What are your options?
- [RAG04-073] Your cross-encoder adds 150 ms at p95. When is that worth it, and when do you distill it into the bi-encoder?
- [RAG04-074] When would you skip reranking altogether?
- [RAG04-075] If your system serves both simple factual queries and complex analytical questions, how do you decide when to bypass the re-ranker?
- [RAG04-076] What breaks when documents exceed the reranker's maximum sequence length, and how do you handle it?
- [RAG04-077] How do you handle reranking for extremely long queries, such as a whole pasted paragraph?
- [RAG04-078] How would you pick a relevance cutoff for a "no good answer found" path?
- [RAG04-079] Your reranker improves offline NDCG but end-to-end answer quality does not move in production. What could explain it?
- [RAG04-080] You retrieved 50 candidate passages but the model's useful context budget is about 10. How do you choose, and how do you know the choices are good?
- [RAG04-081] How should you order reranked chunks in the prompt, given that models attend unevenly across long contexts?
- [RAG04-082] What roles do ranking and post-processing play in RAG, such as reranking, filtering, deduplication, and context compression?
- [RAG04-083] How do you diversify results after reranking and apply business rules without hurting relevance?

## Late interaction and LLM rerankers
- [RAG04-084] Explain the intuition behind multi-vector dense representations.
- [RAG04-085] What is ColBERT, and how does late-interaction retrieval with MaxSim scoring work?
- [RAG04-086] Where does ColBERT-style late interaction fit between bi-encoders and cross-encoder rerankers?
- [RAG04-087] Explain the difference between bi-encoders, cross-encoders, and late-interaction models. When would you choose each?
- [RAG04-088] When would you use ColBERT over a bi-encoder?
- [RAG04-089] Why is ColBERT's MaxSim more robust to document length than single-vector pooling?
- [RAG04-090] ColBERT stores one vector per token. How does it scale, and what are the storage tradeoffs?
- [RAG04-091] Estimate storage for 10M chunks under bi-encoder, cross-encoder, and ColBERT architectures. Where does a listwise LLM reranker fit?
- [RAG04-092] What do ColBERTv2 and PLAID change about index size and speed?
- [RAG04-093] How do ColPali and ColQwen differ from text-based late-interaction retrieval?
- [RAG04-094] For a legal search system with 5M documents, choose between dense bi-encoder plus cross-encoder reranker, ColBERT, and hybrid with reranking.
- [RAG04-095] Compare reranker architectures: cross-encoder, ColBERT, and LLM-based rerankers.
- [RAG04-096] Why not just ask an LLM to judge relevance instead of using embeddings?
- [RAG04-097] When would you use LLM-based reranking, and how do pointwise, pairwise, and listwise approaches differ?
- [RAG04-098] How do you choose between an LLM reranker and a dedicated reranker?
- [RAG04-099] How would you measure position bias in a listwise LLM reranker on your own data?
- [RAG04-100] How many labelled pairs do you need to distill an LLM reranker into a cross-encoder, and how do you check the student did not inherit the teacher's biases?

## Query transformation
- [RAG04-101] What is the difference between query rewriting and query expansion?
- [RAG04-102] What query transformation techniques exist (rewriting, expansion, multi-query, HyDE, step-back, decomposition), and when does each help?
- [RAG04-103] What are the pros and cons of query transformation techniques in RAG?
- [RAG04-104] How do you handle ambiguous or vague user queries in RAG?
- [RAG04-105] Your semantic search fails for short queries. How do you improve it?
- [RAG04-106] What is step-back prompting, and for which kinds of questions does it improve retrieval?
- [RAG04-107] How do you do LLM query expansion without causing query drift away from the user's intent?
- [RAG04-108] What is HyDE (Hypothetical Document Embeddings), how does it work, and when does it outperform standard dense retrieval?
- [RAG04-109] Why is HyDE risky for some applications, and when does it hurt?
- [RAG04-110] A grounded factual QA system over clean internal docs already has good recall, and a teammate proposes HyDE. What is the best call?
- [RAG04-111] What is RAG-Fusion, what problem of traditional RAG does it solve, and how are rewritten queries and results fused?
- [RAG04-112] In multi-query retrieval, how many query variants should you generate, and how do you deduplicate and rank the combined results?
- [RAG04-113] How does query decomposition help with multi-part questions?
- [RAG04-114] How would you implement query understanding and decomposition to split a complex query into sub-queries and recombine the results?
- [RAG04-115] How would you implement sub-question decomposition in RAG, and when does it make things worse?
- [RAG04-116] How would you decide cheaply, at query time, whether a question needs decomposition?
- [RAG04-117] How do you keep the final synthesis answering the original question rather than the sub-questions?
- [RAG04-118] What is contextual retrieval, and why does contextual BM25 matter and not only contextual embeddings?
- [RAG04-119] How does contextual retrieval compare to HyDE for improving retrieval quality?
- [RAG04-120] How do you handle retrieval in a multi-turn conversation?
- [RAG04-121] What goes wrong in multi-turn retrieval when the user abruptly changes topic?
- [RAG04-122] How do you measure whether query rewriting is actually helping retrieval?
- [RAG04-123] How do you evaluate query rewriting offline, and what does the golden set look like for multi-turn conversations?
- [RAG04-124] How would you keep total pre-retrieval latency under 300ms while using query rewriting, HyDE, and similar techniques?

## Routing, filtering, diversity, and special cases
- [RAG04-125] What is the role of metadata filtering in RAG systems?
- [RAG04-126] What is the difference between pre-filtering and post-filtering with metadata in vector search, and how does each affect recall?
- [RAG04-127] How does self-querying work, where an LLM turns a natural-language question into metadata filters, and how can it fail?
- [RAG04-128] A metadata filter is too restrictive and returns no results. How do you design a fallback?
- [RAG04-129] How do you add metadata filters and recency weighting to ranking in enterprise search?
- [RAG04-130] How do you handle time in retrieval: "latest" queries, superseded documents, and questions about the past?
- [RAG04-131] How would you pick the time-decay constant tau for a corpus rather than guessing?
- [RAG04-132] A user asks "what is our parental leave policy" and three versions of the document exist. What should the retriever return?
- [RAG04-133] How do you balance relevance and diversity when retrieving document chunks for RAG?
- [RAG04-134] How would you pick the MMR lambda without hand-tuning it on intuition?
- [RAG04-135] When is returning duplicate content actually the right behaviour in retrieval?
- [RAG04-136] Your product has several distinct corpora (docs, tickets, code, CRM). How do you route queries?
- [RAG04-137] How would you implement a query router: rules, embedding similarity, or an LLM classifier? What are the tradeoffs?
- [RAG04-138] How do you build the evaluation set for query routing, and what accuracy is acceptable?
- [RAG04-139] When would you route a numeric question to text-to-SQL instead of RAG, and how do you decide which path a query takes?
- [RAG04-140] Your corpus is multilingual and users query in several languages. What breaks, and how do you fix it?
- [RAG04-141] In multilingual retrieval, why translate the query rather than the corpus, and when would you flip that decision?
- [RAG04-142] How do you keep entity names, such as scheme or place names, from being mangled across scripts in cross-lingual RAG?
- [RAG04-143] How would you evaluate code retrieval, given that the relevant result is often a set of files rather than one chunk?

## Retrieval metrics and evaluation
- [RAG04-144] What are the key metrics for evaluating retrieval quality in RAG?
- [RAG04-145] Which retrieval metrics (recall@k, MRR, nDCG) would you track, what does each tell you, and when does each matter?
- [RAG04-146] Explain the difference between Precision@k and Recall@k in RAG. When might you prefer one?
- [RAG04-147] Why does recall@k matter more than precision@k for RAG specifically?
- [RAG04-148] What is the difference between hit rate and recall@k?
- [RAG04-149] Suppose your retriever gets perfect Recall@10 but low Precision@10. What problems could this cause for the generator?
- [RAG04-150] Why is MRR unsuitable when there are multiple relevant chunks per query, and how does MAP address this?
- [RAG04-151] How do you calculate MAP@5 for a retrieval result, and what does MAP reveal that raw precision does not?
- [RAG04-152] Compute MRR for three queries whose first relevant result appears at rank 1, rank 3, and not at all.
- [RAG04-153] When is nDCG more informative than MAP, and how do binary versus graded relevance labels change the choice?
- [RAG04-154] How would NDCG@k change if all relevant chunks are retrieved but in reverse order (least to most relevant)?
- [RAG04-155] Explain the most common metric used in information retrieval and when it fails.
- [RAG04-156] For a Quora-like question-answering system that should surface the most pertinent answers quickly, which evaluation metric would you choose?
- [RAG04-157] How would you evaluate the effectiveness of a reranker? Which of MRR, MAP, and NDCG would you prioritize and why?
- [RAG04-158] How do you build a labeled golden set for retrieval when you have no annotators, using synthetic queries or LLM judges?
- [RAG04-159] Retrieval metrics improved after a change but end-to-end answer quality did not. Why might that happen?
- [RAG04-160] How would you detect retrieval regressions after swapping the embedding model or the chunking strategy?

## Additional questions
- [RAG04-161] To minimize RAG system latency, which pre-retrieval enhancement technique would you choose?
- [RAG04-162] When training a code-retrieval component for an agent with a retrieval reward, why weight precision over recall?
- [RAG04-163] In multilingual retrieval evals, reranking helps Korean-query-to-English-document retrieval much more than English-to-English. Why might that be?
- [RAG04-164] How would you combine keyword and vector retrieval and merge their ranked lists?
