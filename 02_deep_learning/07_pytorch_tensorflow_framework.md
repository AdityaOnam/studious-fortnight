---
domain: dl
topic: pytorch_tensorflow_framework
title: PyTorch / TensorFlow / framework questions
tags: [pytorch, tensorflow, keras, numpy, pandas]
count: 169
---
# PyTorch / TensorFlow / framework questions

## NumPy fundamentals
- [DL07-001] What is NumPy, and why is it important for machine learning work?
- [DL07-002] How do NumPy arrays differ from Python lists in memory layout, speed and supported operations?
- [DL07-003] What are the main attributes of an ndarray, and how do you inspect its shape, size and dtype?
- [DL07-004] What data types does NumPy support, and how does the dtype affect memory use and numerical results?
- [DL07-005] What does the axis argument mean in np.sum or np.mean on a 3D array, and how do you reduce over several axes at once?
- [DL07-006] Explain broadcasting in NumPy: what are the rules, and when does it silently produce a wrongly shaped result?
- [DL07-007] What is the difference between a deep copy and a shallow copy (a view) in NumPy?
- [DL07-008] When does NumPy indexing return a view and when a copy, comparing basic slicing with fancy or boolean indexing?
- [DL07-009] Why is vectorized NumPy code much faster than a Python loop, and when does vectorization stop helping?
- [DL07-010] How would you compute all pairwise Euclidean distances between two matrices without loops, and what is the memory cost?

## Pandas for ML data work
- [DL07-011] What is Pandas, and why is it used for data analysis and preparation in ML?
- [DL07-012] Explain the difference between a Series and a DataFrame in Pandas.
- [DL07-013] How do you read and write data from and to a CSV file in Pandas?
- [DL07-014] What are Pandas indexes, and how are they used?
- [DL07-015] How would you use Pandas to load and clean a raw dataset before modelling?
- [DL07-016] What is the purpose of apply() in Pandas, and how do you apply a function to every element of a column?
- [DL07-017] What is the difference between apply and applymap in Pandas?
- [DL07-018] How do you compute the Euclidean distance between two pandas Series?
- [DL07-019] How does groupby work in Pandas? Give an example of aggregating a feature per group.
- [DL07-020] How do you pivot data in a DataFrame?
- [DL07-021] What is the difference between loc and iloc, and why can chained indexing trigger SettingWithCopyWarning or silently fail to update data?
- [DL07-022] What is the difference between slicing and filtering in Pandas?
- [DL07-023] Explain data alignment in Pandas and how it differs from NumPy broadcasting.
- [DL07-024] How does joining and merging work in Pandas, and how do the join types differ?
- [DL07-025] A left join unexpectedly increases your row count. What likely happened and how do you prevent it?
- [DL07-026] How do you apply conditional logic to columns using where() in Pandas?
- [DL07-027] How would you handle missing values in Pandas for an ML dataset without introducing leakage?
- [DL07-028] Why are iterrows and row-wise apply slow, and which vectorized alternatives would you use?
- [DL07-029] How would you do a time-based train/test split in Pandas so that no future data leaks into training?
- [DL07-030] You must process a CSV much larger than memory. How would you do it with Pandas, and how can you cut a DataFrame's footprint (dtypes, categoricals, chunking)?

## Scikit-learn API
- [DL07-031] What is Scikit-Learn, and why is it so popular in machine learning?
- [DL07-032] What are the main categories of algorithms included in Scikit-Learn?
- [DL07-033] What is the typical workflow for building a predictive model with Scikit-Learn, and where does it fit in an ML project?
- [DL07-034] What is the difference between fit, transform and fit_transform, and what goes wrong if you fit a scaler on the test set?
- [DL07-035] Explain the design principles behind Scikit-Learn's consistent estimator API.
- [DL07-036] Describe the roles of transformers, estimators and predictors in Scikit-Learn.
- [DL07-037] What is a Pipeline in Scikit-Learn, and how does it help prevent data leakage during cross-validation?
- [DL07-038] Describe the use of ColumnTransformer in Scikit-Learn.
- [DL07-039] How do you run GridSearchCV or RandomizedSearchCV over a Pipeline, and how are the parameter names written?
- [DL07-040] How would you write a custom transformer that works inside a Scikit-Learn Pipeline?
- [DL07-041] When would you choose StratifiedKFold or GroupKFold over plain KFold?
- [DL07-042] How do you handle categorical features with OneHotEncoder when unseen categories appear at serving time?
- [DL07-043] How do you persist a fitted Scikit-Learn pipeline for serving, and what version risks come with it?

