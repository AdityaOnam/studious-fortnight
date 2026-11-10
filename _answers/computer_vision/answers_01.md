### DL03-001
A CNN is a neural network whose core layers are **convolutions**: small learnable filters (e.g. 3×3) slide over the image and compute a dot product with each local patch, producing a feature map.
- Stacking conv → nonlinearity (ReLU) → occasional downsampling (pooling or stride) builds a hierarchy: edges → textures → parts → objects.
- Each layer sees a larger region of the input (growing receptive field) while sharing weights across positions.
- A head (global pooling + fully connected/softmax layer) turns the final feature maps into class scores.
- Training is standard backpropagation with SGD/Adam on a loss such as cross-entropy.

### DL03-002
Typical block: **Conv → BatchNorm → ReLU**, repeated, with downsampling every few blocks, then a head.
- **Convolution:** learns local feature detectors; output channels = number of filters.
- **Normalization (BN):** stabilizes activations, allows higher learning rates.
- **Activation (ReLU/GELU):** adds nonlinearity.
- **Pooling / strided conv:** reduces spatial size, increases receptive field, adds small-shift invariance.
- **Residual connections (modern CNNs):** keep gradients flowing in deep stacks.
- **Global average pooling + FC + softmax:** aggregates spatial features into a vector and maps it to class probabilities.
- **Dropout (head):** regularization.

### DL03-003
- **Parameter efficiency:** a fully connected layer on a 224×224×3 image with 1,000 hidden units needs ~150M weights; a 3×3×3×64 conv needs 1,728.
- **Locality prior:** nearby pixels are correlated; convolutions model local patterns directly.
- **Weight sharing / translation equivariance:** the same detector works anywhere in the image, so the network does not have to relearn a pattern at every position.
- **Hierarchy:** stacked convs compose simple features into complex ones.
- Result: far less overfitting, less data needed and better generalization than an MLP on raw pixels, which ignores spatial structure entirely (permuting pixels would not change what it can learn).

### DL03-004
- **Fully connected:** every output connects to every input; weights = in × out; no notion of spatial position; input size fixed.
- **Convolutional:** each output connects only to a local K×K×C_in window (sparse connectivity), and the same kernel is reused at every position (weight sharing); weights = K·K·C_in·C_out, independent of image size; output keeps a spatial layout; works on any input size.
- A conv layer is a fully connected layer with a constrained (sparse, shared, Toeplitz-structured) weight matrix. Conversely an FC layer equals a conv whose kernel covers the whole input.

### DL03-005
A traditional (fully connected) network flattens the image into a vector and learns a separate weight for every pixel-unit pair. A CNN keeps the 2D grid and uses local, shared filters. Consequences:
- CNNs exploit spatial structure and are translation-equivariant; MLPs are not.
- CNNs have orders of magnitude fewer parameters for the same input.
- CNNs learn hierarchical features automatically, which replaced hand-crafted features (SIFT, HOG) plus a shallow classifier.
- CNNs accept variable input sizes (with global pooling); MLPs need a fixed input length.

### DL03-006
A feature map is the 2D output produced by applying **one filter** across the whole input (plus bias and activation). A conv layer with N filters outputs N feature maps stacked into an H×W×N tensor. Each value measures how strongly that filter's pattern is present at that location. Early feature maps respond to edges and colors; deeper ones to textures, parts and whole objects.

### DL03-007
Filters learn the patterns that reduce the loss.
- **Early layers:** low-level, generic detectors that resemble Gabor filters: oriented edges, color blobs, simple gradients. These are similar across datasets and transfer well.
- **Middle layers:** textures, corners, repeated motifs, simple shapes.
- **Deep layers:** large receptive fields; class-specific parts and objects (faces, wheels, text), increasingly invariant to position and pose.
This is why fine-tuning often freezes early layers and retrains deep layers for a new task.

