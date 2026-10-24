---
domain: rag
topic: rag_evaluation_and_failure_modes
title: RAG evaluation and failure modes
tags: [rag-eval, ragas, failure-modes]
count: 205
---
# RAG evaluation and failure modes

## Evaluation fundamentals and frameworks
- [RAG06-001] What is the RAG triad, and which failures does each dimension expose? How does an LLM judge fit into it?
- [RAG06-002] Why is reading a handful of sample answers not an adequate way to evaluate a RAG system?
- [RAG06-003] How do you evaluate a RAG system end to end while separating retrieval quality from generation quality?
- [RAG06-004] Why evaluate the retriever and the generator separately instead of only measuring end-to-end answer quality?
- [RAG06-005] How do you evaluate the retriever, the reranker and the generator as separate components?
- [RAG06-006] What are the four core RAGAS metrics, what does each measure, and how would you optimize each one?
- [RAG06-007] How do RAGAS, TruLens, DeepEval and UpTrain compare, and when would you pick each?
- [RAG06-008] What is the difference between offline and online evaluation of a RAG system, and what does each one catch?
- [RAG06-009] When do you need end-to-end answer-quality evals, and when are retrieval-only evals enough?
- [RAG06-010] Where does a typical RAG system lose the most quality, in retrieval or in generation, and how would you find out for yours?
- [RAG06-011] How do you test a RAG question-answering system, and where do you draw the test boundaries between ingestion, retrieval and generation?
- [RAG06-012] Describe a full RAG evaluation lifecycle, from offline metrics through iterative optimization to production monitoring.
- [RAG06-013] "It works in the demo": how do you know a RAG system is production-ready?
- [RAG06-014] How do you set up regression gates in CI so a pipeline change cannot silently degrade RAG quality?

## Retrieval metrics: precision, recall and relevancy
- [RAG06-015] What does context precision measure in a RAG retriever, and how does it differ from context recall?
- [RAG06-016] What is the difference between hit rate, MRR and nDCG, and when would you prefer each for judging a RAG retriever?
- [RAG06-017] Which retrieval metrics such as recall@k, precision@k, MRR and nDCG would you track, and how do they relate to end-to-end answer quality?
- [RAG06-018] How does Context Precision@K differ from standard precision@k in classical information retrieval?
- [RAG06-019] Why does Context Precision@K use a weighted sum with relevance indicators, and how does that reflect retriever ranking quality?
- [RAG06-020] Relevant chunks appear at positions 2, 4, 6 and 8 out of 10 retrieved. Compute Context Precision@10 and say what it tells you about the ranking.
- [RAG06-021] A RAG system achieves Context Precision@5 = 0.8. What scenarios could produce that score?
- [RAG06-022] How does Context Recall differ from classic IR recall, and why is it computed over ground-truth claims rather than counted documents?
- [RAG06-023] If a retriever has high context precision but low context recall, which kinds of user queries suffer most?
- [RAG06-024] When would you prioritize context precision over context recall, and how does that affect the generator?
- [RAG06-025] If context recall is consistently below 0.6, what are the likely root causes?
- [RAG06-026] Why optimize context precision and recall together, and what trade-offs appear when you push on one?
- [RAG06-027] Why is Context Relevancy reference-free while Context Precision and Recall need references, and when would you prefer it?
- [RAG06-028] Describe a case where a retriever has high Context Relevancy but low Context Precision. What does it imply?
- [RAG06-029] A retriever finds all relevant chunks but also many irrelevant ones, giving low context relevancy. How would you fix it?
- [RAG06-030] How would you measure the marginal value of each additional retrieved chunk to answer quality, and use it to choose k?
- [RAG06-031] Why might recall@5 matter more than recall@20 even though your context window fits 20 chunks?
- [RAG06-032] Recall@100 is 95% but recall@5 after reranking is 60%. Where is the bug?
- [RAG06-033] Recall@10 is 95% but end-to-end correctness is 70%. Where do you look?
- [RAG06-034] Recall@5 improved but end-to-end answer quality dropped. What could have happened?
- [RAG06-035] Your new embedder improves nDCG but end-to-end RAG answers get worse. What mechanisms could explain that?
- [RAG06-036] How do retrieval metrics mislead when your golden set has incomplete relevance labels?

