## BM25, sparse and dense retrieval
- [E] What are the common retrieval approaches used in RAG systems, and how do they differ? {Q003433}
- [E] Why does a RAG system need very high-quality search? {Q007156}
- [E] Explain how keyword-based retrieval works and what an inverted index provides. {Q004315,Q007159,GEN}
- [E] What does BM25 compute? Walk through the moving parts of the formula. {Q007850}
- [M] Why does BM25 saturate term frequency and normalize by document length, and what would go wrong without those two terms? {GEN}
- [M] Why does BM25 still matter next to dense embeddings, and why does it remain a strong baseline? {D00390,D04844}
- [M] Why does BM25 need no training while a dense retriever does? {Q007852}
- [M] How would you tune k1 and b in BM25 for a corpus of very short documents like support ticket titles? {Q007851}
- [M] How do tokenization, stemming, and stopword handling change BM25 results, for example on code, product SKUs, or non-English text? {GEN}
- [M] How does multi-tenant keyword scoring distort BM25 statistics such as IDF, and how do you avoid it? {D00395}
- [M] How do sparse embeddings differ from dense embeddings in keyword matching and interpretability? {Q003443,Q004295}
- [M] Why are sparse text representations often cheaper to store and search than dense embeddings? {Q004296}
- [M] How do sparse vectors (BM25, SPLADE) differ from dense embedding vectors, and when should you use each? {Q006000,Q011815}
- [M] What is the vocabulary mismatch problem, and which retriever families address it? {GEN}
- [M] When does BM25 beat dense embeddings on enterprise data, and how would you combine them? {Q009570}
- [M] Give a query distribution where you would weight BM25 above dense retrieval. {Q007842}
- [M] Your enterprise RAG assistant retrieves well on conceptual questions but fails on exact error codes and SKU IDs. What is the fix? {Q007105,Q007033}
- [M] Why do dense retrievers struggle with rare entities, identifiers, and out-of-domain jargon? {GEN}
- [M] What is learned sparse retrieval (SPLADE-style), and when would you pick it over BM25 or a dense retriever? {Q007918,Q011375,D00393}
- [H] SPLADE's term expansion lengthens postings lists. What would you tune to keep query latency acceptable? {Q007919}
- [M] Would you fuse SPLADE with dense retrieval, or does the expansion make dense retrieval redundant? {Q007920}

## Hybrid search
- [E] What is hybrid search, and how does it work in RAG retrieval? {Q011160,Q003440,Q007165,Q007063}
- [E] Why is hybrid search better than pure vector search, and why does pure vector search fail on some queries? {Q004757,Q011067,Q007840}
- [M] When would you use hybrid search instead of pure dense or semantic search? {Q003441,Q011373,D00389,Q010815}
- [M] When is hybrid retrieval unnecessary? Queries are paraphrased natural language over a small clean FAQ and a teammate wants to add BM25 and RRF. {Q007038}
- [M] Why do production systems fuse BM25 and dense retrieval and then run a cross-encoder, instead of doing one bigger vector search? {Q007034}
- [M] Walk me through hybrid retrieval: keyword, vector, and reranking. When does each stage earn its cost? {Q009787}
- [M] You turned on hybrid search, but searches for part numbers like "ACME-X200" still miss although the docs contain them. What is the likely cause? {Q007035}
- [M] What problems do chunking strategy, metadata, hybrid search, query rewriting, and reranking each solve in RAG retrieval, and when does each help? {Q003603,D03815}
- [M] What are the main architecture patterns for retrieval and semantic search in LLM systems? {Q004311,Q007155}
- [H] How do you achieve efficient and accurate search over large-scale corpora? {Q004312,Q007157}
- [M] What techniques can improve retrieval, and how do you improve recall when retrieval results look irrelevant? {Q007168,D00410}
- [M] Should BM25 and the ANN search run in parallel or sequentially in hybrid search, and how does that affect latency? {GEN}
- [M] How would you show that hybrid search actually beats dense-only retrieval on your own data? {GEN}
- [H] Would you run hybrid search inside one engine (Elasticsearch, OpenSearch, pgvector) or across separate systems? What are the tradeoffs? {GEN}
- [H] Where do document ACL filters go in a hybrid retrieval pipeline, and what do they do to recall? {Q009789}
- [M] How do you balance dense versus sparse weight in hybrid search, including query-adaptive weights? {Q011376,D00392}
- [H] How do you tune the lexical/dense balance in hybrid search per tenant without per-tenant training data? {Q009572}

