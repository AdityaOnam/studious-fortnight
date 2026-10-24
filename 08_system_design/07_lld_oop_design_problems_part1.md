---
domain: sd
topic: lld_oop_design_problems
title: LLD / object-oriented design problems
tags: [lld, ood, design-patterns, class-design]
count: 142
part: 1/2
---
# LLD / object-oriented design problems (part 1)

## LLD interview approach and design principles
- [SD07-001] What steps would you follow in a low-level design interview, from clarifying requirements to the final class diagram?
- [SD07-002] How would you approach a prompt like "design a parking lot, an elevator system, or an LRU cache" in a low-level design round?
- [SD07-003] What clarifying questions would you ask in the first few minutes of an LLD problem, and how do the answers shape your scope?
- [SD07-004] What is the difference between a low-level design interview, a machine coding round and a high-level design interview?
- [SD07-005] How do you identify the core entities, relationships and responsibilities when given a vague object-oriented design problem?
- [SD07-006] When would you choose composition over inheritance in an OOD problem? Give a concrete example from a system you might be asked to design.
- [SD07-007] How do you decide between modelling a concept as an enum, an interface with implementations, or a class hierarchy in an OOD problem?
- [SD07-008] How do you decide between the strategy pattern, the state pattern and plain polymorphism when behaviour varies in your design?
- [SD07-009] How do you decide which design patterns to apply in a low-level design problem without over-engineering?
- [SD07-010] How do SOLID principles translate into concrete decisions when a new requirement, such as a new vehicle type or payment method, arrives?
- [SD07-011] How do you model the boundary between domain objects and service or manager classes in an OOD solution?
- [SD07-012] When should a low-level design use a singleton for services such as a manager or controller, and what testing problems does it cause?
- [SD07-013] How does dependency injection make an LLD easier to extend and test, and where would you inject dependencies in your design?
- [SD07-014] Why should money not be stored in float or double in a class design, and what representation would you use instead?
- [SD07-015] How do you design time-dependent logic (expiry, timeouts, fees) so it can be tested deterministically?
- [SD07-016] How do you handle extensibility questions, such as add a new vehicle type or a new payment method, after you present your design?
- [SD07-017] How do you design input validation and error reporting in the public API of your classes: exceptions, result objects or error codes?
- [SD07-018] How do you keep your low-level design testable, and what would you mock when unit testing the core classes?
- [SD07-019] Which diagrams would you draw in a low-level design interview, and what does each one communicate?
- [SD07-020] Walk through how you would refactor a god-class in a low-level design into cohesive classes using SOLID principles.
- [SD07-021] How do you incorporate concurrency considerations into a low-level design after the single-threaded model is complete?
- [SD07-022] For an in-memory booking system, when would you use a global lock, a per-resource lock or optimistic versioning, and what does each cost?
- [SD07-023] How do you design for idempotency and failure handling in a low-level design that involves payments or bookings?
- [SD07-024] What are common mistakes candidates make in object-oriented design interviews, and how can they be avoided?
- [SD07-025] Halfway through, the interviewer says the system must now run across multiple machines. Which parts of your class design survive and which must change?

