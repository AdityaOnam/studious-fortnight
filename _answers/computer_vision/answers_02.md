### DL03-061
Pre-trained models supply **general visual features** learned from millions of images: edges, textures, parts, object shapes. In transfer learning they are either a **fixed feature extractor** (frozen backbone plus a new classifier) or an **initialization** for fine-tuning. They reduce the labeled data needed, speed up convergence, improve generalization and robustness, and act as a strong prior. The closer the pretraining data is to the target domain, the bigger the benefit.

### DL03-062
A feature extractor is a pretrained network with its classification head removed, used to map an image to an embedding (e.g. the 2048-d ResNet-50 vector after global pooling, or an intermediate conv map). The backbone is **frozen**, and features are computed once and fed to a lightweight model (logistic regression, SVM, small MLP, k-NN). This is cheap, works with very little data and avoids overfitting, but it cannot adapt the features to the new domain the way fine-tuning can.

### DL03-063
1. **Data:** split train, val and test; resize or crop to the backbone's input size (e.g. 224); normalize with the pretraining mean and std; add augmentation.
2. **Model:** load a pretrained backbone (e.g. torchvision ResNet-50) and replace the final layer: model.fc = nn.Linear(2048, num_classes).
3. **Stage 1:** freeze the backbone, train the head (lr ≈ 1e-3) for a few epochs.
4. **Stage 2:** unfreeze some or all layers and fine-tune with a lower lr (1e-4 to 1e-5), optionally with discriminative learning rates; use AdamW or SGD with momentum, cosine schedule, weight decay; keep BN in eval mode if batches are tiny.
5. **Validate** with early stopping; evaluate on the test set; calibrate thresholds if needed.

### DL03-064
**Recommended:**
- small or medium labeled datasets;
- target images similar to the source (natural photos);
- limited compute or time;
- tasks needing general visual features (classification, detection, segmentation).

**Less useful or harmful:**
- huge in-domain datasets, where training from scratch can match it, though pretraining still speeds convergence;
- very different modalities (spectrograms, SAR, hyperspectral, X-ray), where low-level features may not transfer and domain-specific pretraining is better;
- different input statistics (16-bit, many channels);
- when the source model's biases or license are unacceptable;
- negative transfer, when source and target tasks conflict.

### DL03-065
It depends on **dataset size** and **domain similarity**:
- **Small data, similar domain:** freeze almost everything and train the head (maybe the last block).
- **Small data, different domain:** freeze only early layers (generic edges) and fine-tune middle and late layers carefully, or use features from earlier layers.
- **Large data, similar domain:** fine-tune all layers with a small learning rate.
- **Large data, different domain:** fine-tune everything, or train from scratch with pretrained initialization.
In practice, train the head first, then progressively unfreeze from the top (gradual unfreezing), and pick the depth by validation score.

### DL03-066
Pretrained weights are already good. A large learning rate makes big updates that **destroy useful features** (catastrophic forgetting), especially early on when the new head is random and sends large, noisy gradients. Discriminative learning rates (e.g. 10× smaller for early layers than late layers, increasing toward the head) reflect that early layers hold generic features needing little change, while later layers and the new head must adapt more. Warmup and a short frozen-backbone phase serve the same purpose.

### DL03-067
Domain shift (different textures, color statistics, intensity ranges, resolution, scale, orientation, number of channels) means the pretrained features are less relevant:
- low-level filters may still transfer, but high-level ImageNet semantics (dogs, cars) often do not;
- you need to fine-tune more layers, use more labeled target data and larger learning rates for deep layers;
- BatchNorm statistics must be re-estimated on the target domain;
- the gains from ImageNet pretraining shrink. In-domain pretraining (RadImageNet, satellite foundation models, self-supervised pretraining on unlabeled target images) usually works better.
- Watch for input mismatches (grayscale versus RGB, 12/16-bit data, multispectral bands) that need adapted stems.

