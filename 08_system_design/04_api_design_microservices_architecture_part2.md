---
domain: sd
topic: api_design_microservices_architecture
title: API design, microservices, architecture
tags: [api-design, microservices, rest, grpc]
count: 102
part: 2/3
---
# API design, microservices, architecture (part 2)

## API versioning and compatibility
- [SD04-105] Why is API versioning important?
- [SD04-106] What counts as a breaking versus a non-breaking change to an API?
- [SD04-107] What are the main API versioning strategies and their trade-offs, and which would you recommend for a production REST API?
- [SD04-108] How do you evolve an API without breaking existing clients, and what strategies ensure backward compatibility?
- [SD04-109] How do you implement versioning with headers or content negotiation, and how does version negotiation work?
- [SD04-110] What is the difference between semantic versioning and date-based versioning for APIs?
- [SD04-111] How do you properly deprecate an API version?
- [SD04-112] What versioning and compatibility strategies apply to internal versus external APIs, and which works best for microservices?
- [SD04-113] How do you version APIs when clients have very different update cycles, such as mobile apps?
- [SD04-114] What does the tolerant reader principle mean, and how does it help API evolution?
- [SD04-115] What are the challenges of maintaining multiple API versions at once?
- [SD04-116] How should error response formats be handled across API versions?
- [SD04-117] How do you handle database schema changes across API versions?
- [SD04-118] When is backwards compatibility worth more than a better API?
- [SD04-119] How would you roll out a breaking redesign of a widely used library API without breaking downstream forks?
- [SD04-120] How would you sunset an API used by thousands of third-party clients, and how would you measure who is still on the old version?

## API documentation and testing
- [SD04-121] How would you document an API for end users?
- [SD04-122] How do you document pagination, errors and authentication in API documentation?
- [SD04-123] How do you ensure API documentation stays current?
- [SD04-124] How do you version OpenAPI specs?
- [SD04-125] How do you generate SDKs from OpenAPI specs?
- [SD04-126] How do you validate and document parameters in OpenAPI and keep validation logic in sync with the spec?
- [SD04-127] What are the different types of API testing, and when would you use each?
- [SD04-128] How do you test authentication and authorization in REST APIs?
- [SD04-129] What strategies help ensure API contract compatibility during testing, and how do you keep mocks in sync with the contract?
- [SD04-130] How does consumer-driven contract testing work, and when is it better than end-to-end tests?
- [SD04-131] How do you implement effective performance testing for APIs?
- [SD04-132] What are the best practices for test data management in API testing?
- [SD04-133] How do you test error handling and edge cases in APIs?
- [SD04-134] What approaches help test APIs that have external dependencies?
- [SD04-135] When should you use static versus dynamic API mocks?
- [SD04-136] How do you simulate rate limiting, delays and errors in API mocks?
- [SD04-137] How do you transition from mocks to real services?
- [SD04-138] How do you measure and improve API test coverage?

## GraphQL
- [SD04-139] What is GraphQL, and how does it differ from REST?
- [SD04-140] What is a GraphQL schema and why is it important? How are types and scalar types handled?
- [SD04-141] What are queries and mutations in GraphQL, and what role do subscriptions play?
- [SD04-142] Describe the structure of a GraphQL query, including fields, arguments and fragments.
- [SD04-143] What are the main components and core features of a GraphQL architecture?
- [SD04-144] What is the role of resolvers in GraphQL?
- [SD04-145] What are the advantages of GraphQL over other API query approaches?
- [SD04-146] What problems does GraphQL solve, such as over-fetching and under-fetching, and what new problems does it introduce?
- [SD04-147] When would you choose GraphQL over REST?
- [SD04-148] How do you prevent N+1 queries in GraphQL, and how does this show up in real-world resolvers?
- [SD04-149] How does caching work in GraphQL, and how does it differ from REST caching?
- [SD04-150] How do you paginate in GraphQL, and what are Relay-style connections?
- [SD04-151] How do you protect a GraphQL API from expensive or malicious queries, using depth limits, cost analysis or persisted queries?
- [SD04-152] Where should authorization be enforced in a GraphQL API?
- [SD04-153] How are errors reported in GraphQL when the HTTP status is usually 200, and what does that mean for monitoring?
- [SD04-154] Can REST be strongly typed like GraphQL? How?
- [SD04-155] Compare versioning strategies in REST and GraphQL.
- [SD04-156] What are typical performance pitfalls in REST, GraphQL and SOAP APIs?
- [SD04-157] When would you use GraphQL federation or a gateway to compose many backend services into one graph, and what are the risks?

