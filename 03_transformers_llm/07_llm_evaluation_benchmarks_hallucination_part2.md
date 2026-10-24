---
domain: llm
topic: llm_evaluation_benchmarks_hallucination
title: LLM evaluation, benchmarks and hallucination
tags: [llm-eval, benchmarks, hallucination, llm-as-judge]
count: 151
part: 2/2
---
# LLM evaluation, benchmarks and hallucination (part 2)

## Building and maintaining eval sets
- [LLM07-137] What is the smallest useful eval suite you would build in week one, and what is the minimum viable eval before launching an LLM feature?
- [LLM07-138] How do you build a custom eval set for a new LLM feature step by step, and how many examples do you need and where do they come from?
- [LLM07-139] What is the role of a golden dataset in AI evaluation, and how do you build and maintain one?
- [LLM07-140] How big should a golden evaluation set be, who should own it, and how do you grow it?
- [LLM07-141] Where does the eval signal come from: human annotation, user feedback, implicit signals or synthetic generation?
- [LLM07-142] What are the delay and noise of the evaluation signal in an LLM system (a click is not satisfaction; no complaint does not mean correct)?
- [LLM07-143] What failure classes should you evaluate for in an LLM application, such as wrong answer, missing citation, refusal, latency and cost?
- [LLM07-144] How do you split eval data into dev, test and held-out sets for an LLM application, and why does it matter?
- [LLM07-145] What makes a single eval case well specified, and what are the common ways individual cases go wrong?
- [LLM07-146] How do you decide an eval example is hard before you have seen failures?
- [LLM07-147] Who should write reference answers for an eval set in a domain where nobody on the team is an expert?
- [LLM07-148] How do you build an eval set when there is no labelled ground truth and the experts who could judge quality are expensive?
- [LLM07-149] When building an eval set with a rubric, how do you stop the rubric author's own style preferences from becoming the metric?
- [LLM07-150] What goes in the eval set versus a unit test?
- [LLM07-151] Why do you version an eval dataset, and what exactly belongs in the version?
- [LLM07-152] Your eval is 95% passing and stops discriminating between candidate prompts. What do you do?
- [LLM07-153] How would you handle an example everyone agrees is mislabelled but that has been in the frozen eval suite for a year?
- [LLM07-154] How do you keep a golden eval set from going stale and representative as the product evolves?
- [LLM07-155] How do you prevent and detect the team overfitting to the dev eval set as it iterates?
- [LLM07-156] Who triages the production-failure queue, and what is the admission bar for a new eval case?
- [LLM07-157] How would you use synthetic data to build or extend an eval set (say 50 real inputs to 5,000), and what are the failure modes and review process?
- [LLM07-158] How would you measure the diversity of an LLM-generated test set?
- [LLM07-159] When is synthetic test data outright inappropriate?
- [LLM07-160] How would you measure whether your synthetic eval set predicts production performance?
- [LLM07-161] What would make you throw an eval task out entirely?

## Deterministic graders and task-specific checks
- [LLM07-162] Exact-match assertions are useless for LLM output. What kinds of code-graded assertions can you use, and where do they break down?
- [LLM07-163] How would you evaluate an LLM feature that must return structured output such as JSON that follows a schema?
- [LLM07-164] Give a concrete criterion that looks judge-worthy but can be reduced to a code assertion.
- [LLM07-165] Your regex grader shows 95% pass but users complain. What is happening?
- [LLM07-166] When property-based assertions on an LLM response pass but the answer is still wrong, what catches that?
- [LLM07-167] How do you pick and maintain the similarity threshold when asserting on LLM responses with embedding similarity?
- [LLM07-168] How would you grade a summarisation task, where every summary is legitimately different, without an LLM judge?
- [LLM07-169] What is your eval for an LLM extraction feature?
- [LLM07-170] How do you keep the grader out of reach of the system being evaluated?

