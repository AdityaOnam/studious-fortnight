---
domain: genai
topic: multimodal_vision_audio_llms
title: Multimodal, vision and audio models
tags: [multimodal, vlm, clip, speech]
count: 113
part: 2/2
---
# Multimodal, vision and audio models (part 2)

## Video, generative media and VLA
- [GA06-103] How do models understand video, and what are the current limits?
- [GA06-104] What changes when you move from images to video in multimodal models?
- [GA06-105] How does a video-understanding agent process long videos, and how does fixed-frame sampling compare with agentic processing?
- [GA06-106] When does sampling video at 1 fps break down?
- [GA06-107] Why is counting event repetitions in video so hard for video-understanding models?
- [GA06-108] How would you build "find when the package was delivered" over 24 hours of doorbell footage without ingesting 24 hours of tokens?
- [GA06-109] How does an image-generation sub-agent work, and how do you evaluate generation accuracy and diversity?
- [GA06-110] How does an image-editing agent differ from a text-to-image agent?
- [GA06-111] A marketplace wants AI-generated lifestyle photos of sellers' own products. How do you keep the product accurate: LoRA, IP-Adapter, ControlNet or an editing model?
- [GA06-112] A seller uploads one blurry photo. Which approaches for generating product lifestyle images still work, and what do you tell the seller?
- [GA06-113] How would you harmonise lighting and shadows when compositing original product pixels into a generated scene?
- [GA06-114] How would you detect that an image-editing model subtly changed the text on a product label?
- [GA06-115] How do you regression-test a generative media pipeline when outputs are not reproducible?
- [GA06-116] Design a service that turns a script into a narrated, music-backed video. What are the hard parts?
- [GA06-117] How would you evaluate temporal consistency of generated video automatically?
- [GA06-118] How do provenance and watermarking apply to generated media pipelines?
- [GA06-119] What is a vision-language-action (VLA) model? Contrast discrete action tokens (RT-2, OpenVLA) with flow-matching action heads (pi0).
- [GA06-120] How is a vision-language-action model different from an LLM that calls tools?
- [GA06-121] Explain action chunking. Why predict a sequence of future actions, and how would you choose the chunk length?
- [GA06-122] What goes wrong when a VLA action chunk is executed open-loop and the scene changes mid-chunk?
- [GA06-123] Why does co-training on web vision-language data matter for a VLA when you only care about robot success?
- [GA06-124] A humanoid control system splits into a large slow model and a small fast one. Why not one end-to-end network, and what happens if the slow model stalls for a second?
- [GA06-125] How would you compare two VLA checkpoints fairly with only 50 real-robot trials each?

## Speech recognition
- [GA06-126] What is WER, how is it computed, and what does it miss?
- [GA06-127] How does Whisper work, and why is it so robust compared with earlier ASR systems?
- [GA06-128] What does weak supervision mean in the context of Whisper, and why did it beat curated data?
- [GA06-129] Compare CTC, attention-based encoder-decoder and transducer (RNN-T) architectures for ASR. When do you use each?
- [GA06-130] Why does Whisper hallucinate on silence, and how would you guard against it in production?
- [GA06-131] How would you build streaming transcription on top of a 30-second-window batch model like Whisper?
- [GA06-132] How do you evaluate ASR quality beyond WER, and how do you evaluate TTS quality when there is no single correct output?
- [GA06-133] How would you build an entity error rate metric for speech recognition without hand-labelling thousands of hours?
- [GA06-134] How do you handle noisy audio environments in a speech pipeline?
- [GA06-135] Build a Voice Activity Detector from scratch. How do you make it robust for phone-quality Indian-language audio?
- [GA06-136] How would you evaluate voice activity detection quality without frame-level labels?
- [GA06-137] How do you handle code-switching and accents in a production ASR system?
- [GA06-138] Whisper transcribes Hinglish poorly, forcing output into one language or hallucinating. Why, and how would you build an ASR that handles code-mixed speech?
- [GA06-139] How would you build a labelled code-mixed speech evaluation set cheaply?
- [GA06-140] For code-mixed ASR output, would you normalise to native script or keep transliteration, and why?
- [GA06-141] Design a speaker diarisation system, and explain how you attribute roles such as agent and caller rather than just clusters.
- [GA06-142] How would you evaluate diarisation quality in a way that correlates with downstream note errors rather than with DER?
- [GA06-143] How would you build and improve an ASR system for a clinic room with two or three speakers, background noise, accents and a vocabulary full of drug names?
- [GA06-144] A patient's chart already lists their medications. How would you use that to improve drug-name transcription, size the bias list, and keep it from backfiring?
- [GA06-145] Where should speech recognition run for a healthcare voice assistant: cloud under an agreement or on-premises?
- [GA06-146] How do speaker diarisation and medical entity extraction fit into a clinical note pipeline?
- [GA06-147] How would you adapt a general ASR model to domain vocabulary: hotword boosting, language-model fusion, or fine-tuning?
- [GA06-148] Why do speech models use log-mel spectrograms rather than raw waveforms as input?

