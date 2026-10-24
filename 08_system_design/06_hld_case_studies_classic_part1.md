---
domain: sd
topic: hld_case_studies_classic
title: HLD case studies (classic)
tags: [hld, case-study, design-x]
count: 103
part: 1/3
---
# HLD case studies (classic) (part 1)

## Approaching a design interview
- [SD06-001] How do you approach a system design interview question, from requirements through to bottlenecks?
- [SD06-002] Before drawing any boxes, how do you turn a back-of-envelope estimate of DAU into QPS, storage and bandwidth numbers?
- [SD06-003] What clarifying questions do you ask about scale, consistency and failure handling before designing anything?
- [SD06-004] Why present the data model and API before the high-level architecture, and how does that shape the rest of the design?
- [SD06-005] When explaining a design, how do you justify the choice between SQL and NoSQL for its main data?
- [SD06-006] Which consistency model would you pick for a news feed, a bank balance and a shopping cart, and why?
- [SD06-007] For a given Design X prompt, how do you decide which components can be eventually consistent and which need strong consistency?
- [SD06-008] After drawing the high-level architecture, what steps do you follow to find and resolve bottlenecks?
- [SD06-009] How do you argue that your design never reaches an inconsistent state when multiple writers act concurrently?
- [SD06-010] How do you distinguish peak QPS from average QPS when sizing a system, and what headroom do you plan for?
- [SD06-011] The interviewer says the system must now support 100x more traffic. What is your process for finding and relieving the next bottleneck?
- [SD06-012] Design a system that scales from one user to millions of users on AWS. What do you add at each growth stage?

## URL shortener
- [SD06-013] What are the functional and non-functional requirements of a URL shortener?
- [SD06-014] Design a URL shortening service such as TinyURL or bit.ly that supports creating short links and redirecting to the original URL.
- [SD06-015] Why do you need an API key in a URL shortener's API design?
- [SD06-016] Estimate requests per second, storage, bandwidth and cache size for a URL shortener that creates 100 million links per month with a 100:1 read-to-write ratio.
- [SD06-017] How do you generate unique short keys: hashing and truncating, base62 encoding of a counter, or a pre-generated key service? Compare the options.
- [SD06-018] How do you avoid hash collisions and prevent two app servers from handing out the same short key, including concurrent access to the key generation service?
- [SD06-019] Which database would you use for a URL shortener, how do you store the mappings, and how would you partition it as it grows to billions of rows?
- [SD06-020] Should a URL shortener redirect with HTTP 301 or 302, and how does that choice affect analytics and caching?
- [SD06-021] Which cache eviction policy suits a URL shortener, and why?
- [SD06-022] How do you handle a cache miss in a URL shortener?
- [SD06-023] How do you implement the redirect servers in a URL shortener?
- [SD06-024] How would you expire, purge and clean up old or deleted short URLs without hurting performance?
- [SD06-025] How do you store click statistics in a URL shortener?
- [SD06-026] How would you partition the aggregation tier that computes click statistics in a URL shortener?
- [SD06-027] How do you support custom aliases, link analytics and abuse prevention in a URL shortener?
- [SD06-028] How do you prevent a URL shortener from being used to reach restricted or malicious sites?
- [SD06-029] What consistency does a URL shortener need for newly created links, and how do replicas and caches affect it?
- [SD06-030] For a read-heavy service like a URL shortener, what is your failure-handling plan for cache, database and app server outages?
- [SD06-031] How would you make a URL shortener resilient to the loss of its key generation service or its primary database?
- [SD06-032] How would you scale a URL shortener to 100x traffic, including a viral link accessed millions of times per minute?

## Pastebin and blogging platforms
- [SD06-033] Design Pastebin, where users upload a block of text and get a link with optional expiration.
- [SD06-034] Where would you store paste contents versus metadata in Pastebin, and why use an object store for the content?
- [SD06-035] How does a Pastebin service track page view analytics and delete expired pastes at scale?
- [SD06-036] Design a service for creating and viewing pastes that sustains 40 reads per second per write. Where do the bottlenecks appear at 10x growth?
- [SD06-037] Design a URL shortener and a Pastebin as one platform. Which components can be shared between them?
- [SD06-038] Design a multi-user blogging platform for 5 million daily readers and 10,000 daily writers, with image support, search and per-author blog counts.
- [SD06-039] In a blogging platform, how would you show the number of blogs written by each author on a profile page without expensive counting queries?
- [SD06-040] How would you design low-latency blog reads and cache invalidation when authors edit or delete a post?

## Rate limiter, load balancer and API gateway
- [SD06-041] Compare token bucket, leaky bucket, fixed window and sliding window rate limiting. Which would you choose for a public API and why?
- [SD06-042] Design a rate limiter as a standalone service shared by many APIs.
- [SD06-043] Build a per-key token-bucket rate limiter for an API gateway, then extend it to work across a cluster of gateway instances.
- [SD06-044] Design a token-based rate limiter for a multi-tenant LLM API. Implement the core, then explain what changes when it is distributed.
- [SD06-045] Design a distributed rate limiter that is accurate under bursts, adds minimal latency, and degrades gracefully when its store fails.
- [SD06-046] If the rate limiter's backing store is unreachable, should it fail open or fail closed? Justify your answer.
- [SD06-047] For a rate limiter shared by multiple regions, how do you balance accuracy against cross-region latency?
- [SD06-048] How do you rate limit by user, IP and API key at once, and what do you do about a single hot key?
- [SD06-049] What should a rate limiter return to clients that exceed their limit, and what headers help them back off?
- [SD06-050] Design a load balancer. How does it pick backends, detect unhealthy ones, and avoid being a single point of failure itself?
- [SD06-051] Design an L7 load balancer that handles millions of requests per second and uses backend load feedback.
- [SD06-052] Design an API gateway for a large microservice platform.

