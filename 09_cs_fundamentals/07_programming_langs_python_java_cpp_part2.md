---
domain: cs
topic: programming_langs_python_java_cpp
title: Programming language internals: Python, Java, C++
tags: [python, java, cpp, jvm, big-o]
count: 116
part: 2/2
---
# Programming language internals: Python, Java, C++ (part 2)

## JVM memory model and class loading
- [CS07-147] What are the runtime memory areas of the JVM (heap, stack, method area, PC register, direct memory), and what does each store?
- [CS07-148] What is the difference between the heap and the stack in Java, what is stored in a stack frame, and what happens to local variables when a method returns?
- [CS07-149] What are the method area, metaspace and the runtime constant pool, and how did metaspace replace the permanent generation?
- [CS07-150] Is direct memory part of the JVM runtime data areas, what are its benefits, and why can it also cause OOM?
- [CS07-151] What is the difference between the Java memory areas and the Java Memory Model (JMM)?
- [CS07-152] What are the steps of creating an object in the JVM, from class check to header initialization?
- [CS07-153] How do you choose between pointer-bumping and free-list allocation, and what problems do CAS and TLAB each solve under concurrent allocation?
- [CS07-154] What is the memory layout of a Java object, and how does a reference locate the object via handles or direct pointers?
- [CS07-155] What can cause StackOverflowError versus OutOfMemoryError, and how does each arise when a method builds a large list of objects?
- [CS07-156] What is the role of the ClassLoader in Java?
- [CS07-157] What are the phases of class loading: loading, verification, preparation, resolution and initialization?
- [CS07-158] When does class initialization get triggered, and when can a class be unloaded?
- [CS07-159] What is the parent delegation model of class loaders, why does it exist, and how can it be broken?
- [CS07-160] When would you write a custom class loader, and should you override findClass() or loadClass()?
- [CS07-161] What does a compiled class file contain (magic number, constant pool, access flags, fields, methods, attributes)?
- [CS07-162] What do the class loader, bytecode interpreter and JIT compiler each do in the JVM?
- [CS07-163] How does tiered JIT compilation and warm-up affect the performance of a freshly started Java service?
- [CS07-164] What is escape analysis, and how can it let the JIT avoid heap allocation?
- [CS07-165] Can a memory leak happen in a garbage-collected language, and how does Java avoid the leaks typical of C/C++?

## Garbage collection concepts and collectors
- [CS07-166] What is garbage collection, why do managed runtimes use it, and how does it work in Java?
- [CS07-167] How does the JVM decide an object is dead: reference counting versus reachability analysis, and what are GC roots?
- [CS07-168] Explain strong, soft, weak and phantom references and a use case for each.
- [CS07-169] Compare mark-sweep, mark-compact and copying garbage collection algorithms.
- [CS07-170] Why do collectors split the heap into young and old generations, how do Eden, survivor spaces and promotion work, and what is the weak generational hypothesis?
- [CS07-171] What is the difference between minor, major and full GC, and what triggers each?
- [CS07-172] Why are large objects allocated directly into the old generation, and what problems do they cause?
- [CS07-173] How do the goals and suitable scenarios of Serial, Parallel, CMS, G1 and ZGC differ?
- [CS07-174] How does G1 control pause times using regions, collection-value prediction and mixed GC?
- [CS07-175] How do low-pause collectors like ZGC reach sub-millisecond pauses with colored pointers and load barriers?
- [CS07-176] What does stop-the-world mean, and how do concurrent collectors reduce pause times?
- [CS07-177] How does concurrent marking cope with objects modified during marking, for example via write barriers?
- [CS07-178] What are card tables and remembered sets, and why do generational and region-based collectors need them?
- [CS07-179] How do you trade off throughput, latency and memory footprint when choosing a collector for a service?