### DL03-068
This is **open-set recognition / out-of-distribution detection**: classify the 10 classes and reject everything else.
- **Baselines:** train a normal classifier and reject when the maximum softmax probability (or max logit or energy score) is below a threshold tuned on validation data.
- **Better:** feature-space methods (Mahalanobis distance to class means, k-NN distance in embedding space); ODIN (temperature plus input perturbation); outlier exposure (train with an auxiliary dataset of non-CIFAR images, e.g. Tiny Images or 80M Tiny, pushing them toward uniform predictions); an added "background" class; a one-class or contrastive approach on the in-distribution data.
- **Evaluate** with AUROC, FPR at 95% TPR, using held-out OOD sets (SVHN, LSUN, Textures).

### DL03-069
Image classification outputs **one label (or label set) per image**. Object detection outputs, for **every object instance**, a **bounding box plus a class label and a confidence**. So detection must localize (regress box coordinates), handle a variable number of objects at different scales, and suppress duplicates (NMS), and it is trained with combined classification and localization losses. It is evaluated with mAP at IoU thresholds rather than accuracy.

### DL03-070
- **Two-stage (Faster R-CNN):** a region proposal network proposes ~300–2,000 candidate boxes, then RoIAlign plus a second head classifies and refines each box. Higher accuracy, especially for small objects and precise localization; slower (≈ 5–20 FPS); used where accuracy matters (medical, offline analytics, as the base for Mask R-CNN).
- **One-stage (YOLO, SSD, RetinaNet, FCOS):** predict classes and boxes densely over feature-map locations in one pass. Faster (30–200+ FPS), simpler to deploy; historically less accurate because of foreground–background imbalance (fixed by focal loss and better label assignment). Modern YOLOs match two-stage accuracy on many benchmarks. Used for real-time video, edge devices, robotics.

### DL03-071
- **R-CNN (2014):** ~2,000 selective-search proposals; each crop warped and passed through a CNN separately; SVMs classify and a regressor refines boxes. Very slow (~47 s per image), multi-stage training.
- **Fast R-CNN (2015):** run the CNN **once** on the whole image; **RoI pooling** extracts fixed-size features for each proposal from the shared feature map; one network with softmax classification plus box regression trained jointly with a multi-task loss. ~0.3 s per image (excluding proposals).
- **Faster R-CNN (2015):** replaces selective search with a learned **region proposal network** sharing the backbone features, so the whole detector is end-to-end and near real-time (~5–17 FPS).
- Later: FPN for multi-scale features, Mask R-CNN (masks plus RoIAlign), Cascade R-CNN (progressively higher IoU thresholds).

### DL03-072
An RPN is a small fully convolutional network that slides over the backbone feature map. At each position it considers **k anchors** (e.g. 3 scales × 3 aspect ratios = 9) and predicts:
- an **objectness score** for each anchor (object versus background), and
- **box regression offsets** (Δx, Δy, Δw, Δh) refining the anchor.

Training labels anchors with IoU > 0.7 to a ground-truth box as positive and IoU < 0.3 as negative, sampling 256 anchors per image at a 1:1 ratio; the loss is binary cross-entropy plus smooth-L1. At inference the top-scoring refined anchors go through NMS (IoU 0.7) and the top ~300–2,000 become proposals for the second stage.

### DL03-073
Anchors are **predefined reference boxes** of several scales and aspect ratios tiled at every feature-map location; the detector predicts class scores and offsets relative to them.
**Assignment during training:**
1. Compute IoU between every anchor and every ground-truth box.
2. An anchor is **positive** if its IoU ≥ a high threshold (e.g. 0.5 in RetinaNet, 0.7 in the RPN) with some ground truth, and is assigned to the box with the highest IoU.
3. For each ground truth, the highest-IoU anchor is also made positive, so every object gets at least one.
4. Anchors below a low threshold (0.4 or 0.3) are **negative** (background); those in between are ignored.
5. Positives get regression targets: t_x = (x − x_a)/w_a, t_y = (y − y_a)/h_a, t_w = log(w/w_a), t_h = log(h/h_a).

Anchor sizes and ratios should match the dataset (k-means on box sizes, as in YOLOv2).

### DL03-074
Detectors output many overlapping boxes for the same object. Non-maximum suppression keeps the best one:
1. Sort boxes by confidence (per class).
2. Take the highest-scoring box and keep it.
3. Remove all remaining boxes whose IoU with it exceeds a threshold (typically 0.5–0.7).
4. Repeat until no boxes remain.

