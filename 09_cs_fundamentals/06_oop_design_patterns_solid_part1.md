---
domain: cs
topic: oop_design_patterns_solid
title: OOP, design patterns, SOLID
tags: [oop, design-patterns, solid, testing]
count: 112
part: 1/2
---
# OOP, design patterns, SOLID (part 1)

## OOP fundamentals and classes
- [CS06-001] What is object-oriented programming, and why is it used?
- [CS06-002] What is the difference between procedural and object-oriented programming?
- [CS06-003] What are the four pillars of OOP, and what problem does each one solve?
- [CS06-004] What is the difference between a class, an object and an instance?
- [CS06-005] Is OOP always the best choice? When would another paradigm fit better?
- [CS06-006] What is a constructor, and how does it differ from an ordinary method?
- [CS06-007] What happens if you do not provide a constructor in a class?
- [CS06-008] What are the types of constructors, and what is a copy constructor?
- [CS06-009] Can constructors be overloaded, and how does constructor chaining work?
- [CS06-010] Can a constructor be private, and what are the use cases?
- [CS06-011] What is a destructor or finalizer, and why is it used?
- [CS06-012] Do all languages implement destructors the same way (RAII, garbage-collected finalizers)?
- [CS06-013] What does 'this' or 'self' refer to inside a class?
- [CS06-014] What is the difference between static (class) and instance members, when should each be used, and what restrictions apply to static methods?
- [CS06-015] What are enums used for in object-oriented design, and when do they replace conditional logic or class hierarchies?
- [CS06-016] What are the benefits of immutable objects, and how do you design a class to be immutable?
- [CS06-017] What is the difference between a value object and an entity, and why does it matter for equality and immutability?
- [CS06-018] What is the difference between equals and identity comparison, and what is the contract between equals and hashCode?
- [CS06-019] What is the difference between a shallow copy and a deep copy, and when does each cause bugs?
- [CS06-020] What are the core principles of functional programming, and how do they compare with object-oriented programming, especially for concurrency?
- [CS06-021] What is generic programming, and how do generics give type safety compared with raw types or type erasure?
- [CS06-022] Python has no truly private members. How does it still support encapsulation, and how does that differ from Java?

## Encapsulation, abstraction and interfaces
- [CS06-023] What is encapsulation and why is it important?
- [CS06-024] What is the difference between encapsulation and data hiding?
- [CS06-025] How do you achieve encapsulation, and how do access modifiers (public, protected, private, package-private) support it?
- [CS06-026] Can encapsulation be broken, for example through reflection or by exposing mutable internals?
- [CS06-027] Why are getters and setters sometimes considered an anti-pattern, and how do you protect class invariants without exposing state?
- [CS06-028] A getter returns a reference to an internal mutable list. What can go wrong, and how do you fix it?
- [CS06-029] What is abstraction, and how is it implemented (abstract classes, interfaces)?
- [CS06-030] What is the difference between abstraction and encapsulation?
- [CS06-031] In a payment processing system, how do abstraction, encapsulation and polymorphism each help?
- [CS06-032] What is an interface, and why use interfaces together with polymorphism?
- [CS06-033] What is the difference between an abstract class and an interface?
- [CS06-034] How do you decide between an abstract class and an interface when designing a type hierarchy?
- [CS06-035] Why and when would you use an abstract class, and can it be instantiated?
- [CS06-036] Can an abstract class have a constructor, and why would it?
- [CS06-037] Can an abstract class have no abstract methods, and why would you do that?
- [CS06-038] How do you decide between using an abstract class and using composition?
- [CS06-039] What did default and static methods in interfaces change, how do they blur the line with abstract classes, and what risks do they add?
- [CS06-040] How is the conflict resolved when a class implements two interfaces that define the same default method?
- [CS06-041] How do Python abstract base classes and duck typing differ in how they enforce an interface?
- [CS06-042] What are pure virtual functions in C++, and why should a base class with virtual functions have a virtual destructor?

## Inheritance and composition
- [CS06-043] What is inheritance, and what are its types? Which languages allow multiple inheritance?
- [CS06-044] How do you implement inheritance in Java, C++ or Python, and what happens if a derived constructor does not call super()?
- [CS06-045] Why does Java not support multiple class inheritance?
- [CS06-046] What is the diamond problem, and how do Java, C++ and other languages avoid or resolve it?
- [CS06-047] How do inheritance, mixins and composition compare for reuse, and when is multiple inheritance justified?
- [CS06-048] What problems do deep inheritance hierarchies cause, and what is the fragile base class problem?
- [CS06-049] Does the choice between 'is-a' and 'has-a' always give a clear answer? How do you decide which relationship fits?
- [CS06-050] Why is composition often preferred over inheritance, and when is inheritance still the right choice?
- [CS06-051] How would you design a class hierarchy for a real-world problem, and how do you decide what belongs in the base class?
- [CS06-052] A design uses inheritance to share code between unrelated classes. How would you refactor it to composition, and what would you gain?
- [CS06-053] A subclass overrides a method that the parent class calls internally and breaks the parent's invariants. How does this happen, and how do you prevent it?

