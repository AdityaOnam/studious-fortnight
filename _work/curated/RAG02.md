## Chunking fundamentals
- [E] Why do we chunk documents in a RAG system, and how does chunking affect answer quality? {Q004281,Q007127,Q011065,Q012424}
- [E] What are the most common chunking methods used in RAG? {Q003426,Q007129}
- [E] What is the purpose of overlap between chunks, and what does it cost you? {Q003454}
- [E] Why not embed whole documents with a long-context embedding model instead of chunking them? {GEN}
- [M] What factors influence the right chunk size for a RAG system, and how do you find a good value for your corpus? {Q003413,Q007128,Q007130,Q011161,D00335}
- [M] Explain the intuition behind chunk size using a concrete example. {Q004282}
- [M] What are the consequences of chunks that are too large versus chunks that are too small? {Q003414}
- [M] How do chunk size and overlap affect retrieval recall and answer quality, and what numbers would you start with? {Q007824,D04831}
- [M] Why does a chunk that covers several topics embed poorly? What is happening in the vector space? {Q007825}
- [M] If you embed each page (about 450 tokens) as a chunk, what do you do when the needed information spans several pages? {Q004283}
- [M] Your chunk overlap produces redundant results in the top-k. How do you reduce the redundancy? {Q004778}
- [M] How do you align chunking with the tokenizer so that chunks fit the embedding model's input limit? {Q011203,D00358}
- [M] What happens when a chunk exceeds the embedding model's maximum sequence length, and how should the pipeline guard against it? {GEN}
- [M] How would chunking differ for a corpus of tweets versus a corpus of legal contracts? {Q007826}
- [H] A corpus has 10M pages of about 500 tokens each. Estimate the vector count and storage for 512-token chunks with 15% overlap and 768-dim float32 embeddings. {GEN}
- [H] You retrieve top-5 chunks of 800 tokens each into a 4k-token window. How do you rebalance chunk size and top-k? {GEN}

## Chunking strategies
- [M] What chunking strategies do you know, and what criteria do you use to pick one for a given corpus? {Q003427,Q007820,Q010808,Q004752}
- [M] Compare fixed-size, recursive, semantic and structure-aware chunking. {Q004753,D00337,D04832}
- [M] Why is fixed-size chunking with overlap problematic in production systems? {Q011357,D00336}
- [M] Why is the recursive character text splitter a common default, and when should you not use it? {Q006191,D00343}
- [M] When should you use semantic chunking? {Q011066}
- [M] How does semantic chunking decide where to split, and how do you choose the breakpoint threshold? {GEN}
- [M] What do recent studies say about the benefit of semantic chunking over fixed-size chunks, and is its extra cost justified? {D00344}
- [M] How would you chunk Markdown, HTML or heading-structured documents so the section hierarchy stays attached to each chunk? {GEN}
- [M] When would you prefer sentence-level chunks over paragraph- or section-level chunks? {GEN}
- [M] What goes wrong when a splitter cuts mid-sentence or mid-table, and how do you prevent it? {GEN}
- [M] What chunking strategy would you use for a large technical documentation corpus, and why? {Q011814}
- [M] How does chunking differ for structured documents (PDFs with tables and figures) versus plain-text documents? {Q003428}
- [M] What is proposition-based or LLM-driven (agentic) chunking, and what are its cost and consistency tradeoffs? {GEN}
- [M] What chunk enhancement techniques exist in RAG, and what are their pros and cons? {Q003424,Q003425}
- [H] How would you extend a legal-document chunker to handle schedules and exhibits that are effectively separate documents? {Q009688}
- [M] How do you handle list items during chunking? {Q007134}
- [M] Where does chunking need to change when documents mix English and Hindi on the same page? {Q010082}

