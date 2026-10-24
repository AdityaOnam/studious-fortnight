---
domain: genai
topic: safety_guardrails_security_jailbreaks
title: Safety, guardrails, security and jailbreaks
tags: [safety, guardrails, prompt-injection, responsible-ai]
count: 82
part: 4/4
---
# Safety, guardrails, security and jailbreaks (part 4)

## PII and privacy in LLM pipelines
- [GA05-286] How do you handle PII and sensitive data in LLM prompts, outputs, logs and training data?
- [GA05-287] What are the key data privacy considerations (GDPR, CCPA) when building AI applications?
- [GA05-288] A stakeholder wants to send sensitive customer data to a third-party model API, saying the business need justifies it. What do you do?
- [GA05-289] How would you build a PII redaction layer for data sent to a model API, and how would you evaluate its recall and the cost of a miss?
- [GA05-290] After redacting PII before sending text to an LLM, how do you re-insert the real names into the model's answer?
- [GA05-291] Your NER-based PII redactor misses about 5% of names. Is that acceptable, and what breaks when it misses an identifier?
- [GA05-292] Prompts and completions contain user data. How do you redact PII in traces without destroying your ability to debug?
- [GA05-293] How do you debug a failure whose root cause was the exact text you redacted?
- [GA05-294] Design the PII-handling pipeline for documents or support transcripts feeding an LLM system.
- [GA05-295] How do you handle PII inside images or scanned PDFs in a document pipeline feeding an LLM system?
- [GA05-296] What is data leakage in an LLM system, and what are the main channels? Which do teams most often forget?
- [GA05-297] What is the difference between "the vendor doesn't train on my data" and "zero data retention," and does the former fully address the risk?
- [GA05-298] What changes if the sensitive data sent to a third-party model API is health records?
- [GA05-299] PHI is in every audio file, transcript and note in a clinical documentation system. How does that shape the architecture and what can you send to a third-party API?
- [GA05-300] A new frontier model would clearly improve note quality, but the vendor will not sign a BAA. What are your options?
- [GA05-301] A developer pasted a customer's PII into a prompt that is now in your trace store and an eval set. Walk through remediation.
- [GA05-302] How do you get PII-laden production conversations into an eval set legally and safely?
- [GA05-303] What data privacy and security controls would you build into an ML platform that trains on user data?
- [GA05-304] How would you improve an on-device model using signals from user devices without collecting user content, and where does the differential-privacy epsilon budget bind?
- [GA05-305] What is differential privacy, how is it applied during training, and how do you balance privacy and utility when accuracy drops?
- [GA05-306] You removed PII, but users were re-identified from the anonymized data. How do you prevent re-identification?
- [GA05-307] For AI summaries of users' private messages, legal asks "can we ever see the summaries?" What do you answer, and what changes if messages are end-to-end encrypted?

## Retention, deletion and unlearning
- [GA05-308] A regulated customer requires zero data retention, but the frontier model you want requires 30-day retention for misuse monitoring. How do you resolve it?
- [GA05-309] How do you enforce data-retention guarantees technically in an LLM platform, not just contractually?
- [GA05-310] How would you prove to an auditor that a specific patient's audio was deleted on schedule?
- [GA05-311] How do you reconcile "log everything for audit" with "retain nothing for privacy"?
- [GA05-312] After a user invokes the right to erasure, where does their data survive across caches, traces, eval sets, embeddings and backups? How do you carry deletion through every derived store?
- [GA05-313] A user invokes the right to be forgotten, but their data is in your model weights. How do you comply?
- [GA05-314] How do you handle a deletion request against a fine-tuning dataset that has already been used to train a model?
- [GA05-315] Why is fine-tuning on PII a deletion nightmare, and why does tenant-data fine-tuning complicate isolation and deletion?
- [GA05-316] How would you verify that an unlearning method worked, and why is that harder than it sounds?
- [GA05-317] Embeddings can leak content under inversion attacks. Does deleting the text but keeping the vector satisfy a deletion request?
- [GA05-318] How do you handle secrets, data retention and compliance for an LLM platform?

