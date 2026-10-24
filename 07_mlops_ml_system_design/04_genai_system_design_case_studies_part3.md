---
domain: mlsd
topic: genai_system_design_case_studies
title: GenAI / LLM system design case studies
tags: [genai-system-design, llm-platform, case-study]
count: 95
part: 3/3
---
# GenAI / LLM system design case studies (part 3)

## Agent platforms and long-running agents
- [MS04-172] Design an agentic workflow with a planner/executor and tools.
- [MS04-173] Design an agentic workflow assistant that plans, calls tools and keeps memory across sessions.
- [MS04-174] Design a multi-agent workflow system where agents collaborate on complex tasks.
- [MS04-175] Design a deep research agent.
- [MS04-176] Design an agent that automates an enterprise workflow, for example drafting responses to RFPs using internal documents and a CRM. What does "enterprise-grade" add?
- [MS04-177] Design an always-on AI agent as a long-lived service that can be woken by messages, schedules and webhooks.
- [MS04-178] Why should an agent loop run on the server and not inside the sandbox VM, and what state must be durable across crashes?
- [MS04-179] How do durable workflow engines differ from plain job queues for multi-hour or multi-day agent tasks?
- [MS04-180] How would you let an agent sleep when idle and wake on triggers while keeping compute cost low?
- [MS04-181] How would you design approval gates for irreversible agent actions such as sending emails or making payments?
- [MS04-182] How would you isolate an agent's code execution environment with microVMs, and what must never be placed in the model context?
- [MS04-183] How should an agent system prioritize and deduplicate concurrent triggers from multiple channels?
- [MS04-184] How do you manage long-running agent context through compaction and long-term memory while preserving prompt cache hits?
- [MS04-185] How do you prevent untrusted inputs such as emails and web pages from being treated as user instructions in an agent system?
- [MS04-186] Describe the layers of an agent system from application to hardware, and what the harness, serving system and runtime each contribute.
- [MS04-187] How would you trace, debug and replay a failed multi-step agent run in production?
- [MS04-188] How do you bound the cost and runtime of an agent that loops, and what limits do you put in the platform?

## Voice, multimodal and on-device assistants
- [MS04-189] Design a real-time voice AI agent.
- [MS04-190] Design a production voice agent. Cover pipeline versus speech-to-speech, the latency budget and interruption handling.
- [MS04-191] Design a real-time voice agent for a citizen helpline in Hindi and three regional languages, targeting sub-250 ms perceived latency over a phone line.
- [MS04-192] In a voice agent, how do you handle barge-in, background noise and misrecognized names or numbers?
- [MS04-193] Design a real-time AI transcription system for concurrent audio streams.
- [MS04-194] Design a pipeline that turns about 100k hours per month of call recordings into searchable, analysable data. What are the stages and where does it go wrong?
- [MS04-195] How would you evaluate a call-recording transcription and analysis pipeline end to end when you have no reference transcripts for your own calls?
- [MS04-196] Where would you put a human in the loop in a call-recording analysis pipeline, given the volume?
- [MS04-197] Design a voice-based system that fills a shopping cart through spoken conversation.
- [MS04-198] Design the serving system for a multimodal assistant (text and image in, streaming text out) at hundreds of millions of users.
- [MS04-199] Design a text-to-image generation service (Midjourney-like).
- [MS04-200] Design a music generation service (Suno-like).
- [MS04-201] Design a video generation service (Sora-like).
- [MS04-202] Design an on-device AI assistant.
- [MS04-203] Design a hybrid architecture in which some LLM requests run on-device, some on a first-party server model and some on a third-party model. How does the router decide?
- [MS04-204] How do you keep the model router itself cheap enough to run on every request?
- [MS04-205] How do you detect that the on-device model is silently producing worse answers than the server model would have?
- [MS04-206] Design a hybrid browser architecture combining on-device privacy with cloud AI assistance.

## Serving stack, LLM gateway and inference platforms
- [MS04-207] How would you design a production-grade LLM gateway, including provider routing, failover, caching, budgets and rate limits?
- [MS04-208] How would you design an LLM API gateway with multi-model routing and A/B testing?
- [MS04-209] Design an internal LLM gateway for about 40 product teams. What does "platform as product" mean concretely here?
- [MS04-210] A team demands a model that is not in your LLM gateway's catalog, today. What is the path?
- [MS04-211] An internal LLM gateway becomes a single point of failure. What is the availability story?
- [MS04-212] Your platform must support multiple LLM providers, including restricted environments where only some models are available. How do you architect model selection?
- [MS04-213] Design LLM inference at scale.
- [MS04-214] Design an LLM inference platform (vLLM-as-a-service).
- [MS04-215] Design the serving stack for a Claude-scale LLM API. Maximise GPU utilisation without wrecking p99 latency.
- [MS04-216] Design the serving stack for a ChatGPT-scale consumer assistant: hundreds of millions of weekly users, streaming chat, multiple model tiers.
- [MS04-217] Design a multi-tenant inference platform that serves many foundation models to thousands of customers.
- [MS04-218] How do you handle a 10x traffic spike on one model in a multi-tenant inference platform?
- [MS04-219] In a multi-tenant inference platform, where does prompt caching fit, and what is the leak risk across tenants?
- [MS04-220] In an LLM serving stack, how do you handle one tenant sending 200k-token contexts?
- [MS04-221] Design a serverless inference layer where any of thousands of hosted models can receive a request at any moment.
- [MS04-222] Design a serverless inference platform serving 100+ open models on a shared GPU fleet.
- [MS04-223] In a serverless inference platform, a new 400B MoE model launches and traffic grows 100x in an hour. Walk through what happens.
- [MS04-224] How do you run engine upgrades (a new vLLM or kernel version) across a GPU inference fleet without breaking SLOs?
- [MS04-225] A team prototyped on Ollama and wants to ship it as a shared API. What changes and why?
- [MS04-226] How would you autoscale a GPU-backed LLM service given slow model load times, and what do you do about cold starts?
- [MS04-227] What metrics and SLOs would you define for an LLM serving platform, and how do time-to-first-token and inter-token latency drive scheduling choices?

