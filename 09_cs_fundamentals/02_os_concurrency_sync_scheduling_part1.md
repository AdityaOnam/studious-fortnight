---
domain: cs
topic: os_concurrency_sync_scheduling
title: OS and concurrency: synchronization, scheduling, deadlocks
tags: [os, scheduling, deadlock, concurrency, threads]
count: 147
part: 1/2
---
# OS and concurrency: synchronization, scheduling, deadlocks (part 1)

## Threads and concurrency fundamentals
- [CS02-001] What is the difference between concurrency and parallelism, and between synchronous and asynchronous execution?
- [CS02-002] What is the difference between a process and a thread, and why are threads called lightweight?
- [CS02-003] What state is shared between the threads of one process, and what is private to each thread?
- [CS02-004] What are the advantages of multithreading, and when is it particularly useful?
- [CS02-005] What is the difference between multithreading and multiprocessing, and why might you choose threads over processes?
- [CS02-006] When is multithreading beneficial for CPU-bound versus I/O-bound workloads?
- [CS02-007] Does multithreading help on a single-core CPU? When can adding more threads make a program slower?
- [CS02-008] When can parallelism make your algorithms run faster, and when can it make them run slower?
- [CS02-009] If 20% of a program is inherently serial, what is the maximum speedup on 16 cores, and what does Amdahl's law imply for design?
- [CS02-010] How would you parallelize merge sort across threads, and at what point does parallelism stop paying off?
- [CS02-011] What is a thread context switch, and what does it cost?
- [CS02-012] How do user-level threads relate to kernel threads, and what are the common mapping models (1:1, M:1, M:N)?
- [CS02-013] What are the typical states in a thread lifecycle, and what events cause transitions between them?
- [CS02-014] What does it mean for code to be thread-safe, and what techniques make a class thread-safe?
- [CS02-015] What problems can multithreading introduce, such as deadlocks, memory leaks and context-switch overhead?
- [CS02-016] What are the benefits and disadvantages of many small threads versus a few large threads?
- [CS02-017] What happens if multiple threads access the same static or global variable without coordination?
- [CS02-018] What is a daemon thread, and when would you use one?
- [CS02-019] What happens if you call a thread's run method directly instead of starting the thread?
- [CS02-020] What are good practices for writing multithreaded code, such as naming threads, minimizing lock scope and preferring concurrent collections?

## CPU scheduling
- [CS02-021] What is CPU scheduling, and why does an operating system need a scheduler?
- [CS02-022] What is the ready queue?
- [CS02-023] What is the difference between preemptive and non-preemptive scheduling, and why is preemption useful?
- [CS02-024] What happens to a process that blocks on I/O, and what other events make a task leave the CPU?
- [CS02-025] Define CPU utilization, throughput, turnaround time, waiting time and response time as scheduling criteria.
- [CS02-026] Which metrics do schedulers optimise, and why do throughput, response time and fairness conflict?
- [CS02-027] Given processes with arrival and burst times, how do you compute average waiting time and turnaround time under FCFS?
- [CS02-028] Why is FCFS scheduling non-preemptive, and what are its drawbacks?
- [CS02-029] What is the convoy effect in FCFS scheduling?
- [CS02-030] Compare FCFS, SJF, SRTF, priority and Round Robin scheduling and their trade-offs.
- [CS02-031] Why is SJF optimal for average waiting time, and why can it not be implemented exactly in practice?
- [CS02-032] How does SRTF differ from SJF, and how can a scheduler estimate the next CPU burst length?
- [CS02-033] What are the advantages and disadvantages of Round Robin scheduling?
- [CS02-034] How does the choice of time quantum affect Round Robin throughput and response time?
- [CS02-035] If a context switch takes 1 ms and the Round Robin quantum is 10 ms, what fraction of CPU time is lost to switching, and how does it change at 2 ms?
- [CS02-036] Why can starvation occur in priority scheduling or SJF, and how can it be prevented?
- [CS02-037] How does aging work, and why is it needed in scheduling?
- [CS02-038] What is a multilevel feedback queue, how does it work, and what problems does it solve?
- [CS02-039] What distinguishes real-time scheduling from interactive scheduling, and how do EDF and rate-monotonic scheduling differ?
- [CS02-040] How do cooperative and preemptive scheduling differ, and what are the implications for coroutine-based runtimes?
- [CS02-041] How does the Linux CFS scheduler pick the next task, and what motivated the move toward EEVDF?
- [CS02-042] How do multicore schedulers handle per-CPU run queues and load balancing, and what is the cost of migrating a task?
- [CS02-043] What is CPU affinity, and why might pinning threads to cores improve performance?
- [CS02-044] A service shows high load average but low CPU utilisation. What can cause this, and how do you tell load average from CPU utilisation?
- [CS02-045] You receive a CPU alert on a production host. How do you tell whether user code, kernel, I/O wait or run-queue contention is responsible?

