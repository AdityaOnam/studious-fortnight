---
domain: cs
topic: operating_systems_processes_memory
title: Operating systems: processes, threads, memory
tags: [os, process, memory, paging]
count: 103
part: 2/2
---
# Operating systems: processes, threads, memory (part 2)

## Page tables, TLB and page faults
- [CS01-090] What is a page table, and why are multi-level page tables used instead of a single flat one?
- [CS01-091] What are the advantages and disadvantages of hierarchical paging?
- [CS01-092] With 32-bit addresses, 4 KB pages and 4-byte entries, how large is a flat page table per process, and how does a two-level table reduce it?
- [CS01-093] What information does a page table entry hold, such as present, dirty, referenced and protection bits?
- [CS01-094] What are the trade-offs of choosing a larger or smaller page size?
- [CS01-095] What are huge pages, and when do they help or hurt performance?
- [CS01-096] What is a TLB, and why is it important?
- [CS01-097] Describe the address translation flow when a TLB is used. What happens on a TLB miss compared with a page fault?
- [CS01-098] How does the TLB hit rate affect the effective memory access time?
- [CS01-099] Given a TLB hit rate of 95%, a 10 ns TLB lookup and a 100 ns memory access with a single-level page table, what is the effective access time?
- [CS01-100] Why does a context switch often require flushing the TLB, and how do address-space identifiers (ASIDs) help?
- [CS01-101] What is a page fault, and why does it occur?
- [CS01-102] How is a page fault handled, step by step, when the page must be loaded from disk?
- [CS01-103] Why are page faults expensive?
- [CS01-104] Why is a page fault sometimes normal behaviour and sometimes turns into a SIGSEGV? How does the OS tell them apart?
- [CS01-105] What is the difference between a major (hard) page fault and a minor (soft) page fault?
- [CS01-106] What is demand paging, and what are its advantages and risks?

## Page replacement, thrashing and swap
- [CS01-107] What is page replacement, and why is it needed?
- [CS01-108] What happens when RAM is full in a virtual memory system?
- [CS01-109] In page replacement, why does the choice of victim page matter?
- [CS01-110] What is the difference between FIFO and LRU page replacement?
- [CS01-111] Compare FIFO, LRU, LFU, second-chance and Optimal page replacement.
- [CS01-112] What is Belady's anomaly, and which page replacement algorithms suffer from it?
- [CS01-113] Why is the Optimal page replacement algorithm mostly theoretical?
- [CS01-114] How does the Clock algorithm approximate LRU using hardware reference bits?
- [CS01-115] Why is true LRU hard to implement in hardware, and what approximations are used?
- [CS01-116] What factors affect the choice of page replacement algorithm?
- [CS01-117] For the reference string 7,0,1,2,0,3,0,4,2,3,0,3,2 with 3 frames, how many page faults occur under FIFO and under LRU?
- [CS01-118] What is the difference between global and local page replacement, and how does each affect other processes?
- [CS01-119] How does the Not Recently Used (NRU) or enhanced second-chance algorithm use the reference and dirty bits?
- [CS01-120] What is thrashing, and what causes it?
- [CS01-121] What happens to CPU utilization during thrashing?
- [CS01-122] Why can a global replacement policy make thrashing worse and create a downward spiral?
- [CS01-123] How can you detect thrashing in a running system?
- [CS01-124] What is the working set model, and how does it help prevent thrashing?
- [CS01-125] How do you fix or recover from thrashing, and how do the main anti-thrashing strategies compare?
- [CS01-126] Can thrashing happen even when the swap device is an SSD?
- [CS01-127] What is swap, when should it be enabled or disabled on a database or JVM server, and what are the trade-offs?

## Process memory, fragmentation and allocation
- [CS01-128] What are the main segments of a process address space (text, data, BSS, heap, stack), and in which direction does each grow?
- [CS01-129] What is the difference between stack memory and heap memory in allocation speed, lifetime and fragmentation?
- [CS01-130] Why does deep recursion cause a stack overflow, and what happens to the stack and heap when memory is never freed?
- [CS01-131] Can heap memory outlive the function that allocated it, and is heap memory shared between threads?
- [CS01-132] Is a local variable always stored on the stack? When might it live on the heap or in a register?
- [CS01-133] What happens if heap memory is never released?
- [CS01-134] What is the difference between internal and external fragmentation?
- [CS01-135] How can fragmentation be reduced, and which allocation algorithms minimise external fragmentation?
- [CS01-136] How does memory compaction solve external fragmentation, and what does it cost?
- [CS01-137] Compare First Fit, Best Fit and Worst Fit allocation strategies.
- [CS01-138] How does the buddy system work, and what are its advantages and disadvantages?
- [CS01-139] What is a memory pool, and when would you use one?
- [CS01-140] How do you measure and monitor memory fragmentation in a running system?
- [CS01-141] How does the OS allocate memory to a process through brk and mmap, and how do user-space allocators such as malloc build on them?
- [CS01-142] What do VSZ, RSS and PSS each represent when measuring process memory?
- [CS01-143] What is memory overcommit in Linux, and how does it relate to the OOM killer?
- [CS01-144] A process's allocation succeeds but the process is later killed by the OOM killer. How is that possible and how do you investigate?
- [CS01-145] A server's memory usage keeps growing, but heap profiling shows no leaks. What OS-level causes could explain it?
- [CS01-146] Why does malloc of a very large block succeed instantly, yet memory only increases as pages are touched?
- [CS01-147] Why does cache locality matter for performance, and how do temporal and spatial locality relate to caching and virtual memory?
- [CS01-148] What is the memory hierarchy, why does it exist, and how do L1, L2 and L3 caches differ?
- [CS01-149] Compare direct-mapped, set-associative and fully associative caches.
- [CS01-150] Explain write-through versus write-back cache policies and their trade-offs.
- [CS01-151] What are the three types of cache misses?
- [CS01-152] What is false sharing between cores, and how can it degrade performance?