## Faithfulness, groundedness and citations
- [RAG06-037] How does the Faithfulness metric assess the quality of a RAG generator, and how does RAGAS compute it under the hood?
- [RAG06-038] How does RAGAS context precision work under the hood?
- [RAG06-039] What is the difference between faithfulness (grounded in the retrieved context) and factual correctness (true in the world)? Give an example where they diverge.
- [RAG06-040] How does Response Relevancy differ from Context Relevancy, and why do you need both?
- [RAG06-041] How does the Response Relevancy metric tell you whether the generator addressed the user's query?
- [RAG06-042] What are the risks of relying solely on response relevancy, and how does adding faithfulness help?
- [RAG06-043] Why might a system have high Context Precision but low Faithfulness, and what would that say about the pipeline?
- [RAG06-044] How do LLM hallucinations lower the Faithfulness score, and what techniques would raise it?
- [RAG06-045] How do you measure whether an answer is grounded in the retrieved context, and automate it?
- [RAG06-046] How would you cheaply monitor faithfulness on live traffic where there is no reference answer?
- [RAG06-047] How would you break an answer into atomic claims for faithfulness scoring, and what goes wrong when the decomposition is poor?
- [RAG06-048] When measuring faithfulness, a claim is supported by chunk A but contradicted by chunk B in the same context. What should the metric do?
- [RAG06-049] Your RAG system's faithfulness score is high but users say the answers are wrong. What is happening?
- [RAG06-050] The security team forbids sending data to any external LLM judge. How do you evaluate the faithfulness of a document Q&A system?
- [RAG06-051] How would you turn per-claim citations into an automated groundedness metric?
- [RAG06-052] How do you catch a correct claim that has the wrong citation attached?
- [RAG06-053] Design a citation-verification system so every claim in a generated answer is supported by its cited source.
- [RAG06-054] A generated sentence synthesizes facts from three sources. How does per-claim citation verification handle multi-source composition?
- [RAG06-055] How do you handle a correct synthesis that no single cited passage supports?
- [RAG06-056] What are the latency and cost of per-claim entailment checking, and how would you reduce them?
- [RAG06-057] What is your latency budget for citation verification, and would you run it inline or stream the answer and revise afterwards?
- [RAG06-058] What is your fallback when the citation verifier and the generator disagree at serving time?

## Golden sets, LLM judges and evaluation pipelines
- [RAG06-059] How do you build a golden evaluation set for RAG without months of labelling?
- [RAG06-060] How do you build the first golden set for a RAG product that has not launched and has no logs?
- [RAG06-061] How do you build a golden test set for RAG, including synthetic query generation?
- [RAG06-062] How do you stratify a golden set by query type, difficulty, multi-hop and unanswerable cases so aggregate scores do not hide regressions?
- [RAG06-063] You build a golden set by having an LLM write Q&A from chunks you hand-picked. Offline recall is 0.91 but production recall is 0.40. What went wrong?
- [RAG06-064] Why do synthetic queries overestimate retrieval quality, and how exactly do you counter it?
- [RAG06-065] A chunking change invalidated all chunk-ID labels in your golden set. How should the golden set have been designed?
- [RAG06-066] How big must an evaluation set be to detect a 5-point recall difference, and how do you test significance when comparing two configurations?
- [RAG06-067] How do you keep the golden set from being overfit as engineers tune against it?
- [RAG06-068] How do you detect eval-set staleness as the document corpus grows?
- [RAG06-069] How do you keep the retrieval eval honest when the corpus updates weekly?
- [RAG06-070] How do you validate an LLM judge against human raters, and what agreement is good enough?
- [RAG06-071] Your LLM judge and your human labels agree only 70% of the time. What do you do?
- [RAG06-072] What biases do LLM judges have (position, verbosity, self-preference), and how do they distort RAG evaluation?
- [RAG06-073] How do you evaluate a RAG system when you do not have ground-truth answers?
- [RAG06-074] Your RAG evaluation pipeline costs $500/day in LLM judge calls. How do you reduce it?
- [RAG06-075] How do you build a BM25 baseline and synthetic queries to quantify retrieval quality before tuning embeddings?
- [RAG06-076] How do you evaluate that a chunker, parser or embedding-model change made retrieval better, not just different?
- [RAG06-077] Your golden set says the new chunker is better but users complain answers got worse. What is your hypothesis list?
- [RAG06-078] How do you measure whether ingestion quality is hurting RAG answers, versus retrieval or generation?
- [RAG06-079] Design a retrieval evaluation harness the team will actually use. What runs, when, and what blocks a merge?
- [RAG06-080] You have thumbs-up/down and click logs from a live RAG product. How do you turn them into retrieval improvements?
- [RAG06-081] How would you avoid a feedback loop where the ranker only ever learns from documents it already ranks highly?
- [RAG06-082] An enterprise customer wants to deploy your RAG system but has no labelled data. How do you evaluate it before and after launch?