## Race conditions and critical sections
- [CS02-046] What is a race condition? Give an example with two threads incrementing a shared counter.
- [CS02-047] Why is a race condition called a "race"?
- [CS02-048] What is the difference between a race condition and a data race?
- [CS02-049] How can race conditions be prevented or eliminated, for example in the shared counter case?
- [CS02-050] What is a critical section, and why is it important in concurrent programming?
- [CS02-051] What properties must a correct solution to the critical-section problem satisfy?
- [CS02-052] Is a critical section always protected by a lock?
- [CS02-053] What is the difference between synchronization and mutual exclusion?
- [CS02-054] How does an operating system ensure mutual exclusion among concurrent processes?
- [CS02-055] What are the advantages and disadvantages of Peterson's algorithm?
- [CS02-056] Why do hardware primitives such as test-and-set matter for mutual exclusion, and why is disabling interrupts not a general solution?
- [CS02-057] What are the different ways threads can be synchronized (mutex, condition variable, semaphore, event, read-write lock), and when do you use each?
- [CS02-058] What is the difference between coarse-grained and fine-grained locking, and when does each pay off?
- [CS02-059] What is lock contention, and how can you reduce it by shrinking critical sections or sharding locks?
- [CS02-060] What common mistakes occur when using locks, such as holding a lock across blocking I/O or forgetting to unlock on error paths?
- [CS02-061] When would you choose try-lock or timed locking over blocking lock acquisition?
- [CS02-062] What is the thundering herd problem, and how can it be mitigated in locks or caches?
- [CS02-063] In an annotation platform, two annotators submit the same task simultaneously from different workers. Where is the race condition, and how do you fix it?
- [CS02-064] How do you make a rate limiter safe under concurrent calls?
- [CS02-065] What changes in an in-memory key-value store with transactions if two threads share the store?
- [CS02-066] How would you swap a frequently updated CIDR allow/deny rule set safely while lookups continue concurrently?
- [CS02-067] Which tools, such as ThreadSanitizer, detect data races, and what are their limits?
- [CS02-068] A fix compiles and passes tests, but you suspect a data race. How do you prove it either way?

## Mutexes, semaphores and spinlocks
- [CS02-069] Why do we need a mutex, and how does it work?
- [CS02-070] What happens when another thread tries to acquire a mutex that is already locked?
- [CS02-071] What is a semaphore, why do we need one, and how does it work?
- [CS02-072] What is the difference between a mutex and a semaphore?
- [CS02-073] What is a binary semaphore, and how does it differ from a mutex regarding ownership?
- [CS02-074] When should you use a mutex, and when should you use a semaphore?
- [CS02-075] Why can't we simply use a mutex to manage three identical resources, and what happens if we try?
- [CS02-076] What happens if we use Semaphore(3) to protect a shared counter?
- [CS02-077] Can a semaphore's value be negative?
- [CS02-078] What happens if you call sem_post() more times than sem_wait()?
- [CS02-079] How would you implement a mutex using an atomic test-and-set instruction or using a semaphore?
- [CS02-080] What is busy waiting, and why is it usually undesirable?
- [CS02-081] What is a spinlock, and when is it preferable to a blocking mutex?
- [CS02-082] Why do spinlocks make sense on multicore systems but not on single-core systems?
- [CS02-083] Compare a mutex, a semaphore and a spinlock.
- [CS02-084] What problems do mutexes, semaphores, condition variables, spinlocks and futexes each solve?
- [CS02-085] What is a futex, and how does it avoid system calls in the uncontended case?
- [CS02-086] What is priority inversion, how can it occur with locks, and how do priority inheritance protocols prevent it?

## Monitors, condition variables and lock types
- [CS02-087] Why do we need monitors?
- [CS02-088] Why is wait() special in a monitor?
- [CS02-089] How is a monitor different from a mutex, and can a monitor use a mutex internally?
- [CS02-090] What is a monitor, and how does it improve on raw semaphores for writing correct concurrent code?
- [CS02-091] What is a condition variable, and why must it be used with a mutex and a while-loop predicate check instead of busy waiting?
- [CS02-092] What is a spurious wakeup, and how do you handle it?
- [CS02-093] What is a lost wakeup, and how can it arise when using condition variables?
- [CS02-094] What is a barrier, and how would you build a reusable one from a mutex and a condition variable?
- [CS02-095] What is a reentrant lock, and what problem does it solve compared with a non-reentrant mutex?
- [CS02-096] What is a read-write lock, and when does it help or hurt throughput?