Without NMS you get duplicate detections, which count as false positives and lower precision. **Limitations:** a fixed threshold can delete true detections of heavily overlapping objects (crowds); it is a hand-tuned, sequential, non-differentiable step. Alternatives: soft-NMS, learned NMS, and DETR-style set prediction.

### DL03-075
DETR (DEtection TRansformer) treats detection as **direct set prediction**:
- A CNN backbone feeds a transformer encoder–decoder; **N learned object queries** (e.g. 100) each output one box plus class (or "no object").
- **Training:** bipartite **Hungarian matching** finds the optimal one-to-one assignment between predictions and ground-truth boxes (cost = class probability + L1 + generalized IoU), then the loss is computed on matched pairs.
- **Differences from anchor-based detectors:** no anchors, no hand-designed assignment rules, **no NMS** (the one-to-one matching discourages duplicates), global reasoning through attention.
- **Downsides of the original:** slow convergence (500 epochs) and weak small-object accuracy. Deformable DETR, DINO-DETR and RT-DETR fix these.

### DL03-076
One-stage detectors evaluate ~100k candidate locations per image, almost all **easy background**. With plain cross-entropy, these easy negatives dominate the loss and gradients, so training is overwhelmed and the classifier learns little about the rare foreground. **Focal loss** (RetinaNet):
FL(p_t) = −α_t (1 − p_t)^γ log(p_t), usually γ = 2 and α = 0.25.
The factor (1 − p_t)^γ down-weights well-classified examples (p_t → 1) by orders of magnitude, so training focuses on hard examples. This let one-stage detectors match two-stage accuracy without hard-negative mining or sampling heuristics.

### DL03-077
CNN features are semantically strong but coarse at deep layers, and fine but weak at shallow layers. A **feature pyramid network** builds a multi-scale pyramid with strong semantics at every level:
- **Bottom-up:** the normal backbone (C2–C5, strides 4–32).
- **Top-down:** upsample the deeper map by 2×.
- **Lateral connections:** add a 1×1-projected shallower map to it, then smooth with a 3×3 conv, giving P2–P5 (P6/P7 for large objects).

Objects are predicted on the level matching their size (small objects on high-resolution P2/P3, large on P5). This greatly improves small-object detection at little cost and is used by Faster R-CNN, RetinaNet, Mask R-CNN and YOLO necks (PANet, BiFPN add bottom-up paths).

### DL03-078
- **Resolution:** larger input images, tiling or slicing inference (SAHI), keeping a stride-4 or stride-8 output level (P2 in FPN).
- **Architecture:** FPN or PAN or BiFPN fusion, dilated convs, attention, less early downsampling.
- **Anchors and assignment:** smaller anchor sizes matching the data, IoU-based or adaptive assignment (ATSS), center sampling, losses less sensitive to tiny boxes (normalized Wasserstein distance).
- **Data:** copy-paste and oversampling of small objects, mosaic, scale augmentation, multi-scale training and testing, fixing missing or noisy small-object labels.
- **Post-processing:** lower NMS thresholds or soft-NMS for dense small objects; tuned confidence thresholds.
- **Evaluate** with AP_small to track progress.

### DL03-079
**IoU = area(A ∩ B) / area(A ∪ B)**, from 0 (no overlap) to 1 (perfect match).
- **Training:** assigning anchors or predictions to ground truth (positive if IoU > threshold), NMS, and directly as a loss: IoU loss, GIoU, DIoU and CIoU add terms for non-overlapping boxes, center distance and aspect ratio.
- **Evaluation:** a detection is a true positive if IoU ≥ threshold (0.5 for VOC, 0.5:0.95 for COCO) with an unmatched ground truth of the same class; otherwise it is a false positive. These matches drive precision, recall and AP.

