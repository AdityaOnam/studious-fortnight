---
domain: cs
topic: os_concurrency_sync_scheduling
title: OS and concurrency: synchronization, scheduling, deadlocks
tags: [os, scheduling, deadlock, concurrency, threads]
count: 115
part: 2/2
---
# OS and concurrency: synchronization, scheduling, deadlocks (part 2)

## Atomics and lock-free programming
- [CS02-148] What does it mean for an operation to be atomic, and why is a statement like count++ not atomic?
- [CS02-149] What is compare-and-swap, how do atomic classes use it, and how does it enable lock-free algorithms?
- [CS02-150] How does compare-and-swap work at the hardware level, and why is it atomic?
- [CS02-151] What is the ABA problem, and how do version stamps or tagged references address it?
- [CS02-152] What are the drawbacks of CAS under high contention, and why is it limited to a single variable?
- [CS02-153] How do adder-style accumulators achieve better throughput than a single contended atomic counter?
- [CS02-154] Compare optimistic and pessimistic locking in databases and in application code, and when each is appropriate.
- [CS02-155] How can optimistic locking be implemented with version numbers and with compare-and-swap?
- [CS02-156] What is the difference between lock-free and wait-free algorithms?
- [CS02-157] When can a lock-free design be slower than a well-chosen lock?
- [CS02-158] What is false sharing, and how does cache-line padding fix it?

## Memory model and visibility
- [CS02-159] Why is a memory model needed at the language level, and what problems do CPU caches and instruction reordering cause?
- [CS02-160] Explain the three properties of concurrent programs: atomicity, visibility and ordering.
- [CS02-161] Why can two threads on different cores see stale values of a shared variable, and what do memory barriers do?
- [CS02-162] What types of instruction reordering exist, and how do memory barriers prevent surprising results?
- [CS02-163] What is the happens-before relation, what are its main rules, and what does it guarantee between threads?
- [CS02-164] Explain the Java memory model: main memory versus working memory, atomicity, visibility, ordering and the happens-before rules.
- [CS02-165] Why do locks also provide memory-ordering guarantees, and what can go wrong with unsynchronised reads of shared data?
- [CS02-166] What does volatile guarantee, and what does it not guarantee?
- [CS02-167] How does volatile enforce visibility and prohibit reordering using memory barriers?
- [CS02-168] Why is count++ on a volatile field still unsafe?
- [CS02-169] What is the difference between synchronized and volatile?
- [CS02-170] Why does double-checked locking need a volatile field in the singleton pattern?
- [CS02-171] What are acquire and release semantics, and when is relaxed memory ordering safe?
- [CS02-172] What is safe publication of an object, and how do immutability and final fields help?

## Java locks and synchronizers
- [CS02-173] What is the difference between extending Thread and implementing Runnable, and why is the latter generally preferred?
- [CS02-174] What is the difference between Runnable and Callable, and how does a Future obtain the result?
- [CS02-175] Describe the lifecycle states of a Java thread and what causes transitions between BLOCKED, WAITING and TIMED_WAITING.
- [CS02-176] What is the difference between a lock on an object instance and a lock on the class in synchronized methods?
- [CS02-177] How does a synchronized block work at the bytecode level with monitor enter and exit instructions?
- [CS02-178] What lock optimizations does a JVM use (spinning, lock elision, coarsening, biased, lightweight and heavyweight locks), and why was biased locking removed?
- [CS02-179] Compare synchronized and ReentrantLock in features, fairness, interruptibility and condition support.
- [CS02-180] What is a fair versus unfair lock, and why is the unfair variant usually faster?
- [CS02-181] How does thread interruption work, and how should a task respond to it?
- [CS02-182] What is interruptible lock acquisition, and when would you want it?
- [CS02-183] What do wait(), notify() and notifyAll() do, and why must wait be called in a loop while holding the monitor?
- [CS02-184] Compare sleep and wait: which releases the lock, who wakes the thread, and why is wait defined on objects rather than threads?
- [CS02-185] How do await and signal on a Condition differ from wait and notify on a monitor?
- [CS02-186] How do CountDownLatch, CyclicBarrier and Semaphore differ, and when would you use each?
- [CS02-187] How would you use a semaphore to limit concurrent access to a resource?
- [CS02-188] Why can a read lock not be upgraded to a write lock while a write lock can be downgraded?
- [CS02-189] How does an optimistic read in a stamped lock work, and why can it outperform a read-write lock?
- [CS02-190] How is reentrancy tracked in a reentrant lock, and what happens when the hold count reaches zero?

