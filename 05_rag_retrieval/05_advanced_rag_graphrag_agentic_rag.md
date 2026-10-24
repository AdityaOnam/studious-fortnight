---
domain: rag
topic: advanced_rag_graphrag_agentic_rag
title: Advanced RAG: GraphRAG, agentic RAG
tags: [graphrag, agentic-rag, self-rag, multi-hop]
count: 100
---
# Advanced RAG: GraphRAG, agentic RAG

## Long context vs RAG
- [RAG05-001] Is RAG still relevant now that frontier LLMs ship 1M-token context windows?
- [RAG05-002] When would you choose long context over retrieval, and when should you use RAG instead?
- [RAG05-003] A teammate wants to stuff all relevant docs into a 200k-token context per query instead of retrieving. Why push back, and what would you measure?
- [RAG05-004] What are the known failure modes of stuffing very long contexts, such as lost-in-the-middle and distraction by irrelevant text?
- [RAG05-005] Why is context caching better than RAG for a 50k-token document, and when does that stop being true?
- [RAG05-006] How does prompt caching change the full-context versus retrieval decision for a contract a lawyer asks twenty questions about?
- [RAG05-007] How would prefix caching change the cost calculus for a long shared context reused across many queries?
- [RAG05-008] How do you decide empirically how many chunks to retrieve, given that long contexts make retrieving generously cheap?
- [RAG05-009] How exactly does prompt caching shift the crossover corpus size between long-context stuffing and RAG? Sketch the cost math.
- [RAG05-010] Compare per-query cost and latency of a 1M-token prompt with a 5k-token RAG prompt at 100k queries a day. What numbers drive the decision?
- [RAG05-011] When would you put a whole contract in the context window instead of retrieving over it? Defend the answer with numbers.
- [RAG05-012] At what corpus size would you stop hybridising long-context and retrieval approaches and go retrieval-only?
- [RAG05-013] What retrieval failure would long context mask, and is masking it good or bad?
- [RAG05-014] If effective context length keeps improving, which RAG components die first and which never do?
- [RAG05-015] Design a hybrid system where retrieval narrows a large corpus and a long-context model then reads the shortlist in full. What are the tradeoffs?

## Multi-hop and multi-faceted queries
- [RAG05-016] What is a multi-hop question, and why does single-shot top-k retrieval fail on it?
- [RAG05-017] How do you handle multi-document and multi-hop or multifaceted questions in RAG?
- [RAG05-018] Your RAG system fails on questions that require combining multiple facts. How do you diagnose and fix it?
- [RAG05-019] Why can plain top-k retrieval never answer "summarise the main themes of this corpus"?
- [RAG05-020] Compare query decomposition with iterative retrieve-then-reason approaches such as IRCoT for multi-hop questions.
- [RAG05-021] How do you evaluate multi-hop RAG separately from single-hop RAG? Which intermediate signals would you log?
- [RAG05-022] How do you prevent error propagation across hops, where a wrong first-hop retrieval poisons every later hop?
- [RAG05-023] A lawyer asks about a 200-page credit agreement where the operative clause on page 140 depends on a defined term on page 8. How do you build retrieval that gets this right?
- [RAG05-024] In a RAG system over legal agreements, how do you handle an amended and restated agreement where an amendment on page 190 supersedes the clause on page 140?

## GraphRAG and knowledge graphs
- [RAG05-025] What problem does GraphRAG solve, and how does it differ from standard vector RAG?
- [RAG05-026] Users mostly ask narrow factual lookups such as "what is the refund window for plan X?", and a teammate wants to switch everything to GraphRAG. What is the right call?
- [RAG05-027] How would you build a knowledge graph for GraphRAG from unstructured documents?
- [RAG05-028] Why is entity extraction the bottleneck of GraphRAG indexing?
- [RAG05-029] How does community summarization let GraphRAG answer aggregate questions that exceed the context window?
- [RAG05-030] What is the difference between local and global search in GraphRAG, and which queries suit each?
- [RAG05-031] What is a property graph, and why can it beat basic vector RAG on relationship-heavy questions?
- [RAG05-032] What is the graph-as-reranker pattern, and when does it help?
- [RAG05-033] How would you handle entity resolution errors that pollute the knowledge graph in GraphRAG?
- [RAG05-034] What is the maintenance tail of a knowledge graph, and when does it outweigh the benefits?
- [RAG05-035] How would you let an LLM answer questions over a graph database, for example via generated Cypher, and what can go wrong?
- [RAG05-036] How would you update a GraphRAG index incrementally when documents are added, edited, or deleted every day?
- [RAG05-037] Estimate indexing cost for GraphRAG versus standard RAG on a 1M-chunk corpus.
- [RAG05-038] How would you evaluate whether GraphRAG actually beats a well-tuned hybrid-search baseline on your data?

