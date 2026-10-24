## What RAG is and why use it
- [E] What is Retrieval-Augmented Generation (RAG), and what problem does it solve for LLMs? {Q004749,Q010759,Q007808,D00306,D04824,Q004279}
- [E] Explain the core intuition behind RAG: what is retrieved, what is generated, and how are the two connected? {GEN}
- [E] Why is RAG often better than relying on an LLM alone? {Q012421}
- [E] What are the main benefits of using a RAG system? {Q007124}
- [M] How does RAG handle long-tail knowledge, private data, data freshness and source attribution that a base LLM cannot? {D04825}
- [E] Can you give examples of real-world applications where RAG has demonstrated value? {Q003407}
- [E] What kinds of knowledge belong in model weights versus in an external retrieval index? {GEN}
- [M] How does RAG help reduce hallucinations in LLM-generated responses? {Q003432}
- [M] How would you explain to a PM why RAG does not make hallucination impossible? {Q007811}
- [M] Why would you still use RAG if frontier models offer million-token context windows? {D00309}
- [M] Someone proposes replacing your RAG pipeline by loading all documents into a million-token context on every call. How do you evaluate that proposal? {D00310}
- [H] Where is the cost break-even between long context with prompt caching and RAG, and which variables move it? {D00311}

## RAG pipeline and components
- [E] What are the main parts of a RAG system? {Q012420,Q004751,D04826}
- [E] Explain the architecture of a basic RAG system. {Q004750}
- [E] How does the RAG pipeline work end to end, separating the offline indexing flow from the online query flow? {Q012422,D00307}
- [E] What happens at indexing time versus query time, and which components are shared between the two? {GEN}
- [M] Why must the embedding model used for queries match the one used for indexing documents? {GEN}
- [M] Why do you need a vector database for RAG, and why can a plain relational database not do the job on its own? {D00315}
- [M] Walk me through every stage of a production RAG pipeline, from raw documents to a cited answer. {Q007816,Q010801}
- [M] Which stage of a RAG pipeline would you invest in first for a new system, and why? {Q007817}
- [M] What different invocation patterns of RAG exist (retrieve once, iterative retrieval, retrieval on demand), and when would you use each? {D04827,Q011669}
- [M] How do LlamaIndex, LangChain and similar frameworks structure a RAG pipeline, and what do these abstractions cost you versus writing it yourself? {D04838,Q006054}
- [M] Why should the indexing and query pipelines of an enterprise RAG system be separated? {D00332}
- [M] What role does metadata play in a RAG pipeline, from ingestion through to answer generation? {GEN}

## Naive RAG limits and variants
- [M] What are the fundamental challenges of RAG systems? {Q003406}
- [M] What limits naive RAG, and what is the retrieval quality gap you see in practice? {D00313}
- [M] Describe naive, advanced, agentic and graph RAG and what each adds over the previous one. {D00308}
- [M] Why do naive RAG systems fail on multi-hop or comparison questions, and what would you change? {D04842}
- [M] The user question is ambiguous or has several possible meanings. How does RAG handle that? {D00331}
- [M] Where does a vanilla top-k similarity search fail even though the answer is present in the corpus? {GEN}
- [M] Why does an enterprise RAG deployment often fail on real use cases, and how do you choose which enhancement to add? {D00321}
- [M] A customer says "just index everything" for a RAG system. Why is that a bad idea? {Q010458}
- [H] How does retrieval noise, such as irrelevant or near-duplicate chunks, degrade answer quality even when the right chunk is present? {GEN}

## Grounding, hallucination and citations
- [M] What is a common design pattern for grounding LLM answers in facts? {Q004277}
- [M] How do you increase accuracy and reliability, and make answers verifiable, in an LLM system? {Q007123}
- [M] Search results are relevant, but the model ignores them and answers from training data. How do you fix this? {D00316}
- [M] How do you implement citation and source attribution in RAG? {Q004774,Q007905}
- [M] Would you ever let a RAG model answer from parametric knowledge without a citation? {Q007908}
- [M] How should a RAG system behave when the retrieved context does not contain the answer? {GEN}
- [M] How would you verify that a cited passage actually supports the claim attached to it? {GEN}
- [H] How do you attribute every claim in a generated answer to a specific retrieved span? {Q011825}
- [H] A customer's lawyers say RAG answers must be traceable to exact clause text. How does that change the design? {Q010439}