## Statistics, variance and pass@k
- [LLM07-171] How do you compare two models or prompts in a statistically rigorous way?
- [LLM07-172] Your new prompt scores 78% versus the old prompt's 74% on a 100-example eval. Is that real, and do you ship it?
- [LLM07-173] Your eval reports 82% pass on 100 examples. What does that number not tell you?
- [LLM07-174] What would make you distrust an 82% eval pass rate even with a tight confidence interval?
- [LLM07-175] How large does an eval set need to be before you trust a 3-point difference between two versions or a model swap?
- [LLM07-176] How would you compute a confidence interval for an eval pass rate, and when is a bootstrap preferable?
- [LLM07-177] You want to detect a 3-4 point improvement in pass rate. How many examples do you need, and how do you get that number down?
- [LLM07-178] Your minimum-detectable-effect calculation says you need 2,800 eval examples and you have 200. What do you actually do?
- [LLM07-179] How does per-case flip variance change your confidence-interval math when comparing two prompts?
- [LLM07-180] When comparing two LLM configurations on an eval set, when is a paired design not available to you?
- [LLM07-181] Evals are nondeterministic (temperature, sampling, flaky agents). How do you get trustworthy numbers and test a chatbot that answers differently every time?
- [LLM07-182] How does non-determinism of LLM outputs change your definition of a flaky test?
- [LLM07-183] An eval case passes 50% of the time across ten trials of the same configuration. Is it a good case or a broken one?
- [LLM07-184] How do you handle eval cases that flip on identical inputs during error analysis?
- [LLM07-185] Your CI budget allows one run per eval case or three runs on a third of the cases. Which do you choose and why?
- [LLM07-186] Define pass@k. Why is the naive way of computing it problematic, and what is the fix?
- [LLM07-187] What is the difference between pass@k and pass^k, and when does each matter?
- [LLM07-188] How many trials and tasks do you need before a pass^k difference is signal rather than noise?
- [LLM07-189] When is optimising pass@10 legitimate for a product?
- [LLM07-190] How does pass@k relate to best-of-n sampling with a verifier at inference time?

## Code and agent evaluation
- [LLM07-191] How would you build an execution-based eval for a code-generation feature?
- [LLM07-192] How do you evaluate code edits in a large existing repo versus writing functions from scratch?
- [LLM07-193] Your code-generation eval pass rate is 60%. How do you decompose that into actionable failure categories?
- [LLM07-194] For an AI code-completion model, acceptance rate went up 2% but retained characters went down. What happened?
- [LLM07-195] How do you evaluate a code-editing model before shipping it? Design the offline and online eval story.
- [LLM07-196] How do you evaluate agents with metrics such as tool-selection quality, step success and trajectory adherence?
- [LLM07-197] How do you evaluate end-to-end task success versus step-level correctness for an agent, and when do they diverge?
- [LLM07-198] How would you evaluate an agentic coding model on SWE-bench and tau-bench style benchmarks, and beyond a single benchmark number, without fooling yourself?

## Long-context and multi-turn evaluation
- [LLM07-199] Why do needle-in-a-haystack results overstate long-context ability, and how should you evaluate long-context recall?
- [LLM07-200] A vendor advertises 1M context with 100% needle-in-a-haystack. What has that actually proven?
- [LLM07-201] How would you design an eval for usable context length on your workload, including for a model whose main improvement is long context?
- [LLM07-202] How would you test whether a model uses information from the middle of a long context?
- [LLM07-203] How would you construct hard distractors automatically from a customer's corpus for a long-context evaluation?
- [LLM07-204] In a long-context evaluation, what does an unanswerable-question false-positive rate tell you that accuracy does not?
- [LLM07-205] How would you construct an eval that a needle-in-a-haystack-only model would fail, and what should a long-context agentic benchmark test?
- [LLM07-206] How would you build an eval that separates real long-context retrieval from a model that merely compresses well?
- [LLM07-207] How would you show a hybrid linear/full-attention or local-attention model has not lost long-range recall or persona consistency at turn 150?
- [LLM07-208] How would you detect that int8 training has degraded a specific behaviour, like staying in character, when aggregate evals show parity?
- [LLM07-209] How do you evaluate multi-turn conversation quality?
- [LLM07-210] How do you handle failure modes that only appear in multi-turn context during error analysis?
- [LLM07-211] Users complain that characters drift out of persona. How would you build a persona scorer that does not just reward verbosity?

