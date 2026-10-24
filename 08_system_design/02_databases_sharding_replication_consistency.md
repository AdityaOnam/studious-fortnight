---
domain: sd
topic: databases_sharding_replication_consistency
title: Databases, sharding, replication, consistency
tags: [sharding, replication, consistency, nosql]
count: 164
---
# Databases, sharding, replication, consistency

## Choosing a database
- [SD02-001] What is the difference between SQL and NoSQL databases?
- [SD02-002] What are the main differences between relational and non-relational databases?
- [SD02-003] What advantages do NoSQL databases offer for managing large data volumes, and what do they give up?
- [SD02-004] Compare SQL and NoSQL databases in terms of schema, scaling model, consistency guarantees and query capabilities.
- [SD02-005] When would you pick a relational database over a NoSQL store, and when the reverse?
- [SD02-006] How do you decide between SQL and NoSQL for a new service? Which questions about data and access patterns drive the decision?
- [SD02-007] What is polyglot persistence, and what operational costs does it introduce?
- [SD02-008] What are common database scaling strategies, and at what point do you reach for each one?
- [SD02-009] How do you decide between scaling a single PostgreSQL-style database up and moving to a distributed database?
- [SD02-010] A startup's single Postgres instance is at 70% CPU and growing. What would you try before sharding, and in what order?
- [SD02-011] What is a serverless database, and what trade-offs come with it compared with a provisioned cloud database?
- [SD02-012] What does a multi-model database offer, and what are its trade-offs?
- [SD02-013] Compare data lakes, data warehouses and operational databases. When is each used?
- [SD02-014] Why can the database become the bottleneck in a write-heavy system, and what options do you have: queues, LSM engines, sharding, batching?
- [SD02-015] How would you design the database layer for a large-scale application, starting from requirements and access patterns?
- [SD02-016] How would you separate analytical queries from the transactional database so reporting does not hurt production latency?

## NoSQL models and data modelling for scale
- [SD02-017] What are the main types of NoSQL databases, and what is a typical use case for each?
- [SD02-018] Compare relational, document, key-value, wide-column, graph and time-series databases, and give a good use case for each.
- [SD02-019] How do NoSQL databases achieve horizontal scalability?
- [SD02-020] How does data modelling in NoSQL databases differ from relational modelling?
- [SD02-021] In a document database, when do you embed related data and when do you reference it?
- [SD02-022] Why does a wide-column store such as Cassandra force you to model tables around queries, and why is partition key design so important?
- [SD02-023] What is the role of an index in a NoSQL store compared with an RDBMS?
- [SD02-024] What is schema-on-write versus schema-on-read, and what are the pros and cons of flexible schemas?
- [SD02-025] Compare document, key-value and wide-column databases for storing user activity feeds.
- [SD02-026] When would you deliberately denormalize a schema, and what consistency burdens does that create?
- [SD02-027] What are materialized views, and when would you use them for read-heavy dashboards?
- [SD02-028] What is a star schema, and when would you use it?
- [SD02-029] What are the pros and cons of foreign keys and cascading deletes at large scale?
- [SD02-030] What are the main data management approaches in a microservice architecture: database per service, shared database, API composition?
- [SD02-031] How do you run queries that span several services' data without distributed joins?
- [SD02-032] How would you isolate tenants in a multi-tenant SaaS database: shared schema, schema per tenant, or database per tenant?
- [SD02-033] How would you change the schema of a table with billions of rows in production without downtime?
- [SD02-034] How would you store trillions of chat messages so that reading the recent messages of a conversation stays fast as data grows?
- [SD02-035] How would you model and index photo tags to efficiently answer both "photos where user X is tagged" and "who is tagged in photo Y"?
- [SD02-036] How would you store and update a per-user set of senders with new messages so updates are real time and reads are very cheap?
- [SD02-037] What non-traditional storage approaches suit a read-heavy, rarely updated dictionary service, and how would you roll out weekly updates safely?

