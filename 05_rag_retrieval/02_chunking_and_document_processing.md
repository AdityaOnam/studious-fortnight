---
domain: rag
topic: chunking_and_document_processing
title: Chunking and document processing
tags: [rag, chunking, parsing, ingestion]
count: 115
---
# Chunking and document processing

## Chunking fundamentals
- [RAG02-001] Why do we chunk documents in a RAG system, and how does chunking affect answer quality?
- [RAG02-002] What are the most common chunking methods used in RAG?
- [RAG02-003] What is the purpose of overlap between chunks, and what does it cost you?
- [RAG02-004] Why not embed whole documents with a long-context embedding model instead of chunking them?
- [RAG02-005] What factors influence the right chunk size for a RAG system, and how do you find a good value for your corpus?
- [RAG02-006] Explain the intuition behind chunk size using a concrete example.
- [RAG02-007] What are the consequences of chunks that are too large versus chunks that are too small?
- [RAG02-008] How do chunk size and overlap affect retrieval recall and answer quality, and what numbers would you start with?
- [RAG02-009] Why does a chunk that covers several topics embed poorly? What is happening in the vector space?
- [RAG02-010] If you embed each page (about 450 tokens) as a chunk, what do you do when the needed information spans several pages?
- [RAG02-011] Your chunk overlap produces redundant results in the top-k. How do you reduce the redundancy?
- [RAG02-012] How do you align chunking with the tokenizer so that chunks fit the embedding model's input limit?
- [RAG02-013] What happens when a chunk exceeds the embedding model's maximum sequence length, and how should the pipeline guard against it?
- [RAG02-014] How would chunking differ for a corpus of tweets versus a corpus of legal contracts?
- [RAG02-015] A corpus has 10M pages of about 500 tokens each. Estimate the vector count and storage for 512-token chunks with 15% overlap and 768-dim float32 embeddings.
- [RAG02-016] You retrieve top-5 chunks of 800 tokens each into a 4k-token window. How do you rebalance chunk size and top-k?

## Chunking strategies
- [RAG02-017] What chunking strategies do you know, and what criteria do you use to pick one for a given corpus?
- [RAG02-018] Compare fixed-size, recursive, semantic and structure-aware chunking.
- [RAG02-019] Why is fixed-size chunking with overlap problematic in production systems?
- [RAG02-020] Why is the recursive character text splitter a common default, and when should you not use it?
- [RAG02-021] When should you use semantic chunking?
- [RAG02-022] How does semantic chunking decide where to split, and how do you choose the breakpoint threshold?
- [RAG02-023] What do recent studies say about the benefit of semantic chunking over fixed-size chunks, and is its extra cost justified?
- [RAG02-024] How would you chunk Markdown, HTML or heading-structured documents so the section hierarchy stays attached to each chunk?
- [RAG02-025] When would you prefer sentence-level chunks over paragraph- or section-level chunks?
- [RAG02-026] What goes wrong when a splitter cuts mid-sentence or mid-table, and how do you prevent it?
- [RAG02-027] What chunking strategy would you use for a large technical documentation corpus, and why?
- [RAG02-028] How does chunking differ for structured documents (PDFs with tables and figures) versus plain-text documents?
- [RAG02-029] What is proposition-based or LLM-driven (agentic) chunking, and what are its cost and consistency tradeoffs?
- [RAG02-030] What chunk enhancement techniques exist in RAG, and what are their pros and cons?
- [RAG02-031] How would you extend a legal-document chunker to handle schedules and exhibits that are effectively separate documents?
- [RAG02-032] How do you handle list items during chunking?
- [RAG02-033] Where does chunking need to change when documents mix English and Hindi on the same page?

