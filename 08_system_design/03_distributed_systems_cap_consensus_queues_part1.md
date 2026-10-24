---
domain: sd
topic: distributed_systems_cap_consensus_queues
title: Distributed systems: CAP, consensus, queues
tags: [cap, consensus, kafka, distributed]
count: 113
part: 1/2
---
# Distributed systems: CAP, consensus, queues (part 1)

## Distributed systems fundamentals, failure detection and clocks
- [SD03-001] What is a distributed system, and how does it differ from a cluster or a microservice architecture?
- [SD03-002] Why is partial failure the defining difficulty of distributed systems, and what new classes of problems appear compared with a single-node monolith?
- [SD03-003] What is the Two Generals problem, and what does it say about reliable communication over an unreliable link?
- [SD03-004] How do you detect node failures in a distributed system?
- [SD03-005] How do heartbeat-based failure detectors work, and how do push, pull and quorum variants differ?
- [SD03-006] Why can't a node tell a crashed peer from a slow one or a network partition, and what does that imply for choosing timeouts?
- [SD03-007] How does a phi-accrual failure detector differ from a fixed-timeout heartbeat detector?
- [SD03-008] Why can't machines in a distributed system rely on a single global clock, and what alternatives exist for ordering events?
- [SD03-009] How do Lamport clocks and vector clocks work, and what can vector clocks detect that Lamport clocks cannot?
- [SD03-010] How do Google Spanner's TrueTime and commit wait provide externally consistent transactions?
- [SD03-011] Why do leap seconds break timestamp assumptions, and why have large companies stopped using them or started smearing them?
- [SD03-012] How do you design a distributed ID generator, and how do auto-increment, segment allocation, UUID and Snowflake compare?
- [SD03-013] What problems does clock rollback cause for Snowflake-style ID generators, and how can you defend against them?
- [SD03-014] What does the FLP impossibility result say, and how do practical consensus systems work around it?

## CAP theorem, PACELC and consistency trade-offs
- [SD03-015] What are the three guarantees in the CAP theorem, and why can't a distributed system provide all three during a partition?
- [SD03-016] What does consistency mean in the CAP theorem, and how does it differ from consistency in ACID?
- [SD03-017] What does availability mean in the CAP theorem, and how does it differ from the everyday notion of high availability?
- [SD03-018] Explain partition tolerance in CAP and why it is not optional in practice, so that a "CA" system is not meaningful.
- [SD03-019] Why is the "pick two of three" framing of CAP misleading, and how useful is the theorem really?
- [SD03-020] During a network partition, how does a CP system behave compared with an AP system?
- [SD03-021] Give examples of real systems that favor consistency over availability and the reverse, and describe what users see during a partition.
- [SD03-022] What does PACELC add to CAP, and why does it matter when there is no partition?
- [SD03-023] If a network partition occurs, what strategies can you use to keep serving requests?
- [SD03-024] How do databases such as Cassandra and DynamoDB deal with the trade-offs posed by CAP?
- [SD03-025] What does eventual consistency mean in the context of CAP?
- [SD03-026] What do basically available, soft state and eventual consistency mean in BASE, and how does BASE relate to ACID?
- [SD03-027] What is the relationship between CAP and BASE, in which scenarios is eventual consistency appropriate, and how can it be made tolerable to users?
- [SD03-028] Compare strong, weak and eventual consistency with a product feature suited to each; where do DNS, memcached and relational databases fall?
- [SD03-029] How does linearizability differ from serializability, and which of the two does the C in CAP refer to?
- [SD03-030] What trade-offs do you accept when designing a system that needs high availability, according to CAP?
- [SD03-031] How would you apply CAP thinking per feature inside one product, for example strong consistency for payments but eventual consistency for a view counter?
- [SD03-032] Pick a real system you would build as CP and one as AP, and justify each choice including its failure behaviour.
- [SD03-033] How do idempotency, commutativity and convergence help in designs that accept the AP side of CAP?
- [SD03-034] A database is documented as CP but returns stale reads during a partition. What could explain this?