## Replication and read scaling
- [SD02-038] What is database replication, how does it work, and why is it useful?
- [SD02-039] What are the two fundamental techniques of replication and partitioning, and what problem does each solve?
- [SD02-040] What is read-write splitting, and how is it typically implemented?
- [SD02-041] How does leader-follower (master-slave) replication work in a relational database, and what is replication lag?
- [SD02-042] Compare single-leader, multi-leader and leaderless replication. When would you use each?
- [SD02-043] Compare master-slave and master-master replication, including what happens when the primary fails.
- [SD02-044] Compare synchronous, semi-synchronous and asynchronous replication in terms of durability, latency and availability.
- [SD02-045] How do statement-based, row-based (logical) and physical log-shipping replication differ?
- [SD02-046] What happens to acknowledged writes if the master fails before replicating them, and how do you fail over and promote a replica safely?
- [SD02-047] What is split brain after a failover, and how do you prevent it?
- [SD02-048] How would you route reads and writes to primary and replicas: in application code or through database middleware?
- [SD02-049] Describe the read replica pattern and how you would implement it.
- [SD02-050] What causes replication lag, and how can you reduce it?
- [SD02-051] How do you avoid users reading stale data after a write when using read replicas?
- [SD02-052] A user places an order and immediately cannot see it because the read hit a lagging replica. What are several ways to fix this?
- [SD02-053] Followers lag by several minutes during peak write traffic. How do you investigate and fix it?
- [SD02-054] What trade-offs come with replicating a database across regions for latency and disaster recovery?

## Sharding and partitioning
- [SD02-055] What is database sharding, and why is it used?
- [SD02-056] What is the difference between sharding, partitioning and replication?
- [SD02-057] Compare horizontal and vertical partitioning (sharding) of a database or table.
- [SD02-058] When do you need to shard, and what should you try before doing so?
- [SD02-059] Compare hash-based, range-based, list-based, directory-based and composite sharding. How does each handle hot spots and rebalancing?
- [SD02-060] What are the main data sharding algorithms, and how do they differ in rebalancing cost?
- [SD02-061] How do you choose a shard key, and what makes a bad one?
- [SD02-062] How would you choose a shard key for a social app so that common queries stay on one shard and no shard becomes a hot spot?
- [SD02-063] How does a query execute in a sharded database, and how is it routed: client-side, proxy-based or via a coordinator?
- [SD02-064] What happens if a query does not provide the shard key in a sharded database?
- [SD02-065] What is database federation, and when would you split databases by function?
- [SD02-066] What problems appear after sharding (cross-shard joins, distributed transactions, global IDs, pagination, resharding), and how do you handle each?
- [SD02-067] How would you support queries on a non-shard-key column, such as a global secondary index, in a sharded database?
- [SD02-068] What is table partitioning within a single database node, and how do partition pruning and dropping old partitions help?
- [SD02-069] How would you partition data when a single user's data may grow unbounded or one entity becomes a hot key?
- [SD02-070] How would you detect and mitigate a hot shard in production?
- [SD02-071] When would you shard by tenant, by user or by geography, and what are the data locality and compliance implications?
- [SD02-072] How would you add shards to a hash-sharded database without remapping all data?
- [SD02-073] You must reshard from 8 to 16 shards with no downtime. Describe a safe approach.
- [SD02-074] How would you migrate a large live database from a single instance to a sharded layout with zero downtime?
- [SD02-075] How would you shard a SQL-backed key-value store and handle rebalancing when you add shards?

## Global IDs, hot spots and hot/cold data
- [SD02-076] How do you generate unique row IDs across shards? Compare auto-increment, UUID, Snowflake, database segments and Redis counters.
- [SD02-077] Design a unique ID generator that works across many machines with roughly sortable IDs. What happens if a clock moves backwards?
- [SD02-078] Why can random UUIDs as primary keys hurt database insert performance?
- [SD02-079] What is hot and cold data separation, and what are its benefits and costs?
- [SD02-080] How do you migrate cold data out of a hot database while keeping consistency, and how can you roll back?
- [SD02-081] How do you route queries between hot and cold storage in the application and keep cold queries acceptable?
- [SD02-082] How does cold-hot separation differ from archiving and from table partitioning?
- [SD02-083] Design the storage for an order system that must keep five years of orders while most queries target the last three months.
- [SD02-084] What is a hotspot account in a payment system, and how can you increase throughput on it?
- [SD02-085] Why would you split a hot balance into sub-accounts or use a cache-first balance, and what risks does each introduce?
- [SD02-086] Compare pessimistic locking, optimistic concurrency control and a single-writer queue for assigning each seat to exactly one passenger under heavy concurrency.
- [SD02-087] How would you protect the database from a burst of purchase attempts in a flash sale while guaranteeing no overselling?
- [SD02-088] How would you handle celebrity accounts with millions of followers in a follow-graph design?
- [SD02-089] How would you implement a like or view counter updated by millions of clients without creating a hot row?

