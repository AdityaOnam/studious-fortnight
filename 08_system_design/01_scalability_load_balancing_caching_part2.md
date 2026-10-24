---
domain: sd
topic: scalability_load_balancing_caching
title: Scalability, load balancing, caching
tags: [scalability, load-balancing, caching, cdn, rate-limiting]
count: 106
part: 2/2
---
# Scalability, load balancing, caching (part 2)

## Eviction, invalidation and cache failure modes
- [SD01-081] What is cache eviction, and what are the most popular strategies and how do they work?
- [SD01-082] Describe the steps to implement a basic cache. Why are hash maps useful in it?
- [SD01-083] How is an LRU cache built, and which data structures give O(1) get and put?
- [SD01-084] Compare LRU, LFU, FIFO and random eviction. What workload makes LRU perform badly?
- [SD01-085] What are the drawbacks of plain LRU, and how do LFU, 2Q, ARC or TinyLFU address them?
- [SD01-086] How do pluggable eviction policies such as LRU, LFU and random affect performance and memory overhead?
- [SD01-087] How does an LRU cache with per-entry TTL change when it is shared by multiple processes in an inference server?
- [SD01-088] What design considerations apply to a cache that supports high concurrency, and how would you keep a single-node cache lock-free while eviction runs in the background?
- [SD01-089] How does cache invalidation work, and why is it necessary?
- [SD01-090] Cache invalidation is called one of the hard problems in computer science. What makes it hard, and how do you keep distributed caches fresh?
- [SD01-091] How do you handle cache coherence when multiple API instances each hold a local cache?
- [SD01-092] How can cache systems go wrong?
- [SD01-093] What is a cache stampede (thundering herd), and how do you prevent it for a hot key that expires?
- [SD01-094] Explain cache penetration, cache breakdown and cache avalanche, and the mitigation for each.
- [SD01-095] How do null caching and Bloom filters protect the database from queries for nonexistent keys, and what are the trade-offs of false positives?
- [SD01-096] If your entire cache cluster goes down, what happens to the database, and how do you design for it?
- [SD01-097] A hot key receives a huge share of read traffic and overloads a single cache node. How do you diagnose and fix it?
- [SD01-098] What is the cache bottomless-pit phenomenon when adding more cache nodes, and how can it be reduced?
- [SD01-099] What is request coalescing (single-flight), and how does it differ from locking or probabilistic early expiry?
- [SD01-100] A slow request reads an old value from the database and writes it to the cache after a newer write has deleted the key. How does the stale value persist, and how do you prevent it?
- [SD01-101] What is negative caching, and what are its risks?

## Distributed caches and consistent hashing
- [SD01-102] What is the issue with simple modulo hashing for distributing data across servers when nodes are added or removed?
- [SD01-103] Explain consistent hashing and why we need it.
- [SD01-104] What fraction of keys move when a node is added to a modulo-hash cluster versus a consistent-hash ring?
- [SD01-105] What is the data skew problem in consistent hashing, and how do virtual nodes address it?
- [SD01-106] How is consistent hashing used in real-world systems?
- [SD01-107] Given a list of Memcached servers, how does the client determine which server to query?
- [SD01-108] Compare hash distribution and range distribution of data across nodes.
- [SD01-109] What are hot spots in a hash-partitioned system, and how can you mitigate them?
- [SD01-110] How does a consistent-hash ring handle node failure and replication to successor nodes? What happens to the load on neighbors?
- [SD01-111] How would you implement consistent hashing with virtual nodes and replication for a distributed cache, and how does it handle hot keys?
- [SD01-112] How would you use consistent hashing and replication to scale a cache cluster up and down with minimal cache misses?
- [SD01-113] Design a distributed cache supporting get, put, delete and TTL that is highly available and scales without major data movement.
- [SD01-114] Compare a hash ring with rendezvous hashing and with fixed hash slots. What are the trade-offs?
- [SD01-115] What is bounded-load consistent hashing, and what problem does it solve?
- [SD01-116] How many replicas of cached data do you need, and when is losing a cache node's data acceptable?

## CDN and HTTP caching
- [SD01-117] What is a CDN, and what problems does it solve?
- [SD01-118] How does a CDN work, how does it reduce latency and origin load, and what kinds of content benefit?
- [SD01-119] How does a CDN reduce latency compared with deploying the origin in multiple regions?
- [SD01-120] Compare push CDNs and pull CDNs. Which would you choose for a rarely changing site versus a large catalog of content?
- [SD01-121] How does a CDN direct a user to the closest edge node, and what happens on a cache miss?
- [SD01-122] How do you invalidate or update content cached on CDN edges, and what are the trade-offs of TTLs versus versioned URLs?
- [SD01-123] How does a CDN speed up HTTPS access and accelerate dynamic content?
- [SD01-124] How does a CDN stream video?
- [SD01-125] How do you serve large files efficiently using a CDN and range requests?
- [SD01-126] How do you prevent hotlinking or unauthorized consumption of CDN resources?
- [SD01-127] What are the disadvantages and costs of using a CDN, and when is it not worth it?
- [SD01-128] How would you handle cache invalidation and CDN propagation when a user switches their profile picture behind a stable URL?
- [SD01-129] How would you use a CDN and short-TTL caching to serve a read-heavy live commentary feed without a thundering herd on the origin?
- [SD01-130] How should caching be configured for HTML, hashed JS and CSS files, images and downloadable files?
- [SD01-131] When should you use private versus public Cache-Control directives?
- [SD01-132] What are stale-while-revalidate and stale-if-error, and when are they useful?
- [SD01-133] How do conditional requests with ETag or Last-Modified work, and when do they save bandwidth?
- [SD01-134] How do query parameters affect caching, and how do you design cache-friendly URLs?
- [SD01-135] How does content negotiation (the Vary header) affect caching strategies?
- [SD01-136] What caching considerations apply to paginated responses?
- [SD01-137] How do you cache authenticated responses safely?
- [SD01-138] What are the security implications of caching in APIs?
- [SD01-139] What is an origin shield or tiered cache in a CDN, and what problem does it solve?