## Context assembly and prompting
- [M] How is the prompt given to the LLM in a RAG system different from a standard, non-RAG prompt? {Q003416}
- [M] You have retrieved chunks and a question. How do you build the prompt when some documents are irrelevant and two of them contradict each other? {Q007736}
- [M] How do you handle conflicting information across retrieved chunks? {D00324}
- [M] How do you assemble and order the final context from retrieved chunks, including citations? {D00317}
- [M] If recall matters and you must send 40 retrieved chunks to the LLM, what changes in the prompt? {Q007738}
- [M] What response generation strategies exist for RAG (stuff, map-reduce, refine), and how do they trade off context use and cost? {D04836}
- [M] What is context compression in RAG, and how do LLM-based, embedding-based, rerank-based and token-pruning approaches compare, including accuracy risks? {D00318,D00319}
- [M] Why does the position of a chunk within the prompt matter, and how would you order chunks to account for it? {GEN}
- [M] How do you decide how many chunks to put in the context window for a given question? {GEN}
- [H] How do you budget the context window between system prompt, conversation history, retrieved chunks and the generated answer? {GEN}

## Design choices and tradeoffs
- [M] What are the key hyperparameters in a RAG pipeline? {Q003417}
- [M] How do you choose values for LLM inference hyperparameters such as temperature and max tokens in a RAG system? {Q003418}
- [M] What are the key considerations when choosing an LLM for a RAG system? {Q003415}
- [M] What are the key RAG tradeoffs, such as latency versus accuracy, chunk size versus context, and cost versus quality? {Q007067}
- [M] When should a RAG request skip retrieval entirely, and how would you build the decision logic? {D04964,D00327}
- [M] How would you diagnose whether a bad answer came from retrieval, context assembly or generation? {GEN}
- [M] Which components of a RAG system would you evaluate and tune independently, and why? {GEN}
- [H] When does compiling knowledge once into summaries or a wiki beat both classic RAG and an agentic retrieval loop? {GEN}
- [H] Compare RAG, long-context prompting and fine-tuning for injecting domain knowledge into an LLM across freshness, cost and accuracy. {GEN}

## Production architecture, freshness, cost and latency
- [H] How would you design a complete production-grade RAG pipeline? {Q006151,Q007215}
- [M] How do you update a RAG knowledge base without rebuilding everything, using batch, real-time or versioned updates? {Q003618,D00322}
- [M] How do you keep a RAG index fresh within minutes of a document changing? {Q009433}
- [M] How do you handle deleted or access-restricted documents so they never appear in retrieved context? {GEN}
- [M] How do you reduce the cost of a RAG system, including tiered models, progressive detail and cost guardrails? {D00320,D00333}
- [M] How do you optimize RAG latency using parallel retrieval, batched embedding and streaming? {D00329}
- [M] What does a typical latency budget look like across the stages of a RAG request, and where do you cut first? {GEN}
- [M] How would you enforce per-user permissions in a multi-tenant RAG system? {GEN}
- [H] A RAG system works well in demos but poorly in production. What gaps between the two would you look for? {GEN}
- [H] Estimate the storage and embedding cost of indexing 10 million documents of about 2,000 tokens each. {GEN}

## Design scenarios
- [M] You are building support QA over a fixed 40k-document knowledge base with a 1.5 s latency budget. What architecture would you choose and why? {Q007023}
- [H] Design the smallest RAG system that could work for "chat with our docs." When do you need more, and when is RAG the wrong call? {Q010599}
- [H] Design a RAG assistant for an internal engineering wiki with frequent edits and per-team access control. What are the main components? {GEN}
- [H] Design a RAG system for answering questions over legal contracts where wrong answers carry real risk. {GEN}
- [H] Your RAG chatbot answers well for single-turn questions but breaks in multi-turn conversations. What changes in the architecture? {GEN}
- [H] Design a RAG system that must serve both short factual lookups and long analytical questions over the same corpus. {GEN}
