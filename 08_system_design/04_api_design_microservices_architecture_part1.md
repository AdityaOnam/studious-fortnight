---
domain: sd
topic: api_design_microservices_architecture
title: API design, microservices, architecture
tags: [api-design, microservices, rest, grpc]
count: 104
part: 1/3
---
# API design, microservices, architecture (part 1)

## API and REST fundamentals
- [SD04-001] What is an API, and how does an API differ from a web service?
- [SD04-002] What is an API endpoint?
- [SD04-003] Is every API a web service? Give examples of APIs that are not web services.
- [SD04-004] What is REST, and what is the difference between REST and a RESTful API?
- [SD04-005] Which HTTP methods are commonly used in a REST API, and what does each one do?
- [SD04-006] How do you map CRUD operations to HTTP methods, and when is POST versus PUT appropriate for creating a resource?
- [SD04-007] What are the differences between PUT and PATCH, and when should you use each?
- [SD04-008] What is the difference between GET and POST, and which properties such as safety and idempotency matter for API design?
- [SD04-009] In a RESTful API, how should resource paths, HTTP methods and status codes be used together?
- [SD04-010] What makes an API truly RESTful rather than just REST-like?
- [SD04-011] What principles make an API easy for clients to consume and safe to use?
- [SD04-012] What are the main drawbacks of using REST?
- [SD04-013] How would you authenticate and authorize clients of a public API, and how do API keys, OAuth 2.0 and JWTs fit together?
- [SD04-014] Design APIs that let developers access an LLM provider's models securely and efficiently.
- [SD04-015] You are asked to design a public API for a new product. Walk through the key decisions: resources, auth, errors, pagination, versioning and rate limits.

## REST constraints, statelessness and HATEOAS
- [SD04-016] What are the REST constraints, and which ones are most often compromised in practice and why?
- [SD04-017] Why is statelessness important in REST, and how does it improve scalability?
- [SD04-018] In a stateless API, how do you handle user context and session management?
- [SD04-019] What are the challenges of implementing stateless APIs, and what is wrong with storing conversation state on the server?
- [SD04-020] Can you offer real-time features through a stateless API?
- [SD04-021] What are the benefits of the client-server constraint?
- [SD04-022] How does the uniform interface constraint improve API design?
- [SD04-023] How does the cacheable constraint improve API performance, and what are examples of cache-friendly REST patterns?
- [SD04-024] Which HTTP caching headers would you use for a read-heavy API, and how do ETag and conditional GET work?
- [SD04-025] Why is the layered system constraint important for modern APIs?
- [SD04-026] Can you explain the levels of the Richardson maturity model?
- [SD04-027] What is HATEOAS, what problem does it solve, and why is it considered the highest level of REST maturity?
- [SD04-028] Is HATEOAS worth the cost in practice? Compare it with out-of-band documentation and with pragmatically embedding links.
- [SD04-029] Are HATEOAS and REST required together?
- [SD04-030] How do you version and document hypermedia link relations, and how would you test that links are present and correct?

## Resource and URL design
- [SD04-031] Why should REST URLs use nouns instead of verbs?
- [SD04-032] Should collection URLs use singular or plural nouns, and what other URL naming conventions matter?
- [SD04-033] How do you design clean resource URLs, and when should you use path parameters versus query parameters?
- [SD04-034] How do you handle nested resources in URL design?
- [SD04-035] How do you represent actions such as approve or cancel in REST paths, and how do you handle other non-CRUD operations?
- [SD04-036] What are the downsides of action-based endpoints?
- [SD04-037] How would you refactor /createUser and /updateUser endpoints into a RESTful design?
- [SD04-038] How do you evolve a non-RESTful API toward REST without breaking existing clients?
- [SD04-039] How do you design URLs for file uploads and downloads, and what are the trade-offs between multipart uploads and direct-to-storage uploads?
- [SD04-040] How do you resume interrupted uploads and downloads?
- [SD04-041] How do you design URLs for complex queries and reports?
- [SD04-042] How would you model a many-to-many relationship, such as users and groups, in a REST API?