## Text-to-speech and dubbing
- [GA06-149] What is text-to-speech (TTS), and what kinds of models are used for it?
- [GA06-150] How does modern TTS work, and what makes speech generation hard in a real-time product?
- [GA06-151] What are neural audio codecs such as EnCodec or SoundStream, and why do speech language models use them?
- [GA06-152] How does sentence chunking reduce the latency of a voice agent's TTS?
- [GA06-153] Walk through streaming TTS: how do you chunk input text and how do you size the jitter buffer?
- [GA06-154] Why does sentence-chunked streaming TTS sound choppy, and how do you fix it?
- [GA06-155] How would you make jitter buffer sizing adaptive in streaming TTS without oscillating?
- [GA06-156] Where do you meter characters for billing in a streaming TTS service when a stream is cancelled halfway?
- [GA06-157] Serving real-time TTS is a different capacity problem from serving a text LLM. Why, and how do you plan capacity?
- [GA06-158] There is no single correct output for an utterance. How do you evaluate speech synthesis quality at scale?
- [GA06-159] How many CMOS raters do you need to detect a small change in speech quality?
- [GA06-160] How would you automatically regression-test TTS quality in CI, including prosody regressions an ASR-based WER check would pass?
- [GA06-161] What changes when TTS moves inside a speech-to-speech omni-model?
- [GA06-162] A bank wants account numbers read in groups of four with pauses. Where does that logic live: the text normaliser or the model?
- [GA06-163] How do you version a customer's pronunciation lexicon for TTS without regressing their old audio?
- [GA06-164] What are the hard parts of text normalisation and prosody for code-mixed, mixed-script Indian-language TTS?
- [GA06-165] How would you handle a sentence that switches script mid-word in a TTS front-end?
- [GA06-166] Why might an LLM-based front-end beat rule-based prosody for expressive TTS, and what does it cost you?
- [GA06-167] What are the consent and abuse risks of zero-shot voice cloning, and what safeguards would you build into a TTS product?
- [GA06-168] Design the dubbing pipeline: an English video becomes Spanish, with the same speakers and the same timing.
- [GA06-169] In a video dubbing pipeline, two speakers overlap for four seconds. What does your pipeline do?
- [GA06-170] In a dubbing pipeline, how do you handle a proper noun that should not be translated but must be pronounced natively?

