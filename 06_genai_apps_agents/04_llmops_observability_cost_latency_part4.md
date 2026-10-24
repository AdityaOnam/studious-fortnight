---
domain: genai
topic: llmops_observability_cost_latency
title: LLMOps, observability, cost and latency
tags: [llmops, observability, cost, latency]
count: 153
part: 4/4
---
# LLMOps, observability, cost and latency (part 4)

## Prompt caching
- [GA04-326] How does prompt (prefix) caching work, and why is it one of the biggest cost levers available?
- [GA04-327] Where does prompt caching change the cost model of an LLM API, and what invalidates a cached prefix?
- [GA04-328] Your prompt-cache hit rate is near 0% despite a large, seemingly stable system prompt, or it dropped to near zero after a deploy. What do you look for?
- [GA04-329] How would you measure prompt-cache hit rate, and what would a low hit rate tell you?
- [GA04-330] How would you alert on prefix-cache hit rate without paging on every deploy?
- [GA04-331] What deploy-time check would catch a prompt-prefix change that breaks prefix caching before it ships?
- [GA04-332] Where would you place prompt-cache breakpoints in a multi-tenant agent with shared tools but per-user memory?
- [GA04-333] How does prompt caching interact with per-user ACL'd context?
- [GA04-334] How does caching interact with personalised prompts?
- [GA04-335] A feature sends a 1,200-token prompt (1,000 tokens of stable system prefix) and returns about 250 tokens on a frontier model at 200k requests/day. Where is the biggest cost win?
- [GA04-336] A RAG chat assistant reuses a 1,500-token system prompt and retrieved context on every call. How do you cut cost and latency most effectively?

## Response and semantic caching
- [GA04-337] Design the caching strategy for an LLM-backed feature: what can you cache, what can't you, and what is the invalidation story?
- [GA04-338] Which workload is semantic response caching most likely to help?
- [GA04-339] What is semantic caching, how is it different from prompt or prefix caching, and what are its failure modes?
- [GA04-340] How do you design an LLM semantic cache, including similarity threshold and TTL, and how do you trade off hit rate against accuracy?
- [GA04-341] Design the cache key for a semantic cache in a multi-tenant RAG product.
- [GA04-342] What is semantic drift in caching, and how do you prevent it?
- [GA04-343] Why is a semantic cache sometimes more expensive than a raw LLM call at low volume?
- [GA04-344] You already use provider prompt caching. Should you also add a semantic cache?
- [GA04-345] How would you detect that your semantic-cache similarity threshold is causing false hits in production, and how do you measure whether it serves wrong answers?
- [GA04-346] What cache hit rate do you need before the complexity of an LLM cache pays for itself?
- [GA04-347] How do you detect that a previously stable query has gone hot so you can invalidate its cache?
- [GA04-348] Where would you cache to cut latency for common queries in a real-time voice agent?
- [GA04-349] What are the security risks of a shared semantic cache across users or tenants?

## Model routing and cascades
- [GA04-350] What is semantic routing, and how do you implement it in a multi-model system?
- [GA04-351] How would you design a router that dynamically selects the cheapest model that can handle a query at acceptable quality, and how do you decide the routing boundary empirically?
- [GA04-352] Design tiered model routing that drops cost by 50% without regressing quality.
- [GA04-353] Design cost-aware multi-provider LLM routing given very different per-token prices across frontier and low-cost models.
- [GA04-354] Where does semantic caching fit in a cost-aware multi-provider routing design?
- [GA04-355] Design a request-level model router that achieves frontier quality at much lower cost. Where do the training labels come from, and how do you avoid feedback loops?
- [GA04-356] How do you build a difficulty router for LLM requests without labelled data?
- [GA04-357] Design a confidence-thresholded router using logprobs. What would you validate?
- [GA04-358] What is a cascade pattern of models, and how do you decide the escalation signal?
- [GA04-359] You add a router that sends easy queries to a cheap model and hard ones to a frontier model. How do you evaluate the router?
- [GA04-360] Your model router cuts cost 60% and aggregate quality drops 1 point. What else do you check before shipping?
- [GA04-361] How would you evaluate a cascade that tries the cheap model first and escalates on low confidence, versus routing up front?
- [GA04-362] You add a cheap-to-expensive model cascade and savings look great at launch, but two months later spend is back up with flat traffic. What is the likely cause and the right instrumentation?
- [GA04-363] How do you evaluate a model router that sends sensitive queries to a different model?
- [GA04-364] A high-volume extraction endpoint with a shallow task and strict structured output runs on a reasoning model for accuracy, and cost and p99 are too high. What is the best move?
- [GA04-365] Which step types in a long-running agent would you never hand to a cheap model, and how would you prove that with data? Is the split static rules or learned routing?
- [GA04-366] When processing 10M document pages per month with a model cascade, how do you decide the escalation threshold and when the frontier model's accuracy gain justifies 20x the cost?
- [GA04-367] How does the document-processing cascade design change if 40% of pages are handwritten?
- [GA04-368] How would you decide, per query, whether to answer on-device or escalate to the cloud?

