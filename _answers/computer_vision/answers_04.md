### DL03-144
**SimCLR:**
1. Each image x gets two random augmentations (crop + resize, color jitter, blur), giving x_i and x_j, a **positive pair**.
2. An encoder (ResNet) plus a projection MLP maps them to z_i and z_j.
3. The **NT-Xent / InfoNCE loss** pulls positives together and pushes away all other 2(N − 1) samples in the batch (negatives): ℓ = −log[exp(sim(z_i, z_j)/τ) / Σ_(k≠i) exp(sim(z_i, z_k)/τ)], with cosine similarity and temperature τ.
4. After pretraining, drop the projection head and use the encoder features.

**Why large batches or many negatives:** the loss estimates a contrast against the data distribution. More negatives give a tighter mutual-information bound, harder negatives and a better-conditioned gradient, which prevents trivial solutions. SimCLR needed batches of 4096–8192. MoCo avoids the large batch with a **momentum encoder plus a queue** of past negatives (65k).

### DL03-145
Without negatives, the trivial solution is collapse: every image maps to the same vector. They avoid it through **architectural asymmetry and target design**:
- **BYOL:** an online network (with an extra **predictor** MLP) predicts the output of a **target network** whose weights are an **exponential moving average** of the online weights, and the target receives **no gradient** (stop-gradient). The predictor plus slowly moving target creates dynamics that do not converge to collapse (SimSiam shows stop-gradient plus predictor alone suffices).
- **DINO:** self-distillation where a student matches the softmax output of an EMA teacher across multi-crop views (global and local crops). Collapse is prevented by **centering** the teacher outputs (subtract a running mean, which stops one dimension dominating) and **sharpening** them (low teacher temperature, which stops a uniform output). The two balance each other.

Other approaches: Barlow Twins and VICReg (decorrelation and variance terms).

### DL03-146
- **High masking (75%):** images are highly **spatially redundant**. With low masking, missing patches can be filled in by interpolating from neighbors, a trivial low-level task. Masking most of the image forces the model to reason about objects, shapes and context to reconstruct, which gives semantic representations. Contrast BERT, where ~15% suffices because language is information-dense.
- **Encoder on visible patches only:** with 75% masked, the encoder processes only 25% of the tokens, so **pretraining is ~3–4× faster** with lower memory, and there is **no train–test mismatch** from mask tokens (at fine-tuning the encoder sees real patches only). A **lightweight decoder** takes the encoded visible tokens plus learnable mask tokens with positions and reconstructs pixels (normalized per patch); the loss is computed on masked patches only. The decoder is discarded afterwards.

### DL03-147
- **Linear probing:** freeze the encoder and train a linear classifier on its features. Measures **linear separability** of the frozen representation; cheap.
- **k-NN:** classify by nearest neighbors in feature space (cosine). No training; measures local neighborhood semantics; sensitive to feature scale and geometry.
- **Fine-tuning:** train all weights end to end on labeled data. Measures how good an **initialization** the model is; usually the highest accuracy.

**They disagree** because they test different properties. Contrastive and distillation methods (DINO, MoCo) produce linearly separable, k-NN-friendly features, so they are strong on linear probing and k-NN. MAE features are not linearly separable (strong on fine-tuning, weaker on linear probing) because reconstruction learns rich but non-linear, less invariant features. Report several protocols, plus low-shot and transfer to detection or segmentation.

### DL03-148
CLIP jointly trains an **image encoder** (ResNet or ViT) and a **text encoder** (transformer) on ~400M image–caption pairs.
1. Embed a batch of N images and N texts and project them to a shared space; L2-normalize.
2. Compute the N×N cosine-similarity matrix, scaled by a temperature: logits = (I·Tᵀ) · exp(t).
3. **Symmetric contrastive (InfoNCE) loss:** cross-entropy over rows (image to text) plus columns (text to image), where the diagonal entries are the correct pairs and the other N − 1 in each row and column are negatives. A very large batch (32k) provides many negatives.

**Temperature (a learned logit scale, initialized at 1/0.07 and clipped at 100):** it controls how peaked the softmax is. Too high a temperature gives soft distributions and weak separation; too low gives unstable, overconfident gradients. Learning it lets the model adjust the sharpness of the contrast as embeddings improve.