## Evaluating special RAG settings
- [RAG06-083] How do you evaluate retrieval separately from generation for a code-editing assistant?
- [RAG06-084] How would you evaluate a RAG chatbot in multi-turn conversations where follow-up questions depend on history?
- [RAG06-085] How do you evaluate an agentic RAG system when every run takes a different trajectory?
- [RAG06-086] How would you design the evaluation that decides whether the dense retrieval leg stays in an agentic search setup?
- [RAG06-087] How do you check that chart-dependent questions in a multimodal RAG system are really answered from the chart?
- [RAG06-088] How would you evaluate answer quality for an answer engine continuously and at scale, with automated and human signals?
- [RAG06-089] How would you evaluate multilingual retrieval when employees query in French and Korean over mostly-English documents?
- [RAG06-090] How do you gather realistic non-English queries before launching a multilingual retrieval system?
- [RAG06-091] How would you build an evaluation set for cross-lingual retrieval without native speakers for every language?
- [RAG06-092] Design the evaluation framework for an enterprise AI assistant when you cannot look at customer data.
- [RAG06-093] A research agent returns a memo citing an authority that has since been overruled. Where should that be caught?

## Hallucination and abstention
- [RAG06-094] How does RAG help reduce hallucinations in LLMs?
- [RAG06-095] What is the difference between intrinsic and extrinsic hallucination in a RAG answer?
- [RAG06-096] Your RAG system hallucinates even though the retrieved context contains the answer. How do you fix it?
- [RAG06-097] Why can telling the model to "only use the context" fail to stop hallucinations, and what else can you do?
- [RAG06-098] Your search results are relevant but the LLM ignores them and answers from its training data. How do you fix this?
- [RAG06-099] What is the "lost in the middle" problem in RAG?
- [RAG06-100] How do you mitigate hallucinations caused by poorly ordered retrieved chunks in production?
- [RAG06-101] How does adding more retrieved chunks affect hallucination and faithfulness, and how do you find the right amount?
- [RAG06-102] Retrieval returns irrelevant documents but the LLM still produces a plausible-sounding answer. How do you detect and prevent that?
- [RAG06-103] How do you prevent hallucination in a production RAG system?
- [RAG06-104] How do you detect and measure hallucinations in a production RAG system?
- [RAG06-105] Design a hallucination eval for a RAG product. What is the metric?
- [RAG06-106] How do you prevent hallucinated numbers in a financial RAG assistant?
- [RAG06-107] An enterprise customer says their RAG knowledge assistant hallucinates too much. What do you do in the first 48 hours?
- [RAG06-108] A customer demands "zero hallucinations" in the contract. How do you respond?
- [RAG06-109] Your QA system always produces an answer even when none exists in the context. How do you detect unanswerable questions?
- [RAG06-110] How do you handle the case where retrieval returns no results?
- [RAG06-111] How do you handle queries where all 50 retrieved candidates are bad?
- [RAG06-112] How do you stop the model from answering from parametric memory when retrieval returns nothing relevant?
- [RAG06-113] Your assistant must say "I don't know" when the corpus lacks the answer. How do you decide when to abstain and set the threshold?
- [RAG06-114] When the answer is not in the knowledge base at all, what should the agent do, and how do you detect this class of query at scale?
- [RAG06-115] How would you build near-miss unanswerable questions for evaluation without contaminating the corpus?
- [RAG06-116] The assistant's abstain rate doubled overnight with no deploy. What are your first three checks?
- [RAG06-117] Your enterprise RAG system returns contradictory answers from different source documents. How do you resolve the conflicts?
- [RAG06-118] An agent answers from a customer knowledge base with outdated and contradictory articles. How do you prevent confidently wrong answers?

