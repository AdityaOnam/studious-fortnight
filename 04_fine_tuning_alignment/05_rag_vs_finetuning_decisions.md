---
domain: finetune
topic: rag_vs_finetuning_decisions
title: RAG vs fine-tuning vs prompting decisions
tags: [rag-vs-finetuning, decision, tradeoffs]
count: 134
---
# RAG vs fine-tuning vs prompting decisions

## Prompting, RAG, and fine-tuning basics
- [FT05-001] Explain prompting, Retrieval-Augmented Generation (RAG), and fine-tuning, and what each one changes about an LLM system.
- [FT05-002] What is the difference between RAG and fine-tuning?
- [FT05-003] What problem does each of prompting, RAG, and fine-tuning solve best, and what can each not fix?
- [FT05-004] What is in-context learning, and how do you decide between it and fine-tuning?
- [FT05-005] In what order would you try prompting, RAG, and fine-tuning on a new problem, and why is that ordering usually the cheapest path?
- [FT05-006] How do you decide between prompt engineering, RAG, tool calling, and fine-tuning for a given problem?
- [FT05-007] What are the architecture patterns for customizing an LLM with proprietary data?
- [FT05-008] Why do people say RAG supplies "knowledge" and fine-tuning supplies "behavior"? Where does that rule of thumb break down?
- [FT05-009] How do you inject domain knowledge into an LLM: prompting, RAG, continued pretraining, or fine-tuning?
- [FT05-010] Does every vertical domain need its own domain-specific LLM? What would you weigh between a general model and a specialized one?
- [FT05-011] How do RAG and agent Skills differ, and how do you decide whether a piece of agent knowledge belongs in a Skill or a RAG corpus?
- [FT05-012] When should an agent skill or prompt-based procedure graduate to fine-tuning?
- [FT05-013] A startup with a limited GPU budget wants a domain-specific assistant. Lay out a decision tree among prompting, RAG, LoRA fine-tuning, and continued pretraining.

## Prompting versus fine-tuning
- [FT05-014] When would you fine-tune a model instead of using prompting or RAG?
- [FT05-015] When might prompt engineering be preferred over task-specific fine-tuning?
- [FT05-016] When should you prefer task-specific fine-tuning over prompt engineering?
- [FT05-017] How do you decide when to stop prompt engineering and fine-tune instead?
- [FT05-018] A model answers factually but will not reliably emit your strict JSON tool schema or house tone, even with a careful prompt and examples. What is the best durable fix?
- [FT05-019] A latency-critical, high-volume classifier uses a 2,000-token few-shot prompt per call and the labels are stable. What is the strongest optimisation?
- [FT05-020] How much training data do you need before fine-tuning beats few-shot prompting?
- [FT05-021] A customer has only 50 labelled examples and wants to fine-tune anyway. What do you tell them?
- [FT05-022] When does many-shot in-context learning substitute for fine-tuning?
- [FT05-023] When does in-context learning fail where fine-tuning succeeds?
- [FT05-024] When does a long cached system prompt beat a fine-tune economically?
- [FT05-025] When would you ship the prompted baseline instead of a fine-tuned model?
- [FT05-026] What would make you undo a fine-tune and go back to prompting?
- [FT05-027] Give an example where you would not fine-tune despite having plenty of data.
- [FT05-028] How do prompt compression or distilling a long prompt into model weights change the cost per call, and when is that worth the effort?
- [FT05-029] Your prompt-only solution hits 85% accuracy and fine-tuning might reach 90%. How do you decide whether that gap is worth it?
- [FT05-030] You fine-tuned a model and general capabilities regressed. How do you diagnose it and decide whether fine-tuning was the right lever?
- [FT05-031] When would you fine-tune instead of using RAG or prompt engineering, and if you do fine-tune, would you choose LoRA or full fine-tuning?