### DL03-149
- **Counting:** cannot reliably distinguish "three dogs" from "five dogs".
- **Spatial relations and compositionality:** "a horse on a man" versus "a man on a horse"; attribute binding ("red cube, blue sphere"); negation. It behaves like a bag of concepts.
- **Typographic attacks:** an apple with a handwritten label "iPod" is classified as an iPod, because CLIP reads text strongly.
- **Fine-grained and specialized domains:** car models, medical images, satellite imagery, digits (weak MNIST performance).
- **Abstract or systematic tasks:** distances, orientation, OCR of long text.
- **Biases** from web data (social stereotypes); sensitivity to **prompt wording**.
- **Weak localization** (global embedding only) and poor calibration on out-of-distribution data.

### DL03-150
- **Zero-shot recognition:** classify categories with **no training images** of those classes, using side information that links classes: attribute vectors, word embeddings or, today, **text prompts with a vision-language model** (CLIP), which matches image embeddings to class-description embeddings.
- **Few-shot learning:** a **small number of labeled examples** per new class (e.g. 1–5, "N-way K-shot"). Methods: metric learning (prototypical or matching networks), meta-learning (MAML), fine-tuning or linear probing on strong pretrained features, adapter or prompt tuning of VLMs (CoOp, Tip-Adapter).
- **Generalized zero-shot:** test classes include both seen and unseen classes, which brings a bias toward seen classes.

### DL03-151
**Challenges:**
- overfitting with 1–5 examples per class;
- high variance of the estimates;
- intra-class variation not covered by the few shots;
- domain shift between base and novel classes;
- class imbalance between abundant base classes and rare novel ones.

**Prototypical networks:** learn an embedding f where classes form clusters. For each class, the **prototype** is the mean embedding of its support examples, c_k = (1/K) Σ f(x_i). A query is classified by softmax over negative squared Euclidean distance to the prototypes. Training is **episodic** (sample N-way K-shot tasks from base classes) so it matches the test conditions.
The approach is simple, has few parameters (no per-class training), and averaging reduces noise. Modern practice shows that strong pretrained features plus a simple prototype or linear classifier is often as good as complex meta-learning.

### DL03-152
Choice depends on the hardware, accuracy and latency targets:
- **YOLO family** (YOLOv5/v8, YOLOX, YOLOv7/v9/v10/v11): best-supported real-time choice, 30–300 FPS depending on size (n/s/m/l/x), easy export to ONNX, TensorRT or CoreML.
- **RT-DETR:** a real-time transformer detector without NMS, competitive accuracy on GPUs.
- **SSD-MobileNet, EfficientDet-Lite, NanoDet, PicoDet:** for mobile CPUs and microcontrollers.
- **CenterNet or FCOS:** simple anchor-free options.

**Reasons:** single-stage, fully convolutional or simple heads, good accuracy per FLOP, mature deployment tooling, INT8 support. Select by benchmarking mAP against latency on the target device at the target input size, including NMS and preprocessing time.

### DL03-153
**YOLOv1:** divide the image into an S×S grid (7×7). Each cell predicts B boxes (x, y, w, h, objectness) and class probabilities, all from **one forward pass** of one network, trained with a sum-squared regression loss. Very fast, but poor on small objects and crowds (each cell predicts few objects).
**Later versions:**
- **v2:** BatchNorm, **anchor boxes** from k-means, higher resolution, multi-scale training, Darknet-19.
- **v3:** **multi-scale predictions** (FPN-like, 3 scales), Darknet-53, logistic class predictions.
- **v4/v5:** CSP backbones, PANet neck, Mosaic augmentation, CIoU loss, auto-anchors, a PyTorch ecosystem.
- **YOLOX / v6 / v8:** **anchor-free**, **decoupled** classification and regression heads, advanced label assignment (SimOTA, task-aligned assignment), distribution focal loss.
- **v7/v9:** re-parameterization, E-ELAN, programmable gradient information.
- **v10:** **NMS-free** training with consistent dual assignments.

