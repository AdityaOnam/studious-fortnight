---
domain: cs
topic: programming_langs_python_java_cpp
title: Programming language internals: Python, Java, C++
tags: [python, java, cpp, jvm, big-o]
count: 146
part: 1/2
---
# Programming language internals: Python, Java, C++ (part 1)

## Compilation, complexity and algorithm concepts
- [CS07-001] How does a program written in C++, Java or Python get from source code to execution, and how do compiled, interpreted and VM-based runtimes differ?
- [CS07-002] What are the pros and cons of compiled, interpreted and JIT-compiled languages?
- [CS07-003] What does a just-in-time compiler do, how does it differ from ahead-of-time compilation, and why is AOT not used everywhere?
- [CS07-004] What does Big-O notation describe, and how does it differ from Big-Theta and Big-Omega?
- [CS07-005] How do you analyse the time and space complexity of code with loops and recursion, and what are the common complexity classes?
- [CS07-006] Why does Big-O drop constants and lower-order terms, and when do those terms still matter in practice?
- [CS07-007] Why can an algorithm with a better Big-O be slower in practice, and how does measured runtime differ from asymptotic complexity?
- [CS07-008] What is amortized analysis, and how does it justify O(1) append for a dynamic array?
- [CS07-009] What is the difference between pseudo-polynomial and polynomial time complexity?
- [CS07-010] How does expected-case analysis of a randomized algorithm, such as randomized quicksort, differ from worst-case analysis of a deterministic one?
- [CS07-011] What are the trade-offs between recursion and iteration, including stack usage and tail calls?
- [CS07-012] What is the time and space complexity of naive recursive Fibonacci, and how does memoization change it?
- [CS07-013] What is a stable sort, why does it matter, and how do in-place and out-of-place sorts differ?
- [CS07-014] Compare the common comparison-based sorts (quick, merge, heap, insertion) by time complexity, space and stability. When is each preferred?
- [CS07-015] Quicksort versus mergesort: why is quicksort often faster in practice despite its worse worst case, how is that case avoided, and why is merge sort used for external sorting?
- [CS07-016] Which sorting algorithm would you choose for nearly sorted data, for linked lists, or for data too large for memory?
- [CS07-017] When can counting, bucket and radix sort beat O(n log n), and what assumptions do they need?
- [CS07-018] How does Timsort work, and why do Python and Java use it as their default object sort?
- [CS07-019] What preconditions does binary search need, and why is it O(log n)?
- [CS07-020] What is the difference between dynamic programming, greedy algorithms and divide and conquer?
- [CS07-021] How do you recognise that a problem suits dynamic programming, and how do memoization and tabulation compare?
- [CS07-022] How do you decide a greedy choice is safe, and how does a greedy algorithm differ from dynamic programming?
- [CS07-023] How does Dijkstra's algorithm work, why does it fail with negative edge weights, and how do BFS and Bellman-Ford differ from it?
- [CS07-024] What are topological sorting and minimum spanning trees (Kruskal versus Prim), and where are they used?

## Data structures: lists, hashing, trees and graphs
- [CS07-025] Compare arrays and linked lists (singly, doubly, circular) in access, insertion, memory locality and space. Why do arrays often win in practice?
- [CS07-026] What are the differences between a stack and a queue, and where is each used in real systems?
- [CS07-027] How would you implement a queue using two stacks, and what is its amortized cost?
- [CS07-028] How is a circular queue implemented with an array, and how do you distinguish full from empty?
- [CS07-029] Why does the call stack use a stack structure, and what causes a stack overflow?
- [CS07-030] How does a hash table work, and why is lookup O(1) on average but O(n) in the worst case?
- [CS07-031] Compare chaining and open addressing for collision resolution, including clustering and deletion.
- [CS07-032] What is the load factor of a hash table, and why and when does it resize?
- [CS07-033] What makes a good hash function, and what happens to lookup cost with many colliding or adversarial keys?
- [CS07-034] What is the cost of rehashing during a resize, and how can incremental rehashing avoid latency spikes?
- [CS07-035] What is the difference between a hash map and an ordered (tree-based) map in complexity and ordering?
- [CS07-036] What is a Bloom filter, and what trade-off does it make compared with a hash set?

