---
domain: rag
topic: embeddings_vector_db_ann_indexes
title: Embeddings, vector databases and ANN indexes
tags: [embeddings, vector-db, hnsw, ann]
count: 166
---
# Embeddings, vector databases and ANN indexes

## Embedding fundamentals
- [RAG03-001] What is a vector embedding, and what does a dimension count such as 1536 mean for retrieval?
- [RAG03-002] What is an embedding model, and how does it convert text into vectors?
- [RAG03-003] What role do embedding models play in a RAG pipeline and in LLM applications more broadly?
- [RAG03-004] What is the difference between sparse and dense embeddings?
- [RAG03-005] What does it mean for two pieces of text to be close in embedding space, and what does that space actually encode?
- [RAG03-006] What are the different types of text embeddings (sparse, dense, multi-vector, learned sparse)?
- [RAG03-007] When would a learned sparse representation such as SPLADE beat a dense embedding for retrieval?
- [RAG03-008] Explain the intuition behind single-vector dense representations and what information they inevitably lose.
- [RAG03-009] Why do raw BERT [CLS] or mean-pooled vectors make poor sentence embeddings without contrastive training? How do pooling choices (CLS, mean, last-token) matter?
- [RAG03-010] How does a bi-encoder embedding model work at retrieval time, and what is the key limitation of that architecture?
- [RAG03-011] Compare bi-encoders, cross-encoders and late-interaction models in cost and accuracy, and explain why they are combined in retrieve-then-rerank.
- [RAG03-012] Why can't you just feed a decoder LLM's internal token vectors into a vector database for semantic search?
- [RAG03-013] How do multimodal embeddings such as CLIP and SigLIP create a shared space for text and images?
- [RAG03-014] What is the difference between embedding short and long content, and how do you embed documents longer than the model's input limit?
- [RAG03-015] What is the vocabulary mismatch problem in embedding-based retrieval?
- [RAG03-016] What is asymmetric retrieval, and why do many embedding models require different query and document prefixes or instructions?
- [RAG03-017] Where do embeddings fail: negation, temporal reasoning, exact identifiers, numeric precision?
- [RAG03-018] How does a multilingual embedding model enable cross-lingual retrieval, and where does quality typically degrade?
- [RAG03-019] Why not simply ask an LLM to judge relevance instead of using embeddings for first-stage retrieval?
- [RAG03-020] When would you maintain multiple embedding spaces rather than a single one?
- [RAG03-021] When retrieving code for a coding agent, when would you still keep an embedding index around?
- [RAG03-022] How does an embedding cache work, and what should the cache key include?

## Similarity metrics and geometry
- [RAG03-023] Explain cosine similarity, dot product and Euclidean distance for vector search, and what role cosine plays in retrieving relevant chunks.
- [RAG03-024] How would you decide the right similarity metric for a use case, and does the choice actually matter?
- [RAG03-025] Why do Euclidean distance and cosine similarity give the same ranking on normalized vectors? Show it.
- [RAG03-026] When would dot product beat cosine similarity, for example in a recommender?
- [RAG03-027] What breaks if you index cosine-trained embeddings with an L2 metric without normalizing? When would you actually see a quality difference?
- [RAG03-028] Why is maximum inner product search harder for ANN indexes than cosine search?
- [RAG03-029] Why can embeddings from two different models not be compared directly, even if they have the same dimension?
- [RAG03-030] When does cosine similarity mislead you? Discuss embedding-space pathologies relevant to retrieval systems.
- [RAG03-031] What is the hubness problem in high-dimensional embedding spaces, and how does it hurt nearest-neighbour retrieval?
- [RAG03-032] What does distance concentration (the curse of dimensionality) mean for nearest-neighbour search quality?

## Training embedding models
- [RAG03-033] Explain contrastive learning and how it is used to train embedding models that capture semantic similarity.
- [RAG03-034] Explain the InfoNCE loss. How are modern embedding models (CLIP, text retrievers) actually trained end to end?
- [RAG03-035] What does the temperature parameter do in a contrastive loss, and what happens if it is too high or too low?
- [RAG03-036] Why do larger batches help contrastive training but matter less for standard supervised training?
- [RAG03-037] What are hard negatives, and why do they matter when training a dense retriever? How are they mined?
- [RAG03-038] How do hard negatives change what the embedding space learns, and what is the risk of false negatives?
- [RAG03-039] What do alignment and uniformity mean in the Wang and Isola framing of contrastive learning?
- [RAG03-040] Why do modern embedding models use a large weakly-supervised pretraining stage followed by supervised fine-tuning?
- [RAG03-041] How can distillation from a cross-encoder improve a bi-encoder embedding model?
- [RAG03-042] How would you build the training set for a code-search embedding model?