## Domain and product evaluations
- [LLM07-212] How would you evaluate a meeting-summarisation feature before shipping it to a hundred million users?
- [LLM07-213] Two good clinicians write different notes for the same visit. How do you evaluate note quality at all?
- [LLM07-214] How would you evaluate a clinical note type for which you have no annotated data?
- [LLM07-215] How would you evaluate an Indic-language LLM properly, and why is running translated English benchmarks not enough?
- [LLM07-216] How do you evaluate answer quality for a real-time-search chatbot when ground truth changes hourly?
- [LLM07-217] How would you evaluate a customer-facing RAG chatbot end to end: retrieval quality, answer faithfulness and user outcomes?
- [LLM07-218] How would you build an eval that catches a model confidently answering about events after its knowledge cutoff?
- [LLM07-219] What is overrefusal, and how would you build an over-refusal eval that balances safety and helpfulness (for example for a security-tools customer)?
- [LLM07-220] How do you evaluate personalization and memory features without storing sensitive user data in eval sets?
- [LLM07-221] Your proxy metrics for notification summarisation look flat but journalists post screenshots of bad summaries. What went wrong in your eval design?
- [LLM07-222] How would you evaluate whether third-party data enrichment actually improves an LLM service's answers?
- [LLM07-223] Give a concrete task where the deployment metric is inherently discontinuous. What smooth proxy would you monitor?
- [LLM07-224] A customer wants an accuracy SLA for an LLM system in the contract. What do you agree to and how do you make it measurable?
- [LLM07-225] A customer has no labelled data and no eval culture. How do you establish "is it working?" for an LLM deployment?

## Error analysis and the benchmark-to-production gap
- [LLM07-226] What is error analysis in the context of evaluating LLM applications?
- [LLM07-227] When should you stop reviewing traces during error analysis?
- [LLM07-228] What is the difference between error analysis and automated evals, and when should you prioritize each?
- [LLM07-229] How do you move from ad hoc notes on traces to a failure taxonomy, using open and axial coding?
- [LLM07-230] You have 500 production transcripts flagged as failures. Walk me through your error-analysis process.
- [LLM07-231] In error analysis of flagged failures, what do you do with the "not actually a failure" cluster?
- [LLM07-232] What is the benchmark-to-production gap, and how do you bridge it?
- [LLM07-233] What are common evaluation pitfalls, such as small test sets, leakage, ignoring variance and evaluating a different system than you ship?
- [LLM07-234] Where does Goodhart's law bite in LLM evaluation? Give concrete examples and defences.
- [LLM07-235] Your new model scores higher on every benchmark, but users say it got worse. Why does this happen and how do you find the problem?
- [LLM07-236] Users say the new model "feels worse" but every eval slice improved, or the open model wins evals but the PM says it feels worse. Next move?
- [LLM07-237] Your eval suite is green and scores keep improving, but production complaints are flat or rising. Debug it and redesign the eval system.
- [LLM07-238] Your new prompt improves the aggregate pass rate by 3 points, but one customer segment drops 8. How do you catch this before shipping?
- [LLM07-239] How do you pick eval slices for failure modes you have not thought of yet?
- [LLM07-240] The regressed eval slice has only 12 examples in total. What do you do?
- [LLM07-241] Your eval suite is green but the complaints come from 3 users out of 50,000. What do you do?
- [LLM07-242] Your length penalty cut reasoning tokens sharply and the aggregate eval is flat, but complaints on hard queries rise. How do you find the regression?
- [LLM07-243] After reducing the cost of an LLM workload, how do you prove quality did not regress?
- [LLM07-244] How do you set up the eval after migrating from a proprietary API to an open model so that it stays useful?

