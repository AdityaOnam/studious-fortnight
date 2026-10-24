## Embedding fundamentals
- [E] What is a vector embedding, and what does a dimension count such as 1536 mean for retrieval? {Q004285,Q004870,Q007137,D00359}
- [E] What is an embedding model, and how does it convert text into vectors? {Q004287,Q004755}
- [E] What role do embedding models play in a RAG pipeline and in LLM applications more broadly? {Q003436,Q012423,Q004288,Q007138}
- [E] What is the difference between sparse and dense embeddings? {Q004873}
- [E] What does it mean for two pieces of text to be close in embedding space, and what does that space actually encode? {GEN}
- [M] What are the different types of text embeddings (sparse, dense, multi-vector, learned sparse)? {Q004289}
- [M] When would a learned sparse representation such as SPLADE beat a dense embedding for retrieval? {GEN}
- [M] Explain the intuition behind single-vector dense representations and what information they inevitably lose. {Q004293}
- [M] Why do raw BERT [CLS] or mean-pooled vectors make poor sentence embeddings without contrastive training? How do pooling choices (CLS, mean, last-token) matter? {GEN}
- [M] How does a bi-encoder embedding model work at retrieval time, and what is the key limitation of that architecture? {Q007828}
- [M] Compare bi-encoders, cross-encoders and late-interaction models in cost and accuracy, and explain why they are combined in retrieve-then-rerank. {D00362,D04843}
- [M] Why can't you just feed a decoder LLM's internal token vectors into a vector database for semantic search? {Q006970}
- [M] How do multimodal embeddings such as CLIP and SigLIP create a shared space for text and images? {D00371}
- [M] What is the difference between embedding short and long content, and how do you embed documents longer than the model's input limit? {Q007139}
- [M] What is the vocabulary mismatch problem in embedding-based retrieval? {Q011360,D00365}
- [M] What is asymmetric retrieval, and why do many embedding models require different query and document prefixes or instructions? {Q011399,D00366,Q007859}
- [M] Where do embeddings fail: negation, temporal reasoning, exact identifiers, numeric precision? {Q007066,Q007831}
- [M] How does a multilingual embedding model enable cross-lingual retrieval, and where does quality typically degrade? {GEN}
- [M] Why not simply ask an LLM to judge relevance instead of using embeddings for first-stage retrieval? {D00372}
- [M] When would you maintain multiple embedding spaces rather than a single one? {Q009587}
- [M] When retrieving code for a coding agent, when would you still keep an embedding index around? {Q009332}
- [M] How does an embedding cache work, and what should the cache key include? {Q004878}

## Similarity metrics and geometry
- [E] Explain cosine similarity, dot product and Euclidean distance for vector search, and what role cosine plays in retrieving relevant chunks. {Q004874,Q004310,Q003439,Q003455}
- [M] How would you decide the right similarity metric for a use case, and does the choice actually matter? {Q007152,Q007847,Q007253,D00361}
- [H] Why do Euclidean distance and cosine similarity give the same ranking on normalized vectors? Show it. {Q007254a}
- [M] When would dot product beat cosine similarity, for example in a recommender? {Q007254b}
- [M] What breaks if you index cosine-trained embeddings with an L2 metric without normalizing? When would you actually see a quality difference? {Q007255,Q007848}
- [M] Why is maximum inner product search harder for ANN indexes than cosine search? {GEN}
- [M] Why can embeddings from two different models not be compared directly, even if they have the same dimension? {GEN}
- [H] When does cosine similarity mislead you? Discuss embedding-space pathologies relevant to retrieval systems. {Q007361}
- [H] What is the hubness problem in high-dimensional embedding spaces, and how does it hurt nearest-neighbour retrieval? {GEN}
- [H] What does distance concentration (the curse of dimensionality) mean for nearest-neighbour search quality? {GEN}

## Training embedding models
- [M] Explain contrastive learning and how it is used to train embedding models that capture semantic similarity. {Q004291,Q004872,D00360,Q011221}
- [H] Explain the InfoNCE loss. How are modern embedding models (CLIP, text retrievers) actually trained end to end? {Q007351,Q004290}
- [M] What does the temperature parameter do in a contrastive loss, and what happens if it is too high or too low? {GEN}
- [H] Why do larger batches help contrastive training but matter less for standard supervised training? {Q007352}
- [M] What are hard negatives, and why do they matter when training a dense retriever? How are they mined? {Q007830,D04845}
- [H] How do hard negatives change what the embedding space learns, and what is the risk of false negatives? {Q007353}
- [H] What do alignment and uniformity mean in the Wang and Isola framing of contrastive learning? {Q007364}
- [M] Why do modern embedding models use a large weakly-supervised pretraining stage followed by supervised fine-tuning? {GEN}
- [H] How can distillation from a cross-encoder improve a bi-encoder embedding model? {GEN}
- [H] How would you build the training set for a code-search embedding model? {Q007354}

