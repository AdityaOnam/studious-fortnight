---
domain: genai
topic: multimodal_vision_audio_llms
title: Multimodal, vision and audio models
tags: [multimodal, vlm, clip, speech]
count: 102
part: 1/2
---
# Multimodal, vision and audio models (part 1)

## Multimodal fundamentals and fusion
- [GA06-001] What are multimodal AI models, and how do they process different types of data such as text, images and audio?
- [GA06-002] Transformers were designed for text, so how can they also understand images?
- [GA06-003] What is visual question answering (VQA), and how do modern multimodal LLMs approach it?
- [GA06-004] How do image embeddings work, and how are they produced?
- [GA06-005] Explain early fusion versus late fusion in multimodal models, and when you would pick each.
- [GA06-006] Compare contrastive dual encoders such as CLIP, adapter-based VLMs and cross-attention approaches to multimodal modelling.
- [GA06-007] How would you build a system that accepts both images and text and answers questions over them?
- [GA06-008] How would you add a new modality, such as audio, to an existing text-only LLM?
- [GA06-009] How do you handle multimodal inputs and outputs in an agentic system, including degradation when one modality fails?
- [GA06-010] How do audio and vision-language-action models integrate with VLMs to form a single multimodal agent?
- [GA06-011] How do you design the tool set for a vision agent, and when should it call tools rather than answer from pixels?
- [GA06-012] What are the challenges of real-time multimodal AI processing?
- [GA06-013] What are the latency and cost considerations of running multimodal models in production?
- [GA06-014] How would you route between models to build a low-latency multimodal agent?
- [GA06-015] What are the trade-offs of deploying a small open-weight multimodal model on device versus calling a hosted one?
- [GA06-016] What is an omni model with a thinker-talker architecture, and why does it matter for voice and vision?
- [GA06-017] How do you evaluate multimodal systems, covering both understanding and generation?
- [GA06-018] How do you evaluate a vision-language agent, and what do benchmarks such as MathVista, ChartQA, DocVQA and MMMU each measure?
- [GA06-019] Adapter-based VLMs versus natively multimodal (early-fusion, any-to-any) models: what is the real trade-off?
- [GA06-020] Why does a shared softmax over mixed-modality tokens cause training instability in natively multimodal models?
- [GA06-021] Where do adapter-based multimodal models still beat natively multimodal ones on benchmarks, and why?
- [GA06-022] A multimodal product must keep working when the image is missing or corrupted at inference. How would you make the model robust to missing modalities?

## CLIP and multimodal embeddings
- [GA06-023] What is CLIP, how is it trained, and why did it become the foundation for so much multimodal work?
- [GA06-024] How does CLIP perform zero-shot classification, why does it work well, and where does it break down?
- [GA06-025] Why do large batch sizes matter so much for contrastive learning?
- [GA06-026] What role does the temperature parameter play in CLIP's contrastive loss, and what happens if it is too high or too low?
- [GA06-027] How do BLIP and CLIP differ, and why was BLIP needed?
- [GA06-028] Why did SigLIP's sigmoid loss displace CLIP's softmax contrastive loss for vision encoder pretraining?
- [GA06-029] Why does a learnable bias term matter for the sigmoid loss specifically?
- [GA06-030] If you were pretraining a vision encoder for dense document text rather than natural images, what would you change about the recipe?
- [GA06-031] When does a contrastive (CLIP-style) encoder underperform a captioning-trained one as the LLM's vision encoder?
- [GA06-032] What is the modality gap in CLIP-style embedding spaces, and when does it actually bite you?
- [GA06-033] How would mean-centring per modality change your CLIP retrieval results, and what could it break?
- [GA06-034] How would you make "image-to-caption" and "image-to-image" similarity scores comparable in a single ranking?
- [GA06-035] How would you use CLIP to build a zero-shot content moderation filter, and where would it fail?
- [GA06-036] What are multimodal embeddings, and how are they generated?
- [GA06-037] How are multimodal embeddings used for cross-modal search, such as text-to-image retrieval?
- [GA06-038] How do multimodal embedding models change the design of a RAG system?
- [GA06-039] How do you build an image-text retrieval system with multimodal models, from indexing to ranking?
- [GA06-040] What similarity metric and normalisation would you use when indexing CLIP embeddings in an ANN index, and why?
- [GA06-041] How would you build multimodal retrieval over images, video and text in a single index?
- [GA06-042] You need one embedding space for your own domain: product photos, PDF spec sheets and text queries. Off-the-shelf CLIP is not good enough. How do you build it?
- [GA06-043] How would you detect and handle false negatives in click-mined training data for a multimodal embedding model?
- [GA06-044] When would you skip parsing entirely and retrieve over page images with a visual retriever such as ColPali?
- [GA06-045] How would you cut the per-page vector count in a ColPali-style retriever without losing the benefit of late interaction?
- [GA06-046] How do you produce a precise citation when your retrieval unit is a page image?

