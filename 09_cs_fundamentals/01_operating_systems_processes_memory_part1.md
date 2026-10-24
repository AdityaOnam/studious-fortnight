---
domain: cs
topic: operating_systems_processes_memory
title: Operating systems: processes, threads, memory
tags: [os, process, memory, paging]
count: 89
part: 1/2
---
# Operating systems: processes, threads, memory (part 1)

## OS basics, kernel design and system calls
- [CS01-001] What is an operating system, and what are its main functions?
- [CS01-002] What are the main types of operating systems, such as batch, time-sharing, real-time and distributed?
- [CS01-003] What is a device driver, and why does an operating system need one?
- [CS01-004] What is multiprocessing, where two or more CPUs run programs at the same time and share the work?
- [CS01-005] Why is the OS described as a resource manager and as an abstraction layer between hardware and applications?
- [CS01-006] What is a kernel, and how does a monolithic kernel differ from a microkernel?
- [CS01-007] Compare a monolithic kernel with a microkernel in terms of performance, isolation and fault tolerance.
- [CS01-008] Why do microkernel designs place so much emphasis on IPC performance?
- [CS01-009] What is the difference between user mode and kernel mode, and why does the CPU need both?
- [CS01-010] Which events cause the CPU to switch from user mode to kernel mode?
- [CS01-011] What is a system call, and what are some common examples?
- [CS01-012] Why can't user programs simply call kernel functions directly?
- [CS01-013] Walk through what happens at the hardware and kernel level when a user program invokes a system call such as read().
- [CS01-014] How does a system call differ from an ordinary function call, and why is it more expensive?
- [CS01-015] How do interrupts, exceptions, traps, faults and system calls differ, and which of them does a system call use?
- [CS01-016] What does a boot loader do, and what happens between power-on and the OS taking control?
- [CS01-017] Compare MBR and GPT partition tables.
- [CS01-018] What is a hypervisor, and how do Type 1 and Type 2 hypervisors differ?
- [CS01-019] Why use a virtual machine, and how does a virtual machine work?
- [CS01-020] How do containers differ from virtual machines from the operating system's point of view?

## Processes and process lifecycle
- [CS01-021] What is the difference between a program and a process?
- [CS01-022] What does a process contain?
- [CS01-023] What is a Process Control Block (PCB), what information does it hold, and why is it important?
- [CS01-024] Describe the process state transition diagram and the events that cause each transition.
- [CS01-025] What is the difference between the Ready and Waiting states, and what causes a running process to move to each?
- [CS01-026] Explain suspended process states and why an OS needs them.
- [CS01-027] What do fork, exec and wait each do in Linux?
- [CS01-028] What does fork() return in the parent and in the child, and how is the return value used?
- [CS01-029] What does fork() actually do, and how does copy-on-write make it cheap?
- [CS01-030] What happens to a process's memory and file descriptors when it forks and when it calls exec?
- [CS01-031] What is an orphan process and what is a zombie process? How does each get cleaned up?
- [CS01-032] How can zombie processes accumulate on a server, and how do you detect and prevent it?
- [CS01-033] What is SIGCHLD used for, and how do wait() and waitpid() differ?
- [CS01-034] How does the Linux kernel deliver a signal to a process, and which signals cannot be caught?
- [CS01-035] What is the difference between load average and CPU utilization?
- [CS01-036] What happens to a process's resources, such as memory, file descriptors and locks, when it exits or is killed?
- [CS01-037] Why does the PID 1 process in a container matter for zombie reaping and signal handling?
- [CS01-038] A process is stuck in uninterruptible sleep (state D) and cannot be killed. What causes this and how do you investigate it?