## Consensus: Paxos, Raft and ZAB
- [SD03-035] What properties must a consensus protocol satisfy, and why does agreement on a value not imply the system keeps making progress?
- [SD03-036] What is the Byzantine Generals Problem, how do Byzantine faults differ from crash faults, and why do Raft and Paxos assume crash faults only?
- [SD03-037] Why do oral messages require at least 3m+1 nodes to tolerate m traitors, and how do signed messages change that bound?
- [SD03-038] Explain Basic Paxos: the roles of proposer, acceptor and learner, the prepare and accept phases, and the purpose of proposal numbers.
- [SD03-039] Why does Paxos require a majority quorum, and what role do proposal numbers play in it?
- [SD03-040] How does Paxos guarantee safety once a value has been chosen, even when proposers and acceptors crash and restart?
- [SD03-041] Why can Basic Paxos livelock with competing proposers, and how do practical systems mitigate it?
- [SD03-042] What problem does Multi-Paxos solve relative to Basic Paxos, and why is Paxos considered hard to understand and implement?
- [SD03-043] Compare Paxos and Raft on understandability, leader handling, log replication and membership change.
- [SD03-044] What are the three node roles in Raft, and how does a node move between them?
- [SD03-045] Explain how consensus algorithms such as Paxos or Raft elect a leader, including terms, randomized election timeouts, the majority vote and split votes.
- [SD03-046] How does Raft replicate log entries, and when is an entry considered committed?
- [SD03-047] What happens in a Raft cluster when a network partition isolates the current leader from the majority?
- [SD03-048] Why are consensus clusters usually deployed with an odd number of nodes, and how many failures can a 5-node cluster tolerate?
- [SD03-049] Explain Raft's Log Matching Property and how a new leader repairs a follower whose log diverges from its own.
- [SD03-050] Why does Raft restrict leader election to candidates with sufficiently up-to-date logs?
- [SD03-051] Why does a Raft leader commit entries from earlier terms only indirectly by counting replicas of its own term, and what anomaly does that prevent?
- [SD03-052] How does a Raft cluster serve linearizable reads, and why is answering from the leader's local state alone not always safe?
- [SD03-053] How does Raft change cluster membership safely, and why is replacing many members at once dangerous?
- [SD03-054] Why do Raft implementations take snapshots and compact the log, and what does a leader do for a follower that is far behind?
- [SD03-055] How does ZAB work in its broadcast and crash-recovery modes, and what happens when the leader fails?
- [SD03-056] What are ZXID and epoch used for in a leader-based atomic broadcast protocol such as ZAB?
- [SD03-057] How does ZAB compare with Raft and Paxos in how it orders writes and recovers after a leader crash?

## Leader election, quorums, gossip and coordination services
- [SD03-058] What is leader election, and what problems does split brain cause?
- [SD03-059] What is split brain in a replicated cluster, and how do majority-quorum rules prevent it?
- [SD03-060] How does a quorum read and write scheme with R + W > N provide consistency, and how do quorums trade consistency against availability?
- [SD03-061] Why is a majority quorum not a complete answer to split brain, and which additional mechanisms such as epochs, leases and fencing tokens are needed?
- [SD03-062] Is a single-leader system necessarily a single point of failure? How do leader-based systems stay available?
- [SD03-063] Compare active-passive failover, active-active and quorum-based replication as strategies for fault tolerance.
- [SD03-064] How does the bully algorithm elect a leader, and why is it a poor fit for large or unreliable networks?
- [SD03-065] In a two-data-center deployment, where do you place the nodes of a majority-quorum cluster, and what role does a witness or tie-breaker node play?
- [SD03-066] Why do some systems need a leader while others are better off using gossip to propagate state?
- [SD03-067] How does gossip spread information and why does it scale with the number of nodes? How do anti-entropy and rumor-mongering differ?
- [SD03-068] Roughly how many gossip rounds does it take for an update to reach all N nodes, and which parameters control convergence speed and network cost?
- [SD03-069] What are the main drawbacks of gossip protocols, such as convergence delay, redundant messages and Byzantine behaviour?
- [SD03-070] Where is gossip used in real systems, and how does gossip-based failure detection scale compared with centralized heartbeating?
- [SD03-071] What is Apache ZooKeeper, and what coordination problems is it designed to solve?
- [SD03-072] Explain ZooKeeper's znode types, and how sessions and ephemeral nodes interact when a session expires.
- [SD03-073] How does a watcher work in a coordination service, and what are its delivery semantics and limitations?
- [SD03-074] How would you implement leader election, naming service and group membership on top of ZooKeeper?
- [SD03-075] Which consistency guarantees does ZooKeeper provide for reads and writes, and why can a read from a follower be stale?
- [SD03-076] Compare ZooKeeper and etcd in terms of consensus protocol, data model and typical use cases.