Throughout: better accuracy–speed trade-offs and easier deployment.

### DL03-154
- **Haar features:** rectangular light–dark contrast patterns (edges, lines, center-surround), computed in O(1) using an **integral image**.
- **AdaBoost** selects a few discriminative features from ~160k candidates, combining weak classifiers (each a thresholded feature) into a strong classifier.
- **Attentional cascade:** a sequence of increasingly complex classifiers. Early stages quickly reject most background windows (with high recall); only promising windows reach later stages, enabling real-time sliding-window detection across scales (2001, face detection on 2000s hardware).

**Why replaced:** hand-crafted features are limited; poor robustness to pose, lighting, occlusion and in-plane rotation; one detector per object class and viewpoint; many false positives. CNN detectors learn features end to end, handle many classes and variations, and are far more accurate while still running in real time on GPUs and NPUs.

### DL03-155
- **FCOS:** each feature-map location **inside** a ground-truth box predicts the class, the **distances to the four box edges (l, t, r, b)** and a **centerness** score (which down-weights low-quality predictions far from the object center). An FPN assigns objects to pyramid levels by size range.
- **CenterNet ("objects as points"):** predicts a **heatmap of object centers** per class (Gaussian-splatted targets, focal loss) plus box size and center offset at each peak. Peaks are extracted with 3×3 max pooling, so no NMS is needed in the simple setting.

**Problems with anchors they avoid:**
- many anchor hyperparameters (scales, ratios, IoU thresholds) that must be tuned per dataset;
- severe positive–negative imbalance from huge numbers of anchors;
- extra compute for IoU matching;
- poor generalization to unusual shapes;
- ambiguous assignment.

Anchor-free detectors are simpler and generalize better, and they now dominate (YOLOX and v8, FCOS-based designs).

### DL03-156
- **Hungarian matching:** DETR predicts a fixed set of N predictions. During training it computes the optimal **one-to-one bipartite matching** between predictions and ground-truth objects (padded with "no object") by minimizing a matching cost: −class probability + λ₁·L1(box) + λ₂·(1 − GIoU). Each object is matched to exactly **one** prediction; unmatched predictions are trained to predict "no object". Duplicates are penalized, and decoder self-attention lets queries communicate to avoid them, so **NMS is unnecessary**.
- **Slow convergence (~500 epochs on COCO):**
  - initially uniform cross-attention over all image positions must learn to focus on sparse object regions, which is hard;
  - the Hungarian assignment is **unstable** early on (the same query matches different objects from epoch to epoch);
  - object queries carry no positional prior.
- **Fixes:** Deformable DETR (attend to a few sampled points, multi-scale), conditional or DAB-DETR (anchor-like positional queries), DN-DETR and DINO (denoising training with noised ground-truth boxes), and one-to-many auxiliary assignments (H-DETR, Co-DETR). These cut training to around 12–50 epochs.

### DL03-157
Standard NMS **deletes** any box whose IoU with a higher-scoring box exceeds the threshold. In crowds or with overlapping objects, a true detection of a second object is suppressed, which lowers recall.
**Soft-NMS** instead **decays the score** of overlapping boxes according to their overlap:
- linear: s_i ← s_i · (1 − IoU) when IoU > N_t;
- Gaussian: s_i ← s_i · exp(−IoU² / σ).

Then it continues by score. Heavily overlapping duplicates get low scores, while moderately overlapping true objects survive with reduced scores, which a later threshold or the AP computation can still use.
It beats standard NMS when objects **overlap significantly** (pedestrians, crowds, cars in traffic, densely packed retail items) and under mAP averaged over strict IoU thresholds. It is a drop-in change with no retraining; it may slightly increase false positives at low thresholds.

### DL03-158
**COCO:**
- AP is computed per class at **10 IoU thresholds, 0.50:0.05:0.95**, each using **101-point interpolated precision** (recall 0, 0.01, …, 1), then averaged over thresholds and over the 80 classes. The resulting "AP" is mAP@[.5:.95].
- Also reports **AP50** and **AP75**, and **AP_S / AP_M / AP_L** by object area (< 32², 32²–96², > 96² pixels), plus AR (average recall) with a maximum of 1, 10 or 100 detections per image.
- Crowd regions are marked "iscrowd" and ignored.

