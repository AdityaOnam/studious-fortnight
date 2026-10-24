---
domain: genai
topic: safety_guardrails_security_jailbreaks
title: Safety, guardrails, security and jailbreaks
tags: [safety, guardrails, prompt-injection, responsible-ai]
count: 73
part: 3/4
---
# Safety, guardrails, security and jailbreaks (part 3)

## Guardrail design
- [GA05-213] What are guardrails for LLMs, and how do you implement input and output safety protection in a production system?
- [GA05-214] What is the difference between input guardrails (injection, PII, off-topic) and output guardrails (groundedness, toxicity, schema), and why do you need both?
- [GA05-215] What are the layers of a guardrail architecture, and where does each check run?
- [GA05-216] How do you select and deploy guardrail models, and what use cases suit Llama Guard, Prompt Guard and similar classifiers?
- [GA05-217] How do NeMo Guardrails and Guardrails AI compare?
- [GA05-218] Design a guardrail system for a customer-service chatbot or consumer-facing assistant. Input filters, output filters, or both?
- [GA05-219] Design the guardrail layer for a customer-facing chat product. What goes in, and what does it cost you in latency and false positives?
- [GA05-220] How do you keep input classifiers from adding 500 ms of latency, and keep an output guardrail from destroying streaming latency?
- [GA05-221] How do you guardrail a streaming response without killing the user experience?
- [GA05-222] Where would you spend a strict 150 ms overhead budget: a better input classifier or stricter output handling?
- [GA05-223] How do you set a guardrail classifier threshold, and what business trade-off does it encode? What false-positive rate would you accept on an off-topic classifier?
- [GA05-224] What is your plan when the guardrail model itself becomes a target and attackers probe its blind spots?
- [GA05-225] Design a defense-in-depth strategy for a customer-facing agent that reads user data and can take actions.
- [GA05-226] If you could implement only two layers of a defense-in-depth design for such an agent, which would you choose and why?
- [GA05-227] Where does a defense-in-depth design for an LLM agent still fail, and is that residual risk acceptable?
- [GA05-228] What risks arise when hallucinated facts reach a user-facing product, and what guardrails would you add?
- [GA05-229] Where would you still choose a hard rule over model judgment in your own product, and why?
- [GA05-230] What are the cost and latency trade-offs of an LLM-as-judge guardrail versus a small fine-tuned classifier?

## Content moderation and sensitive domains
- [GA05-231] How do you implement content filtering and safety filters for AI-generated content?
- [GA05-232] How do you handle multimodal content moderation?
- [GA05-233] Your content moderation flags normal cultural expressions as offensive in other markets. How do you adapt cross-culturally?
- [GA05-234] How do you handle misuse and abuse of AI systems in production?
- [GA05-235] How do you distinguish a safety issue from a quality issue in an AI feature?
- [GA05-236] Your healthcare or pharmacy assistant is asked for diagnoses or drug-interaction advice it should not give. How do you add safety guardrails?
- [GA05-237] Your AI mental-health chatbot gave harmful advice to a user in crisis. How do you mitigate harm and prevent a repeat?
- [GA05-238] How do you prevent a welfare-scheme assistant from confidently stating an eligibility conclusion it should not?
- [GA05-239] How do you decide that a category (for example, breaking news) should not be summarized at all?
- [GA05-240] Design the safety system for open-ended character chat, including how to handle user-authored character definitions that cache across users.
- [GA05-241] How do you approach GenAI safety in consumer products?
- [GA05-242] When is intervening during decoding better than filtering the finished reply, and how do you keep a safety classifier head calibrated as the base model is post-trained?
- [GA05-243] Design age assurance for a platform where the under-18 experience is fundamentally different.
- [GA05-244] How do you evaluate an NSFW classifier before launch, and what base-rate math matters?
- [GA05-245] When would you decide a language is too low-resource to serve responsibly and route to human agents instead?