### DL03-008
Parameter sharing means one kernel (one set of weights) is applied at every spatial position, instead of learning separate weights per position.
- **Fewer parameters:** the count depends on kernel size and channels, not image size; this reduces overfitting and memory.
- **Translation equivariance:** a pattern detected in one place is detected anywhere.
- **Better statistical efficiency:** every position provides a training signal for the same weights.
It is the right prior when the same feature can appear anywhere. It is less suitable when position matters (e.g. aligned faces), which is why some models use locally connected layers or positional information.

### DL03-009
A conv kernel always spans **all input channels**.
- **Grayscale (1 channel):** each filter is K×K×1.
- **RGB (3 channels):** each filter is K×K×3; it convolves each channel and **sums** the results plus a bias, giving one 2D map.
- The **next layer's shape** is H_out × W_out × N, where N = number of filters, and H_out = ⌊(H + 2P − K)/S⌋ + 1 (same for W).
- So the next layer's kernels must be K×K×N.

### DL03-010
The depth of a conv layer is the **number of filters**, which equals the number of output channels (feature maps). Depth sets how many different features the layer can detect, and it becomes the channel depth of the next layer's input. (Network depth, the number of layers, is a different concept.)

### DL03-011
The fully connected head maps the learned feature vector to class scores. It combines features globally ("wheels + windows + road → car"), and its final layer has one output per class, followed by softmax. Older networks (AlexNet, VGG) had large FC stacks holding most of the parameters (~120M of VGG-16's 138M). Modern networks use global average pooling plus a single linear layer, which needs far fewer parameters and overfits less.

### DL03-012
Yes. An FC layer on a k×k×C feature map is equivalent to a k×k convolution with C_out filters, and later FC layers become 1×1 convolutions. This gives a **fully convolutional network**:
- It accepts inputs larger than the training size.
- In one forward pass it produces a spatial **map of predictions**, equivalent to sliding the classifier over the image but sharing computation (OverFeat; the basis of FCN segmentation and dense detection).
- Inference on large images is much cheaper than cropping windows and running the network repeatedly.

### DL03-013
Often yes. **1D convolutions** over time capture local temporal patterns (waveform shapes, sensor motifs) efficiently, with shift equivariance in time.
- **Raw audio:** 1D CNNs (WaveNet-style, dilated convs for long context).
- **Spectrograms:** 2D CNNs treat time-frequency as an image (common in speech and audio classification).
- **Sensor and accelerometer data, ECG:** 1D CNNs or temporal convolutional networks are strong and cheaper than RNNs.
- **Caveats:** very long-range dependencies need dilation, pooling or attention; if the signal is not locally structured or is mostly tabular features, simpler models may do better.

### DL03-014
- **Data augmentation:** flips, crops, color jitter, Mixup/CutMix (the most effective lever).
- **Weight decay (L2)** and **dropout** (mainly in the head, or spatial dropout).
- **Batch normalization** (mild regularizing effect).
- **Global average pooling** instead of big FC layers, to reduce parameters.
- **Transfer learning** from pretrained weights when data is small.
- **Early stopping**, label smoothing, stochastic depth.
- Matching model capacity to the amount of data.

### DL03-015
Weights = K × K × C_in × C_out = 3 × 3 × 64 × 128 = **73,728**. Biases = 128. Total = **73,856** parameters. (If followed by BatchNorm, the bias is usually dropped and BN adds 2 × 128 learnable parameters plus 2 × 128 running statistics.)

### DL03-016
Standard order: **Conv → BN → ReLU** (in pre-activation ResNets: BN → ReLU → Conv).
- BN normalizes each channel using the batch mean and variance over (N, H, W), then applies a learnable scale γ and shift β per channel.
- The conv bias becomes redundant (BN's β replaces it), so use bias=False.
- **Training effects:** smoother loss landscape, so higher learning rates work; less sensitivity to initialization; faster convergence; mild regularization from batch noise.
- At inference it uses running averages of the statistics, and it can be folded into the preceding conv weights for speed.

### DL03-017
Padding adds pixels (usually zeros) around the border before convolving.
- **Preserves spatial size:** "same" padding with P = (K − 1)/2 for stride 1 keeps H×W, so deep networks do not shrink to nothing.
- **Uses border information:** without padding, edge pixels take part in fewer outputs.
- **Types:** zero, reflect, replicate, circular. "Valid" means no padding (the output shrinks by K − 1).
- Zero padding can leak absolute-position cues and create border artifacts; reflect padding reduces this in image-to-image tasks.

### DL03-018
Stride is the step size of the kernel as it slides. Stride S downsamples the output by roughly a factor of S in each dimension: H_out = ⌊(H + 2P − K)/S⌋ + 1. Stride 2 halves the resolution, cuts compute roughly 4× for later layers and enlarges the receptive field. Large strides can skip information and cause aliasing.

### DL03-019
**H_out = ⌊(H_in + 2P − K) / S⌋ + 1**, and the same for width.
- With dilation D, use the effective kernel K_eff = D(K − 1) + 1.
- Example: 224 input, K = 7, P = 3, S = 2 gives ⌊(224 + 6 − 7)/2⌋ + 1 = 112.
- For transposed convolution: H_out = (H_in − 1)·S − 2P + K + output_padding.

### DL03-020
The receptive field (RF) is the region of the input image that can influence a given activation.
- **Recursion:** RF_l = RF_(l−1) + (K_l − 1) × (product of the strides of all previous layers), with RF_0 = 1.
- Example: three 3×3 stride-1 convs give RF = 7. A stride-2 layer doubles the growth rate of every later layer.
- RF grows linearly with depth for stride 1 and exponentially with downsampling or dilation.
- The **effective** RF is smaller and roughly Gaussian: central pixels dominate.
- Detection and segmentation need an RF large enough to cover the objects and their context.

### DL03-021
Two stacked 3×3 convs have the RF of one 5×5; three have the RF of one 7×7 (VGG's insight).
- **Fewer parameters:** 3 × (3²C²) = 27C² versus 49C² for a 7×7, about 45% fewer.
- **More nonlinearities:** three ReLUs instead of one, so the function is more expressive.
- **Hardware efficiency:** 3×3 convs are highly optimized (Winograd).
- Trade-off: more layers mean more sequential steps and activation memory.

### DL03-022
A dilated (atrous) convolution inserts gaps of D − 1 between kernel taps, so a 3×3 kernel with dilation 2 covers a 5×5 area using only 9 weights.
- It grows the receptive field exponentially when stacked, **without downsampling or extra parameters**.
- **Uses:** semantic segmentation (DeepLab keeps high resolution with large context), audio generation (WaveNet), dense prediction.
- **Pitfall:** gridding artifacts when all layers use the same dilation; mix the rates (hybrid dilated convolution).

### DL03-023
A 1×1 convolution is a per-pixel linear map across channels, like an FC layer applied at every location.
- **Changes channel count:** reduces it (bottleneck) or expands it cheaply.
- **Mixes channel information** and adds nonlinearity (network-in-network).
- **Inception:** 1×1 reductions before the expensive 3×3 and 5×5 branches cut FLOPs dramatically.
- **ResNet bottleneck:** 1×1 reduce (e.g. 256 → 64), 3×3 at the low width, 1×1 expand back (64 → 256).
- Also used for projection shortcuts and as the pointwise step of depthwise separable convs.

### DL03-024
It factorizes a standard convolution into:
1. a **depthwise** convolution: one K×K filter per input channel, giving spatial filtering only, and
2. a **pointwise** 1×1 convolution that mixes channels.
**Advantages:** about 8–9× fewer FLOPs and parameters for 3×3 kernels with little accuracy loss, which makes it the basis of MobileNet, Xception and EfficientNet. **Drawbacks:** lower arithmetic intensity, so it is memory-bound on GPUs and real speedups are smaller than the FLOP reduction; slightly less expressive per layer.

### DL03-025
For an H×W output, kernel K, C_in input and C_out output channels:
- **Standard:** H·W·K²·C_in·C_out multiply-adds; parameters K²·C_in·C_out.
- **Depthwise separable:** H·W·K²·C_in + H·W·C_in·C_out; parameters K²·C_in + C_in·C_out.
- **Ratio** = 1/C_out + 1/K². For K = 3 and C_out = 256 that is ≈ 0.115, about 8.7× cheaper.

### DL03-026
A transposed convolution ("deconvolution") is a learnable upsampling layer: the gradient of a strided convolution with respect to its input. Each input pixel scatters a weighted copy of the kernel into a larger output, and overlapping contributions are summed.
- **Checkerboard artifacts:** when the kernel size is not divisible by the stride (e.g. K = 3, S = 2), some output pixels receive contributions from more input pixels than their neighbors, producing a periodic uneven pattern.
- **Fixes:** use K divisible by S (K = 4, S = 2), or replace it with resize (bilinear or nearest) followed by a normal conv, or use pixel shuffle (sub-pixel convolution).

### DL03-027
- **MACs** = H_out · W_out · K_h · K_w · C_in · C_out / groups; **FLOPs ≈ 2 × MACs** (a multiply and an add). Add bias and activation if needed.
- **Why FLOPs mispredict latency:**
  - **Memory bandwidth:** depthwise and 1×1 convs and element-wise ops are memory-bound.
  - **Kernel launch overhead** and the number of layers (depth versus width).
  - **Parallelism and hardware utilization:** small tensors, odd channel counts not multiples of 8 or 16.
  - **Operator support and fusion** on the target (TensorRT, NPUs), data layout conversions, precision (INT8 or FP16 tensor cores).
  - **Pre- and post-processing** (NMS, resizing) are not in the FLOP count.
- Always benchmark on the target device.

### DL03-028
Pooling summarizes a local window into one value.
- **Purpose:** downsample (less compute and memory), enlarge the receptive field, add robustness to small translations and distortions, and control overfitting.
- **Types:** max pooling, average pooling, global average or max pooling (whole map to one value), L2 or stochastic pooling, RoI pooling and RoIAlign (detection), spatial pyramid pooling (multi-scale, fixed-length output), adaptive pooling (output size fixed regardless of input).

### DL03-029
- **Max pooling** keeps the strongest activation: "is the feature present anywhere in this window". It preserves sharp, sparse features and is more invariant to small shifts. Common inside classification backbones.
- **Average pooling** keeps the mean response: smoother, retains information from the whole window, less noisy gradients. Preferred for **global** pooling before the classifier, and when overall intensity or texture matters.
- Max pooling sends gradient only to the argmax position; average pooling spreads it evenly.

### DL03-030
For classification, what matters is **whether** a discriminative feature occurs, not exactly where. Max pooling acts like a detector "OR" over the window: it keeps the strongest evidence, discards weak responses and background noise, gives invariance to small translations and reduces resolution cheaply. Empirically it outperformed average pooling inside classic CNNs (AlexNet, VGG). Many modern networks replace it with strided convolutions and use global average pooling only at the end.

### DL03-031
- **Equivariance:** shifting the input shifts the output by the same amount: f(T(x)) = T(f(x)). Convolution with weight sharing is translation-**equivariant** (up to border effects and stride).
- **Invariance:** the output does not change: f(T(x)) = f(x). CNNs gain approximate translation **invariance** from pooling, striding and finally global pooling, which discard position.
- In practice CNNs are not perfectly invariant: striding and pooling cause aliasing, so one-pixel shifts can change predictions (fixed by anti-aliased blur pooling), and zero padding leaks absolute position.

### DL03-032
No. Standard CNNs are **not rotation-invariant**: convolution is equivariant to translation only. A rotated image activates different filters, so predictions can change or degrade, especially for large rotations or orientation-dependent classes (6 versus 9).
**Remedies:**
- rotation augmentation during training (learned approximate invariance);
- test-time augmentation (average over rotations);
- rotation-equivariant architectures (group-equivariant CNNs, harmonic or steerable filters);
- spatial transformer networks that learn to canonicalize orientation.
Some tasks, such as aerial imagery or microscopy, need full rotation invariance; others, such as natural photos, do not.

### DL03-033
GAP averages each final feature map to a single number, turning an H×W×C tensor into a C-dimensional vector, followed by one linear layer.
- **No parameters**, versus tens of millions in VGG-style FC heads, so it overfits less.
- **Any input size:** spatial dimensions are averaged away.
- **Interpretability:** each channel acts as a class-evidence map, which enables CAM and Grad-CAM localization.
- Introduced by Network-in-Network and used by GoogLeNet, ResNet and EfficientNet.

### DL03-034
Yes ("all-convolutional net").
- **Pros:** the downsampling is **learned**; it is more expressive; it is common in modern designs (ResNet stems and stages, GAN discriminators where max pooling hurts gradients).
- **Cons:** extra parameters and FLOPs; slightly less built-in invariance; can alias (pooling or a blur before the stride helps).
- Pooling remains a cheap, parameter-free choice when you just need robust downsampling.

### DL03-035
Local response normalization (from AlexNet) normalizes each activation by the summed squares of activations in **neighboring channels** at the same position: b = a / (k + α Σ a_j²)^β. It mimics lateral inhibition, so strongly firing channels suppress their neighbors, which encourages competition and was said to help generalization. It is obsolete: batch normalization (and later layer or group norm) gives much larger, more reliable benefits, and VGG reported LRN did not help.

### DL03-036
- **Classic:** LeNet-5, AlexNet (ReLU, dropout, GPUs), ZFNet, VGG (stacked 3×3), GoogLeNet/Inception (multi-branch, 1×1 reductions).
- **Residual era:** ResNet, ResNeXt (grouped convs), DenseNet (dense connections), Wide ResNet, SENet (channel attention).
- **Efficient:** MobileNet v1–v3, ShuffleNet, SqueezeNet, EfficientNet (compound scaling), RegNet.
- **Modern:** ConvNeXt (CNN modernized with transformer design choices), NFNet, and transformer backbones (ViT, DeiT, Swin).

### DL03-037
torchvision, timm, Keras Applications and the Hugging Face Hub provide ImageNet-pretrained ResNet-18/34/50/101/152, ResNeXt, Wide-ResNet, DenseNet, VGG-11/16/19, Inception-v3, GoogLeNet, MobileNet v2/v3, EfficientNet B0–B7 and V2, RegNet, ConvNeXt, ViT, DeiT and Swin. timm alone offers hundreds of variants with different pretraining (ImageNet-21k, CLIP, self-supervised). Detection and segmentation zoos (torchvision, Detectron2, MMDetection, Ultralytics) add Faster/Mask R-CNN, RetinaNet, DETR, YOLO, DeepLab and SAM.

### DL03-038
VGG used a uniform recipe: only 3×3 convolutions with stride 1 and padding 1, 2×2 max pooling with stride 2, channels doubling after each pool (64 → 512), and depth 16–19.
- **Simplifications:** one block design repeated; stacked small kernels give large receptive fields with fewer parameters and more nonlinearities.
- **Drawbacks:** ~138M parameters (most in the FC layers), ~15.5 GFLOPs per 224² image, slow and memory-hungry, hard to train deeper without residuals, worse accuracy per FLOP than ResNet or EfficientNet. Still used as a feature extractor (perceptual and style losses).

### DL03-039
Inception addressed **what kernel size to use** and how to go deep and wide without exploding compute. Objects appear at different scales, so an Inception module runs **parallel branches** (1×1, 3×3, 5×5 convs and 3×3 max pooling) and concatenates their outputs along channels, letting the network choose the useful scales. **1×1 convolutions before the 3×3 and 5×5 branches** reduce channels, making this affordable. GoogLeNet reached top ImageNet accuracy (2014) with ~6.8M parameters (12× fewer than AlexNet). Later versions factorized 5×5 into two 3×3, and n×n into 1×n plus n×1.

### DL03-040
ResNets (2015) made **very deep networks trainable** (152 layers on ImageNet, 1,000+ on CIFAR) by learning residual functions with identity shortcuts. They solved the degradation problem, won ILSVRC 2015 (3.57% top-5 error), and became the default backbone for detection, segmentation and transfer learning. Residual connections are now ubiquitous, including in transformers.

### DL03-041
A residual block computes **y = x + F(x)**, where F is a few conv-BN-ReLU layers and the skip connection adds the input unchanged (a 1×1 projection if shapes differ).
- **Easy identity:** if extra layers are not needed, F can go to zero, so adding depth cannot make the optimum worse.
- **Gradient flow:** ∂y/∂x = I + ∂F/∂x, so gradients reach early layers directly through the identity path even when ∂F/∂x is small, which avoids vanishing gradients.
- **Better conditioned loss landscape** and an implicit ensemble of many shallower paths.

### DL03-042
This is the **degradation problem**: deeper plain networks have **higher training error**, not just test error, so it is an optimization issue, not overfitting.
- It is hard for stacked nonlinear layers to learn even the identity mapping.
- Gradients become small or noisy through many layers (vanishing gradients, mostly handled by BN, but optimization stays poor).
- Signal propagation degrades and the loss surface becomes more chaotic.
Residual connections fix this by making the identity the default.

### DL03-043
A bottleneck block (ResNet-50 and deeper) uses three layers: **1×1 conv reduces channels** (e.g. 256 → 64), a **3×3 conv** operates at the reduced width, and a **1×1 conv expands back** (64 → 256), with the skip connection around them. The expensive 3×3 runs on 4× fewer channels, so a block costs about the same as a basic two-layer 3×3 block at lower width while allowing much deeper and wider networks. ResNet-50 has ~25.6M parameters and ~4.1 GFLOPs.

### DL03-044
- **MobileNet v1:** depthwise separable convolutions (8–9× fewer FLOPs); a width multiplier α and resolution multiplier ρ to trade accuracy for speed.
- **MobileNet v2:** inverted residual blocks (expand with 1×1, depthwise 3×3, project with 1×1), linear bottlenecks (no ReLU on the narrow output, to avoid losing information), shortcuts between narrow layers.
- **MobileNet v3:** NAS-designed architecture, squeeze-and-excitation, h-swish activation, a cheaper last stage.
- They are designed for low latency and memory on mobile CPUs and NPUs and quantize well to INT8.

### DL03-045
EfficientNet scales **depth, width and resolution together** with one coefficient φ: depth ∝ α^φ, width ∝ β^φ, resolution ∝ γ^φ, under α·β²·γ² ≈ 2 (each step roughly doubles FLOPs). Grid search on B0 gave α = 1.2, β = 1.1, γ = 1.15.
**Why it is better:** the dimensions are interdependent. Higher resolution needs more depth (a bigger receptive field) and more width (finer patterns). Scaling only one saturates quickly. Balanced scaling reached better accuracy per FLOP (B7: 84.3% top-1 with 66M parameters, 8.4× smaller than the previous best).

### DL03-046
1. Define the target: the device (GPU, mobile CPU, NPU, Jetson), runtime (TensorRT, CoreML, TFLite), precision (FP16 or INT8), batch size, latency budget (e.g. p95 < 20 ms) and accuracy floor.
2. Shortlist families that fit the hardware (MobileNetV3, EfficientNet-Lite, RegNet, ResNet-18/50, small ConvNeXt or YOLO variants) and **benchmark them on the actual device**, then fine-tune the best on your data.
3. **Why the metrics disagree:**
   - Parameter count measures memory and size, not compute (a 3×3 conv on a large map has few weights but many FLOPs).
   - FLOPs ignore memory traffic: depthwise convs and element-wise ops are bandwidth-bound.
   - Latency depends on parallelism, kernel launches, layer count, operator fusion and support, data layout, and quantization support.
   - So a low-FLOP model can be slower than a "heavier" ResNet on a GPU.

### DL03-047
Transformers process a sequence of tokens with self-attention, so any modality that can be tokenized works:
- **Vision:** split images into patches (ViT) for classification; DETR for detection; Mask2Former and SegFormer for segmentation; video transformers (TimeSformer, ViViT); Swin as a general backbone.
- **Multimodal:** CLIP aligns image and text; VLMs (LLaVA and others) feed image tokens into an LLM.
- **Beyond NLP:** speech (Whisper), protein structure (AlphaFold), time series, RL (decision transformer), point clouds, graphs.
Their advantage is global context and scalability with data; their cost is quadratic attention and weaker inductive biases.

### DL03-048
1. Split the H×W×C image into non-overlapping P×P patches, giving N = HW/P² patches (224² with P = 16 gives 196).
2. Flatten each patch (P²·C values) and apply a learned linear projection to dimension D. This is equivalent to a conv with kernel = stride = P.
3. Prepend a learnable [CLS] token (optional).
4. Add learned 1D position embeddings, since attention is permutation-invariant.
5. Feed the N + 1 tokens to a standard transformer encoder; classify from CLS (or the mean of the patch tokens) with an MLP head.

### DL03-049
CNNs build in **locality** (each unit sees a small neighborhood), **translation equivariance** (weight sharing), and a **hierarchical, multi-scale** structure with pooling. ViTs only have patchification and learned position embeddings; attention is global from layer one, and spatial relations must be learned from data.
**Consequence:** with small or medium datasets ViTs underperform CNNs and overfit; with very large datasets (JFT, LAION) or strong pretraining they match or beat CNNs, because fewer built-in assumptions mean a higher ceiling. Hybrid and local-attention designs (Swin, ConvNeXt-style choices) put some biases back.

### DL03-050
Because they lack locality and translation priors (DL03-049), ViTs must learn these regularities from data, so they have higher sample complexity and overfit small datasets. They also have weaker gradients early in training and less built-in invariance.
**Remedies:** pretraining on huge datasets (ImageNet-21k, JFT) or self-supervised pretraining (MAE, DINO); the DeiT recipe of strong augmentation (RandAugment, Mixup, CutMix, random erasing), stochastic depth, label smoothing, long schedules with AdamW and warmup, and distillation from a CNN teacher; or adding convolutional stems or local attention.

### DL03-051
CLIP trains an image encoder and a text encoder so that matching image–caption pairs have high cosine similarity in a shared embedding space (400M web pairs, contrastive loss).
**Zero-shot classification:**
1. Write each class name as a prompt ("a photo of a {class}"), often averaging several templates.
2. Encode the prompts into text embeddings, which act as classifier weights.
3. Encode the image and compute cosine similarity to each class embedding; softmax gives probabilities.
No task-specific training is needed; new classes are added just by writing text. Accuracy depends on prompt wording and on whether the concept was common in the pretraining data.

### DL03-052
They create a learning signal from the data itself:
- **SimCLR (contrastive):** two random augmentations of the same image are pulled together in embedding space and pushed away from other images in the batch (InfoNCE loss). The network learns augmentation-invariant semantic features.
- **DINO (self-distillation):** a student network matches the output distribution of a momentum (EMA) teacher across different crops (global and local); centering and sharpening the teacher output prevent collapse. It produces features with emergent object segmentation.
- **MAE (masked autoencoding):** mask ~75% of patches and reconstruct their pixels from the visible ones, which forces the model to learn shape and context.
The pretrained encoder is then used for linear probing or fine-tuning on downstream tasks with few labels.

### DL03-053
- **Narrow, well-defined domain with plenty of labels** (industrial defects, medical scans, specific product SKUs): a supervised CNN learns domain-specific cues that a VLM never saw.
- **Fine-grained distinctions** (bird species, part numbers), counting, precise localization: VLMs are weak at these.
- **Strict latency, cost or edge deployment:** a small CNN runs in milliseconds on-device.
- **Need for calibrated, deterministic, auditable outputs** and a fixed label set.
- **Images unlike web photos** (X-ray, SAR, microscopy), where pretraining coverage is poor.
VLMs win at open-ended, zero-shot, long-tail or language-dependent tasks.

### DL03-054
**Image captioning** is an encoder–decoder problem:
- **Classic:** a CNN encoder plus an LSTM decoder generating words, with **attention** over spatial features (Show, Attend and Tell). Trained with cross-entropy (teacher forcing), then often fine-tuned with RL on CIDEr (self-critical sequence training).
- **Modern:** a vision transformer or CLIP encoder plus a transformer or LLM decoder (BLIP, GIT, CoCa, LLaVA-style VLMs), pretrained on large image–text corpora.
- **Decoding:** beam search or sampling.
- **Evaluation:** BLEU, METEOR, CIDEr, SPICE, CLIPScore, plus human judgment for hallucinated objects.

### DL03-055
Augmentations are label-preserving transformations of training images (flips, crops, color changes and so on). They are needed because:
- they enlarge the effective dataset and reduce overfitting;
- they teach invariances you care about (position, scale, lighting) that the architecture does not guarantee;
- they improve robustness to real-world variation (camera, weather, viewpoint);
- they are essential for data-hungry models (ViTs) and for self-supervised contrastive learning, where augmentations define what "similar" means.

### DL03-056
- **Geometric:** horizontal or vertical flip, random resized crop, rotation, scaling, translation, shear, affine and perspective warps, elastic deformation.
- **Photometric:** brightness, contrast, saturation, hue jitter, gamma, grayscale, blur, noise, JPEG compression, sharpening.
- **Occlusion and mixing:** Cutout and random erasing, Mixup, CutMix, Mosaic (YOLO), copy-paste (instance segmentation).
- **Learned or automated policies:** AutoAugment, RandAugment, TrivialAugment, AugMix.
- **Domain-specific:** weather and fog simulation, stain normalization (pathology), style transfer, synthetic rendering.

### DL03-057
Augmentation regularizes the model by exposing it to plausible variations of each training image, so it learns features that are invariant to nuisance factors instead of memorizing pixels. Effects: lower variance and overfitting, better out-of-distribution robustness and often better calibration (Mixup).
**Techniques:** random resized crop and flip (the baseline), color jitter, RandAugment or AutoAugment, Mixup and CutMix, random erasing, Mosaic and copy-paste for detection, test-time augmentation at inference.
Tune strength to model size: large models and ViTs benefit from heavy augmentation, small models from lighter.

### DL03-058
Augmentation is harmful when it **changes the label** or creates **impossible inputs**:
- **Digits and text:** rotating 180° turns 6 into 9; horizontal flips make letters invalid; heavy shear changes 1 versus 7.
- **Medical imaging:** left–right flips can swap anatomical side (situs, laterality); color jitter can destroy stain-based diagnostic cues in pathology; intensity changes can alter CT Hounsfield units that carry meaning; aggressive crops can remove the lesion.
- **Traffic signs and directions:** flipping "turn left" into "turn right".
- **Fine-grained or counting tasks:** CutMix or crops can remove the discriminative part or change the count.
Rule: only use transformations under which the label is genuinely invariant.

### DL03-059
- **Cutout / random erasing:** blank out a random rectangle. This forces the model to use multiple parts of the object instead of one discriminative patch.
- **Mixup:** blend two images and their labels: x = λx₁ + (1 − λ)x₂, y = λy₁ + (1 − λ)y₂, with λ ~ Beta(α, α). This encourages linear behavior between classes, smoother decision boundaries and better calibration.
- **CutMix:** paste a patch from image B into image A; the label is mixed in proportion to the patch area. It keeps natural local statistics (unlike Mixup's ghosting) and combines occlusion robustness with label mixing.
All three act as strong regularizers, reduce overconfidence and improve robustness and localization.

### DL03-060
Transfer learning reuses a model trained on a large source task (e.g. ImageNet) as the starting point for a target task.
**In practice:**
1. Load pretrained weights.
2. Replace the task head (new classifier with the right number of classes).
3. Either freeze the backbone and train only the head (feature extraction), or fine-tune some or all layers with a small learning rate.
It gives faster convergence, much better accuracy with limited data and lower compute. It is the default for almost all practical vision tasks.