**PASCAL VOC:** a single IoU threshold of **0.5** (AP50); VOC2007 used **11-point** interpolation, VOC2010+ the area under the full monotone PR curve; 20 classes; "difficult" objects are ignored.
COCO's averaging over strict IoUs rewards **precise localization**, while VOC mainly rewards finding objects.

### DL03-159
Label assignment decides which anchors, points or queries are trained as positives (with which ground-truth box) and which as negatives. It shapes **what the network learns**:
- **Too few positives:** weak supervision and slow learning. **Too many low-quality positives:** noisy box regression, duplicates, poor localization.
- Fixed IoU thresholds are brittle across object sizes and shapes (small objects get few positives).
- A misalignment between classification score and localization quality means NMS keeps the wrong box.

**Better strategies:**
- **ATSS:** adaptive IoU threshold per object from the statistics of candidate IoUs.
- **OTA / SimOTA:** treat assignment as optimal transport using classification plus regression cost.
- **TAL (task-aligned learning, TOOD and YOLOv8):** the alignment metric s^α·u^β uses both the classification score and the IoU.
- **Hungarian one-to-one assignment** (DETR), which removes NMS.

Changing only the assignment often yields 1–3 AP or more with no inference cost.

### DL03-160
- **Training data:** include occluded examples labeled with full ("amodal") or visible boxes consistently; occlusion augmentation (Cutout, random erasing, copy-paste of occluders).
- **Context and part-based reasoning:** large receptive fields and attention let the model infer an object from visible parts and context; part-based models and multiple heads (full body plus visible region, as in CrowdDet).
- **Post-processing:** soft-NMS, adaptive NMS, or set-based (NMS-free) prediction, so overlapping objects are not suppressed; repulsion loss to keep predicted boxes apart in crowds.
- **Temporal information** in video (tracking keeps identity through brief occlusions); multi-view or sensor fusion.
- **Amodal segmentation** predicts the hidden extent.
- **Evaluate** on occlusion-specific subsets (CrowdHuman, CityPersons heavy-occlusion split).

### DL03-161
They replace the fixed classification layer with **text embeddings**:
- **OWL-ViT:** start from CLIP; remove token pooling so each ViT output token predicts a box, then project the token embeddings into CLIP's joint space. Class "weights" are text embeddings of arbitrary queries ("a photo of a giraffe"), or image embeddings for image-conditioned queries. Fine-tuned on detection data while keeping image–text alignment.
- **Grounding DINO:** a DINO-DETR detector with **deep vision–language fusion** (feature enhancer, language-guided query selection, cross-modality decoder), trained on detection plus **phrase-grounding** plus caption data, so it localizes any phrase in the prompt.

Generalization to unseen classes comes from **large-scale image–text pretraining** (concepts learned from captions) plus region–word alignment. Limitations: lower accuracy than closed-set detectors on known classes; sensitivity to prompt wording; confusion between similar concepts; weaker results on rare or specialized categories.

### DL03-162
- **Resampling:** repeat-factor sampling (LVIS) oversamples images containing rare classes; class-aware sampling.
- **Loss re-weighting:** equalization loss (ignore suppressing gradients from frequent classes on rare ones), seesaw loss, focal loss, federated loss; logit adjustment or balanced softmax.
- **Decoupled training:** train the representation normally, then re-balance or retrain the classifier head with balanced sampling (cRT, BAGS).
- **Data:** copy-paste augmentation of rare instances, synthetic rendering, mining more examples (active learning), merging fine classes.
- **Few-shot detection techniques:** fine-tune only the last layers on balanced data (TFA), cosine classifiers.
- **Open-vocabulary or VLM-based detectors** that leverage text knowledge for rare categories.
- **Evaluate** with per-class AP and AP_rare / AP_c / AP_f.

