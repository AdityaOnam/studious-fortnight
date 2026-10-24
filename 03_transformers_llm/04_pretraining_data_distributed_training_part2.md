---
domain: llm
topic: pretraining_data_distributed_training
title: Pretraining, data and distributed training
tags: [pretraining, distributed-training, zero, fsdp]
count: 108
part: 2/2
---
# Pretraining, data and distributed training (part 2)

## Mixed precision and memory-saving techniques
- [LLM04-108] What is TF32, and how many bits does it use for sign, exponent and mantissa compared with FP32, FP16 and BF16?
- [LLM04-109] Compare FP16 and BF16 for LLM training. Why is BF16 usually more stable, and when would loss scaling still be needed?
- [LLM04-110] How does mixed-precision training keep FP32 master weights, and what is dynamic loss scaling?
- [LLM04-111] Why do mixed-precision recipes keep reductions such as softmax, layer norm and the loss in FP32?
- [LLM04-112] What is the FP8 data type, and what are its advantages?
- [LLM04-113] Compare BF16, FP8 and FP4 training: what range and precision issues arise at each level?
- [LLM04-114] What changes in training and serving if you move from int8 to FP8 on newer hardware?
- [LLM04-115] What do 8-bit optimizers do, and what risks do they carry for training stability?
- [LLM04-116] Why does BF16 remove the need for loss scaling? What is the actual bit-level difference from FP16?
- [LLM04-117] How do you train an LLM in low precision without compromising accuracy?
- [LLM04-118] FP8 training at 671B scale is hard. What actually breaks in low precision, and how do you make it stable?
- [LLM04-119] In FP8 training, why is per-tensor scaling insufficient while per-block scaling is enough?
- [LLM04-120] Which tensors would you never put in FP8 in large-model training, and why keep FP32 master weights?
- [LLM04-121] What is activation (gradient) checkpointing, what is its compute overhead, and why does it trade compute for memory?
- [LLM04-122] What is the cost of recomputation in extra forward FLOPs, and how does selective recomputation reduce it?
- [LLM04-123] When is gradient checkpointing a bad trade-off?
- [LLM04-124] What is gradient accumulation, and how do micro-batch size, global batch size and the number of GPUs relate?
- [LLM04-125] In distributed training of a large model, where does gradient accumulation fit?
- [LLM04-126] Explain CPU offloading and compute-communication overlapping as training optimizations.
- [LLM04-127] Training hits out-of-memory errors. List the levers you would pull, in order, and the cost of each.
- [LLM04-128] A single GPU is all you have for fine-tuning a 7B model. What memory-saving techniques make that feasible?
- [LLM04-129] How does heterogeneous-memory training (GPU, CPU, NVMe) change achievable model sizes, and what throughput penalty does it add?
- [LLM04-130] Explain gradient accumulation, gradient checkpointing and ZeRO/FSDP, and how you would combine them for a real training run.
- [LLM04-131] How would you detect and localise NaN or inf values in a mixed-precision run, and what would you change first?