## RAG versus fine-tuning
- [FT05-032] When should you use RAG instead of fine-tuning an LLM, and when the reverse?
- [FT05-033] Why is RAG the stronger choice than fine-tuning for knowledge that changes frequently?
- [FT05-034] Compare RAG and supervised fine-tuning (SFT) for adding knowledge. When would you choose each or combine them?
- [FT05-035] Which factors (update frequency, privacy, latency, cost, hallucination risk) decide RAG versus fine-tuning for an enterprise Q&A product?
- [FT05-036] A support assistant must answer from a knowledge base that changes weekly and cite the document it used. Is the primary lever prompting, RAG, or fine-tuning?
- [FT05-037] "RAG or fine-tuning to make the model answer from our internal wiki?" What is the strongest opening answer?
- [FT05-038] Why would you choose RAG over fine-tuning for a regulated knowledge base that changes monthly, such as a compliance assistant?
- [FT05-039] Your LLM coding assistant generates outdated code using deprecated libraries. How do you fix it?
- [FT05-040] Why is RAG the usual architecture for an enterprise assistant over company data instead of fine-tuning, and where does RAG itself break?
- [FT05-041] How does training data memorisation influence a RAG-versus-fine-tuning decision for private data?
- [FT05-042] Fine-tuning does not reliably inject new facts. Why not, and what happens when you fine-tune on facts the base model does not know?
- [FT05-043] In a bake-off, RAG and fine-tuning score the same. What do you recommend and why?
- [FT05-044] When do you recommend fine-tuning versus fixing retrieval to reduce hallucinations in a RAG assistant?
- [FT05-045] How do you evaluate whether RAG or fine-tuning actually closed the quality gap?
- [FT05-046] For an assistant over a customer's internal document corpus, when would fine-tuning on the corpus actually be defensible?
- [FT05-047] For an assistant over an internal document corpus, how does your RAG-versus-fine-tuning choice change if p95 latency must be under 500 ms?
- [FT05-048] Where would you still fine-tune inside an enterprise RAG product (query understanding, rerankers, embedding models) even though knowledge stays in retrieval?
- [FT05-049] Where would you draw the line at which fine-tuning beats retrieval for factual content?
- [FT05-050] What would change your mind about knowledge editing, that is, directly editing facts into model weights, versus using retrieval?
- [FT05-051] In a fine-tuning pipeline for a customer-support model, where does RAG sit in training data versus serving, and why must the two match?

## Combining approaches and long context
- [FT05-052] When would you use RAG and fine-tuning together, and what does each contribute in the combined system?
- [FT05-053] When would you choose RAG versus long-context stuffing versus fine-tuning?
- [FT05-054] Your corpus is 500 pages and updates monthly. Would you pick RAG, long-context stuffing, or fine-tuning?
- [FT05-055] Estimate the per-query cost and latency of stuffing a 200k-token corpus into every request versus retrieving about 5k relevant tokens.
- [FT05-056] Why can a long context window fail to replace retrieval even when the whole corpus fits?
- [FT05-057] Give an example of a system that combines a fine-tuned model for style and format with RAG for facts. How do you split responsibilities?
- [FT05-058] How does prompt caching change the RAG-versus-long-context economics?
- [FT05-059] At what corpus size, query volume, and update rate does the best choice flip between long context with caching and RAG?

## Fine-tuning readiness and failure modes
- [FT05-060] How do you make the decision to fine-tune?
- [FT05-061] What evaluation would you build before deciding whether to fine-tune?
- [FT05-062] What are the limitations of fine-tuning that interviewers commonly probe?
- [FT05-063] When is fine-tuning the wrong call? Describe failure modes you would warn a team about.
- [FT05-064] What is the ongoing maintenance cost of a fine-tuned model compared with a prompted one when the base model is upgraded?
- [FT05-065] Hosted fine-tuning APIs versus training it yourself: how do you decide?
- [FT05-066] What clauses do you check in a provider's fine-tuning terms before uploading data?
- [FT05-067] When would fine-tuning your own model beat a frontier API?
- [FT05-068] At what point does fine-tuning your own small model beat paying for a frontier model?
- [FT05-069] A small open-weight coding model resolves 35% of internal tasks against 60% for a frontier API the customer cannot use. Is it worth deploying?
- [FT05-070] For a browser-operating agent, how would you use RL or fine-tuning on trajectories versus prompting a general model?
- [FT05-071] How would distilling a frontier model into a smaller fine-tuned model change your cost and quality tradeoffs?
- [FT05-072] What breaks when you migrate a hosted fine-tune to open weights?
- [FT05-073] When would you fine-tune a small model for table extraction instead of prompting a frontier vision-language model?
- [FT05-074] How would you decide between fine-tuning a 7B open vision-language model and just prompting a frontier model, given a fixed budget?

## Stakeholder and customer scenarios
- [FT05-075] A PM says "fine-tune it on our docs so it knows our product." How do you respond?
- [FT05-076] An enterprise customer wants the model to "know our business." How do you decide among prompting, RAG, and fine-tuning?
- [FT05-077] A customer with 2,000 pages of internal PDFs insists on fine-tuning because "we don't want our data leaving in prompts." How do you respond?
- [FT05-078] A customer insists on fine-tuning for prestige reasons rather than need. What do you do?
- [FT05-079] What if the executive mandate really is just "we must say we trained a model"?
- [FT05-080] A customer insists on fine-tuning an open model on their support tickets because "we want our own model," but you think RAG over their knowledge base solves it. What do you do?
- [FT05-081] A client wants better quality, lower latency, and lower cost at once. How do you negotiate the tradeoffs?
- [FT05-082] Classify support tickets into 40 categories: LLM API, fine-tuned small model, or classical classifier? How do you decide?
- [FT05-083] For a 40-category ticket classifier, does a taxonomy that changes quarterly flip your choice between an LLM API, a fine-tuned small model, and a classical classifier?
- [FT05-084] For a support assistant needing house voice, strict output format, and a tool schema over weekly-changing tickets, what is the right primary architecture?

