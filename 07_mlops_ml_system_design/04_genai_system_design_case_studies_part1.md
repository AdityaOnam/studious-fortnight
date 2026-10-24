---
domain: mlsd
topic: genai_system_design_case_studies
title: GenAI / LLM system design case studies
tags: [genai-system-design, llm-platform, case-study]
count: 105
part: 1/3
---
# GenAI / LLM system design case studies (part 1)

## Approach, scoping and cross-cutting concerns
- [MS04-001] How would you define AI system design, and how does it differ from classical ML system design?
- [MS04-002] What clarifying questions do you ask before designing an open-ended LLM application?
- [MS04-003] What are the hard problems you expect when shipping a product built on a general LLM, such as latency, reliability and evaluation?
- [MS04-004] When would you choose a fixed workflow over an autonomous agent, or avoid using an LLM altogether?
- [MS04-005] How do you decide between a hosted API model, a fine-tuned open-weight model and a self-hosted model for a new product?
- [MS04-006] An enterprise customer says "We want AI to automate our claims processing." As the engineer in the room, what do the first two weeks look like?
- [MS04-007] How would you build a 0-to-1 MVP for a vertical-industry AI project such as a law firm, and which modules would you build first?
- [MS04-008] A take-home asks for a tool that answers questions over public docs in a weekend. How do you approach it, and what do you deliberately skip?
- [MS04-009] After building that weekend docs question-answering tool, what would you build in week two?
- [MS04-010] How would you structure a service that takes a user question, enriches it with data from a third-party API, and answers via a chat-model API?
- [MS04-011] How would you design a hybrid architecture with a Go backend and a Python AI service, and why should Go handle business logic while Python handles AI orchestration?
- [MS04-012] How do you approach capacity planning for an AI system?
- [MS04-013] How would you design infrastructure for 1M LLM queries per day?
- [MS04-014] Estimate the GPU fleet and monthly cost for a chat assistant with 5M daily users, about 6 turns each, averaging 500 input and 300 output tokens per turn.
- [MS04-015] In a RAG/LLM serving system, what breaks first at 10x traffic: the GPU queue, vector index RAM, the reranker, or the database?
- [MS04-016] How do you degrade gracefully under a traffic spike rather than fall over in an LLM serving system?
- [MS04-017] What reliability patterns such as timeouts, retries, fallbacks, queues and circuit breakers apply to an LLM service?
- [MS04-018] How would you design guardrails for an LLM product covering input filtering, output filtering, PII and grounding checks?
- [MS04-019] How would you account for and reduce cost and latency in a production LLM application using caching, routing and streaming?
- [MS04-020] What would you monitor in a production LLM system, such as quality drift, retrieval hit rate and cost per request?
- [MS04-021] Design an LLM evaluation platform that teams across a company can use to test prompts, models and pipelines.
- [MS04-022] How do you build an offline evaluation set for a new LLM feature before launch when you have no production traffic?
- [MS04-023] An LLM feature's quality dropped after a release. How do you determine whether the cause is the model, the prompt, retrieval or the data?
- [MS04-024] A product team wants to A/B test a new model or prompt on live traffic. How do you design the experiment infrastructure, guardrail metrics and rollback?