## Threads and context switching
- [CS01-039] Why do we need threads when we already have processes?
- [CS01-040] What is the difference between a process and a thread?
- [CS01-041] Which resources do threads of the same process share, and which are private to each thread?
- [CS01-042] When would you choose a multi-process design over a multi-threaded one, and vice versa?
- [CS01-043] Why is creating a thread faster than creating a process?
- [CS01-044] What happens when one thread crashes compared with when a process crashes?
- [CS01-045] What is a Thread Control Block (TCB), and how does it relate to a PCB?
- [CS01-046] How does the operating system create and manage threads, for example what do pthread_create and clone() do on Linux?
- [CS01-047] What is the difference between a user-level thread and a kernel-level thread?
- [CS01-048] Compare user-level, kernel-level and hybrid threading models. What do many-to-one and one-to-one mappings imply?
- [CS01-049] What are coroutines, fibers and virtual threads, and how do they differ from kernel threads in scheduling, stack usage and switch cost?
- [CS01-050] Does adding more threads always make a program faster? What causes multithreading to hurt performance?
- [CS01-051] How is thread-local storage implemented and where does it live in a process?
- [CS01-052] How are threads represented inside the Linux kernel, and what role do the clone() flags play?
- [CS01-053] What is context switching, and why is it needed?
- [CS01-054] What exactly happens during a context switch, and what state is saved and restored?
- [CS01-055] Why is a context switch costly? Consider cache and TLB effects and the impact on concurrency.
- [CS01-056] Why is a context switch between threads of the same process cheaper than one between two processes?
- [CS01-057] How can excessive context switching be reduced?
- [CS01-058] A service shows very high context-switch rates and poor throughput. How would you confirm it and find the cause?

## Inter-process communication
- [CS01-059] What is inter-process communication and why is it needed?
- [CS01-060] List the main IPC mechanisms and when you would choose each.
- [CS01-061] What is the difference between an anonymous pipe and a named pipe?
- [CS01-062] Compare pipes, named pipes, message queues, sockets and shared memory for IPC. Which ones need explicit synchronisation?
- [CS01-063] What are the advantages and disadvantages of shared memory versus message passing?
- [CS01-064] Why is shared memory the fastest IPC mechanism, and what extra problem does it introduce?
- [CS01-065] When would you use pipes versus sockets?
- [CS01-066] When would you use Unix domain sockets rather than TCP sockets between local processes?
- [CS01-067] How do two processes on different machines communicate, and how does that differ from local IPC?
- [CS01-068] What is the difference between a semaphore and a signal when used for process coordination?
- [CS01-069] What happens if a process dies while holding a system resource such as a message queue or shared memory segment?
- [CS01-070] What happens when you write to a full pipe, read from an empty pipe, or write after the read end is closed?
- [CS01-071] How would you design IPC between a high-throughput producer process and a consumer process on the same machine?

## Virtual memory, paging and segmentation
- [CS01-072] What is virtual memory, why do we need it, and what problems does it solve?
- [CS01-073] How does virtual memory work, and what happens when a page is not in RAM?
- [CS01-074] How does virtual memory give processes isolation while still allowing controlled sharing?
- [CS01-075] What is the role of the MMU, and how is a virtual address translated into a physical address?
- [CS01-076] What is the difference between a logical (virtual) address and a physical address?
- [CS01-077] What is paging, and why do we need it?
- [CS01-078] How does address translation work in a paging system?
- [CS01-079] Given a 32-bit virtual address and 4 KB pages, how is the address split into page number and offset?
- [CS01-080] Why does paging eliminate external fragmentation, and which kind of fragmentation does it still suffer from?
- [CS01-081] What is the difference between paging and segmentation?
- [CS01-082] Why is segmentation used in memory management?
- [CS01-083] What are the advantages and disadvantages of segmentation, and how does it compare with paging?
- [CS01-084] How does address translation work in segmentation?
- [CS01-085] In segmentation, what happens if the offset exceeds the segment limit?
- [CS01-086] How are shared segments implemented in a segmentation system?
- [CS01-087] What is external fragmentation in segmentation and how can it be solved?
- [CS01-088] What is segmented paging, and which advantages of each scheme does it combine?
- [CS01-089] How do page protection bits, such as read, write and execute-disable, protect memory?