### DL03-163
**TTA for detection:**
1. Run the detector on several transformed versions of the image: horizontal flip, multiple scales (e.g. 0.8×, 1×, 1.2×), sometimes small crops or color variants.
2. **Invert the transform on the predicted boxes**: unflip x coordinates, rescale to the original size.
3. **Merge** the pooled detections:
   - **NMS** or soft-NMS over the union (simple; keeps the single best box);
   - **Weighted Boxes Fusion (WBF):** cluster boxes by IoU and average their coordinates weighted by confidence, adjusting the score by how many models or augmentations agreed. Usually the most accurate, giving better localization (higher AP75).

It costs k× the inference time; it is useful for offline or competition settings, rarely for real time.

### DL03-164
**Panoptic segmentation** gives every pixel a semantic class **and**, for countable "things", an instance ID. "Stuff" (sky, road) has only a class. Segments must be non-overlapping.
**Panoptic quality:** predicted and ground-truth segments of the same class are **matched if IoU > 0.5** (this makes the matching unique). Then:
- PQ = Σ_(TP) IoU(p, g) / (|TP| + ½|FP| + ½|FN|);
- PQ = **SQ × RQ**, where segmentation quality SQ = mean IoU of the matched pairs, and recognition quality RQ = |TP| / (|TP| + ½|FP| + ½|FN|), an F1-like detection score.

It is computed per class and averaged (also reported separately as PQ_things and PQ_stuff).

### DL03-165
- **Atrous (dilated) convolutions** let DeepLab remove the last downsampling strides (output stride 16 or 8 instead of 32) while keeping large receptive fields and reusing pretrained weights, so features stay dense and high resolution without extra parameters.
- **ASPP (Atrous Spatial Pyramid Pooling):** parallel branches on the same feature map:
  - a 1×1 conv;
  - three 3×3 atrous convs with different rates (6, 12, 18 at output stride 16);
  - **image-level pooling** (global average pool, 1×1 conv, upsample) for global context.

  They are concatenated and fused with a 1×1 conv. Each branch sees a different effective field of view, capturing objects and context at multiple scales.
- **DeepLabv3+** adds a simple decoder that fuses low-level features for sharper boundaries.

### DL03-166
Mask2Former treats **all segmentation tasks as mask classification**: predict a set of N binary masks, each with one class label (including "no object").
- **Backbone plus pixel decoder** (multi-scale deformable attention) produce per-pixel embeddings at several resolutions.
- **Transformer decoder:** N learnable queries; each query outputs a class and a mask embedding, and the mask = sigmoid(query embedding · per-pixel embeddings).
- **Masked attention:** each query's cross-attention is restricted to the foreground of its own predicted mask from the previous layer, which gives faster convergence and better small objects.
- **Training:** Hungarian matching between predicted and ground-truth masks; losses are cross-entropy for the class plus Dice and binary cross-entropy for the mask (computed on sampled points for efficiency).

**Unification:** semantic segmentation merges masks by class; instance segmentation takes each mask as an instance; panoptic segmentation combines both. One architecture achieves state of the art on all three.

### DL03-167
**SAM** (Segment Anything) is a **promptable segmentation foundation model**: given an image and a **prompt** (points, a box, a rough mask; text was explored), it outputs valid object masks.
- **Architecture:** a heavy **ViT image encoder** (MAE-pretrained, run once per image), a lightweight **prompt encoder** and a fast **mask decoder** (two-way attention, about 50 ms), which outputs **3 masks** for ambiguous prompts (whole, part, sub-part) with predicted IoU scores.
- **Data:** SA-1B, 11M images and 1.1B masks, built with a model-in-the-loop data engine.

**Difference from class-specific segmentation:** SAM segments "whatever the prompt points to", with **no class labels** and class-agnostic, zero-shot generalization to new objects and domains. Class-specific models (DeepLab, Mask R-CNN) output fixed categories and need labeled training data for each class. For semantic labels SAM must be combined with a detector or classifier (e.g. Grounding DINO + SAM). SAM 2 extends this to video with memory.