## Debugging poor RAG answers
- [RAG06-119] What are the common failure modes of production RAG systems, and how do you debug them?
- [RAG06-120] Which three production failure modes would you build detection for first on a new system?
- [RAG06-121] Describe your approach to debugging a poor-performing RAG system. Where do you look first?
- [RAG06-122] What are the possible reasons a RAG retriever performs poorly, and what are the common challenges in RAG retrieval?
- [RAG06-123] What symptoms show that a weak retriever is the bottleneck in a RAG system?
- [RAG06-124] What symptoms show that a weak generator LLM is the bottleneck even when retrieval is good?
- [RAG06-125] Users report that answers are sometimes wrong. How do you systematically diagnose and fix the system?
- [RAG06-126] Users complain a RAG chatbot gives confident but wrong answers. How do you find whether retrieval or generation is at fault?
- [RAG06-127] When the gold document is missing from the top-k, how do you tell a parsing or chunking failure from an embedding failure or a ranking failure?
- [RAG06-128] Which failure taxonomy would you use to classify RAG errors during error analysis?
- [RAG06-129] How do you run error analysis on a RAG system using open coding and axial coding?
- [RAG06-130] How do you decide whether to fix a bad answer with a prompt change, a retrieval change or a data change?
- [RAG06-131] How do you decide whether a single bad answer warrants a pipeline change?
- [RAG06-132] In a RAG system the gold chunk was retrieved at rank 3 and the model still ignored it. What are the top three hypotheses?
- [RAG06-133] Your RAG system works well on test data but fails in production. What do you check?
- [RAG06-134] A client's RAG system gives inaccurate answers and you find retrieval is the problem. What steps do you take to improve it?
- [RAG06-135] Two weeks into a RAG project, retrieval hit rate is 55%. What is your triage order?
- [RAG06-136] A pilot RAG system gives wrong answers on a customer's contracts. How do you debug it?
- [RAG06-137] Retrieval hit rate is fine but users still distrust the RAG system. What do you look at?
- [RAG06-138] Your vector search returns irrelevant results despite high similarity scores. How do you fix it?
- [RAG06-139] Your RAG system returns duplicate or near-duplicate results. How do you deduplicate?
- [RAG06-140] How would you detect hubness in a production RAG system?
- [RAG06-141] After a customer 10x'd their indexed documents, retrieval quality dropped even though ANN recall is fine and gold documents are in the top-100 but not the top-5. What next?
- [RAG06-142] Answers to the same query differ across runs. How do you handle non-determinism when debugging and evaluating RAG?

## Freshness, versioning and index maintenance
- [RAG06-143] How do you keep a RAG index fresh as source documents are updated or deleted?
- [RAG06-144] How do you handle stale data and freshness requirements in a real-time RAG system?
- [RAG06-145] Which data in a typical enterprise should bypass the RAG index entirely and be fetched live?
- [RAG06-146] How do you manage versioning when the knowledge base is updated frequently?
- [RAG06-147] Users report the assistant confidently cites a policy that was revised last month. What production gap does this reveal?
- [RAG06-148] Latency, throughput and individual retrievals look healthy, but users say answers are subtly out of date and dashboards are green. What is the likely failure and how would you have caught it?
- [RAG06-149] How do you handle time-sensitive queries such as "latest" or "current" when older documents outrank newer ones?
- [RAG06-150] How do you use document timestamps and version metadata in ranking and in the prompt to avoid answering from a superseded document?
- [RAG06-151] What is the re-indexing story for contextual retrieval when documents are edited?
- [RAG06-152] In a RAG index, a document's chunk count changes between versions. Walk through the failure and your fix.
- [RAG06-153] How do you verify that deletions have actually propagated to every index, cache and derived artifact?
- [RAG06-154] A source system's webhook was down for six hours. How do you detect and heal the gap in the vector index?
- [RAG06-155] A document must be removed for legal or privacy reasons. How do you guarantee it can no longer surface in answers?
- [RAG06-156] What is embedding drift in a RAG system, and how do you detect and mitigate it?
- [RAG06-157] How do you detect retrieval quality drift and index drift after launch?
- [RAG06-158] How would you continuously evaluate the freshness quality of an answer engine?

