## Long context vs RAG
- [E] Is RAG still relevant now that frontier LLMs ship 1M-token context windows? {Q003405,Q007068,Q011156,Q011352,Q007044}
- [M] When would you choose long context over retrieval, and when should you use RAG instead? {Q004772,Q011338,Q011988,Q009881,Q009391}
- [M] A teammate wants to stuff all relevant docs into a 200k-token context per query instead of retrieving. Why push back, and what would you measure? {Q007106,Q009410}
- [M] What are the known failure modes of stuffing very long contexts, such as lost-in-the-middle and distraction by irrelevant text? {GEN}
- [M] Why is context caching better than RAG for a 50k-token document, and when does that stop being true? {Q011298}
- [M] How does prompt caching change the full-context versus retrieval decision for a contract a lawyer asks twenty questions about? {Q009694}
- [M] How would prefix caching change the cost calculus for a long shared context reused across many queries? {Q009882}
- [M] How do you decide empirically how many chunks to retrieve, given that long contexts make retrieving generously cheap? {Q007978}
- [H] How exactly does prompt caching shift the crossover corpus size between long-context stuffing and RAG? Sketch the cost math. {Q007977a}
- [H] Compare per-query cost and latency of a 1M-token prompt with a 5k-token RAG prompt at 100k queries a day. What numbers drive the decision? {GEN}
- [H] When would you put a whole contract in the context window instead of retrieving over it? Defend the answer with numbers. {Q009693}
- [H] At what corpus size would you stop hybridising long-context and retrieval approaches and go retrieval-only? {Q009695}
- [H] What retrieval failure would long context mask, and is masking it good or bad? {Q009883}
- [H] If effective context length keeps improving, which RAG components die first and which never do? {Q007977b}
- [M] Design a hybrid system where retrieval narrows a large corpus and a long-context model then reads the shortlist in full. What are the tradeoffs? {GEN}

## Multi-hop and multi-faceted queries
- [E] What is a multi-hop question, and why does single-shot top-k retrieval fail on it? {GEN}
- [M] How do you handle multi-document and multi-hop or multifaceted questions in RAG? {Q004761,Q007167}
- [M] Your RAG system fails on questions that require combining multiple facts. How do you diagnose and fix it? {Q004785}
- [M] Why can plain top-k retrieval never answer "summarise the main themes of this corpus"? {Q007941b}
- [M] Compare query decomposition with iterative retrieve-then-reason approaches such as IRCoT for multi-hop questions. {GEN}
- [M] How do you evaluate multi-hop RAG separately from single-hop RAG? Which intermediate signals would you log? {GEN}
- [H] How do you prevent error propagation across hops, where a wrong first-hop retrieval poisons every later hop? {GEN}
- [H] A lawyer asks about a 200-page credit agreement where the operative clause on page 140 depends on a defined term on page 8. How do you build retrieval that gets this right? {Q012105,Q009673}
- [H] In a RAG system over legal agreements, how do you handle an amended and restated agreement where an amendment on page 190 supersedes the clause on page 140? {Q009674}

## GraphRAG and knowledge graphs
- [E] What problem does GraphRAG solve, and how does it differ from standard vector RAG? {Q004765,Q005954,Q003605,Q007939,D00415}
- [M] Users mostly ask narrow factual lookups such as "what is the refund window for plan X?", and a teammate wants to switch everything to GraphRAG. What is the right call? {Q007041}
- [M] How would you build a knowledge graph for GraphRAG from unstructured documents? {D00419}
- [M] Why is entity extraction the bottleneck of GraphRAG indexing? {Q011388,D00416}
- [M] How does community summarization let GraphRAG answer aggregate questions that exceed the context window? {Q011389,D00417}
- [M] What is the difference between local and global search in GraphRAG, and which queries suit each? {GEN}
- [M] What is a property graph, and why can it beat basic vector RAG on relationship-heavy questions? {Q011540}
- [M] What is the graph-as-reranker pattern, and when does it help? {D00420}
- [M] How would you handle entity resolution errors that pollute the knowledge graph in GraphRAG? {Q007940}
- [M] What is the maintenance tail of a knowledge graph, and when does it outweigh the benefits? {D00418}
- [M] How would you let an LLM answer questions over a graph database, for example via generated Cypher, and what can go wrong? {GEN}
- [H] How would you update a GraphRAG index incrementally when documents are added, edited, or deleted every day? {GEN}
- [H] Estimate indexing cost for GraphRAG versus standard RAG on a 1M-chunk corpus. {Q007941a}
- [H] How would you evaluate whether GraphRAG actually beats a well-tuned hybrid-search baseline on your data? {GEN}

## Agentic RAG
- [E] What is agentic RAG? {Q010765}
- [M] How does agentic RAG differ from traditional or advanced RAG, and when is the extra complexity justified? {Q010904,Q011353,Q011819,Q005955,Q007942}
- [M] What do multi-hop reasoning, agentic RAG and GraphRAG each add over a basic RAG pipeline, and when are they worth the cost? {D03816}
- [M] What is the reasoning-retrieval balance in agentic RAG, and how do you stop the agent from over-searching? {Q011394,D00424}
- [M] Why does agentic RAG often give higher quality but lower reliability and determinism? {Q011395,D00421}
- [M] What new failure modes does agentic RAG introduce compared to a linear pipeline? {D00425}
- [M] What guardrails cap cost when the model controls how many searches it runs? {Q007944}
- [M] When does letting the model write its own queries beat an explicit query-rewriting step? {Q007904}
- [M] What does an agent need in a search tool's results so it can reformulate well after a miss? {Q008004}
- [M] What is state-aware or agentic retrieval, and how does it differ from standard retrieval? {D00435}
- [M] How would you evaluate an agentic RAG system: final-answer quality, trajectory quality, or both? {GEN}
- [M] How do you decide when an agentic RAG loop should stop searching and answer? {GEN}
- [M] When does an embedding index beat an agent using grep over a code repository? {Q007928}
- [M] How might a code assistant retrieve relevant context from a repository, and what unique challenges does code retrieval pose? {D04839}
- [H] When is RAG-then-stuff worse than an agentic search-and-read loop over the corpus? {Q007707}
- [H] A teammate wants to delete the vector index and give the agent grep, file reads and keyword search, as coding agents do. Where are they right, and where does it break outside code? {Q008002}
- [H] When would you compile knowledge up front instead of running an agentic retrieval loop at query time? {Q011396}
- [H] How would you design routing in an agentic RAG system with several specialised retrieval tools (vector, SQL, web, graph)? {GEN}
- [H] Your agentic RAG p95 latency is 25 seconds. Where does the time go, and how do you cut it without hurting quality? {GEN}