## Parent-child chunks and context enrichment
- [M] What is parent-child (hierarchical) chunking, and how does it improve retrieval? {Q004776,D00338}
- [M] What are Parent-Document Retrieval and Sentence Window Retrieval, and when do you use each? {Q005956}
- [M] How do you choose child and parent sizes, and how does returning parents change token cost and precision? {GEN}
- [M] When expanding a retrieved chunk with its neighbours, how do you decide how many neighbours to include? {GEN}
- [M] What is Contextual Retrieval, how does it improve RAG, and when would you skip it? {Q004754,Q011358,Q011409,D00340}
- [M] A chunk says "revenue grew 3% over the previous quarter" with no company or quarter, and it never ranks for "ACME Q2 2023 revenue". What is the strongest fix? {Q007027}
- [M] What is late chunking, and how does it differ from contextual retrieval? {D00339,Q007865}
- [M] What cheaper alternatives to LLM-generated context exist, such as prepending titles and section headers, and what do they miss? {GEN}
- [M] What retrieval failures does contextual retrieval not fix? {GEN}
- [H] A 50,000-document knowledge base needs Contextual Retrieval. How do you manage the ingestion cost? {Q011410,D00341}
- [H] How does prompt caching make contextual retrieval affordable at 10M chunks? Sketch the cost math. {Q007866a}

## Tables, code, figures and heterogeneous content
- [M] How do you handle tables during chunking? {Q007132}
- [M] What breaks when you chunk a table row by row, and how do you keep headers attached when a table spans pages? {Q007822,GEN}
- [M] How do you chunk and index a 500-row table or other very large table for better retrieval? {Q007133,Q010356}
- [M] Would you embed a table as Markdown, HTML or a natural-language summary, and what are the tradeoffs? {GEN}
- [H] A financial table answers most user questions. How would you ingest it, and when is per-page VLM parsing worth the cost? {Q007864}
- [M] How do you extract and retrieve information from complex PDF tables? {D00347}
- [M] How do you make tables and charts in documents retrievable and answerable in a RAG system? {Q007912,Q007136,Q010820}
- [M] Should figures be handled by VLM captioning or by multimodal embeddings, and what are the tradeoffs? {GEN}
- [M] How do you handle structured data such as tables and SQL databases in a RAG pipeline? {Q004766}
- [M] How would you chunk source code differently from prose, and how does retrieval over a codebase differ? {Q007821,Q007927,D00342}
- [M] When indexing a codebase with fixed 512-token splits, "where is parseConfig defined?" returns fragments. What is the best fix? {Q007031}
- [M] How would you chunk meeting transcripts or chat logs where meaning spans many short messages? {GEN}
- [M] How do you handle a 400-message Slack thread that resolves an incident: one chunk, many chunks or a summary chunk? {Q009586}
- [H] How would you chunk and embed heterogeneous enterprise content such as Slack threads, Jira tickets, Google Docs and PDFs? {Q012108,Q009585}

## Document parsing, layout and OCR
- [M] How does a RAG knowledge base parse and extract content from PDF, Word and HTML, and how do you handle each format? {Q006237,D00346}
- [M] What data acquisition and parsing steps are needed before indexing enterprise documents? {D04830}
- [M] What are the common failure modes of PDF text extraction (multi-column layouts, headers and footers, hyphenation, ligatures)? {GEN}
- [M] How do you recover reading order and logical structure from complex layouts? {D00352}
- [M] Your RAG system struggles with PDFs containing tables and complex layouts. How do you fix the parsing? {Q004788,Q011823,D04965}
- [M] What breaks in a RAG pipeline when a document is a scanned PDF rather than a native one? {Q009675}
- [M] How do you tell automatically whether a PDF is born-digital or scanned? {GEN}
- [M] Your corpus is mostly scanned PDFs with tables, recall is poor and numeric facts come out garbled. Where do you look first? {Q007032}
- [M] How do OCR errors hurt dense and BM25 retrieval, and how do you mitigate them? {GEN}
- [M] How would you handle low-quality scans and handwriting in an ingestion pipeline? {D00353}
- [M] Why would you still use Textract, Azure Document Intelligence or classic OCR engines when vision LLMs can read pages? {Q011587,D00348}
- [M] When is OCR plus vision-model parsing worth the cost? {Q010375}
- [M] How do you process a 500-page PDF with vision models efficiently? {Q011588,D00351}
- [M] When do you choose rule-based parsers, layout-detection models or an end-to-end VLM for a given document type? {GEN}
- [M] How would you route pages to the cheapest parsing tier that still works? {D00349}
- [H] You must parse 5M pages a month of mixed born-digital and scanned files. Frontier VLM, specialist API or self-hosted model, and what cost controls? {Q011439,Q011589,D00350}
- [H] What is the best method to digitize and chunk complex documents like annual reports? {Q007131}
- [H] Parsing PDFs, HTML, spreadsheets, email and scans at scale: what breaks and how do you build for it? {Q010373}
- [H] A customer's documents are scanned PDFs, Excel exports with merged cells and an old SharePoint, but the pilot assumed clean text. What do you do? {Q010456}
- [M] Everyone focuses on retrieval algorithms. What is actually the hardest part of building RAG over enterprise documents? {Q007862}