## Payloads, content negotiation and errors
- [SD04-043] Why is JSON preferred for most web APIs?
- [SD04-044] Compare JSON and XML for performance and tooling. How do you validate each, and when would you still choose XML?
- [SD04-045] How do you implement content negotiation to serve JSON and XML, and language negotiation in a REST API?
- [SD04-046] What are the performance implications of content negotiation, and how should mobile and desktop clients handle it differently?
- [SD04-047] Why prefer a top-level JSON object over a top-level array in API responses?
- [SD04-048] Compare JSON Patch with JSON Merge Patch.
- [SD04-049] How do you handle partial updates safely?
- [SD04-050] How do you prevent lost updates when two clients edit the same resource concurrently?
- [SD04-051] Which HTTP headers improve the ergonomics of CRUD APIs, and how should rate limit information be communicated through headers?
- [SD04-052] Which HTTP status codes would you return for create, update, delete, validation failure, unauthorized, forbidden, conflict and rate-limited requests?
- [SD04-053] How should the server and the browser each handle HTTP errors, especially when the client is at fault?
- [SD04-054] What makes a good error response in a REST API, and how do you design error envelopes that are readable by both machines and humans?
- [SD04-055] When would you use the Problem Details format (RFC 7807) for errors, and what fields would you include?
- [SD04-056] How do you structure validation errors, including cases with multiple field issues, for good client UX?
- [SD04-057] Where should validation live in a layered architecture?
- [SD04-058] What are the trade-offs between JSON Schema and custom validators, and how do you validate nested arrays and objects?
- [SD04-059] What is the difference between 400, 409 and 422, and how do you decide among them for a request that conflicts with business rules?

## Pagination, filtering and search
- [SD04-060] How do you paginate API responses, and what considerations influence your choice of approach?
- [SD04-061] What are the trade-offs between offset-based and cursor-based pagination?
- [SD04-062] Why does offset-based pagination become slow with large offsets, and how do you avoid deep paging?
- [SD04-063] How do you implement keyset pagination over a composite sort key such as created_at plus id?
- [SD04-064] How do you handle pagination when the underlying data changes between requests?
- [SD04-065] What can go wrong with pagination and sorting consistency?
- [SD04-066] A client reports duplicate and missing items when paging through a feed sorted by timestamp. How do you debug and fix it?
- [SD04-067] How would you design a consistent pagination response shape?
- [SD04-068] Should an API return the total count with each page, and what does it cost?
- [SD04-069] How do you implement pagination in a stateless manner?
- [SD04-070] What is the best way to implement pagination for search results?
- [SD04-071] How should you handle pagination in mobile applications?
- [SD04-072] How do you implement pagination for aggregated or grouped data?
- [SD04-073] What pagination strategy works best for real-time data streams?
- [SD04-074] What is the best approach for paginating across multiple data sources?
- [SD04-075] How do you design a consistent filtering and sorting API for a collection endpoint, including complex filters?
- [SD04-076] How do you prevent abuse of filtering and sorting queries?
- [SD04-077] How do you implement sparse fieldsets and projections?
- [SD04-078] When should you add a dedicated search endpoint instead of filters, and how would you expose complex search versus simple filters?
- [SD04-079] How do you design facets and aggregations in API responses?

## Idempotency and retries
- [SD04-080] What is idempotence in API design, why is it important, and which HTTP methods are idempotent by definition?
- [SD04-081] Which HTTP methods are safe and which are idempotent, and how should you make POST requests safe to retry?
- [SD04-082] Describe several techniques for making a write endpoint idempotent, such as a unique index, dedup table, token or optimistic lock.
- [SD04-083] How would you design an Idempotency-Key header: where to store keys, how long to keep them, and what to do when the same key arrives with a different payload?
- [SD04-084] A client times out on POST /payments and retries. How do you guarantee the customer is charged exactly once?
- [SD04-085] How does a one-time token mechanism prevent duplicate submissions, and what races does it need to handle?
- [SD04-086] When using a token to prevent duplicate submissions, what are the risks in the order of consuming the token versus executing the business logic?
- [SD04-087] How can a unique business key combined with a status check guard against duplicate processing of messages?
- [SD04-088] Design idempotent handling for a payment callback that the provider may deliver multiple times and out of order.
- [SD04-089] How would you test and verify that an idempotency scheme works under concurrency and retries?
- [SD04-090] Why are retries in a workflow engine unsafe without idempotent steps?

## Bulk and long-running operations
- [SD04-091] How do you design bulk CRUD endpoints, and how do you handle bulk operations in REST?
- [SD04-092] How do you design idempotent bulk operations?
- [SD04-093] When should you return 200 versus 207 for bulk results?
- [SD04-094] How do you handle validation and transactions for bulk operations?
- [SD04-095] How do you handle partial failures and report errors in bulk or batch operations?
- [SD04-096] How do you paginate bulk input, and what batching strategies exist?
- [SD04-097] How do you stream large bulk results?
- [SD04-098] When should you choose an asynchronous pattern for an API operation instead of a synchronous one?
- [SD04-099] How do you indicate that a long-running operation has started, for example with 202 Accepted and a status URL?
- [SD04-100] An agent task takes 2 to 10 minutes. How do you design the API so clients can start, track and resume such jobs?
- [SD04-101] How do you secure job status endpoints?
- [SD04-102] How do you handle failures, retries and error reporting for asynchronous API jobs?
- [SD04-103] How do you estimate and report progress of a long-running job?
- [SD04-104] How would you let a client cancel a running asynchronous job, and what guarantees can you give?