## Self-RAG, corrective and adaptive RAG
- [M] How does Self-RAG work, and how does the model decide when to retrieve? {Q004764}
- [M] What are reflection tokens in Self-RAG, and how are they used to critique retrieved passages and generations? {GEN}
- [M] Explain Self-RAG and corrective RAG. How do they decide whether to retrieve or re-retrieve, and do they earn their complexity in production? {Q007933,D00422}
- [M] In corrective RAG, what is the right fallback when the grader says every retrieved document is irrelevant and no web search is available? {Q007934}
- [M] How would you keep a retrieval grading loop from doubling your p95 latency? {Q007935}
- [M] How would you implement adaptive retrieval where effort scales with query complexity? {D00426}
- [M] How does a self-healing RAG system detect and recover from bad retrieval? {D00428}
- [M] How would you build and validate a retrieval relevance grader? What failure rates are acceptable? {GEN}
- [M] When should a system skip retrieval entirely for a query, and how would you detect that? {GEN}
- [H] Your relevance grader has a 10% false-negative rate and discards useful documents. What are the consequences and the mitigations? {GEN}

## Multimodal RAG
- [E] What is multimodal RAG, and how does it differ from text-only RAG? {Q005087}
- [M] Your text-only RAG system now needs to handle images and tables. How do you extend it? {Q004783}
- [M] How do image-text multimodal RAG systems index and retrieve mixed content? {D00434}
- [M] How do you build a dual representation of charts and diagrams for retrieval? {D00433}
- [M] How does ColPali-style page-as-image retrieval compare with a parse-then-embed pipeline? {D00432}
- [M] What are the storage and latency costs of multi-vector page-image retrieval, and how would you reduce them? {GEN}
- [M] How would you handle OCR and table-extraction errors in a multimodal RAG pipeline? {GEN}
- [H] When is caption-and-embed strictly better than ColPali for multimodal document retrieval? {Q008969}
- [H] Design multimodal RAG over 50k PDFs full of tables, charts and diagrams. Where does ColPali-style retrieval fit? {Q008967}
- [M] Design a multimodal RAG system for a financial research platform with charts, tables and text. {D00429}
- [H] How would you answer a query that needs information from both a chart and a table on different pages? {Q011422,D00430}
- [H] Users want to query a 10,000-hour video library. How do you design and cost multimodal retrieval over it? {D00431}
- [H] How would you evaluate retrieval and answer quality in a multimodal RAG system where ground truth lives in images? {GEN}

## Structured data, enterprise graphs and ontologies
- [H] Some questions are answered by your data warehouse, some by documents, and some by both. How do you design retrieval across structured and unstructured data? {Q007936}
- [H] Users ask "how many open orders are blocked on a supplier issue?" and plain RAG gets it wrong. Why, and what is the right architecture? {Q012116,Q009985}
- [H] A query needs documents and tickets joined together. How does each retrieval architecture cope? {Q007948}
- [M] How would you design a hierarchical or multi-index strategy for a large heterogeneous corpus? {D00438}
- [M] What is an ontology, and why put LLM agents on top of one instead of on raw tables and documents? {Q009964}
- [H] Who maintains an ontology used by LLM agents when the business changes, and what breaks when it drifts? {Q009965}
- [H] When is building an ontology layer for LLM agents not worth it? {Q009966}
- [H] An enterprise search ranking leans on a knowledge graph of people, content and activity. How would you build that graph, and how does it improve retrieval beyond embedding similarity? {Q009596}
- [H] How do you resolve the same person or project across ten systems with no shared identifier when building an enterprise knowledge graph? {Q009597}
- [M] How would you let an agent decide between text-to-SQL and document retrieval for a given question? {GEN}

## Caching and memory-augmented retrieval
- [M] What caching strategies apply to RAG systems, and what are the invalidation traps? {Q007974}
- [M] How do you pick the similarity threshold for a semantic cache? What experiment would you run? {Q007975}
- [M] What is the difference between caching retrieval results, caching embeddings, and caching final LLM answers? {GEN}
- [H] Why does keying a semantic cache by user break its hit rate, and what is the middle ground? {Q007952}
- [H] A semantic cache returns a wrong but similar-looking answer to a different question. How do you detect and prevent such false hits? {GEN}
- [M] How do REALM and WebGPT integrate retrieval or browsing into language models? {D04847}
- [M] How would you design long-term memory for an LLM agent using retrieval, and how do you decide what to store and what to forget? {GEN}
- [M] When should an agent's memory store use a vector database and when a knowledge graph? {D00436}
- [H] How do you handle contradictory or outdated memories when an agent retrieves from its own long-term store? {GEN}

## Additional questions
- [M] How does multi-hop reasoning work in an agentic retrieval loop? {D00423}