## Trees, heaps, tries and graphs
- [CS07-037] What is a binary search tree, and what are the time complexities of its operations, including balanced variants?
- [CS07-038] Why can a BST degrade to O(n), and how do AVL rotations and red-black invariants restore balance? How do the two trees compare?
- [CS07-039] How do you delete a node with two children from a BST?
- [CS07-040] What do pre-order, in-order, post-order and level-order traversals produce, and what does in-order give on a BST?
- [CS07-041] What is the difference between a full, complete, perfect and balanced binary tree?
- [CS07-042] Compare BSTs, balanced trees and hash tables as symbol table implementations.
- [CS07-043] What is a heap, how is it stored in an array, and what are the complexities of insert, delete-min and peek?
- [CS07-044] Why is building a heap from n elements O(n) rather than O(n log n)?
- [CS07-045] How does heap sort work, and why is it not stable and often slower than quicksort in practice?
- [CS07-046] How would you find the top K elements in a stream? Compare heap, quickselect and full sorting.
- [CS07-047] What is a trie, what problems suit it, and how do its memory costs compare with a hash table?
- [CS07-048] When does a trie beat a binary search or hash lookup for CIDR-based IP allow-list matching?
- [CS07-049] What is a skip list, why is lookup O(log n) on average, and how does it compare with a balanced tree under concurrency?
- [CS07-050] What is a disjoint-set (union-find) structure, and how do path compression and union by rank make it fast?
- [CS07-051] How do you represent a graph in memory? Compare an adjacency matrix with adjacency lists.
- [CS07-052] When would you use BFS versus DFS on a graph or search problem, and what are their time and space costs?
- [CS07-053] How do you choose between DFS, BFS and backtracking for a search problem, and how do you prune duplicates?
- [CS07-054] Which data structures implement an LRU cache in O(1), and why is a doubly linked list needed with the hash map?
- [CS07-055] How would you make an LRU cache thread-safe with good concurrency, and how do the trade-offs differ against LFU?

## Python language and object model
- [CS07-056] How is Python code executed (bytecode and the interpreter), and what are the key characteristics of the language?
- [CS07-057] What are Python's built-in data types, and what is the difference between mutable and immutable objects?
- [CS07-058] What are the differences between a list, a tuple and a set, and why can only hashable types be dictionary keys?
- [CS07-059] How are Python lists and dictionaries implemented internally, and what are the complexities of their operations?
- [CS07-060] What is the difference between == and is in Python, and why can small integers behave unexpectedly?
- [CS07-061] Why is a mutable default argument in a Python function a bug waiting to happen?
- [CS07-062] What is the difference between a shallow and a deep copy in Python, and what happens with nested mutable objects?
- [CS07-063] What is a Python generator, how does it differ from a list comprehension in memory use and laziness, and when would you use a generator expression?
- [CS07-064] What is the iterator protocol, and how does an iterable differ from an iterator?
- [CS07-065] What do *args and **kwargs do in function definitions?
- [CS07-066] What is a decorator in Python, how does it work with closures, and when would you use one?
- [CS07-067] How would you write a timing decorator that preserves the wrapped function's name and docstring?
- [CS07-068] Why do closures created in a loop often capture the last value of the loop variable, and how do you fix it?
- [CS07-069] What is a lambda in Python, what are its limitations, and where would you use one?
- [CS07-070] How does the with statement work, and how do you write a context manager?
- [CS07-071] Python does not support traditional method or constructor overloading. How do you get similar flexibility?
- [CS07-072] What does the del statement actually do, and does del obj call __del__()?
- [CS07-073] Why should __del__() not be used for critical cleanup, and when is it appropriate?
- [CS07-074] How do you handle exceptions in Python, and what are the best practices for exception handling?
- [CS07-075] When should you use a dataclass, a plain class, a function or an abstract base class, and how would you define a typed configuration object?
- [CS07-076] How does method resolution order work with multiple inheritance in Python, and what does super() actually do?
- [CS07-077] What does __slots__ do, and when does it reduce memory use?