## Chat assistants and memory
- [MS04-025] Design ChatGPT end to end, from training to serving.
- [MS04-026] Design a chat assistant service like Claude.
- [MS04-027] Design a personal AI chat assistant.
- [MS04-028] Design a system that lets an LLM chat handle several distinct questions within a single conversation thread.
- [MS04-029] Build a chatbot that helps people book hotels. What components do you need?
- [MS04-030] Design memory for a personal AI assistant, including memory that persists across sessions.
- [MS04-031] Design the memory and personalisation layer for an assistant serving millions of users. What do you store, when do you summarise versus retrieve, and how do you evaluate memory quality?
- [MS04-032] How do you handle a user correcting a fact that the memory system extracted wrongly?
- [MS04-033] How would you let users view, edit and delete what an assistant remembers about them, and what does deletion mean for derived summaries and embeddings?
- [MS04-034] When does injecting long-term memory hurt answer quality, and how do you decide what to include in a given prompt?
- [MS04-035] Design an AI-powered email assistant.
- [MS04-036] Design a personalized learning assistant.
- [MS04-037] Design a meeting assistant for thousands of meetings daily: recording, diarisation, summary, action items and integrations.
- [MS04-038] Design a system that summarizes long team chat threads and conversations.
- [MS04-039] Design an LLM-powered shopping assistant that helps users find products through dialogue.
- [MS04-040] Design an AI copilot that helps product managers with strategy and analysis.
- [MS04-041] How would you design a recommendation system in which an LLM acts as a ranker or a feature generator?
- [MS04-042] How do you prevent an LLM from hallucinating facts about movies in a movie recommendation system?
- [MS04-043] How would you design a batch pipeline that generates and summarizes content at scale with safety filtering?
- [MS04-044] Design a generative AI system that extracts structured information from unstructured customer notes.

## RAG and knowledge Q&A systems
- [MS04-045] Design a RAG system that lets users chat with their documents, such as private company documents.
- [MS04-046] Design a knowledge Q&A system.
- [MS04-047] Design a Q&A assistant over our internal docs. What is the strongest first move?
- [MS04-048] How would you design a question answering system that extracts an answer from a large collection of documents given a user query?
- [MS04-049] When would you choose RAG, fine-tuning or long-context prompting to give a model access to company knowledge?
- [MS04-050] How would you budget context tokens for a RAG system, and what do you do when no answer exists in the corpus?
- [MS04-051] How would you parse and chunk a heterogeneous corpus of PDFs with tables, slide decks, wiki pages and code in the ingestion pipeline?
- [MS04-052] How do you design an enterprise production RAG system, and why must the ingestion and query pipelines be separated?
- [MS04-053] Design a RAG system over an enterprise's data: 10M documents in object storage plus structured tables, with per-user access controls. Walk through the architecture and how you would evaluate it.
- [MS04-054] Where does an enterprise RAG design built for 10M documents break at 100M documents across 50 connectors?
- [MS04-055] A new B2B customer wants the assistant over their private wiki: exact part-number queries are common, about 3M docs, a 1.5 s budget, strict isolation and weekly doc updates. What is the end-to-end design?
- [MS04-056] How do you design and deploy an embedding service for large-scale RAG, including embedding API cost optimization and vector index version management?
- [MS04-057] How do you keep a RAG index fresh when source documents change hourly, including deleting stale chunks and re-embedding after a model change?
- [MS04-058] Your RAG assistant confidently answers questions whose answer is not in the corpus. How do you diagnose and fix it?
- [MS04-059] Offline retrieval recall looks good but users complain about answer quality. Where do you look first?
- [MS04-060] How do you design citations so users can verify answers, and how do you check that the citations are faithful?
- [MS04-061] Estimate the memory needed for a vector index of 200M chunks with 1024-dimensional embeddings, and which options reduce it.
- [MS04-062] Design a RAG system for a financial research platform that must answer questions about earnings reports containing text, tables and charts.
- [MS04-063] Design cross-lingual RAG where the knowledge base is in English and Hindi, but users ask in Tamil, Telugu or transliterated Hinglish.
- [MS04-064] Users want to ask questions across a 10,000-hour library of training videos. How do you design and cost it?