## Choosing and evaluating embedding models
- [M] What are the key considerations when choosing an embedding model for a RAG system (quality, dimension, context length, latency, cost, licence)? {Q003437,Q003596,Q004298,Q004756,Q010912}
- [M] How would you choose and compare embedding models for a domain-specific corpus with specialized vocabulary? {D00367,D04967}
- [M] How would you use MTEB to choose an embedding model, and what are its limits? {Q007832}
- [M] How do you benchmark and evaluate embedding model quality on your own data? {Q004297,Q004885,Q007140}
- [H] Your domain is medical device manuals. How do you build an evaluation set for choosing an embedding model without human labelers? {Q007833}
- [M] Which retrieval metrics (recall@k, MRR, nDCG) would you use to compare embedding models, and why is an average benchmark score not enough? {GEN}
- [M] A teammate proposes fixing weak RAG answers by upgrading to the largest available embedding model. What is the senior response? {Q007022}
- [M] When is a self-hosted open-weights embedding model clearly better than a hosted API? {Q007834}
- [M] Your embedding model silently truncates long inputs. How do you detect that and what do you do about it? {GEN}
- [H] How would you detect from production data alone that the index was built without the required document prefix? {Q007860}
- [H] If the embedding instruction lives only on the query side, what can you tune without reindexing, and how would you test it? {Q007861}

## Dimensionality, Matryoshka and quantization
- [M] What is the tradeoff of embedding dimensionality, and how does it affect quality, latency, memory and cost? {Q004880,Q011225,Q007868}
- [M] What is a Matryoshka embedding, and why would you choose one for a billion-vector index? {D00363,Q011361}
- [M] Why must you renormalize Matryoshka embeddings after truncating them? {Q007869}
- [H] How would you combine Matryoshka truncation with int8 or binary quantization? {Q007870}
- [H] You need to cut a 3072-dimensional embedding index in half without hurting recall. Walk through your options and how you would validate the choice. {Q007323a}
- [M] At what corpus scale does embedding dimensionality start to dominate your infrastructure bill? {Q007871}
- [M] What is quantization of embeddings, and how does it reduce storage cost? {Q004305,Q004884}
- [H] What advantages does quantization offer over dimensionality reduction for scaling embeddings, and when is the reverse true? {Q003445}
- [M] How do int8 and binary quantization reduce vector storage, and how much recall do you lose? {D00364}
- [M] What is binary quantization, and how does it differ from product quantization? {Q005997,D00379}
- [H] Why does rescoring with full-precision vectors recover recall lost to quantization, and where do you keep those full-precision vectors? {GEN}
- [H] In semantic search over about 100M documents with binary-quantized embeddings and rescoring, how do you pick the rescoring depth empirically? {Q009376}
- [M] Where does recall loss from binary-quantized retrieval show up in RAG quality metrics? {Q009377}
- [M] At what point does the ANN index's RAM cost push you toward quantization? {Q007839}
- [H] Sketch the memory math for 1B 768-dimensional vectors under float32, int8 and PQ-96. When would binary quantization with rescoring beat PQ? {Q007882}

## Fine-tuning and adapting embeddings
- [M] When would you fine-tune your embedding model, and how would you actually do it? {Q007872,Q003444,Q004889,D00368}
- [M] Your RAG system fails on domain-specific jargon. How do you fix it? {Q004782}
- [H] After benchmarking an off-the-shelf embedding model, accuracy is low. How would you improve the accuracy of the embedding-based search? {Q007141}
- [H] Walk me through the steps of improving a sentence-transformer model used for embedding. {Q007142}
- [M] Why are hard negatives essential when fine-tuning an embedding model? What happens with only random negatives? {Q007873}
- [M] How would you generate synthetic training queries for fine-tuning an embedder when you have no labelled data? {GEN}
- [M] Fine-tuned embedder versus fine-tuned reranker: how do you choose? {Q007874}
- [M] When would you fine-tune an embedding model instead of the LLM? {Q009792}
- [M] How do you avoid regressing on general queries after fine-tuning an embedding model on a narrow domain? {GEN}
- [H] What is a lightweight query-side adapter on frozen embeddings, and when is it preferable to full fine-tuning? {GEN}