## Clinical documentation and healthcare AI
- [MS04-228] Design a medical diagnosis assistant using AI.
- [MS04-229] How would you protect patient data (PHI) and meet compliance requirements in an ambient clinical documentation system?
- [MS04-230] In a clinical note generation system, how would you detect a medication change that contradicts the patient's chart?
- [MS04-231] A generated clinical note contains a medication the patient never mentioned. Treating that as a safety incident, how do you detect it before a clinician sees it?
- [MS04-232] Your hallucination verifier itself has a false-negative rate. How do you set its operating point?
- [MS04-233] How do you ensure a clinical documentation AI does not miss critical information, and how would you catch omissions that no entailment check will surface?
- [MS04-234] Clinicians will not sign what they cannot verify. How would you build span-level provenance from every line of a generated note back to the conversation?
- [MS04-235] A sentence in a generated note summarises three separate moments in the visit. How do you present its provenance?
- [MS04-236] Edit rate is the obvious measure of clinician trust in generated notes. What does it hide, and what would you instrument instead?
- [MS04-237] How would you automatically distinguish a style edit from a correctness edit?
- [MS04-238] A health system reports high satisfaction with generated notes but rising post-signature amendments. What is your hypothesis?
- [MS04-239] Turn a clinical conversation into billable diagnosis codes. What is the accuracy bar, and how do you build to it?
- [MS04-240] How would you monitor for systematic over-coding drift across a health system?
- [MS04-241] What do you do when the conversation supports a condition but the patient chart contradicts it?
- [MS04-242] In an ambient note-generation system where the note should be ready before the clinician leaves, what breaks first when a specialty's visits run 90 minutes instead of 15?
- [MS04-243] Would you stream a generated note to the clinician section by section, and what does that cost you in coherence?
- [MS04-244] Walk me through writing a finished note back into an EHR such as Epic. What goes wrong?
- [MS04-245] Design a service that turns a clinical conversation into draft orders (labs, imaging, referrals, prescriptions) via tool calls against the EHR.
- [MS04-246] In a service that drafts clinical orders from a conversation, what does the system do when the clinician mentions a drug the patient is allergic to?
- [MS04-247] How would you evaluate a draft-order generation system end to end, given that a missed order and a spurious order have very different costs?
- [MS04-248] Nurses chart structured flowsheet rows across a twelve-hour shift, not one narrative note per visit. How would you adapt an ambient pipeline built for physician visits to draft flowsheet entries?
- [MS04-249] A nurse describes the patient in bed A while standing at bed B. How does an ambient charting system know which patient is meant?

## Finance, compliance and sovereign deployments
- [MS04-250] Design a hallucination-free banking chatbot.
- [MS04-251] How do you prevent hallucinated financial data in an LLM-based financial assistant?
- [MS04-252] Design a real-time fraud detection system with a hard p99 latency requirement of under 500 ms, using both ML rules and an LLM-RAG layer. Walk through the latency budget breakdown.
- [MS04-253] How do you handle regulations that require human judgment in a regulatory compliance AI system?
- [MS04-254] In a regulatory compliance RAG system, how do you handle the FDA updating a regulation mid-month?
- [MS04-255] How do you explain an AI system's reasoning to regulators during an audit?
- [MS04-256] A bank wants the whole stack (model, RAG, agents) deployed air-gapped on their own GPUs. What actually changes versus a SaaS deployment?
- [MS04-257] Design an on-prem deployment of an open-weight model for a European bank that cannot send data to any external API.
- [MS04-258] A bank has 4x A100 80GB in total. What model and quantization do you pick for an on-prem LLM deployment, and how many concurrent users does that support?
- [MS04-259] A regulated customer wants a coding agent built on an open-weight coding model small enough to run on a single GPU, entirely inside their network. How do you decide whether it is good enough, and what does the deployment look like?
- [MS04-260] A state agency wants to move a paper-and-call-centre welfare-scheme service onto a multilingual assistant, on-prem for data residency. How do you scope and ship it?
- [MS04-261] What audit logging, data retention and model-change controls would you put in place for an LLM system in a regulated industry?

## Additional questions
- [MS04-262] What happens to span-level provenance when a generated note is regenerated after an edit?
- [MS04-263] How would you onboard a site whose flowsheet template has hundreds of custom rows?
- [MS04-264] Design a platform that lets teams build, deploy and monitor many ML models company-wide.
- [MS04-265] Design a marketing automation platform that uses ML to choose audiences, content and timing.
- [MS04-266] Design a system that automates the playtesting of video games using learned agents.