## Framework landscape and TensorFlow basics
- [DL07-044] What is a deep learning framework, and what problems does it solve beyond a plain numerical library?
- [DL07-045] Which Python libraries are most commonly used in machine learning, and what is each used for?
- [DL07-046] What are some popular deep learning frameworks and libraries used for computer vision tasks?
- [DL07-047] What is PyTorch, and how does it differ from TensorFlow?
- [DL07-048] Explain eager versus graph execution and why modern frameworks default to eager.
- [DL07-049] When would you pick PyTorch over TensorFlow for a research project versus for production serving?
- [DL07-050] What is TensorFlow, and what are its main features?
- [DL07-051] What are tensors in TensorFlow?
- [DL07-052] What is a Variable in TensorFlow, and why is it important?
- [DL07-053] What data types does TensorFlow support?
- [DL07-054] What types of devices does TensorFlow support for computation?
- [DL07-055] What is TensorFlow Lite, and where is it used?
- [DL07-056] How does TensorFlow differ from other machine learning libraries?
- [DL07-057] Explain the computation graph in TensorFlow.
- [DL07-058] What is the difference between TensorFlow 1.x and TensorFlow 2.x?
- [DL07-059] In legacy TensorFlow 1.x, what is a Session and what role does it play?
- [DL07-060] In legacy TensorFlow 1.x, what is a Placeholder and how is it used?
- [DL07-061] How does TensorFlow handle automatic differentiation?
- [DL07-062] What does tf.function do, and what are the pitfalls of tracing and retracing?
- [DL07-063] How do you build an efficient tf.data input pipeline, and why does the order of map, shuffle, batch and prefetch matter?

## Keras models and layers
- [DL07-064] What is Keras, and how does it relate to TensorFlow?
- [DL07-065] What are the core components of a Keras model?
- [DL07-066] What are some advantages of using Keras over other deep learning frameworks?
- [DL07-067] What is the purpose of the Dense layer in Keras?
- [DL07-068] Explain the difference between the Sequential and Functional APIs in Keras.
- [DL07-069] How do you configure a neural network in Keras?
- [DL07-070] What does dropout do, and how do you use it in a Keras model?
- [DL07-071] How do you save and load models in Keras?
- [DL07-072] What does from_logits=True mean in Keras loss functions, and what happens if you set it wrongly?
- [DL07-073] How do you build a neural network in TensorFlow end to end?
- [DL07-074] Explain the process of compiling a model in TensorFlow/Keras: what do the optimizer, loss and metrics arguments control?
- [DL07-075] How would you implement a convolutional neural network in Keras?
- [DL07-076] How do recurrent networks differ from feedforward networks, and how would you implement one in Keras?
- [DL07-077] How do you use Batch Normalization in a Keras model, and where does it go relative to the activation?
- [DL07-078] What is a custom layer in Keras, and how would you implement one?
- [DL07-079] How would you construct a residual network (ResNet) in Keras?
- [DL07-080] Which Keras callbacks (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau) do you use, and what does each do?
- [DL07-081] How do you do transfer learning in Keras, and how do trainable flags and BatchNorm layers interact when you freeze a base model?
- [DL07-082] When would you write a custom training loop with tf.GradientTape instead of calling model.fit?

