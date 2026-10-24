---
domain: sd
topic: api_design_microservices_architecture
title: API design, microservices, architecture
tags: [api-design, microservices, rest, grpc]
count: 112
part: 3/3
---
# API design, microservices, architecture (part 3)

## Monolith versus microservices
- [SD04-207] What is a microservice, and how does it differ from a monolithic architecture?
- [SD04-208] What are the main benefits of using microservices?
- [SD04-209] What benefits and costs come from building a system as microservices rather than a monolith?
- [SD04-210] Compare monolith, modular monolith and microservices architectures.
- [SD04-211] Is microservice architecture a silver bullet, and why might a team be better off not adopting it?
- [SD04-212] When would you split a monolithic e-commerce application into distributed services, and when would you deliberately keep it as a monolith?
- [SD04-213] Why did a video quality monitoring team move from serverless microservices back to a monolith and save around 90 percent in cost, and what does it teach about architecture choices?
- [SD04-214] What new problems does moving to microservices introduce, such as distributed transactions, latency, observability and deployment complexity?
- [SD04-215] What are the pitfalls of microservices, such as the distributed monolith, and how do you avoid them?
- [SD04-216] What are the DevOps implications of a monolith versus microservices?
- [SD04-217] What principles and best practices underlie a good microservices architecture, such as independent deployability, ownership and observability?
- [SD04-218] How should service boundaries be decided when splitting a monolith?
- [SD04-219] How would you decompose a monolithic application into microservices?
- [SD04-220] Your team runs a large monolith and wants to migrate to microservices incrementally. How would you plan and execute it without a big-bang rewrite?
- [SD04-221] How would you decide the right size of a service, and what is the nano-service anti-pattern?

## Microservice communication and design patterns
- [SD04-222] How do microservices collaborate and communicate with each other?
- [SD04-223] Compare synchronous and asynchronous communication between microservices: when to use each, the failure modes of each, and where queues and back pressure fit.
- [SD04-224] How do you avoid tight coupling between services?
- [SD04-225] How do you handle data consistency when each microservice owns its own database?
- [SD04-226] What is the difference between orchestration and choreography in microservice workflows, and when would you use a workflow engine rather than plain events?
- [SD04-227] How do you handle exceptions and partial failures in a microservices architecture?
- [SD04-228] What design patterns are commonly used in microservices architectures?
- [SD04-229] How do cloud design patterns such as bulkhead, circuit breaker and retry help an application?
- [SD04-230] How does the sidecar pattern work?
- [SD04-231] What are the essential components of a production microservice application beyond the business services, and what does a typical architecture look like end to end?
- [SD04-232] How would you design an API whose response combines the responses from three other microservices?
- [SD04-233] How can a Java main site reliably integrate a Python agent service, and at which layer should authentication, SSE, timeouts, circuit breaking and observability sit?
- [SD04-234] How do you trace a single request across ten microservices, and what do you need to put in place for that?
- [SD04-235] A call chain across five services has a p99 latency far worse than any single service. How do you investigate and reduce it?

## API gateway and Backend for Frontend
- [SD04-236] What does an API gateway do, and why do we need one in a microservices architecture?
- [SD04-237] How does an API gateway work internally?
- [SD04-238] Which cross-cutting concerns should an API gateway handle, such as authentication, rate limiting, routing and logging?
- [SD04-239] How do you implement authentication at the API gateway versus in the services?
- [SD04-240] Where should rate limiting live, at the API gateway or in each service?
- [SD04-241] How do you handle canary releases through an API gateway?
- [SD04-242] Compare the features of an API gateway with those of a service mesh.
- [SD04-243] What are the boundaries between an API gateway and Nginx, a load balancer, and a BFF?
- [SD04-244] What is the Backend for Frontend pattern, and when is it worth using?
- [SD04-245] How do you make an API gateway highly available and keep it from becoming a bottleneck or single point of failure?
- [SD04-246] Explain a two-tier gateway architecture with a traffic gateway and a business gateway, and why teams adopt it.
- [SD04-247] How does a gateway implement dynamic routing without restarts?
- [SD04-248] What is the difference between route predicates and filters in a gateway, and how do global and per-route filters differ?
- [SD04-249] Why did gateways move from blocking thread-per-request models to non-blocking designs?
- [SD04-250] What are the downsides of putting business logic in an API gateway?

## Service discovery, service mesh and configuration
- [SD04-251] Why do we need service discovery?
- [SD04-252] In a microservices architecture, how do services find each other, especially when instances scale up and down?
- [SD04-253] Compare client-side and server-side discovery, and self-registration versus third-party registration.
- [SD04-254] What are the roles of the registry, provider and consumer in a service registration and discovery architecture?
- [SD04-255] What are the differences between ZooKeeper, Eureka and Nacos when used as a service registry?
- [SD04-256] How do health checks and deregistration work in a service registry, and what happens when a registry node fails?
- [SD04-257] What are the disadvantages of a service discovery system, and how do Consul, etcd and ZooKeeper address health checking and key-value lookup?
- [SD04-258] What is a service mesh, how does it help manage microservices, and what does it solve compared with putting the logic in client libraries?
- [SD04-259] What are the costs and risks of adopting a service mesh, and when would you avoid it?
- [SD04-260] What problems does a centralized configuration center solve compared with config files in each service, and how do you manage configuration across environments?
- [SD04-261] What is the difference between a configuration center and a service registry, and where does Kubernetes ConfigMap fit?
- [SD04-262] Compare push, long-polling and pull mechanisms for propagating configuration changes to clients.
- [SD04-263] How should a client survive a configuration center outage, including local snapshots and startup order?
- [SD04-264] What features does a production configuration center need, such as versioning, gray release, rollback, audit and permissions?
- [SD04-265] Design a configuration center that supports millions of config reads and near real-time updates across thousands of clients.