## AbstractQueuedSynchronizer internals
- [CS02-191] What is the core idea of AbstractQueuedSynchronizer, built on a state variable and a CLH-style wait queue?
- [CS02-192] Why does AQS use a variant of the CLH lock queue?
- [CS02-193] Walk through how a thread acquires an exclusive lock in AQS: CAS on state, enqueueing, parking and wake-up on release.
- [CS02-194] What is the difference between exclusive and shared modes in a queued synchronizer?
- [CS02-195] Why do AQS nodes need different wait states, and how are cancelled waiters handled?
- [CS02-196] In AQS, how are cancelled nodes generated in shouldParkAfterFailedAcquire, and when is a node's waitStatus set to -1?
- [CS02-197] How would you implement a custom non-reentrant mutex or a bounded resource gate on top of a synchronizer framework?

## ThreadLocal
- [CS02-198] What is ThreadLocal, and how is it implemented internally with a per-thread map, including collision handling?
- [CS02-199] Why is the key of a ThreadLocal entry designed as a weak reference?
- [CS02-200] What memory-leak risk does ThreadLocal carry in thread pools, and why must you clean it up at the end of a task?
- [CS02-201] How can you propagate thread-local context to child threads or to tasks submitted to a thread pool?

## Thread pools and executors
- [CS02-202] What is a thread pool, and why is it better than creating a new thread per task?
- [CS02-203] What is the difference between Executor and ExecutorService?
- [CS02-204] How do you size a thread pool for CPU-bound versus I/O-bound workloads?
- [CS02-205] How would you size a thread pool and its queue given downstream capacity limits and a latency SLO?
- [CS02-206] Explain the core parameters of a configurable thread pool: core size, max size, queue, keep-alive and rejection policy.
- [CS02-207] In what order does a thread pool use core threads, the queue and extra threads as tasks arrive?
- [CS02-208] Why are the factory-method built-in thread pools discouraged in production?
- [CS02-209] Compare bounded and unbounded queues for a thread pool, and the failure modes of each.
- [CS02-210] What happens when the pool's queue is full and maximum threads are running? Compare the common rejection policies.
- [CS02-211] Can caller-runs rejection provide backpressure, and what are its risks?
- [CS02-212] What happens to a worker thread when a task throws an uncaught exception, and why are exceptions in async tasks easily lost?
- [CS02-213] Why should different workloads use isolated thread pools?
- [CS02-214] Does cancelling a task or hitting a timeout actually stop the running thread? How do you make tasks cooperatively cancellable?
- [CS02-215] What metrics should you monitor on a thread pool in production?
- [CS02-216] How do you gracefully shut down a thread pool, and how does shutdown differ from an immediate shutdown?
- [CS02-217] How would you dynamically adjust thread pool parameters at runtime, and what are the limits of doing so?
- [CS02-218] How would you design a thread pool that executes tasks by priority?
- [CS02-219] Why name threads in a pool, and how does it help diagnose production problems?
- [CS02-220] Do core threads in a pool ever get reclaimed, and how does a worker thread loop pull tasks?
- [CS02-221] What is the fork/join framework, and how does work stealing improve CPU utilization?

