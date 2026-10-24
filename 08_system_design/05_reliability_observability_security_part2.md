---
domain: sd
topic: reliability_observability_security
title: Reliability, observability, security in system design
tags: [reliability, observability, slo, security]
count: 121
part: 2/2
---
# Reliability, observability, security in system design (part 2)

## Disaster recovery and multi-region
- [SD05-084] Why is disaster recovery important?
- [SD05-085] Why do replicas not replace backups, and how do you verify that a backup can actually be restored?
- [SD05-086] What do RTO and RPO mean, and how do they drive the choice of a disaster recovery architecture?
- [SD05-087] What do RTO and RPO each constrain, and what costs does an RPO of 0 bring?
- [SD05-088] Compare cold, warm and hot standby sites in cost and recovery time.
- [SD05-089] Compare backup and restore, pilot light, warm standby and multi-site active-active disaster recovery strategies.
- [SD05-090] Compare same-city disaster recovery, remote disaster recovery, same-city active-active and geo-distributed active-active.
- [SD05-091] How do you justify the cost of a design and trade it off against availability and durability requirements?
- [SD05-092] How do you route traffic between regions (GeoDNS, anycast, global load balancer) and fail it over?
- [SD05-093] What are the main challenges of multi-region active-active, particularly data consistency and traffic routing?
- [SD05-094] What hidden dependencies (control plane, IAM, DNS) can break a failover plan during a full cloud region outage?
- [SD05-095] Design disaster recovery for a payments database with an RPO of seconds and an RTO of 15 minutes.
- [SD05-096] What are the key considerations for multi-region deployment of AI systems?
- [SD05-097] How would you drain a region for a deploy of a real-time TTS service without dropping live calls?
- [SD05-098] What is your failure model when one chip in a several-hundred-chip inference instance goes down mid-request?
- [SD05-099] In a ChatGPT-scale serving stack, how do you handle a region losing 30% of its GPU capacity?

## Observability: logs, metrics, traces and alerting
- [SD05-100] What is the ELK stack and why is it popular for centralized logging?
- [SD05-101] What is the difference between monitoring and observability? How do logs, metrics and traces complement each other?
- [SD05-102] Compare the push and pull models for a metrics system, such as Prometheus-style scraping versus agents pushing.
- [SD05-103] What are the RED and USE methods, and when would you apply each?
- [SD05-104] What key indicators would you monitor to ensure system reliability?
- [SD05-105] What should be monitored in production (system, application, business metrics) so you detect issues before users report them?
- [SD05-106] How do you implement a monitoring system that accurately reflects system availability?
- [SD05-107] What metrics predict incidents early?
- [SD05-108] How do you detect partial outages?
- [SD05-109] What is the problem with high-cardinality metric labels, and how do you control it?
- [SD05-110] How do you design actionable alerts, and why alert on symptoms rather than causes?
- [SD05-111] How would you alert on a sudden drop in sign-up conversion without causing alert fatigue?
- [SD05-112] How do you trace requests across services?
- [SD05-113] How can a trace ID be propagated across HTTP, RPC and message queues?
- [SD05-114] How are trace and span IDs generated and propagated in distributed tracing, and what uniqueness properties do they need?
- [SD05-115] Compare head-based and tail-based sampling in distributed tracing.
- [SD05-116] What log levels exist, and how do you choose what to log at each level in production?
- [SD05-117] What should and should not be written to application logs, and how do you log errors without exposing sensitive data?
- [SD05-118] How do you implement comprehensive security monitoring for REST APIs?
- [SD05-119] What metrics would you export to observe the health of a consensus cluster, such as leader changes and replication lag?
- [SD05-120] Design a centralized logging pipeline that ingests one million log lines per second.
- [SD05-121] At 3 a.m. you are paged for a p99 latency spike. Walk through how you use logs, metrics and traces to find the cause.

## Deployments, CI/CD and cloud basics
- [SD05-122] What is the difference between blue-green and canary deployment?
- [SD05-123] Compare blue-green, canary, rolling and recreate deployment strategies.
- [SD05-124] How would you design a zero-downtime deployment, and how do you roll back safely?
- [SD05-125] How would you roll out a new version of a microservice safely, and how does gray release differ from blue-green?
- [SD05-126] How would you roll out a risky change to a live system with the ability to roll back quickly?
- [SD05-127] Blue/green versus rolling deployment for a model version bump: which would you choose and why?
- [SD05-128] A rolling deploy of 20 LLM serving replicas with 5-minute drains takes forever. How do you speed it up without killing streams?
- [SD05-129] How do feature flags differ from canary releases, and when would you use each?
- [SD05-130] How do you change a database schema during a zero-downtime deployment (expand and contract)?
- [SD05-131] Which metrics would drive an automated canary analysis and rollback decision?
- [SD05-132] What does a continuous integration pipeline do, and what benefit does it give a team?
- [SD05-133] What is the difference between continuous integration, continuous delivery and continuous deployment?
- [SD05-134] What are the main stages of a CI/CD pipeline and what quality gates should be present?
- [SD05-135] How do we manage configurations in a system?
- [SD05-136] What does cloud native mean, and how do you transform a system to be cloud native?
- [SD05-137] Explain the cloud shared responsibility model.
- [SD05-138] What is the difference between a security group and a NACL?
- [SD05-139] Compare virtual machines and containers and when you would use each.
- [SD05-140] What are the main Kubernetes service types and when do you use each?
- [SD05-141] What are the top Kubernetes design patterns, such as sidecar and ambassador?
- [SD05-142] How does AWS Lambda run code behind the scenes, and what causes cold starts?
- [SD05-143] What Docker best practices matter for production images?
- [SD05-144] What is the difference between DevOps, SRE and platform engineering?
- [SD05-145] What are the hidden costs of the cloud that engineers often overlook when designing systems?

