---
domain: genai
topic: safety_guardrails_security_jailbreaks
title: Safety, guardrails, security and jailbreaks
tags: [safety, guardrails, prompt-injection, responsible-ai]
count: 118
part: 2/4
---
# Safety, guardrails, security and jailbreaks (part 2)

## Agent permissions, sandboxing and containment
- [GA05-095] What are the security risks of agentic systems, and how do you mitigate them?
- [GA05-096] How do you implement guardrails for an agent that can take real-world actions, and what guardrails does a production agent loop need?
- [GA05-097] Your AI agent deleted a production database. How do you prevent irreversible actions by agents?
- [GA05-098] Why can't tool descriptions and prompts replace backend permission checks, and where does the security boundary actually live in an agent?
- [GA05-099] Why is function calling still unsafe even when a schema is defined?
- [GA05-100] Why does flexibility in an agent introduce security risk, and how do you constrain tool permissions with allowlists and capabilities?
- [GA05-101] Design a permission model for an agent that can call your internal APIs as tools.
- [GA05-102] How do you handle an agent action that is reversible in theory (such as a refund) but costly in practice?
- [GA05-103] LLMs are non-deterministic, but a refund over $200 must never be auto-approved. Where is the line between prompting and code?
- [GA05-104] How should an agent authenticate to downstream systems? Compare a shared service account with acting on behalf of the user.
- [GA05-105] How do you handle a legitimate background agent that runs when no user is present, so there is no user token to delegate?
- [GA05-106] Security asks how to revoke an agent's access for one user within five minutes. What is your answer?
- [GA05-107] How would you scope credentials so a prompt-injected coding agent cannot push to an unrelated repository?
- [GA05-108] What is continuous authorization for agents, and what are signed agent manifests?
- [GA05-109] What is sandboxing in AI agents, and when do you choose sandboxed versus unsandboxed execution?
- [GA05-110] Your agent can execute arbitrary Python code. How do you make that safe, for example with microVMs or containers?
- [GA05-111] You are reviewing a coding agent that executes model-generated code. What is your threat model and what controls do you apply?
- [GA05-112] Why is blocking network egress the highest-leverage single control for a code-executing agent?
- [GA05-113] Why must credentials never live inside a code-execution sandbox, even if the task seems to need them?
- [GA05-114] When a code-executing agent's stdout goes back to the model, what is the risk?
- [GA05-115] How would you let sandboxed agent code use pip install safely?
- [GA05-116] What syscall and network policy do you set for a test-execution sandbox used by a coding agent?
- [GA05-117] Does the sandboxing calculus change for an agent running on the user's own machine versus a hosted service?
- [GA05-118] What permissions would you give an agent working in an untrusted repository?
- [GA05-119] Engineers say the sandbox makes their coding agent too slow to be useful. What do you relax first, and what never?

