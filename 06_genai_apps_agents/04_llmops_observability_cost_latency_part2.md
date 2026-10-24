---
domain: genai
topic: llmops_observability_cost_latency
title: LLMOps, observability, cost and latency
tags: [llmops, observability, cost, latency]
count: 110
part: 2/4
---
# LLMOps, observability, cost and latency (part 2)

## Quality drift and silent degradation
- [GA04-098] How do you detect quality degradation in production?
- [GA04-099] How do you detect output quality decline and semantic drift in production agents?
- [GA04-100] What is the difference between data drift, concept drift, and model drift in an LLM application, and which of them can you actually observe?
- [GA04-101] How do you monitor a deployed LLM system for drift, and what kinds of drift matter?
- [GA04-102] How do you detect silent degradation in an agent when the success rate is stable but quality is dropping?
- [GA04-103] What is typically the earliest signal that a prompt change quietly regressed your agent?
- [GA04-104] Users report your support bot got noticeably worse this week though you shipped nothing. What is the most likely cause, and what safeguard do you put in place?
- [GA04-105] An agent's cost per task rose 40% and its tone changed overnight with no code or dependency change on your side. What happened, and how do you make it impossible to miss next time?
- [GA04-106] How would you detect that a provider quietly changed a model behind a pinned version string or an unchanged model ID?
- [GA04-107] How would you build a canary prompt set that runs on a schedule against a provider endpoint to detect behaviour changes?
- [GA04-108] Your production LLM app shows a 30% jump in hallucination rate after the provider silently updated the model. How do you detect and respond?
- [GA04-109] The model provider denies changing anything, but your eval diff says otherwise. What do you do?
- [GA04-110] Refusal rate doubled overnight with no deploy on your side. How do you investigate?
- [GA04-111] How do you catch an SDK or harness upgrade that silently changes the model's behavior?
- [GA04-112] A customer says the model got worse after you upgraded model versions in their deployment. How do you verify and respond?
- [GA04-113] How do you detect quality or precision regression after a model version upgrade you do not control?
- [GA04-114] After a foundation-model version upgrade, what monitoring would catch a regression in minutes rather than through next-day metrics?
- [GA04-115] Your LLM judge says quality is fine but retry rates spiked in the field. What do you look at?
- [GA04-116] In a hybrid on-device/cloud architecture, the on-device path succeeds but produces a bad answer. How would you even know?
- [GA04-117] Your feature runs on an OS-provided model and an OS update changed the model overnight. How do you detect it, and how do you design so it does not hurt next time?
- [GA04-118] A new model version rolls out and regressions are reported only in one language. How does your design catch that?

## Evals and regression testing in CI
- [GA04-119] How do you evaluate an AI application? How do golden sets, LLM-as-judge, online canary releases, and trace replay fit together?
- [GA04-120] What is the evaluation harness responsible for in an AI application, and how does a test harness differ from test scripts?
- [GA04-121] How do you wire evals into CI/CD so that prompt or model changes cannot silently regress quality?
- [GA04-122] You are writing the first tests for an LLM service's probabilistic output. Which kind of test do you ship first?
- [GA04-123] How would you write a regression test for an LLM feature that cannot rely on exact output matching?
- [GA04-124] How do you write regression tests for behaviour that is correct only 95% of the time?
- [GA04-125] How do you write assertions for an agent whose output legitimately differs on every run?
- [GA04-126] How do you test an LLM application with pytest and mocks, and how do you isolate tests from networks, time, and databases?
- [GA04-127] How do you make an LLM client testable and swappable using protocols and dependency injection?
- [GA04-128] How do you handle flaky tests, especially in LLM-dependent code?
- [GA04-129] How do you test an agent in CI on every pull request in under five minutes?
- [GA04-130] How would you design the testing strategy for an AI coding agent in CI?
- [GA04-131] Your recorded-response test cassettes drift from real model behaviour, and CI passes while production breaks. How do you detect that?
- [GA04-132] How would you test agent cancellation behaviour in CI?
- [GA04-133] Would you cache model outputs in CI, and what does that trade away?
- [GA04-134] Eval suites are slow, expensive, and noisy. How do you put one in CI without making everyone hate it, and how do you control its cost and runtime?
- [GA04-135] How do you keep judge-based CI costs sane as the team's PR volume grows?
- [GA04-136] Daily golden-set evals cost real money. How do you budget them?
- [GA04-137] A PR improves the target task but flips two unrelated eval cases to failing. What is your process?
- [GA04-138] A flaky LLM judge is blocking merges every few days. Walk me through the triage.
- [GA04-139] How do you handle eval velocity when 30 engineers push prompt changes daily?
- [GA04-140] How do you build a regression test set for an LLM feature that ships weekly?