## LRU, LFU and cache components
- [SD07-026] Design an LRU cache with O(1) get and put.
- [SD07-027] Which data structures back an O(1) LRU cache and why is each one necessary?
- [SD07-028] Implement an LRU cache with O(1) get/put, then add per-entry TTL expiry.
- [SD07-029] How would you add per-entry TTL expiry and a write-through or write-back backing store to a cache class design?
- [SD07-030] How do you implement TTL expiry in a cache: lazy expiry on access, a background sweeper or a timer wheel, and what are the trade-offs?
- [SD07-031] Extend an LRU cache design to LFU (least-frequently-used). What data structures and bookkeeping change?
- [SD07-032] How would you generalize an LRU cache design into a cache with pluggable eviction policies such as LFU, FIFO and TTL-based?
- [SD07-033] Design a cache module that is generic, reusable and easy to integrate across various modules within an organization.
- [SD07-034] How should a cache API handle a loader function, null results and negative caching: cache-aside versus read-through?
- [SD07-035] How would you make an LRU cache thread-safe while keeping contention low, and what are the trade-offs between a single lock, lock striping and a concurrent design?
- [SD07-036] Design a thread-safe cache with TTL.
- [SD07-037] Many threads request the same missing key at once. How does your cache avoid a stampede of redundant loads?
- [SD07-038] Roughly how much memory overhead does an LRU with 10 million small entries add through its hash map and linked list nodes, and how could you reduce it?
- [SD07-039] The hit ratio of your in-process cache drops sharply after a deploy. How would you debug it?

## Rate limiter design
- [SD07-040] Design an API rate limiter.
- [SD07-041] Compare fixed window, sliding window log, sliding window counter, token bucket and leaky bucket in terms of accuracy, memory and burst handling.
- [SD07-042] Implement a token-bucket rate limiter, then make it distributed.
- [SD07-043] Design a rate limiter library that supports multiple algorithms and per-client limits.
- [SD07-044] How would you design a rate limiter class so the algorithm (token bucket, sliding window, fixed window) is swappable and the limiter is thread-safe?
- [SD07-045] Build a rate limiter whose requirements arrive incrementally: per-tenant limits, burst allowances, then a sliding window. How do you keep the code from collapsing?
- [SD07-046] Implement a token-bucket rate limiter for an LLM API where cost scales with tokens, then make it distributed.
- [SD07-047] How would you choose the limiting key (user, IP, API key, tenant) and stop per-key state from growing without bound?
- [SD07-048] How would you unit test a rate limiter without sleeping in the tests?
- [SD07-049] In a distributed rate limiter backed by a shared store, how do you make check-and-decrement atomic and cope with clock skew between nodes?

## Logging, messaging and scheduling components
- [SD07-050] Design and implement a logger library that applications can use to log messages, with log levels, multiple output destinations and configurable formatting.
- [SD07-051] Which design patterns appear in a typical logging framework (chain of responsibility, singleton, strategy, observer) and what role does each play?
- [SD07-052] How would you support runtime-changeable log levels and per-package loggers in a logging framework design?
- [SD07-053] How would you make a logging framework thread-safe and non-blocking for application threads, and which patterns would you apply?
- [SD07-054] In your logger design, what happens when an appender fails or the disk is full, and how do you prevent logging from crashing or stalling the application?
- [SD07-055] Design an in-memory publish-subscribe system with topics, publishers and subscribers.
- [SD07-056] How would you add message filtering, subscription by pattern and unsubscription at runtime to a pub-sub class design?
- [SD07-057] How would you design delivery guarantees, ordering and slow-subscriber handling in an in-memory pub-sub system?
- [SD07-058] How do you make an in-memory pub-sub broker thread-safe so that publishing never blocks on slow subscribers?
- [SD07-059] Create your own queue that holds JSON messages without using standard library queue classes.
- [SD07-060] Design an in-memory message queue where publishers produce JSON messages and subscribers register regex filters and callbacks at runtime.
- [SD07-061] How would you support dependency ordering among subscribers (A must process after B) and retries on processing failure in an in-memory message queue?
- [SD07-062] How would you detect and prevent circular dependencies between subscribers in a dependency-aware message queue design?
- [SD07-063] Design a thread-safe bounded blocking queue with multiple producers and consumers. How do you coordinate waiting and wake-up?
- [SD07-064] Design an in-memory data streaming service with topics, partitions, producers and consumer offsets.
- [SD07-065] Design and create a task scheduler that runs jobs at given times or intervals using a worker pool.
- [SD07-066] Design a service that calls any given endpoint at a fixed interval.
- [SD07-067] What data structure lets a scheduler find the next due job quickly, and how does a worker sleep until that job is due?
- [SD07-068] Design a scheduler that accepts 10 scheduling requests at a time and can execute 100 jobs at a time, where the jobs are HTTP requests.
- [SD07-069] How do you guarantee a scheduled job is not executed twice when several worker threads poll the same job store?

