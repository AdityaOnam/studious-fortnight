---
domain: cs
topic: oop_design_patterns_solid
title: OOP, design patterns, SOLID
tags: [oop, design-patterns, solid, testing]
count: 138
part: 2/2
---
# OOP, design patterns, SOLID (part 2)

## Design pattern basics and creational patterns
- [CS06-113] What are design patterns, why do they help, and how are they categorised into creational, structural and behavioural patterns? Give examples of each.
- [CS06-114] What are the risks of overusing design patterns, and how do you tell when a pattern is justified?
- [CS06-115] What is the Singleton pattern, when is it appropriate, and what are its drawbacks?
- [CS06-116] How do you implement a thread-safe Singleton? Compare eager, lazy, double-checked locking, holder and enum approaches, and explain what is wrong with naive double-checked locking.
- [CS06-117] How can a Singleton be broken (reflection, serialization, multiple class loaders), and how do you defend against it?
- [CS06-118] Why is Singleton often criticised as hidden global state that hurts testability, and what alternatives exist?
- [CS06-119] How does a Singleton differ from a class that exposes only static methods, and when would you choose each?
- [CS06-120] What is the Factory Method pattern, and what problem does it solve?
- [CS06-121] What is the difference between a simple factory, the Factory Method pattern and the Abstract Factory pattern?
- [CS06-122] When would you choose Abstract Factory over Factory Method, and what is its main drawback when adding new product types?
- [CS06-123] Compare Factory Method, Abstract Factory and Builder. What does each one optimise for?
- [CS06-124] What problem does the Builder pattern solve compared with telescoping constructors?
- [CS06-125] When should you prefer a builder over constructor overloading or named parameters, and how do you validate required fields?
- [CS06-126] When is the Prototype pattern useful, and what are the pitfalls of shallow versus deep copying when cloning objects?

## Structural patterns
- [CS06-127] What is the Adapter pattern, and when would you use it?
- [CS06-128] What is the difference between a class adapter and an object adapter?
- [CS06-129] What pitfalls arise when adapting a third-party library, such as leaking the adaptee's interface into your code?
- [CS06-130] How does the Bridge pattern decouple abstraction from implementation and prevent a class explosion when two dimensions of variation exist?
- [CS06-131] How does the Bridge pattern differ from the Adapter pattern?
- [CS06-132] What is the Composite pattern, and how does it model tree structures such as a file system?
- [CS06-133] In the Composite pattern, should child-management operations live on the common component or only on the composite? What are the trade-offs?
- [CS06-134] How does the Decorator pattern add behaviour without subclassing, and how does it differ from inheritance?
- [CS06-135] What are the drawbacks of the Decorator pattern, such as ordering sensitivity and many small objects?
- [CS06-136] Composite and Decorator both rely on recursive composition. How do they differ in structure and intent?
- [CS06-137] What is the Facade pattern, and how does it reduce coupling between subsystems?
- [CS06-138] How does a facade differ from an adapter and a mediator?
- [CS06-139] How does the Flyweight pattern reduce memory usage, and what is the difference between intrinsic and extrinsic state?
- [CS06-140] When does Flyweight actually save memory, what does it cost in complexity and thread safety, and how does it differ from object pooling?
- [CS06-141] What is the Proxy pattern, and what are virtual, protection and remote proxies?
- [CS06-142] How do proxy, decorator and adapter differ when they all wrap another object? Compare static and dynamic proxies.
- [CS06-143] How can the Proxy pattern provide lazy loading, caching or access control, and how do dynamic proxies work?

