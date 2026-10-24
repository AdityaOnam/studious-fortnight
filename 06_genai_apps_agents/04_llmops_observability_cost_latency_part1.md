---
domain: genai
topic: llmops_observability_cost_latency
title: LLMOps, observability, cost and latency
tags: [llmops, observability, cost, latency]
count: 97
part: 1/4
---
# LLMOps, observability, cost and latency (part 1)

## LLMOps fundamentals and production readiness
- [GA04-001] What is LLMOps, and how does it differ from traditional MLOps?
- [GA04-002] What must you operate after an LLM application goes live that classical MLOps did not cover, and what in LLMOps is just rebranding?
- [GA04-003] Which tool in a classical MLOps stack has no counterpart in an LLMOps stack, and why?
- [GA04-004] How does shipping an LLM feature differ from shipping a classical ML model in terms of what you version, test, and monitor?
- [GA04-005] What problems must be solved to take a model API integration from prototype to production deployment?
- [GA04-006] Your agent passes every staging test but misbehaves in production. What is the most likely cause, and how do you fix it?
- [GA04-007] How do you decide when an AI prototype is ready for production, and how do you answer "is your agent production-ready"?
- [GA04-008] How does the production-readiness bar differ between an internal AI tool and a customer-facing feature?
- [GA04-009] You must take a working GenAI agent prototype to production for an enterprise customer. What is your checklist between demo and launch?
- [GA04-010] The customer wants to launch in three weeks. Which checklist items do you cut, and which never get cut?
- [GA04-011] How do you decide that the quality bar for launching a GenAI agent is met, and who signs off?
- [GA04-012] How would you decide that an LLM-powered assistant is ready to launch to millions of customers?
- [GA04-013] For a customer-facing airline agent, what is your launch gate: which metric at what threshold?
- [GA04-014] Walk me through taking an AI feature from idea to production in two weeks. What does v1 actually look like?
- [GA04-015] When taking an AI feature to production in two weeks, what would make you cut streaming from v1?
- [GA04-016] What reliability patterns would you use for a production LLM system?
- [GA04-017] What is the biggest anti-pattern you see in LLM applications?
- [GA04-018] Employees in a 20,000-person company build their own agents in a no-code builder. Design the governance layer: pre-launch checks, run-time enforcement, and how you decide an agent is worth keeping.
- [GA04-019] A popular employee-built agent's owner leaves the company. What happens to the agent?

## Tracing and observability design
- [GA04-020] What is LLM observability?
- [GA04-021] What should you trace in an LLM application, and what makes a complete trace?
- [GA04-022] How is LLM observability different from conventional service observability, and what do you log for an LLM endpoint that you would not for a normal API?
- [GA04-023] How do you implement observability for an LLM application: traces, spans, costs, and user feedback?
- [GA04-024] Your AI pipeline gives you zero visibility into which step is failing. How do you add observability to a chain of prompts and tool calls?
- [GA04-025] Design the observability stack for a production LLM application. What does a good trace look like?
- [GA04-026] How does agent observability differ from general LLM monitoring, and what does good observability look like for an agent system?
- [GA04-027] What are the differences between metrics, logs, traces, evaluation, and audit?
- [GA04-028] How do you distinguish a trace, span, session, run, and attempt?
- [GA04-029] How should you split a single agent request into spans, and how do you preserve the trace across threads and services?
- [GA04-030] What are OpenTelemetry's GenAI semantic conventions, and has OpenTelemetry standardized agent spans?
- [GA04-031] How do you design a GenAI observability system for LLMs, and how do you integrate OpenTelemetry for traces and spans?
- [GA04-032] Where do you put an OpenTelemetry collector in a multi-agent mesh, and what spans do you emit?
- [GA04-033] What would you do when a semantic convention you depend on changes names in a new release?
- [GA04-034] How do you trace streaming responses and attribute time to first token versus generation time?
- [GA04-035] What trace sampling policy keeps costs sane at 10M requests/day without losing the failures?
- [GA04-036] How would you attach an eval score to a span after the fact?
- [GA04-037] What is the relationship between tracing and evaluation?
- [GA04-038] What is the difference between observability and evals for LLM applications, and which would you build first for a brand new feature?
- [GA04-039] If your LLM observability bill were cut in half, what would you stop capturing?
- [GA04-040] Why is trace attribution critical for senior engineers working on LLM applications?
- [GA04-041] How do you justify the cost of an observability platform such as LangSmith?
- [GA04-042] How do you choose between observability and eval platforms such as Langfuse, Phoenix, LangSmith, Opik, and Braintrust?
- [GA04-043] How would you structure agent logs so they are searchable and analyzable?

