---
domain: genai
topic: prompt_engineering_context
title: Prompt engineering and context engineering
tags: [prompting, chain-of-thought, context-engineering]
count: 103
part: 1/2
---
# Prompt engineering and context engineering (part 1)

## Prompt basics and system prompts
- [GA01-001] What is prompt engineering, and why does it matter when building LLM applications?
- [GA01-002] What are the main elements of a prompt, and what problem does each of role, task, context and format solve?
- [GA01-003] What are the common prompt engineering techniques or types of prompting?
- [GA01-004] What strategies do you use to write a good prompt?
- [GA01-005] How would you tighten a vague prompt such as "summarize this document" so it produces consistent, useful results?
- [GA01-006] How do temperature and top-p interact with prompting, and when would you set temperature to zero?
- [GA01-007] What is role prompting, and when is it effective?
- [GA01-008] How do delimiters and structured sections in a prompt reduce ambiguity and injection risk?
- [GA01-009] What is the difference between prompt engineering and prompt tuning?
- [GA01-010] What methodology would you follow to design a prompt for a specific task?
- [GA01-011] What are common prompt anti-patterns, such as God prompts, vague instructions or missing output formats, that you would flag in review?
- [GA01-012] What is a system prompt, how does it differ from a user prompt, and what belongs in the system, user and assistant roles?
- [GA01-013] Why do system prompts carry more weight than user prompts, and what is the instruction hierarchy?
- [GA01-014] How do OpenAI's developer role and instruction-hierarchy training relate to the system, user and assistant roles?
- [GA01-015] What makes a good system prompt for a stable agent, and what sections would you include?
- [GA01-016] When would you deliberately fabricate an assistant turn in the prompt?
- [GA01-017] What happens to system-prompt adherence over a 50-turn conversation, and how do you counter the drift?
- [GA01-018] How do you handle multi-turn conversations with an LLM?
- [GA01-019] Why do negations sometimes work fine in prompts, and when is "never do X" appropriate?
- [GA01-020] How do you detect contradictions in a prompt systematically?
- [GA01-021] The model does not know what day it is. How do you handle dates, recency and the knowledge cutoff in your prompts?
- [GA01-022] A user insists on a fact that is newer than the model's training data and that the model believes is false. What should happen?
- [GA01-023] Your system prompt has grown into a 60-rule, 1,500-token mega-prompt and a small edit just caused a regression. How do you refactor it safely?

## In-context learning and few-shot prompting
- [GA01-024] What is the difference between zero-shot, one-shot and few-shot prompting, and when would you use each?
- [GA01-025] What is in-context learning, and how is few-shot prompting related to it?
- [GA01-026] When does in-context learning fail?
- [GA01-027] Why does in-context learning work at all when the model's weights do not change?
- [GA01-028] Why does in-context learning improve with model scale?
- [GA01-029] Why can exemplars with wrong labels still improve accuracy, and what does that imply for where you invest effort in choosing examples?
- [GA01-030] Some work claims in-context learning is implicit gradient descent. What is the claim, what is the evidence, and does it change what you do?
- [GA01-031] How would you test whether a task is merely being selected from pretraining versus genuinely learned in context?
- [GA01-032] Does the task-vector view of in-context learning suggest anything about compressing long system prompts?
- [GA01-033] How do you choose few-shot examples, and what are the known pitfalls of selection and ordering?
- [GA01-034] Why not put all 50 available examples in the prompt?
- [GA01-035] How many few-shot examples are typically enough, and does ordering matter?
- [GA01-036] What aspects should you keep in mind when using few-shot prompting?
- [GA01-037] How would you measure whether few-shot examples actually help versus just adding tokens?
- [GA01-038] Your few-shot prompt gives inconsistent results on similar inputs. How do you stabilise it?
- [GA01-039] What is label bias in in-context learning, and how does example ordering affect outputs?
- [GA01-040] Your 5-shot classifier over-predicts one class. What do you check first?
- [GA01-041] When is it deliberately correct to match the few-shot label distribution to a skewed real-world prior?
- [GA01-042] How would you test few-shot example ordering sensitivity cheaply?
- [GA01-043] The model copies surface features of your examples, such as their length or phrasing. How do you diagnose and fix it?
- [GA01-044] Compare dynamic and static few-shot selection, and when would you use each?
- [GA01-045] Design an example store for dynamic few-shot selection. What do you gain, and what does it cost?
- [GA01-046] How would you keep a mislabelled example from silently degrading a dynamic few-shot system in production?
- [GA01-047] When would bucketed static examples beat true per-request retrieval of few-shot examples?