## Behavioural patterns
- [CS06-144] What is the Observer pattern, what problem does it solve, and where is it used in practice?
- [CS06-145] What are the pitfalls of the Observer pattern, such as memory leaks from forgotten listeners, notification ordering and cascading updates?
- [CS06-146] How does Observer differ from publish-subscribe and event buses, and when would you prefer one over the other?
- [CS06-147] What is the difference between push and pull models of observer notification?
- [CS06-148] An observer throws an exception while the subject is notifying subscribers synchronously. What happens, and how would you design for it?
- [CS06-149] What is the Strategy pattern, and how does it remove conditional logic?
- [CS06-150] How would you refactor a long if-else chain choosing between algorithms into the Strategy pattern, and how does this relate to the Open/Closed Principle?
- [CS06-151] What is the difference between the Strategy pattern and the State pattern?
- [CS06-152] What is the State pattern, and when is it better than a switch on an enum?
- [CS06-153] Who should own state transitions in the State pattern, the context or the states, and what are the implications?
- [CS06-154] What is the Template Method pattern, and how do abstract classes support it?
- [CS06-155] How does Template Method relate to the Hollywood principle, how does it differ from Strategy, and what are the drawbacks of relying on inheritance?
- [CS06-156] What is the Command pattern, and what does it enable beyond a direct method call?
- [CS06-157] How does the Command pattern support undo, redo, queuing and logging of operations?
- [CS06-158] How does the Iterator pattern decouple traversal from the underlying collection?
- [CS06-159] What happens when a collection is modified during iteration, and how do fail-fast and snapshot iterators differ?
- [CS06-160] What is the Visitor pattern, and what problem does double dispatch solve?
- [CS06-161] What is the main trade-off of the Visitor pattern when adding new element types versus adding new operations?
- [CS06-162] How does the Mediator pattern reduce many-to-many coupling, and what is the risk of a mediator becoming a god object?
- [CS06-163] How does the Memento pattern save and restore object state without breaking encapsulation?
- [CS06-164] How does the Chain of Responsibility pattern work, and where do web frameworks use it (middleware, filters)?
- [CS06-165] What happens in Chain of Responsibility when no handler processes a request, and how do you guarantee termination?
- [CS06-166] What is the Null Object pattern, and when is it better than returning null?
- [CS06-167] What is the Interpreter pattern, and when is a small domain-specific language worthwhile versus a parser generator?

## Pattern selection and architectural patterns
- [CS06-168] Which design patterns appear in standard libraries and well-known frameworks? Give examples (iterator, adapter, factory, decorator).
- [CS06-169] Strategy, State and Bridge look structurally similar. How do you distinguish their intent?
- [CS06-170] Which pattern fits a payment system that must support many payment methods, gateways and promotions chosen at runtime?
- [CS06-171] A class has a long if-else chain choosing behaviour by type. Which patterns could remove it, and which would you choose?
- [CS06-172] Which pattern would you use to add caching, logging or authorization to an existing service without modifying it?
- [CS06-173] Which pattern would you use to build a text-formatting pipeline with optional stages, and why?
- [CS06-174] Which pattern fits a UI toolkit where widgets are nested in containers and treated uniformly?
- [CS06-175] Which patterns would you combine to design an event-driven notification module with multiple channels and retry behaviour?
- [CS06-176] Which patterns help build a document editor that supports undo, multiple views and format conversion?
- [CS06-177] How would you build an HTTP request-processing middleware pipeline, and how does ordering matter?
- [CS06-178] Design an extensible plugin system for a class library. Which patterns and principles make it open to extension?
- [CS06-179] How would you design a registry that lets callers look up interchangeable components, such as strategies or preprocessing functions, by name?
- [CS06-180] What does MVC separate, how do the model, view and controller interact, and how do MVP, MVVM and similar patterns differ?
- [CS06-181] How do the Repository and Unit of Work patterns separate persistence from domain logic?
- [CS06-182] What is the difference between Active Record and Data Mapper, and when would each be preferable?
- [CS06-183] What is event sourcing at the object level, and how does it relate to the Memento and Command patterns?
- [CS06-184] What is the difference between a design pattern and a distributed-systems pattern such as sidecar, circuit breaker or saga?
- [CS06-185] What are anti-patterns such as god object, spaghetti code and golden hammer, and how do they emerge?
- [CS06-186] What is the difference between a library and a framework from a control-flow perspective?
- [CS06-187] What is the difference between an API and an SPI, and how do you evolve a public interface without breaking clients?
- [CS06-188] How do object-oriented design principles show up in a machine coding round, and what do interviewers look for?
- [CS06-189] Design the classes for a parking lot. Which entities, relationships, principles and patterns would you use?
- [CS06-190] Design a vending machine using the State pattern. What are the states, transitions and classes?
- [CS06-191] Design the class structure for an elevator control system. How do you keep it extensible for new scheduling policies?

