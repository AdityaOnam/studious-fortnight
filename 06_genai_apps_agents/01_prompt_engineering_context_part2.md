---
domain: genai
topic: prompt_engineering_context
title: Prompt engineering and context engineering
tags: [prompting, chain-of-thought, context-engineering]
count: 99
part: 2/2
---
# Prompt engineering and context engineering (part 2)

## Prompt templates, versioning and evaluation
- [GA01-104] What is a prompt template, and how do you design one for production use?
- [GA01-105] What can go wrong when you inject variables into a prompt template?
- [GA01-106] How would you unit test a prompt template?
- [GA01-107] What is composable prompt design, and how does it lower maintenance cost?
- [GA01-108] Why should prompts live in version control or a config store rather than be hard-coded in application code?
- [GA01-109] How do you version prompts in production and detect prompt drift?
- [GA01-110] How would you run A/B tests and offline regression tests for prompt changes?
- [GA01-111] How would you roll out a prompt change safely, using shadow traffic or a canary?
- [GA01-112] How do you evaluate and iterate on prompt quality?
- [GA01-113] Walk me through your process for systematically improving a prompt that is underperforming.
- [GA01-114] What is a golden dataset, and how do you build and maintain one?
- [GA01-115] What production metrics would you track for a prompt, beyond accuracy?
- [GA01-116] How do you evaluate prompt tooling such as LangSmith, Braintrust and Promptfoo?
- [GA01-117] A prompt must change for a model upgrade and behaves differently on both models. How do you handle the migration?
- [GA01-118] Rate limits and pricing now vary by model tier. How does that change your prompt design?

## Automatic prompt optimisation and DSPy
- [GA01-119] What are meta-prompts, and how can they be used to generate or improve prompts?
- [GA01-120] What is meta-prompting? How would you use a model to improve your prompts, and what are the pitfalls?
- [GA01-121] Why do model-rewritten prompts tend to get longer, and why is that bad?
- [GA01-122] How would you set up an automated prompt-search loop without overfitting the eval set?
- [GA01-123] When would you trust a meta-prompt improvement enough to ship it?
- [GA01-124] What goes wrong when you optimise a prompt against an LLM judge?
- [GA01-125] If a single phrase can unlock accuracy, how would you search for better phrases systematically?
- [GA01-126] What are APE and OPRO-style prompt optimisers, and how do they differ from manual iteration?
- [GA01-127] What is DSPy, how does it fundamentally differ from hand-written prompts, and when would you use it?
- [GA01-128] How does DSPy turn prompting into programming with signatures and optimizers?
- [GA01-129] How does DSPy address the fragility of prompt engineering?
- [GA01-130] What is a teleprompter or optimizer in DSPy, and what does metric-driven optimisation require?
- [GA01-131] Why is DSPy sometimes called anti-prompt engineering, and why is there a trend toward programming rather than prompting?
- [GA01-132] What is the biggest drawback of using DSPy in production?
- [GA01-133] When would you use GEPA instead of MIPROv2 for prompt optimisation?
- [GA01-134] How does bootstrapped-demo selection differ from retrieval-based dynamic few-shot?
- [GA01-135] How many labelled examples do you need before running a prompt optimiser, and how do you guard against overfitting?
- [GA01-136] When is prompt compression worth it, and how would you do it?
- [GA01-137] Why might token-level prompt compression hurt an extraction task more than a summarisation task?

## Prompt failures, hallucination and injection
- [GA01-138] What are the common failure modes in prompting, and how do you debug them?
- [GA01-139] How do you debug a prompt that behaves inconsistently across inputs?
- [GA01-140] How do you handle edge cases and adversarial inputs in prompt design?
- [GA01-141] Your LLM classification is too sensitive to prompt wording changes. How do you reduce that sensitivity?
- [GA01-142] The model follows instructions at the start of a long prompt but ignores those at the end. What could be happening and what do you try?
- [GA01-143] The model changes a correct answer as soon as the user pushes back. How do you reduce this sycophancy through prompting?
- [GA01-144] What is hallucination, and how can it be controlled using prompt engineering?
- [GA01-145] How do you prompt a model to honestly refuse when it does not know, instead of making things up?
- [GA01-146] What does a good RAG prompt template contain to ensure grounded, citable answers and graceful handling of insufficient context?
- [GA01-147] How do you handle multilingual prompting effectively, and how do you fix a system that works in English but fails in other languages?
- [GA01-148] Zero-shot cross-lingual transfer from English fails on other languages. How do you fix it?
- [GA01-149] Your Japanese users report an overly casual tone from the LLM. What do you change?
- [GA01-150] What is prompt injection, and how does it differ from prompt leakage?
- [GA01-151] What is the difference between direct and indirect prompt injection? Give an example of each.
- [GA01-152] How do you prevent system prompt leakage?
- [GA01-153] Why can't prompt wording alone fully prevent prompt injection, and what layered defences would you add?
- [GA01-154] Your agent reads untrusted web pages and emails. How do you design its prompts and permissions to limit injection damage?
- [GA01-155] How would you test whether a feature follows instructions embedded in user-supplied documents?
- [GA01-156] How does jailbreaking differ from prompt injection?

