---
domain: sd
topic: distributed_systems_cap_consensus_queues
title: Distributed systems: CAP, consensus, queues
tags: [cap, consensus, kafka, distributed]
count: 92
part: 2/2
---
# Distributed systems: CAP, consensus, queues (part 2)

## Message queue fundamentals
- [SD03-114] What is a message queue, how does it work, and what problems does it solve in a distributed system?
- [SD03-115] What are some common message queues, and what are they used for?
- [SD03-116] Compare the point-to-point queue model with the publish-subscribe topic model.
- [SD03-117] What is the difference between a message broker, a message queue, a task queue and an event streaming platform?
- [SD03-118] How do message queues enable asynchronous processing, peak shaving, decoupling and notifications?
- [SD03-119] What new problems does introducing a message queue create, such as availability, consistency and operational complexity?
- [SD03-120] What is the difference between using RPC and a message queue to communicate between services?
- [SD03-121] How would you choose between Kafka, RabbitMQ and a cloud queue, and how do Kafka, RocketMQ and RabbitMQ differ in message model, throughput, latency, replay and operations?

## Reliability, ordering and consumer patterns
- [SD03-122] A consumer crashes after processing a message but before acknowledging it. What happens next, and how should the system be designed for it?
- [SD03-123] How do you ensure no message is lost at the producer, the broker and the consumer?
- [SD03-124] How do you guarantee message ordering in a partitioned queue, and what do you give up in parallelism?
- [SD03-125] What is a dead-letter queue and a poison-pill message, and how should consumers handle them?
- [SD03-126] How do you avoid head-of-line blocking when one message keeps failing in a queue that must preserve order?
- [SD03-127] What is backpressure in a queue-based system and how can you apply it?
- [SD03-128] Compare blocking and non-blocking, bounded and unbounded queues, and FIFO, priority, delay and dead-letter queues.
- [SD03-129] What does the competing consumers pattern guarantee, and what does it sacrifice?
- [SD03-130] What is the claim check pattern, and when do you use it instead of sending large payloads through a broker?
- [SD03-131] Compare push and pull consumption models in a message queue.
- [SD03-132] What is replay (rewind) consumption by offset or time, and when is it useful?
- [SD03-133] A queue backlog grows to millions of messages. How do you diagnose and drain it safely?
- [SD03-134] How would you size and scale a queue-based pipeline that must absorb a sudden tenfold traffic spike?

## Event sourcing, CQRS and change data capture
- [SD03-135] Explain event sourcing and compare it with ordinary event-driven architecture. How would you introduce it into an existing system?
- [SD03-136] What are the benefits of event sourcing for reactive systems, and what challenges come with snapshots, schema evolution and replay?
- [SD03-137] What is CQRS, and when does separating read and write models help or hurt?
- [SD03-138] How does Change Data Capture work?
- [SD03-139] What are the trade-offs between log-based CDC, polling the database and dual writes for publishing changes?
- [SD03-140] In a CQRS system a user submits a form and immediately sees stale data on the read side. How do you handle it?
- [SD03-141] How do you evolve the schema of immutable events in an event-sourced system?
- [SD03-142] How do you rebuild a projection from the event log without downtime, and how do snapshots help?

## Kafka
- [SD03-143] Why use Apache Kafka?
- [SD03-144] What are the responsibilities of topics, partitions, replicas, brokers, consumer groups and offsets in Kafka?
- [SD03-145] Why is Kafka so fast, considering sequential I/O, the page cache, zero-copy and batching?
- [SD03-146] How do Kafka partitions and consumer groups provide scalability, and what limits the parallelism of one consumer group?
- [SD03-147] How does Kafka replication with a leader, followers and ISR provide durability and tolerate broker failures?
- [SD03-148] What is the relationship between leader, follower, ISR, HW and LEO in Kafka?
- [SD03-149] Can Kafka lose messages? Which producer, broker and consumer settings determine it?
- [SD03-150] Which settings (acks, replication factor, min.insync.replicas, retries, offset commit strategy) are needed so that no message is lost?
- [SD03-151] With auto commit disabled, when is the right time to commit an offset, and how do you avoid both lost and duplicate processing?
- [SD03-152] Why does Kafka only guarantee ordering within a partition, and how should you choose the message key?
- [SD03-153] What problems do Kafka's idempotent producer and transactions solve, and can exactly-once cover an external database?
- [SD03-154] Is Kafka an AP or CP system in the CAP theorem, and which settings change its behaviour?
- [SD03-155] What is the role of ZooKeeper in Kafka?
- [SD03-156] Can Kafka run without ZooKeeper, and how does KRaft mode differ from the earlier ZooKeeper-based mode?
- [SD03-157] What is a consumer group rebalance, why is it risky, and how can you reduce its impact?
- [SD03-158] What happens when a consumer fails to process a message, and how do you design retry topics and a dead-letter queue?
- [SD03-159] What is the difference between log retention and log compaction in Kafka, and when would you use each?
- [SD03-160] How would you decide the number of partitions for a topic, and what goes wrong if you increase it later for a keyed topic?
- [SD03-161] Consumer lag keeps growing on one partition only. What are the possible causes and how would you investigate?
- [SD03-162] What is unclean leader election in Kafka, and what trade-off does it make between availability and durability?
- [SD03-163] How do producer batching settings such as linger.ms and batch.size trade throughput against latency?