## VLM architecture and training
- [GA06-047] What is a vision-language model, and how are its components arranged?
- [GA06-048] Walk me through how a VLM turns an image into something an LLM can answer questions about.
- [GA06-049] How does LLaVA connect its vision encoder to the LLM?
- [GA06-050] How does a VLM combine a vision encoder, a projector and an LLM, and how is it trained in stages?
- [GA06-051] How do VLMs get images into an LLM: projector, cross-attention, or native tokens?
- [GA06-052] What is a Perceiver Resampler, and how does it compare to a linear projection?
- [GA06-053] Compare VLM projector designs: MLP versus resampler versus cross-attention. How does the choice interact with the training recipe?
- [GA06-054] Why can you get away with training only the projector in stage 1 of VLM training?
- [GA06-055] What breaks if you use a randomly initialised vision encoder instead of a pretrained one such as CLIP in a VLM?
- [GA06-056] When would you unfreeze the vision encoder in a VLM, and what can go wrong?
- [GA06-057] What data mix would you use to train a VLM: captions, interleaved image-text, and instruction data? Why each?
- [GA06-058] What is interleaved image-text data, and why does it matter for multi-image and in-context multimodal ability?
- [GA06-059] How do you fine-tune a vision-language model for a domain task?
- [GA06-060] You LoRA-fine-tune a VLM on your domain and its general text abilities degrade. Which components do you adapt, and how do you prevent forgetting?
- [GA06-061] How does a multimodal model handle multi-image input differently from single-image input?
- [GA06-062] How does the token count per image change multi-image and video capability in a VLM?
- [GA06-063] How does a VLM handle an image whose aspect ratio does not match the vision encoder's training resolution?
- [GA06-064] How do images become tokens in a VLM, and why does image resolution drive inference cost?

## Resolution, documents and OCR
- [GA06-065] Why does a native dynamic-resolution ViT with window attention and multimodal RoPE beat fixed-size tiling, and what does MRoPE encode?
- [GA06-066] Why is native resolution especially important for OCR and grounding compared with image captioning?
- [GA06-067] How does a variable token count per image complicate batching and serving of a vision-language model?
- [GA06-068] How would you estimate the monthly bill for a screenshot-heavy agent?
- [GA06-069] How would you decide the pixel budget per document class rather than globally in a VLM document pipeline?
- [GA06-070] Your model misreads totals on receipts. How do you decide whether to raise the resolution or change approach?
- [GA06-071] Why did resampler-based VLMs with a fixed token budget per image underperform on DocVQA?
- [GA06-072] What is document understanding, and how do models parse documents with complex layouts?
- [GA06-073] How do vision LLMs extract layout and structure from documents, and when do you still prefer specialist OCR APIs?
- [GA06-074] How would you reliably extract tables and charts from documents?
- [GA06-075] A VLM returns a beautifully formatted table with one hallucinated row. What catches it?
- [GA06-076] How do you evaluate chart extraction when the only ground truth is the image?
- [GA06-077] Your VLM answers single-image questions well but fails on multi-page documents. How do you fix it?
- [GA06-078] Design an invoice recognition and reimbursement agent built around a vision-language model.
- [GA06-079] Your VLM extracts invoice fields at about 91% per-field accuracy. The customer needs 99% and you cannot fine-tune the model. What do you do?
- [GA06-080] How would you set the abstention threshold for invoice field extraction without a large labelled set?
- [GA06-081] What changes in an invoice extraction system if the 99% requirement applies per document rather than per field?
- [GA06-082] Design the evaluation for a document understanding feature where users upload invoices and scanned forms and ask questions about them.
- [GA06-083] How would you evaluate document QA on a 40-page document where the answer needs two facts from different pages?
- [GA06-084] Your vision-model judge for document evals costs more than the feature itself. What now?
- [GA06-085] When is a dedicated OCR plus layout parser better than sending page images straight to a VLM, and when is it worse?

## VLM failure modes, grounding and evaluation
- [GA06-086] What do vision-language models reliably get wrong?
- [GA06-087] Your vision-language model generates factually incorrect image descriptions. How do you detect and reduce this?
- [GA06-088] How would you measure object hallucination in image captioning, for example with POPE-style probing or CHAIR?
- [GA06-089] Your multimodal LLM ignores the image and answers from the text alone. How do you diagnose and fix it, and how would you detect it in the first place?
- [GA06-090] What is spatial grounding, and why is it one of the hardest capabilities for VLMs?
- [GA06-091] Why does contrastive pretraining specifically produce weak spatial reasoning in vision-language models?
- [GA06-092] What does grounding mean for a VLM, and how does a model actually output a bounding box?
- [GA06-093] How would you evaluate VLM grounding quality, and why is IoU a poor fit for a document-redaction use case?
- [GA06-094] A VLM returns bounding boxes that are close but consistently shifted down and right. What do you check first?
- [GA06-095] How would you collect training data for GUI grounding at scale?
- [GA06-096] Which common VLM failure modes have reasoning models improved, and which persist?
- [GA06-097] How would you catch a VLM confidently misreading a dollar amount in production without humans reviewing every document?
- [GA06-098] When should a VLM hand off to a dedicated vision model such as a detector, segmenter or tracker instead of answering from pixels?
- [GA06-099] A safety-compliance camera system must flag missing harnesses. Sketch the specialist-first pipeline and say where the VLM sits and who wins when the two disagree.
- [GA06-100] How would you build a crop-and-zoom tool loop for a VLM, and what stops it from looping forever?
- [GA06-101] An attacker embeds instructions as text inside an image sent to your multimodal assistant. How does that attack work and how do you defend against it?
- [GA06-102] How would you build an evaluation set that tests a VLM's perception rather than its language priors?