## Choosing and evaluating embedding models
- [RAG03-043] What are the key considerations when choosing an embedding model for a RAG system (quality, dimension, context length, latency, cost, licence)?
- [RAG03-044] How would you choose and compare embedding models for a domain-specific corpus with specialized vocabulary?
- [RAG03-045] How would you use MTEB to choose an embedding model, and what are its limits?
- [RAG03-046] How do you benchmark and evaluate embedding model quality on your own data?
- [RAG03-047] Your domain is medical device manuals. How do you build an evaluation set for choosing an embedding model without human labelers?
- [RAG03-048] Which retrieval metrics (recall@k, MRR, nDCG) would you use to compare embedding models, and why is an average benchmark score not enough?
- [RAG03-049] A teammate proposes fixing weak RAG answers by upgrading to the largest available embedding model. What is the senior response?
- [RAG03-050] When is a self-hosted open-weights embedding model clearly better than a hosted API?
- [RAG03-051] Your embedding model silently truncates long inputs. How do you detect that and what do you do about it?
- [RAG03-052] How would you detect from production data alone that the index was built without the required document prefix?
- [RAG03-053] If the embedding instruction lives only on the query side, what can you tune without reindexing, and how would you test it?

## Dimensionality, Matryoshka and quantization
- [RAG03-054] What is the tradeoff of embedding dimensionality, and how does it affect quality, latency, memory and cost?
- [RAG03-055] What is a Matryoshka embedding, and why would you choose one for a billion-vector index?
- [RAG03-056] Why must you renormalize Matryoshka embeddings after truncating them?
- [RAG03-057] How would you combine Matryoshka truncation with int8 or binary quantization?
- [RAG03-058] You need to cut a 3072-dimensional embedding index in half without hurting recall. Walk through your options and how you would validate the choice.
- [RAG03-059] At what corpus scale does embedding dimensionality start to dominate your infrastructure bill?
- [RAG03-060] What is quantization of embeddings, and how does it reduce storage cost?
- [RAG03-061] What advantages does quantization offer over dimensionality reduction for scaling embeddings, and when is the reverse true?
- [RAG03-062] How do int8 and binary quantization reduce vector storage, and how much recall do you lose?
- [RAG03-063] What is binary quantization, and how does it differ from product quantization?
- [RAG03-064] Why does rescoring with full-precision vectors recover recall lost to quantization, and where do you keep those full-precision vectors?
- [RAG03-065] In semantic search over about 100M documents with binary-quantized embeddings and rescoring, how do you pick the rescoring depth empirically?
- [RAG03-066] Where does recall loss from binary-quantized retrieval show up in RAG quality metrics?
- [RAG03-067] At what point does the ANN index's RAM cost push you toward quantization?
- [RAG03-068] Sketch the memory math for 1B 768-dimensional vectors under float32, int8 and PQ-96. When would binary quantization with rescoring beat PQ?

## Fine-tuning and adapting embeddings
- [RAG03-069] When would you fine-tune your embedding model, and how would you actually do it?
- [RAG03-070] Your RAG system fails on domain-specific jargon. How do you fix it?
- [RAG03-071] After benchmarking an off-the-shelf embedding model, accuracy is low. How would you improve the accuracy of the embedding-based search?
- [RAG03-072] Walk me through the steps of improving a sentence-transformer model used for embedding.
- [RAG03-073] Why are hard negatives essential when fine-tuning an embedding model? What happens with only random negatives?
- [RAG03-074] How would you generate synthetic training queries for fine-tuning an embedder when you have no labelled data?
- [RAG03-075] Fine-tuned embedder versus fine-tuned reranker: how do you choose?
- [RAG03-076] When would you fine-tune an embedding model instead of the LLM?
- [RAG03-077] How do you avoid regressing on general queries after fine-tuning an embedding model on a narrow domain?
- [RAG03-078] What is a lightweight query-side adapter on frozen embeddings, and when is it preferable to full fine-tuning?