## PyTorch tensors and autograd
- [DL07-083] What are tensors in PyTorch?
- [DL07-084] How do you create tensors on a specific device and dtype, and what happens if you mix devices in one operation?
- [DL07-085] What is the difference between a Tensor and a Variable in PyTorch?
- [DL07-086] How do you convert a NumPy array to a PyTorch tensor?
- [DL07-087] After torch.from_numpy(arr), what happens if you modify arr in place, and why?
- [DL07-088] What is the purpose of the .grad attribute of a tensor?
- [DL07-089] What is the difference between view, reshape and contiguous in PyTorch, and when does a copy occur?
- [DL07-090] Explain contiguous tensors and .contiguous() in PyTorch.
- [DL07-091] What bug can arise from calling squeeze() when the batch size is one?
- [DL07-092] How would you normalize each row of a tensor without using a Python loop?
- [DL07-093] How does broadcasting work in tensor operations, and what shape bugs does it commonly hide?
- [DL07-094] What are strides and storage, and why does transpose not copy data?
- [DL07-095] How does PyTorch autograd build and traverse the computation graph?
- [DL07-096] What are requires_grad and leaf tensors, and why is .grad None for a non-leaf tensor?
- [DL07-097] Compare detach(), clone() and torch.no_grad() in PyTorch.
- [DL07-098] How do in-place operations affect autograd?
- [DL07-099] Describe the process of backpropagation in PyTorch.
- [DL07-100] What happens when you call backward() on a non-scalar output, and when do you need retain_graph?
- [DL07-101] What are tensor and module hooks in PyTorch, and when would you use them for debugging or gradient inspection?
- [DL07-102] How would you compute second-order derivatives or a gradient penalty in PyTorch, and what does create_graph=True do?

## nn.Module and the training loop
- [DL07-103] What are the main steps for creating a neural network model in PyTorch?
- [DL07-104] How does nn.Sequential differ from subclassing nn.Module?
- [DL07-105] What is the role of the forward method in a PyTorch Module?
- [DL07-106] What is the difference between an nn.Parameter, a registered buffer and a plain tensor attribute in a Module?
- [DL07-107] Why must submodules be stored in nn.ModuleList or ModuleDict rather than a plain Python list?
- [DL07-108] How do you implement a custom layer in PyTorch?
- [DL07-109] What are optimizers in PyTorch, and how do you use them?
- [DL07-110] What are the essential steps in a PyTorch training loop?
- [DL07-111] Why and when do you call zero_grad() in PyTorch, and what happens if you forget it?
- [DL07-112] How does gradient accumulation work in PyTorch, and how must you scale the loss when you do it deliberately?
- [DL07-113] How can you implement learning rate scheduling in PyTorch, and where does scheduler.step() go in the loop?
- [DL07-114] How do you freeze part of a model and assign different learning rates to different parameter groups?
- [DL07-115] Why does nn.CrossEntropyLoss expect raw logits and class indices, and what bugs come from passing softmax outputs?
- [DL07-116] Why does validation behave differently between train() and eval() modes in PyTorch?
- [DL07-117] What does model.eval() change in PyTorch besides dropout?
- [DL07-118] What is the difference between model.eval() and torch.no_grad() or torch.inference_mode(), and what goes wrong if you forget either at inference?
- [DL07-119] How do you calculate the epoch loss correctly when the final batch is smaller than the others?
- [DL07-120] How would you debug a PyTorch training run whose loss stays flat or becomes NaN?
- [DL07-121] How do you save and load a model for inference versus for resuming training, including optimizer state?
- [DL07-122] How does torch.autocast with a GradScaler enable mixed-precision training, and why is bf16 easier to use than fp16?
- [DL07-123] How can PyTorch Lightning simplify a PyTorch workflow, and what do you give up?