### DL03-080
1. For each class, sort all detections by confidence.
2. Match each detection to an unmatched ground-truth box of that class with IoU ≥ threshold. A match is a TP; otherwise it is an FP (duplicates are FPs). Unmatched ground truths are FNs.
3. Compute cumulative precision and recall down the ranked list, giving a precision–recall curve.
4. **AP** = area under the interpolated PR curve (precision made monotonic; VOC 2007 uses 11 points, COCO uses 101 points).
5. **mAP** = mean AP over classes. COCO also averages over IoU thresholds 0.50:0.05:0.95 and reports AP50, AP75 and AP for small, medium and large objects.
Also check per-class AP, recall at a fixed precision, and speed.

### DL03-081
The detector **finds the objects** (correct class, rough location) but its **boxes are imprecise**: localization quality is poor, not recognition.
**Likely causes:** coarse feature resolution, weak box regression loss, inconsistent or loose annotation boxes, anchor mismatch, aggressive downsampling, small objects, low-IoU positive assignment during training.
**Improvements:**
- better regression losses (GIoU, DIoU, CIoU, distribution focal loss);
- cascade refinement (Cascade R-CNN with rising IoU thresholds);
- IoU-aware or quality-aware classification scores (IoU-aware heads, varifocal loss) so NMS keeps the best-localized box;
- higher-resolution features (FPN, P2) and RoIAlign instead of RoIPool;
- stricter positive assignment;
- cleaning box annotations;
- test-time augmentation with weighted box fusion.

### DL03-082
- **Input:** a point cloud is sparse, irregular and unordered (x, y, z, intensity), not a dense grid; density falls off with distance; there is no color or texture.
- **Output:** 3D boxes with 7+ degrees of freedom (x, y, z, l, w, h, yaw) in metric space, usually in bird's-eye view.
- **Architectures:** point-based (PointNet++, PointRCNN), voxel-based (VoxelNet, SECOND with sparse 3D convs), pillar-based (PointPillars, which flattens to a BEV pseudo-image), range-view, and center-based heads (CenterPoint).
- **Why heavy:** 100k+ points per sweep; 3D voxel grids are huge (cost grows cubically with resolution); neighbor search and grouping for point methods is expensive; the large spatial extent (±100 m) and multi-sweep accumulation add more. Sparse convolutions and pillars are used to cut cost.

### DL03-083
Goal: predict 3D boxes from N surround-view cameras.
1. **Shared 2D backbone** (ResNet, ConvNeXt or ViT) plus FPN extracts per-camera features.
2. **View transform to bird's-eye view (BEV):**
   - **Lift-splat (LSS, BEVDet):** predict a per-pixel depth distribution, lift features into 3D frustums, and splat them onto a BEV grid using camera intrinsics and extrinsics.
   - **Query-based (BEVFormer, DETR3D, PETR):** BEV or object queries attend to image features by projecting 3D reference points into each camera (deformable or spatial cross-attention).
3. **Temporal fusion:** align previous BEV features with ego-motion (BEVFormer temporal self-attention, BEVDet4D) for velocity and occlusion handling.
4. **BEV encoder plus 3D detection head** (CenterPoint-style heatmaps or DETR-style set prediction with Hungarian matching).

Depth estimation is the key weakness. Supervise depth with lidar during training (BEVDepth), use multi-frame stereo cues, and calibrate cameras precisely.

### DL03-084
Sensors fail differently:
- **Cameras:** rich semantics (lights, signs, lanes, color) and cheap, but poor direct depth and they fail in glare, darkness and fog.
- **Lidar:** precise 3D geometry and distance, works at night; expensive, degraded by rain and snow, no color.
- **Radar:** measures velocity directly (Doppler) and range, works in fog and rain, long range; low resolution and noisy.

Fusing them gives **redundancy** (safety), complementary strengths and robustness to adverse conditions.
**Fusion points:**
- **Early (raw or data level):** project lidar points onto images or paint points with image semantics (PointPainting).
- **Mid (feature level):** fuse in a shared BEV feature space (BEVFusion, TransFusion). This is the modern default.
- **Late (object level):** fuse per-sensor detections and tracks with a Kalman filter. Simple and modular but loses information.

Accurate calibration and time synchronization are prerequisites.

### DL03-085
They run an automated **detect-then-blur pipeline** on Street View and Look Around imagery:
1. **Detection:** high-recall detectors for faces and license plates (CNN-based, multi-scale, trained on large labeled sets), tuned for recall over precision because missing one is a privacy failure.
2. **Anonymization:** apply strong Gaussian blur or pixelation to the detected regions (irreversible at that resolution) before publishing.
3. **Quality control:** manual review queues and user-reported "request blurring" flows for misses; whole houses or people can be blurred on request.

