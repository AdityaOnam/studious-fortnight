---
domain: sd
topic: reliability_observability_security
title: Reliability, observability, security in system design
tags: [reliability, observability, slo, security]
count: 83
part: 1/2
---
# Reliability, observability, security in system design (part 1)

## Availability and reliability fundamentals
- [SD05-001] What does availability mean when designing a system, and how do you measure it?
- [SD05-002] What is high availability, and how do you express it in "nines" of uptime?
- [SD05-003] How much downtime per year do 99.9%, 99.99% and 99.999% availability allow?
- [SD05-004] Why is a 100% availability target unrealistic, and what should you aim for instead?
- [SD05-005] What is the difference between availability and reliability in a software system?
- [SD05-006] What is a single point of failure, and how do you find and mitigate one?
- [SD05-007] How do you compute availability for components in series versus in parallel? Compare two 99.9% components each way.
- [SD05-008] What is the difference between high availability and fault tolerance?
- [SD05-009] How does redundancy improve reliability, and what new costs or failure modes does it introduce?
- [SD05-010] What is MTBF and why does it matter in reliability engineering?
- [SD05-011] What role does MTTR play in system availability?
- [SD05-012] Why is it often more effective to reduce MTTR than to increase MTBF?
- [SD05-013] What are the common causes of system unavailability, and which design measures address each?
- [SD05-014] What design patterns are commonly used to improve system availability?
- [SD05-015] A product promises 99.99% availability but depends serially on four services that each offer 99.95%. Can it meet the target, and what would you change?

## SLI, SLO, SLA and error budgets
- [SD05-016] What is the difference between SLI, SLO and SLA, and why are they important? What is an error budget?
- [SD05-017] What are SLOs and error budgets, and how do you define them?
- [SD05-018] How would you choose SLIs and set an SLO for a user-facing API?
- [SD05-019] Why should an internal SLO be stricter than the SLA you promise customers?
- [SD05-020] Why use percentiles rather than averages for latency SLIs?
- [SD05-021] What do you do when a service exhausts its error budget?
- [SD05-022] Your service depends on a third party offering a 99.9% SLA. What availability SLO can you responsibly offer?
- [SD05-023] How does multi-window burn-rate alerting on an SLO work, and why is it better than a simple threshold alert?
- [SD05-024] What SLIs and SLOs would you define for an LLM inference service (for example time to first token, throughput, error rate)?

## High availability architecture and failover
- [SD05-025] Why do stateless services make high availability easier to achieve?
- [SD05-026] What is the difference between a Region and an Availability Zone, and why does the distinction matter?
- [SD05-027] How would you architect a system for high availability?
- [SD05-028] How do you design for high availability across layers: DNS, load balancer, application, database and storage?
- [SD05-029] How can load balancing improve availability, and what are its pitfalls?
- [SD05-030] What role do health checks play in keeping a system available?
- [SD05-031] What is the difference between liveness, readiness and startup probes, and what goes wrong if they are misused?
- [SD05-032] How much spare capacity do you need to survive the loss of one availability zone?
- [SD05-033] What is failover clustering?
- [SD05-034] Compare active-passive and active-active failover. What are the data loss risks and other disadvantages of failover?
- [SD05-035] How does automatic failover work with a sentinel or a keepalived virtual IP, and what can go wrong with false failover?
- [SD05-036] How does DNS-based failover work, and what limits it (TTL, caching)?
- [SD05-037] How do asynchronous calls and caching contribute to availability, and what new risks do they introduce?
- [SD05-038] What are the key patterns for designing fault-tolerant systems?
- [SD05-039] How does message-driven architecture contribute to the resilience of a reactive system?
- [SD05-040] What strategy might a reactive system use to stay responsive during a component failure?
- [SD05-041] How would a reactive system address a transient failure differently from a network partition?
- [SD05-042] What is split-brain during failover, and how do fencing and quorum prevent it?
- [SD05-043] Design a highly available order service for flash sales and explain which availability mechanisms you would layer in.
- [SD05-044] How do you design an AI system for high availability and fault tolerance?
- [SD05-045] What is chaos engineering and how is it used to build resilient systems?
- [SD05-046] How would you use chaos experiments to validate that a consensus-based cluster tolerates leader crashes and network partitions?
- [SD05-047] How would you prove that your failover actually works, and how often should you drill it?

