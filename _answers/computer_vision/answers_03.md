### DL03-111
- **Decode** efficiently (hardware decoders, PyAV, decord); handle variable frame rate and rotation metadata.
- **Frame sampling:** uniform sampling of T frames across the clip (TSN-style segments) or dense consecutive frames with a stride (e.g. 16 or 32 frames at stride 2–4) for 3D CNNs; resample to a fixed FPS; skip near-duplicate frames for efficiency.
- **Spatial processing:** resize the short side (e.g. 256), then center or random crop (224); apply the **same** crop, flip and color jitter to all frames in a clip so motion stays consistent.
- **Normalize** with per-channel mean and std; arrange as (C, T, H, W) for 3D CNNs or (T, C, H, W).
- **Long videos:** sliding windows or multiple clips at inference, with scores averaged.
- Optionally precompute optical flow (two-stream) or cache features.

### DL03-112
1. **Define** the task, classes, metric and latency or deployment constraints.
2. **Collect and label data:** cover real-world variation (lighting, devices, viewpoints); write labeling guidelines and quality checks.
3. **Split** into train, val and test without leakage (group by source or scene).
4. **Preprocess and augment.**
5. **Baseline:** fine-tune a pretrained CNN or ViT; establish metrics.
6. **Iterate:** error analysis (confusion matrix, failure cases), more or cleaner data, hyperparameter tuning, architecture changes.
7. **Evaluate:** held-out test, robustness and calibration checks, per-slice metrics.
8. **Optimize and deploy:** quantization, ONNX or TensorRT, serving API or edge.
9. **Monitor:** drift, accuracy on sampled production data; retrain loop.

### DL03-113
- **Problem:** N classes, accuracy and F1 target, inference budget.
- **Data:** gather and label images; deduplicate; stratified (and group-aware) split; check class balance.
- **Pipeline:** a dataset class with decode, aspect-aware resize and crop, normalization, and training augmentation (random resized crop, flip, color jitter, RandAugment, Mixup or CutMix).
- **Model:** pretrained ResNet-50, EfficientNet or ConvNeXt with a new linear head; AdamW, cosine learning rate with warmup, label smoothing; mixed precision; early stopping on val loss and F1.
- **Evaluate:** accuracy, macro-F1, confusion matrix, calibration (ECE; temperature scaling), error analysis and slice metrics.
- **Deploy:** export to ONNX or TorchScript; quantize to FP16 or INT8 and verify accuracy; serve behind an API with batching; identical preprocessing.
- **Operate:** logging, drift monitoring, human review of low-confidence cases, periodic retraining with newly labeled data.

### DL03-114
Simple, controlled problem, so start simple:
- **Classical:** grayscale, threshold, find contours, then approxPolyDP to count vertices (3 = triangle, 4 = square, many = circle), plus circularity 4πA/P² ≈ 1 for circles and aspect ratio ≈ 1 for squares. Fast and interpretable, no training.
- **Learning-based:** generate a **synthetic dataset** (random size, position, rotation, color, line width, noise, backgrounds) and train a small CNN (a few conv layers plus GAP plus a 3-way softmax) with rotation and scale augmentation, since shape identity is invariant to them. Add an "other" class if non-shapes can appear.
- **Evaluate** on real or hand-drawn shapes to check the synthetic-to-real gap.

### DL03-115
- **Lighting:** shadows, highlights, low light (noise), color casts change pixel values drastically, though the object is the same.
- **Viewpoint and pose:** 3D objects look very different from different angles; parts self-occlude.
- **Orientation and scale:** CNNs are not rotation-invariant and have limited scale robustness.
- **Intra-class variation** (many chair designs) versus **inter-class similarity** (husky versus wolf).
- **Occlusion, clutter, deformation**, motion blur, low resolution.
- **Dataset bias:** training data covers a narrow slice of conditions (e.g. daytime, canonical views).

Mitigations: diverse data, augmentation (photometric and geometric), multi-view and 3D-aware models, normalization (histogram equalization), and large pretrained models.