## Authentication and authorization design
- [SD05-146] What is the difference between authentication and authorization?
- [SD05-147] How do you design secure access to a web API?
- [SD05-148] What are the top forms of authentication mechanisms for APIs and when would you use each?
- [SD05-149] Explain session-cookie authentication. How does it work across multiple server nodes, and what if the client disables cookies?
- [SD05-150] Why do cookie-based sessions need CSRF protection, and how do token headers change the picture?
- [SD05-151] Compare session-based authentication with JWT. What are the revocation and scaling issues of each?
- [SD05-152] What are the three parts of a JWT, and what does each contain?
- [SD05-153] How does JWT authentication work, what is the difference between decoding and verifying a token, and what prevents payload tampering?
- [SD05-154] What are the main advantages of stateless JWT authentication over server-side sessions?
- [SD05-155] How do you log out or revoke a JWT before it expires, given that the token is stateless?
- [SD05-156] How do you implement JWT renewal with short-lived access tokens and refresh tokens?
- [SD05-157] What security practices strengthen a JWT deployment, such as algorithm pinning, short expiry, secure storage and key rotation?
- [SD05-158] What is OAuth 2.0, which roles does it define, how does the authorization code flow work, and what does OpenID Connect add?
- [SD05-159] Why is the authorization code flow preferred over the implicit flow?
- [SD05-160] Compare the common OAuth 2.0 flows and when each should be used.
- [SD05-161] What problem does PKCE solve, and when is it required?
- [SD05-162] What is single sign-on, and what benefits does it bring?
- [SD05-163] Compare SAML with OAuth 2.0 and OpenID Connect, and describe how single sign-on works.
- [SD05-164] Design an SSO system covering login state storage, ticket validation, logout propagation and cross-domain login.
- [SD05-165] How do you authenticate service-to-service calls inside a microservice mesh, for example mTLS versus signed tokens?
- [SD05-166] What is RBAC, and how does it differ from ABAC?
- [SD05-167] How do you design a permission system? Compare ACL, DAC, MAC, RBAC and ABAC.
- [SD05-168] How do you secure file access per user or role?
- [SD05-169] Design an authorization system for an enterprise platform with menu, data and operation permissions, role management and an audit trail.
- [SD05-170] Design an authentication and authorization service that supports OTP, OAuth and similar methods.

## Data protection, secrets and abuse protection
- [SD05-171] What is sensitive data?
- [SD05-172] How do you manage sensitive data and secrets in a system, including encryption at rest and in transit?
- [SD05-173] How do you design a secure system overall, covering network, application, data and operational concerns?
- [SD05-174] What are the key steps for building secure APIs?
- [SD05-175] How can you configure middleware to ensure secure data transmission?
- [SD05-176] What is the difference between encryption at rest and in transit, and how does envelope encryption with a KMS work?
- [SD05-177] How would you manage, distribute and rotate secrets such as API keys and database passwords instead of hardcoding them?
- [SD05-178] Compare symmetric and asymmetric encryption, and explain how they combine in practice, such as in TLS.
- [SD05-179] What is the difference between hashing, encryption, encoding and tokenization, and when do you use each?
- [SD05-180] Compare AES and RSA in speed, key management and typical use.
- [SD05-181] How do digital signatures work and what do they guarantee?
- [SD05-182] How should passwords be stored? Why use a salted, slow adaptive hash like bcrypt rather than encryption or MD5?
- [SD05-183] What is a salt and how does it defend against rainbow-table attacks?
- [SD05-184] Why do websites offer password reset rather than password retrieval, and what should a secure reset flow include?
- [SD05-185] How does two-factor authentication such as TOTP work?
- [SD05-186] How do passkeys work and why are they more phishing-resistant than passwords?
- [SD05-187] What is data masking, and where in the pipeline should it be applied for logs, APIs and databases?
- [SD05-188] Why must input validation be done on the server even when the client validates it?
- [SD05-189] What is the difference between input validation, authorization checks and business rule validation, and where does each belong?
- [SD05-190] Design a login API that remains secure even if the SSL certificate is compromised.
- [SD05-191] What does defense in depth mean, and how does a zero-trust model change how you design internal service access?
- [SD05-192] How would you mitigate a DDoS attack on a public service?
- [SD05-193] How can load balancers help mitigate DDoS attacks?
- [SD05-194] How do you prevent and detect API abuse and DDoS attacks?
- [SD05-195] How does a CDN help protect an origin against traffic spikes and attacks?

## Additional questions
- [SD05-196] Design a system that lets multiple teams query a shared dataset without exposing raw data.
- [SD05-197] Compare the token bucket, leaky bucket and sliding window algorithms for rate limiting.
- [SD05-198] Design a sensitive-word filtering service that scans user content at high QPS, and compare brute force, Trie, Aho-Corasick and DFA approaches.
- [SD05-199] How does a Bloom filter act as a quick pre-filter in a content filtering pipeline, and what trade-off do false positives introduce?
- [SD05-200] How can a keyword filter cope with obfuscated variants and support hot updates of the word list without downtime?
- [SD05-201] How do you troubleshoot growing message queue lag in a production consumer?
- [SD05-202] How do you troubleshoot a sudden slowdown of a cache server such as Redis?
- [SD05-203] What is the role of reconciliation in a payment system, and why do you need it even if the system claims exactly-once semantics?
- [SD05-204] Explain double-entry bookkeeping and why a ledger should be append-only.