## Agentic RAG
- [RAG05-039] What is agentic RAG?
- [RAG05-040] How does agentic RAG differ from traditional or advanced RAG, and when is the extra complexity justified?
- [RAG05-041] What do multi-hop reasoning, agentic RAG and GraphRAG each add over a basic RAG pipeline, and when are they worth the cost?
- [RAG05-042] What is the reasoning-retrieval balance in agentic RAG, and how do you stop the agent from over-searching?
- [RAG05-043] Why does agentic RAG often give higher quality but lower reliability and determinism?
- [RAG05-044] What new failure modes does agentic RAG introduce compared to a linear pipeline?
- [RAG05-045] What guardrails cap cost when the model controls how many searches it runs?
- [RAG05-046] When does letting the model write its own queries beat an explicit query-rewriting step?
- [RAG05-047] What does an agent need in a search tool's results so it can reformulate well after a miss?
- [RAG05-048] What is state-aware or agentic retrieval, and how does it differ from standard retrieval?
- [RAG05-049] How would you evaluate an agentic RAG system: final-answer quality, trajectory quality, or both?
- [RAG05-050] How do you decide when an agentic RAG loop should stop searching and answer?
- [RAG05-051] When does an embedding index beat an agent using grep over a code repository?
- [RAG05-052] How might a code assistant retrieve relevant context from a repository, and what unique challenges does code retrieval pose?
- [RAG05-053] When is RAG-then-stuff worse than an agentic search-and-read loop over the corpus?
- [RAG05-054] A teammate wants to delete the vector index and give the agent grep, file reads and keyword search, as coding agents do. Where are they right, and where does it break outside code?
- [RAG05-055] When would you compile knowledge up front instead of running an agentic retrieval loop at query time?
- [RAG05-056] How would you design routing in an agentic RAG system with several specialised retrieval tools (vector, SQL, web, graph)?
- [RAG05-057] Your agentic RAG p95 latency is 25 seconds. Where does the time go, and how do you cut it without hurting quality?

## Self-RAG, corrective and adaptive RAG
- [RAG05-058] How does Self-RAG work, and how does the model decide when to retrieve?
- [RAG05-059] What are reflection tokens in Self-RAG, and how are they used to critique retrieved passages and generations?
- [RAG05-060] Explain Self-RAG and corrective RAG. How do they decide whether to retrieve or re-retrieve, and do they earn their complexity in production?
- [RAG05-061] In corrective RAG, what is the right fallback when the grader says every retrieved document is irrelevant and no web search is available?
- [RAG05-062] How would you keep a retrieval grading loop from doubling your p95 latency?
- [RAG05-063] How would you implement adaptive retrieval where effort scales with query complexity?
- [RAG05-064] How does a self-healing RAG system detect and recover from bad retrieval?
- [RAG05-065] How would you build and validate a retrieval relevance grader? What failure rates are acceptable?
- [RAG05-066] When should a system skip retrieval entirely for a query, and how would you detect that?
- [RAG05-067] Your relevance grader has a 10% false-negative rate and discards useful documents. What are the consequences and the mitigations?

## Multimodal RAG
- [RAG05-068] What is multimodal RAG, and how does it differ from text-only RAG?
- [RAG05-069] Your text-only RAG system now needs to handle images and tables. How do you extend it?
- [RAG05-070] How do image-text multimodal RAG systems index and retrieve mixed content?
- [RAG05-071] How do you build a dual representation of charts and diagrams for retrieval?
- [RAG05-072] How does ColPali-style page-as-image retrieval compare with a parse-then-embed pipeline?
- [RAG05-073] What are the storage and latency costs of multi-vector page-image retrieval, and how would you reduce them?
- [RAG05-074] How would you handle OCR and table-extraction errors in a multimodal RAG pipeline?
- [RAG05-075] When is caption-and-embed strictly better than ColPali for multimodal document retrieval?
- [RAG05-076] Design multimodal RAG over 50k PDFs full of tables, charts and diagrams. Where does ColPali-style retrieval fit?
- [RAG05-077] Design a multimodal RAG system for a financial research platform with charts, tables and text.
- [RAG05-078] How would you answer a query that needs information from both a chart and a table on different pages?
- [RAG05-079] Users want to query a 10,000-hour video library. How do you design and cost multimodal retrieval over it?
- [RAG05-080] How would you evaluate retrieval and answer quality in a multimodal RAG system where ground truth lives in images?

## Structured data, enterprise graphs and ontologies
- [RAG05-081] Some questions are answered by your data warehouse, some by documents, and some by both. How do you design retrieval across structured and unstructured data?
- [RAG05-082] Users ask "how many open orders are blocked on a supplier issue?" and plain RAG gets it wrong. Why, and what is the right architecture?
- [RAG05-083] A query needs documents and tickets joined together. How does each retrieval architecture cope?
- [RAG05-084] How would you design a hierarchical or multi-index strategy for a large heterogeneous corpus?
- [RAG05-085] What is an ontology, and why put LLM agents on top of one instead of on raw tables and documents?
- [RAG05-086] Who maintains an ontology used by LLM agents when the business changes, and what breaks when it drifts?
- [RAG05-087] When is building an ontology layer for LLM agents not worth it?
- [RAG05-088] An enterprise search ranking leans on a knowledge graph of people, content and activity. How would you build that graph, and how does it improve retrieval beyond embedding similarity?
- [RAG05-089] How do you resolve the same person or project across ten systems with no shared identifier when building an enterprise knowledge graph?
- [RAG05-090] How would you let an agent decide between text-to-SQL and document retrieval for a given question?

## Caching and memory-augmented retrieval
- [RAG05-091] What caching strategies apply to RAG systems, and what are the invalidation traps?
- [RAG05-092] How do you pick the similarity threshold for a semantic cache? What experiment would you run?
- [RAG05-093] What is the difference between caching retrieval results, caching embeddings, and caching final LLM answers?
- [RAG05-094] Why does keying a semantic cache by user break its hit rate, and what is the middle ground?
- [RAG05-095] A semantic cache returns a wrong but similar-looking answer to a different question. How do you detect and prevent such false hits?
- [RAG05-096] How do REALM and WebGPT integrate retrieval or browsing into language models?
- [RAG05-097] How would you design long-term memory for an LLM agent using retrieval, and how do you decide what to store and what to forget?
- [RAG05-098] When should an agent's memory store use a vector database and when a knowledge graph?
- [RAG05-099] How do you handle contradictory or outdated memories when an agent retrieves from its own long-term store?

## Additional questions
- [RAG05-100] How does multi-hop reasoning work in an agentic retrieval loop?