### DL03-168
Depth gives **geometry** that RGB lacks: object boundaries where depth jumps, surface normals, height above the floor, 3D shape, all invariant to lighting and texture.
- **Input fusion (early):** stack depth as a 4th channel, or encode it as HHA (horizontal disparity, height, angle with gravity) to be more CNN-friendly.
- **Two-stream networks:** separate RGB and depth encoders fused at multiple levels (FuseNet, RedNet, ACNet), with attention-based fusion.
- **Depth-aware operations:** depth-aware convolution and pooling (weight neighbors by depth similarity), 3D point-cloud or voxel processing.
- **Multi-task learning:** predict depth and semantics jointly.

It helps separate objects with similar color, recognize floors and walls, and work in poor lighting. Challenges: noisy or missing depth (reflective or transparent surfaces), RGB–depth alignment, extra sensor cost.

### DL03-169
**Causes:**
- downsampling (stride 16–32) and bilinear upsampling blur fine detail;
- the loss is dominated by interior pixels;
- annotation noise at edges;
- class imbalance at thin structures.

**Fixes:**
- **Architecture:** keep high resolution (HRNet), skip connections and decoders (U-Net, DeepLabv3+), multi-scale fusion.
- **Refinement:** PointRend (predict at adaptively selected uncertain points with fine-grained features), CRF or dense-CRF post-processing, guided filters, SegFix-style boundary offset correction, cascade refinement.
- **Losses:** boundary-aware losses (boundary loss, active contour, Hausdorff), Lovász, weighted cross-entropy near edges, auxiliary edge-prediction tasks.
- **Data:** higher-quality boundary annotations, higher input resolution.
- **Evaluate** with boundary F1 or boundary IoU to track progress.

### DL03-170
**Weakly supervised segmentation:**
- **Image-level tags:** train a classifier, extract **class activation maps** (CAM, Grad-CAM) as seed regions, expand and refine them (affinity propagation such as AffinityNet or IRNet, CRFs, adversarial erasing to cover whole objects), use them as **pseudo-masks** and retrain a segmentation network; iterate.
- **Boxes:** generate masks inside boxes (GrabCut, or SAM prompted with the box); use the box-tightness prior (BoxInst: projection loss on box edges plus pairwise color-affinity loss); multiple-instance learning.
- **Points or scribbles:** partial cross-entropy on labeled pixels plus regularization that propagates labels to similar neighboring pixels (CRF loss, normalized cut, random walk); SAM with point prompts.
- **Combine with:** self-training and pseudo-label filtering by confidence, semi-supervised learning with a few full masks, and foundation models (SAM, DINOv2 features) to generate high-quality pseudo-labels.

### DL03-171
HOG (Dalal and Triggs, 2005):
1. Optional gamma or color normalization.
2. Compute gradients (simple [−1, 0, 1] filters), giving magnitude and orientation per pixel.
3. Divide the image into **cells** (e.g. 8×8 pixels). For each cell, build a **histogram of gradient orientations** (9 bins over 0–180°, unsigned), with votes weighted by gradient magnitude and interpolated between bins.
4. Group cells into overlapping **blocks** (2×2 cells) and **normalize** each block (L2-Hys) for illumination and contrast invariance.
5. Concatenate all block histograms into one feature vector (3,780-d for a 64×128 pedestrian window).
6. Classify with a linear SVM in a sliding-window detector.

It captures **local shape and edge structure**, is robust to small deformations and lighting changes, and is not rotation-invariant.

### DL03-172
| | Speed | Invariance | Descriptor | Typical use |
|---|---|---|---|---|
| **SIFT** | Slow | Scale, rotation, illumination; partly affine | 128-d float (L2) | Precise matching, stitching, SfM, 3D reconstruction |
| **SURF** | ~3× faster than SIFT | Scale, rotation (Hessian keypoints, box filters, integral images) | 64-d float | Faster SIFT-like matching (patented) |
| **ORB** | Very fast (real time) | Rotation (oriented FAST), scale via pyramid; less robust | 256-bit binary (Hamming) | SLAM (ORB-SLAM), mobile AR, tracking |
| **HOG** | Moderate | Illumination (block norm); not rotation or scale invariant | Dense grid histograms | Object detection in a sliding window (pedestrians) |

SIFT, SURF and ORB are **sparse keypoint** detectors and descriptors for matching. HOG is a **dense window** descriptor for classification and detection. Learned features (SuperPoint plus SuperGlue or LightGlue) now outperform them for matching.