## Reasoning effort and thinking budgets
- [GA04-369] Why do output tokens cost more than input tokens, and how should that shape how you build?
- [GA04-370] How do reasoning tokens change your cost model for an agentic loop?
- [GA04-371] When is it worth paying for more output tokens for chain-of-thought?
- [GA04-372] When would you use extended or adaptive thinking versus standard mode, and how do you control costs?
- [GA04-373] How would you build a router that picks the model and reasoning effort level per query?
- [GA04-374] How would you decide a thinking budget per request class in production?
- [GA04-375] What would you monitor in production to detect that your chosen reasoning budget has drifted out of calibration?
- [GA04-376] A model upgrade improved quality but doubled reasoning tokens. How do you decide whether to adopt it?
- [GA04-377] How would you expose effort levels of an agent model to customers so they do not all pick the maximum?

## Cost estimation, ROI and attribution
- [GA04-378] How do you estimate the cost of running an AI-powered feature in production?
- [GA04-379] How do you set the cost budget per request and per month for an LLM system?
- [GA04-380] Estimate the annual serving cost of adding an LLM summary feature for 100 million weekly active users, and explain how you would cut it by 10x.
- [GA04-381] Estimate the cost and turnaround of an LLM diligence workflow over a 5,000-document data room, and say which lever you would pull first.
- [GA04-382] A team wants to move a 300K-token-context workload to another provider because both list the same per-token price. What do you check?
- [GA04-383] How would you measure cost per successful task rather than prompt-cache hit rate?
- [GA04-384] How do you measure the ROI of an AI feature, and how do you evaluate and control the ROI of an AI agent?
- [GA04-385] How do you justify the cost of an AI system to a CFO?
- [GA04-386] Why do AI products have worse gross margins than SaaS, and what do engineers do about it?
- [GA04-387] How can token costs be attributed to tenants, users, features, models, and prompt versions?
- [GA04-388] How would you attribute LLM cost to a specific customer without high-cardinality metrics?
- [GA04-389] How do you attribute the cost of a shared prompt cache across tenants?
- [GA04-390] How do you price internal chargeback when 60% of a tenant's input tokens are cache hits?
- [GA04-391] One tenant is 60% of your agent platform's spend and 2% of revenue. What do you do technically?
- [GA04-392] How do you keep LLM costs under control in a multi-tenant product?
- [GA04-393] In a multi-tenant LLM product, a tenant's spend doubled overnight. Walk me through the investigation.
- [GA04-394] How do you detect a silent LLM API repricing before finance does?
- [GA04-395] How do you handle token counting for cost control and context planning?