### DL03-116
**Likely causes:**
- **Distribution shift:** different cameras, lighting, resolution, compression, user behavior.
- **Data leakage** inflated validation: near-duplicates, the same subjects or scenes in train and val.
- **Training–serving skew:** different preprocessing (BGR/RGB, resize method, normalization, EXIF rotation, color range).
- **Label or class-prior shift**, new classes, open-set inputs.
- **Shortcut learning** (watermarks, backgrounds).
- An unrepresentative validation set.

**Debugging:**
1. Collect and label a sample of production images; measure real accuracy and the confusion matrix.
2. Compare input statistics and embeddings between training and production (drift tests, adversarial validation).
3. Replay production images through the training pipeline to find preprocessing bugs.
4. Re-split validation by source or time and deduplicate.
5. Inspect failures and Grad-CAM for shortcuts.
6. Fix by adding production-like data, augmentation, aligned preprocessing, an OOD rejection option and monitoring.

### DL03-117
- **Measure correctly:** per-class recall and precision, macro-F1, balanced accuracy, PR curves, not overall accuracy.
- **Data level:** collect or augment more minority examples; oversample minority classes (class-balanced sampler) or undersample the majority; synthetic data or GAN and diffusion augmentation, used carefully.
- **Loss level:** class-weighted cross-entropy, focal loss, class-balanced loss (effective number of samples), logit adjustment or balanced softmax, label-distribution-aware margin (LDAM).
- **Training schemes:** two-stage decoupling (learn the representation with instance sampling, then retrain the classifier with balanced sampling), pretrained backbones, metric learning for rare classes.
- **Decision level:** per-class threshold tuning, calibration, prior correction.

### DL03-118
- **Transfer learning:** a strong pretrained backbone (ImageNet, CLIP, DINOv2) used as a frozen feature extractor plus a linear probe or k-NN, then light fine-tuning.
- **Zero- and few-shot:** CLIP zero-shot prompts; prototypical networks or a cosine classifier on embeddings.
- **Self-supervised pretraining** on your unlabeled images (SimCLR, DINO, MAE) before fine-tuning.
- **Semi-supervised learning:** pseudo-labeling and consistency regularization (FixMatch, Mean Teacher) using unlabeled data.
- **Heavy augmentation** and synthetic data.
- **Active learning** to label the most informative images.
- **Regularization:** a small model or head, strong weight decay, early stopping; cross-validation for reliable estimates.

### DL03-119
- **Quantization:** post-training INT8 with a representative calibration set (per-channel weights, per-tensor activations); if accuracy drops, quantization-aware training. FP16 is often near-lossless.
- **Pruning:** structured channel or filter pruning (real speedups on hardware) by magnitude or BN-scale criteria, then fine-tuning; unstructured sparsity needs sparse-kernel support.
- **Distillation:** train a small student (MobileNet or EfficientNet-Lite) to match a large teacher's soft logits and/or features.
- **Combine:** distill, then prune, then quantize; export with TFLite, CoreML or TensorRT.

**Risks to watch:**
- accuracy loss concentrated on **rare classes, small objects or hard slices** (check per-class and per-slice metrics, not just the average);
- **calibration** shifts;
- layers sensitive to quantization (first and last layers, depthwise convs, activations with outliers);
- BN folding errors;
- operator-support fallbacks that kill speed;
- mismatch between simulated and on-device numerics.

Always validate on the device with real data.

### DL03-120
- **Convolution:** the forward pass is y = x ⋆ W (cross-correlation). Backward:
  - **∂L/∂W** = cross-correlation of the input x with the output gradient ∂L/∂y (summed over batch and positions, since weights are shared);
  - **∂L/∂x** = "full" convolution of ∂L/∂y with the kernel **rotated 180°**, which is a transposed convolution (with stride, the gradient is dilated by inserting zeros);
  - **∂L/∂b** = sum of ∂L/∂y over positions.
- **Max pooling:** the gradient flows only to the input position that was the max in each window (switch recorded in the forward pass); others get 0.
- **Average pooling:** the gradient is divided equally among the k² inputs of the window.
- **ReLU:** the gradient passes where the input > 0.

