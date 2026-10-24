---
domain: mlsd
topic: genai_system_design_case_studies
title: GenAI / LLM system design case studies
tags: [genai-system-design, llm-platform, case-study]
count: 66
part: 2/3
---
# GenAI / LLM system design case studies (part 2)

## Customer-support and action-taking assistants
- [MS04-106] Design a customer-support agent that combines RAG with real actions (refunds, order changes) and escalates to humans.
- [MS04-107] Design an LLM-powered customer-support assistant on top of an existing help centre, with guardrails, resolution of common tickets and escalation to humans.
- [MS04-108] Design the backend for a customer-facing chatbot. Walk me through the request path.
- [MS04-109] Design a multi-agent customer support system.
- [MS04-110] Design a system that lets a customer support agent answer questions using data from Zendesk, Salesforce and an internal knowledge base.
- [MS04-111] Design a customer-facing agent for an airline that can cancel and rebook flights. How do you keep it from violating fare policy?
- [MS04-112] Design an in-app assistant that can take actions in your app (for example "book it", "send it to Sam").
- [MS04-113] For an LLM customer-support system, what is the online metric (deflection, CSAT, task completion) and its counter-metric (escalation rate, false-refusal rate, hallucination rate)?
- [MS04-114] In a multilingual LLM customer-support system, why not translate to English and back?
- [MS04-115] In a customer-support AI, what do you do if the AI keeps apologizing but never actually helps?
- [MS04-116] How does a customer-support AI handle a customer who insists on talking to a human?
- [MS04-117] How do you decide when the support agent should escalate to a human, and what context do you hand over?
- [MS04-118] How do you make agent actions such as refunds safe against retries, double submissions and requests the customer is not authorized to make?
- [MS04-119] Design an agent that can take actions in a spreadsheet ("insert a pivot table of Q3 sales by region"): orchestration, tools and failure handling.
- [MS04-120] How would you design a system that lets non-technical users automate desktop tasks using AI?
- [MS04-121] Design an end-to-end cloud service that lets users delegate multi-step phone tasks ("order my usual coffee") to an autonomous agent. Cover architecture and failure modes.
- [MS04-122] How would you test a customer-support agent before launch, and how would you replay production conversations against a new version?

## Text-to-SQL and data platforms for AI
- [MS04-123] Design a text-to-SQL system over a data warehouse with thousands of tables. What is hard, and how do you evaluate it?
- [MS04-124] How do you stop a text-to-SQL agent from producing plausible-but-wrong joins between tables that share column names?
- [MS04-125] How do you evaluate text-to-query accuracy when the customer cannot share their data?
- [MS04-126] Design a system that converts natural language into queries over an observability dataset using an LLM.
- [MS04-127] In a company-wide AI assistant, where does text-to-SQL fit versus RAG over documentation?
- [MS04-128] Design the data platform for a company-wide AI assistant.
- [MS04-129] Which single component of a company-wide AI assistant's data platform would you build first to de-risk the design?
- [MS04-130] Leadership wants an agent that answers business questions straight from the warehouse. What does the data platform need before you would let it?
- [MS04-131] An agent and a finance dashboard disagree on last quarter's revenue. How do you find out which is right?
- [MS04-132] How do you stop agent query load from blowing the data warehouse budget?
- [MS04-133] How would you make a text-to-SQL agent safe to run on production data: read-only access, cost limits and row-level permissions?
- [MS04-134] A business user asks an ambiguous question such as "How many active customers did we have last quarter?" How should the text-to-SQL system respond?

## Document intelligence and extraction
- [MS04-135] Design a document-intelligence pipeline: scanned PDFs in, structured fields out, at 10M documents.
- [MS04-136] Design an AI-powered document processing pipeline for a financial institution.
- [MS04-137] Design a document-extraction system. When do you use an OCR pipeline versus sending pages to a vision-language model?
- [MS04-138] How does the OCR-versus-VLM calculus in a document-extraction system change at 10M pages per month?
- [MS04-139] In a document-extraction system, where does human-in-the-loop go, and how do you decide the confidence threshold?
- [MS04-140] In a contract data extraction system, what do you do if the extraction confidence is low?
- [MS04-141] How do you handle contracts with non-standard layouts in a contract extraction system?
- [MS04-142] How do you handle contracts where key terms are defined in exhibits in a contract extraction system?
- [MS04-143] How would you evaluate an extraction pipeline and detect silent regressions when document templates change?
- [MS04-144] Design an AI-powered legal document review system.
- [MS04-145] Design an agent that takes a draft NDA and returns a redlined Word document reflecting the firm's playbook, not a chat response.
- [MS04-146] In a batch LLM document-review workflow, the client adds three questions after the batch has run. What re-runs and what does not?
- [MS04-147] How would the design of a batch LLM document-review workflow change if turnaround had to be under ten minutes?

## Coding assistants and coding agents
- [MS04-148] Design an LLM-powered coding assistant that suggests code completions inside an editor.
- [MS04-149] Design a next-edit prediction (tab completion) system for a code editor that must feel instant, with sub-100 ms perceived latency, for millions of daily users.
- [MS04-150] Design a code assistant: repo indexing, context assembly, edit application and evaluation.
- [MS04-151] How would you index a 100k-file monorepo so an AI editor can retrieve relevant context, and keep the index fresh as the user edits?
- [MS04-152] When diffing repository snapshots by content hash for incremental indexing, how do you handle renames where a content hash matches at a new path?
- [MS04-153] When using a Merkle tree of file hashes for incremental repository indexing, where would you persist the tree so a restart does not rescan the repo?
- [MS04-154] Your agent model outputs an edited version of a 500-line file. Applying it verbatim is slow and error-prone. How do you make "apply" fast and reliable?
- [MS04-155] An AI model is streaming a multi-file edit while the user keeps typing in one of those files. How do you apply the edits without corrupting the buffer?
- [MS04-156] How does your design for applying streamed AI edits to an editor buffer change for two users plus an agent (three writers)?
- [MS04-157] How do you make a multi-file AI edit atomically undoable?
- [MS04-158] Design an AI coding agent (SWE-bench-style) that takes an issue and produces a verified patch.
- [MS04-159] How should a coding agent handle tasks that require changes across 20+ files?
- [MS04-160] How do you prevent a coding agent from introducing security vulnerabilities?
- [MS04-161] An agent needs to iterate on code (run builds, tests, lints) without disturbing what the user sees in their editor. How do you architect that?
- [MS04-162] How would you extend a local sandboxed code-iteration agent to cloud agents on a repo the user has not checked out, and to handing a session from cloud back to local?
- [MS04-163] Design the execution environment for thousands of concurrent cloud coding agents. It must survive an agent waiting forty minutes for CI.
- [MS04-164] In an execution environment for cloud coding agents, what is your rollback granularity, and how do you avoid a snapshot chain that grows without bound?
- [MS04-165] Design a code generation and review system.
- [MS04-166] Design an LLM system that automatically reviews pull requests and tags them.
- [MS04-167] We want an LLM agent to triage SAST findings and review PRs for vulnerabilities. How would you design it, and how would you know it works?
- [MS04-168] Design an AI system for automated code migration.
- [MS04-169] Explain how you would design a system that uses an AI coding agent as a CI/CD component for automated bug fixing.
- [MS04-170] Design an LLM system that diagnoses production incidents and proposes mitigations for cloud services.
- [MS04-171] How would you evaluate a coding assistant or agent offline and online, beyond pass-rate on a public benchmark?