## Cost investigation and reduction
- [GA04-396] Your LLM costs are 10x higher than expected. Walk through your investigation.
- [GA04-397] Your LLM bill doubled month over month with flat traffic. How do you find and fix it?
- [GA04-398] Your agent platform's bill jumped from $8k to $40k in a month and nobody knows why. How do you find out, and how do you make sure it never happens blind again?
- [GA04-399] Your LLM bill tripled this quarter. Design a cost-engineering programme covering attribution, cascades, and context management.
- [GA04-400] Your CFO says cut inference spend by 70% without killing quality. What is your plan, and how do you prove quality held?
- [GA04-401] Your LLM costs are too high in production. How do you reduce them without degrading quality?
- [GA04-402] How do you engineer an agent for cost and latency without wrecking quality?
- [GA04-403] How would you optimize costs for a high-volume RAG application?
- [GA04-404] How do you optimize prompts for cost and latency?
- [GA04-405] What is prompt compression, and how do methods like LLMLingua work?
- [GA04-406] Your AI agent burns too many tokens per task. How do you reduce token consumption in long-running workflows?
- [GA04-407] Your AI agent keeps exceeding its budget per task. What is a token budget, and how do you enforce it so agents cannot run away with cost?
- [GA04-408] How do you govern the cost of LLM applications, and what cost controls are needed besides token metering?
- [GA04-409] Why does caching tend to be the top cost lever, and how do batch and async tiers change the economics?
- [GA04-410] How do you monitor an agent's token consumption and cost, and what optimization strategies exist?
- [GA04-411] How do you instrument cost and latency for an agentic feature, and what actually drives cost creep?
- [GA04-412] Your cost per task doubled but every per-call metric is flat. Where do you look?
- [GA04-413] Why would an agent's monthly bill grow much faster than the number of steps per task?
- [GA04-414] Cost per call on your agent has been flat for weeks, yet the monthly bill is climbing and tasks resolve at the same rate. What is happening?
- [GA04-415] Why can aggressive history truncation increase cost in an agent?

## Latency budgets and tail latency
- [GA04-416] How do you design for latency versus quality trade-offs in AI systems, and when would you accept worse quality for speed?
- [GA04-417] How do you optimize latency for real-time LLM applications?
- [GA04-418] What are time to first token, inter-token latency, and end-to-end latency, and which matters for which product?
- [GA04-419] How does output length drive latency and cost, and how would you shorten outputs without hurting quality?
- [GA04-420] Why do we obsess over P99 latency rather than the average, and what causes tail latency in LLM serving specifically?
- [GA04-421] Why does an agent workflow's end-to-end tail latency degrade faster than any single call's?
- [GA04-422] Your LLM API has latency spikes during peak hours. How do you stabilize it?
- [GA04-423] Your LLM endpoint's p99 latency doubled after a deploy with no model change. Walk through the diagnosis.
- [GA04-424] If an LLM endpoint's p99 latency doubled but p50 is flat, what does that tell you?
- [GA04-425] p50 time-to-first-token is unchanged and only p95 regressed. What does that tell you?
- [GA04-426] For an LLM feature, P50 latency is fine but P99 is 30 seconds. What do you look at?
- [GA04-427] What alarm or dashboard would have caught a p99 latency regression before customers noticed?
- [GA04-428] An interactive LLM feature has p50 TTFT of 600 ms but p99 of about 8 s, and cost has headroom. What is the strongest lever?
- [GA04-429] When would you hedge LLM API requests, and when does request hedging pay off?
- [GA04-430] An enterprise customer reports slow LLM responses. Token counts are unchanged and the canary is slow only at peak hours. What do you investigate next?
- [GA04-431] A Copilot chat feature has a p95 budget of 3 seconds to first useful content. Where does the time go, and how do you cut it?
- [GA04-432] What would you do differently for a 300 ms autocomplete latency budget compared with a chat feature?
- [GA04-433] Walk through the latency and cost budget of a RAG query: query understanding, retrieval, rerank, generation, guardrail. What is the p99 budget per stage, and where do you cut?
- [GA04-434] Your RAG system's p95 latency is 4 s and product wants 1.5 s. Walk through the cuts you would make, in order.
- [GA04-435] In a RAG query pipeline, where do you put timeouts, and what degrades gracefully: dropping the reranker or a slow shard?
- [GA04-436] How do you set per-span latency budgets when different teams own different spans?