Challenges: small, distant, occluded or angled faces and plates, false positives (blurring signs), and panorama distortion.

### DL03-086
Image segmentation assigns a label to **every pixel**, partitioning the image into meaningful regions.
- **Semantic:** class per pixel.
- **Instance:** separate mask per object.
- **Panoptic:** both, for things and stuff.

**Applications:** medical imaging (tumor and organ delineation), autonomous driving (road, lane, drivable area), satellite and aerial mapping (buildings, land cover), photo editing and background removal, AR, robotics grasping, agriculture (crop and weed), industrial inspection, video matting.

### DL03-087
- **Semantic segmentation** labels each pixel with a class but does **not separate instances**: two adjacent people form one "person" region. Usually also covers "stuff" (sky, road).
- **Instance segmentation** detects each object and produces a **separate mask per instance** (person 1, person 2), typically for countable "things" only. It is detection plus masks (Mask R-CNN).
- **Panoptic segmentation** combines both: every pixel gets a class, and thing pixels also get an instance ID.

### DL03-088
- **Semantic:** FCN, SegNet, U-Net (and nnU-Net for medical), DeepLab v1–v3+ (atrous convs, ASPP), PSPNet (pyramid pooling), HRNet (high-resolution throughout), SegFormer (transformer).
- **Instance:** Mask R-CNN, YOLACT, SOLO and SOLOv2, CondInst, PointRend (boundary refinement).
- **Panoptic and universal:** Panoptic FPN, MaskFormer and Mask2Former, OneFormer.
- **Promptable and foundation:** SAM and SAM 2.
- **Real-time:** BiSeNet, Fast-SCNN, DDRNet.

### DL03-089
Segmentation needs both **what** (semantic context, which needs large receptive fields and deep, downsampled features) and **where** (precise pixel locations, which needs high resolution).
- The **encoder** (a classification backbone) downsamples to capture context and semantics cheaply.
- The **decoder** upsamples back to input resolution (transposed convs or bilinear upsampling plus convs) to produce a dense per-pixel output.
- **Skip connections** bring fine spatial detail from the encoder to the decoder.

Without the decoder, outputs are coarse (stride 16–32) and boundaries are blurry. Without the downsampling encoder, computation at full resolution is prohibitive and context is limited.

### DL03-090
U-Net is a symmetric encoder–decoder ("U" shape). At each decoder level, the upsampled features are **concatenated** with the encoder features of the same resolution (skip connections), followed by convs.
- Downsampling loses precise spatial information; skips reinject **high-resolution edges and textures**, so the decoder can place boundaries accurately while using deep semantic context.
- They improve gradient flow and training with small datasets (U-Net was designed for biomedical images with few labels, plus heavy elastic augmentation).

Concatenation (rather than addition, as in FPN) lets the decoder learn how to combine the two sources.

### DL03-091
**Mask R-CNN** = Faster R-CNN plus a parallel **mask head**: a small FCN that predicts a 28×28 binary mask per RoI for each class. A per-class sigmoid with binary cross-entropy decouples masks from classification. The box branch and RPN stay the same.
**RoIAlign fixes RoIPool's quantization.** RoIPool rounds RoI coordinates and bin boundaries to integer feature-map cells, which causes misalignments of up to half a stride (e.g. 16 px), fine for classification but bad for pixel masks. **RoIAlign** keeps floating-point coordinates and **bilinearly interpolates** features at regularly sampled points in each bin, then pools. This gave large mask AP gains (+10–50% relative at strict IoU) and also improved box AP.

### DL03-092
An FCN replaces every fully connected layer with convolutions (FC → 1×1 conv), so the network contains only convs, pooling and upsampling. Convolutions work on any spatial size, so an input of any H×W produces a proportionally sized class-score map. Coarse outputs (stride 32) are **upsampled** with learnable transposed convs or bilinear interpolation back to input resolution, and FCN-16s and FCN-8s add **skip connections** from earlier, finer layers to recover detail. Training uses per-pixel cross-entropy on the full image, efficiently sharing computation across all pixels.

