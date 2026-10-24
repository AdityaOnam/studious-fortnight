## Building and maintaining eval sets
- [M] What is the smallest useful eval suite you would build in week one, and what is the minimum viable eval before launching an LLM feature? {Q008388,Q009072}
- [M] How do you build a custom eval set for a new LLM feature step by step, and how many examples do you need and where do they come from? {D00189,Q008395}
- [M] What is the role of a golden dataset in AI evaluation, and how do you build and maintain one? {Q005015,Q005945}
- [M] How big should a golden evaluation set be, who should own it, and how do you grow it? {Q006792,Q008389}
- [M] Where does the eval signal come from: human annotation, user feedback, implicit signals or synthetic generation? {Q006790}
- [M] What are the delay and noise of the evaluation signal in an LLM system (a click is not satisfaction; no complaint does not mean correct)? {Q006791}
- [M] What failure classes should you evaluate for in an LLM application, such as wrong answer, missing citation, refusal, latency and cost? {Q006793}
- [M] How do you split eval data into dev, test and held-out sets for an LLM application, and why does it matter? {GEN}
- [M] What makes a single eval case well specified, and what are the common ways individual cases go wrong? {Q008425}
- [M] How do you decide an eval example is hard before you have seen failures? {Q008396}
- [M] Who should write reference answers for an eval set in a domain where nobody on the team is an expert? {Q008426}
- [H] How do you build an eval set when there is no labelled ground truth and the experts who could judge quality are expensive? {Q005016,Q011849,Q009678}
- [H] When building an eval set with a rubric, how do you stop the rubric author's own style preferences from becoming the metric? {Q009679}
- [M] What goes in the eval set versus a unit test? {Q008421}
- [M] Why do you version an eval dataset, and what exactly belongs in the version? {Q008419}
- [M] Your eval is 95% passing and stops discriminating between candidate prompts. What do you do? {Q008397}
- [H] How would you handle an example everyone agrees is mislabelled but that has been in the frozen eval suite for a year? {Q008420}
- [M] How do you keep a golden eval set from going stale and representative as the product evolves? {Q009226,Q010624,Q008359,Q011004,Q010636}
- [M] How do you prevent and detect the team overfitting to the dev eval set as it iterates? {Q008465,Q010138,Q008466}
- [M] Who triages the production-failure queue, and what is the admission bar for a new eval case? {Q008467}
- [M] How would you use synthetic data to build or extend an eval set (say 50 real inputs to 5,000), and what are the failure modes and review process? {Q008468,Q010642,Q010638}
- [M] How would you measure the diversity of an LLM-generated test set? {Q010643}
- [M] When is synthetic test data outright inappropriate? {Q010644}
- [H] How would you measure whether your synthetic eval set predicts production performance? {Q008469}
- [M] What would make you throw an eval task out entirely? {Q009680}

## Deterministic graders and task-specific checks
- [M] Exact-match assertions are useless for LLM output. What kinds of code-graded assertions can you use, and where do they break down? {Q008392,Q010625}
- [E] How would you evaluate an LLM feature that must return structured output such as JSON that follows a schema? {GEN}
- [M] Give a concrete criterion that looks judge-worthy but can be reduced to a code assertion. {Q008391a}
- [M] Your regex grader shows 95% pass but users complain. What is happening? {Q008394}
- [M] When property-based assertions on an LLM response pass but the answer is still wrong, what catches that? {Q010627}
- [H] How do you pick and maintain the similarity threshold when asserting on LLM responses with embedding similarity? {Q010626}
- [M] How would you grade a summarisation task, where every summary is legitimately different, without an LLM judge? {Q008393,Q008415}
- [M] What is your eval for an LLM extraction feature? {Q010587}
- [M] How do you keep the grader out of reach of the system being evaluated? {D00211}