## Parent-child chunks and context enrichment
- [RAG02-034] What is parent-child (hierarchical) chunking, and how does it improve retrieval?
- [RAG02-035] What are Parent-Document Retrieval and Sentence Window Retrieval, and when do you use each?
- [RAG02-036] How do you choose child and parent sizes, and how does returning parents change token cost and precision?
- [RAG02-037] When expanding a retrieved chunk with its neighbours, how do you decide how many neighbours to include?
- [RAG02-038] What is Contextual Retrieval, how does it improve RAG, and when would you skip it?
- [RAG02-039] A chunk says "revenue grew 3% over the previous quarter" with no company or quarter, and it never ranks for "ACME Q2 2023 revenue". What is the strongest fix?
- [RAG02-040] What is late chunking, and how does it differ from contextual retrieval?
- [RAG02-041] What cheaper alternatives to LLM-generated context exist, such as prepending titles and section headers, and what do they miss?
- [RAG02-042] What retrieval failures does contextual retrieval not fix?
- [RAG02-043] A 50,000-document knowledge base needs Contextual Retrieval. How do you manage the ingestion cost?
- [RAG02-044] How does prompt caching make contextual retrieval affordable at 10M chunks? Sketch the cost math.

## Tables, code, figures and heterogeneous content
- [RAG02-045] How do you handle tables during chunking?
- [RAG02-046] What breaks when you chunk a table row by row, and how do you keep headers attached when a table spans pages?
- [RAG02-047] How do you chunk and index a 500-row table or other very large table for better retrieval?
- [RAG02-048] Would you embed a table as Markdown, HTML or a natural-language summary, and what are the tradeoffs?
- [RAG02-049] A financial table answers most user questions. How would you ingest it, and when is per-page VLM parsing worth the cost?
- [RAG02-050] How do you extract and retrieve information from complex PDF tables?
- [RAG02-051] How do you make tables and charts in documents retrievable and answerable in a RAG system?
- [RAG02-052] Should figures be handled by VLM captioning or by multimodal embeddings, and what are the tradeoffs?
- [RAG02-053] How do you handle structured data such as tables and SQL databases in a RAG pipeline?
- [RAG02-054] How would you chunk source code differently from prose, and how does retrieval over a codebase differ?
- [RAG02-055] When indexing a codebase with fixed 512-token splits, "where is parseConfig defined?" returns fragments. What is the best fix?
- [RAG02-056] How would you chunk meeting transcripts or chat logs where meaning spans many short messages?
- [RAG02-057] How do you handle a 400-message Slack thread that resolves an incident: one chunk, many chunks or a summary chunk?
- [RAG02-058] How would you chunk and embed heterogeneous enterprise content such as Slack threads, Jira tickets, Google Docs and PDFs?

## Document parsing, layout and OCR
- [RAG02-059] How does a RAG knowledge base parse and extract content from PDF, Word and HTML, and how do you handle each format?
- [RAG02-060] What data acquisition and parsing steps are needed before indexing enterprise documents?
- [RAG02-061] What are the common failure modes of PDF text extraction (multi-column layouts, headers and footers, hyphenation, ligatures)?
- [RAG02-062] How do you recover reading order and logical structure from complex layouts?
- [RAG02-063] Your RAG system struggles with PDFs containing tables and complex layouts. How do you fix the parsing?
- [RAG02-064] What breaks in a RAG pipeline when a document is a scanned PDF rather than a native one?
- [RAG02-065] How do you tell automatically whether a PDF is born-digital or scanned?
- [RAG02-066] Your corpus is mostly scanned PDFs with tables, recall is poor and numeric facts come out garbled. Where do you look first?
- [RAG02-067] How do OCR errors hurt dense and BM25 retrieval, and how do you mitigate them?
- [RAG02-068] How would you handle low-quality scans and handwriting in an ingestion pipeline?
- [RAG02-069] Why would you still use Textract, Azure Document Intelligence or classic OCR engines when vision LLMs can read pages?
- [RAG02-070] When is OCR plus vision-model parsing worth the cost?
- [RAG02-071] How do you process a 500-page PDF with vision models efficiently?
- [RAG02-072] When do you choose rule-based parsers, layout-detection models or an end-to-end VLM for a given document type?
- [RAG02-073] How would you route pages to the cheapest parsing tier that still works?
- [RAG02-074] You must parse 5M pages a month of mixed born-digital and scanned files. Frontier VLM, specialist API or self-hosted model, and what cost controls?
- [RAG02-075] What is the best method to digitize and chunk complex documents like annual reports?
- [RAG02-076] Parsing PDFs, HTML, spreadsheets, email and scans at scale: what breaks and how do you build for it?
- [RAG02-077] A customer's documents are scanned PDFs, Excel exports with merged cells and an old SharePoint, but the pilot assumed clean text. What do you do?
- [RAG02-078] Everyone focuses on retrieval algorithms. What is actually the hardest part of building RAG over enterprise documents?