## JVM tuning and production troubleshooting
- [CS07-180] What causes OutOfMemoryError in Java and how can it be prevented?
- [CS07-181] After a Java process hits OOM, how do you determine whether the problem is in the heap, metaspace, direct memory or native memory?
- [CS07-182] What situations trigger a Full GC, and what data do you check first when Full GC is frequent?
- [CS07-183] Why do server applications often set -Xms and -Xmx to the same value?
- [CS07-184] Which JVM flags control heap size, young generation ratio, metaspace and GC choice, and how do you pick starting values?
- [CS07-185] How do you configure GC logging in JDK 8 versus JDK 9 and later?
- [CS07-186] How do you automatically generate a heap dump on OOM, and why should you confirm storage space in advance?
- [CS07-187] Which command-line tools inspect a running JVM (jstat, jmap, jstack), and how do you monitor and optimize Java memory usage?
- [CS07-188] What is the difference between a heap dump and a thread dump, and which one does kill -3 produce?
- [CS07-189] When should a heap dump be taken, and what are the risks of running jmap -dump directly in production?
- [CS07-190] When analyzing a heap dump with MAT, what are the dominator tree and the reference chain to GC roots used for?
- [CS07-191] A Java service has frequent Full GCs and growing heap usage. How do you tell a leak from normal growth and troubleshoot it?
- [CS07-192] An application suffers long GC pauses and frequent full GCs. How do you investigate and tune it?
- [CS07-193] How do you investigate frequent young GCs?
- [CS07-194] A service shows high CPU usage. How do you find the hot thread and the code responsible?
- [CS07-195] A service shows high load average but low CPU usage. What do you check?
- [CS07-196] A slow API has low CPU. How do you tell whether the time goes to thread-pool queuing, connection pools, downstream calls or locks?
- [CS07-197] A containerized JVM is OOM-killed even though the heap is below -Xmx. What could explain it?

## C and C++ memory, pointers and types
- [CS07-198] What are the main differences between C and C++, and what are the main features of C++?
- [CS07-199] What is the difference between a pointer and a reference, and when would you use each?
- [CS07-200] What is the difference between pass by value and pass by reference?
- [CS07-201] What is the relationship between arrays and pointers in C, and what does pointer arithmetic do?
- [CS07-202] Compare stack and heap allocation in terms of lifetime, speed and size.
- [CS07-203] Compare malloc/free with new/delete: constructors, type safety, failure behavior and why mixing them is a bug.
- [CS07-204] What happens if you allocate with new[] but release with delete instead of delete[]?
- [CS07-205] What is placement new, and when is it used?
- [CS07-206] What are memory leaks, dangling pointers, wild pointers and double frees, how do they arise, and how would you detect and prevent each?
- [CS07-207] Is delete this legal, and under what conditions is it safe?
- [CS07-208] What does const mean for variables, pointers, member functions and parameters, and how do a pointer to const, a const pointer and a const pointer to const differ?
- [CS07-209] What are the different uses of static in C and C++ (storage duration, linkage, class members), and how do local and global variables differ?
- [CS07-210] What does volatile tell the compiler, and why is it not a substitute for atomics or synchronization?
- [CS07-211] What does sizeof return for a struct, and how do alignment and padding affect layout and member ordering?
- [CS07-212] What are bit fields, and what portability problems do they have?
- [CS07-213] What is a union, how does it differ from a struct in layout, and what is type punning?
- [CS07-214] What does extern "C" do, and how does name mangling support function overloading?
- [CS07-215] What is the difference between struct and class in C++, and between a C struct and a C++ struct?
- [CS07-216] How can you implement classes and virtual dispatch in plain C?
- [CS07-217] What are the stages of building a C/C++ program (preprocess, compile, assemble, link), and how do headers, translation units and the one-definition rule lead to linker errors?
- [CS07-218] What is the difference between static and dynamic linking?
- [CS07-219] How does inline differ from a macro, and what are the dangers of preprocessor macros compared with inline functions, constexpr and templates?
- [CS07-220] What are bitwise operations, and what are their real-world applications?
- [CS07-221] How do AND, OR, XOR, shifts, rotations and bit masks work, and how can bitmasks represent sets?
- [CS07-222] What is undefined behavior in C/C++, and why can a program work in a debug build but fail in release?