## Online evaluation, feedback and review
- [GA04-141] How do you implement continuous evaluation for production AI systems?
- [GA04-142] How do you do automated agent evaluation in production, and what is the right way to use LLM-as-a-Judge?
- [GA04-143] Running your LLM judge on every production trace would cost more than the feature itself. How do you monitor quality online at scale?
- [GA04-144] How would you sample production traffic for quality scoring without a labelling budget that scales with traffic?
- [GA04-145] Design online evaluation: what do you log, what do you sample, and what do you A/B test?
- [GA04-146] Your prompt scores 95% offline but users complain, or offline evals are high while online performance dropped. What is broken?
- [GA04-147] Your eval scores keep improving but production complaints stay flat. How do you diagnose it?
- [GA04-148] How would you detect eval-production mismatch after the fact from logs?
- [GA04-149] How do you keep the eval set from going stale and aligned with drifting production traffic?
- [GA04-150] How would you tell a genuine improvement from overfitting to last week's failures?
- [GA04-151] How do you evaluate an AI application when the current time and web search results keep changing?
- [GA04-152] How do you design a feedback loop for continuous improvement of an LLM product?
- [GA04-153] What is a data flywheel, and how do you build one in an agent product?
- [GA04-154] Your product adds thumbs up/down on assistant messages. What do you build, and where does the data go?
- [GA04-155] Most users never press thumbs up or down. How do you design around sparse explicit feedback?
- [GA04-156] With sparse explicit feedback, which proxy metrics have real signal, and how do you validate a proxy?
- [GA04-157] Design a human review queue for a production LLM feature. What gets reviewed, and how much?
- [GA04-158] How would you keep two human reviewers of LLM outputs consistent over six months?
- [GA04-159] What would you cut first if the human review budget for an LLM feature halved?
- [GA04-160] For an AI agent that schedules hospital appointments, how do you decide when to stop reviewing 100% of outcomes?
- [GA04-161] You cannot hand-grade 400 customer-built agents. How do you keep a bad one from reaching a client?
- [GA04-162] How do you set up evals as a team culture without engineers gaming the metrics?
- [GA04-163] A team ships prompt changes on vibes. How do you move them toward eval maturity without halting shipping?
- [GA04-164] The founder says "our users are the eval". How do you respond?
- [GA04-165] Which single metric would you put on the team dashboard first for an LLM product, and why that one?
- [GA04-166] How would you build a minimal multilingual eval without native speakers on the team?

## Prompt versioning and change management
- [GA04-167] How do you version and manage prompts in production, including rollbacks and prompt drift?
- [GA04-168] If someone asks which prompt produced a bad output three weeks ago, can you answer?
- [GA04-169] Build a prompt-versioning system.
- [GA04-170] What belongs in a prompt registry entry besides the prompt text?
- [GA04-171] Should prompts live in code, in a database, or in a vendor console? What are the tradeoffs?
- [GA04-172] A teammate edited the prompt in the vendor console, and a week later quality dropped on unrelated inputs with nobody able to tell what changed. What practice would have prevented this?
- [GA04-173] Who should be allowed to change prompts in production on your team, and what gates those changes?
- [GA04-174] Design the regression gate that decides whether a prompt or model change ships. How do you version, evaluate, and gate a prompt change?
- [GA04-175] How would you gate promotion of a prompt version on evals without blocking every small copy change?
- [GA04-176] A one-line system-prompt change is in a PR. What runs before it merges, and what blocks it?
- [GA04-177] A system-prompt change improves the targeted behaviour but drops an unrelated eval tag by 4%. Do you ship it?
- [GA04-178] When a system-prompt change regresses unrelated evals, who owns fixing it, the prompt author or QA?
- [GA04-179] How do you test prompt changes before production?
- [GA04-180] How do you prove a prompt or skill change did not regress quality?
- [GA04-181] You want to change your agent's system prompt. How do you ship it without finding out from customers that you broke something?
- [GA04-182] How would you integrate prompt compilation into CI/CD?
- [GA04-183] How do you test a prompt change inside a multi-step agent where one turn's output feeds the next?
- [GA04-184] Your prompt change gained 3 points on the eval. How confident are you that it is real?
- [GA04-185] How would you construct a perturbation set for prompt evaluation without accidentally changing the task?

## A/B testing, canary and shadow deployments
- [GA04-186] How do you implement A/B testing for LLM systems?
- [GA04-187] How would you A/B test a prompt change safely in production?
- [GA04-188] How do you A/B test an agent, and what evaluation metrics do you use?
- [GA04-189] How would you A/B test an LLM-powered feature, and how does that differ from testing a ranking-model change? What implicit feedback signals would you use?
- [GA04-190] How do you size and time-box an A/B test for an LLM feature when outputs are noisy and the primary metric is low-rate?
- [GA04-191] What is interleaved evaluation, and when is it better than a standard A/B test for comparing two LLM variants?
- [GA04-192] What is the difference between guardrail metrics and quality metrics? Give examples of each.
- [GA04-193] How would you set the threshold for a guardrail metric like jailbreak rate: zero or nonzero?
- [GA04-194] A helpfulness A/B win ships, and escalation rate rises 15% while thumbs-up rate also rose. What happened?
- [GA04-195] In an A/B test of an LLM feature, thumbs-up rate is flat but edit distance on accepted outputs dropped 30%. Do you ship it?
- [GA04-196] A prompt variant wins the A/B test but loses offline. What do you do?
- [GA04-197] What would make you trust offline evals enough to skip an A/B test for a small prompt change?
- [GA04-198] You are swapping the model behind a live feature. Walk me through shadow, canary, and A/B, and when you use each.
- [GA04-199] How would you shadow-test an agent that writes to a production database?
- [GA04-200] Your canary looks fine at 2% traffic and quality tanks at 50%. What happened?
- [GA04-201] Your canary is green but user complaints are rising. What is your canary missing?
- [GA04-202] How do you safely roll out a new LLM version under heavy production traffic, using shadow traffic, interleaved evals, and rollback?
- [GA04-203] Your new agent version scores higher on every benchmark, but internal users say it got worse. Find the problem.
- [GA04-204] How would you ship the new agent version safely while you investigate why users say it got worse?
- [GA04-205] When a new agent version wins on benchmarks but user sentiment says it got worse, what would make you override sentiment and ship anyway?
- [GA04-206] A challenger model wins overall but loses on your two most important customer slices. What do you ship?
- [GA04-207] What would you measure to distinguish a real productivity gain from an AI coding agent from work simply moving from writing to reviewing?
