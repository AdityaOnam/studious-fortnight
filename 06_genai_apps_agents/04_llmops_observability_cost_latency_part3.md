---
domain: genai
topic: llmops_observability_cost_latency
title: LLMOps, observability, cost and latency
tags: [llmops, observability, cost, latency]
count: 118
part: 3/4
---
# LLMOps, observability, cost and latency (part 3)

## Model versioning, rollout and rollback
- [GA04-208] What is model versioning, and how do you handle model rollbacks?
- [GA04-209] What is the role of feature flags in AI deployments?
- [GA04-210] How do you handle model updates and migrations without downtime?
- [GA04-211] Model versions now ship weekly. How do you keep model selection current without breaking production?
- [GA04-212] A new frontier model is released and scores better on your benchmarks. What happens before it reaches customers?
- [GA04-213] Why are model migrations treated as deploys, and how do you gate them?
- [GA04-214] What triggers should cause an automatic rollback of an LLM deployment?
- [GA04-215] What does a rollback look like when an LLM regression came from the model provider rather than from your own deploy?
- [GA04-216] How would you structure a model rollback so a customer mid-task is not switched to a different model underneath them?
- [GA04-217] How do you move thousands of customer-built agents to a new model without switching a customer mid-task?
- [GA04-218] What is your rollback plan if a hospital appointment-scheduling agent misbooks a slot at 2 a.m.?
- [GA04-219] A customer's voice agent runs on an older real-time TTS model and product wants the newer, more expressive one. How do you decide, and how do you roll it out?
- [GA04-220] A new model version is better on average but worse for two of your supported languages. Do you ship it, hold it back, or route those locales elsewhere?
- [GA04-221] What is your rollout and monitoring plan for adding a fifth and sixth language to a multilingual assistant?

## Model deprecation and provider migration
- [GA04-222] How do you handle model updates and deprecations from providers over the life of a product?
- [GA04-223] Your provider is retiring the model your product runs on in 60 days. How do you migrate safely?
- [GA04-224] An agent you shipped four months ago runs on a base model being deprecated in 60 days. How do you swap the model without regressing quality, and what had to be in place beforehand?
- [GA04-225] Your model provider deprecates the model your product depends on, with 90 days' notice. How would you handle the migration?
- [GA04-226] How would you handle a model deprecation with 30 days' notice instead of 90?
- [GA04-227] How do you eval-gate a provider-initiated model deprecation that forces you onto a new version?
- [GA04-228] How do you handle model deprecation across dozens of air-gapped installs?
- [GA04-229] Why is a prompt tested on one model not validated on a newer version of the same model?
- [GA04-230] When migrating to a new model, do you first re-tune the old prompt for the new model or re-derive the prompt from the task spec?
- [GA04-231] How do you decide when a model or provider migration is done?
- [GA04-232] How do you handle prompt changes needed for a model upgrade?
- [GA04-233] You want to switch model providers and your prompts break. Why, and how would you have made them portable without sinking to the lowest common denominator?
- [GA04-234] Design a model registry that survives divergent deprecation calendars across vendors and clouds.
- [GA04-235] A vendor changes its subscription terms so usage limits no longer cover third-party agent harnesses. What does this tell you about vendor lock-in risk in your architecture?
- [GA04-236] You moved a prompt from a hosted API to a self-hosted copy of the same open-weight model and quality dropped. What do you check?
- [GA04-237] Why can a chat template that drops the system prompt still pass a casual smoke test?
- [GA04-238] How would you build a regression test that fails when someone changes the chat template?
- [GA04-239] Once token sequences match between hosted and self-hosted serving and quality is still lower, what do you suspect next?