### DL03-173
The Hough transform detects shapes by **voting in parameter space**:
- **Lines:** each line is parameterized as ρ = x·cosθ + y·sinθ (avoids infinite slopes). For each edge pixel (from Canny), vote for all (ρ, θ) bins consistent with it, which traces a sinusoid in the accumulator. Lines appear as **peaks** where many sinusoids intersect; threshold and apply non-maximum suppression. The probabilistic Hough transform samples points and returns segments.
- **Circles:** parameters (a, b, r). Each edge pixel votes for possible centers at radius r, a 3D accumulator, so the Hough gradient method uses edge direction to vote only along the gradient line, which reduces cost.

**Pros:** robust to noise, gaps and occlusion. **Cons:** memory and time grow with the number of parameters; bin resolution and threshold tuning are needed.

### DL03-174
Morphological operations are nonlinear operations on binary (or grayscale) images using a **structuring element** (kernel shape):
- **Erosion:** a pixel stays 1 only if the whole kernel fits inside the foreground. Shrinks objects, removes small noise and thin protrusions.
- **Dilation:** a pixel becomes 1 if the kernel touches any foreground. Grows objects, fills small holes and gaps.
- **Opening** = erosion then dilation. Removes small specks and noise while roughly preserving shape.
- **Closing** = dilation then erosion. Fills small holes and joins nearby fragments.
- **Others:** morphological gradient (dilation − erosion) gives outlines; top-hat and black-hat extract small bright or dark details; skeletonization.

**Uses:** cleaning segmentation masks and thresholded images, OCR and document preprocessing, separating touching objects (with distance transform and watershed), counting cells, defect inspection.

### DL03-175
- **Histogram equalization** remaps intensities using the **cumulative distribution** (CDF) of the image histogram so output intensities are spread roughly uniformly, which increases global contrast. Problems: it amplifies noise, over-enhances, and a single global mapping fails when parts of the image differ (a dark region next to a bright one).
- **CLAHE** (Contrast-Limited Adaptive Histogram Equalization) equalizes **locally** on tiles (e.g. 8×8 grid), **clips** each histogram at a limit (redistributing the excess) to prevent noise amplification, and **bilinearly interpolates** between tiles to avoid block artifacts.

Use CLAHE for images with **non-uniform lighting or local low contrast**: medical X-ray and retinal images, underwater, night and foggy scenes, OCR of unevenly lit documents. Apply it to the luminance channel (LAB L) for color images.

### DL03-176
An image pyramid is a set of progressively **downsampled** copies of an image:
- **Gaussian pyramid:** blur, then subsample by 2 at each level.
- **Laplacian pyramid:** the difference between a Gaussian level and the upsampled next level, storing band-pass detail; the image can be reconstructed exactly.

**Uses:**
- **Multi-scale detection:** run a fixed-size detector (sliding window HOG or Viola–Jones) at each pyramid level to find objects of different sizes; SIFT's DoG scale space; coarse-to-fine optical flow and registration (handle large motion at low resolution, refine at high). CNN feature pyramids (FPN) are the learned analogue.
- **Blending:** Laplacian pyramid blending of two images with a mask pyramid blends low frequencies over wide regions and high frequencies over narrow ones, giving seamless panoramas and composites without visible seams.
- Also compression and image editing at multiple scales.

### DL03-177
A **homography** H is a 3×3 projective transformation (8 degrees of freedom, defined up to scale) mapping points between two images of a **planar scene**, or of any scene when the camera **only rotates** about its center: x′ ~ H x in homogeneous coordinates.

**Robust estimation for stitching:**
1. Detect and describe keypoints (SIFT, ORB) in both images; match them with the ratio test.
2. **RANSAC:** repeatedly pick **4 random correspondences** (the minimum, no three collinear), compute H by the **DLT** (direct linear transform, solved by SVD), count inliers whose reprojection error ‖x′ − Hx‖ is below τ pixels; keep the H with the most inliers.
3. Refine H on all inliers (least squares or Levenberg–Marquardt, with normalized coordinates).
4. Warp one image into the other's frame and blend (feathering or multi-band blending); for many images, run bundle adjustment.