## In-memory databases and key-value stores
- [SD07-070] Build an in-memory database in levels: SET/GET/DELETE first, then filtered scans, then TTL with timestamps, then file compaction.
- [SD07-071] Build an in-memory key-value store with SET/GET/DELETE, then add transactions with BEGIN/COMMIT/ROLLBACK, including nested transactions.
- [SD07-072] In an in-memory key-value store with transactions, how would you add consistent iteration over all keys in the middle of a transaction?
- [SD07-073] How would you implement nested transactions: full snapshot copies, an undo log or layered overlays, and what does each cost?
- [SD07-074] Design an in-memory database with tables, indexing and basic queries, including adding and removing tables.
- [SD07-075] Design a key-value store and an index.
- [SD07-076] How would you add secondary indexes and transaction support to an in-memory database design?
- [SD07-077] How would you design filter objects (comparisons combined with AND/OR) for scans so new operators can be added without changing the scan code?
- [SD07-078] How would you implement TTL in an in-memory store without a background thread, and when would you compact expired data?
- [SD07-079] Build core business logic for a toy banking application, with a specification that grows across four progressive levels.
- [SD07-080] Create a database ORM step by step.
- [SD07-081] In multi-level machine-coding rounds where each level adds requirements, how do you structure code on day one so later levels do not force a rewrite?

## File systems, editors, parsers and utilities
- [SD07-082] Design an in-memory file system with directories, files, create, list, read and delete operations.
- [SD07-083] Which pattern models files and directories uniformly in an in-memory file system, and how would you add permissions and search?
- [SD07-084] In an in-memory file system, how would you resolve relative paths and compute directory sizes efficiently?
- [SD07-085] Design an in-memory text editor with display, insert, delete, copy, paste, undo and redo commands.
- [SD07-086] Implement the core of a text buffer for an editor with efficient insert/delete at arbitrary positions and fast line lookup. What data structure do you pick?
- [SD07-087] Which design pattern gives you undo and redo in a text editor, and how would you structure the command history?
- [SD07-088] How would you support multi-level undo and redo efficiently for large documents, and what are the memory trade-offs between command and memento approaches?
- [SD07-089] Design a spreadsheet engine with cells, formulas and dependency recalculation.
- [SD07-090] How would you detect cyclic references and recompute dependent cells efficiently in a spreadsheet class design?
- [SD07-091] Design a JSON parser from scratch that validates and parses at the same time and supports nested objects.
- [SD07-092] How would you design a parser for untrusted JSON input so it fails safely on malformed input and resists deeply nested or oversized payloads?
- [SD07-093] Design a CSV parser that handles quoting, escaped delimiters and malformed rows.
- [SD07-094] Design a URL shortener at the class level with key generation, storage and expiry.
- [SD07-095] Design a distributed unique ID generator in the style of Twitter Snowflake.
- [SD07-096] How do you handle clock skew, sequence overflow and worker-id assignment in a Snowflake-style ID generator?
- [SD07-097] Write a web crawler over a domain: first synchronous, then make it async.
- [SD07-098] Design a concurrent Bloom filter.
- [SD07-099] Design a configuration management system with add, delete, search and subscription to configuration updates.
- [SD07-100] Design a business rules engine.
- [SD07-101] Design a unit-testing framework that discovers tests, runs them and reports results.
- [SD07-102] Design a bar graph library.