## Voice agent architecture, latency and turn-taking
- [GA06-171] What are ASR, LLM, TTS and VAD each responsible for in a voice system?
- [GA06-172] Cascaded ASR + LLM + TTS versus a native speech-to-speech model: what are the trade-offs?
- [GA06-173] Chained pipeline, single speech-to-speech model, or a duplex front end with a backend: how do you choose?
- [GA06-174] What would make you migrate a shipped cascaded voice agent to a native speech-to-speech model?
- [GA06-175] Budget the end-to-end latency for a real-time voice agent (VAD, ASR, LLM, TTS, network). Where does the time go, and what is the single biggest lever?
- [GA06-176] Why is time-to-first-audio a different problem from an LLM's time-to-first-token?
- [GA06-177] A voice agent's p50 latency is fine but p99 is 2.5 s. Which term of the budget do you attack first?
- [GA06-178] How does the latency budget of a voice agent change over PSTN telephony rather than WebRTC?
- [GA06-179] What is turn-taking in a voice agent, and how does it detect that the user has finished speaking?
- [GA06-180] How do you tune the endpoint silence timeout differently for a form-filling bot and an open conversation?
- [GA06-181] Your voice agent both cuts users off mid-sentence and leaves awkward dead air. Diagnose and fix.
- [GA06-182] How would you collect labelled data to train a semantic turn detector for your domain?
- [GA06-183] Design turn detection for 8 kHz phone audio: how do you tell a pause from the end of a turn, and "uh-huh" from an interruption?
- [GA06-184] How do you handle barge-in (user interruptions) in a voice agent?
- [GA06-185] Design barge-in for a voice agent. What breaks if you get it wrong?
- [GA06-186] How do you tune the backchannel threshold in barge-in handling without a labelled dataset?
- [GA06-187] What changes in barge-in handling when the caller is on a speakerphone in a car?
- [GA06-188] How do you regression-test barge-in behaviour in a voice agent?
- [GA06-189] What is speculative (preemptive) LLM generation in a voice agent, and how does it reduce latency?
- [GA06-190] Eager end-of-turn detection raises LLM calls by 50 to 70%. How do you decide whether speculative generation is worth it?
- [GA06-191] How does a full-duplex speech model listen and talk at the same time, and when would you choose it over a turn-based pipeline?
- [GA06-192] Why does distilling the first codebook towards semantic features help a speech language model?
- [GA06-193] What training data would you need to teach a full-duplex speech model backchannelling, and how would you get it?

## Voice agents in production
- [GA06-194] Your chat agent is moving to the phone. What actually changes?
- [GA06-195] A managed voice platform handles turns and interruptions for you. Why not just use it instead of building your own?
- [GA06-196] When a user interrupts a voice agent mid-tool-call, what state do you roll back?
- [GA06-197] A caller hangs up between hold and confirm while the agent is booking. How do you design tool execution so a mid-call correction or drop never double-books?
- [GA06-198] While the backend is slow, a voice agent tells the caller a fee should be waived. How do you catch this, and how do you stop it recurring?
- [GA06-199] When a long voice call is restarted as a new session, what goes into the seed and how big should it be?
- [GA06-200] A caller spells their surname and the agent still gets it wrong twice. How do you capture exact identifiers like member IDs and dates of birth reliably over voice?
- [GA06-201] A caller switches from Spanish to English mid-call. What breaks first in a voice agent?
- [GA06-202] How do you keep the LLM in a voice agent from switching language mid-answer when the user code-mixes?
- [GA06-203] Leadership wants the voice agent in four new languages because the vendor claims it "supports 97 languages." How do you decide what launches, and what do you build differently per language?
- [GA06-204] How do you evaluate a voice agent end to end?
- [GA06-205] Design the release gate for a voice agent: a change to the model, prompt, voice or framework must be proven at least as good. What is in the harness and what blocks a release?
- [GA06-206] How do you keep the simulated caller honest in a voice agent evaluation harness?
- [GA06-207] Which production metrics would you monitor for a live voice agent, and what alerts would you set?
- [GA06-208] Build a cost model for one million voice minutes per month across architecture options.
- [GA06-209] Where do you put safety filtering in a speech-to-speech architecture that has no text midpoint?
- [GA06-210] How would you add a safety filter to a full-duplex speech model without reintroducing turn latency?
- [GA06-211] What consent, disclosure and opt-out handling does an outbound AI calling product need?
- [GA06-212] How do you threat-model a banking voice agent against audio injection and cloned voices?
- [GA06-213] How should a voice agent take card numbers or other sensitive data so they stay out of transcripts and LLM context?
- [GA06-214] How should a voice agent detect voicemail or an answering machine on an outbound call, and what should it do?
- [GA06-215] How do you hand a call off to a human agent without making the caller repeat everything?