## Timeouts and retries
- [SD05-048] Why is setting timeouts essential for remote calls, and what happens to a system without them?
- [SD05-049] How do you choose a timeout for a downstream call, and how should it relate to the caller's overall deadline?
- [SD05-050] How is a timeout budget propagated layer by layer along a call chain?
- [SD05-051] How can APIs be unreliable and unpredictable, and how do you design clients to cope?
- [SD05-052] How do you handle failure in a microservice?
- [SD05-053] Compare retry strategies: fixed interval, exponential backoff and backoff with jitter. Why does jitter matter?
- [SD05-054] Which errors are safe to retry and which are not, and why must retries be paired with idempotency?
- [SD05-055] What is an idempotency key and how does it make retrying a POST request safe?
- [SD05-056] How should clients handle intermittent server errors (5xx) in production APIs?
- [SD05-057] What is a retry storm, and how can retry budgets, timeouts and circuit breakers bound retry amplification across layers?
- [SD05-058] A service calls three downstreams in series, each retrying three times. What happens during a downstream outage and how would you redesign it?
- [SD05-059] What is the thundering herd after an outage recovers, and how do jitter, warm-up and gradual ramp-up mitigate it?
- [SD05-060] What metrics would you watch to detect misconfigured timeouts and retries in production?
- [SD05-061] What are the risks of hedged requests for non-idempotent operations?
- [SD05-062] Should a retry policy for model-endpoint calls live in every caller, in the SDK client, or in a gateway in front of the model?
- [SD05-063] How do retries work when a streaming response fails halfway through?
- [SD05-064] A coding assistant wrote a retry helper that catches any exception, sleeps 2^attempt seconds, tries five times, and returns None on failure. Review it for production: what is wrong and what would you change?

## Circuit breakers, bulkheads and degradation
- [SD05-065] What is the purpose of the circuit breaker pattern, and why do we need it in a microservices ecosystem?
- [SD05-066] How does a circuit breaker work, and what are its closed, open and half-open states?
- [SD05-067] What triggers a breaker to open (error ratio, slow-call ratio, consecutive failures) and how is the half-open probe done?
- [SD05-068] Can you use P99 latency directly as a circuit breaker condition? Discuss the pitfalls of tail-latency percentiles.
- [SD05-069] How do you prevent a circuit breaker from flapping or from being stampeded by traffic when it half-opens?
- [SD05-070] How does a service avalanche or cascading failure happen in a call chain, and what patterns prevent it?
- [SD05-071] How would you handle a cascading failure in which one slow dependency exhausts threads across upstream services?
- [SD05-072] What is the bulkhead pattern and how does it contain failure?
- [SD05-073] Compare thread-pool isolation and semaphore isolation for protecting a service from slow dependencies.
- [SD05-074] How do timeouts, bulkheads and load shedding contribute to resilience?
- [SD05-075] What is the difference between rate limiting, service degradation and circuit breaking, and how do they cooperate on a single request?
- [SD05-076] What is service degradation, when is it triggered, and at what granularity can it be applied?
- [SD05-077] What does a good fallback look like, and what pitfalls (such as a fallback calling another failing dependency) must be avoided?
- [SD05-078] What is the difference between load shedding and backpressure?
- [SD05-079] When you must shed load, how do you decide which requests to drop first?
- [SD05-080] What is system adaptive protection that throttles traffic by load, CPU and concurrency rather than static thresholds?
- [SD05-081] How would you operate degradation switches at scale, including pre-defined plans, switch storage and safe rollback?
- [SD05-082] How do you design an AI system that degrades gracefully when the model is unavailable?
- [SD05-083] How would you deterministically test the circuit-breaker behaviour of a multi-provider LLM client pool?