### DL03-093
With heavy imbalance (e.g. a 1% tumor region), per-pixel CE is dominated by the many easy background pixels. Predicting all background already gives a low loss and 99% accuracy, so the model under-segments small structures.
**Alternatives:**
- **Dice loss:** 1 − 2Σ(p·g)/(Σp + Σg). It optimizes overlap directly, is normalized by region size and is insensitive to background count.
- **Tversky loss** (weights FP versus FN; good for recall), **focal loss** (down-weights easy pixels), **Lovász-softmax** (a surrogate for IoU), **boundary losses**.
- **Weighted CE** (inverse class frequency).
- **Combo Dice + CE:** common default; CE gives stable gradients, Dice handles imbalance.

Patch sampling around foreground also helps.

### DL03-094
For prediction mask P and ground truth G, per class:
- **IoU (Jaccard)** = |P ∩ G| / |P ∪ G| = TP / (TP + FP + FN).
- **Mean IoU** = average IoU over classes, usually computed from a confusion matrix accumulated over the whole dataset (not averaged per image); background included or not per convention. Frequency-weighted IoU weights by class frequency.
- **Dice (F1)** = 2|P ∩ G| / (|P| + |G|) = 2TP / (2TP + FP + FN). Dice = 2·IoU / (1 + IoU), so it is always ≥ IoU; common in medical imaging, often reported per case.
- **Complements:** pixel accuracy (misleading under imbalance), boundary metrics (Boundary F1, Hausdorff distance HD95) for contour quality, and AP-based metrics for instance segmentation.

### DL03-095
Computer vision is the field of making computers **extract meaning from images and video**: recognizing objects, reading text, estimating depth and motion, understanding scenes. It is loosely inspired by human vision: the visual cortex processes information hierarchically, from edges (V1 simple cells, which motivated Gabor-like filters and CNNs) to shapes and objects. But humans use rich priors, attention, 3D understanding, context and learning from few examples, with strong invariance; machines rely on statistical learning from data, can be fooled by adversarial noise and textures, and can exceed humans on narrow tasks while lacking general understanding.

### DL03-096
- **Image processing:** image in, **image out**. It transforms or enhances pixels: denoising, sharpening, contrast adjustment, filtering, resizing, compression, color correction. No semantic understanding is required.
- **Computer vision:** image in, **understanding out**: labels, boxes, masks, depth, 3D structure, descriptions.

Image processing is often a preprocessing step inside CV pipelines; the boundary blurs with learned methods (super-resolution, inpainting).

### DL03-097
- **Decode and convert color space:** BGR → RGB (OpenCV loads BGR), handle grayscale and alpha, correct EXIF orientation.
- **Resize:** aspect-preserving resize plus crop or letterbox padding to the model input size.
- **Normalize:** scale to [0, 1] and standardize with the per-channel mean and std used in pretraining; convert to CHW float.
- **Optional:** denoising, histogram equalization or CLAHE, deskewing (OCR), cropping regions of interest, stain or intensity normalization (medical).
- **Training only:** augmentation.
- Keep training and serving preprocessing **identical**, to avoid training–serving skew.

### DL03-098
- **Downscaling** loses fine detail (small objects, text, textures) and can alias; small objects may vanish entirely.
- **Upscaling** adds no information but increases compute.
- **Aspect-ratio distortion** (squashing) changes shapes the model learned; letterboxing or cropping avoids this.
- **Train/test resolution mismatch** shifts the apparent object size and receptive-field statistics, which hurts accuracy (see FixRes).
- **Compute** scales roughly with H×W, so resolution is a key accuracy–latency knob (EfficientNet scales it deliberately).
- **Interpolation method** (bilinear versus area versus nearest; antialiasing) must match between training and serving.