## Chain-of-thought and self-consistency
- [GA01-048] What is chain-of-thought prompting, how does it differ from standard few-shot prompting, and when is it most useful?
- [GA01-049] Why does chain-of-thought improve performance on multi-step and math word problems?
- [GA01-050] For which tasks does chain-of-thought help, and for which is it unnecessary or harmful?
- [GA01-051] What are the limitations of chain-of-thought, such as dependence on model scale?
- [GA01-052] What does it mean for a chain of thought to be unfaithful, and why does it matter?
- [GA01-053] How would you decide empirically whether chain-of-thought is worth the latency for a given task?
- [GA01-054] How do you use chain-of-thought in a production system where latency is critical?
- [GA01-055] How does chain-of-thought relate to test-time compute scaling?
- [GA01-056] What is zero-shot CoT, and why did "Let's think step by step" become famous?
- [GA01-057] Why did RL-trained reasoning make the "Let's think step by step" trick largely obsolete, and where would you still use it?
- [GA01-058] How can you improve the reasoning ability of an LLM through prompt engineering?
- [GA01-059] Your chain-of-thought prompt is not improving accuracy on a reasoning task. What do you change?
- [GA01-060] A math word problem feature is 70% accurate with direct answers and you can afford a moderate cost increase. What gives the biggest reliable lift?
- [GA01-061] In a chain-of-thought prompt, should the reasoning come before the final answer, and how do you extract the answer reliably?
- [GA01-062] What is self-consistency prompting, how does it improve reasoning, and when is it worth the cost?
- [GA01-063] How would you apply the self-consistency idea to code generation, where outputs are long?
- [GA01-064] Design an adaptive self-consistency scheme that spends more samples only on hard inputs.
- [GA01-065] Why do errors tend to be uncorrelated across samples in self-consistency, and when would that assumption break?
- [GA01-066] Self-consistency with 5 samples is proposed for a feature serving 1M requests a day. How do you estimate the cost and decide?

## Advanced reasoning, ReAct and prompt chaining
- [GA01-067] What is ReAct (Reasoning + Acting) prompting, and how does it work?
- [GA01-068] What are ReAct prompting's limitations, and how do you mitigate them in practice?
- [GA01-069] A ReAct agent loops forever or invents tool observations. How do you debug it?
- [GA01-070] What is Tree of Thoughts, how does it differ from CoT and ReAct, and when is tree search not worth the cost?
- [GA01-071] When is Tree-of-Thought significantly better than simple chain-of-thought?
- [GA01-072] What is the main drawback of Tree-of-Thought in a consumer-facing app?
- [GA01-073] Do you still need explicit Tree-of-Thought prompting when the model is already a reasoning model?
- [GA01-074] What is Auto-CoT, and how does it reduce the need for hand-written examples?
- [GA01-075] What is Chain-of-Verification, and how does it reduce hallucination?
- [GA01-076] What is Self-Refine, and how does it differ from CoVe and Reflexion?
- [GA01-077] How does Chain of Density work, and when would you use it instead of ordinary summarization?
- [GA01-078] What is prompt chaining, how do you design a chain for a complex task, and how does it differ from simple CoT?
- [GA01-079] When would you decompose a task into multiple prompts instead of one? Explain least-to-most prompting and how it extends basic CoT.
- [GA01-080] How do you stop error cascades in a multi-stage prompt pipeline?
- [GA01-081] Given a fixed latency budget, how do you choose between one big reasoning-model call and a three-stage pipeline?
- [GA01-082] How would you evaluate the task decomposition step itself in a multi-prompt pipeline?
- [GA01-083] When would you pick a single prompt, a prompt chain or an agent loop for a task?
- [GA01-084] How do reasoning models change prompting practice? What transfers and what becomes obsolete?
- [GA01-085] Why can few-shot CoT examples hurt a reasoning model?
- [GA01-086] How do you debug a wrong answer when you cannot see the raw chain of thought?
- [GA01-087] How do reasoning effort and thinking controls differ across providers, and how do you choose an effort level?

## Structured output and output control
- [GA01-088] How do you structure prompts to get consistent structured output such as JSON or XML?
- [GA01-089] Your LLM keeps ignoring instructions about the output format. How do you make it follow a structured format?
- [GA01-090] When would you ask for JSON, XML tags or markdown as the output format?
- [GA01-091] How do structured outputs differ from JSON mode and from function calling?
- [GA01-092] Why is JSON mode more reliable than just asking for JSON in the prompt?
- [GA01-093] How does constrained decoding enforce a schema, and what are its tradeoffs compared with prompt-only formatting?
- [GA01-094] Why can a strict output schema hurt accuracy, and how do you fix it?
- [GA01-095] Why might you put a reasoning field before the answer field in an output schema?
- [GA01-096] What is the risk of requesting too many structured fields in one call, and how does multi-stage extraction help?
- [GA01-097] How do you handle validation failures from structured output, including retry with correction?
- [GA01-098] An extraction pipeline forced a tool call to get JSON, and after a model upgrade every request errors. What changed and how do you fix it?
- [GA01-099] How do the OpenAI, Anthropic and Google structured output mechanisms differ, and how do you choose?
- [GA01-100] The model wraps its JSON in markdown fences or adds chatty prose. How do you get parseable output reliably?
- [GA01-101] How do you design a schema so the model returns null for missing fields instead of inventing values?
- [GA01-102] Your LLM generates responses that are too verbose. How do you control response length reliably, and why does "exactly 100 words" rarely work?
- [GA01-103] How would you shorten model answers without losing a caveat that legal requires?