## Context engineering
- [GA01-157] What is context engineering, and how does it differ from prompt engineering?
- [GA01-158] Why is optimising only the prompt not enough in agent scenarios?
- [GA01-159] What goes into the context window of an LLM agent at each step, and who or what assembles it?
- [GA01-160] What tools are used in context engineering?
- [GA01-161] Why does context length matter when designing prompts?
- [GA01-162] What is the difference between the model context window and the application context window?
- [GA01-163] What is the "lost in the middle" problem, and how does context engineering handle it?
- [GA01-164] You have a 200k-token context with instructions and 50 documents. Where do you put what, and why?
- [GA01-165] Explain the write, select, compress and isolate framework for agent context management.
- [GA01-166] What are the core context engineering techniques: compaction, just-in-time loading, note-taking and sub-agent isolation?
- [GA01-167] How do you budget context across system prompt, tools, history and retrieved documents?
- [GA01-168] How do you manage token budgets as conversations grow, using compression that keeps key information?
- [GA01-169] When would you summarise, truncate or retrieve old conversation turns?
- [GA01-170] When is just-in-time retrieval better than preloading context, and what does it cost?
- [GA01-171] When is delegating to a sub-agent with an isolated context worth the extra cost and complexity?
- [GA01-172] How many tools can you expose to an agent before tool descriptions start hurting accuracy, and what do you do about it?
- [GA01-173] Your agent performs well on short tasks but degrades badly past 30 minutes of autonomous work. Diagnose and fix it using context engineering.
- [GA01-174] How do you evaluate that context compaction is not losing critical facts?
- [GA01-175] What is context pollution in agents, and how do you deal with it?
- [GA01-176] How would you detect context self-poisoning in agent traces automatically?
- [GA01-177] What makes a compaction prompt good at dropping poisoned context but keeping decisions?
- [GA01-178] Who owns context engineering when the prompt is assembled by five different subsystems?
- [GA01-179] A gateway falls back to a different model mid-conversation and quality drops. What context-related issues could be involved?

## Prompt caching
- [GA01-180] What is prompt caching, and why does it significantly reduce API cost and latency?
- [GA01-181] How does prompt caching work, and how should it change the way you structure prompts?
- [GA01-182] How do you order prompt content to maximise the cache hit rate?
- [GA01-183] What are the cache TTL, write premium and read discount, and how do they determine the break-even point?
- [GA01-184] A 20k-token prefix is reused at 100 requests per minute and cached reads cost about 10% of base price. Estimate the savings.
- [GA01-185] How can prompt caching optimise token cost, and how do you quantify the actual benefit for a given workload?
- [GA01-186] Explain provider-level prompt caching and how you would architect a system to maximise cache hit rate.
- [GA01-187] What are cache breakpoints, and how do you design them when tools or system prompts change mid-session?
- [GA01-188] How does prefix caching change how you design system prompts?
- [GA01-189] You need four few-shot examples in a high-traffic feature and want provider caching to help. Where do the examples go?
- [GA01-190] Dynamic few-shot retrieval versus static examples: how does prompt caching change the calculus?
- [GA01-191] How do you keep cache hits when a per-user personalised string must appear in the system prompt?
- [GA01-192] Why does inserting the current date at the top of a system prompt destroy caching, and where should it go instead?
- [GA01-193] Where do you place the conversation summary and the recent turns to keep prefix caching effective?
- [GA01-194] Where do you place retrieved RAG documents to get both good grounding and prompt-cache reuse?
- [GA01-195] How does document ordering interact with prompt caching when the document set is semi-stable?
- [GA01-196] How does context engineering interact with prompt caching, and where do they conflict?
- [GA01-197] What happens to your prompt cache when a reasoning model's thinking blocks enter the message history?
- [GA01-198] How does prompt caching change the cost math for bloated tool results?
- [GA01-199] An MCP server sends a list-changed notification mid-session. What happens to your prompt cache?
- [GA01-200] Your agent's prompt cache hit rate is 20% when you expected 90%. Walk me through the debugging.
- [GA01-201] How does prompt caching change the long-context versus retrieval cost analysis for agent loops?
- [GA01-202] How does provider prompt caching differ from semantic or response caching, and when would you use each?