### DL03-099
- **Linear filters:** mean or box filter, **Gaussian blur** (good for Gaussian noise but blurs edges).
- **Nonlinear:** **median filter** (excellent for salt-and-pepper noise, preserves edges), **bilateral filter** (edge-preserving: weights by spatial and intensity distance).
- **Non-local means** and **BM3D** (exploit repeated patches).
- **Frequency domain:** low-pass, Wiener filtering, wavelet thresholding.
- **Temporal averaging** of multiple frames (video, burst photography).
- **Learned:** denoising CNNs (DnCNN), denoising autoencoders, diffusion-based restoration.
- Choose based on the noise type (Gaussian, Poisson, impulse) and how much edge detail must be kept.

### DL03-100
Edges are locations of strong intensity change, found via image gradients.
- **Sobel:** convolve with 3×3 kernels Gx = [[−1,0,1],[−2,0,2],[−1,0,1]] and Gy (its transpose). Gradient magnitude = √(Gx² + Gy²), direction = atan2(Gy, Gx). Thresholding the magnitude gives edges. Simple, but edges are thick and noise-sensitive.
- **Canny:**
  1. Gaussian smoothing.
  2. Sobel gradients (magnitude and direction).
  3. **Non-maximum suppression** along the gradient direction, to thin edges to 1 px.
  4. **Double threshold** (strong versus weak edges).
  5. **Hysteresis**: keep weak edges only if connected to strong ones.

  The result is thin, continuous, well-localized edges with good noise robustness.
- Others: Laplacian of Gaussian (zero crossings), Prewitt, Scharr, learned edge detectors (HED).

### DL03-101
A color space is a coordinate system for representing color:
- **RGB:** device-oriented, channels correlated with brightness.
- **HSV/HSL:** separates hue, saturation and value; good for color thresholding and segmentation, robust to lighting changes.
- **YCbCr/YUV:** luma plus chroma; used in compression, broadcasting and skin detection.
- **CIELAB:** perceptually uniform (Euclidean distance ≈ perceived difference); good for color comparison and transfer.
- **Grayscale:** intensity only.

They matter because the right space makes a task easier (illumination-invariant features, color-based segmentation), because pipelines must match (OpenCV BGR versus RGB bugs), and because color-related augmentations operate in specific spaces.

### DL03-102
Feature extraction transforms raw pixels into a compact, informative representation that downstream tasks can use.
- **Hand-crafted:** edges, corners (Harris), keypoints and descriptors (SIFT, SURF, ORB), HOG, LBP, color histograms, Gabor filters.
- **Learned:** activations or embeddings from CNNs and ViTs, which are task-adaptive and far more powerful.

Good features are discriminative, robust (invariant to nuisance factors such as lighting, scale and rotation) and compact.

### DL03-103
A descriptor is a **vector summarizing the local appearance around a keypoint** (or a whole image) so that the same physical point can be recognized in different images. Examples: SIFT and SURF (gradient histograms, float), ORB, BRIEF and BRISK (binary, Hamming distance), HOG, learned descriptors (SuperPoint, HardNet). They matter because matching descriptors enables image stitching, 3D reconstruction (structure from motion, SLAM), object recognition, image retrieval, tracking and registration. Good descriptors are distinctive and invariant to scale, rotation, illumination and viewpoint changes.

### DL03-104
SIFT (Scale-Invariant Feature Transform, Lowe 2004):
1. **Scale-space extrema:** build a Gaussian pyramid, compute Difference-of-Gaussians, and find local extrema across space and scale.
2. **Keypoint refinement:** subpixel and subscale localization (Taylor fit); reject low-contrast points and edge responses (Hessian ratio).
3. **Orientation assignment:** histogram of gradient orientations around the keypoint; the dominant orientation(s) define the keypoint's angle.
4. **Descriptor:** a 16×16 window rotated to that orientation, split into 4×4 cells, each with an 8-bin orientation histogram, giving a **128-d** vector, normalized, clipped at 0.2 and renormalized.

**Invariances:** scale, in-plane rotation, illumination (gradients plus normalization), partial robustness to affine and viewpoint change and noise. Matching uses nearest neighbor with Lowe's **ratio test** (d1/d2 < 0.8).

### DL03-105
Use **RANSAC**:
1. Randomly sample the minimal set (3 points) and fit a plane.
2. Count inliers: points with distance to the plane below a threshold τ.
3. Repeat N iterations, where N = log(1 − p) / log(1 − w³) for success probability p and inlier ratio w.
4. Keep the plane with the most inliers.
5. Refit the plane with least squares (SVD or PCA on the inliers: the normal is the smallest singular vector).