## Statistics, variance and pass@k
- [M] How do you compare two models or prompts in a statistically rigorous way? {Q005019}
- [M] Your new prompt scores 78% versus the old prompt's 74% on a 100-example eval. Is that real, and do you ship it? {Q008502,Q008358}
- [M] Your eval reports 82% pass on 100 examples. What does that number not tell you? {Q008416}
- [H] What would make you distrust an 82% eval pass rate even with a tight confidence interval? {Q008418}
- [M] How large does an eval set need to be before you trust a 3-point difference between two versions or a model swap? {Q009053,Q009456,Q009948,Q010594}
- [M] How would you compute a confidence interval for an eval pass rate, and when is a bootstrap preferable? {GEN}
- [H] You want to detect a 3-4 point improvement in pass rate. How many examples do you need, and how do you get that number down? {Q008503,Q008473}
- [H] Your minimum-detectable-effect calculation says you need 2,800 eval examples and you have 200. What do you actually do? {Q008474}
- [H] How does per-case flip variance change your confidence-interval math when comparing two prompts? {Q008504}
- [M] When comparing two LLM configurations on an eval set, when is a paired design not available to you? {Q008475}
- [M] Evals are nondeterministic (temperature, sampling, flaky agents). How do you get trustworthy numbers and test a chatbot that answers differently every time? {Q008513,Q010619}
- [M] How does non-determinism of LLM outputs change your definition of a flaky test? {Q010634}
- [M] An eval case passes 50% of the time across ten trials of the same configuration. Is it a good case or a broken one? {Q008427}
- [M] How do you handle eval cases that flip on identical inputs during error analysis? {Q008515}
- [H] Your CI budget allows one run per eval case or three runs on a third of the cases. Which do you choose and why? {Q008514}
- [M] Define pass@k. Why is the naive way of computing it problematic, and what is the fix? {Q008401}
- [M] What is the difference between pass@k and pass^k, and when does each matter? {GEN}
- [H] How many trials and tasks do you need before a pass^k difference is signal rather than noise? {Q010137}
- [M] When is optimising pass@10 legitimate for a product? {Q008402}
- [M] How does pass@k relate to best-of-n sampling with a verifier at inference time? {Q008403}

## Code and agent evaluation
- [M] How would you build an execution-based eval for a code-generation feature? {Q008445}
- [M] How do you evaluate code edits in a large existing repo versus writing functions from scratch? {Q008446}
- [M] Your code-generation eval pass rate is 60%. How do you decompose that into actionable failure categories? {Q008447}
- [M] For an AI code-completion model, acceptance rate went up 2% but retained characters went down. What happened? {Q009403}
- [H] How do you evaluate a code-editing model before shipping it? Design the offline and online eval story. {Q009402}
- [M] How do you evaluate agents with metrics such as tool-selection quality, step success and trajectory adherence? {D03774}
- [M] How do you evaluate end-to-end task success versus step-level correctness for an agent, and when do they diverge? {GEN}
- [H] How would you evaluate an agentic coding model on SWE-bench and tau-bench style benchmarks, and beyond a single benchmark number, without fooling yourself? {Q011995,Q010296,Q009872}

## Long-context and multi-turn evaluation
- [M] Why do needle-in-a-haystack results overstate long-context ability, and how should you evaluate long-context recall? {Q007560,D00202}
- [H] A vendor advertises 1M context with 100% needle-in-a-haystack. What has that actually proven? {Q007542}
- [H] How would you design an eval for usable context length on your workload, including for a model whose main improvement is long context? {Q007559,Q009632}
- [M] How would you test whether a model uses information from the middle of a long context? {GEN}
- [H] How would you construct hard distractors automatically from a customer's corpus for a long-context evaluation? {Q007543}
- [H] In a long-context evaluation, what does an unanswerable-question false-positive rate tell you that accuracy does not? {Q007544}
- [H] How would you construct an eval that a needle-in-a-haystack-only model would fail, and what should a long-context agentic benchmark test? {Q009874,Q009880}
- [H] How would you build an eval that separates real long-context retrieval from a model that merely compresses well? {Q009888}
- [H] How would you show a hybrid linear/full-attention or local-attention model has not lost long-range recall or persona consistency at turn 150? {Q010058,Q009285}
- [H] How would you detect that int8 training has degraded a specific behaviour, like staying in character, when aggregate evals show parity? {Q009288}
- [M] How do you evaluate multi-turn conversation quality? {Q005014}
- [M] How do you handle failure modes that only appear in multi-turn context during error analysis? {Q008463}
- [M] Users complain that characters drift out of persona. How would you build a persona scorer that does not just reward verbosity? {Q009297}