## Clean code and refactoring
- [CS06-192] What are the characteristics of clean code, and how do naming, function size and comments contribute?
- [CS06-193] Why does naming matter for maintainability, and what makes identifiers readable? Where are camelCase, snake_case and kebab-case typically used?
- [CS06-194] When are comments harmful, and what should good comments communicate?
- [CS06-195] Why should functions have few side effects and few parameters?
- [CS06-196] How would you refactor a deeply nested conditional or a very long function?
- [CS06-197] What is refactoring, and how is it different from performance optimisation?
- [CS06-198] When is the right time to refactor, and why are automated tests a prerequisite?
- [CS06-199] What are the risks of refactoring for its own sake, and how do you keep refactoring incremental and safe?
- [CS06-200] What is a code smell? Name several well-known smells and the refactorings that address them.
- [CS06-201] What are design smells such as rigidity, fragility, immobility and viscosity?
- [CS06-202] What do the DRY, KISS and YAGNI principles mean, and when do they conflict?
- [CS06-203] When is duplication preferable to a premature abstraction, what is the rule of three, and what makes a utility reusable without over-abstraction?
- [CS06-204] What is the principle of least astonishment, and how does it apply to API and class design?
- [CS06-205] What is technical debt, and how do you decide when to refactor versus ship?
- [CS06-206] When is a rewrite cheaper than a refactor, and what safety nets should be in place before refactoring?
- [CS06-207] You have about 120 lines of working but messy code with passing tests. Do you refactor straight away or write tests first, and what do you change first?
- [CS06-208] You inherit a large class with hundreds of lines, mixed responsibilities and no tests. Describe how you would safely restructure it.
- [CS06-209] How do you decide whether a block of code should become a new method, a new class or stay where it is?

## Robust design and code review
- [CS06-210] What are the goals of code review, and what should a reviewer prioritise?
- [CS06-211] What is the difference between exceptions and error return values, and when should custom exception types be created? How would you design the errors for invalid input to a library function?
- [CS06-212] What are checked versus unchecked exceptions, and what is the argument for each?
- [CS06-213] What is design by contract, and how do preconditions, postconditions and invariants appear in everyday code?
- [CS06-214] What is the difference between defensive programming and fail-fast, and which input validation belongs at module boundaries versus inside internal functions?

## Testing fundamentals
- [CS06-215] What is software testing, and why is it important?
- [CS06-216] What is the difference between verification and validation?
- [CS06-217] What is the difference between static and dynamic testing?
- [CS06-218] What role does testing play in each phase of the software development life cycle?
- [CS06-219] What are the levels of software testing?
- [CS06-220] What is integration testing, and what are its types?
- [CS06-221] What is system testing, and how does it differ from other types of testing?
- [CS06-222] What is acceptance testing, and what are its types?
- [CS06-223] What is the difference between alpha and beta testing?
- [CS06-224] What is the difference between unit, integration and end-to-end tests, what is the test pyramid, and why does testable design matter?
- [CS06-225] What is the difference between white-box, black-box and grey-box testing?
- [CS06-226] Explain black-box testing techniques such as equivalence partitioning and boundary value analysis.
- [CS06-227] What is white-box testing, and what is code coverage?
- [CS06-228] What are the main types of coverage (line, statement, branch, path)?
- [CS06-229] Why is high code coverage not a guarantee of quality?
- [CS06-230] What is a test case, and what elements should it contain?
- [CS06-231] What is regression testing, and why is it performed?
- [CS06-232] What is the difference between retesting and regression testing?
- [CS06-233] What is the difference between smoke testing and sanity testing?
- [CS06-234] Explain the defect (bug) life cycle.
- [CS06-235] What are the benefits of test automation?
- [CS06-236] When would you choose not to automate test cases?
- [CS06-237] What makes a test flaky, and how would you diagnose and fix it?
- [CS06-238] An AI-generated test suite has 95% coverage and all tests are green. What do you check before trusting it?
- [CS06-239] Would you gate merges on mutation score, and at what cost?

## TDD, test doubles and testable design
- [CS06-240] What is Test-Driven Development, and what is the red-green-refactor cycle?
- [CS06-241] What are the benefits and the costs of TDD?
- [CS06-242] What is behaviour-driven development, and how does it differ from TDD?
- [CS06-243] What is the purpose of unit testing, how does it support refactoring and continuous integration, and which tools might you use?
- [CS06-244] What makes a good unit test in terms of isolation, determinism and speed (the FIRST principles)?
- [CS06-245] What problems do mocks and stubs each solve?
- [CS06-246] What are mocks, stubs, fakes and spies, and when is mocking harmful?
- [CS06-247] How does good object-oriented design make code easier to unit test, and how should an ML or data-processing codebase be structured for independent testing?
- [CS06-248] What is the Arrange-Act-Assert structure of a unit test, and why does it help readability?
- [CS06-249] How do you test a class that depends on the current time, random numbers or the network?
- [CS06-250] Should you test private methods directly? What does a need to do so say about the design?