## Fusion and merging ranked lists
- [M] If you have results from several retrievers, how would you merge them into a single homogeneous ranking? {Q007166,Q004968}
- [M] How does reciprocal rank fusion work, and why fuse by rank instead of by score? {Q007890,Q005958,Q006190,Q003604}
- [M] Why is score-based fusion between BM25 and cosine similarity problematic, and why is RRF safer than adding raw scores? {Q009788,Q011374,D00391}
- [M] What does the constant k in RRF control, and what changes if it is very small or very large? {GEN}
- [M] If a document appears only in the dense result list, what is its ceiling in the fused RRF ranking? {Q007893}
- [M] When would weighted fusion beat RRF, and what data do you need to tune it? {Q007891}
- [M] A teammate wants to replace RRF with a tuned weighted fusion (alpha*bm25 + (1-alpha)*dense) for a few NDCG points. What is the senior caveat? {Q007036}
- [M] If you normalize scores (min-max, z-score) before weighted fusion, what failure modes appear? {GEN}
- [M] How many results should you pull from each retriever before fusing, and how would you choose? {GEN}
- [M] How does reciprocal rank fusion interact with multi-query expansion? {Q007892}
- [H] When merging ranked results from N shards whose scores are not comparable (different BM25 statistics), how do you merge them? {Q009591}
- [M] When merging ranked results from N shards, how does the approach change with pagination, for example fetching results 90-100? {Q009592}
- [M] How do you make relevance scores comparable when fusing results across different corpora? {Q007949}

## Cross-encoder reranking fundamentals
- [E] What is re-ranking, and why add it after initial vector retrieval in RAG? {Q011068,Q007843,Q003453,Q004758,Q007064}
- [M] How does re-ranking differ from the initial retrieval step? {Q003446}
- [E] Explain the difference between a cross-encoder and a bi-encoder. {Q004292}
- [M] Why is a cross-encoder fundamentally more accurate than a bi-encoder, and why is it used as the re-ranker? {Q011380,D00396,Q003448}
- [M] Why can't cross-encoders pre-compute text representations like bi-encoders can, and what does that mean for storage and serving? {Q003452}
- [M] Why can't you run a cross-encoder for first-stage retrieval over a 10M-document corpus, or over the whole corpus? {Q007829,Q007039,Q007363}
- [M] A RAG system retrieves 20 chunks but only 5 fit in the context window. How does skipping re-ranking hurt, and what does a re-ranker fix? {Q003449}
- [M] Describe a scenario where BM25 returns relevant chunks in poor order. How does a neural re-ranker address that? {Q003450}
- [M] What are the different types of re-ranker models used in RAG? {Q003447}
- [M] Compare re-rankers against simply raising the similarity threshold in initial retrieval for reducing noise. When is each more appropriate? {Q003456}
- [M] Recall@50 is poor because the gold chunk is often never retrieved, and a teammate adds a cross-encoder reranker. Will it help? {Q007042}
- [M] Recall@20 is healthy, answers are vague, and precision@5 is 0.55. What is the best first move? {Q007028}
- [M] The correct document enters the candidate pool but always ranks outside the top K. Should you adjust recall or add reranking? {Q003606}
- [M] How are reranking models trained, and how do you fine-tune one for a new domain? {Q004316,Q007160}
- [M] How do you mine hard negatives when training a reranker, and what goes wrong with false negatives? {GEN}
- [M] Why not fine-tune the bi-encoder instead of adding a reranker? {Q007845}
- [H] You have an embedding model and a reranker. Design the two-stage retrieval pipeline and explain when the reranker earns its latency. {Q009354}

## Reranker latency, depth, and tuning
- [M] What challenges do re-rankers face in computational overhead and latency? {Q003457}
- [M] How do you choose a reranking model, tune it, and decide whether a cross-encoder cost is worth it? {Q005957,Q006066,D00413,Q011816}
- [M] How do you decide how many candidates to rerank, and how would you pick candidate depth (top-100 vs top-1000) empirically? {Q011381,D00397,Q009355}
- [M] Your reranker adds 250ms of latency and the product manager objects. What are your options? {Q007844}
- [H] Your cross-encoder adds 150 ms at p95. When is that worth it, and when do you distill it into the bi-encoder? {Q009999}
- [M] When would you skip reranking altogether? {Q010818,D00400}
- [H] If your system serves both simple factual queries and complex analytical questions, how do you decide when to bypass the re-ranker? {Q003451}
- [M] What breaks when documents exceed the reranker's maximum sequence length, and how do you handle it? {Q009356}
- [H] How do you handle reranking for extremely long queries, such as a whole pasted paragraph? {Q011385,D00399}
- [M] How would you pick a relevance cutoff for a "no good answer found" path? {Q007849}
- [H] Your reranker improves offline NDCG but end-to-end answer quality does not move in production. What could explain it? {GEN}
- [H] You retrieved 50 candidate passages but the model's useful context budget is about 10. How do you choose, and how do you know the choices are good? {Q012086,Q009998,Q003442}
- [M] How should you order reranked chunks in the prompt, given that models attend unevenly across long contexts? {GEN}
- [M] What roles do ranking and post-processing play in RAG, such as reranking, filtering, deduplication, and context compression? {D04835}
- [H] How do you diversify results after reranking and apply business rules without hurting relevance? {D00412}