### DL03-121
**Advantages of depth:** hierarchical composition of features (edges → parts → objects), large receptive fields, more nonlinearities, so more expressive functions with fewer parameters than wide shallow networks (depth efficiency) and better generalization in practice.

**Difficulties:**
- vanishing and exploding gradients;
- the degradation problem (optimization gets harder);
- internal signal propagation and initialization sensitivity;
- more memory for activations and longer, sequential compute;
- overfitting with little data.

**Solutions:** residual connections, BatchNorm, careful initialization (He), good optimizers and learning-rate schedules, and regularization.

### DL03-122
- **Size:** 3×3 is the default (stack them for larger receptive fields); 1×1 for channel mixing; a larger first-layer kernel (7×7 stride 2) for a cheap stem; dilation for context without extra cost; small kernels for fine detail; large kernels (7×7 depthwise, as in ConvNeXt) for wide context cheaply.
- **Number:** start small (32–64) and **double the channels each time resolution halves**, keeping compute per layer roughly balanced; widths that are multiples of 8 or 16 for hardware efficiency.
- **Tune** by validation accuracy versus FLOPs and latency; use known scaling rules (EfficientNet compound scaling, RegNet design-space findings) rather than ad-hoc choices.

### DL03-123
The number refers to the dimensions the kernel slides over:
- **1D conv** slides over one axis (time or sequence): audio waveforms, sensor and accelerometer data, ECG, text (over tokens), time series.
- **2D conv** slides over height and width: images, spectrograms, 2D maps; channels are fully connected.
- **3D conv** slides over three axes (time × H × W, or depth × H × W): video clips (spatiotemporal), volumetric medical scans (CT and MRI), voxelized 3D data. Cost and memory grow by an extra K factor, so they are expensive; (2+1)D factorization or pseudo-3D are cheaper.

### DL03-124
- **CNNs:** data with local, translation-invariant structure on a grid; fully parallel; fast. Use cases: images, video frames, spectrograms, local patterns in sequences (1D CNN or TCN for audio and sensors, short-text classification).
- **RNNs (LSTM, GRU):** sequential data where order and long-term state matter and inputs arrive step by step; streaming with constant memory. Use cases: language modeling (pre-transformer), speech recognition, time-series forecasting, handwriting.

Prefer CNNs (or TCNs) when parallel training and speed matter and dependencies are fairly local; prefer RNNs for online and streaming inference with unbounded context. Today transformers have replaced both for many long-range sequence tasks.

### DL03-125
Standard dropout zeroes individual activations independently. In conv feature maps, neighboring pixels are **strongly correlated**, so a dropped pixel's information is recovered from its neighbors: dropout regularizes weakly and adds noise. **Spatial dropout (Dropout2d)** drops **entire channels** (feature maps), forcing the network not to rely on any single feature detector, which is a much stronger, more meaningful regularizer for convs. **DropBlock** drops contiguous spatial blocks for a similar reason. In modern CNNs, dropout is often used only before the final classifier; BN plus augmentation plus weight decay regularize the conv layers, and stochastic depth regularizes residual networks.

### DL03-126
Convert to float, scale to [0, 1] (divide by 255), then **standardize per channel**: x' = (x − μ_c) / σ_c, e.g. ImageNet μ = (0.485, 0.456, 0.406), σ = (0.229, 0.224, 0.225).
**Why:**
- zero-centered, unit-variance inputs give well-conditioned gradients and faster, more stable optimization (matching weight-initialization assumptions);
- it equalizes channel scales so no channel dominates;
- with a pretrained model you **must use the same statistics** it was trained with, or the input distribution shifts and accuracy drops.

For other domains (medical, satellite), compute the statistics on your training set (or use domain-specific normalization such as CT windowing).

### DL03-127
- **Plain resize (stretch):** simple, keeps all content, but distorts shapes; acceptable if objects are large and distortion is consistent between training and test.
- **Resize short side, then center or random crop:** keeps aspect ratio but may cut off content at the edges; the standard for ImageNet classification.
- **Letterbox (resize long side, then pad):** keeps aspect ratio and all content; standard in detection (YOLO); wastes some compute on padding; box coordinates must be adjusted.
- **Alternatives:** aspect-ratio bucketing (batch similar ratios together), models that accept variable sizes (FCN, ViT with interpolated positions, NaViT), tiling for very large images.