Alternatives: M-estimators (Huber or Tukey robust least squares), MSAC and MLESAC (score by residuals), PROSAC, LO-RANSAC. Choose τ from the sensor noise level.

### DL03-106
**Registration** aligns two images (or volumes) into a common coordinate frame: choose a transformation model (rigid, affine, homography, deformable), a similarity measure (feature matches, sum of squared differences, normalized cross-correlation, mutual information for multimodal medical images) and an optimizer. Feature-based: detect and match keypoints, then fit the transform with RANSAC. Intensity-based: optimize the transform parameters directly. Deep methods: VoxelMorph and learned matchers.

**Optical flow** estimates per-pixel motion between frames under brightness constancy (I_x·u + I_y·v + I_t = 0).
- **Sparse (Lucas–Kanade):** flow only at selected keypoints, assuming constant flow in a small window; fast, good for tracking features; often pyramidal for large motion.
- **Dense (Horn–Schunck, Farnebäck, deep RAFT):** a flow vector for every pixel with smoothness regularization; richer (segmentation by motion, frame interpolation, action recognition) but more expensive and error-prone in textureless or occluded regions.

### DL03-107
OCR (optical character recognition) converts images of text (printed or handwritten, scanned or in natural scenes) into machine-readable text.
**Applications:** document digitization and search, invoice and receipt and form processing (key-value extraction), ID and passport reading, license plate recognition, check processing, translation apps, accessibility (screen readers for images), postal sorting, scene-text understanding for robots and maps, digitizing historical archives.

### DL03-108
1. **Preprocessing:** deskew, denoise, binarize or enhance contrast, correct perspective (documents), normalize resolution (DPI).
2. **Text detection:** find text regions or lines with segmentation-based detectors (DBNet, CRAFT, EAST, PSENet), which handle arbitrary orientation and curved text.
3. **Rectification:** crop and deskew each region; a thin-plate-spline spatial transformer for curved text.
4. **Text recognition:** a CNN or ViT encoder plus a sequence decoder. Options: CRNN (CNN + BiLSTM + **CTC loss**, no character-level alignment needed), attention or transformer decoders (TrOCR, PARSeq), language-model rescoring.
5. **Post-processing:** dictionary or language-model correction, layout analysis (reading order, tables), key-information extraction (LayoutLM, Donut, or VLMs).
6. **Train** on synthetic text (SynthText) plus real data; evaluate with character and word error rates (CER, WER) and detection F1.

### DL03-109
**Tracking-by-detection:**
1. **Detect** objects in each frame.
2. **Predict** each existing track's next state with a **Kalman filter** (constant-velocity model on box position and size), which gives a predicted box and uncertainty.
3. **Associate** detections to tracks by solving an assignment problem (**Hungarian algorithm**) on a cost matrix:
   - **SORT:** IoU between predicted and detected boxes.
   - **DeepSORT:** adds an **appearance embedding** (re-ID CNN, cosine distance) and Mahalanobis distance gating, so it can re-identify objects after occlusion; a matching cascade prioritizes recently seen tracks.
4. **Update** matched tracks with the Kalman correction step. Create new tracks for unmatched detections (tentative until confirmed over several frames) and delete tracks unmatched for too long.

Modern variants: ByteTrack (also associates low-score detections), OC-SORT, BoT-SORT, and end-to-end trackers (MOTR).

### DL03-110
- **Occlusion** and objects leaving and re-entering, which cause identity switches.
- **Appearance changes:** pose, lighting, scale, motion blur, similar-looking objects (crowds, uniforms).
- **Fast or erratic motion** and camera motion that break constant-velocity assumptions.
- **Detector errors:** missed and false detections propagate into tracks.
- **Latency and compute budget:** detection plus re-ID embedding per frame at 30+ FPS on edge hardware; handling many objects.
- **Long-term re-identification** across cameras.
- **Initialization and termination** of tracks.
- **Drift** and accumulated error in single-object trackers.
- **Varying frame rates**, dropped frames, network delays.