## Vector database fundamentals
- [RAG03-079] What is a vector database, and what does it store for LLM and RAG use?
- [RAG03-080] How does a vector database differ from a traditional database, and why not use a general-purpose database for vector search?
- [RAG03-081] What is the role of metadata stored alongside vectors?
- [RAG03-082] How does a vector database work, from ingestion to query?
- [RAG03-083] Explain the difference between a vector index, a vector database and a vector plugin.
- [RAG03-084] What is the difference between a vector library like FAISS and a full vector database like Milvus?
- [RAG03-085] How does a vector database handle inserts, updates and deletes (segments, tombstones, compaction)?
- [RAG03-086] How long after an insert does a new vector become searchable, and what consistency tradeoffs does that imply?
- [RAG03-087] How do you decide the best vector database for your needs? What criteria matter?
- [RAG03-088] Compare pgvector, dedicated vector stores and search engines as a vector backend.
- [RAG03-089] Why choose PostgreSQL with pgvector, and when should you switch to a dedicated vector database?
- [RAG03-090] Under what circumstances does a pgvector HNSW index degrade into a slower scan?
- [RAG03-091] How do you keep pgvector search fast while the same instance takes heavy writes?
- [RAG03-092] How would you choose between Pinecone and a self-hosted solution?
- [RAG03-093] A 4-person startup is launching a B2B RAG product with about 2M vectors per customer and a strict data-residency requirement. Should it build or buy the vector store?
- [RAG03-094] When is Elasticsearch's BM25 maturity worth its operational weight?
- [RAG03-095] What consistency bugs appear when the vector index is a separate system from the document store?
- [RAG03-096] How do you combine vector similarity with business conditions in a single query?

## ANN search and index algorithms
- [RAG03-097] When do you need approximate nearest neighbour search instead of exact search, and why is it acceptable for results to be inexact?
- [RAG03-098] You have a small dataset of customer reviews and perfect accuracy matters more than speed. Which search strategy would you choose and why?
- [RAG03-099] What are the different strategies for searching in a vector database or index? Compare tree-based, LSH and clustering-based ANN methods.
- [RAG03-100] Explain clustering in vector retrieval and how it reduces the search space.
- [RAG03-101] When does clustering-based pruning fail, and how can you mitigate those failures?
- [RAG03-102] Explain locality-sensitive hashing and its relation to k-NN.
- [RAG03-103] Explain the random projection index.
- [RAG03-104] Explain the concept of inverted indices in vector retrieval.
- [RAG03-105] Compare IVF, IVF-PQ and HNSW, and say when each fits.
- [RAG03-106] How do IVF centroids get trained, what does nprobe control, and what goes wrong with skewed clusters?
- [RAG03-107] Why does IVF need retraining as data drifts but HNSW does not?
- [RAG03-108] Explain how HNSW works, and what the layers and the M and ef parameters do.
- [RAG03-109] How do M, efConstruction and efSearch affect recall, latency and memory in HNSW?
- [RAG03-110] Explain how HNSW works and when you would not use it.
- [RAG03-111] What is the difference between HNSW and IVFFlat?
- [RAG03-112] How do you tune HNSW's ef_search, and what happens when it is increased or decreased?
- [RAG03-113] How would you tune HNSW M and ef differently for a 99%-recall offline job versus a 20ms-p99 online API?
- [RAG03-114] Your retriever's recall@20 is stuck at 0.86 and tuning chunking has not moved it. You are on HNSW with default parameters. What is worth trying first?
- [RAG03-115] What happens to search quality after deleting 40% of vectors from an HNSW index?
- [RAG03-116] Your p99 latency doubled after deleting 30% of vectors from the index. What happened?
- [RAG03-117] Why do graph indexes like HNSW use more memory than IVF, and how do their build times and update behaviour compare?
- [RAG03-118] Explain product quantization: how does it compress vectors, and what error does it introduce?
- [RAG03-119] What is DiskANN, and when would you choose a disk-based index over a RAM-based one like HNSW?
- [RAG03-120] What is ScaNN, and how does it differ fundamentally from IVF-PQ and HNSW?
- [RAG03-121] How does FAISS implement efficient approximate nearest neighbour search?
- [RAG03-122] Compare flat, HNSW and IVF-PQ indexes. How do you pick, and what does recall@k cost in latency?
- [RAG03-123] Given a project scenario, compare vector indexes and explain which one you would use and why.
- [RAG03-124] How exactly would you measure the recall your ANN index achieves?
- [RAG03-125] How do you read a recall-versus-QPS benchmark curve when comparing ANN libraries?
- [RAG03-126] How do you monitor and tune a vector index in production for recall and latency?