## MCP, browser agents and tool ecosystem security
- [GA05-120] What are the security risks of connecting a third-party MCP server, and how do you mitigate them?
- [GA05-121] What security governance does a production-grade MCP server need?
- [GA05-122] What are the core risks in the OWASP MCP Top 10, and how do you defend against them?
- [GA05-123] What are the main MCP security challenges (registry supply chain, STDIO execution, instruction/input boundary failure, authentication), and how do you defend against each?
- [GA05-124] How is a poisoned tool description different from injecting text into a document?
- [GA05-125] How can MCP tool poisoning combine with server-side vulnerabilities into an attack chain, and how do you defend against it?
- [GA05-126] What is a rug pull in the context of MCP servers, and which control specifically defends against it?
- [GA05-127] How do you monitor an already-approved MCP server for behavior drift over time?
- [GA05-128] Why is a stdio MCP server more dangerous than a remote HTTP one?
- [GA05-129] Is MCP secure once OAuth is used? Does OAuth address description-based attacks such as tool poisoning?
- [GA05-130] Your agent connects to a dozen third-party MCP servers over OAuth. How do you stop one malicious server from stealing credentials meant for the others?
- [GA05-131] What breaks in the on-behalf-of-user authentication model when the agent calls a third-party MCP server that does its own OAuth?
- [GA05-132] How do you secure an application that calls untrusted MCP servers?
- [GA05-133] You need to let 50 engineers safely use about 30 internal and community MCP servers. What is the scalable architecture, including an enterprise gateway?
- [GA05-134] Would you accept a closed-source MCP server you cannot fully audit, and under what compensating controls?
- [GA05-135] How does MCP elicitation interact with prompt injection risk, and would you let a third-party server's UI trigger a write tool without fresh approval?
- [GA05-136] In a multi-tenant agent platform, a tenant's MCP server description contains an injection aimed at your orchestrator. Which isolation controls help?
- [GA05-137] How would you secure a browser agent that acts inside the user's logged-in browser?
- [GA05-138] The task needs a browser agent to read an email and then act on a different site. How do you keep that useful without rebuilding the cross-origin bridge?
- [GA05-139] What would you show the user at a browser agent's confirmation step so they can actually evaluate it rather than click through?
- [GA05-140] How would you design a browsing agent that has payment authority while resisting injected instructions hidden in trusted-looking data fields?
- [GA05-141] A self-propagating npm worm plants malicious editor and agent configurations. How does that change your policy on plugins and skills from public marketplaces?
- [GA05-142] Why do agent frameworks suffer remote code execution vulnerabilities, and how do you defend against them systematically?
- [GA05-143] What is slopsquatting, and how do you stop a coding agent from installing a package that does not exist?
- [GA05-144] How would you find out after the fact whether an agent-authored change pulled in a squatted package, and do the defenses carry over to container images and API endpoints?

## Poisoning, backdoors and model supply chain
- [GA05-145] What is data poisoning, and how can it affect AI models?
- [GA05-146] How can an attacker poison training data or plant a backdoor in a model, and how would you catch it?
- [GA05-147] Your LLM's training data was deliberately poisoned by an adversary. How do you respond?
- [GA05-148] How does poisoning a RAG index differ, operationally, from poisoning fine-tuning data?
- [GA05-149] One malicious participant is poisoning your federated learning model. How do you defend against it?
- [GA05-150] What is a model backdoor, and why can't you just inspect the weights to find it?
- [GA05-151] A pre-trained model from an open-source repo may contain a hidden backdoor. How do you detect it, and what would convince you an inherited open-weights model has none?
- [GA05-152] Explain model supply-chain risks: pickle versus safetensors, weights provenance, dependencies.
- [GA05-153] Why exactly is unpickling dangerous, and what does safetensors change?
- [GA05-154] What does trust_remote_code=True do, why is it a security boundary, and what attack surface remains even with safetensors weights?
- [GA05-155] A vendor publishes fine-tuned weights but not training data. Walk through your supply-chain trust process: what does model signing buy you, and what gaps remain?
- [GA05-156] How would you retrofit hash pinning and provenance checks into a pipeline that currently pulls "latest" from a public model hub?
- [GA05-157] What is your incident response if a model you are already serving is later found to be compromised upstream?
- [GA05-158] How would you design a model hub's scanning pipeline for the pickle files that still get uploaded?
- [GA05-159] What is memory poisoning in an agent, and why is it worse than a one-shot prompt injection?
- [GA05-160] How do you prevent memory poisoning when agents can write to their own long-term store, and when does memory become an injection surface?
- [GA05-161] How would you detect memory poisoning in production, or audit an existing memory store to see if it was already poisoned?
- [GA05-162] What are adversarial attacks on AI systems, and how do you defend against them?
- [GA05-163] What is adversarial testing for AI systems?
- [GA05-164] What security problems appear in a multi-agent system that do not exist with a single agent?
- [GA05-165] How would you implement taint propagation across agent messages in a framework that has no concept of it?
- [GA05-166] Does a critic or judge agent that reads the same context provide any real safety benefit, or is it theatre?