Choose based on whether edge content matters and whether shape distortion changes the label; keep training and inference consistent.

### DL03-128
- **Architecture:** efficient backbones (MobileNet, EfficientNet, RegNet), depthwise separable or grouped convs, bottlenecks, early downsampling, fewer channels, smaller input resolution.
- **Numerics:** mixed precision (FP16 or BF16, tensor cores), INT8 quantization at inference.
- **Model compression:** structured pruning, distillation into a smaller student.
- **Systems:** channels-last memory format, cuDNN autotuning, operator fusion (conv + BN + ReLU), torch.compile or TensorRT or ONNX Runtime, larger batches for throughput, efficient data loading (GPU decode, prefetching, caching).
- **Algorithmic:** Winograd or FFT convolutions, early exit, cascades (cheap model first), progressive resizing during training, fewer epochs with better schedules.

### DL03-129
- **Squeeze-and-Excitation (SE):**
  1. **Squeeze** each channel to one value with global average pooling.
  2. **Excite** with a small MLP (reduce by r = 16, ReLU, expand, sigmoid), producing per-channel weights in (0, 1).
  3. **Rescale** the feature maps channel-wise.

  It models channel interdependencies and recalibrates which features matter for this input. About 1–2% ImageNet gain for under 1% extra compute.
- **CBAM:** channel attention (using both average- and max-pooled descriptors), followed by **spatial attention** (pool across channels, 7×7 conv, sigmoid map), so it emphasizes **what** and **where**.

Both add dynamic, input-dependent weighting and some global context to otherwise local convolutions.

### DL03-130
Convolutions are **local**: global context only emerges after many layers, and the **effective receptive field** is much smaller than the theoretical one, so long-range relationships (two distant parts of an object, scene context) are hard to model.
**Fixes:**
- **Dilated convolutions:** exponentially larger receptive field without downsampling (DeepLab).
- **Pyramid pooling and ASPP:** aggregate context at several scales.
- **Non-local blocks:** self-attention over all positions; each output is a weighted sum of features at every location (y_i = Σ_j f(x_i, x_j) g(x_j)).
- **Attention modules** (SE for global channel context, CBAM), transformers and hybrids (ViT, Swin, BoTNet), large-kernel convs (ConvNeXt 7×7, RepLKNet 31×31), global pooling branches.

### DL03-131
Capsule networks (Sabour, Frosst and Hinton, 2017) replace scalar neurons with **capsules**: vectors whose **length** encodes the probability that an entity exists and whose **orientation** encodes its pose (position, rotation, scale). Lower capsules predict higher capsules' poses through learned transformation matrices, and **dynamic routing by agreement** sends output to the parent capsules whose predictions agree.
**Differences from CNNs:**
- they aim for **equivariance** (pose information preserved) instead of the invariance from max pooling, which discards spatial relationships;
- they model part–whole hierarchies explicitly;
- they generalize better to new viewpoints in small experiments.

**Downsides:** slow iterative routing, hard to scale, and no clear advantage on large benchmarks, so they remain mostly a research topic.

### DL03-132
- **Filter visualization:** plot first-layer kernels directly (edges, colors); deeper filters are not directly interpretable.
- **Activation maps:** show the feature maps for an input to see what each channel fires on; find the dataset images or patches that maximally activate a unit.
- **Activation maximization / feature visualization:** optimize an input image to maximize a neuron or channel, with regularizers (jitter, blur) for natural-looking patterns.
- **Saliency and attribution:** vanilla gradients, SmoothGrad, Integrated Gradients, occlusion sensitivity.
- **CAM and Grad-CAM:** weight the last conv feature maps by the global-average-pooled gradients of the class score, sum, apply ReLU and upsample, giving a class-specific heatmap of the image regions driving the prediction. Grad-CAM++ and Score-CAM are variants.

