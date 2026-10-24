---
domain: dl
topic: classic_nlp_embeddings
title: Classic NLP and word embeddings
tags: [nlp, word2vec, tfidf, bert]
count: 120
---
# Classic NLP and word embeddings

## NLP basics and text preprocessing
- [DL06-001] What is Natural Language Processing, and what makes it harder than working with structured tabular data?
- [DL06-002] What do the terms corpus, tokenization and stopwords mean in NLP?
- [DL06-003] What is the difference between stemming and lemmatization, and when would you use one over the other?
- [DL06-004] What are the main types of linguistic ambiguity, and why do they make NLP difficult?
- [DL06-005] How do morphology and syntax differ, and which NLP tasks depend on each?
- [DL06-006] What are the first steps you would take to clean and prepare a raw text corpus before applying an NLP algorithm?
- [DL06-007] Why can stemming produce non-words, and what are over-stemming and under-stemming?
- [DL06-008] When can lowercasing or stopword removal hurt model performance, for example in sentiment or NER?
- [DL06-009] How would you preprocess noisy user-generated text such as tweets with emojis, hashtags, misspellings and slang?
- [DL06-010] What does Zipf's law say about word frequencies, and how does it affect vocabulary building and sparsity?
- [DL06-011] How would you preprocess text for a transformer model, including normalization, pre-tokenization and special tokens?

## Syntactic and semantic analysis: POS, parsing, NER
- [DL06-012] Why is Part-of-Speech tagging significant in NLP, and which downstream tasks use it?
- [DL06-013] What makes POS tagging hard, and how do dictionary-lookup taggers differ from statistical taggers?
- [DL06-014] What approach would you use for part-of-speech tagging?
- [DL06-015] What is a named entity, and how is Named Entity Recognition useful in downstream NLP tasks?
- [DL06-016] What is the difference between constituency parsing and dependency parsing, and what downstream tasks use each?
- [DL06-017] What is dependency parsing, how does a dependency parser work, and what information does it provide?
- [DL06-018] How has deep learning changed syntactic parsing compared with grammar-rule-based approaches?
- [DL06-019] What is the difference between transition-based and graph-based dependency parsing?
- [DL06-020] How would you tag entities in text with nested or overlapping mentions, and what does the BIO scheme fail to handle?
- [DL06-021] How do you evaluate an NER system, and why is entity-level F1 preferred over token-level accuracy?
- [DL06-022] How does entity linking differ from NER, and what makes it difficult?
- [DL06-023] How would you train a model to decide whether the word "jaguar" in a sentence refers to the animal or the car?
- [DL06-024] How would you map nicknames such as Pete, Andy, Nick and Rob to real names?
- [DL06-025] How would you build an NER system for a new domain such as clinical notes when you have very little labeled data?
- [DL06-026] How are Hidden Markov Models applied in NLP tasks?
- [DL06-027] How would an HMM-based POS tagger be trained and decoded, and what independence assumptions does it make?
- [DL06-028] How does an HMM tagger handle words that never appeared in training, and what does this do to emission probabilities?
- [DL06-029] What is the difference between the Viterbi algorithm and the forward algorithm in an HMM?
- [DL06-030] Why is Chinese word segmentation hard, and what are the main sources of ambiguity (granularity, overlapping ambiguity, unseen words)?
- [DL06-031] Compare dictionary-based segmentation (forward and backward maximum matching) with statistical segmentation approaches.
- [DL06-032] How does a DAG with dynamic programming find the max-probability segmentation, and what role does an HMM play for out-of-vocabulary words?
- [DL06-033] Explain how a Viterbi decoder is used with a BMES tagging scheme to segment unseen words.
- [DL06-034] Compare HMMs, MEMMs and CRFs for sequence labeling. What is the label bias problem?
- [DL06-035] Why add a CRF layer on top of a BiLSTM or BERT encoder for NER instead of independent per-token softmax?

