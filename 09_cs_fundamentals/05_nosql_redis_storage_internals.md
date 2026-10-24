---
domain: cs
topic: nosql_redis_storage_internals
title: NoSQL, Redis and storage internals
tags: [nosql, redis, mongodb, lsm]
count: 162
---
# NoSQL, Redis and storage internals

## NoSQL models and trade-offs
- [CS05-001] What are the main types of NoSQL databases? Give an example system and a typical use case for each.
- [CS05-002] How does a key-value store work, and what is a good use-case example?
- [CS05-003] How is a document in a document-oriented database different from a row in a relational database?
- [CS05-004] What kinds of applications are a typical fit for a document-oriented database?
- [CS05-005] Can you use SQL or SQL-like queries with NoSQL databases?
- [CS05-006] How does indexing work in document-oriented databases?
- [CS05-007] When would you choose a NoSQL database over a relational one, and when would you stay relational?
- [CS05-008] What strategies can you use to scale a key-value store for high demand or very large data volumes?
- [CS05-009] What are the drawbacks of key-value stores compared with other NoSQL types, and when are they a poor fit?
- [CS05-010] How do you model many-to-many relationships and query-driven access patterns in a NoSQL store that has no joins?
- [CS05-011] What is BASE, and how does eventual consistency differ from the ACID guarantees of a relational database?
- [CS05-012] Explain how Cassandra, MongoDB and DynamoDB each position themselves on the CAP and PACELC trade-offs.

## MongoDB data model, indexes and queries
- [CS05-013] What is MongoDB, and how is data organised into databases, collections, documents and BSON? What role does the _id field play?
- [CS05-014] How does MongoDB differ from a relational database such as MySQL?
- [CS05-015] What are indexes in MongoDB and why are they used?
- [CS05-016] Which index types does MongoDB support (single field, compound, multikey, text, geospatial, TTL), and when would you use a TTL index?
- [CS05-017] Does field order matter in a MongoDB compound index, and does the left-prefix rule apply?
- [CS05-018] What is a covered query in MongoDB and what conditions must hold for it?
- [CS05-019] What kinds of applications suit MongoDB, and which do not?
- [CS05-020] What business scenarios are MongoDB and Elasticsearch each best suited for?
- [CS05-021] When should you embed related data in a MongoDB document versus reference it?
- [CS05-022] What is the MongoDB aggregation pipeline, and which stages would you use to build a report?
- [CS05-023] How would you use explain() to diagnose a slow MongoDB query, and what plan stages are red flags?
- [CS05-024] What is the equality-sort-range guideline for ordering fields in a compound index?
- [CS05-025] What goes wrong when documents contain unbounded arrays or approach the 16 MB limit, and how do you redesign them?

## MongoDB storage engine, replication and sharding
- [CS05-026] Is WiredTiger based on an LSM tree or a B+ tree, and what does that imply for read and write performance?
- [CS05-027] How does MongoDB compress data on disk, and what are the trade-offs between compression algorithms?
- [CS05-028] How do WiredTiger journaling, checkpoints and document-level concurrency work?
- [CS05-029] Does MongoDB support multi-document transactions, and what are their costs and limitations?
- [CS05-030] How do replica sets provide high availability and disaster recovery, and how do elections work?
- [CS05-031] What do read concern and write concern each control in MongoDB?
- [CS05-032] What is the oplog, and how does it support replication and secondary lag?
- [CS05-033] How does sharding work in MongoDB, how do you choose a shard key, and what happens with a poor choice?
- [CS05-034] With w:1 writes and a primary failover, which writes can be lost or rolled back, and how does w:majority change that?
- [CS05-035] A MongoDB shard is overloaded while others are idle. How do you diagnose it and what fixes are available?