## Consistency models: ACID vs BASE
- [SD02-090] What do ACID and BASE mean, and what is the trade-off between them?
- [SD02-091] What is the difference between strong consistency and eventual consistency?
- [SD02-092] Compare strong, weak and eventual consistency and give an example of a system suited to each.
- [SD02-093] Explain eventual consistency and its role in NoSQL databases.
- [SD02-094] What are read-your-writes, monotonic reads and causal consistency, and how can you provide them over eventually consistent storage?
- [SD02-095] What are common patterns for achieving eventual consistency in practice, such as event-based sync, background reconciliation, saga and CQRS?
- [SD02-096] Describe the consistency models available in NoSQL databases and how they handle transactions and conflict resolution.
- [SD02-097] How do quorum reads and writes (R + W > N) give tunable consistency in a replicated store, and what are the failure cases?
- [SD02-098] How are write conflicts resolved in multi-leader or leaderless systems: last-write-wins, vector clocks, CRDTs?
- [SD02-099] How do read repair and anti-entropy with Merkle trees keep replicas converged?
- [SD02-100] Which consistency level would you choose for a shopping cart, a bank transfer and a social feed, and why?
- [SD02-101] How do globally distributed SQL databases such as Spanner provide strong consistency across shards, and what latency cost do they pay?

## Indexing and query performance at scale
- [SD02-102] How do database indexes speed up reads, and what do they cost on writes and storage?
- [SD02-103] What is the difference between dense and sparse indexes?
- [SD02-104] Compare B-tree indexes with LSM-tree based storage for read-heavy and write-heavy workloads.
- [SD02-105] When does a composite index beat several single-column indexes, and how does the leftmost prefix rule apply?
- [SD02-106] What are the costs of over-indexing, redundant indexes and indexing frequently updated columns?
- [SD02-107] What situations cause an index to be ignored, such as functions on columns, implicit type conversion or leading wildcards?
- [SD02-108] When is a prefix index on a string column useful, and what are its limitations?
- [SD02-109] What is a covering index, and when does it help avoid table lookups?
- [SD02-110] In a partitioned database, what is the difference between local and global secondary indexes, and what are the trade-offs?
- [SD02-111] When are joins acceptable, and what makes a join expensive on large tables?
- [SD02-112] What is the N+1 query problem, and how do you detect and fix it?
- [SD02-113] How do you diagnose and optimize a slow SQL query using execution plans?
- [SD02-114] Why is deep pagination with LIMIT and a large OFFSET slow in a relational database?
- [SD02-115] Compare cursor-based pagination, subquery, deferred join and covering index approaches for deep pagination.
- [SD02-116] How would you add an index to a billion-row production table without blocking traffic?
- [SD02-117] A query that was fast at 10 million rows is slow at 1 billion rows. What has changed and how do you investigate?
- [SD02-118] Why do large fleets of application servers need connection pooling or a database proxy, and what happens when connections are exhausted?

## Search indexes and data synchronisation
- [SD02-119] How does an inverted index work, and how does a search engine use it to answer queries?
- [SD02-120] How would you update an inverted index incrementally as new documents arrive?
- [SD02-121] How does TF-IDF scoring work, and what are its weaknesses compared with BM25?
- [SD02-122] How would you implement typo-tolerant search using edit distance, n-grams or a BK-tree, and what are the performance trade-offs?
- [SD02-123] How do you measure and tune search relevance?
- [SD02-124] What are the top use cases of Elasticsearch, and what makes it a poor primary store?
- [SD02-125] What are the pros and cons of a full-text search engine versus database indexes for search queries?
- [SD02-126] How is a search index partitioned across nodes: by document or by term, and what are the query-time trade-offs?
- [SD02-127] How do you paginate deeply through search results without the cost of large offsets?
- [SD02-128] How does change data capture work, and what problems does it solve for keeping caches, search indexes and warehouses in sync?
- [SD02-129] How would you keep an Elasticsearch index in sync with a MySQL database? Compare dual writes, scheduled sync and binlog CDC, and cover full sync, incremental sync and reconciliation.
- [SD02-130] What delivery and ordering guarantees must a database-to-search-index sync provide, and how do you handle deletes, retries and backfills?
- [SD02-131] What is the dual-write problem when updating a database and another system, and how does the transactional outbox pattern solve it?
- [SD02-132] How would you reindex a large search index with a new mapping without downtime?