## Polymorphism, overriding and dispatch
- [CS06-054] What is polymorphism, and what are its types?
- [CS06-055] Does polymorphism require inheritance, and how does polymorphism differ from inheritance?
- [CS06-056] What is the difference between compile-time and runtime polymorphism?
- [CS06-057] How does method overriding enable runtime polymorphism, and why is that useful?
- [CS06-058] What are the rules for method overloading and overriding, and how do they differ, including for static methods?
- [CS06-059] Why is method overloading useful, and in what ways can a method be overloaded?
- [CS06-060] Can a method be both overloaded and overridden?
- [CS06-061] Can you override static methods? Why or why not?
- [CS06-062] What is dynamic dispatch (dynamic method dispatch), how does it resolve calls in an inheritance hierarchy, and how does it differ from static binding?
- [CS06-063] How does dynamic dispatch work under the hood using a virtual table?
- [CS06-064] Why is calling an overridable method from a constructor dangerous?
- [CS06-065] What do covariance and contravariance mean for return and parameter types when overriding a method?
- [CS06-066] What do upcasting and downcasting mean, and why can downcasting fail at runtime?
- [CS06-067] What is object slicing in C++, and how can it break polymorphism?
- [CS06-068] How do Go's struct embedding and implicit interfaces provide reuse and polymorphism without inheritance, and what are the downsides?
- [CS06-069] How does Rust provide encapsulation, aggregation and inheritance-like reuse without classes, and why would you use trait objects?

## Object relationships, coupling and UML
- [CS06-070] What is the difference between association, aggregation and composition?
- [CS06-071] How do object lifetimes differ between aggregation and composition, and how does that affect ownership and deletion?
- [CS06-072] When should you use aggregation rather than composition or inheritance?
- [CS06-073] What is the difference between unidirectional and bidirectional association, and what maintenance problems do bidirectional links cause?
- [CS06-074] What is a dependency relationship in UML, and how does it differ from association?
- [CS06-075] What are coupling and cohesion, and what should we aim for?
- [CS06-076] Why is low coupling useful, and how do you measure or improve coupling and cohesion?
- [CS06-077] What is the Law of Demeter (principle of least knowledge), and how does violating it lead to tight coupling?
- [CS06-078] What is the tell-don't-ask principle, and how does it improve object design?
- [CS06-079] What is an anemic domain model, and why is it often considered an anti-pattern?
- [CS06-080] What does 'program to an interface, not an implementation' mean, and why does it matter?
- [CS06-081] What is separation of concerns, and how do modularity and layered architecture implement it?
- [CS06-082] What is the difference between inheritance-based and delegation-based reuse, and how does the delegation pattern work?
- [CS06-083] What are the main UML diagram types, and which are most useful in a design interview?
- [CS06-084] How do you notate inheritance, interface realization, association, aggregation, composition and dependency in a UML class diagram?
- [CS06-085] What do multiplicity and navigability mean on an association in a class diagram?
- [CS06-086] When would you draw a sequence diagram rather than a class diagram?
- [CS06-087] What does a use case diagram capture, and how do actors and use cases relate to requirements?
- [CS06-088] How do activity diagrams differ from state machine diagrams, and when is a state machine the right tool for modelling an object?
- [CS06-089] Sketch the class diagram for a library management system. Which relationships (inheritance, association, composition) would you choose and why?

## SOLID principles
- [CS06-090] What are the SOLID principles? Explain each with a short example of a violation.
- [CS06-091] Explain the Single Responsibility Principle. How do you identify a class with more than one responsibility?
- [CS06-092] Explain the Open/Closed Principle and how polymorphism helps satisfy it in practice.
- [CS06-093] What does the Liskov Substitution Principle require, and why does a Square extending Rectangle violate it?
- [CS06-094] Why does a subclass that throws UnsupportedOperationException for an inherited method violate the Liskov Substitution Principle?
- [CS06-095] Explain the Interface Segregation Principle and what a fat interface causes for its clients.
- [CS06-096] Explain the Dependency Inversion Principle with an example. What is being inverted?
- [CS06-097] How do the five SOLID principles work together?
- [CS06-098] You are given shape classes that compute area. How do you add a new shape without modifying existing code?
- [CS06-099] Review a class that violates several SOLID principles at once and describe how you would refactor it step by step.
- [CS06-100] Can following SOLID too rigidly hurt a codebase? Describe the trade-off between abstraction and simplicity.

## Dependency injection and inversion of control
- [CS06-101] What is dependency injection, why is it used, and what are constructor, setter and interface injection?
- [CS06-102] Explain Inversion of Control and the Hollywood principle, and how IoC relates to dependency injection.
- [CS06-103] How does dependency injection affect maintainability and unit testing?
- [CS06-104] Compare constructor injection, setter injection and method injection. When would you use method injection?
- [CS06-105] Is there a preferred type of dependency injection when working with immutable objects?
- [CS06-106] Can mixing different types of injection in the same class cause problems?
- [CS06-107] What is a dependency injection container, what are its responsibilities, and how do you configure dependencies in it?
- [CS06-108] When would you choose manual wiring or a lightweight container over a full-fledged DI framework?
- [CS06-109] What is the difference between dependency injection and the service locator pattern?
- [CS06-110] What are singleton, scoped and transient lifetimes in a DI container, and what bugs arise from mismatched lifetimes?
- [CS06-111] How can you use interfaces and dependency injection to make an external API client testable and replaceable?
- [CS06-112] A service creates its own concrete database class inside its constructor. Walk through how you would apply DIP and DI to decouple it.