## Python memory, GIL and concurrency
- [CS07-078] How does Python manage memory, covering reference counting, the private heap and object allocation?
- [CS07-079] How does Python's garbage collector work, and how does it handle circular references and generations?
- [CS07-080] What is the Global Interpreter Lock, why does CPython have it, and what does it protect?
- [CS07-081] How does the GIL affect CPU-bound versus I/O-bound code, and when do you choose threads, multiprocessing or asyncio?
- [CS07-082] How does asyncio's event loop differ from threads, and what happens when a coroutine runs blocking code?
- [CS07-083] What changes with the free-threaded (no-GIL) builds of CPython, and what would break or slow down?
- [CS07-084] How do you locate memory growth and event-loop blocking in a long-running Python AI service, and how do you troubleshoot OOM?
- [CS07-085] What kinds of reference leaks happen in Python even with garbage collection, and how do weakref and tracemalloc help?
- [CS07-086] How would you profile slow Python code and speed up hot paths, such as with vectorization, caching or native extensions?
- [CS07-087] How does a pseudo-random number generator such as Python's random module work, and is it suitable for security?

## Java language fundamentals
- [CS07-088] What are the JDK, JRE and JVM, and how does Java achieve platform independence ("write once, run anywhere")?
- [CS07-089] What is the difference between the path and the classpath in Java?
- [CS07-090] What is Java bytecode, and what happens from compiling a source file to running java MyClass?
- [CS07-091] What are the main differences between Java and C++?
- [CS07-092] Is Java a pure object-oriented language? What does static typing mean, and which features are not object-oriented?
- [CS07-093] Is Java pass-by-value or pass-by-reference? Explain with an example involving object references.
- [CS07-094] What are wrapper classes and autoboxing, and how does int differ from Integer?
- [CS07-095] What are the pitfalls of autoboxing (performance, null unboxing), and how does the Integer cache affect comparisons?
- [CS07-096] What do final and static mean on variables, methods and classes?
- [CS07-097] What is the difference between final, finally and finalize?
- [CS07-098] Can static methods be overridden or overloaded, and what about the main method? When should static methods be avoided?
- [CS07-099] What is the difference between this and super, and how does constructor chaining work?
- [CS07-100] What are the rules for method overriding, including covariant returns and exceptions in the throws clause?
- [CS07-101] What is the contract between equals() and hashCode(), and what breaks if only one is overridden?
- [CS07-102] What is the difference between == and equals(), and between String#equals and Object#equals?