## Domain and product evaluations
- [M] How would you evaluate a meeting-summarisation feature before shipping it to a hundred million users? {Q009793}
- [H] Two good clinicians write different notes for the same visit. How do you evaluate note quality at all? {Q009156}
- [M] How would you evaluate a clinical note type for which you have no annotated data? {Q009158}
- [H] How would you evaluate an Indic-language LLM properly, and why is running translated English benchmarks not enough? {Q010089}
- [H] How do you evaluate answer quality for a real-time-search chatbot when ground truth changes hourly? {Q010253}
- [M] How would you evaluate a customer-facing RAG chatbot end to end: retrieval quality, answer faithfulness and user outcomes? {GEN}
- [M] How would you build an eval that catches a model confidently answering about events after its knowledge cutoff? {Q007749}
- [M] What is overrefusal, and how would you build an over-refusal eval that balances safety and helpfulness (for example for a security-tools customer)? {Q008136,D00206}
- [H] How do you evaluate personalization and memory features without storing sensitive user data in eval sets? {Q009754,Q009769}
- [H] Your proxy metrics for notification summarisation look flat but journalists post screenshots of bad summaries. What went wrong in your eval design? {Q009273}
- [M] How would you evaluate whether third-party data enrichment actually improves an LLM service's answers? {Q009843}
- [H] Give a concrete task where the deployment metric is inherently discontinuous. What smooth proxy would you monitor? {Q007570}
- [M] A customer wants an accuracy SLA for an LLM system in the contract. What do you agree to and how do you make it measurable? {Q010448}
- [M] A customer has no labelled data and no eval culture. How do you establish "is it working?" for an LLM deployment? {Q010450}

## Error analysis and the benchmark-to-production gap
- [E] What is error analysis in the context of evaluating LLM applications? {Q010716}
- [M] When should you stop reviewing traces during error analysis? {Q010721}
- [M] What is the difference between error analysis and automated evals, and when should you prioritize each? {Q010959}
- [M] How do you move from ad hoc notes on traces to a failure taxonomy, using open and axial coding? {GEN}
- [M] You have 500 production transcripts flagged as failures. Walk me through your error-analysis process. {Q008462}
- [M] In error analysis of flagged failures, what do you do with the "not actually a failure" cluster? {Q008464}
- [M] What is the benchmark-to-production gap, and how do you bridge it? {D00212}
- [M] What are common evaluation pitfalls, such as small test sets, leakage, ignoring variance and evaluating a different system than you ship? {D00190}
- [M] Where does Goodhart's law bite in LLM evaluation? Give concrete examples and defences. {Q008511}
- [H] Your new model scores higher on every benchmark, but users say it got worse. Why does this happen and how do you find the problem? {Q005008,Q011852}
- [H] Users say the new model "feels worse" but every eval slice improved, or the open model wins evals but the PM says it feels worse. Next move? {Q009697,Q010192}
- [H] Your eval suite is green and scores keep improving, but production complaints are flat or rising. Debug it and redesign the eval system. {Q011003,Q008530,Q010597}
- [M] Your new prompt improves the aggregate pass rate by 3 points, but one customer segment drops 8. How do you catch this before shipping? {Q008518}
- [M] How do you pick eval slices for failure modes you have not thought of yet? {Q008519}
- [M] The regressed eval slice has only 12 examples in total. What do you do? {Q008520}
- [H] Your eval suite is green but the complaints come from 3 users out of 50,000. What do you do? {Q008532}
- [H] Your length penalty cut reasoning tokens sharply and the aggregate eval is flat, but complaints on hard queries rise. How do you find the regression? {Q009776}
- [M] After reducing the cost of an LLM workload, how do you prove quality did not regress? {Q009208}
- [M] How do you set up the eval after migrating from a proprietary API to an open model so that it stays useful? {Q010193}