## Vector database fundamentals
- [E] What is a vector database, and what does it store for LLM and RAG use? {Q003438,Q004299,Q005342}
- [E] How does a vector database differ from a traditional database, and why not use a general-purpose database for vector search? {Q004300,Q004875,Q007143,Q011363}
- [E] What is the role of metadata stored alongside vectors? {Q004886}
- [M] How does a vector database work, from ingestion to query? {Q004301}
- [M] Explain the difference between a vector index, a vector database and a vector plugin. {Q007144}
- [M] What is the difference between a vector library like FAISS and a full vector database like Milvus? {GEN}
- [M] How does a vector database handle inserts, updates and deletes (segments, tombstones, compaction)? {GEN}
- [M] How long after an insert does a new vector become searchable, and what consistency tradeoffs does that imply? {GEN}
- [M] How do you decide the best vector database for your needs? What criteria matter? {Q004304,Q007154,Q010863,Q011158}
- [M] Compare pgvector, dedicated vector stores and search engines as a vector backend. {Q007883}
- [M] Why choose PostgreSQL with pgvector, and when should you switch to a dedicated vector database? {Q003602,Q010316,D00383}
- [H] Under what circumstances does a pgvector HNSW index degrade into a slower scan? {Q003622}
- [H] How do you keep pgvector search fast while the same instance takes heavy writes? {Q010317}
- [M] How would you choose between Pinecone and a self-hosted solution? {Q011368,D00382}
- [M] A 4-person startup is launching a B2B RAG product with about 2M vectors per customer and a strict data-residency requirement. Should it build or buy the vector store? {Q007049}
- [M] When is Elasticsearch's BM25 maturity worth its operational weight? {Q007886}
- [M] What consistency bugs appear when the vector index is a separate system from the document store? {Q007884}
- [M] How do you combine vector similarity with business conditions in a single query? {GEN}

## ANN search and index algorithms
- [E] When do you need approximate nearest neighbour search instead of exact search, and why is it acceptable for results to be inexact? {Q007836,Q003598,Q004876}
- [M] You have a small dataset of customer reviews and perfect accuracy matters more than speed. Which search strategy would you choose and why? {Q007145}
- [M] What are the different strategies for searching in a vector database or index? Compare tree-based, LSH and clustering-based ANN methods. {Q004302,Q007146,D03479}
- [M] Explain clustering in vector retrieval and how it reduces the search space. {Q004303}
- [H] When does clustering-based pruning fail, and how can you mitigate those failures? {Q007147}
- [M] Explain locality-sensitive hashing and its relation to k-NN. {Q001537,Q004306,Q007149}
- [M] Explain the random projection index. {Q007148}
- [M] Explain the concept of inverted indices in vector retrieval. {Q004308}
- [M] Compare IVF, IVF-PQ and HNSW, and say when each fits. {D00375}
- [M] How do IVF centroids get trained, what does nprobe control, and what goes wrong with skewed clusters? {GEN}
- [M] Why does IVF need retraining as data drifts but HNSW does not? {Q007881}
- [M] Explain how HNSW works, and what the layers and the M and ef parameters do. {Q004309,Q007065}
- [M] How do M, efConstruction and efSearch affect recall, latency and memory in HNSW? {Q007876,D00374}
- [M] Explain how HNSW works and when you would not use it. {Q011369,D00373}
- [M] What is the difference between HNSW and IVFFlat? {Q003599}
- [H] How do you tune HNSW's ef_search, and what happens when it is increased or decreased? {Q003600}
- [H] How would you tune HNSW M and ef differently for a 99%-recall offline job versus a 20ms-p99 online API? {Q007879}
- [M] Your retriever's recall@20 is stuck at 0.86 and tuning chunking has not moved it. You are on HNSW with default parameters. What is worth trying first? {Q007025}
- [M] What happens to search quality after deleting 40% of vectors from an HNSW index? {Q007878}
- [H] Your p99 latency doubled after deleting 30% of vectors from the index. What happened? {Q007838}
- [H] Why do graph indexes like HNSW use more memory than IVF, and how do their build times and update behaviour compare? {GEN}
- [M] Explain product quantization: how does it compress vectors, and what error does it introduce? {Q004307,Q007150,D00376}
- [M] What is DiskANN, and when would you choose a disk-based index over a RAM-based one like HNSW? {Q005994,Q011370,D00377}
- [M] What is ScaNN, and how does it differ fundamentally from IVF-PQ and HNSW? {Q005999,D00378}
- [M] How does FAISS implement efficient approximate nearest neighbour search? {Q003493}
- [H] Compare flat, HNSW and IVF-PQ indexes. How do you pick, and what does recall@k cost in latency? {Q004877,Q011822,Q006194,Q007880,Q010823}
- [H] Given a project scenario, compare vector indexes and explain which one you would use and why. {Q007151,D03814}
- [M] How exactly would you measure the recall your ANN index achieves? {Q007837}
- [M] How do you read a recall-versus-QPS benchmark curve when comparing ANN libraries? {GEN}
- [M] How do you monitor and tune a vector index in production for recall and latency? {D00381}