## Late interaction and LLM rerankers
- [M] Explain the intuition behind multi-vector dense representations. {Q004294}
- [H] What is ColBERT, and how does late-interaction retrieval with MaxSim scoring work? {Q004759,D00401}
- [M] Where does ColBERT-style late interaction fit between bi-encoders and cross-encoder rerankers? {Q007846}
- [M] Explain the difference between bi-encoders, cross-encoders, and late-interaction models. When would you choose each? {Q011415,Q007894}
- [M] When would you use ColBERT over a bi-encoder? {Q011222}
- [H] Why is ColBERT's MaxSim more robust to document length than single-vector pooling? {Q007895}
- [H] ColBERT stores one vector per token. How does it scale, and what are the storage tradeoffs? {Q011416,D00402}
- [H] Estimate storage for 10M chunks under bi-encoder, cross-encoder, and ColBERT architectures. Where does a listwise LLM reranker fit? {Q007896}
- [M] What do ColBERTv2 and PLAID change about index size and speed? {Q005995,D00404}
- [M] How do ColPali and ColQwen differ from text-based late-interaction retrieval? {D00405}
- [H] For a legal search system with 5M documents, choose between dense bi-encoder plus cross-encoder reranker, ColBERT, and hybrid with reranking. {Q011417,D00403}
- [H] Compare reranker architectures: cross-encoder, ColBERT, and LLM-based rerankers. {Q004760,Q012085}
- [M] Why not just ask an LLM to judge relevance instead of using embeddings? {Q011227}
- [M] When would you use LLM-based reranking, and how do pointwise, pairwise, and listwise approaches differ? {Q011384,D00398,Q007999}
- [M] How do you choose between an LLM reranker and a dedicated reranker? {Q003619}
- [H] How would you measure position bias in a listwise LLM reranker on your own data? {Q008000}
- [H] How many labelled pairs do you need to distill an LLM reranker into a cross-encoder, and how do you check the student did not inherit the teacher's biases? {Q008001}

## Query transformation
- [E] What is the difference between query rewriting and query expansion? {GEN}
- [M] What query transformation techniques exist (rewriting, expansion, multi-query, HyDE, step-back, decomposition), and when does each help? {Q003421,D04834,D00406,Q004773,Q007897}
- [M] What are the pros and cons of query transformation techniques in RAG? {Q003422}
- [M] How do you handle ambiguous or vague user queries in RAG? {Q003420}
- [M] Your semantic search fails for short queries. How do you improve it? {Q004895}
- [M] What is step-back prompting, and for which kinds of questions does it improve retrieval? {GEN}
- [M] How do you do LLM query expansion without causing query drift away from the user's intent? {GEN}
- [M] What is HyDE (Hypothetical Document Embeddings), how does it work, and when does it outperform standard dense retrieval? {Q006182,Q011818}
- [M] Why is HyDE risky for some applications, and when does it hurt? {Q011398,D00407,Q007899}
- [M] A grounded factual QA system over clean internal docs already has good recall, and a teammate proposes HyDE. What is the best call? {Q007043}
- [M] What is RAG-Fusion, what problem of traditional RAG does it solve, and how are rewritten queries and results fused? {Q006181,D00394}
- [M] In multi-query retrieval, how many query variants should you generate, and how do you deduplicate and rank the combined results? {GEN}
- [M] How does query decomposition help with multi-part questions? {D00408}
- [H] How would you implement query understanding and decomposition to split a complex query into sub-queries and recombine the results? {Q004313}
- [M] How would you implement sub-question decomposition in RAG, and when does it make things worse? {Q007915}
- [M] How would you decide cheaply, at query time, whether a question needs decomposition? {Q007916}
- [M] How do you keep the final synthesis answering the original question rather than the sub-questions? {Q007917}
- [M] What is contextual retrieval, and why does contextual BM25 matter and not only contextual embeddings? {Q011159,Q007866b}
- [M] How does contextual retrieval compare to HyDE for improving retrieval quality? {Q011411,D00409}
- [M] How do you handle retrieval in a multi-turn conversation? {Q007901}
- [M] What goes wrong in multi-turn retrieval when the user abruptly changes topic? {Q007903}
- [M] How do you measure whether query rewriting is actually helping retrieval? {Q007898}
- [H] How do you evaluate query rewriting offline, and what does the golden set look like for multi-turn conversations? {Q007902}
- [H] How would you keep total pre-retrieval latency under 300ms while using query rewriting, HyDE, and similar techniques? {Q007900}