Used to debug shortcut learning, verify localization and explain models.

### DL03-133
BN normalizes with **batch statistics**. Detection and segmentation use large images, so each GPU holds only 1–4 images and the per-batch mean and variance are **noisy, biased estimates**. That gives unstable training, poor running statistics and a train–inference mismatch.
**Alternatives:**
- **SyncBN:** compute statistics across all GPUs.
- **Group Normalization:** normalizes over channel groups within each sample, independent of batch size (the Mask R-CNN and Detectron default).
- **Frozen BN:** use the pretrained statistics and affine parameters fixed, which is common when fine-tuning backbones.
- **LayerNorm** (transformers, ConvNeXt), Instance Norm (style tasks), batch renormalization, or weight standardization combined with GN.

### DL03-134
Training uses **RandomResizedCrop**, which zooms in, so objects look **larger** in training images than in center-cropped test images at the same resolution. The apparent object size differs between training and test (Touvron et al., FixRes). Testing at a somewhat higher resolution makes test objects match the training object scale, so accuracy improves.
**Fixes:**
- **FixRes:** train at a lower resolution (cheaper), then **fine-tune the classifier (and BN statistics)** briefly at the test resolution;
- choose the test resolution about 1.15–1.3× the training resolution;
- progressive resizing; matching test-time crop ratios; multi-scale training.

### DL03-135
- **LeNet-5 (1998):** conv + pooling + FC for digits; established the core design.
- **AlexNet (2012):** deeper and wider, **ReLU**, **dropout**, data augmentation, GPU training, LRN; won ImageNet by a large margin and started the deep learning era.
- **ZFNet (2013):** tuned AlexNet using visualization.
- **VGG (2014):** uniform stacks of **3×3** convs, depth 16–19; simple but heavy (138M parameters).
- **GoogLeNet / Inception (2014):** multi-branch modules, **1×1 reductions**, global average pooling; efficient.
- **ResNet (2015):** **residual connections** plus BN; 50–152+ layers trainable; bottleneck blocks.
- **Later refinements:** DenseNet (dense connectivity), ResNeXt (grouped convs, "cardinality"), SENet (channel attention), MobileNet and ShuffleNet (efficient convs).
- **EfficientNet (2019):** NAS-designed MBConv blocks plus **compound scaling**; best accuracy per FLOP of its time.
- **Afterwards:** RegNet, NFNet, ConvNeXt (2022), and vision transformers.

The trend: deeper, then easier to optimize, then more efficient, then scaled systematically.

### DL03-136
ConvNeXt ("A ConvNet for the 2020s") modernized ResNet-50 step by step using Swin Transformer design choices:
- **training recipe:** AdamW, 300 epochs, Mixup, CutMix, RandAugment, stochastic depth, label smoothing;
- **macro design:** stage compute ratio 1:1:3:1, and a **"patchify" stem** (4×4 conv with stride 4);
- **depthwise convs** (like per-channel attention mixing), wider channels;
- **inverted bottleneck** (expand 4×);
- **large 7×7 depthwise kernels**, with the depthwise conv moved up;
- **fewer activations and norms**, **GELU** instead of ReLU, **LayerNorm** instead of BN;
- separate downsampling layers.

The result matched or beat Swin at the same FLOPs. **Lesson:** much of the ViT advantage came from training recipes and design choices, not attention itself; a pure CNN with modern choices is competitive and often faster and simpler to deploy.

### DL03-137
Global self-attention over all patches is O(N²) in the number of tokens, which is infeasible for high-resolution images.
**Swin:**
- computes self-attention **within local non-overlapping windows** (e.g. 7×7 patches), so cost is **linear in image size**: O(N·M²) for window size M;
- in alternate layers, **shifts the window partition** by half a window (M/2), so tokens near window borders attend across the previous windows' boundaries, connecting windows and growing the receptive field (efficiently implemented with cyclic shift plus attention masks);
- uses **hierarchical patch merging** (2×2 neighboring patches concatenated and projected), halving resolution and doubling channels per stage, which produces multi-scale feature maps like a CNN (strides 4, 8, 16, 32), suitable for FPN-based detection and segmentation;
- adds a relative position bias.

