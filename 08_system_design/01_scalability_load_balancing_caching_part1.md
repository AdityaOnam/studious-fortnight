---
domain: sd
topic: scalability_load_balancing_caching
title: Scalability, load balancing, caching
tags: [scalability, load-balancing, caching, cdn, rate-limiting]
count: 80
part: 1/2
---
# Scalability, load balancing, caching (part 1)

## Scaling fundamentals and architecture evolution
- [SD01-001] What is the difference between vertical and horizontal scaling, and when would you choose each?
- [SD01-002] Explain latency versus throughput and why optimizing one can hurt the other.
- [SD01-003] How does scalability differ from raw performance, and how can you tell whether your system has a performance problem or a scalability problem?
- [SD01-004] What are the limits and costs of scaling up versus scaling out?
- [SD01-005] What is the difference between scalability and extensibility in a system?
- [SD01-006] Why do cloud architectures prefer stateless application tiers, and how do you externalize state to make horizontal scaling easy?
- [SD01-007] How do the approaches for scaling a stateless application tier differ from those for a stateful storage tier?
- [SD01-008] How do you keep user sessions working in a cluster: sticky sessions, session replication, a shared session store, or client-side tokens?
- [SD01-009] What is autoscaling, and how does it decide when to scale?
- [SD01-010] What are the main trade-offs between scaling a database vertically and scaling it horizontally?
- [SD01-011] At what point do you separate the application server and the database onto different machines, and what does that change for failure modes?
- [SD01-012] How would you scale a web service? Walk through the bottleneck you fix at each step as a single-server site evolves to serve millions of users.
- [SD01-013] What is the AKF scale cube, and how does scaling a monolith by cloning differ from scaling by splitting functionality or data?
- [SD01-014] Name common production problems such as read-heavy load, write-heavy load, single points of failure and high latency, and the standard remedy for each.
- [SD01-015] How would you design for graceful degradation when traffic exceeds capacity?
- [SD01-016] Why does adding servers often fail to give linear throughput gains, and what limits scaling?
- [SD01-017] How do you scale a read-heavy system differently from a write-heavy one?
- [SD01-018] What problems can an autoscaler cause, such as flapping or lag behind a sudden spike, and how do you tune around them?
- [SD01-019] Your site grows from 1,000 to 10 million users. In what order do you introduce load balancers, replicas, caches, a CDN and sharding, and why?
- [SD01-020] How would you design a system to handle flash sales with very high request rates?
- [SD01-021] How can a single server support 1 million concurrent connections?

## Load balancing concepts and algorithms
- [SD01-022] What is a load balancer, why is it needed in a horizontally scaled system, and how does it improve reliability?
- [SD01-023] What is the difference between hardware and software load balancers?
- [SD01-024] Compare Layer 4 and Layer 7 load balancing: what can each see, what can each do, and when would you use each?
- [SD01-025] What is the difference between server-side and client-side load balancing, and how does middleware spread requests across instances?
- [SD01-026] What are the common client-side load balancing strategies in an RPC framework, and when does each fit?
- [SD01-027] Compare round robin, weighted round robin, least connections, random and IP-hash load balancing.
- [SD01-028] What are the advantages and disadvantages of round-robin load balancing?
- [SD01-029] What is the significance of the least-connections method?
- [SD01-030] In what scenarios would you use weighted load balancing?
- [SD01-031] When would you pick least-active-requests or fastest-response routing over round robin?
- [SD01-032] Under what conditions does each of round robin, weighted round robin, least connections, least response time and consistent hashing perform badly?
- [SD01-033] Why can least-connections or latency-based balancing cause a herd effect when several load balancers act on stale information?
- [SD01-034] How does a load balancer distribute traffic in a stateless versus a stateful scenario?
- [SD01-035] What is a sticky session (session persistence), and why is it used?
- [SD01-036] What problems do sticky sessions introduce for scaling, failover and scale-in?
- [SD01-037] Explain the power-of-two-choices algorithm. Why does it balance load nearly as well as global least-loaded selection with far less coordination?
- [SD01-038] Why is distributing requests evenly not the same as distributing load evenly, and how can a balancer use real-time backend load feedback?
- [SD01-039] What role does DNS play in load balancing, and what are its limitations such as TTL caching and no health awareness?
- [SD01-040] How do DNS-based load balancing and reverse-proxy load balancing differ, and why are they often combined?
- [SD01-041] How does global load balancing across regions work, and how does anycast differ from DNS-based routing?