## Redis data types and internals
- [CS05-036] What is Redis, how does it store data, and what are its main use cases beyond caching?
- [CS05-037] Which data types does Redis support, and what is a typical use case for each?
- [CS05-038] What are hashes and lists in Redis, and what common operations do they support?
- [CS05-039] How should you design Redis keys for clarity and performance, and what production conventions would you adopt?
- [CS05-040] Should you store object data in Redis as a serialized String or as a Hash? Compare the trade-offs.
- [CS05-041] Would you store a shopping cart as a String or a Hash in Redis? Justify the design.
- [CS05-042] Compare Redis and Memcached in data types, persistence, threading, clustering and memory management. When is Memcached the better choice?
- [CS05-043] Why use a distributed cache like Redis instead of a local in-process cache, and what are the trade-offs?
- [CS05-044] How is the Redis String implemented (SDS), and why not use plain C strings?
- [CS05-045] Which internal encodings does Redis use for small versus large lists, hashes, sets and sorted sets, and why switch between them?
- [CS05-046] How does Redis implement its dictionary, and how does incremental rehashing avoid long pauses?
- [CS05-047] How does a skip list work, including search, insertion and probabilistic level assignment?
- [CS05-048] Why does a Redis sorted set use a skip list instead of a balanced tree, red-black tree or B+ tree?
- [CS05-049] Why is Redis so fast even though it executes commands on a single thread?
- [CS05-050] Explain the Redis event loop: file events, time events and I/O multiplexing.
- [CS05-051] How did Redis threading change in version 6.0, and which work was parallelised?
- [CS05-052] Why did Redis avoid multithreaded command execution for so long, and which background threads does it have?
- [CS05-053] How has Redis evolved from a single node to persistence, replication, Sentinel and Cluster?
- [CS05-054] What are Redis Modules, and what capabilities such as search or Bloom filters do they add?
- [CS05-055] What causes Redis memory fragmentation, how do you detect it from INFO, and how can you reduce it?
- [CS05-056] Roughly how much memory would 100 million small string keys need in Redis, and which overheads dominate?

## Redis persistence, expiration and eviction
- [CS05-057] How does Redis persist data to disk?
- [CS05-058] Compare RDB snapshots and AOF logging in durability, recovery time, file size and performance impact.
- [CS05-059] Do SAVE and BGSAVE block the main thread? How do fork and copy-on-write work, and what risks do they pose to latency and memory?
- [CS05-060] Why does Redis AOF log commands after executing them rather than before, and what are the consequences?
- [CS05-061] Compare the AOF fsync policies always, everysec and no. What data can each lose?
- [CS05-062] What is AOF rewrite, why is it needed, and how does it avoid blocking clients?
- [CS05-063] What are the differences between RDB, AOF, AOF rewrite and hybrid persistence, and what problem does hybrid solve on restart?
- [CS05-064] How would you choose between RDB, AOF or both for a given workload, and what do you monitor in production?
- [CS05-065] How does Redis detect and recover from a truncated or corrupted AOF file?
- [CS05-066] How do very large keys affect Redis persistence, replication and latency?
- [CS05-067] How do you set an expiration on a Redis key, and why do cached keys need TTLs?
- [CS05-068] Compare lazy deletion and periodic deletion of expired keys in Redis. What are the weaknesses of each?
- [CS05-069] What happens when many keys expire at the same time, and how do you avoid it?
- [CS05-070] Which eviction policies does Redis offer when memory is full, and how do you choose among LRU, LFU and TTL-based policies?
- [CS05-071] How does Redis approximate LRU instead of maintaining an exact LRU list, and why?
- [CS05-072] When would LFU eviction beat LRU, for example with scan-heavy workloads?
- [CS05-073] How are expired keys handled on replicas and in the AOF and RDB files?
- [CS05-074] Can Redis safely be used as a primary database? Which durability and memory limits matter?

## Redis replication, Sentinel and Cluster
- [CS05-075] How does Redis master-replica replication work, from full sync to partial resync and command propagation?
- [CS05-076] What is the difference between Redis master-replica replication, Sentinel and Cluster?
- [CS05-077] What does Sentinel do in a Redis deployment, and how does it handle failover?
- [CS05-078] How is the leader elected among Sentinels during a failover?
- [CS05-079] How does Redis Cluster shard data with hash slots, and what happens during resharding or node failure?
- [CS05-080] Why does Redis Cluster have 16384 hash slots?
- [CS05-081] What are the trade-offs between Redis Cluster, Sentinel and client-side sharding?
- [CS05-082] How do hash tags let you run multi-key operations in Redis Cluster, and what is the downside?
- [CS05-083] Under asynchronous replication, how would you handle a master failure that loses the most recent writes?
- [CS05-084] Is it safe to read from Redis replicas? What staleness can occur?
- [CS05-085] Can Redis Sentinel failover guarantee RPO=0? What role does the quorum play in the election?
- [CS05-086] How does a Redis network partition cause split brain, and how do min-replicas-to-write and similar settings limit data loss?
- [CS05-087] How does Redis Cluster detect failed nodes with gossip (PFAIL versus FAIL) and promote a replica?
- [CS05-088] A replica keeps falling into repeated full resynchronisations. What are the likely causes and fixes?