### DL03-138
For an H×W image and patch size P, the number of tokens is N = HW / P².
- **Smaller patches** (e.g. 8 instead of 16) give 4× more tokens: finer detail, typically **higher accuracy**, especially for dense tasks and small objects, but attention cost grows with N² (16× more attention FLOPs and memory) and MLP cost grows with N (4×).
- **Larger patches** (32): cheaper and faster, coarser, lower accuracy.

ViT naming (ViT-B/16, B/32) shows this trade-off; FlexiViT trains one model for multiple patch sizes.

### DL03-139
Self-attention costs O(N²·D) FLOPs and O(N²) memory for the attention matrix, with N = HW/P². Doubling image resolution gives 4× the tokens and **16× the attention cost**. Dense prediction (detection, segmentation) needs **high-resolution inputs and fine feature maps** (e.g. 1024×1024 with stride 4–8), where N reaches tens of thousands of tokens, so global attention becomes prohibitively expensive in compute and memory.
**Solutions:** windowed or local attention (Swin), deformable attention (attend to a few sampled points), hierarchical or pyramid ViTs with spatial-reduction attention (PVT), linear or efficient attention, FlashAttention to cut memory, and plain ViT backbones with windowed blocks plus a few global blocks (ViTDet).

### DL03-140
- Keep the **patch size** fixed, so a higher resolution gives **more tokens**.
- The learned 1D position embeddings were trained for a fixed grid (e.g. 14×14 for 224/16). Reshape them to 2D and **interpolate** (bicubic) to the new grid (e.g. 24×24 for 384), keeping the CLS embedding separate.
- Then **fine-tune** at the new resolution (usually with a lower learning rate) so the network adapts to the interpolated positions and the new object scale.
- Relative position bias tables (Swin) are interpolated similarly.

Higher-resolution fine-tuning typically improves accuracy (e.g. ViT at 384) at roughly 3× compute.

### DL03-141
The CLS token is an extra **learnable embedding** prepended to the patch tokens. Through self-attention it aggregates information from all patches, and its final state is fed to the classification head (inherited from BERT).
**Global average pooling** of the final patch tokens is an alternative: it is equally good or better with the right learning rate, it avoids a special token, and it is often preferred in newer models (DeiT III, MAE fine-tuning). CLS can learn an adaptive weighting of patches (attention maps from CLS give useful saliency, as in DINO); GAP treats all patches equally and is more translation-robust. Some models use both (e.g. distillation tokens).

### DL03-142
**Choose a CNN when:**
- data is limited and there is no strong pretrained ViT;
- deployment is on **edge or mobile** hardware with mature conv kernels and INT8 support;
- strict latency at high resolution (convs scale linearly with pixels);
- dense tasks needing multi-scale features cheaply;
- the team needs simplicity and robustness (BN folding, quantization).

**Choose a ViT when:**
- large-scale pretrained weights exist (CLIP, DINOv2, MAE) and transfer matters;
- abundant data or compute;
- you need global context or multimodal integration (VLMs);
- you want the best accuracy at server scale;
- the hardware has efficient attention (GPUs or TPUs with FlashAttention).

**Hierarchical hybrids** (Swin, ConvNeXt, EfficientViT) are a common compromise. Benchmark both on the target device and data.

### DL03-143
Hybrids combine convolutions and attention:
- a **conv stem or early stages** (e.g. ResNet stages, CoAtNet, the convolutional stem in ViTC) provide **locality, translation equivariance, efficient high-resolution processing** and faster, more stable training with less data;
- **transformer blocks in later stages** at low resolution provide **global context and content-dependent interactions** where N is small, so attention is affordable.

Examples: the original ViT-hybrid (ResNet features into ViT), BoTNet (self-attention replacing 3×3 convs in the last ResNet stage), CoAtNet, CvT (convolutional projections), MobileViT and EfficientViT (mobile), DETR (CNN backbone plus transformer). They often achieve better accuracy and efficiency trade-offs than pure CNNs or pure ViTs, especially at moderate data scale.