## Tensor, sequence and pipeline parallelism
- [LLM04-132] What is model parallelism versus data parallelism in distributed training?
- [LLM04-133] What is model parallelism, and how is it used in LLM pre-training?
- [LLM04-134] What is tensor parallelism (intra-layer parallelism), and how does it differ from pipeline parallelism?
- [LLM04-135] What is pipeline parallelism, and why is naive pipeline parallelism inefficient?
- [LLM04-136] Explain column-parallel and row-parallel linear layers, and how Megatron-LM partitions an MLP block with only one all-reduce in the forward pass.
- [LLM04-137] How does Megatron-LM split self-attention across GPUs, and why does the number of heads constrain the tensor-parallel degree?
- [LLM04-138] Why is tensor parallelism usually confined to a single node, and how much communication does it add per transformer layer?
- [LLM04-139] What problem does sequence parallelism solve in tensor-parallel training, and which activations does it partition?
- [LLM04-140] Compare 1D, 2D, 2.5D and 3D tensor parallelism in memory use and communication.
- [LLM04-141] Why do the embedding and output projection need special treatment (vocab parallelism) under tensor parallelism?
- [LLM04-142] Explain micro-batching in GPipe and derive the pipeline bubble fraction for K stages and M micro-batches.
- [LLM04-143] What is the bubble ratio with 8 pipeline stages and 32 micro-batches, and how would you reduce it?
- [LLM04-144] Compare GPipe and 1F1B schedules in terms of bubble size and peak activation memory.
- [LLM04-145] Why does pipeline parallelism under 1F1B require careful handling of activation memory in the first stages?
- [LLM04-146] How do you partition layers across pipeline stages to balance load, and what happens when the embedding or LM head makes stages unequal?
- [LLM04-147] What does the interleaved 1F1B schedule in Megatron-LM change, and what extra cost does it introduce?
- [LLM04-148] What are PipeDream, PipeDream-2BW and PipeDream-Flush, and how do they handle weight versions and staleness?
- [LLM04-149] When is pipeline parallelism the wrong tool compared with more tensor or data parallelism?
- [LLM04-150] What is zero-bubble pipeline scheduling, and how does it shrink the bubble?
- [LLM04-151] Explain ring attention or context parallelism for training with very long sequences. How is attention computed when K/V are sharded?
- [LLM04-152] DualPipe overlaps computation and communication in training. Why is that overlap the whole game at this scale, and what is the trade-off?
- [LLM04-153] Where does the extra memory in DualPipe come from, and how would you bound it?
- [LLM04-154] How does context parallelism differ from Megatron-style sequence parallelism, and when do you need each?

## Combining parallelism and cluster topology
- [LLM04-155] Compare data parallelism, tensor parallelism and pipeline parallelism, and say when you combine them.
- [LLM04-156] How are DP, TP and PP combined into 3D parallelism, and how do you map each to the cluster topology?
- [LLM04-157] Which parallelism dimension should be placed on the fastest interconnect, and why?
- [LLM04-158] How do you pick the tensor x pipeline x data parallel layout for a given cluster topology?
- [LLM04-159] Given a single node with several GPUs, how do you choose between DDP, ZeRO, PP and TP depending on whether the model fits on one GPU?
- [LLM04-160] Given multiple nodes with a slow inter-node network, which combination of parallelism strategies would you pick and why?
- [LLM04-161] A 13B model fits on one GPU and you have 64 GPUs. Why might pure data parallelism still be the best choice?
- [LLM04-162] Why can ZeRO-3 underperform 3D parallelism at thousand-GPU scale?
- [LLM04-163] Can pipeline parallelism be combined with ZeRO-2 or ZeRO-3, and why is that generally discouraged?
- [LLM04-164] What is expert parallelism for MoE models, and what role does all-to-all communication play?
- [LLM04-165] Why does expert parallelism require all-to-all, and how does its cost scale with the number of nodes?
- [LLM04-166] What is automatic parallelism (Alpa, GSPMD, FlexFlow, Mesh-TensorFlow), and what search space do these systems explore?
- [LLM04-167] How does Alpa decompose the problem into inter-operator and intra-operator parallelism?
- [LLM04-168] What do Megatron-LM, DeepSpeed, FairScale and Colossal-AI each offer, and how would you choose among them?
- [LLM04-169] How did BLOOM and Megatron-Turing NLG combine DeepSpeed and Megatron to train at scale?
- [LLM04-170] Compare tensor, pipeline, data, sequence and expert parallelism for a run on hundreds of accelerators. When do you combine them?
- [LLM04-171] How would you decide between wider tensor parallelism and deeper pipeline parallelism?
- [LLM04-172] You have 1024 GPUs across 128 nodes of 8 GPUs and must train a 175B model. Choose TP, PP and DP sizes and justify them.
- [LLM04-173] Design the training setup for a model that does not fit on one accelerator, say a 70B-parameter model on a pod.
- [LLM04-174] How would you decide the order and sizes of TP, PP, DP and EP given model shape, GPU memory and network bandwidth?
- [LLM04-175] How do you combine expert parallelism with data and tensor parallelism, and what are the load-imbalance and communication pitfalls?
- [LLM04-176] Where would you place shared versus routed experts across devices to minimise communication?
- [LLM04-177] What changes in large-scale distributed training when the cluster spans buildings with different network tiers?