## Bag of words, TF-IDF and latent semantic methods
- [DL06-036] What is the bag-of-words model, and what are its limitations?
- [DL06-037] How does TF-IDF measure word importance, and why is the inverse document frequency term logarithmic?
- [DL06-038] What is TF-IDF, and how does it differ from word embeddings?
- [DL06-039] Why is cosine similarity usually preferred over Euclidean distance for comparing TF-IDF vectors?
- [DL06-040] How does BM25 improve on plain TF-IDF for ranking, and what do its parameters k1 and b control?
- [DL06-041] How would you select the most informative features from a very large bag-of-words vocabulary (chi-square, mutual information)?
- [DL06-042] What is Latent Semantic Indexing (LSI), and how does it use SVD to capture semantic similarity?
- [DL06-043] What are the trade-offs between statistical text encoders like TF-IDF and learned encoders like BERT for ranking features?
- [DL06-044] How do LSA and LDA differ as ways of discovering latent structure in a text corpus?

## n-gram language models and perplexity
- [DL06-045] What is an n-gram model, and how does it contribute to language modeling?
- [DL06-046] How does the Markov assumption affect a bigram language model?
- [DL06-047] How does an n-gram language model estimate probabilities, and why does it suffer from sparsity and limited context?
- [DL06-048] What smoothing techniques are used in n-gram models, and what problem do they solve?
- [DL06-049] How do Kneser-Ney smoothing, backoff and interpolation differ, and why does Kneser-Ney work well?
- [DL06-050] What is perplexity, and what is it used for in NLP?
- [DL06-051] What is the perplexity of a model that assigns a uniform distribution over a vocabulary of size V, and what does this tell you about interpreting it?
- [DL06-052] Why can you not directly compare perplexities of two language models that use different vocabularies or tokenizations?
- [DL06-053] Roughly how much memory would a trigram model over a 50,000-word vocabulary need, and how do real systems cope?
- [DL06-054] Compare n-gram models and deep learning language models in terms of trade-offs.
- [DL06-055] What is the entropy of English, and how did early information-theoretic work motivate statistical language modelling?

## Word embeddings fundamentals
- [DL06-056] What are embeddings in machine learning?
- [DL06-057] What are word embeddings, and why are dense vectors preferred over one-hot representations?
- [DL06-058] What are the most common word embedding methods? Explain each briefly.
- [DL06-059] Besides word2vec, what other ways are there to get word embeddings?
- [DL06-060] In what ways is word2vec better than earlier embedding methods such as LSA or neural-network language model embeddings?
- [DL06-061] How would you turn word vectors into a document or sentence representation, and what are the drawbacks of simple averaging?
- [DL06-062] When training a text classifier, when would you freeze pretrained embeddings versus fine-tune them versus train from scratch?
- [DL06-063] How would you evaluate the quality of a set of trained word vectors, intrinsically and extrinsically?
- [DL06-064] Why does the king - man + woman = queen analogy work, and what are its limitations?
- [DL06-065] How can word embeddings encode social biases, and how would you detect or mitigate them?
- [DL06-066] How would you incrementally update a word-embedding model with new domain vocabulary without retraining from scratch?

## word2vec, GloVe and fastText internals
- [DL06-067] Compare CBOW and skip-gram in word2vec. Which works better for rare words and why?
- [DL06-068] Why does word2vec use negative sampling or hierarchical softmax instead of a full softmax over the vocabulary?
- [DL06-069] What is sampled softmax, and how does it differ from negative sampling?
- [DL06-070] What is subsampling of frequent words in word2vec, and what problem does it solve?
- [DL06-071] How does the context window size change what word2vec embeddings capture?
- [DL06-072] Why does word2vec learn two embedding matrices (input and output), and which would you use?
- [DL06-073] How does GloVe differ from word2vec in its training objective and use of co-occurrence statistics?
- [DL06-074] How does fastText use character n-grams, and why does it help with rare words and out-of-vocabulary words?
- [DL06-075] How are negative samples drawn in word2vec, and why is the unigram distribution raised to the 3/4 power?
- [DL06-076] Explain hierarchical softmax: how does a Huffman tree reduce the cost of computing output probabilities?
- [DL06-077] How is skip-gram with negative sampling related to implicit factorization of a shifted PMI matrix?
- [DL06-078] How many parameters does a skip-gram model have for a 1M-word vocabulary and 300 dimensions, and where does the training cost go?