## Distributed cache
- [SD06-053] Design a distributed cache such as a Redis-like key-value store, including partitioning, replication and eviction.
- [SD06-054] Design a distributed cache like Memcached. How does the client pick a server, and how do you keep data fresh and available?
- [SD06-055] Implement an LRU cache with a hash map and linked list, then explain how you would scale it across machines.
- [SD06-056] Design a key-value cache that stores the results of the most recent web server queries.
- [SD06-057] How would you shard an in-memory query cache and keep it consistent when the underlying results change?
- [SD06-058] Design a service that returns a user's last 10 unique searches with response time below 10 ms.
- [SD06-059] When a cache node fails, how do you avoid sending a surge of queries to the database?
- [SD06-060] How do you prevent a cache stampede on a hot key that has just expired?
- [SD06-061] Compare cache-aside, write-through and write-back caching. When does each cause stale reads or lost writes?
- [SD06-062] For a distributed cache spanning regions, how do you keep caches consistent when the database is updated in one region?
- [SD06-063] How does consistent hashing help a cache cluster, and what problems do virtual nodes solve?
- [SD06-064] Design a session management system for a web application that runs on a cluster of servers.

## Key-value stores and databases
- [SD06-065] Design a distributed key-value store with replication and tunable consistency.
- [SD06-066] Design a Dynamo-style key-value store. How do you handle partitioning, replication, conflict resolution and failure detection?
- [SD06-067] Design a superfast key-value store. What do you trade away to get latency down?
- [SD06-068] Design a key-value store that serves as the index for a search engine.
- [SD06-069] Design a key-value store that is backed by a SQL database. What are the limits of this approach?
- [SD06-070] In a log-structured key-value store, how do you recover the in-memory index after a restart, and how does compaction affect read latency?
- [SD06-071] Design a real-time database that pushes changes to subscribed clients.
- [SD06-072] Design a dictionary service that handles 5 million requests per minute, is updated weekly from a changelog, and cannot use a traditional database.
- [SD06-073] Design the data layer for a shopping cart that must always accept writes, even during network partitions.

## Unique IDs, locks and coordination
- [SD06-074] Design a unique ID generator for a distributed system that produces millions of IDs per second.
- [SD06-075] Design an ID service that scales to 1000 requests per second from each of 1000 devices per person, for every human on earth, for 100 years.
- [SD06-076] For an ID generator, what are the failure modes when machine IDs are misconfigured or clocks drift?
- [SD06-077] Design a distributed lock service that clients across many machines can rely on.
- [SD06-078] Why is a lock with an expiry lease unsafe without fencing tokens, and how does a fencing token fix it?
- [SD06-079] How would you implement leader election for a group of workers, and what happens during a network partition?

## Message queues and job schedulers
- [SD06-080] Design a distributed message queue like Kafka that supports ordering, durability and consumer groups.
- [SD06-081] Design a message broker backed by a SQL database. How would consumers claim messages without double-processing?
- [SD06-082] How would you provide at-least-once versus exactly-once delivery in a message queue, and what does each cost?
- [SD06-083] What do you do when consumers fall behind a message queue and lag keeps growing?
- [SD06-084] Design a distributed job scheduler that runs delayed and recurring jobs reliably.
- [SD06-085] Design a scheduler that sends reminders for reservations using a priority queue.
- [SD06-086] Design a system that sends scheduled emails or reminders to millions of users at the right time.
- [SD06-087] In a job scheduler, how do you prevent a job from running twice when a worker crashes mid-execution?
- [SD06-088] Design a code deployment system that rolls out builds to thousands of servers and supports rollback.

## Webhook delivery
- [SD06-089] Design a webhook delivery service that notifies merchants when a payment succeeds.
- [SD06-090] Design a system that reliably delivers events to customer-registered URLs.
- [SD06-091] How would you build webhooks with at-least-once delivery, signed payloads, exponential backoff retries and a circuit breaker for broken receivers?
- [SD06-092] How do you protect webhook receivers from replay attacks and help them process each event once?
- [SD06-093] How do you protect your own infrastructure from slow or malicious webhook receivers?

## Notification systems
- [SD06-094] How does a typical push notification system work end to end?
- [SD06-095] Design a notification service that sends push, SMS and email to millions of users.
- [SD06-096] How does a large streaming company deliver push messages to millions of connected devices?
- [SD06-097] How do you avoid duplicate or delayed notifications and respect user preferences and quiet hours?
- [SD06-098] How do you add priority handling and retries for third-party delivery providers in a notification service?
- [SD06-099] How do you guarantee at-least-once delivery in a notification service without spamming users on retries?
- [SD06-100] What happens in a notification system when a downstream provider such as an SMS gateway is down for an hour?
- [SD06-101] At 10x scale, how would you shard and parallelize a notification pipeline to reach 100 million devices in minutes?
- [SD06-102] Design a stock price alert system for 3 million users and several thousand stocks that notifies users of 5 and 10 percent moves.
- [SD06-103] How do you avoid sending the same stock alert repeatedly when a price oscillates around a threshold?