## Routing, filtering, diversity, and special cases
- [M] What is the role of metadata filtering in RAG systems? {Q004770}
- [M] What is the difference between pre-filtering and post-filtering with metadata in vector search, and how does each affect recall? {GEN}
- [M] How does self-querying work, where an LLM turns a natural-language question into metadata filters, and how can it fail? {GEN}
- [H] A metadata filter is too restrictive and returns no results. How do you design a fallback? {GEN}
- [M] How do you add metadata filters and recency weighting to ranking in enterprise search? {D00414}
- [M] How do you handle time in retrieval: "latest" queries, superseded documents, and questions about the past? {Q007924}
- [H] How would you pick the time-decay constant tau for a corpus rather than guessing? {Q007925}
- [M] A user asks "what is our parental leave policy" and three versions of the document exist. What should the retriever return? {Q007926}
- [H] How do you balance relevance and diversity when retrieving document chunks for RAG? {Q003442b}
- [M] How would you pick the MMR lambda without hand-tuning it on intuition? {Q007922}
- [M] When is returning duplicate content actually the right behaviour in retrieval? {Q007923}
- [M] Your product has several distinct corpora (docs, tickets, code, CRM). How do you route queries? {Q007946}
- [M] How would you implement a query router: rules, embedding similarity, or an LLM classifier? What are the tradeoffs? {GEN}
- [M] How do you build the evaluation set for query routing, and what accuracy is acceptable? {Q007947}
- [H] When would you route a numeric question to text-to-SQL instead of RAG, and how do you decide which path a query takes? {Q007913}
- [M] Your corpus is multilingual and users query in several languages. What breaks, and how do you fix it? {Q007930}
- [M] In multilingual retrieval, why translate the query rather than the corpus, and when would you flip that decision? {Q007931}
- [M] How do you keep entity names, such as scheme or place names, from being mangled across scripts in cross-lingual RAG? {Q010081}
- [H] How would you evaluate code retrieval, given that the relevant result is often a set of files rather than one chunk? {Q007929,Q009392}

## Retrieval metrics and evaluation
- [M] What are the key metrics for evaluating retrieval quality in RAG? {Q003435}
- [M] Which retrieval metrics (recall@k, MRR, nDCG) would you track, what does each tell you, and when does each matter? {Q007954,Q008451,D04846,D00411,Q007164}
- [M] Explain the difference between Precision@k and Recall@k in RAG. When might you prefer one? {Q003459}
- [M] Why does recall@k matter more than precision@k for RAG specifically? {Q007955}
- [M] What is the difference between hit rate and recall@k? {GEN}
- [M] Suppose your retriever gets perfect Recall@10 but low Precision@10. What problems could this cause for the generator? {Q003462}
- [M] Why is MRR unsuitable when there are multiple relevant chunks per query, and how does MAP address this? {Q003460}
- [M] How do you calculate MAP@5 for a retrieval result, and what does MAP reveal that raw precision does not? {Q003461}
- [E] Compute MRR for three queries whose first relevant result appears at rank 1, rank 3, and not at all. {GEN}
- [M] When is nDCG more informative than MAP, and how do binary versus graded relevance labels change the choice? {GEN}
- [M] How would NDCG@k change if all relevant chunks are retrieved but in reverse order (least to most relevant)? {Q003463}
- [M] Explain the most common metric used in information retrieval and when it fails. {Q007161}
- [M] For a Quora-like question-answering system that should surface the most pertinent answers quickly, which evaluation metric would you choose? {Q007162}
- [M] How would you evaluate the effectiveness of a reranker? Which of MRR, MAP, and NDCG would you prioritize and why? {Q003458}
- [M] How do you build a labeled golden set for retrieval when you have no annotators, using synthetic queries or LLM judges? {GEN}
- [H] Retrieval metrics improved after a change but end-to-end answer quality did not. Why might that happen? {GEN}
- [H] How would you detect retrieval regressions after swapping the embedding model or the chunking strategy? {GEN}

## Additional questions
- [H] To minimize RAG system latency, which pre-retrieval enhancement technique would you choose? {Q003423}
- [H] When training a code-retrieval component for an agent with a retrieval reward, why weight precision over recall? {Q009331}
- [H] In multilingual retrieval evals, reranking helps Korean-query-to-English-document retrieval much more than English-to-English. Why might that be? {Q009381}
- [M] How would you combine keyword and vector retrieval and merge their ranked lists? {D04968}