## File systems and disks
- [CS01-153] What is a file system, and how are files and directories organized on disk?
- [CS01-154] What do a file system's inode, directory entry (dentry) and file name each represent?
- [CS01-155] What is an inode, what metadata does it store, and how does a Unix file system find the data blocks of a file?
- [CS01-156] What happens in the kernel when a process opens a file by path?
- [CS01-157] Compare contiguous, linked and indexed allocation of file blocks on disk.
- [CS01-158] How can a file system track free space? Compare bitmaps and free lists.
- [CS01-159] What is the difference between a symbolic link and a hard link?
- [CS01-160] What happens to a hard link and a soft link when the original file is deleted?
- [CS01-161] Why can't a hard link cross file systems?
- [CS01-162] What is the VFS layer, and what problem does it solve?
- [CS01-163] What is a mount point, and how does the kernel combine multiple file systems into one directory tree?
- [CS01-164] What is the difference between a file descriptor, an open file description and an inode?
- [CS01-165] What is the page cache, and how does it affect file read and write performance?
- [CS01-166] After write() returns successfully, is the data on disk? What do fsync and O_DIRECT change, and how do you design for durability?
- [CS01-167] Why do modern file systems use journaling, and how does a journal protect against corruption after a crash?
- [CS01-168] A disk reports free space but file creation fails. What could be the cause?
- [CS01-169] You delete a large file, but disk usage does not drop. What is happening and how do you fix it?
- [CS01-170] What is the physical structure of a hard disk, and what are the components of disk access time?
- [CS01-171] Compare FCFS, SSTF, SCAN and C-SCAN disk scheduling. Which can cause starvation and why do these algorithms exist?
- [CS01-172] What is RAID, and what are the common RAID levels?
- [CS01-173] Why do disk scheduling algorithms matter less on SSDs, and how do SSDs differ from HDDs for the OS?

## Interrupts, I/O models and zero-copy
- [CS01-174] What is an interrupt, and how does the CPU handle one?
- [CS01-175] Distinguish hardware interrupts from software interrupts with examples.
- [CS01-176] How does the timer interrupt enable preemptive multitasking?
- [CS01-177] What are the top half and bottom half of interrupt handling, and why can't an interrupt handler sleep?
- [CS01-178] What is interrupt livelock, and how do mechanisms like NAPI or interrupt coalescing address it?
- [CS01-179] Why is polling sometimes preferred over interrupt-driven I/O?
- [CS01-180] What are the differences between DMA, interrupt-driven and CPU-driven (programmed) I/O?
- [CS01-181] Trace what happens inside the kernel when a user process calls a blocking read() on a file or socket.
- [CS01-182] What is the difference between synchronous, asynchronous, blocking and non-blocking I/O?
- [CS01-183] Compare the five Unix I/O models: blocking, non-blocking, I/O multiplexing, signal-driven and asynchronous.
- [CS01-184] What is the difference between select, poll and epoll, and why does epoll scale better with many connections?
- [CS01-185] Explain level-triggered versus edge-triggered epoll and the pitfalls of edge-triggered mode.
- [CS01-186] Is epoll always the best choice? In which situations does it give little benefit?
- [CS01-187] How would you build a server that handles 100k concurrent connections on Linux? Discuss threads, event loops and kernel limits.
- [CS01-188] What does mmap do, how does it differ from read/write, and where is shared memory built on it?
- [CS01-189] What is zero-copy, and which copies does the term eliminate?
- [CS01-190] Count the data copies and context switches in a traditional read-then-write file transfer.
- [CS01-191] Compare mmap+write, sendfile and splice for zero-copy transfer. What does DMA scatter-gather add?
- [CS01-192] Why does a message broker such as Kafka benefit from sendfile when serving consumers, and when does it not help, for example with TLS?