## Domain-driven design
- [SD04-266] What is Domain-Driven Design, and what are its core principles?
- [SD04-267] What are the key concepts of DDD, such as bounded context, aggregate, entity and value object?
- [SD04-268] How does DDD differ from a traditional data-driven or service-driven approach?
- [SD04-269] What is the difference between the domain model and the data model in DDD?
- [SD04-270] What are bounded contexts in DDD, and why are they important, including in microservices?
- [SD04-271] What strategies can you use to define bounded contexts in a large system?
- [SD04-272] How do you integrate multiple bounded contexts within a single system?
- [SD04-273] Why is ubiquitous language important in DDD, and how do you establish it?
- [SD04-274] What is the role of entities in DDD, and how do they differ from value objects?
- [SD04-275] How would you identify aggregates in a domain model, and what boundary rules apply to them?
- [SD04-276] What considerations are there for implementing aggregates so that transactional consistency is preserved?
- [SD04-277] What is a domain event, and when would you use one?
- [SD04-278] How do repositories function in DDD, and how does a repository differ from a service?
- [SD04-279] What is the role of a domain service versus an application service?
- [SD04-280] How would you handle complex domain logic that involves multiple entities and value objects?
- [SD04-281] How is DDD related to microservices, and how does it help you decide where service boundaries should be drawn?
- [SD04-282] What is an anti-corruption layer, and when would you use one?

## SOA, ESB and middleware
- [SD04-283] What are the core principles of Service-Oriented Architecture?
- [SD04-284] What is the difference between SOA and a microservices architecture?
- [SD04-285] How does SOA differ from traditional monolithic application architectures?
- [SD04-286] What is a service contract in SOA, and what factors do you consider when designing a service interface?
- [SD04-287] How does SOA facilitate service reusability, and why is loose coupling important?
- [SD04-288] What is the difference between service orchestration and service choreography in SOA?
- [SD04-289] What role does a service registry play in SOA?
- [SD04-290] How is versioning of services handled in a SOA environment?
- [SD04-291] Describe a scenario in which you would choose synchronous over asynchronous communication between services.
- [SD04-292] What data formats are commonly used for service communication in SOA?
- [SD04-293] What is an Enterprise Service Bus, how does it support SOA, and in what scenario would you choose one?
- [SD04-294] Why did the industry move away from the enterprise service bus?
- [SD04-295] How does middleware facilitate decoupling of components, and what common functionality does it provide?
- [SD04-296] How does middleware support both synchronous and asynchronous communication, and data format transformation between disparate systems?
- [SD04-297] What is the purpose of a service layer in a layered architecture?

## Architecture patterns and quality attributes
- [SD04-298] What is the difference between software architecture and software design, and why do we need software architecture?
- [SD04-299] What is a system quality attribute, and why is it important in software architecture?
- [SD04-300] What are the elements of a good software architecture?
- [SD04-301] What is an architectural pattern?
- [SD04-302] What is the layered architectural pattern, what are its benefits, and what do the layers of a three-tier application do?
- [SD04-303] What is an N-tier architecture, and how do 1-tier, 2-tier and 3-tier differ?
- [SD04-304] Why separate the application server tier from the web tier, and what are the disadvantages of an extra application layer?
- [SD04-305] Describe the Model-View-Controller pattern.
- [SD04-306] How are cross-cutting concerns addressed in software architecture?
- [SD04-307] Compare layered, event-driven, microkernel, microservices and space-based architectures.
- [SD04-308] What is a plugin or SPI mechanism in a microkernel architecture, and how does it let you extend behavior without modifying the core?
- [SD04-309] How do you make an architecture decision when two quality attributes conflict, such as latency versus consistency? Walk through a concrete example.

## Event-driven and reactive architecture
- [SD04-310] What is event-driven architecture, and how does it differ from request-response architecture?
- [SD04-311] What are the trade-offs of event-driven integration between services, including ordering, duplication and debugging?
- [SD04-312] How do you evolve event schemas without breaking consumers?
- [SD04-313] What are the defining characteristics of a reactive system according to the Reactive Manifesto?
- [SD04-314] Contrast elasticity with scalability, with specific examples.
- [SD04-315] How is back pressure implemented in reactive systems to manage data flow?
- [SD04-316] Compare synchronous request-response communication with reactive message-driven communication in terms of scalability.
- [SD04-317] What role do reactive systems play in processing continuous data streams, and what industry use cases exist?
- [SD04-318] When would you choose an event-driven design over direct API calls between services, and when would it be a mistake?