## Filtering, multi-tenancy and access control
- [RAG03-127] Explain pre-filtering versus post-filtering in a vector database and the challenges of each.
- [RAG03-128] Why does a highly selective metadata filter hurt HNSW specifically?
- [RAG03-129] Why is metadata filtering often the bottleneck in vector databases? What do in-graph filtering and brute-force fallback do?
- [RAG03-130] A post-filtered ANN query with an ACL filter returns fewer than k results. Why, and how do you fix it?
- [RAG03-131] Your queries use a tenant filter with 5% selectivity. How does that change your vector database choice?
- [RAG03-132] How do you handle multi-tenancy in a vector database: namespaces, per-tenant indexes, or row-level security?
- [RAG03-133] In a multi-tenant RAG system, why not use one vector database or index per tenant?
- [RAG03-134] Design indexing for 10k tenants where the largest has 10M vectors and the median has 5k. How does the DB choose between filtered ANN and brute force, and what would a cost model look at?
- [RAG03-135] How do you enforce document-level permissions and right-to-be-forgotten requests in a vector store?

## Scaling, sharding and capacity
- [RAG03-136] Your RAG retrieval is too slow with a large knowledge base. How do you speed it up?
- [RAG03-137] Your vector database cannot scale to millions of embeddings. How do you find and fix the bottleneck?
- [RAG03-138] If vector data grows from 1 million to 100 million, what architectural changes are needed?
- [RAG03-139] How does a vector database search billions of vectors in milliseconds?
- [RAG03-140] How would you size the index for 50M chunks of 1,536-dimensional embeddings on HNSW?
- [RAG03-141] Your vector database for RAG is consuming too much memory. How do you reduce it?
- [RAG03-142] You are serving 50M chunks and the index will not fit in your RAM budget. Which move shrinks the footprint without re-embedding the corpus?
- [RAG03-143] You must serve 800M vectors on a tight RAM budget. Which index choice fits, and what is the cost?
- [RAG03-144] What embedding dimension, index and rerank depth would you choose for a retrieval system over millions of chunks?
- [RAG03-145] How do you plan capacity for a vector index with hundreds of millions of vectors, including memory tiers and replicas?
- [RAG03-146] Your vector index will not fit on one machine. How do you shard it, and what breaks?
- [RAG03-147] With 20 shards and scatter-gather queries, how do you keep p99 from being dominated by the slowest shard?
- [RAG03-148] In sharded vector search, how much do you over-fetch per shard, and how would you determine that number?
- [RAG03-149] When do you add replicas versus shards in a vector search cluster?
- [RAG03-150] How do you keep multi-vector (ColPali-style) storage from exploding at 5M pages?
- [RAG03-151] When embedding millions of chunks through an embedding service, the service starts returning 429s. How does the batcher adapt?
- [RAG03-152] How do you design an embedding service for large-scale RAG with cost optimization?

## Embedding drift, re-embedding and migration
- [RAG03-153] What is embedding drift, and how do you handle it when the embedding model is updated?
- [RAG03-154] What causes semantic drift in embedding search, and how do you detect it?
- [RAG03-155] What breaks when you change embedding models and forget to re-embed the corpus?
- [RAG03-156] You push vectors from an upgraded embedding model into the existing live index alongside the old ones. What happens?
- [RAG03-157] Your new embedding model has different dimensions from the vectors in production. How do you handle the mismatch?
- [RAG03-158] You must upgrade the embedding model behind a 500M-vector index. How do you roll it out with zero downtime?
- [RAG03-159] A better embedding model ships and you have 400M chunks indexed. How do you decide whether the reindex is worth it?
- [RAG03-160] During an embedding migration, what breaks if the dual-write window has a gap and some documents exist only in the old index?
- [RAG03-161] A re-embedding backfill of 200M vectors is 60% done when the provider deprecates the old model's endpoint. What now?
- [RAG03-162] How do you version a RAG pipeline so you can re-embed safely when you change the embedding model?
- [RAG03-163] In a similarity-search system, what breaks when you swap the embedding encoder for a better one?
- [RAG03-164] How would you migrate a vector database without downtime or retrieval regression?
- [RAG03-165] How do you back up a vector index, and how long would a rebuild after a crash take for 100M vectors?

## Additional questions
- [RAG03-166] How does LangChain handle embeddings and vector stores?
