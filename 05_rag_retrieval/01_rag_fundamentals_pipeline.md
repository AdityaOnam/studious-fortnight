---
domain: rag
topic: rag_fundamentals_pipeline
title: RAG fundamentals and pipeline
tags: [rag, pipeline, fundamentals]
count: 77
---
# RAG fundamentals and pipeline

## What RAG is and why use it
- [RAG01-001] What is Retrieval-Augmented Generation (RAG), and what problem does it solve for LLMs?
- [RAG01-002] Explain the core intuition behind RAG: what is retrieved, what is generated, and how are the two connected?
- [RAG01-003] Why is RAG often better than relying on an LLM alone?
- [RAG01-004] What are the main benefits of using a RAG system?
- [RAG01-005] How does RAG handle long-tail knowledge, private data, data freshness and source attribution that a base LLM cannot?
- [RAG01-006] Can you give examples of real-world applications where RAG has demonstrated value?
- [RAG01-007] What kinds of knowledge belong in model weights versus in an external retrieval index?
- [RAG01-008] How does RAG help reduce hallucinations in LLM-generated responses?
- [RAG01-009] How would you explain to a PM why RAG does not make hallucination impossible?
- [RAG01-010] Why would you still use RAG if frontier models offer million-token context windows?
- [RAG01-011] Someone proposes replacing your RAG pipeline by loading all documents into a million-token context on every call. How do you evaluate that proposal?
- [RAG01-012] Where is the cost break-even between long context with prompt caching and RAG, and which variables move it?

## RAG pipeline and components
- [RAG01-013] What are the main parts of a RAG system?
- [RAG01-014] Explain the architecture of a basic RAG system.
- [RAG01-015] How does the RAG pipeline work end to end, separating the offline indexing flow from the online query flow?
- [RAG01-016] What happens at indexing time versus query time, and which components are shared between the two?
- [RAG01-017] Why must the embedding model used for queries match the one used for indexing documents?
- [RAG01-018] Why do you need a vector database for RAG, and why can a plain relational database not do the job on its own?
- [RAG01-019] Walk me through every stage of a production RAG pipeline, from raw documents to a cited answer.
- [RAG01-020] Which stage of a RAG pipeline would you invest in first for a new system, and why?
- [RAG01-021] What different invocation patterns of RAG exist (retrieve once, iterative retrieval, retrieval on demand), and when would you use each?
- [RAG01-022] How do LlamaIndex, LangChain and similar frameworks structure a RAG pipeline, and what do these abstractions cost you versus writing it yourself?
- [RAG01-023] Why should the indexing and query pipelines of an enterprise RAG system be separated?
- [RAG01-024] What role does metadata play in a RAG pipeline, from ingestion through to answer generation?

## Naive RAG limits and variants
- [RAG01-025] What are the fundamental challenges of RAG systems?
- [RAG01-026] What limits naive RAG, and what is the retrieval quality gap you see in practice?
- [RAG01-027] Describe naive, advanced, agentic and graph RAG and what each adds over the previous one.
- [RAG01-028] Why do naive RAG systems fail on multi-hop or comparison questions, and what would you change?
- [RAG01-029] The user question is ambiguous or has several possible meanings. How does RAG handle that?
- [RAG01-030] Where does a vanilla top-k similarity search fail even though the answer is present in the corpus?
- [RAG01-031] Why does an enterprise RAG deployment often fail on real use cases, and how do you choose which enhancement to add?
- [RAG01-032] A customer says "just index everything" for a RAG system. Why is that a bad idea?
- [RAG01-033] How does retrieval noise, such as irrelevant or near-duplicate chunks, degrade answer quality even when the right chunk is present?

## Grounding, hallucination and citations
- [RAG01-034] What is a common design pattern for grounding LLM answers in facts?
- [RAG01-035] How do you increase accuracy and reliability, and make answers verifiable, in an LLM system?
- [RAG01-036] Search results are relevant, but the model ignores them and answers from training data. How do you fix this?
- [RAG01-037] How do you implement citation and source attribution in RAG?
- [RAG01-038] Would you ever let a RAG model answer from parametric knowledge without a citation?
- [RAG01-039] How should a RAG system behave when the retrieved context does not contain the answer?
- [RAG01-040] How would you verify that a cited passage actually supports the claim attached to it?
- [RAG01-041] How do you attribute every claim in a generated answer to a specific retrieved span?
- [RAG01-042] A customer's lawyers say RAG answers must be traceable to exact clause text. How does that change the design?