## Rate limiting and quotas
- [GA04-240] What is the difference between RPM and TPM limits, and why can you hit one without hitting the other?
- [GA04-241] Your application hits LLM provider rate limits at peak hours. How do you handle 429s and quotas properly?
- [GA04-242] How do you design rate limiting and throttling for an LLM API you serve, including cost management?
- [GA04-243] Would you use a fixed window, sliding window, or token bucket for LLM API rate limiting, and why?
- [GA04-244] How do you implement rate limiting and circuit breaking for an LLM API, including token-rate control and backpressure?
- [GA04-245] Design a rate limiter for an LLM API where cost scales with tokens, not requests.
- [GA04-246] Why are requests-per-second quotas the wrong unit for a shared LLM platform, and what would you use instead?
- [GA04-247] How do you rate-limit by tokens per minute when you do not know the output token count upfront?
- [GA04-248] How do you rate-limit fairly when one customer's requests all have 100k-token contexts?
- [GA04-249] Where does a token-based LLM API rate limiter sit relative to the inference scheduler's own admission control?
- [GA04-250] Your provider gives you 2M tokens/minute. How do you rate-limit your own users so you do not blow through it?
- [GA04-251] When rate-limiting by tokens, how do you handle one legitimately huge request, such as a 300-page PDF upload?
- [GA04-252] When one tenant is 60% of traffic, do you throttle them even when there is spare capacity?
- [GA04-253] How would you set per-user quotas if legitimate power users are 50x heavier than the median user?
- [GA04-254] Where must per-tenant cost attribution live in an LLM system so you can detect a denial-of-wallet attack?
- [GA04-255] In a customer-facing chatbot backend, where do you enforce per-user spend limits in the request path?
- [GA04-256] In an LLM service that enriches questions with a third-party API, what changes if that API rate-limits you at 10 requests per second?
- [GA04-257] When an upstream model hits RPM or TPM limits, how should a gateway queue requests, degrade, or switch models?
- [GA04-258] How do you decide the priority between free-tier chat and paid-tier background jobs when capacity is constrained?

## Retries, timeouts and reliability patterns
- [GA04-259] Why do LLM API calls need retries, rate limiting, fallback, and structured output validation?
- [GA04-260] LLM APIs are slow, expensive, and flaky. How does your retry strategy differ from retrying a normal REST dependency?
- [GA04-261] How do you implement a robust LLM retry mechanism in Python, including exponential backoff?
- [GA04-262] Why is full jitter better than plain exponential backoff?
- [GA04-263] Right after a launch the provider starts returning 429s, and your clients retry immediately, which makes it worse. What is the fix?
- [GA04-264] Which kinds of errors should an LLM API client not retry?
- [GA04-265] Your retries are succeeding but P99 latency tripled. What is happening, and what do you change?
- [GA04-266] How do you prevent a retry storm from turning an incident into a five-figure LLM bill?
- [GA04-267] A timeout fires on an LLM call but the provider actually completed the request and billed you. How do you detect and account for that?
- [GA04-268] How do you set timeouts for LLM calls given highly variable generation time: a total deadline, a time-to-first-token limit, or a per-token idle timeout?
- [GA04-269] How do you make LLM calls safe to retry when the call can trigger tool side effects?
- [GA04-270] Design the reliability layer for calls to an LLM provider: timeouts, retries, circuit breakers, and idempotency.
- [GA04-271] What is the difference between a circuit breaker and a retry?
- [GA04-272] How do bulkheads, circuit breakers, and timeouts layer together in an LLM client?
- [GA04-273] How should an application treat retries and hedging when the provider also enforces rate limits?

