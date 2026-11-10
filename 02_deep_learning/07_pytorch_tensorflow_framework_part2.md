---
domain: dl
topic: pytorch_tensorflow_framework
title: PyTorch / TensorFlow / framework questions
tags: [pytorch, tensorflow, keras, numpy, pandas]
count: 42
part: 2/2
---
# PyTorch / TensorFlow / framework questions (part 2)

## NumPy in depth
- [DL07-170] What are universal functions (ufuncs) in NumPy, and why are they fast?
- [DL07-171] What is the difference between *, np.dot, np.matmul and the @ operator for NumPy arrays?
- [DL07-172] Why should you prefer np.linalg.solve over computing an explicit matrix inverse?
- [DL07-173] What is the difference between np.concatenate, np.stack, np.vstack and np.hstack?
- [DL07-174] What is the difference between flatten, ravel and reshape(-1), and which of them return views?
- [DL07-175] How should you generate random numbers reproducibly in NumPy, and why is np.random.default_rng preferred over the legacy global state?
- [DL07-176] What does the ddof argument change in np.var and np.std?
- [DL07-177] What are strides in a NumPy array, and how can stride tricks such as sliding_window_view create windows without copying data?
- [DL07-178] When do in-place operations and the out= argument improve NumPy performance and memory use?
- [DL07-179] What are structured and record arrays in NumPy, and when are they useful?
- [DL07-180] What are masked arrays in NumPy, and how do they compare with using NaN for missing values?
- [DL07-181] How do you detect and handle NaN and infinite values in NumPy, and what do nan-aware functions such as np.nanmean do?
- [DL07-182] How do you save and load NumPy arrays, and when would you use np.memmap for arrays larger than memory?
- [DL07-183] How do you convert image arrays between HWC and CHW layouts and between uint8 and float before feeding them into a CNN?
- [DL07-184] How do SciPy and NumPy differ, and what does SciPy add?
- [DL07-185] How does JAX's NumPy-like API differ from NumPy, for example in immutability, jit, grad and vmap?

## Pandas in depth
- [DL07-186] How do stack, unstack and melt reshape a DataFrame?
- [DL07-187] What is the difference between astype, pd.to_numeric and pd.to_datetime, and how do they handle bad values?
- [DL07-188] How do you use resample, rolling and expanding windows to build time-series features in Pandas?
- [DL07-189] How do you align and merge several time series in Pandas, for example with merge_asof?
- [DL07-190] What is a MultiIndex in Pandas, and how do you select data with it?
- [DL07-191] When would you move from Pandas to Dask, Polars or Spark, and what changes in how you write the code?

## Scikit-learn in depth
- [DL07-192] How do SimpleImputer, KNNImputer and IterativeImputer differ in scikit-learn?
- [DL07-193] What are scikit-learn's limitations on very large datasets, and how do partial_fit and out-of-core learning help you update a model with new data?
- [DL07-194] What role does joblib play in scikit-learn, both for n_jobs parallelism and for model persistence?

## Keras and TensorFlow in depth
- [DL07-195] How do you turn raw text into sequences or one-hot vectors in Keras, for example with the TextVectorization layer?
- [DL07-196] How do you build a multi-input or multi-output model in Keras, and how are the losses weighted?
- [DL07-197] What is a stateful LSTM in Keras, and what constraints does it put on batching?
- [DL07-198] How do you export a Keras model as a SavedModel and serve it with TensorFlow Serving?
- [DL07-199] What are the main components of TensorFlow Extended (TFX), and what does each do in a production pipeline?
- [DL07-200] What does XLA compilation do in TensorFlow or JAX, and when does it help?
- [DL07-201] How do you use TensorBoard and tf.debugging to debug training, for example with scalars, histograms and the profiler?
- [DL07-202] How would you investigate and fix a shape mismatch error in a TensorFlow or Keras model?

## PyTorch and deployment in depth
- [DL07-203] How do you handle class imbalance in PyTorch, for example with WeightedRandomSampler or the pos_weight argument of BCEWithLogitsLoss?
- [DL07-204] How do post-training quantization and quantization-aware training work in PyTorch or TensorFlow, and when is each used?
- [DL07-205] How would you serve a PyTorch model as a REST API, and what do you need to consider when deploying a deep learning model to production?
- [DL07-206] What concerns arise when using PyTorch for real-time inference, and how do you meet a strict latency target?
- [DL07-207] What are graph neural networks, and how are they implemented with libraries such as PyTorch Geometric?

## Python tooling for ML
- [DL07-208] What are the benefits and pitfalls of using Jupyter notebooks for ML work?
- [DL07-209] How can you parallelize Python computations for ML, and how does the GIL affect the choice between threads and processes?
- [DL07-210] Which Python profiling tools, such as cProfile, line_profiler or py-spy, would you use to speed up ML code?

## Framework shape questions
- [DL07-211] What is the output shape of nn.Linear(5, 7) applied to a tensor of shape (3, 5), and what is the shape of its weight matrix?