## Time-series, graph, geo and key-value stores
- [SD02-133] What is a time-series database, and how is it different from a relational database for metrics and monitoring workloads?
- [SD02-134] How do time-series databases handle downsampling, retention and high-cardinality tags?
- [SD02-135] When is a graph database a better choice than a relational database with join tables?
- [SD02-136] Compare adjacency lists in a relational store, a graph database and a key-value store for follower/following queries, and how you would shard them.
- [SD02-137] Why might a large social network build a dedicated graph store instead of using a look-aside cache over sharded MySQL?
- [SD02-138] How would you design a graph-aware cache layer that supports read-after-write consistency across multiple data centers?
- [SD02-139] How are restaurant locations stored so that a location-based service can return nearby restaurants efficiently?
- [SD02-140] Compare geohash, quadtree and S2/H3 cell indexes for proximity search, including boundary issues and hot cells.
- [SD02-141] How would you handle frequently changing user locations in a nearby-search index without constant index rewrites?
- [SD02-142] Design a key-value store on top of a relational database supporting get, put, delete and TTL, at 1 million concurrent transactions and petabytes of data.
- [SD02-143] How would you implement key expiry efficiently in a SQL-backed key-value store so expired keys are deleted without scanning the full table?
- [SD02-144] Design a single-node persistent key-value store with O(1) get, put and delete whose values do not fit in memory. How do you recover the index after a crash?
- [SD02-145] How does a log-structured hash index like Bitcask handle writes, reads, deletes and compaction, and what are its limitations?
- [SD02-146] How would you handle compaction, crash recovery and key-space limits in a single-node log-structured key-value store?
- [SD02-147] How would you make a single-node persistent key-value store faster than a log-structured hash index, and what hardware or I/O techniques would you use?
- [SD02-148] What trade-offs do memory-mapped files, direct I/O and batched fsync introduce for the latency and durability of a key-value store?

## Blob storage and file systems
- [SD02-149] What is an object store?
- [SD02-150] What is the difference between object, block and file storage, and what are the use cases and limits of each?
- [SD02-151] What are the top use cases of object stores such as S3, and what are they bad at?
- [SD02-152] What is RAID, and how do RAID 0, 1, 5, 6 and 10 trade off capacity, performance and fault tolerance?
- [SD02-153] What are HDFS and its design assumptions, and when is a distributed file system appropriate?
- [SD02-154] How would you upload a very large file to an object store, and how do you optimize its performance?
- [SD02-155] What happens under the hood when you upload a file to an object store such as Amazon S3?
- [SD02-156] Why do clients often upload directly to object storage using pre-signed URLs instead of going through application servers?
- [SD02-157] What are best practices for file metadata and lifecycle management in a storage system?
- [SD02-158] How do you store and serve large binary assets such as photos or videos, and why not store the blobs in the relational database?
- [SD02-159] How would you reduce the metadata overhead of storing billions of small photos on a file system?
- [SD02-160] Design a scalable blob storage service like Amazon S3 with seamless scaling, durability under node failures, multi-tenancy and geographic redundancy.
- [SD02-161] How would you achieve high durability in an object store using replication versus erasure coding, and what are the cost trade-offs?
- [SD02-162] How would you detect and handle data corruption in transit and at rest in a distributed object store?
- [SD02-163] How would you handle hot storage nodes and rebalance data when adding capacity in an object store?
- [SD02-164] How would you design the metadata service and bucket/object namespace for an S3-like storage system?