## Search and answer engines
- [MS04-065] Design a semantic search engine.
- [MS04-066] Design semantic search over a large product catalogue.
- [MS04-067] Design an AI candidate sourcing system with 750M profiles, semantic search and under 500 ms latency.
- [MS04-068] Design a multimodal search system over text, image and video.
- [MS04-069] Design a retrieval pipeline pulling from 100B web pages with sub-second latency and freshness guarantees.
- [MS04-070] Design a ranking system that combines BM25, dense retrieval and LLM reranking across multiple indexes.
- [MS04-071] Design an answer engine: a user types a question and gets a cited, streamed answer, with a 3-second budget to a complete short answer.
- [MS04-072] What changes in an answer-engine design if 30% of queries are follow-ups in an existing conversation?
- [MS04-073] How does an answer engine handle breaking news, such as a query about something that happened 20 minutes ago?
- [MS04-074] Design the serving stack for a consumer chatbot with real-time search over a social-media firehose.
- [MS04-075] For a chatbot with real-time search over a social-media firehose, what is your backpressure strategy when the firehose spikes 10x during a live event?
- [MS04-076] Design a system that finds driving segments similar to a given one across an entire fleet archive.
- [MS04-077] In a system that searches a fleet archive for similar driving segments, how would you handle a query about something that did not happen, such as a pedestrian who nearly stepped out?
- [MS04-078] How would you evaluate a semantic search system offline and online, and what would you do about missing relevance labels?
- [MS04-079] LLM reranking of the top 100 results is too slow and expensive. How do you cut latency and cost without losing much quality?
- [MS04-080] How do you understand and rewrite queries (spelling, intent, filters, multilingual) before retrieval in a search or answer system?

## Enterprise assistants and permission-aware retrieval
- [MS04-081] Design an enterprise assistant that answers employee questions over internal documents, wikis and other knowledge sources of mixed formats, respecting per-user permissions.
- [MS04-082] How would you build an LLM-powered enterprise search system that returns synthesized answers with citations?
- [MS04-083] Design a Copilot feature that answers questions over a user's work email, documents and meetings without ever leaking content the user cannot access.
- [MS04-084] In an enterprise Copilot over a user's documents, how do you handle a document shared with the user mid-conversation? When does it become answerable?
- [MS04-085] Design permission-aware retrieval for a multi-tenant SaaS product or enterprise search, where users must never see results they cannot access in the source system.
- [MS04-086] A document's sharing settings change every few minutes. How fast must an access revocation take effect in permission-aware retrieval, and what is your mechanism?
- [MS04-087] Build RAG over a customer's documents where access control is row- and document-level. How do you guarantee a user never sees restricted content in an answer?
- [MS04-088] How do you handle documents with mixed permissions in an enterprise RAG system?
- [MS04-089] In an enterprise document assistant, how do you handle a document whose ACL is broader than its content should be?
- [MS04-090] How does an enterprise RAG system handle real-time collaboration documents such as Google Docs or live Confluence pages?
- [MS04-091] Design a connector framework that syncs content and permissions from 100+ SaaS apps into one search index.
- [MS04-092] Where do you enforce ACLs in a RAG pipeline: pre-filter in the vector query, post-filter after retrieval, or at the connector? What are the tradeoffs?
- [MS04-093] An employee plants instructions in a wiki page that the assistant later retrieves for other users. How do you defend against this indirect prompt injection?
- [MS04-094] How do you evaluate an enterprise assistant when you are not allowed to read the customer's documents?

## Multi-tenancy in LLM and RAG systems
- [MS04-095] How do you handle multi-tenant RAG systems?
- [MS04-096] In a multi-tenant RAG system, you are choosing between Pinecone namespaces, Weaviate per-tenant shards and pgvector with Row-Level Security. Which fails first under noisy-neighbor pressure, and which under an audit?
- [MS04-097] Design a multi-tenant AI chatbot platform where each business gets a custom chatbot.
- [MS04-098] Design a RAG system that serves 10,000 queries per second across 500 tenants with a p99 latency of 2 seconds.
- [MS04-099] You are building a multi-tenant agent platform. Tenants bring their own MCP servers and their own data. What isolates them?
- [MS04-100] How do you let tenants in a multi-tenant agent platform share a common tool set without sharing the prompt cache?
- [MS04-101] How do you handle "noisy neighbors" in a multi-tenant LLM cluster?
- [MS04-102] A single malformed request crashed a vLLM replica and every tenant on it lost service. What is the design lesson?
- [MS04-103] How would you support per-tenant customization (system prompts, fine-tuned adapters, knowledge bases) while keeping isolation and manageable cost?
- [MS04-104] How would you attribute LLM cost per tenant and enforce per-tenant budgets and fair-share rate limits?
- [MS04-105] How do you offboard a tenant and prove their data is gone from indexes, caches, logs and fine-tuned artifacts?