## Self-hosting versus API cost and latency
- [FT05-085] What are the cost tradeoffs between self-hosted and API-based LLM inference?
- [FT05-086] How do you decide between using an LLM API and self-hosting an open-source model?
- [FT05-087] How do you estimate the cost of running a closed-source LLM through an API versus a self-hosted open-source LLM?
- [FT05-088] When would you recommend self-hosting versus using APIs?
- [FT05-089] When is a self-hosted GPU cluster cheaper than an API?
- [FT05-090] At what scale does self-hosting an LLM beat API pricing?
- [FT05-091] When deciding between self-hosting an open-weights model and calling a provider, what monthly token volume would make you re-evaluate?
- [FT05-092] Should an enterprise self-host an LLM inference cluster or use a cloud provider's managed API, and how should it decide?
- [FT05-093] What hidden costs of self-hosting (idle GPUs, on-call, upgrades, evals, scaling) do teams usually forget when comparing against API pricing?
- [FT05-094] How do provisioned-throughput offerings change the calculus of self-hosting an open-weights model versus calling a provider?
- [FT05-095] When would you tell a customer not to self-host an LLM at all?
- [FT05-096] When would you choose local or on-device inference over a cloud API?
- [FT05-097] You are shipping an AI feature in a mobile app. Do you bundle your own model or use the platform's built-in on-device model?
- [FT05-098] How do you control cost and latency when traffic is spiky and a self-hosted model would sit idle most of the day?
- [FT05-099] Your cost model for next year uses today's per-token prices. What will it get wrong?
- [FT05-100] Sketch the break-even math for self-hosting a 70B-class model versus API pricing.
- [FT05-101] At what GPU utilisation does self-hosting an LLM start winning on cost, and how does that change the security argument?

## Open versus closed models and model selection
- [FT05-102] What is the difference between open-source and closed-source LLMs, and when would you choose one over the other?
- [FT05-103] Explain the tradeoffs between proprietary and open-weight models.
- [FT05-104] Open-weights versus closed-weights models: how do you think about the tradeoff as an engineer today?
- [FT05-105] How do you choose between frontier model providers for a production application?
- [FT05-106] How would you select a model for a production RAG system?
- [FT05-107] You want to launch a hosted coding assistant on an open-weight model. How do you choose one?
- [FT05-108] Why are open-weight coding models important for enterprises?
- [FT05-109] How do you choose between candidate models when there is no time for a full bake-off?
- [FT05-110] Provider model versions now change weekly. How do you keep model selection current without breaking production?
- [FT05-111] How do you avoid vendor lock-in when building on a single closed-model API?
- [FT05-112] When would you choose a BERT-style encoder over a decoder-only LLM for a production NLP task?
- [FT05-113] Which licence terms of an open-weight model (commercial use, usage thresholds, derivative restrictions) would block you from shipping it?
- [FT05-114] How would you set up a routing layer that sends easy requests to a small or open model and hard ones to a frontier model?
- [FT05-115] Open-weight models now reach near-frontier quality at much lower cost. How does this change your production architecture decisions?
- [FT05-116] A major lab stops releasing open weights for its newest model. What does that mean for your open-model strategy?

## Privacy, compliance, and data residency
- [FT05-117] What contractual and data-governance questions matter when sending regulated data to a closed API?
- [FT05-118] Hosted model API or self-hosted open weights: how do you make the security and privacy call?
- [FT05-119] How do sovereign-AI and data-residency requirements change your model hosting choice?
- [FT05-120] A regulated customer requires zero data retention, but the best model requires 30-day retention. What are your options?
- [FT05-121] What are the privacy tradeoffs of RAG versus fine-tuning when the data includes personal or confidential information?
- [FT05-122] How do you handle per-user access control in RAG versus a model fine-tuned on all company documents?
- [FT05-123] A customer's CISO says no data can leave their network. How does that constrain your LLM architecture, and what are the options?
- [FT05-124] A customer picks a self-hosted model, then complains quality is worse than the ChatGPT demo they saw. How do you handle it?
- [FT05-125] A customer wants to migrate from a proprietary frontier-model API to an open model. How do you run that engagement?

## Build versus buy and when not to use an LLM
- [FT05-126] How do you decide whether a problem needs AI or a traditional software solution?
- [FT05-127] When is an LLM the wrong tool? Give real examples where you would push back on a PM.
- [FT05-128] A PM insists on "AI-powered" for marketing reasons. What do you build?
- [FT05-129] Where have you seen an LLM replace something that should have stayed deterministic?
- [FT05-130] When should you not use an LLM in a project, or downgrade from an agent to a deterministic workflow?
- [FT05-131] How do you decide between building in-house, buying a vendor product, and calling a model API?
- [FT05-132] Build versus buy versus open-source framework: how do you decide for an LLM platform component?
- [FT05-133] Your team wants an internal AI assistant. Do you build on an open-source agent framework, buy a vendor product, or build custom on a model API plus tool protocol?
- [FT05-134] What metrics and pilot would you run to justify a custom LLM build over an off-the-shelf product?