## Contextual embeddings and BERT-era NLP
- [DL06-079] Why are static embeddings such as word2vec unable to handle polysemy, and how did ELMo and BERT address this?
- [DL06-080] Walk through the history of NLP pretraining from word embeddings to ELMo, GPT and BERT. What changed at each step?
- [DL06-081] Compare BERT, OpenAI GPT and ELMo in terms of architecture, directionality and how they are used downstream.
- [DL06-082] Compare CNN, RNN and Transformer as feature extractors for text in terms of long-range dependencies, parallelism and compute.
- [DL06-083] What are the main strategies for obtaining a sentence embedding from a pretrained encoder, and when is each appropriate?
- [DL06-084] What are BERT's pretraining objectives, and why does masked language modeling use the 80/10/10 masking scheme?
- [DL06-085] Why is the raw BERT [CLS] vector often a poor sentence embedding for similarity, and how does Sentence-BERT fix it?
- [DL06-086] How do the fine-tuning heads differ when adapting BERT to classification, NER and span-based QA?
- [DL06-087] How do you align word-level NER labels with WordPiece subword tokens when fine-tuning BERT?
- [DL06-088] How would you apply BERT to documents far longer than its 512-token limit?
- [DL06-089] When would you still choose TF-IDF plus logistic regression over a fine-tuned BERT model in production?

## Text classification and sentiment analysis
- [DL06-090] What is sentiment analysis, and what are its main applications?
- [DL06-091] What approach would you take for a sentiment analysis task?
- [DL06-092] How does the Naive Bayes classifier work for text, and why does it perform well despite its independence assumption?
- [DL06-093] What role do Support Vector Machines play in text classification?
- [DL06-094] When are tree-based models such as Decision Trees and Random Forests a good or poor fit for sparse, high-dimensional text features?
- [DL06-095] How can you use neural networks for text classification?
- [DL06-096] How can CNNs be used for text classification, and what do the filters capture?
- [DL06-097] How do LLMs change sentiment analysis, and when would you prefer a classic classifier or a fine-tuned BERT model over prompting an LLM?
- [DL06-098] How does logistic regression compare with Naive Bayes for text classification?
- [DL06-099] How do negation, sarcasm and domain-specific vocabulary break simple sentiment classifiers?
- [DL06-100] How would you handle severe class imbalance in a text classification task, and which metrics would you report?
- [DL06-101] How does lexicon-based sentiment analysis (such as VADER) compare to a supervised model?
- [DL06-102] A deployed text classifier's accuracy has dropped over several months. How would you diagnose and fix it?
- [DL06-103] How would you build a text classifier with only a few hundred labeled examples?

## Evaluation of generation: BLEU, ROUGE and beyond
- [DL06-104] What are the main metrics for text generation evaluation, and what are their weaknesses (BLEU, ROUGE, BERTScore, human evaluation)?
- [DL06-105] How is BLEU computed, and what do modified n-gram precision and the brevity penalty do?
- [DL06-106] Why does BLEU clip n-gram counts? What would happen for the candidate "the the the the" against the reference "the cat sat"?
- [DL06-107] How do ROUGE-N and ROUGE-L differ, and why is ROUGE considered recall-oriented?
- [DL06-108] How does BERTScore work, and what problems of n-gram overlap metrics does it address?
- [DL06-109] How would you design a human evaluation for generated text, and how would you measure annotator agreement?
- [DL06-110] Why do BLEU scores correlate poorly with human judgments at the sentence level, and what would you use instead for a modern system?

## Applied tasks: summarization, QA and translation
- [DL06-111] What are the main approaches for text summarization?
- [DL06-112] How does extractive summarization with TextRank work?
- [DL06-113] What is the difference between extractive, generative and retrieval-based question answering?
- [DL06-114] How do BERT-era approaches to machine reading comprehension predict answer spans?
- [DL06-115] In what ways can LLMs be used for translation, and how would you compare them with a dedicated neural MT system?
- [DL06-116] How did statistical machine translation (phrase-based, IBM models) differ from neural encoder-decoder translation with attention?
- [DL06-117] How would you extract keywords from a document using RAKE, TF-IDF or TextRank?
- [DL06-118] How would you build a spelling corrector using the noisy channel model?
- [DL06-119] How would you detect duplicate questions on a forum, and which text similarity measures would you compare?
- [DL06-120] Why do abstractive summarizers hallucinate, and how would you measure and reduce unfaithful summaries?