## Filtering, multi-tenancy and access control
- [E] Explain pre-filtering versus post-filtering in a vector database and the challenges of each. {Q007153,Q007887}
- [M] Why does a highly selective metadata filter hurt HNSW specifically? {Q007877}
- [H] Why is metadata filtering often the bottleneck in vector databases? What do in-graph filtering and brute-force fallback do? {Q011371,D00380}
- [M] A post-filtered ANN query with an ACL filter returns fewer than k results. Why, and how do you fix it? {GEN}
- [M] Your queries use a tenant filter with 5% selectivity. How does that change your vector database choice? {Q007885}
- [M] How do you handle multi-tenancy in a vector database: namespaces, per-tenant indexes, or row-level security? {Q004883,Q011372,D00385}
- [M] In a multi-tenant RAG system, why not use one vector database or index per tenant? {Q011696,Q010314}
- [H] Design indexing for 10k tenants where the largest has 10M vectors and the median has 5k. How does the DB choose between filtered ANN and brute force, and what would a cost model look at? {Q007889}
- [H] How do you enforce document-level permissions and right-to-be-forgotten requests in a vector store? {Q010379}

## Scaling, sharding and capacity
- [M] Your RAG retrieval is too slow with a large knowledge base. How do you speed it up? {Q004779}
- [M] Your vector database cannot scale to millions of embeddings. How do you find and fix the bottleneck? {Q004891,Q004775}
- [H] If vector data grows from 1 million to 100 million, what architectural changes are needed? {Q003601}
- [H] How does a vector database search billions of vectors in milliseconds? {Q004887,Q012504,Q004314}
- [M] How would you size the index for 50M chunks of 1,536-dimensional embeddings on HNSW? {Q007058}
- [M] Your vector database for RAG is consuming too much memory. How do you reduce it? {Q004890}
- [M] You are serving 50M chunks and the index will not fit in your RAM budget. Which move shrinks the footprint without re-embedding the corpus? {Q007026}
- [H] You must serve 800M vectors on a tight RAM budget. Which index choice fits, and what is the cost? {Q007046}
- [M] What embedding dimension, index and rerank depth would you choose for a retrieval system over millions of chunks? {Q006795,D04833}
- [M] How do you plan capacity for a vector index with hundreds of millions of vectors, including memory tiers and replicas? {D00386}
- [H] Your vector index will not fit on one machine. How do you shard it, and what breaks? {Q007990,D00388}
- [H] With 20 shards and scatter-gather queries, how do you keep p99 from being dominated by the slowest shard? {Q007991}
- [H] In sharded vector search, how much do you over-fetch per shard, and how would you determine that number? {Q007992}
- [M] When do you add replicas versus shards in a vector search cluster? {GEN}
- [H] How do you keep multi-vector (ColPali-style) storage from exploding at 5M pages? {Q008968}
- [M] When embedding millions of chunks through an embedding service, the service starts returning 429s. How does the batcher adapt? {Q010016}
- [M] How do you design an embedding service for large-scale RAG with cost optimization? {D00387}

## Embedding drift, re-embedding and migration
- [M] What is embedding drift, and how do you handle it when the embedding model is updated? {Q004881,Q011224,D00370}
- [H] What causes semantic drift in embedding search, and how do you detect it? {Q011820}
- [M] What breaks when you change embedding models and forget to re-embed the corpus? {Q007835}
- [M] You push vectors from an upgraded embedding model into the existing live index alongside the old ones. What happens? {Q007050}
- [M] Your new embedding model has different dimensions from the vectors in production. How do you handle the mismatch? {Q004892}
- [H] You must upgrade the embedding model behind a 500M-vector index. How do you roll it out with zero downtime? {Q011362,D00369,Q007875,Q010318,Q009571}
- [H] A better embedding model ships and you have 400M chunks indexed. How do you decide whether the reindex is worth it? {Q007979}
- [H] During an embedding migration, what breaks if the dual-write window has a gap and some documents exist only in the old index? {Q007980}
- [H] A re-embedding backfill of 200M vectors is 60% done when the provider deprecates the old model's endpoint. What now? {Q010352}
- [H] How do you version a RAG pipeline so you can re-embed safely when you change the embedding model? {Q007819}
- [M] In a similarity-search system, what breaks when you swap the embedding encoder for a better one? {Q010229}
- [H] How would you migrate a vector database without downtime or retrieval regression? {D00384}
- [M] How do you back up a vector index, and how long would a rebuild after a crash take for 100M vectors? {GEN}

## Additional questions
- [E] How does LangChain handle embeddings and vector stores? {Q012533}