### DL03-178
Projection model: x ~ **K [R | t]** X, mapping world point X to pixel x.
- **Intrinsics K** (camera-internal): focal lengths f_x and f_y (in pixels), principal point (c_x, c_y), skew s (usually 0), plus **lens distortion** coefficients (radial k₁, k₂, k₃ and tangential p₁, p₂). K = [[f_x, s, c_x], [0, f_y, c_y], [0, 0, 1]].
- **Extrinsics [R | t]:** the camera's rotation and translation relative to the world (pose), 6 degrees of freedom.

**Calibration (Zhang's method):**
1. Capture many images of a known pattern (checkerboard or ChArUco) in different poses.
2. Detect corners with subpixel accuracy.
3. Each view gives a homography between the pattern plane and the image; the closed-form solution gives K, and then per-view extrinsics.
4. Refine all parameters (including distortion) by **nonlinear least squares** minimizing reprojection error (bundle adjustment).

Check the RMS reprojection error (< 0.5 px is good). Stereo or multi-camera calibration also estimates the relative extrinsics between cameras.

### DL03-179
**Epipolar geometry** describes the relationship between two views of a 3D scene. A point x in image 1 must lie, in image 2, on its **epipolar line** l′ = F x, because the 3D point lies on the ray through x. All epipolar lines pass through the **epipoles** (the image of the other camera center).
- **Fundamental matrix F** (3×3, rank 2, 7 degrees of freedom) works in **pixel** coordinates: x′ᵀ F x = 0. It is estimated from ≥ 7–8 correspondences (eight-point algorithm with normalization, inside RANSAC) **without knowing the intrinsics**.
- **Essential matrix E** works in **normalized** (calibrated) coordinates: E = K′ᵀ F K = [t]× R (5 degrees of freedom). It can be decomposed into the relative rotation R and translation direction t (four solutions; pick the one with points in front of both cameras).

**Uses in stereo:** recover the relative camera pose; **rectify** images so epipolar lines become horizontal rows, reducing correspondence search to 1D; triangulate 3D points; reject bad matches.

### DL03-180
Neural style transfer (Gatys et al.) optimizes an image x to match the **content** of image c and the **style** of image s, using a fixed pretrained VGG:
- **Content loss:** squared error between feature maps of x and c at a deep layer (e.g. conv4_2), which preserves object layout and structure.
- **Style loss:** for several layers, compute **Gram matrices** G^l_(ij) = Σ_k F^l_(ik) F^l_(jk) (inner products between channel feature maps over spatial positions), and minimize the squared differences between the Gram matrices of x and s.
- **Total:** α·L_content + β·L_style (+ total-variation smoothness), optimized over the pixels of x with L-BFGS or Adam.

**Why the Gram matrix captures style:** it records **which features co-occur** (correlations between channels: textures, colors, brush-stroke patterns) while **summing over positions**, so it discards **where** things are. That spatially invariant summary of texture statistics is "style". Fast feed-forward variants (Johnson et al.) train a network to do this in one pass; AdaIN matches channel means and variances for arbitrary styles.

### DL03-181
- **Frame-level 2D CNNs:** classify frames and pool over time (average, TSN segments). Cheap but weak at motion.
- **Two-stream networks:** a spatial stream on RGB frames (appearance) plus a temporal stream on stacked **optical flow** (motion), fused late. Strong motion modeling, but optical flow is expensive to compute.
- **3D CNNs** (C3D, I3D with ImageNet weights inflated to 3D, SlowFast, X3D): spatiotemporal kernels learn appearance and motion jointly, end to end. Heavy compute and memory, limited temporal range (16–64 frames).
- **Video transformers** (TimeSformer with divided space-time attention, ViViT, Video Swin, VideoMAE): attention models long-range temporal dependencies and scales well with pretraining (VideoMAE, CLIP-initialized). Quadratic token cost requires factorized or windowed attention.

**Trade-off:** two-stream gives good motion cues at the cost of computing flow; 3D CNNs are a solid, efficient default for short clips; transformers give the best accuracy with large-scale pretraining and longer context.