## Data loading, reproducibility and testing
- [DL07-124] What are torchvision transforms used for?
- [DL07-125] How do you build a DataLoader for a custom dataset?
- [DL07-126] What is the difference between a map-style Dataset and an IterableDataset, and what goes wrong with multiple workers on an iterable one?
- [DL07-127] How would you use collate_fn to batch variable-length sequences?
- [DL07-128] How do DataLoader workers, batch size and pinned memory affect input pipeline throughput?
- [DL07-129] Why might using multiple DataLoader workers be slower?
- [DL07-130] Random augmentations come out identical across DataLoader workers. Why does that happen and how do you fix it?
- [DL07-131] How do you make PyTorch experiments reproducible, and what sources of nondeterminism remain on a GPU?
- [DL07-132] How would you write unit tests for a tensor preprocessing, metric or training utility, checking shapes, dtypes and determinism?
- [DL07-133] How do you review tensor code for correctness across devices, dtypes and shapes?
- [DL07-134] How do you balance readable tensor code against vectorization?
- [DL07-135] When should a utility return tensors versus Python numbers?
- [DL07-136] What issues arise when computing a metric on CPU versus GPU in PyTorch?

## GPU memory and performance
- [DL07-137] What is CUDA, and how does it relate to PyTorch?
- [DL07-138] How does a GPU work for deep learning?
- [DL07-139] How do you check whether a PyTorch model is actually running on the GPU?
- [DL07-140] How would you write a utility that works on both CPU and GPU?
- [DL07-141] How do CUDA kernels work?
- [DL07-142] How does a Google TPU work, and how does it differ from a GPU?
- [DL07-143] Why can calling .item() slow down a GPU training loop?
- [DL07-144] Why do you need torch.cuda.synchronize() when timing GPU code, and what do naive timings miss?
- [DL07-145] How do you find a memory leak caused by retained computation graphs in PyTorch?
- [DL07-146] Why does nvidia-smi show more memory than torch.cuda.memory_allocated reports, and what role does the caching allocator play?
- [DL07-147] Your PyTorch training hits a CUDA out-of-memory error. How do you diagnose it and what levers reduce memory?
- [DL07-148] Estimate the GPU memory needed to train a 1B-parameter model with Adam in fp32 versus mixed precision, excluding activations.
- [DL07-149] How does activation checkpointing trade compute for memory?
- [DL07-150] How would you use torch.profiler to tell whether a training step is bound by data loading, CPU overhead or GPU compute?
- [DL07-151] What does torch.compile do, and what are graph breaks?
- [DL07-152] When can torch.compile slow a model down or keep recompiling, for example with dynamic shapes or Python control flow?
- [DL07-153] A custom CUDA kernel is 10x slower than expected. Without running it, what are the usual suspects, and how do you confirm each?

## Distributed training, deployment and model loading
- [DL07-154] What is TorchScript, and how does it help deployment?
- [DL07-155] How do TorchScript, torch.export and ONNX export differ, and what breaks with dynamic shapes or control flow?
- [DL07-156] How do you create a custom C++ or CUDA operation in PyTorch?
- [DL07-157] Why is DistributedDataParallel preferred over DataParallel?
- [DL07-158] How do you use GPUs for distributed PyTorch training?
- [DL07-159] How would you launch multi-node DDP training with torchrun, and what are rank, local rank and world size?
- [DL07-160] How does DDP synchronize gradients, and how do bucketing and overlap with the backward pass hide communication cost?
- [DL07-161] When you scale from 1 to 8 GPUs with DDP, how should the effective batch size and learning rate change?
- [DL07-162] What does DistributedSampler do, and why do you call set_epoch each epoch?
- [DL07-163] Why does DDP with unused parameters hang or error, and how do you debug it?
- [DL07-164] A multi-GPU job hangs or hits an NCCL timeout. How do you diagnose it?
- [DL07-165] How does FSDP differ from DDP in what it shards and when it communicates?
- [DL07-166] When saving a checkpoint under FSDP or ZeRO-3, how are sharded states consolidated and what pitfalls exist?
- [DL07-167] How does tf.distribute (for example MirroredStrategy) change how you write a Keras training script?
- [DL07-168] What actually happens when you call AutoModelForCausalLM.from_pretrained with device_map="auto" and torch_dtype="auto"?
- [DL07-169] How does from_pretrained behave when a checkpoint is sharded across 30 files and you only have 24 GB of GPU memory?