## Failover and multi-provider resilience
- [GA04-274] How do you handle failover and fallback strategies for AI systems when the primary model is unavailable or rate-limited?
- [GA04-275] How do you implement automatic multi-model failover, including failover chains and degradation strategies?
- [GA04-276] How would you design a multi-provider LLM architecture for 99.9% availability?
- [GA04-277] One LLM provider outage took down your entire system. How do you eliminate single points of failure?
- [GA04-278] Your application depends on one LLM provider. How do you switch providers without downtime?
- [GA04-279] Your multi-LLM pipeline fails when one model in the chain breaks. How do you handle orchestration failure?
- [GA04-280] One failing AI component can take down your whole platform. How do you design graceful degradation and degradation levels?
- [GA04-281] Traffic doubles overnight and you cannot get more GPU capacity for a week. What are your graceful-degradation options?
- [GA04-282] Your agent platform runs 40-step tasks on a single frontier provider that just logged four outages in four days. Design for provider failure.
- [GA04-283] How do you keep outputs consistent when steps of one task span two LLM providers?
- [GA04-284] Your gateway falls back from one model to another mid-conversation, and both quality and error rates get worse. What is going on?
- [GA04-285] How do you fail over a long-running agent conversation to another provider?
- [GA04-286] Why must fallback models be eval-gated rather than just API-compatible?
- [GA04-287] A circuit breaker fails over to a cheaper second-provider model during an outage, and a week later you learn quality quietly dropped. What was missing?
- [GA04-288] Your primary model provider goes down. What does your incident response look like?
- [GA04-289] The fallback provider's quota is half your peak load. Who gets cut, and where is that encoded?
- [GA04-290] How do you test LLM provider failover without causing an incident?
- [GA04-291] What is the difference between active-active and active-passive setups across LLM providers, and when would you choose each?
- [GA04-292] Implement a client pool over multiple LLM providers with failover, where providers fail, time out, or rate-limit and callers should just get a completion.
- [GA04-293] How would you build an abstraction over multiple LLM providers, and what breaks?
- [GA04-294] How would you architect a system that works across OpenAI, Anthropic, and local open-weight models?
- [GA04-295] How do you design a system so the model layer stays swappable?
- [GA04-296] With every AI lab shipping its own agent SDK, how do you avoid vendor lock-in?

## LLM gateways
- [GA04-297] What is the gateway pattern for LLM API management, and what does an AI gateway add beyond calling providers directly?
- [GA04-298] Why does a production environment need an LLM gateway, and what problems arise when business services call model APIs directly?
- [GA04-299] Do you really need an LLM gateway? When is it overkill, and what would you do instead?
- [GA04-300] What is the difference between an LLM gateway and an LLM router?
- [GA04-301] What is the relationship between an LLM gateway and RAG, agents, and MCP?
- [GA04-302] How do you choose between a self-built gateway, LiteLLM, Cloudflare AI Gateway, Kong AI Gateway, and similar routers?
- [GA04-303] How do you measure how well an LLM gateway is doing?
- [GA04-304] Rate-limit errors are your top production failure. How does an LLM gateway help, and how could it make things worse?
- [GA04-305] Where does an LLM gateway live, as a library in each service or a standalone proxy, and why?
- [GA04-306] Should model routing live in your product or in a generic gateway?
- [GA04-307] Your gateway holds every provider key. How do you secure it?
- [GA04-308] How do you run evals continuously across backends in an LLM gateway without exploding cost?
- [GA04-309] Which cross-cutting features would you put in an LLM gateway, such as auth, caching, logging, guardrails, and budgets, and which would you keep out?
- [GA04-310] The gateway becomes a single point of failure for all LLM traffic. How do you design it for availability?

## Streaming and response handling
- [GA04-311] How do you implement streaming output for an LLM application, and how do you choose between SSE and WebSocket?
- [GA04-312] What is time to first token, and why does it often matter more than total latency for chat UX?
- [GA04-313] Why does streaming improve user experience, and does it reduce total latency or token cost?
- [GA04-314] How would you stream an LLM response through FastAPI with server-sent events?
- [GA04-315] How do you stream structured output such as JSON to a UI while still validating it?
- [GA04-316] Write the server-side handler for streaming token generation, handling client disconnects correctly.
- [GA04-317] A user closes the tab halfway through a streamed response. What happens on the server, and what should happen?
- [GA04-318] What is the cost signature in your metrics of client disconnects that are never detected?
- [GA04-319] How would you implement a resumable stream for an LLM response?
- [GA04-320] How do you propagate a mid-stream engine failure to a client that already received an HTTP 200?
- [GA04-321] Where would you meter tokens for billing in a streaming LLM service, and do aborted requests bill for generated-but-undelivered tokens?
- [GA04-322] A streamed call dies after about 800 of an expected 1,000 tokens and your generic retry decorator re-fires the whole request. What is the problem, and what is the better design?
- [GA04-323] How does failover across LLM providers interact with a streaming response that is already half-sent to the user?
- [GA04-324] Your production code reads the response text but never checks finish_reason or stop_reason. Why is that a bug, and what do you do with each stop reason?
- [GA04-325] Your length-stop rate doubled after a model upgrade with no prompt change. What happened, and what do you change?