## Rate limiting
- [SD01-140] What is rate limiting, and why is it needed to protect a service?
- [SD01-141] Where in the architecture would you place a rate limiter?
- [SD01-142] How should you handle rate limiting in APIs?
- [SD01-143] Compare token bucket, leaky bucket, fixed window, sliding window log and sliding window counter rate limiting.
- [SD01-144] What is the boundary burst problem of a fixed-window counter, and how do other algorithms fix it?
- [SD01-145] How does a token bucket allow bursts while a leaky bucket smooths output, and when would you pick each?
- [SD01-146] What are the trade-offs between token bucket and sliding window rate limiting?
- [SD01-147] What dimensions can you rate limit on (user, IP, API, tenant), and how do you apply limits per endpoint and per user?
- [SD01-148] How would you implement single-node rate limiting in an application process?
- [SD01-149] What should a rate-limited client receive, and how should well-behaved clients react?
- [SD01-150] What is the memory cost per client of a sliding window log versus a sliding window counter?
- [SD01-151] How would you implement a distributed rate limiter across many instances? What changes with Redis, atomicity and clock skew, and what are the race conditions?
- [SD01-152] A tenant sends 500 concurrent requests to a token-based rate limiter, and each passes the check before any reconciles. What is the failure and the fix?
- [SD01-153] How do you rate-limit fairly across a tenant's sub-organisations?
- [SD01-154] What changes when an API gateway enforces a per-organisation limit shared across thousands of API keys?
- [SD01-155] Design a rate limiting service that handles millions of requests per second with configurable rules and low added latency.
- [SD01-156] Should a rate limiter fail open or fail closed when its backing store is unavailable?
- [SD01-157] How do rate limiting, load shedding and backpressure differ, and when do you use each?

## Back-of-envelope estimation and capacity planning
- [SD01-158] Why do we use back-of-the-envelope estimation in a design interview, and which numbers should you memorize?
- [SD01-159] Which latency numbers should every engineer know, and what design decisions follow from them?
- [SD01-160] How many seconds are in a day, and how do you quickly convert monthly request counts into requests per second?
- [SD01-161] How do you estimate daily storage growth and peak QPS from daily active users and typical user behavior?
- [SD01-162] How do you do back-of-envelope sizing for an application with 100 million daily users?
- [SD01-163] How do you estimate the cache memory you need using the 80/20 rule?
- [SD01-164] How do you do capacity planning?
- [SD01-165] What is the difference between PV, UV, DAU and MAU, and how would you use them in capacity planning?
- [SD01-166] How do you use capacity estimation to justify a design decision such as sharding over a single database?
- [SD01-167] Estimate the bandwidth and storage needed for a video streaming service with 10 million daily viewers.
- [SD01-168] Given a peak load of 50,000 QPS and 2,000 QPS per server, how many servers do you provision, and what headroom do you add?
- [SD01-169] Why is peak traffic different from average traffic, and how do you pick a peak-to-average factor?
- [SD01-170] Why should you not run servers at near 100% utilization when planning capacity?

## Performance, load testing and bottlenecks
- [SD01-171] What metrics measure performance (response time, throughput, concurrency, percentiles), and why do tail latencies matter?
- [SD01-172] Why does average response time not represent tail latency, and how should P95 and P99 be interpreted in a load-test report?
- [SD01-173] What do response time, concurrency, throughput, QPS and TPS each measure, and how are they related?
- [SD01-174] Explain the differences between baseline, load, stress, capacity, stability and spike tests.
- [SD01-175] What precautions should you take before running a load test, including realistic request models, a stop mechanism and baseline data?
- [SD01-176] What is full-link load testing in production, and how do you isolate test traffic and data from real users?
- [SD01-177] When latency spikes under load, how do you systematically find the bottleneck among CPU, memory, I/O, locks and network?
- [SD01-178] What are the best ways to improve API performance, such as pagination, caching, compression, connection pooling and asynchronous logging?
- [SD01-179] Why does connection pooling improve throughput, and what happens when the pool is misconfigured?
- [SD01-180] What are common causes of 100% CPU usage on a server, and how would you investigate each?
- [SD01-181] Which website performance metrics matter most (TTFB, FCP, LCP, TTI), and how would you improve them?
- [SD01-182] When would you handle work synchronously versus offload it to a background queue?
- [SD01-183] A product page takes 2 seconds to load worldwide. Walk through the layers where you would look for improvements.
- [SD01-184] State Little's law and show how you would use it to relate concurrency, throughput and latency.
- [SD01-185] Throughput plateaus and latency rises sharply as load increases. What is happening, and how do you find the knee?
- [SD01-186] Why does fan-out to many backend services inflate tail latency, and what techniques such as hedged requests reduce it?