## Training stability and hyperparameters
- [LLM04-178] What phases does the loss curve typically go through when training a Transformer, and how do you diagnose problems from it?
- [LLM04-179] Why do large pretraining runs set dropout to 0?
- [LLM04-180] How do learning rate, warmup, gradient clipping and effective batch size interact in large-model training?
- [LLM04-181] Why is warmup needed, and what tends to go wrong when it is too short for a large model?
- [LLM04-182] How do you choose the global batch size and learning rate for large-scale pretraining, and what is the critical batch size?
- [LLM04-183] Compare cosine and warmup-stable-decay learning rate schedules for pretraining. What are the trade-offs?
- [LLM04-184] Why do Adam's epsilon and a lower beta2 matter for stability in large-model training?
- [LLM04-185] What are loss spikes in large-scale training, and how do teams detect and recover from them?
- [LLM04-186] If the loss recovers on its own after a spike in a large pretraining run, do you still act?
- [LLM04-187] When a pretraining run diverges and you roll back to a checkpoint, why does deterministic, resumable data ordering matter?
- [LLM04-188] What would you monitor during a training run (grad norm, update-to-weight ratio, activation maxima, logit statistics) to catch instability early?
- [LLM04-189] What is a z-loss or logit regularizer, and how does it help stability?
- [LLM04-190] Your LLM pretraining loss just spiked. Talk me through training stability: gradient clipping, mixed precision and your debugging playbook.
- [LLM04-191] A large training run shows a loss spike followed by divergence. What would you check and what mitigations would you apply?
- [LLM04-192] Your pretraining loss suddenly diverges at step 300k of a long run. Diagnose and fix it.
- [LLM04-193] Gradient clipping fires on 40% of training steps. What do you change?
- [LLM04-194] How do you distinguish a recoverable loss spike from a poisoned run that requires restarting from an earlier checkpoint?
- [LLM04-195] When would you restart a diverged pretraining run entirely rather than roll back to a checkpoint?
- [LLM04-196] Two runs with the same config but different seeds diverge differently. How do you attribute the cause to data, numerics or hardware?
- [LLM04-197] How would you set the peak learning rate for a model 10x bigger?
- [LLM04-198] When training a trillion-parameter model, attention logits can blow up and destabilise the run. What is going on, and how does something like MuonClip address it?
- [LLM04-199] Why do orthogonalised optimizer updates (as in Muon) help efficiency but potentially worsen attention-logit instability?
- [LLM04-200] How does QK-clip differ from QK-norm?

## Fault tolerance and large-scale efficiency
- [LLM04-201] What state must a checkpoint contain to resume a large training run exactly (weights, optimizer, RNG, data loader position)?
- [LLM04-202] A GPU node dies mid-run. How should checkpointing be designed so you do not lose days of progress?
- [LLM04-203] What is a straggler in distributed training, and how do you detect and mitigate one?
- [LLM04-204] Training across nodes is slower than expected. How would you check interconnect bandwidth, NVLink topology and NCCL configuration?
- [LLM04-205] What is goodput in large-scale training, and how does it differ from raw GPU utilization?
- [LLM04-206] What are asynchronous and sharded checkpointing, and why do they matter at scale?
- [LLM04-207] How would you debug a multi-node job that hangs or hits NCCL timeouts?
- [LLM04-208] GPU utilization is low and the data loader seems to be the bottleneck. How do you confirm and fix it?
- [LLM04-209] What is silent data corruption in large clusters, and how would you detect it during training?
- [LLM04-210] How would you design fault tolerance and resume logic for a multi-week, thousand-GPU training run?
- [LLM04-211] You are training on tens of thousands of GPUs and hardware fails constantly. How do you keep goodput high?
- [LLM04-212] How would you decide checkpoint frequency quantitatively for large-scale training with frequent hardware failures?
- [LLM04-213] A customer's distributed training job runs efficiently for 3 hours and then degrades. What does that suggest?
- [LLM04-214] What monitoring would you build so a GPU platform catches distributed-training efficiency degradation before the customer does?
- [LLM04-215] What breaks when you scale LLM training from 8 GPUs to thousands, and how do modern stacks deal with it?