## Redis use cases: transactions, queues, locks and counting
- [CS05-089] How would you implement a simple counter in Redis, and how do you handle atomic operations in general?
- [CS05-090] What guarantees do MULTI/EXEC transactions give? Are they atomic or durable, and how do they differ from relational ACID transactions?
- [CS05-091] How do WATCH and Lua scripts address the limitations of Redis transactions?
- [CS05-092] What is pipelining in Redis, when would you use it, and what are its limits in cluster mode?
- [CS05-093] How would you use Redis as a counter, message queue, session cache and lookup table, and what are the limits of each?
- [CS05-094] How would you implement a leaderboard, and which Redis structures would you use for leaderboards, rate limiters and queues?
- [CS05-095] How would you use Sets for a lottery or de-duplicated likes, and combine sorted sets for a forum's votes and ranking?
- [CS05-096] How can a Bitmap count daily active users or track check-ins, and what are its memory characteristics?
- [CS05-097] What is HyperLogLog, what error rate does it have, and how would you count unique page visitors with it?
- [CS05-098] How would you check whether an element is definitely not in a huge set using Redis, and what are the trade-offs of the options?
- [CS05-099] How does Redis GEO store locations and answer nearby-search queries?
- [CS05-100] How would you design a rate limiter using Redis atomic operations and expiry?
- [CS05-101] Explain the Pub/Sub model in Redis, how it can power a simple chat application, and what its delivery guarantees are.
- [CS05-102] Can Redis be used as a message queue? Compare Lists, Pub/Sub and Streams.
- [CS05-103] What problems do Redis Streams solve compared with Lists and Pub/Sub, and how do consumer groups provide acknowledgement?
- [CS05-104] When would you choose Redis Streams, Kafka or a database table to implement a job queue?
- [CS05-105] How would you implement delayed tasks with Redis? Compare sorted sets, key-expiry notifications and delay-queue libraries.
- [CS05-106] How would you implement a distributed lock with Redis, and what pitfalls exist around expiry, ownership and clock drift?
- [CS05-107] A Redis lock expires while the holder is still working. How do you prevent this, and what do a watchdog and a fencing token do?
- [CS05-108] What are the criticisms of Redlock for distributed locking, and when is it not safe enough?
- [CS05-109] How do you make Redis Streams consumers handle crashes and avoid lost or duplicate processing?
- [CS05-110] Why can Lua scripts cause problems in Redis Cluster or for latency, and how do you avoid them?

## Redis production issues and caching problems
- [CS05-111] What is a big key in Redis, what harm does it cause, and how do you find and fix it?
- [CS05-112] What is a hot key, and how do you detect and mitigate it when a single key receives a huge fraction of traffic?
- [CS05-113] What are Redis slow queries, which commands are risky (KEYS, HGETALL, SMEMBERS), and what are the safe alternatives?
- [CS05-114] Redis latency suddenly spikes. List possible blocking causes (O(n) commands, persistence, swap, big keys, network, CPU contention) and how you would diagnose each.
- [CS05-115] Why can FLUSHALL or deleting a huge key block Redis, and what does lazy free (UNLINK) change?
- [CS05-116] How can swap and CPU contention with other processes affect Redis latency?
- [CS05-117] Which metrics from the INFO command would you alert on in production?
- [CS05-118] Redis hits maxmemory in production and writes start failing. How do you triage and fix it?
- [CS05-119] Compare cache-aside, write-through and write-back caching patterns.
- [CS05-120] What is cache penetration, and what are the solutions (null caching, Bloom filter, validation)?
- [CS05-121] What is a cache breakdown (hot key expiry), and how do you prevent a stampede on a single key?
- [CS05-122] What is a cache avalanche, and how do you protect the database from it?
- [CS05-123] How does cache warming help avoid a cold-start load spike on the database?
- [CS05-124] Your cache hit ratio drops from 95% to 80% after a release. How do you investigate?
- [CS05-125] How do you keep the cache and database consistent? Compare update-then-delete, delete-then-update and delayed double delete.
- [CS05-126] Design a cache consistency mechanism using binlog subscription or message queues. What failure scenarios remain?