## Memorization, extraction and tenant isolation
- [GA05-319] What are memorization and training-data extraction attacks, and how do you evaluate exposure and reduce memorization?
- [GA05-320] Your LLM memorized proprietary training data and leaks it in responses. How do you prevent this?
- [GA05-321] Why does deduplication reduce memorization of training data so much?
- [GA05-322] What is membership inference, and when is it itself the harm?
- [GA05-323] What is model extraction through an API, and how would you detect and limit it?
- [GA05-324] What is a model distillation attack, how does it differ from ordinary distillation, and how do you defend against it?
- [GA05-325] You suspect someone is distilling your model through your public API. How would you detect it, and what can you actually do?
- [GA05-326] Restricting logprobs breaks legitimate uses like classification and eval scoring. How do you decide that trade-off?
- [GA05-327] If you fingerprint a suspect model via canaries, what would you need for that to hold up as evidence?
- [GA05-328] Design a system where one user's prompt cannot leak to another user, with isolation across data, prompts and caches.
- [GA05-329] How do you secure a multi-tenant RAG system against cross-tenant leakage?
- [GA05-330] What is the failure mode of the "shared index plus tenant_id filter" approach, and how do you harden it, including against an ORM bug that bypasses the filter?
- [GA05-331] How can a semantic or shared prompt cache leak data across tenants, and why is it worse than an exact-match cache?
- [GA05-332] A customer reports that another tenant's data appeared in their results, and your logs do not record tenant ID per retrieval. What do you tell them and how do you bound the incident?
- [GA05-333] What is your test strategy for proving there is no cross-user data leakage in an enterprise LLM assistant before shipping?
- [GA05-334] In a multi-tenant LLM system serving law firms, how would you test an ethical wall in CI, and where would you allow cross-matter reuse?
- [GA05-335] Where can permission information still leak in permission-aware enterprise search even with correct document filtering (facet counts, suggestions, agent memory)?
- [GA05-336] A tool returns data the user can see but the target system's other viewers cannot. What does the orchestrator do?
- [GA05-337] Compare RBAC and ABAC for LLM systems, and how do you design access control for a dual-use capability in your own product?
- [GA05-338] How do you handle privacy leakage in a global semantic memory tier shared across users?

## Bias and fairness
- [GA05-339] How do you think about fairness in AI systems, and how do you detect and mitigate bias in ML models and LLMs?
- [GA05-340] How do you evaluate bias in AI model outputs, and how would you audit a deployed model for differential performance across user groups?
- [GA05-341] What are the main fairness metrics (demographic parity, equalized odds, calibration), and why can't you satisfy them all at once?
- [GA05-342] How would you handle an AI model that produces biased or harmful outputs in production?
- [GA05-343] Your model passes one fairness metric but fails another. How do you handle conflicting audit results?
- [GA05-344] Your model was fair at deployment but became biased six months later. How do you monitor continuously?
- [GA05-345] Your resume screening AI rejects more female candidates for engineering roles. How do you fix gender bias?
- [GA05-346] Your model passes bias checks by gender and race separately but fails for intersectional groups. How do you handle it?
- [GA05-347] Your hiring model uses proxy features for protected attributes. How do you eliminate proxy discrimination?
- [GA05-348] Your predictive model creates a feedback loop of biased outcomes. How do you break it?
- [GA05-349] You are asked to ship an LLM-assisted CV screening feature. How do you approach fairness, and is redacting names enough if counterfactual swaps still show a delta?
- [GA05-350] A shipped feature that summarizes job applicants for recruiters is accused of working worse for some groups. How do you establish whether that is true and what do you do?
- [GA05-351] Your counterfactual suite shows a small but consistent tone difference on name swaps. Is that ship-blocking, and who decides?
- [GA05-352] How do you monitor for fairness regressions in production without inspecting customer content?
- [GA05-353] An external auditor cannot reproduce your model's results. How do you ensure audit reproducibility?
- [GA05-354] Your AI denies a service and the user has no way to challenge it. How do you design an appeals process?
- [GA05-355] Your AI denied a loan and the customer demands a GDPR explanation. How do you provide one?
- [GA05-356] How would you evidence human oversight to an auditor when reviewers approve nearly everything?

## Provenance, watermarking and misuse
- [GA05-357] How does LLM watermarking work?
- [GA05-358] How are LLM text watermarks embedded and detected, how do KGW and semantic watermarks differ, and can they survive translation?
- [GA05-359] How do you evaluate an LLM text watermark beyond detectability?
- [GA05-360] Your AI generates fake news images. How do you implement watermarking for AI-generated content?
- [GA05-361] A user screenshots an AI-generated image. What survives, C2PA metadata or SynthID-style watermarks, and why?
- [GA05-362] A customer asks you to prove which of their documents your model wrote. What can you actually deliver, and what if the document was reformatted before it came back?
- [GA05-363] If a regulator requires synthetic output to be labeled, does an invisible watermark satisfy that or do you owe a visible disclosure as well?
- [GA05-364] Why can watermarking and provenance metadata alone not solve misinformation from generated content?
- [GA05-365] What changes for an image-generation open-weights release where you do not control inference?
- [GA05-366] Design the safety stack for voice cloning, covering consent, watermarking and abuse response.
- [GA05-367] A journalist submits audio that your classifier says is synthetic, but the account trace is empty. What do you tell them?