## Java strings, generics, exceptions and functional features
- [CS07-103] Why are String and wrapper classes immutable and final in Java, and what benefits does immutability bring?
- [CS07-104] How do String, StringBuilder and StringBuffer differ in mutability and thread safety?
- [CS07-105] What is the string intern pool, how many objects does new String("abc") create, and how has String storage changed in recent Java versions?
- [CS07-106] What is the difference between shallow and deep copy, and what are the pitfalls of clone()?
- [CS07-107] How do generics work with type erasure, and what limitations and runtime differences follow (for example List<String> versus List<Integer>)?
- [CS07-108] What are bounded wildcards, and what does PECS (producer extends, consumer super) mean?
- [CS07-109] What is reflection, what is it used for, and what are its costs and risks? How do JDK dynamic proxies differ from CGLIB?
- [CS07-110] What are lambdas and functional interfaces, how do they differ from anonymous classes, and what do method references and default methods add?
- [CS07-111] How do lazy intermediate and terminal stream operations work, how do map() and flatMap() differ, and what are the pros and cons of parallel streams?
- [CS07-112] When should you use Optional instead of null, and how does a Record differ from a regular JavaBean?
- [CS07-113] Should monetary amounts be stored as a long in the smallest unit or as a BigDecimal?
- [CS07-114] What is the difference between checked and unchecked exceptions and between Exception and Error, and when should you create custom exceptions of each kind?
- [CS07-115] What is the difference between throw and throws, and what happens if a checked exception is not handled?
- [CS07-116] How do try-with-resources and multi-catch work compared with try-catch-finally?
- [CS07-117] What happens if a finally block or both try and finally throw exceptions, and can finally prevent propagation?
- [CS07-118] How do you design custom exceptions: what information they carry, hierarchies, and the performance cost of stack traces?
- [CS07-119] How do you handle checked exceptions inside lambda expressions?
- [CS07-120] How does Java serialization work, what do transient and serialVersionUID do, and what are the security and compatibility concerns compared with JSON?
- [CS07-121] Compare blocking stream I/O with NIO channels, buffers and selectors, and when are memory-mapped files faster than regular reads?
- [CS07-122] Why does character encoding matter when converting between bytes and characters, and what causes garbled text?

## Java collections and HashMap internals
- [CS07-123] Explain the Java Collections Framework and the differences between List, Set, Queue and Map.
- [CS07-124] Compare ArrayList and LinkedList across random access, insertion, memory overhead and cache behavior.
- [CS07-125] How does ArrayList grow, how do size and capacity differ, and why does LinkedList not implement RandomAccess?
- [CS07-126] Why is Vector considered obsolete, and what does CopyOnWriteArrayList trade for lock-free reads?
- [CS07-127] What is fail-fast iterator behavior, how does it differ from fail-safe, and what happens when you modify a list during iteration?
- [CS07-128] When would you use an Iterator or ListIterator instead of an enhanced for-loop, and which iteration style is most efficient?
- [CS07-129] What are the pitfalls of converting between arrays, lists and sets, such as fixed-size views and shared backing arrays?
- [CS07-130] What is the difference between HashMap, Hashtable and ConcurrentHashMap?
- [CS07-131] Explain how HashMap is implemented: buckets, hash function, collision handling, resizing and treeification.
- [CS07-132] Why does HashMap convert long bucket chains into balanced trees, and what thresholds trigger it?
- [CS07-133] How does HashMap compute the bucket index with power-of-two capacity, what is the load factor, and how are entries redistributed on resize?
- [CS07-134] What can go wrong with HashMap in a multithreaded environment, such as lost updates or infinite loops during resize?
- [CS07-135] Why must keys implement equals() and hashCode() consistently, and what happens if a mutable object is used as a key?
- [CS07-136] Compare HashMap, LinkedHashMap and TreeMap in ordering, complexity and null-key handling.
- [CS07-137] How do you iterate through a Map efficiently, and what are the cost differences between key, value and entry iteration?
- [CS07-138] How does LinkedHashMap preserve order, and how can it implement an LRU cache?
- [CS07-139] What is a WeakHashMap, and when would you use it?
- [CS07-140] How does ConcurrentHashMap achieve thread safety (segment locks versus CAS plus per-bin locking), and how does cooperative resizing work?
- [CS07-141] Why can ConcurrentHashMap not hold null keys or values, and is check-then-put atomic? How do you make compound operations atomic?
- [CS07-142] Compare HashSet, LinkedHashSet and TreeSet, how HashSet ensures uniqueness, and when to prefer TreeSet.
- [CS07-143] What is the difference between Comparable and Comparator?
- [CS07-144] Compare Queue, Deque, ArrayDeque and LinkedList used as a stack or queue.
- [CS07-145] How does PriorityQueue maintain order with a binary heap, and what are its complexities and duplicate handling?
- [CS07-146] Compare ArrayBlockingQueue, LinkedBlockingQueue and ConcurrentLinkedQueue.