## Eval system design and release gating
- [M] How would you convince a team shipping on vibes to invest in evals? {Q008387}
- [H] You do not have an eval team. How do you know your LLM feature actually works and keeps working? {Q010593}
- [H] How do you set up an evaluation framework from scratch for a new LLM application, treating it like a test framework? {Q005022,Q010622}
- [M] Where should an LLM eval harness live: a pytest plugin, a standalone service or a vendor tool? {Q010623}
- [M] What is the difference between offline and online evaluation for AI systems? {Q005012}
- [M] How do you evaluate an LLM or RAG system in production? {Q010763}
- [M] How do you build a regression test suite for an LLM application, and what tooling would you use to run it in CI? {Q005005,D03773,D04861}
- [M] How do you evaluate the robustness of an LLM application across input variations? {Q005020}
- [M] How would you combine offline evals, shadow traffic and canary releases to roll out a new model? {GEN}
- [M] How would you A/B test two models in production, and which metrics and guardrails would you track? {D00203}
- [H] Design an evaluation system for comparing two LLMs on open-ended tasks. {Q010879,D00204}
- [H] Design an evaluation suite for a general-purpose chat model covering knowledge, reasoning, code, safety, instruction following and multilingual ability. {D04963}
- [H] Build the evaluation harness for a new frontier LLM release, and the system you would run before and after each model release. What does it need to do? {Q009630,Q009767}
- [H] How do you evaluate your eval suite itself? What makes one good or bad? {Q008533}
- [H] An agent passes its own evals because the evals are weak. How would you detect a low-quality eval set automatically? {Q009705}
- [H] When validating an eval suite by checking that it detects a deliberately degraded model, how do you build that degraded configuration without it being trivially detectable? {Q008535}
- [M] Your eval suite catches 9 of 10 escaped defects but takes 40 minutes in CI. Is it worth it? {Q008534}
- [M] How would you prevent an eval suite that is green while users see quality regress from recurring, without doubling eval cost? {Q008531}

## Reasoning models and chain-of-thought
- [M] What are reasoning models, and how does test-time compute change the picture? When are they worth the cost versus a standard model? {Q007585,Q010840}
- [M] What is extended thinking, and how does a thinking token budget control how much a model thinks? {Q006109}
- [M] Reasoning models expose a thinking budget or reasoning effort setting. How do you tune it, and what goes wrong? {Q007551}
- [M] When is chain-of-thought overthinking harmful, and how do you control reasoning effort? {D00201}
- [M] How would you set a reasoning budget per request rather than globally? {Q008525}
- [M] How does evaluating and observing a reasoning model differ from a standard instruction-tuned model? {Q006900,Q008524}
- [M] How would you evaluate a reasoning benchmark such as GSM8K or AIME, and what failure modes such as answer-format brittleness can distort scores? {GEN}
- [H] Your pass-rate curve is still climbing at the maximum reasoning budget. What does that tell you? {Q008526}
- [H] How do you evaluate whether extra thinking budget actually buys accuracy rather than just inflating token spend? {Q010034,Q010279}
- [H] A hybrid reasoning model has a thinking mode and a direct mode. How do you build one model that does both, and what are the training and serving implications? {Q010277}
- [H] How would you stop a hybrid reasoning model from over-thinking simple prompts? {Q010278}
- [H] Latent (continuous-space) reasoning reportedly beats token-space chain-of-thought on math benchmarks. When would you deploy it in production? {Q010961}
- [M] Why does chain-of-thought reasoning appear only in sufficiently large models, and what capability is it linked to? {D04867}
- [M] Do LLMs actually reason? What evidence supports or contradicts the claim, and how do you probe for it? {D04769}
- [H] How would you tell whether a model's math gain from chain-of-thought reflects reasoning rather than memorization, for example with perturbed problems? {GEN}
- [H] Self-consistency with 8 samples helps on maths but barely moves open-ended generation. Why? {Q007394}
- [M] What is a reasoning model's chain of thought good for, and why is it not a reliable account of the model's actual computation? {D00199}
- [H] Are chain-of-thought explanations faithful to a model's actual computation? How would you test this? {D04868}
- [H] How would you detect a model producing good-sounding reasons that do not actually drive its behaviour? {Q009249}
- [M] Why can behavioural self-reports from an LLM differ from what it actually does? {D00205}
- [M] Why should you not train against the chain of thought if you want to monitor it? {D00200}
- [H] Can you rely on monitoring a reasoning model's chain of thought as a safety control? {Q008874}
- [H] Your chain-of-thought monitor's hit rate dropped sharply after a model upgrade. Is the new model safer, or is something else going on? {Q008875}
- [H] Should chain-of-thought monitor flags ever block an action automatically, and what would that do to the monitor's value over time? {Q008876}
- [H] How would you design an experiment to test for a specific emergent capability or bias in a large language model? {Q011911}