## Scaling, capacity and load testing
- [GA04-437] How do you implement auto-scaling and capacity planning for AI workloads?
- [GA04-438] What is the role of load balancing in AI serving infrastructure?
- [GA04-439] How do you handle cold start latency for serverless AI deployments?
- [GA04-440] What is the difference between synchronous and asynchronous inference, and when do you use each?
- [GA04-441] When do you put a queue in front of LLM work, and what does that architecture look like?
- [GA04-442] Your AI system handles 100 requests/sec but crashes at 5000. How do you scale for concurrent requests?
- [GA04-443] A traffic spike brings down your AI system. How do you handle peak traffic?
- [GA04-444] How do you scale an AI app to 1 million users, or 1 million LLM queries per day, in production?
- [GA04-445] How do you make batched concurrent calls to an LLM API with asyncio and httpx or worker pools, handling errors, timeouts, cancellation, backpressure, and concurrency limits?
- [GA04-446] How do you load test an LLM service, including the prompt corpus, so the numbers actually mean something?
- [GA04-447] Why does a closed-loop load test with 100 workers understate P99 latency?
- [GA04-448] At what QPS does self-hosting the reranker beat the API?
- [GA04-449] What changes in an LLM deployment if the customer requires a specific processing region with lower capacity?

## Batch processing and service tiers
- [GA04-450] When would you use a batch API, and how do you design a pipeline around one?
- [GA04-451] How do you handle an LLM batch job that comes back 2% failed?
- [GA04-452] Your nightly LLM batch pipeline now needs 4-hour freshness. What changes?
- [GA04-453] A provider offers a 50%-discount batch API with 24 h latency. When do you switch to it for running an LLM call over 50,000 documents?
- [GA04-454] When running an LLM call over 50,000 documents, how would you checkpoint safely if two runs might execute concurrently?
- [GA04-455] In a large LLM batch enrichment job, how do you re-enrich records when the prompt improves without paying full price?
- [GA04-456] Provider batch API (50% cheaper, hours of latency) versus your own queue: when does each win?
- [GA04-457] Providers sell the same model at several service tiers: standard, priority, flex or batch, and provisioned throughput. How do you decide which traffic goes where?
- [GA04-458] Your provisioned LLM capacity runs at 40% utilisation overnight. What do you route into it?
- [GA04-459] How do you decide whether a feature's P99 latency is worth paying priority-tier prices for?

## Additional questions
- [GA04-460] How do you design code review processes for a world where a majority of pull requests are generated by AI agents?
- [GA04-461] After changing the model or modifying the prompt, how do you validate the effect using offline evaluation, trace replay, and online canary release?
- [GA04-462] What changes when your product must handle prompts and content in multiple languages?
- [GA04-463] How would you build a drift monitor that catches behaviour changes in a mocked service used for agent RL training, not just schema changes?
- [GA04-464] If persona drift correlates with higher user retention, what do you do?
- [GA04-465] How would you set the token budget for a voice reply on smart glasses versus a chat reply?
- [GA04-466] A workflow passes evals on the frontier model but fails on the air-gapped model. What are your options besides buying more GPUs?
- [GA04-467] How do you evaluate voice agents, and what is the accuracy-experience trade-off?
- [GA04-468] What are error analysis, open coding and axial coding for LLM products, and why must PMs and QAs take part?
- [GA04-469] What is theoretical saturation in error analysis, and how many traces should you review?
- [GA04-470] When do you use code-based evaluators instead of LLM judges?
- [GA04-471] How do you evaluate multi-step pipelines at the state level and analyze failure distributions?
- [GA04-472] How do you evaluate multi-turn conversations, and which metrics matter?
- [GA04-473] What is the difference between error analysis and automated evals, and when should each be prioritized?
- [GA04-474] How do you prevent evaluation sets from being memorized or leaked into training or prompts?
- [GA04-475] How would you evaluate a new accelerator or serving platform for your fleet?
- [GA04-476] Which memory leaks commonly occur in production agents and how do you track them?
- [GA04-477] How does the Python GIL affect AI services, and how do you work around it?
- [GA04-478] How do you secure LangGraph production debugging with time travel and checkpointing?