## Classic synchronization problems
- [CS02-097] In the semaphore-based bounded-buffer solution, what roles do the empty, full and mutex semaphores play?
- [CS02-098] Explain the producer-consumer (bounded buffer) problem and how to solve it with semaphores or a mutex plus condition variables.
- [CS02-099] What happens if you swap the order of the wait operations in the semaphore-based producer-consumer solution?
- [CS02-100] How would you modify the producer-consumer solution to handle multiple producers and consumers?
- [CS02-101] How do bounded queues provide back-pressure in a producer-consumer design?
- [CS02-102] Explain the dining philosophers problem and at least two ways to avoid deadlock in it.
- [CS02-103] Why is resource ordering important in the dining philosophers problem?
- [CS02-104] Explain the readers-writers problem and the trade-off between reader preference and writer preference.
- [CS02-105] What is the difference between the first and second readers-writers solutions?
- [CS02-106] How would you modify a readers-writers solution so that writers cannot starve?
- [CS02-107] In the sleeping barber problem, why do we need the access_seats semaphore?

## Concurrent data structures and design problems
- [CS02-108] How do you make a collection such as an ArrayList thread-safe, and what are the options?
- [CS02-109] How does a copy-on-write list achieve thread safety, and when is it a good or bad choice?
- [CS02-110] How does a BlockingQueue simplify producer-consumer designs, and how do bounded, unbounded and synchronous queues differ?
- [CS02-111] How do you implement a thread-safe bounded blocking queue with a lock and condition variables, avoiding lost wakeups?
- [CS02-112] Compare array-backed and linked blocking queues in terms of bounding, locking and throughput.
- [CS02-113] What are the differences among offer, put, add and timed-offer on a blocking queue?
- [CS02-114] How do blocking and non-blocking queue algorithms differ, and how would you implement a non-blocking queue?
- [CS02-115] What is a concurrent skip list, and when is it preferable to a concurrent hash map?
- [CS02-116] Design a concurrent hash map. How do lock striping, per-bucket locks and lock-free approaches differ?
- [CS02-117] Design a thread-safe cache with TTL expiry. How do you handle expiry cleanup and concurrent reads and writes?
- [CS02-118] Design a concurrent Bloom filter. How would you make bit-set updates thread-safe without a global lock?
- [CS02-119] Design a thread-safe LRU cache. Where does lock contention appear and how would you reduce it?
- [CS02-120] Design a thread-safe batching logger where many producers call log(msg) and a background thread flushes up to 100 messages every second or when full.
- [CS02-121] In a thread-safe batching logger, what changes if the sink can fail? Where do retries live and what happens to ordering?
- [CS02-122] How would you drop messages under overload in a batching logger without blocking producers?

## Deadlock, livelock and starvation
- [CS02-123] What is a deadlock?
- [CS02-124] What are the four necessary conditions for deadlock?
- [CS02-125] How do the four deadlock conditions work together?
- [CS02-126] Can a single thread deadlock with itself, and under what lock type does that happen?
- [CS02-127] How can two threads deadlock with two locks, and why does a global lock ordering remove the problem?
- [CS02-128] Two threads transfer money between two accounts in opposite directions and occasionally hang. Explain why and fix it.
- [CS02-129] What are the strategies for dealing with deadlock (prevention, avoidance, detection and recovery, ignoring), and what is an example technique of each?
- [CS02-130] What is the difference between deadlock prevention, avoidance and detection?
- [CS02-131] How do you prevent deadlock by breaking each of the four necessary conditions, and which approach is practical?
- [CS02-132] What coding practices reduce deadlock risk, such as lock ordering, timeouts and not calling unknown code while holding a lock?
- [CS02-133] What is a safe state in deadlock avoidance?
- [CS02-134] Explain the Banker's algorithm with an example.
- [CS02-135] Given an allocation matrix, a maximum-demand matrix and available resources for several processes, how do you find a safe sequence?
- [CS02-136] What are the practical limitations of the Banker's algorithm?
- [CS02-137] How does deadlock detection with a resource allocation graph or wait-for graph work, including multiple instances of a resource?
- [CS02-138] Is a cycle in a resource allocation graph always a deadlock?
- [CS02-139] What happens after a deadlock is detected, and what are the recovery options and their costs?
- [CS02-140] Why do many general-purpose operating systems simply ignore deadlocks?
- [CS02-141] What are the trade-offs between different deadlock handling approaches?
- [CS02-142] Why is deadlock difficult to debug?
- [CS02-143] What is a livelock, and how does it differ from a deadlock?
- [CS02-144] What is the difference between deadlock, livelock and starvation? Give an example of each.
- [CS02-145] A service hangs under load with no CPU usage and thread dumps show threads waiting on locks. How do you confirm a lock-ordering deadlock and fix it?
- [CS02-146] How can deadlocks arise in a database, and how do databases detect and resolve them?
- [CS02-147] Does lock-free programming eliminate deadlock, and what other liveness problems can remain?