## C++ OOP and polymorphism
- [CS07-223] How do virtual functions work internally (vptr and vtable), and what is the cost of polymorphism?
- [CS07-224] Why should a base class intended for polymorphic deletion have a virtual destructor?
- [CS07-225] When is the vptr set during construction, and why is calling a virtual function from a constructor a bad idea?
- [CS07-226] What are a pure virtual function and an abstract class, and can a pure virtual function have a body?
- [CS07-227] Can constructors, static member functions or templates be virtual? Explain each.
- [CS07-228] Can a virtual function be inline, and are "inline virtual" member functions ever actually inlined?
- [CS07-229] What is the diamond problem, how does virtual inheritance solve it, and how does it change object layout and access cost?
- [CS07-230] What is object slicing, and how can you avoid it?
- [CS07-231] What is the difference between overloading, overriding and hiding in C++ inheritance?
- [CS07-232] What is operator overloading in C++, and which operators should not be overloaded?
- [CS07-233] What are the types of constructors in C++, and what role do destructors play?
- [CS07-234] What does the explicit keyword prevent for constructors and conversion operators?
- [CS07-235] What is the this pointer, and how is it passed to non-static member functions?
- [CS07-236] What are friend functions and classes, and how do they affect encapsulation?
- [CS07-237] Why is a member initializer list preferred over assignment in the constructor body, and in what order are members initialized?
- [CS07-238] What does std::initializer_list enable, and how does brace initialization prevent narrowing conversions?
- [CS07-239] What is the rule of three/five/zero, why does a class owning raw resources need it, and what bugs does a shallow copy of a pointer member cause?
- [CS07-240] What are static_cast, dynamic_cast, const_cast and reinterpret_cast, and how does RTTI let dynamic_cast work at runtime?
- [CS07-241] How does exception handling interact with destructors, and why does noexcept matter for move operations in containers?
- [CS07-242] How do templates differ from Java generics, and what is code bloat?
- [CS07-243] When would you prefer templates (static polymorphism, CRTP) over virtual functions, and how can final help devirtualization?
- [CS07-244] What are copy elision and return value optimization, and how do they interact with move semantics?

## Modern C++: RAII, smart pointers, move semantics and STL
- [CS07-245] What is RAII, and how does it provide exception-safe resource management?
- [CS07-246] What are lvalue references, rvalue references and forwarding references, what problem does move semantics solve, and what is the state of a moved-from object?
- [CS07-247] What is perfect forwarding, and why is std::forward needed?
- [CS07-248] Compare unique_ptr, shared_ptr and weak_ptr, including ownership semantics and overhead.
- [CS07-249] How does shared_ptr implement reference counting, and is it thread-safe?
- [CS07-250] How can shared_ptr cause a memory leak through cycles, and how does weak_ptr fix it?
- [CS07-251] Why is make_shared preferred to constructing a shared_ptr from new, and what is its downside?
- [CS07-252] Why was auto_ptr deprecated, and what problem does unique_ptr solve differently?
- [CS07-253] When should you pass a smart pointer by value, by reference, or pass a raw pointer to a function?
- [CS07-254] Compare std::vector, std::list, std::deque and std::array in memory layout, iterator invalidation and use cases.
- [CS07-255] How does std::vector grow, how do size and capacity differ, what does reserve do, and which operations invalidate iterators?
- [CS07-256] What data structures underlie std::map and std::unordered_map, how do their complexities differ, and what does a custom key type need?
- [CS07-257] How does std::priority_queue work, and which heap operations does it use?
- [CS07-258] What is the erase-remove idiom, and why is it needed for sequence containers?
- [CS07-259] When do iterators and references into an unordered_map become invalid, and how does rehashing affect them?
- [CS07-260] When is std::string_view or std::span safe to use, and how can they dangle?
- [CS07-261] What does the C++ memory model say about data races, and how do std::atomic and memory orders help?
- [CS07-262] A C++ service crashes intermittently with a segmentation fault in production. How do you find the root cause from a core dump?