## Red teaming and injection testing
- [GA05-167] What is red teaming, and how do you structure red teaming for an LLM application before launch?
- [GA05-168] How does red teaming an LLM product differ from a traditional penetration test?
- [GA05-169] Who owns red teaming in your organization, security or the AI product team, and why does that choice matter?
- [GA05-170] Design a red-teaming program for a model or product you are about to release: manual versus automated, pre-launch versus continuous, and how findings feed back.
- [GA05-171] Why isn't automated red teaming enough on its own?
- [GA05-172] How would you red-team an LLM feature that has tool access?
- [GA05-173] How do you red team a multimodal model when text-only safety tests miss cross-modal attacks?
- [GA05-174] How would you red-team a multi-tenant, permission-aware RAG system before launch?
- [GA05-175] Design a red-team suite for image-borne prompt injection. If the agent must both read attachments and reply to email, what is the minimum viable containment?
- [GA05-176] Your team red-teamed and found 30 ways to break the assistant. How do you turn that into something durable?
- [GA05-177] How exactly does a red-team finding become a regression eval, and why is that step non-negotiable?
- [GA05-178] How do you keep a red-team suite from going stale as models improve?
- [GA05-179] Your red-team attack success rate has been 0% for six months. Is that good news or bad?
- [GA05-180] What triggers a re-test of an LLM product after launch?
- [GA05-181] How would you test a prompt's injection resistance systematically and continuously, rather than once?
- [GA05-182] What does a prompt-injection test suite look like when tool results are the attack channel?
- [GA05-183] How do you red-team an indirect injection path when the retrieved content comes from customer data you cannot read, or needs a specific hard-to-guess format to trigger?
- [GA05-184] How would a red team test for jailbreaks and for prompt injection separately?
- [GA05-185] What attack success rate is acceptable for shipping an LLM feature, and what metric would you report to a security review board?
- [GA05-186] How do you know your prompt-injection classifier is not itself being bypassed?
- [GA05-187] A security eval for prompt injection reports 0% pass@100 on a task where the agent should NOT comply with an injected instruction. What is the most likely explanation?
- [GA05-188] How would you detect an indirect prompt-injection attempt in production logs?
- [GA05-189] What is your policy when prompt-injection defenses conflict with task success?
- [GA05-190] How would you detect prompt-injection exposure in an agent definition without executing it?
- [GA05-191] How do you detect anomalous or abusive usage of an LLM application in production?

## Monitoring, containment and incident response
- [GA05-192] What concrete security monitoring exists for agents in production?
- [GA05-193] What audit logging is required for accountable agent actions?
- [GA05-194] Why should you not use the model's reasoning as your audit trail?
- [GA05-195] Your safety team wants to monitor a coding agent by reading its chain of thought. What do you tell them?
- [GA05-196] How do you know an agent action monitor works if the model behaves differently when it suspects it is being watched?
- [GA05-197] Your evaluation agents run long cyber tasks. A monitor alarmed 12 minutes in, but the run was stopped 2.5 hours later. Redesign the containment.
- [GA05-198] Your team's agent, or an eval run, reached a system it was never supposed to touch. What do you change, and what do you stop?
- [GA05-199] Your agent did something harmful to a third party's system. Walk through your reporting obligations and how you would design the incident process.
- [GA05-200] A coding agent passed tests and a human approved the diff, yet internal data ended up public. How could that happen?
- [GA05-201] How would you detect that a developer's local coding agent has been hijacked?
- [GA05-202] Your production assistant has started quoting wrong prices to customers. Is it an attack or a bug, and how do you find out?
- [GA05-203] Where else in an LLM product would you apply the rule "never let the model generate the number"?
- [GA05-204] If the wrong prices turn out to be injection via a supplier catalog feed, what changes structurally?
- [GA05-205] How would you design an AI incident response plan?
- [GA05-206] Your AI system caused incorrect critical decisions. How do you run a blameless post-mortem?
- [GA05-207] How do you handle approval laundering, over-reliance and operator fatigue in agent oversight?
- [GA05-208] Radiologists agree with AI 98% of the time, even when it is wrong. How do you prevent human over-reliance on AI?
- [GA05-209] How do you make an agent's telemetry safe so it cannot silently upload sensitive data?
- [GA05-210] Why do agents behave differently under pressure, and how do you evaluate behavioral dispositions?
- [GA05-211] How should an agent gateway split identity, permission, isolation and audit responsibilities?
- [GA05-212] Your team wants to keep full prompt and response traces of every production agent run forever for debugging. What is the senior concern?