## Load balancer reliability, proxies and design
- [SD01-042] How do load balancers perform health checks on backends, and how do you avoid sending traffic to a failing node?
- [SD01-043] How does a load balancer handle the failure of a server it manages?
- [SD01-044] How do connection draining and graceful removal work so that taking a backend out of rotation does not drop in-flight requests?
- [SD01-045] How can a load balancer avoid being a single point of failure?
- [SD01-046] Compare active-active and active-passive configurations for load balancers or server clusters.
- [SD01-047] What are the differences between NAT, direct routing and tunneling forwarding modes in layer-4 load balancing?
- [SD01-048] What is the difference between a load balancer and a reverse proxy, and can one component play both roles?
- [SD01-049] Compare a forward proxy and a reverse proxy, with an example of each.
- [SD01-050] Besides load balancing, what does a reverse proxy provide (TLS termination, compression, static content, security), and what are its disadvantages?
- [SD01-051] Design a TCP load balancer that acts as a reverse proxy, supports adding and removing backends, health checks, pluggable strategies and metrics, and scales to millions of concurrent connections.
- [SD01-052] What are the trade-offs of terminating TLS at the load balancer versus re-encrypting to the backends?
- [SD01-053] How do long-lived connections such as WebSockets behave behind a load balancer when you scale in or deploy?
- [SD01-054] How should a new backend be introduced to a pool to avoid being overwhelmed by a flood of traffic on startup?
- [SD01-055] A load balancer retries failed requests on other backends and the whole fleet collapses during a partial outage. What happened, and how do you prevent it?

## Caching fundamentals and write strategies
- [SD01-056] Why do we need a cache, and how does it improve data retrieval time?
- [SD01-057] Explain cache hit and cache miss.
- [SD01-058] What is a cache key and how is it used?
- [SD01-059] How do cache hit rate, maximum size and eviction policy interact when you size a cache, and how does cache size affect performance?
- [SD01-060] Name the caching layers between a user and a database (browser, CDN, reverse proxy, application, database) and what each caches.
- [SD01-061] Your cache hit ratio is low. How would you diagnose and improve it?
- [SD01-062] Where should a cache be placed (client, application server, separate tier, in front of the web tier), and what are the risks of stale data?
- [SD01-063] Compare local, distributed, global and multi-level caches. When would you combine them?
- [SD01-064] What is the CPU multi-level cache hierarchy, and why does cache locality matter for performance?
- [SD01-065] Compare cache-aside, read-through, write-through, write-around and write-back caching, including performance implications.
- [SD01-066] Which caching pattern would you use for a key-value store, and why?
- [SD01-067] When should you choose write-through versus cache-aside?
- [SD01-068] Compare read-through and write-through caches. Which combinations give stronger consistency?
- [SD01-069] What are the failure modes of cache-aside, and how can stale data appear?
- [SD01-070] Why is write-back caching risky, and how would you reduce the chance of data loss?
- [SD01-071] Why is it usually safer to delete a cache entry than to update it on a database write, and what race conditions remain?
- [SD01-072] When should the cache be updated?
- [SD01-073] How do you decide what to cache and what TTL to use for different kinds of data?
- [SD01-074] When should you not use caching, and what are its disadvantages?
- [SD01-075] How would you measure whether adding a cache actually helps a service, and what could make it harmful?
- [SD01-076] Which metrics should you monitor for cache performance?
- [SD01-077] How do you implement cache warming effectively?
- [SD01-078] How would you design the caching strategy for a video streaming service?
- [SD01-079] Your cache hit ratio is 95% yet latency barely improved. What could explain this?
- [SD01-080] How does a write-heavy workload change the usefulness of a cache-aside design?