## RabbitMQ, RocketMQ, SQS and broker features
- [SD03-164] How do exchanges, queues, bindings and routing keys work together in RabbitMQ, and what is a broker node?
- [SD03-165] What types of exchanges does RabbitMQ have (direct, fanout, topic, headers), and which scenarios suit each?
- [SD03-166] Is persisting the exchange, queue and message enough to guarantee no message is lost in RabbitMQ, and how do publisher confirms and consumer acknowledgements fit in?
- [SD03-167] What scenarios suit RabbitMQ classic queues, quorum queues and streams, and how do you provide high availability for queues?
- [SD03-168] What causes a message to be dead-lettered in a broker, and how can dead-lettering or other mechanisms implement delayed and scheduled messages?
- [SD03-169] What are the responsibilities of NameServer, Broker, Producer and Consumer in RocketMQ, and why does a broker cluster need a metadata service for routing?
- [SD03-170] What data do CommitLog, ConsumeQueue and IndexFile store in RocketMQ, and how are the queues of a topic stored?
- [SD03-171] What are synchronous and asynchronous disk flush and replication in a broker, and how do they affect durability and latency?
- [SD03-172] What is a priority queue in a message broker, and what are its drawbacks?
- [SD03-173] What metrics should you monitor on a message broker in production, such as queue depth, consumer lag and unacknowledged messages?
- [SD03-174] What is the difference between SQS standard and FIFO queues, and what duplicates or reordering should consumers of a standard queue expect?
- [SD03-175] How does the SQS visibility timeout work, and what goes wrong if it is shorter than the processing time?
- [SD03-176] How would you fan out one event to several independent consumers using SNS and SQS, and why put a queue in front of each consumer?

## SQL-backed and in-process queues
- [SD03-177] Design a message broker on top of a SQL database that supports multiple producers and consumers, exactly-one-consumer delivery, optional message expiry and high throughput.
- [SD03-178] How can SELECT FOR UPDATE SKIP LOCKED or an equivalent build a safe queue on a relational database, and what are its throughput limits?
- [SD03-179] How would you implement visibility timeouts, retries and dead-letter handling in a SQL-backed message broker?
- [SD03-180] When is a database table an acceptable queue, and when should you move to a real broker?
- [SD03-181] What is the difference between Kafka and an in-process queue such as the Disruptor?
- [SD03-182] What is a ring-buffer based in-process queue like the Disruptor, and why can it be faster than a blocking queue?

## Distributed transactions, sagas and the outbox
- [SD03-183] What is a distributed transaction, and why can't a local database transaction cover it?
- [SD03-184] Explain two-phase commit step by step and identify its main weaknesses, including blocking and the coordinator as a single point of failure.
- [SD03-185] In two-phase commit, what happens if a participant node crashes?
- [SD03-186] In two-phase commit, what happens if the coordinator itself crashes, in particular after the prepare phase?
- [SD03-187] Why is two-phase commit often avoided in modern distributed systems?
- [SD03-188] What does three-phase commit add over 2PC, why is the pre-commit phase helpful, and does it fully solve blocking?
- [SD03-189] What is TCC (Try-Confirm-Cancel), and what must each of the three operations guarantee?
- [SD03-190] What are the empty rollback, hanging and idempotency problems in TCC, and how do you handle them?
- [SD03-191] Explain the saga pattern with orchestration versus choreography, and how compensating transactions work.
- [SD03-192] A saga step in the middle fails after earlier steps have committed. How do you design compensations when they themselves might fail?
- [SD03-193] How do you implement the saga pattern with REST endpoints?
- [SD03-194] How do you handle partial failures and keep data consistent across microservices?
- [SD03-195] What strategies can be used to manage transactions across multiple microservices or in a SOA system?
- [SD03-196] Compare TCC and Saga in terms of isolation, development cost and suitability for long-running business flows.
- [SD03-197] Compare 2PC, TCC, Saga and message-based eventual consistency on consistency strength, performance and complexity, and explain rigid versus flexible transactions.
- [SD03-198] How does a local message table achieve eventual consistency across services?
- [SD03-199] How do transactional messages with half messages and check-back implement distributed transactions in a message broker?
- [SD03-200] What is the best-effort notification pattern for distributed consistency, and when is it appropriate?
- [SD03-201] An order service must deduct inventory and charge payment in two separate services. Which approach would you pick and how do you handle compensation failures?
- [SD03-202] What is the outbox pattern, and what problem does it solve between a database commit and message publication?
- [SD03-203] What is the inbox pattern, and how does it complement the outbox on the consumer side?
- [SD03-204] Why must saga participants be idempotent and tolerate a compensation arriving before the action it compensates?
- [SD03-205] Design a travel booking flow that reserves a flight, a hotel and a payment across three services as a saga, including timeouts and compensations.