## LSM trees, WAL and storage engine internals
- [CS05-127] What is a write-ahead log, and why do databases use one?
- [CS05-128] How do WAL, checkpoints and replay enable crash recovery?
- [CS05-129] What is an LSM tree, and how does it differ from a B+ tree for write-heavy workloads?
- [CS05-130] Describe the LSM write path and read path: memtable, WAL, SSTables, flush and lookup.
- [CS05-131] Compare leveled and size-tiered compaction in terms of write, read and space amplification.
- [CS05-132] How are deletes handled in an LSM tree, and why can tombstones hurt read performance?
- [CS05-133] Why do B+ trees suffer on random writes, and what happens during a page split?
- [CS05-134] How does a Bloom filter work, and what false-positive and false-negative properties does it have?
- [CS05-135] How do you size a Bloom filter for an expected number of elements and a target false-positive rate?
- [CS05-136] Why can items not be deleted from a standard Bloom filter, and how do counting Bloom filters or cuckoo filters help?
- [CS05-137] Where are Bloom filters useful in databases and caches, such as LSM reads or cache-penetration protection?
- [CS05-138] How do object, block and file storage differ in how data is addressed?
- [CS05-139] What is group commit, and how does fsync policy trade durability against throughput?
- [CS05-140] What causes write stalls in an LSM engine such as RocksDB, and how would you tune compaction to avoid them?
- [CS05-141] Design an embedded LSM-based key-value store like RocksDB. What components and write and read paths are needed?
- [CS05-142] Would you pick an LSM-based or B+ tree-based engine for a write-heavy time-series ingest versus a read-heavy OLTP workload? Why?

## Cassandra, DynamoDB, search, graph and analytical stores
- [CS05-143] How do wide-column stores like Cassandra achieve high write throughput and tunable consistency?
- [CS05-144] In Cassandra, what are the partition key and clustering key, and how do you design a table around a query?
- [CS05-145] How do Cassandra quorum reads and writes work, and when does R + W > N give strong consistency?
- [CS05-146] How do hinted handoff, read repair and anti-entropy repair keep Cassandra replicas consistent?
- [CS05-147] Why do tombstones and very wide partitions cause trouble in Cassandra, and how do you avoid them?
- [CS05-148] In DynamoDB, how do you choose partition and sort keys, and what is a hot partition?
- [CS05-149] When would you use a global secondary index versus a local secondary index in DynamoDB?
- [CS05-150] What are the trade-offs of single-table design in DynamoDB?
- [CS05-151] Why can an inverted index make full-text search faster than a B+ tree index in a relational database?
- [CS05-152] Why use Elasticsearch alongside MySQL, and what consistency guarantees does the search index lose compared with the primary store?
- [CS05-153] How do Elasticsearch shards, replicas and Lucene segments work, and why is search only near-real-time?
- [CS05-154] Why is deep pagination expensive in Elasticsearch, and what alternatives exist?
- [CS05-155] When is a graph database a better fit than a relational one, and what does index-free adjacency mean?
- [CS05-156] How do row-oriented and column-oriented storage differ, and why do column stores suit analytics?
- [CS05-157] How do column stores use compression and vectorised execution to speed up scans?
- [CS05-158] What is OLAP used for, and how does it differ from OLTP?
- [CS05-159] What are measures and dimensions in OLAP, and what are levels within a dimension?
- [CS05-160] What are fact tables and dimension tables in OLAP?
- [CS05-161] Compare star and snowflake schemas in a data warehouse.
- [CS05-162] What is a data warehouse, and how does it differ from a data lake?