## Games and turn-based play
- [SD07-103] Design a Tic Tac Toe game with players, board and win detection.
- [SD07-104] How would you generalize a Tic Tac Toe design to an N x N board with K in a row and determine a winner in O(1) per move?
- [SD07-105] How would you extend a Tic Tac Toe design to support an AI player and a human player behind a common interface?
- [SD07-106] Design a Snake and Ladder game with players, board, dice and snakes and ladders.
- [SD07-107] How would you make the dice, board size and winning rule configurable in a Snake and Ladder design?
- [SD07-108] How would you handle snakes and ladders that chain into each other and invalid board configurations?
- [SD07-109] Design a deck of cards.
- [SD07-110] Design a Blackjack game with a dealer, multiple players, betting and hand evaluation.
- [SD07-111] Design Minesweeper, covering board generation, reveal with flood fill, flagging and win and lose detection.
- [SD07-112] Design a Ludo game for two to four players with pieces, a dice, safe squares and captures.
- [SD07-113] In a turn-based multiplayer game, how do you model turn order, a player leaving mid-game and game-over detection?
- [SD07-114] Design a Jackpot machine.
- [SD07-115] Design a card game platform with players, tables, decks, turns and scoring.
- [SD07-116] Design an online card game such as poker.
- [SD07-117] Design a geographically partitioned multi-player card game that supports multiple players and multiple games at a time.
- [SD07-118] Design a chess game with board, pieces, moves, turns and game-end conditions.
- [SD07-119] How would you model piece movement rules, check, checkmate and special moves like castling and en passant in a chess class design?
- [SD07-120] How would you add move history, undo and replay to a chess game design, and which patterns would you use?
- [SD07-121] How would you extend a chess design to support network play, a clock and an AI opponent?

## State-machine devices and controllers
- [SD07-122] Design a vending machine with item selection, payment, dispensing and change return.
- [SD07-123] Which design pattern fits a vending machine's behaviour that changes with its current state, and how would you model the states and transitions?
- [SD07-124] How would you extend a vending machine design to support multiple payment methods (coins, notes, card, UPI) and restocking by an operator?
- [SD07-125] How would you handle failure scenarios in a vending machine design, such as insufficient change, item stuck, or cancellation after partial payment?
- [SD07-126] Design a coffee vending machine that supports multiple beverages, customizable recipes and ingredient inventory.
- [SD07-127] How would you use the decorator or builder pattern to model customizable beverage add-ons in a coffee machine design?
- [SD07-128] How would you handle concurrent orders and ingredient depletion in a coffee machine design, including low-stock alerts?
- [SD07-129] Design a traffic signal control system for an intersection with configurable durations and emergency vehicle handling.
- [SD07-130] How would you model emergency-vehicle preemption and guarantee safe signal transitions in a traffic light controller design?
- [SD07-131] How would you extend a traffic signal design to adapt signal durations to real-time traffic density across multiple intersections?
- [SD07-132] Design an ATM covering card authentication, balance inquiry, cash withdrawal and deposit.
- [SD07-133] Which pattern would you use to model ATM transaction types and ATM states, and why?
- [SD07-134] How does an ATM design decide which denominations to dispense, and how would you make the dispensing strategy extensible?
- [SD07-135] How would you ensure that an ATM withdrawal is atomic and consistent with the bank backend if the network fails mid-transaction?
- [SD07-136] Design an elevator system for a building with multiple elevators, floor requests and a dispatcher.
- [SD07-137] Which pattern models an elevator's movement states (idle, moving up, moving down, door open), and how are transitions handled?
- [SD07-138] What scheduling strategies could an elevator controller use to assign requests to cars, and how do you keep the strategy replaceable?
- [SD07-139] How would you handle concurrent hall calls and in-car requests, overload and emergency stops in an elevator design?
- [SD07-140] Implement a configurable finite state machine library with one start state, multiple end states, runtime-added transitions and per-state notification toggles.
- [SD07-141] How would you design a generic finite state machine so that states and transitions can be added at runtime without breaking running instances?
- [SD07-142] Design a home automation system to remotely control switches and devices, with extensible device types.