## Eval system design and release gating
- [LLM07-245] How would you convince a team shipping on vibes to invest in evals?
- [LLM07-246] You do not have an eval team. How do you know your LLM feature actually works and keeps working?
- [LLM07-247] How do you set up an evaluation framework from scratch for a new LLM application, treating it like a test framework?
- [LLM07-248] Where should an LLM eval harness live: a pytest plugin, a standalone service or a vendor tool?
- [LLM07-249] What is the difference between offline and online evaluation for AI systems?
- [LLM07-250] How do you evaluate an LLM or RAG system in production?
- [LLM07-251] How do you build a regression test suite for an LLM application, and what tooling would you use to run it in CI?
- [LLM07-252] How do you evaluate the robustness of an LLM application across input variations?
- [LLM07-253] How would you combine offline evals, shadow traffic and canary releases to roll out a new model?
- [LLM07-254] How would you A/B test two models in production, and which metrics and guardrails would you track?
- [LLM07-255] Design an evaluation system for comparing two LLMs on open-ended tasks.
- [LLM07-256] Design an evaluation suite for a general-purpose chat model covering knowledge, reasoning, code, safety, instruction following and multilingual ability.
- [LLM07-257] Build the evaluation harness for a new frontier LLM release, and the system you would run before and after each model release. What does it need to do?
- [LLM07-258] How do you evaluate your eval suite itself? What makes one good or bad?
- [LLM07-259] An agent passes its own evals because the evals are weak. How would you detect a low-quality eval set automatically?
- [LLM07-260] When validating an eval suite by checking that it detects a deliberately degraded model, how do you build that degraded configuration without it being trivially detectable?
- [LLM07-261] Your eval suite catches 9 of 10 escaped defects but takes 40 minutes in CI. Is it worth it?
- [LLM07-262] How would you prevent an eval suite that is green while users see quality regress from recurring, without doubling eval cost?

## Reasoning models and chain-of-thought
- [LLM07-263] What are reasoning models, and how does test-time compute change the picture? When are they worth the cost versus a standard model?
- [LLM07-264] What is extended thinking, and how does a thinking token budget control how much a model thinks?
- [LLM07-265] Reasoning models expose a thinking budget or reasoning effort setting. How do you tune it, and what goes wrong?
- [LLM07-266] When is chain-of-thought overthinking harmful, and how do you control reasoning effort?
- [LLM07-267] How would you set a reasoning budget per request rather than globally?
- [LLM07-268] How does evaluating and observing a reasoning model differ from a standard instruction-tuned model?
- [LLM07-269] How would you evaluate a reasoning benchmark such as GSM8K or AIME, and what failure modes such as answer-format brittleness can distort scores?
- [LLM07-270] Your pass-rate curve is still climbing at the maximum reasoning budget. What does that tell you?
- [LLM07-271] How do you evaluate whether extra thinking budget actually buys accuracy rather than just inflating token spend?
- [LLM07-272] A hybrid reasoning model has a thinking mode and a direct mode. How do you build one model that does both, and what are the training and serving implications?
- [LLM07-273] How would you stop a hybrid reasoning model from over-thinking simple prompts?
- [LLM07-274] Latent (continuous-space) reasoning reportedly beats token-space chain-of-thought on math benchmarks. When would you deploy it in production?
- [LLM07-275] Why does chain-of-thought reasoning appear only in sufficiently large models, and what capability is it linked to?
- [LLM07-276] Do LLMs actually reason? What evidence supports or contradicts the claim, and how do you probe for it?
- [LLM07-277] How would you tell whether a model's math gain from chain-of-thought reflects reasoning rather than memorization, for example with perturbed problems?
- [LLM07-278] Self-consistency with 8 samples helps on maths but barely moves open-ended generation. Why?
- [LLM07-279] What is a reasoning model's chain of thought good for, and why is it not a reliable account of the model's actual computation?
- [LLM07-280] Are chain-of-thought explanations faithful to a model's actual computation? How would you test this?
- [LLM07-281] How would you detect a model producing good-sounding reasons that do not actually drive its behaviour?
- [LLM07-282] Why can behavioural self-reports from an LLM differ from what it actually does?
- [LLM07-283] Why should you not train against the chain of thought if you want to monitor it?
- [LLM07-284] Can you rely on monitoring a reasoning model's chain of thought as a safety control?
- [LLM07-285] Your chain-of-thought monitor's hit rate dropped sharply after a model upgrade. Is the new model safer, or is something else going on?
- [LLM07-286] Should chain-of-thought monitor flags ever block an action automatically, and what would that do to the monitor's value over time?
- [LLM07-287] How would you design an experiment to test for a specific emergent capability or bias in a large language model?