## Security, access control and multi-tenancy
- [RAG06-159] Why does RAG turn every ingested document into an attack surface?
- [RAG06-160] How does prompt injection via retrieved documents work, and what actually mitigates it?
- [RAG06-161] What changes when an attacker controls a document in your RAG index?
- [RAG06-162] Should retrieved text be treated as data or as instructions, and how do you structure prompts and tooling to reflect that?
- [RAG06-163] What is context poisoning, and how can a RAG knowledge base defend against it?
- [RAG06-164] Someone floods public sources with fake posts to steer your RAG answers. What stops it?
- [RAG06-165] How would you red-team a RAG application for indirect prompt injection and measure the attack success rate?
- [RAG06-166] Your guardrail blocks jailbreaks in the user prompt, but injecting documents into its context flips its judgments, and retrieved chunks are exactly such documents. What is the lesson?
- [RAG06-167] How can a RAG answer leak data through rendered markdown images or links, and how do you prevent it?
- [RAG06-168] What are the security weaknesses specific to vector stores and embeddings, and how do you mitigate them?
- [RAG06-169] What are the main structural risks enterprise RAG faces, and how do you build a production-grade defense?
- [RAG06-170] How do you prevent personally identifiable information in indexed documents from leaking through answers?
- [RAG06-171] Where in a RAG system should per-user document permissions be enforced, and why must it be there?
- [RAG06-172] Why is post-filtering retrieved results by permission a correctness problem and not just a performance one?
- [RAG06-173] How would you enforce per-user access control at retrieval time without rebuilding the index per user?
- [RAG06-174] Design permission-aware retrieval so users never see content they cannot access in the source system.
- [RAG06-175] How would you handle a document whose permissions change after it has been embedded and indexed?
- [RAG06-176] A junior employee got an answer citing a restricted compensation document from a shared HR and finance index. What is the root cause and fix?
- [RAG06-177] A customer sees an answer referencing a document they cannot access. Which cache do you suspect and why?
- [RAG06-178] A summary generated last month cites a document the user has since lost access to. What happens?
- [RAG06-179] A mixed question needs a warehouse figure and a reason from a ticket the user may not be allowed to see. Where is access enforced on each path?
- [RAG06-180] A multi-tenant RAG system returns correct answers in testing. What is the highest-priority production risk to design against?
- [RAG06-181] How do you implement multi-tenant isolation in a RAG system?
- [RAG06-182] What failure modes arise when one RAG system serves multiple tenants, and which tenant leaks does a metadata filter fail to stop?
- [RAG06-183] How do you continuously test for permission leaks in an access-controlled RAG system, not just at design time?

## Production monitoring, latency and cost
- [RAG06-184] Which production signals and alerts would you set up for a RAG system?
- [RAG06-185] What SLOs would you define for a RAG service across quality, latency and freshness, and how would you measure them?
- [RAG06-186] What monitoring would have caught a retrieval-quality drop after a 10x growth in indexed documents before the customer did?
- [RAG06-187] What must be in your traces to make triaging a wrong RAG answer take minutes, not hours?
- [RAG06-188] How do you sample production traffic for human review of RAG answers?
- [RAG06-189] How do you reduce latency in a production RAG system?
- [RAG06-190] A production RAG system responds slowly. How do you troubleshoot it systematically?
- [RAG06-191] Give a latency budget for a RAG request across embedding, retrieval, reranking and generation, and say where the biggest wins are.
- [RAG06-192] Your RAG costs tripled over a month with no increase in query volume. How do you diagnose and fix it?
- [RAG06-193] Estimate the cost per query of a RAG pipeline that sends 8 chunks of 500 tokens to an LLM, and the extra cost of an LLM judge sampling 5% of traffic.
- [RAG06-194] What quality risks does semantic caching introduce in RAG, such as stale or wrong answers, and how do you limit them?
- [RAG06-195] What is self-healing RAG, and how do you implement self-detection and automatic recovery in production?
- [RAG06-196] How do you run canary releases and rollbacks for changes to the retrieval strategy?
- [RAG06-197] You are swapping embedding vendors and offline RAGAS scores improve. What is the safest way to ship?
- [RAG06-198] Changing the embedding model improves some queries and hurts others. How do you manage this see-saw effect?

## Additional questions
- [RAG06-199] Why might a RAG system with perfect Context Recall still fail to produce accurate responses? How does the Faithfulness metric help diagnose this issue?
- [RAG06-200] Describe a scenario where a RAG system might achieve high Context Recall but still produce poor answers. What complementary metrics would you use alongside Context Recall to get a complete picture of retriever performance?
- [RAG06-201] How do you evaluate a RAG system? Explain faithfulness, relevance, and context precision/recall.
- [RAG06-202] How do you evaluate text-to-SQL when many different queries return the same correct result?
- [RAG06-203] How do you evaluate the generation side of RAG: faithfulness, relevance, and citation quality?
- [RAG06-204] How would you evaluate a validity check (for example, checking whether cited cases are still good law) in a legal research agent?
- [RAG06-205] In a legal research agent that checks citation validity, what do you do in a jurisdiction where you have no citator coverage?