## Metadata, deduplication and governance
- [E] What metadata would you attach to each chunk, and what does it buy you? {Q007856,D04966}
- [M] Which chunk metadata would you embed into the chunk text and which would you keep as filterable fields, and why? {Q007857}
- [M] What provenance fields (document ID, page, offsets, bounding box) do you store to support citations? {GEN}
- [M] How do you extract metadata such as dates, authors and document types at ingestion, and what do you do when it is missing or wrong? {GEN}
- [M] How does storing the embedding model version in chunk metadata help during a model migration? {Q007858}
- [M] Your corpus is full of near-duplicates: document versions, boilerplate, quoted email threads. How do you deduplicate? {Q007921}
- [M] How do you dedupe identical chunks before embedding, and how much does that save on real corpora? {Q010017}
- [M] Why does deduplication matter more for an AI corpus than for a warehouse, and how do you do it at scale? {Q010357,D00354}
- [H] Can you dedupe two near-duplicate documents that have different ACLs? {Q010358}
- [H] How do you tune the similarity threshold for near-duplicate detection without labels? {Q010359}
- [M] How do you handle mixed-permission documents during chunking so access control still holds? {D00357}
- [M] How do you handle PII, consent and governance during ingestion for RAG or fine-tuning? {D00355}
- [M] How do you propagate document deletions or right-to-be-forgotten requests to chunks and vectors? {GEN}

## Ingestion pipeline design
- [H] How do you build a production-grade document processing and indexing pipeline? {Q007135}
- [H] Design the ingestion pipeline that gets 5 million internal documents into a RAG system. {Q010347}
- [M] How do you handle document updates and version management in a RAG knowledge base? {D00356}
- [M] How do you make ingestion incremental and idempotent, for example with content hashing? {GEN}
- [M] How do you handle poison documents, retries and dead-letter queues in a large ingestion run? {GEN}
- [M] Why keep raw files and parsed intermediates in storage in addition to the final chunks? {GEN}
- [M] When would you choose streaming over batch ingestion for a RAG index? {GEN}
- [H] Estimate the time and embedding cost to ingest 5M documents, and say where you would optimize. {GEN}
- [H] You need to change chunk size and the contextualization prompt on a live 1 TB index. What is the safe rollout? {Q007029}
- [H] How do you re-process everything when the chunking logic changes without serving old and new chunks together? {Q010348}
- [H] How does chunking-logic versioning interact with embedding versioning? {Q010353}

## Evaluating chunking and parsing quality
- [M] How do you decide on a chunking strategy, and how do you evaluate whether your chunking is any good? {Q010354,Q004284}
- [M] Many retrieval failures are really chunking failures. How do you recognize them? {D00345}
- [M] How do you build a gold set that compares chunking configurations fairly when chunk boundaries differ between them? {GEN}
- [M] How would you A/B test two chunking strategies? {Q007823}
- [M] What test would show that a structure-aware chunker beats fixed 512-token windows? {Q009689}
- [M] What metric tells you your chunks are too big? {Q007827}
- [M] A RAG answer is wrong. How do you tell whether parsing, chunking, retrieval or generation is to blame? {GEN}
- [M] How do you measure document parsing quality at corpus scale? {Q007863}
- [M] How would you detect that a parser silently corrupted documents without reading every page? {Q007853}
- [M] Which single automatic signal catches the most parse failures per unit of effort? {Q007854}
- [M] When is a flagged page worth re-parsing with a VLM versus dropping from the corpus? {Q007855}
- [H] How do you detect that a parser regression shipped when the pipeline still runs green? {Q010374}
- [M] How do you evaluate table extraction quality specifically? {Q007914}