## Metadata, deduplication and governance
- [RAG02-079] What metadata would you attach to each chunk, and what does it buy you?
- [RAG02-080] Which chunk metadata would you embed into the chunk text and which would you keep as filterable fields, and why?
- [RAG02-081] What provenance fields (document ID, page, offsets, bounding box) do you store to support citations?
- [RAG02-082] How do you extract metadata such as dates, authors and document types at ingestion, and what do you do when it is missing or wrong?
- [RAG02-083] How does storing the embedding model version in chunk metadata help during a model migration?
- [RAG02-084] Your corpus is full of near-duplicates: document versions, boilerplate, quoted email threads. How do you deduplicate?
- [RAG02-085] How do you dedupe identical chunks before embedding, and how much does that save on real corpora?
- [RAG02-086] Why does deduplication matter more for an AI corpus than for a warehouse, and how do you do it at scale?
- [RAG02-087] Can you dedupe two near-duplicate documents that have different ACLs?
- [RAG02-088] How do you tune the similarity threshold for near-duplicate detection without labels?
- [RAG02-089] How do you handle mixed-permission documents during chunking so access control still holds?
- [RAG02-090] How do you handle PII, consent and governance during ingestion for RAG or fine-tuning?
- [RAG02-091] How do you propagate document deletions or right-to-be-forgotten requests to chunks and vectors?

## Ingestion pipeline design
- [RAG02-092] How do you build a production-grade document processing and indexing pipeline?
- [RAG02-093] Design the ingestion pipeline that gets 5 million internal documents into a RAG system.
- [RAG02-094] How do you handle document updates and version management in a RAG knowledge base?
- [RAG02-095] How do you make ingestion incremental and idempotent, for example with content hashing?
- [RAG02-096] How do you handle poison documents, retries and dead-letter queues in a large ingestion run?
- [RAG02-097] Why keep raw files and parsed intermediates in storage in addition to the final chunks?
- [RAG02-098] When would you choose streaming over batch ingestion for a RAG index?
- [RAG02-099] Estimate the time and embedding cost to ingest 5M documents, and say where you would optimize.
- [RAG02-100] You need to change chunk size and the contextualization prompt on a live 1 TB index. What is the safe rollout?
- [RAG02-101] How do you re-process everything when the chunking logic changes without serving old and new chunks together?
- [RAG02-102] How does chunking-logic versioning interact with embedding versioning?

## Evaluating chunking and parsing quality
- [RAG02-103] How do you decide on a chunking strategy, and how do you evaluate whether your chunking is any good?
- [RAG02-104] Many retrieval failures are really chunking failures. How do you recognize them?
- [RAG02-105] How do you build a gold set that compares chunking configurations fairly when chunk boundaries differ between them?
- [RAG02-106] How would you A/B test two chunking strategies?
- [RAG02-107] What test would show that a structure-aware chunker beats fixed 512-token windows?
- [RAG02-108] What metric tells you your chunks are too big?
- [RAG02-109] A RAG answer is wrong. How do you tell whether parsing, chunking, retrieval or generation is to blame?
- [RAG02-110] How do you measure document parsing quality at corpus scale?
- [RAG02-111] How would you detect that a parser silently corrupted documents without reading every page?
- [RAG02-112] Which single automatic signal catches the most parse failures per unit of effort?
- [RAG02-113] When is a flagged page worth re-parsing with a VLM versus dropping from the corpus?
- [RAG02-114] How do you detect that a parser regression shipped when the pipeline still runs green?
- [RAG02-115] How do you evaluate table extraction quality specifically?