## RPC, gRPC and SOAP
- [SD04-158] How does a remote procedure call work, from the client stub to the server implementation?
- [SD04-159] Compare REST and RPC-style APIs in terms of coupling and ease of evolution.
- [SD04-160] Why prefer REST over RPC for public APIs, and when are RPC-style approaches more appropriate, such as for RPC middleware?
- [SD04-161] What are the benefits and drawbacks of REST for public APIs?
- [SD04-162] Why is RPC commonly used for internal service calls instead of HTTP and REST, and what are its disadvantages?
- [SD04-163] Compare TCP, UDP, RPC and REST as communication mechanisms for internal services.
- [SD04-164] Why is gRPC an RPC framework built on HTTP/2, and is it simply HTTP/2 plus Protobuf?
- [SD04-165] With HTTP/2 available, is RPC still needed?
- [SD04-166] Why is gRPC usually faster than REST over JSON, and what limits its use from browsers?
- [SD04-167] What trade-offs exist between gRPC and REST?
- [SD04-168] What are the four gRPC call types, and when would you use each?
- [SD04-169] Design the .proto for a GenerateReport RPC with request parameters and template ID and a server-streaming response that streams tokens for better time to first token.
- [SD04-170] Why can gRPC load balancing behind an L4 load balancer be uneven, and how would you fix it?
- [SD04-171] What are the rules for evolving a Protobuf schema safely?
- [SD04-172] Compare common RPC serialization formats such as JSON, Protobuf, Thrift and Hessian.
- [SD04-173] How would you design an RPC framework from scratch, including serialization, transport, service discovery and load balancing?
- [SD04-174] Compare REST, GraphQL and gRPC, and say when you would choose each.
- [SD04-175] How does a SOAP API differ from a REST API?
- [SD04-176] What advantages does SOAP still offer in enterprise scenarios?
- [SD04-177] Compare REST, SOAP and gRPC as web services.
- [SD04-178] How would you migrate SOAP services to REST, or wrap a SOAP service so it presents a REST API?
- [SD04-179] When is a non-web API preferable, and how does network transport affect API design?
- [SD04-180] What does protocol-agnostic API design mean, and how do you expose a non-web API as a web service?
- [SD04-181] How do you secure APIs compared with web services?

## Real-time push: polling, SSE and WebSockets
- [SD04-182] What options exist for real-time message push on the web, and how do you choose between short polling, long polling, SSE and WebSocket?
- [SD04-183] What is the difference between WebSockets and Server-Sent Events?
- [SD04-184] When would you choose SSE over WebSockets, and what are the advantages of SSE for one-way server push?
- [SD04-185] What are the trade-offs of long polling under load?
- [SD04-186] Can WebSockets be used to broadcast messages to multiple clients, and how?
- [SD04-187] What fallback mechanisms can you use if a browser or server does not support WebSockets?
- [SD04-188] How do heartbeats, idle timeouts and proxies affect long-lived WebSocket or SSE connections?
- [SD04-189] How do you scale WebSockets horizontally?
- [SD04-190] How would you route a message to the right gateway node when users are connected to many WebSocket servers?
- [SD04-191] Design a real-time notification push system for millions of connected web clients, covering connection management and scaling.
- [SD04-192] How do you resume a stream after a disconnect, for example when an SSE connection drops in the middle of a chatbot answer?
- [SD04-193] When is MQTT preferred over HTTP-based push for devices?
- [SD04-194] How do you implement a streaming SSE endpoint in FastAPI, and how does it differ from using WebSocket?
- [SD04-195] Why do LLM products stream responses, and how does streaming actually work over HTTP?
- [SD04-196] What breaks when you put a naive CDN or proxy in front of server-sent events?
- [SD04-197] In a service that proxies streaming audio from an upstream provider, how do you signal a mid-stream upstream failure to a client that has already received a 200 and some audio?
- [SD04-198] How do you build streaming into a chat UI end to end? Walk through the pieces and the gotchas.
- [SD04-199] How would you implement a stop button correctly for a streaming LLM chat?

## Webhooks and callbacks
- [SD04-200] How do webhooks work?
- [SD04-201] Compare polling, webhooks and SSE for notifying a consumer of changes, and when each is the right choice.
- [SD04-202] How do you ensure webhook reliability and idempotency?
- [SD04-203] How do you verify webhook authenticity and defend against replay attacks?
- [SD04-204] How do you handle client downtime gracefully when delivering webhooks, for example when a client's endpoint is down for an hour?
- [SD04-205] What admin tools help troubleshoot webhook delivery problems?
- [SD04-206] How would you design a payment callback webhook so that it is both reliable and secure?