## Futures, CompletableFuture and virtual threads
- [CS02-222] What is the difference between a Future and a CompletableFuture, and what limitations of blocking futures does the latter address?
- [CS02-223] How would you run two independent async tasks and combine their results in a third task that depends on both?
- [CS02-224] How do you handle failures in a chain of async tasks, and how does exception propagation work?
- [CS02-225] Why should async tasks run on a custom executor rather than the shared default pool?
- [CS02-226] How do you wait for many async tasks and apply a timeout without blocking indefinitely?
- [CS02-227] What is a virtual thread, and how does it differ from a platform thread?
- [CS02-228] Why are virtual threads well suited to I/O-bound workloads but not CPU-bound ones?
- [CS02-229] How does a virtual thread get mounted on and unmounted from a carrier thread, and what is pinning?
- [CS02-230] Can synchronized still be used with virtual threads in JDK 21?
- [CS02-231] Should virtual threads be pooled, and how do you limit downstream concurrency without a thread pool?
- [CS02-232] Are virtual threads the same as coroutines, and how do they compare with reactive programming?
- [CS02-233] What caveats arise when using thread-locals or connection pools with a very large number of lightweight threads?
- [CS02-234] How would you migrate a service from a fixed platform thread pool to per-task lightweight threads, and what would you re-verify?
- [CS02-235] How would you diagnose virtual-thread pinning and read thread dumps in production?

## Python GIL, asyncio and Go concurrency
- [CS02-236] What is the Python GIL, why does it exist, and which workloads does it hurt?
- [CS02-237] Can Python threads use multiple CPU cores, and what are the alternatives for CPU-bound parallelism?
- [CS02-238] Why is the GIL placed at the interpreter level instead of using fine-grained locks, and what trade-off did that make?
- [CS02-239] Is a statement such as x += 1 thread-safe in CPython despite the GIL? Explain.
- [CS02-240] What changes with free-threaded (no-GIL) Python, and what code would break or need new locking?
- [CS02-241] What is the difference between threads and async/await, and when would you choose each?
- [CS02-242] When would you choose threading, multiprocessing or asyncio in Python for a mixed I/O and CPU workload?
- [CS02-243] What happens if you make a blocking call inside a coroutine, and how do you find and fix it?
- [CS02-244] What are best practices for Python asyncio / async-await in AI applications?
- [CS02-245] How would you build an async batch processor over an API with concurrency limits, retries with jitter and error isolation?
- [CS02-246] How do goroutines differ from OS threads, and how does the Go scheduler multiplex them?
- [CS02-247] When would you use channels versus a mutex in Go?
- [CS02-248] How do you use the worker pool pattern in Go to handle highly concurrent LLM requests, and what are the common pitfalls?
- [CS02-249] What causes goroutine leaks, and how do context cancellation and select help prevent them?
- [CS02-250] What is the difference between buffered and unbuffered channels, and what causes "all goroutines are asleep - deadlock"?

## I/O models and event-driven servers
- [CS02-251] Compare blocking and non-blocking I/O, and synchronous and asynchronous I/O, using the four combinations.
- [CS02-252] Explain the five Unix I/O models: blocking, non-blocking, I/O multiplexing, signal-driven and asynchronous.
- [CS02-253] Which of the five I/O models are synchronous and which are asynchronous, and why?
- [CS02-254] In a non-blocking synchronous model, what does the caller do while waiting, and why is polling wasteful?
- [CS02-255] Compare select, poll and epoll in scalability, data copying and number of file descriptors.
- [CS02-256] What is the difference between level-triggered and edge-triggered modes in epoll, and what pitfalls does edge-triggered mode have?
- [CS02-257] In what scenarios is epoll not much better than select, and why?
- [CS02-258] Why can one thread with epoll serve thousands of connections while a thread-per-connection model cannot?
- [CS02-259] What is the C10K problem, and what architectures address it?
- [CS02-260] How would you design a high-concurrency server using the Reactor pattern with I/O multiplexing and a worker thread pool?
- [CS02-261] What is the Reactor model, and how does it differ from Proactor?
- [CS02-262] Why are non-blocking I/O operations a necessity in reactive programming, and what problems do they solve?