## Debugging and replay from traces
- [GA04-044] How can you use traces to reconstruct an agent's execution and debug a failing run step by step?
- [GA04-045] How can you use traces to locate common AI bad cases?
- [GA04-046] How do you find root causes from an agent's traces, and what are best practices for root cause analysis?
- [GA04-047] From a wrong answer, how do you trace back to the responsible model, knowledge source, skill, tool, or agent node?
- [GA04-048] How should you conduct a post-mortem of bad cases in an agent project?
- [GA04-049] Your assistant's answer quality regressed and nobody noticed for three weeks. How would you structure the postmortem document?
- [GA04-050] How would you tell context rot apart from a retrieval failure using a trace?
- [GA04-051] A user reports one bad answer from a RAG chatbot. Which trace artifacts do you need to decide whether retrieval, the prompt, or generation caused it?
- [GA04-052] What do you do when an LLM failure only reproduces in 1 of 50 requests?
- [GA04-053] How do you debug non-deterministic bugs in LLM systems?
- [GA04-054] A bug appears in production but never replays locally. What could be different?
- [GA04-055] A customer says the agent did something wrong three days ago and you have the trace. Can you reproduce it, and how do you build a system where the answer is yes?
- [GA04-056] How do you replay an agent run that involved a human approval and a 20-minute pause?
- [GA04-057] Why can an agent harness replay not simply re-call real APIs, and how does replay differ from checkpointing?
- [GA04-058] What would you log per tool call, or per step of a 40-step computer-use trajectory, to debug a failed agent run days later?
- [GA04-059] What telemetry tells you that the agent harness, not the model, is the bottleneck?
- [GA04-060] Storing full payloads for every agent run is expensive at scale. What is your retention policy?
- [GA04-061] How would you instrument an LLM pipeline so that triaging a report of a missed clause takes minutes instead of a day?
- [GA04-062] How do you detect abnormal agent behavior such as loops or runaway tool calls?

## Logging, privacy and audit
- [GA04-063] What should you log for every LLM call in production, and what are the pitfalls?
- [GA04-064] Is it acceptable to store full prompts and tool results in traces?
- [GA04-065] What would you redact from agent traces without destroying debuggability?
- [GA04-066] How do you keep prompt and completion payloads out of logs while still being able to debug?
- [GA04-067] How would you implement "delete this user's data" when their text appears inside other logged prompts?
- [GA04-068] What retention periods and access controls would you set for LLM trace data that contains user PII?
- [GA04-069] What would you log differently for a voice agent?
- [GA04-070] How would you measure end-to-end action accuracy across third-party apps without logging what people asked for?
- [GA04-071] How do you detect quality regressions of an LLM feature after launch without reading user content?
- [GA04-072] A customer running an air-gapped deployment reports a quality regression after an update and cannot share any prompts. How do you debug?
- [GA04-073] How do you implement audit trails and logging for AI decisions?
- [GA04-074] An auditor asks why your AI rejected a request six months ago and you have no logs. How do you build audit trails?
- [GA04-075] How do you prove to an auditor which model version handled a given request last March?
- [GA04-076] How do you anonymize replay data from online traces and move it into a regression set?

## Monitoring, alerting and SLOs
- [GA04-077] How do you monitor LLM applications in production, and what monitoring do you consider mandatory?
- [GA04-078] What metrics would you track for a production LLM system across operational, quality, and cost dimensions?
- [GA04-079] How does monitoring an LLM application differ from monitoring a classical ML model in production?
- [GA04-080] What are the key SLAs and metrics for production AI systems, such as latency, throughput, and availability?
- [GA04-081] Design the SLOs for a new LLM-powered feature. What do you promise, and how do you measure it?
- [GA04-082] Why should timeout-terminated requests be measured inside the latency distribution?
- [GA04-083] Your LLM provider's P99 is worse than the SLO you want to offer. What are your options?
- [GA04-084] How do you design SLAs and alerting rules for an agent, and what are the key thresholds?
- [GA04-085] Define SLOs for a customer support agent when every span returns 200 and latency is fine. What do you actually alert on?
- [GA04-086] How do you set an error budget for something you only measure on a 2% sample?
- [GA04-087] What is on your dashboard for an LLM serving platform, and what do you alert on?
- [GA04-088] Which three alerts page a human at 3 a.m. for an LLM platform or agent fleet, and which wait until morning?
- [GA04-089] What would you add to LLM serving monitoring for a multi-tenant platform?
- [GA04-090] How do you monitor and profile LLM inference in production, including TTFT, inter-token latency, and GPU utilization?
- [GA04-091] Which single online metric would you alarm on first for a newly launched LLM assistant?
- [GA04-092] What would make you page on an answer-quality regression rather than catch it in a weekly review?
- [GA04-093] How would you page on a regression that affects only 2% of an LLM feature's traffic?
- [GA04-094] How do you reduce alert fatigue for a probabilistic LLM system where some failure rate is always nonzero?
- [GA04-095] After a routine dependency upgrade your LLM dashboards go quiet, with fewer spans and lower token counts, while traffic and the provider bill are unchanged. What happened, and how do you prevent it?
- [GA04-096] Design end-to-end observability and containment for a fleet of production agents.
- [GA04-097] How do you build a behavioural baseline for an agent fleet when legitimate behaviour changes with every prompt edit?