## Refusals and safety evaluation
- [GA05-246] Your model refuses perfectly legitimate requests. How do you diagnose and fix over-refusal, and manage the helpfulness-versus-safety tension?
- [GA05-247] How would you build an eval that catches over-refusal, including a benign-but-scary set for a medical product?
- [GA05-248] Why can't you optimize the refusal rate in isolation, and why must a safety benchmark be paired with an over-refusal benchmark?
- [GA05-249] Where would you set the refusal operating point for a security-research assistant versus a mental-health chatbot?
- [GA05-250] When is over-refusal a signal that you picked the wrong model rather than the wrong prompt?
- [GA05-251] What safety evals and benchmarks should you know, and what are their limitations?
- [GA05-252] How do jailbreak benchmarks like HarmBench and JailbreakBench work, and how is attack success rate computed?
- [GA05-253] Why did StrongREJECT need to exist given that HarmBench already did?
- [GA05-254] How do you turn scattered jailbreak samples into a recurring automated red-team harness?
- [GA05-255] How do you build a red-team set without leaking it into training or overfitting to it?
- [GA05-256] How do you calibrate an LLM judge for safety evaluations?
- [GA05-257] How do you build an eval for harms specific to your product?
- [GA05-258] How would you evaluate whether a model is safe to deploy, and what does "aligned" mean operationally?
- [GA05-259] What do you see as the most pressing unsolved problem in AI alignment?
- [GA05-260] What is mechanistic interpretability, and why do labs invest in it?
- [GA05-261] How would you balance performance optimization with model interpretability?
- [GA05-262] A team fine-tuned an aligned model on a few thousand benign support transcripts and its refusals got weaker. Why, and how do you guard against it?
- [GA05-263] Which slice of a safety eval would you expect to move first after a benign fine-tune, and why?
- [GA05-264] How would you design a fine-tuning API that lets customers tune freely without shipping models that comply with clearly harmful requests?
- [GA05-265] Why does narrow training on insecure code generalize to unrelated misbehavior, and how would you design probes that would catch it?

## Responsible AI, regulation and governance
- [GA05-266] What is responsible AI, and what frameworks exist for implementing it?
- [GA05-267] What are some challenges or ethical considerations associated with large language models?
- [GA05-268] What is model card documentation and why is it important, and how does a model card differ from a system card?
- [GA05-269] What is the NIST AI Risk Management Framework (AI RMF)?
- [GA05-270] What is the EU AI Act, and what does it require engineers to implement for an LLM product?
- [GA05-271] What is the difference between the EU AI Act and the NIST AI RMF, and when does each matter?
- [GA05-272] The EU AI Act may classify your system as high-risk. How do you prepare engineering-wise to comply without building a separate compliance stack?
- [GA05-273] If you are building a resume-screening tool for the EU, which AI Act risk tier are you in and what does that force you to build?
- [GA05-274] How do you plan engineering work for EU AI Act high-risk obligations when application dates and scope are in flux?
- [GA05-275] A regulation requires transparency labeling of AI-generated content with large fines, and a similar state law takes effect the same day. You ship text and images in both markets. What do you build?
- [GA05-276] How do you handle copyright and intellectual property concerns with AI-generated content, including verbatim reproduction and disclosure?
- [GA05-277] How do you build trust with users in AI-powered applications?
- [GA05-278] How would you prepare an LLM feature for a compliance or security audit?
- [GA05-279] What is the gap between "we have a policy" and "we have evidence" for an AI system, and how do you close it?
- [GA05-280] How do you keep model and system cards from going stale when the model or prompt changes weekly?
- [GA05-281] What goes into the security review packet you would prepare for a customer's CISO for an LLM deployment?
- [GA05-282] A CISO asks about prompt injection specifically. Give the two-minute version, and say what in your own application layer you would audit first.
- [GA05-283] You write most integration code with a coding agent while embedded at a customer, and their security lead asks what that agent can see and do. How do you answer?
- [GA05-284] An on-call team wants a coding agent to read production logs while debugging incidents. How do you grant that access?
- [GA05-285] A customer wants agent changes auto-shipped with no review. What, if anything, do you allow?