## Context assembly and prompting
- [RAG01-043] How is the prompt given to the LLM in a RAG system different from a standard, non-RAG prompt?
- [RAG01-044] You have retrieved chunks and a question. How do you build the prompt when some documents are irrelevant and two of them contradict each other?
- [RAG01-045] How do you handle conflicting information across retrieved chunks?
- [RAG01-046] How do you assemble and order the final context from retrieved chunks, including citations?
- [RAG01-047] If recall matters and you must send 40 retrieved chunks to the LLM, what changes in the prompt?
- [RAG01-048] What response generation strategies exist for RAG (stuff, map-reduce, refine), and how do they trade off context use and cost?
- [RAG01-049] What is context compression in RAG, and how do LLM-based, embedding-based, rerank-based and token-pruning approaches compare, including accuracy risks?
- [RAG01-050] Why does the position of a chunk within the prompt matter, and how would you order chunks to account for it?
- [RAG01-051] How do you decide how many chunks to put in the context window for a given question?
- [RAG01-052] How do you budget the context window between system prompt, conversation history, retrieved chunks and the generated answer?

## Design choices and tradeoffs
- [RAG01-053] What are the key hyperparameters in a RAG pipeline?
- [RAG01-054] How do you choose values for LLM inference hyperparameters such as temperature and max tokens in a RAG system?
- [RAG01-055] What are the key considerations when choosing an LLM for a RAG system?
- [RAG01-056] What are the key RAG tradeoffs, such as latency versus accuracy, chunk size versus context, and cost versus quality?
- [RAG01-057] When should a RAG request skip retrieval entirely, and how would you build the decision logic?
- [RAG01-058] How would you diagnose whether a bad answer came from retrieval, context assembly or generation?
- [RAG01-059] Which components of a RAG system would you evaluate and tune independently, and why?
- [RAG01-060] When does compiling knowledge once into summaries or a wiki beat both classic RAG and an agentic retrieval loop?
- [RAG01-061] Compare RAG, long-context prompting and fine-tuning for injecting domain knowledge into an LLM across freshness, cost and accuracy.

## Production architecture, freshness, cost and latency
- [RAG01-062] How would you design a complete production-grade RAG pipeline?
- [RAG01-063] How do you update a RAG knowledge base without rebuilding everything, using batch, real-time or versioned updates?
- [RAG01-064] How do you keep a RAG index fresh within minutes of a document changing?
- [RAG01-065] How do you handle deleted or access-restricted documents so they never appear in retrieved context?
- [RAG01-066] How do you reduce the cost of a RAG system, including tiered models, progressive detail and cost guardrails?
- [RAG01-067] How do you optimize RAG latency using parallel retrieval, batched embedding and streaming?
- [RAG01-068] What does a typical latency budget look like across the stages of a RAG request, and where do you cut first?
- [RAG01-069] How would you enforce per-user permissions in a multi-tenant RAG system?
- [RAG01-070] A RAG system works well in demos but poorly in production. What gaps between the two would you look for?
- [RAG01-071] Estimate the storage and embedding cost of indexing 10 million documents of about 2,000 tokens each.

## Design scenarios
- [RAG01-072] You are building support QA over a fixed 40k-document knowledge base with a 1.5 s latency budget. What architecture would you choose and why?
- [RAG01-073] Design the smallest RAG system that could work for "chat with our docs." When do you need more, and when is RAG the wrong call?
- [RAG01-074] Design a RAG assistant for an internal engineering wiki with frequent edits and per-team access control. What are the main components?
- [RAG01-075] Design a RAG system for answering questions over legal contracts where wrong answers carry real risk.
- [RAG01-076] Your RAG chatbot answers well for single-turn questions but breaks in multi-turn conversations. What changes in the architecture?
- [RAG01-077] Design a RAG system that must serve both short factual lookups and long analytical questions over the same corpus.