## Distributed locks, leases and fencing
- [SD03-077] Why do we need distributed locks when each process already has a local lock, and what can go wrong if the holder pauses or the lock expires?
- [SD03-078] Does every multi-instance deployment need a distributed lock? What alternatives exist, such as unique constraints or optimistic locking?
- [SD03-079] What properties should a correct distributed lock have, including mutual exclusion, deadlock freedom, reentrancy and fault tolerance?
- [SD03-080] How would you implement a distributed lock using a database unique index?
- [SD03-081] How do you implement a distributed lock with Redis SET NX and expiry, and why must acquisition and expiry be set atomically?
- [SD03-082] Why must a lock have an expiry, what goes wrong if the holder outlives it, and why release it with an owner check in an atomic Lua script?
- [SD03-083] How is a reentrant distributed lock implemented, and what extra state must be stored?
- [SD03-084] How does a watchdog or automatic lease renewal work, and what failure scenarios can it still not prevent?
- [SD03-085] How does a ZooKeeper lock with ephemeral sequential nodes work, and why does watching only the predecessor avoid the thundering herd?
- [SD03-086] Explain the Redlock algorithm and the criticism that it is unsafe without fencing tokens, including failover of a single Redis master.
- [SD03-087] Compare database, Redis and ZooKeeper or etcd based distributed locks on correctness, performance and failure behaviour.
- [SD03-088] A client holds a distributed lock, pauses for a long garbage collection and resumes after its lease expired. How can the protected resource defend itself?
- [SD03-089] Why does a lease also need a fencing token, given that a lease cannot prove the old holder has stopped acting?
- [SD03-090] What is a fencing token, and how does a storage service use it to reject writes from a stale lock holder when you build a lock on Redis or a consensus system?
- [SD03-091] Three instances of a service each run a scheduled job that must run once per tick. Design the coordination mechanism and discuss its failure modes.
- [SD03-092] Two workers pick up the same approved action at the same moment. What prevents double execution?
- [SD03-093] A remote queue removes and returns its head on each fetch with no protection against concurrent consumers. How do you synchronize consumers so each element is processed once?
- [SD03-094] How would you implement a distributed lock for queue consumers and what happens if the holder crashes mid-processing? Compare it with a single-leader consumer and with partitioning the queue.
- [SD03-095] Production data was corrupted even though a distributed lock was in use. How would you investigate how two clients both believed they held it?

## Idempotency and delivery guarantees
- [SD03-096] What does idempotency mean in an API or message consumer, why does it matter, and in which cases must you apply it?
- [SD03-097] How does an idempotent operation differ from a safe one, and which HTTP methods are each?
- [SD03-098] How do you implement idempotency for a POST endpoint, including in stateless APIs?
- [SD03-099] How do idempotency keys work in a payment API, and how do you handle key storage and expiry?
- [SD03-100] What race conditions must you avoid when implementing API idempotency?
- [SD03-101] What should an API do when it receives the same idempotency key with a different request body?
- [SD03-102] How does idempotency interact with eventual consistency?
- [SD03-103] How can an API prevent double payments using idempotency?
- [SD03-104] A Java service's retry caused a Python service to create two tickets. What is the root cause and how do you fix it?
- [SD03-105] How do you make an EHR write-back idempotent when the EHR returns a timeout with no result?
- [SD03-106] What do at-most-once, at-least-once and exactly-once delivery mean, and where does each fit?
- [SD03-107] Why does at-least-once delivery produce duplicate messages, and how can a consumer ensure idempotent processing?
- [SD03-108] How would you implement a consumer-side deduplication table so the dedupe record and the business side effect commit atomically?
- [SD03-109] Why is exactly-once delivery practically impossible, and how does at-least-once delivery plus idempotent processing give effectively-once behaviour?
- [SD03-110] How do you handle failures and retries in a message consumer without causing duplicate side effects?
- [SD03-111] Why is deduplication a concern when delivering events to external endpoints, and what do you do if the external endpoint is not idempotent?
- [SD03-112] In a webhook delivery system, what happens when a customer's endpoint is up but takes 30 seconds to respond?
- [SD03-113] A Spark Structured Streaming job reads Kafka and writes with foreachBatch into Postgres, and the customer wants exactly-once delivery. What do you build?
