### DL03-182
A **CNN extracts per-frame features** (a pretrained backbone, frame to vector), and an **RNN (LSTM or GRU) models the temporal sequence** of those vectors. The final hidden state, or all hidden states, feed a classifier or a sequence decoder (LRCN, Donahue et al.).
**Uses:** action recognition, video captioning, gesture recognition, sign language, frame-level event detection, image-sequence prediction (ConvLSTM keeps spatial structure in the recurrent state, for weather nowcasting and video prediction).
**Pros:** flexible sequence length, reuses image pretraining, cheaper than 3D CNNs.
**Cons:** late temporal fusion misses fine motion; sequential RNNs are slow and limited at long range. 3D CNNs and transformers have largely replaced them.

### DL03-183
A (2+1)D convolution (R(2+1)D, Tran et al.) replaces a t×d×d 3D kernel with:
1. a **2D spatial conv** (1×d×d), then
2. a **1D temporal conv** (t×1×1),

with a nonlinearity in between and the number of intermediate channels chosen to keep the parameter count about equal to the 3D conv.
**Why it trains better:**
- it **doubles the number of nonlinearities**, so the network is more expressive at the same cost;
- **spatial and temporal factors are decoupled**, which makes optimization easier (lower training error, as reported);
- the spatial part can be initialized from 2D ImageNet models.

It gave better accuracy than full 3D convs on Kinetics and Sports-1M. Related designs: P3D, S3D, and factorized attention in TimeSformer.

### DL03-184
- **MOTA (Multiple Object Tracking Accuracy)** = 1 − (FN + FP + IDSW) / GT, summed over frames, where IDSW counts identity switches. It is dominated by **detection** quality (FP and FN), barely reflects association, and can be negative.
- **IDF1** = 2·IDTP / (2·IDTP + IDFP + IDFN). It measures how consistently the **same identity** is kept over time (global one-to-one matching of trajectories), so it is association-focused.
- **HOTA (Higher Order Tracking Accuracy)** = √(DetA · AssA), averaged over localization thresholds α. It explicitly balances detection accuracy, association accuracy and localization, and decomposes into interpretable sub-metrics. It is now the standard (MOTChallenge, KITTI).

Also: MOTP (localization precision), ID switches, fragmentations, MT/ML (mostly tracked or mostly lost trajectories).

### DL03-185
Pose estimation predicts the locations of **body keypoints** (joints: shoulders, elbows, knees) in 2D or 3D, often connected into a skeleton. It also covers hand, face and animal poses and **6-DoF object pose**.
- **Top-down:** detect each person first, then estimate keypoints in each cropped box with a single-person model (heatmap regression: SimpleBaseline, HRNet, ViTPose). More accurate, especially for small people; cost grows with the number of people; fails when the detector misses or boxes overlap.
- **Bottom-up:** detect **all keypoints in the image at once**, then **group** them into individuals (OpenPose part affinity fields, associative embedding, HigherHRNet). Runtime is roughly constant with crowd size and robust in crowds; grouping is harder and less accurate for small or overlapping people.
- **One-stage or direct regression** (YOLO-Pose, DEKR, RTMPose variants) blur the line between the two.

**Applications:** sports and fitness analytics, AR, motion capture and animation, action recognition, human–robot interaction, ergonomics.

### DL03-186
- **Stereo:** two calibrated, rectified cameras separated by baseline B. For each pixel, find the corresponding pixel along the same row in the other image; the horizontal shift is the **disparity d**. Depth **Z = f·B / d** (f is the focal length in pixels). Matching uses block matching or SGM (semi-global matching) with cost aggregation, or deep stereo networks (cost volumes such as PSMNet, RAFT-Stereo). Accuracy falls with distance (error ∝ Z²), and textureless, reflective or occluded regions are hard.
- **Monocular ambiguity:** a single image is a **projection that discards depth**. Infinitely many 3D scenes (a small near object or a large far one) produce the same image, so absolute **scale is unobservable**. Monocular networks (MiDaS, Depth Anything, ZoeDepth) rely on **learned priors**: object sizes, perspective, texture gradients, occlusion, defocus, shading. They give good relative depth but metric depth only with known camera intrinsics, scene priors or extra cues, and they can fail on unusual scenes or optical illusions.

### DL03-187
PointNet takes N points (x, y, z, plus features) directly, without voxelizing:
1. A **shared MLP** is applied independently to each point (per-point features, the same weights for every point).
2. A **symmetric aggregation function**, **max pooling** across points, produces a global feature vector. Because max is invariant to input order, the network is **permutation invariant**: any ordering of the same points gives the same output.
3. A classification MLP runs on the global feature; for segmentation, the global feature is concatenated back to each point feature.

Optional **T-Nets** predict alignment transforms (input and feature) for rough rotation invariance. Theory: max pooling plus MLPs can approximate any continuous symmetric set function. **Limitation:** no local neighborhood structure. **PointNet++** adds hierarchical local grouping (farthest point sampling plus ball query plus mini-PointNets) to capture local geometry at multiple scales.

### DL03-188
A **BEV** representation projects the 3D world onto a **top-down 2D grid** around the ego vehicle (e.g. 200×200 cells covering ±50 m), with features or semantic layers per cell.
**Why driving stacks use it:**
- it is the **natural frame for planning and control**, since driving happens on the ground plane;
- it is a **unified space for fusing** multiple cameras, lidar and radar, plus HD maps and time (ego-motion alignment is simple);
- objects keep their **true metric size and position** without perspective distortion or scale changes with distance, and occlusion handling is cleaner;
- it suits many tasks (3D detection, lane and map segmentation, occupancy, motion forecasting) from one shared feature map.

**Challenges:** cameras need a learned view transform (depth estimation or attention, as in LSS and BEVFormer), resolution is limited at long range, and heights are lost (3D occupancy grids extend it).

### DL03-189
- **NeRF:** an MLP maps a 3D position and viewing direction to **density and view-dependent color**. Images are rendered by **volume rendering**: sample points along each camera ray and alpha-composite their colors. It is trained per scene from posed images with a photometric loss (positional encoding for high-frequency detail). **Quality:** excellent, continuous, compact, handles view-dependent effects. **Speed:** slow training (hours) and rendering (seconds per frame), because hundreds of MLP evaluations are needed per ray. Speedups: Instant-NGP hash grids, Plenoxels, distillation.
- **3D Gaussian Splatting:** represents the scene as **millions of explicit 3D Gaussians** (position, covariance or anisotropic shape, opacity, spherical-harmonic color), initialized from SfM points and optimized with **differentiable rasterization**, sorting and alpha-blending projected 2D Gaussians. **Speed:** real-time rendering (100+ FPS at 1080p), training in minutes. **Quality:** comparable to or better than NeRF on many scenes. **Cons:** large memory and storage (hundreds of MB), artifacts in sparse views, less compact, editing and anti-aliasing issues.

### DL03-190
A **Siamese network** has two (or more) branches with **shared weights** that embed two inputs, followed by a distance or similarity function. The goal is to learn an embedding where similar items are close.
**Training:**
- **contrastive loss** on pairs: pull same-class pairs together and push different-class pairs at least a margin m apart (L = y·d² + (1 − y)·max(0, m − d)²);
- or **triplet loss** (anchor, positive, negative);
- or binary classification on the |f(a) − f(b)| features.

**Applications:** face verification (DeepFace, FaceNet), signature and fingerprint verification, person and vehicle re-identification, one-shot classification, image retrieval and deduplication, object tracking (SiamFC, SiamRPN template matching), change detection in satellite imagery.
It generalizes to **new identities without retraining**: just compare embeddings.

### DL03-191
**Triplet loss:** for an anchor a, a positive p (same class) and a negative n (different class): L = max(0, ‖f(a) − f(p)‖² − ‖f(a) − f(n)‖² + α). It requires the negative to be farther than the positive by margin α (FaceNet).
**Why mining matters:** most random triplets are **easy** (already satisfy the margin, giving zero loss and no gradient), so training stalls. But the **hardest** negatives can be label noise or cause collapse (all embeddings equal) and unstable training.
**Strategies:**
- **semi-hard** negatives (farther than the positive but within the margin; FaceNet), mined **online within large batches**;
- **batch-hard** (hardest positive and negative per anchor in the batch);
- distance-weighted sampling.

Alternatives that avoid mining: multi-similarity loss, N-pair or InfoNCE losses, and proxy-based or classification-margin losses (ArcFace), which are often more stable.

### DL03-192
**Margin-based softmax losses** train face embeddings as a classification problem over training identities, with an **angular margin** for compactness:
- L2-normalize both the features and the class weights, so the logit = s·cos θ_y (θ_y is the angle to the class center, s the scale, e.g. 64).
- **ArcFace** adds an **additive angular margin m** (≈ 0.5) to the target angle: logit_y = s·cos(θ_y + m). The model must place a sample at least m radians closer to its own class center than the decision boundary, giving **tighter intra-class clusters and larger inter-class gaps** on the hypersphere. Related: SphereFace (multiplicative margin), CosFace (cos θ − m).
- At test time the classifier is discarded and the **normalized embedding** is used with cosine similarity.

**Verification (1:1):** "is this the same person as the claimed identity?" Compare two embeddings and threshold the similarity; evaluated with TAR at a fixed FAR (e.g. 1e-6), ROC.
**Identification (1:N):** "who is this?" Search a gallery of N enrolled identities for the nearest match (plus open-set rejection if no match exceeds the threshold); evaluated with rank-1 accuracy and the FPIR/FNIR trade-off. It is harder as N grows.

### DL03-193
- **Two-stage fine-tuning:** first learn features (fine-tune the backbone with standard or mildly balanced sampling), then **retrain the classifier head with class-balanced sampling** (decoupled training).
- **Loss:** class-weighted cross-entropy, focal loss, class-balanced loss, LDAM with deferred re-weighting, logit adjustment.
- **Sampling:** oversample minority classes (with strong augmentation to avoid memorizing repeats); undersample the majority carefully.
- **Freeze more of the backbone** if minority classes have few examples, to avoid overfitting them; use a pretrained backbone with good general features.
- **Augment** minority classes more (Mixup or CutMix variants such as Remix that favor the minority label), synthetic generation.
- **Evaluate** with macro-F1, per-class recall, balanced accuracy and PR-AUC; **tune decision thresholds** per class on validation data.
- Consider anomaly detection or metric learning if a class is extremely rare.

### DL03-194
- **Fine-tuning** on labeled target data (the most effective with even a few hundred labels): lower learning rate, unfreeze progressively, re-estimate BN statistics.
- **Unsupervised domain adaptation** (no target labels):
  - **feature alignment:** match source and target feature distributions (MMD, CORAL);
  - **adversarial** domain classifier with gradient reversal (DANN);
  - **self-training:** pseudo-label confident target samples and retrain (with consistency regularization, teacher–student);
  - **AdaBN:** recompute BatchNorm statistics on target data (simple and surprisingly effective);
  - **test-time adaptation** (TENT: entropy minimization).
- **Input-level alignment:** image translation (CycleGAN) to make source images look like the target, color and style normalization, physics-based augmentation.
- **Domain-specific self-supervised pretraining** on unlabeled target images (continued pretraining).
- Validate on a small labeled target set; monitor for negative transfer.

### DL03-195
- **Feature-distribution distances:** embed both datasets with a pretrained network, then compute **FID / Fréchet distance**, **MMD**, CORAL distance (covariance difference) or Wasserstein distance between the feature distributions.
- **Proxy A-distance (domain classifier):** train a classifier to tell source from target. Accuracy near 50% means the domains are similar; near 100% means very different. d_A = 2(1 − 2·error).
- **Transferability estimators:** LogME, LEEP, NCE, H-score estimate how well pretrained features will fit target labels without full fine-tuning.
- **Low-level statistics:** color histograms, intensity distributions, resolution, object scale; quick visual inspection and t-SNE or UMAP plots of embeddings.
- **Empirical:** linear probe accuracy of source features on a small labeled target sample.

### DL03-196
Knowledge distillation trains a **student** to mimic a **teacher**:
- **Response-based (Hinton):** minimize the KL divergence between temperature-softened teacher and student outputs, L = α·CE(y, p_s) + (1 − α)·T²·KL(p_t^T ‖ p_s^T). The soft targets ("dark knowledge") convey class similarities.
- **Feature-based:** match intermediate features or attention maps (FitNets, attention transfer); relation-based (pairwise similarity structure).

**As transfer learning:**
- transfer knowledge from a **large pretrained model** (or a model trained on a different, larger domain) into a **smaller or differently structured** student for deployment;
- **cross-modal distillation:** an RGB teacher supervises a depth, thermal or lidar student on paired unlabeled data;
- **unlabeled target data:** the teacher's soft labels on target-domain images act as pseudo-labels for adaptation (self-training and Noisy Student);
- distilling foundation models (CLIP, DINOv2, SAM) into task-specific efficient models.

### DL03-197
**DANN (Domain-Adversarial Neural Network):** a shared feature extractor feeds two heads:
1. a **label classifier**, trained on labeled source data;
2. a **domain classifier**, which predicts source versus target.

A **gradient reversal layer** between the features and the domain classifier multiplies the gradient by −λ during backprop. The domain classifier learns to distinguish domains, while the feature extractor is pushed to **fool it**, learning **domain-invariant features** that are also discriminative for the task. Theory (Ben-David et al.): target error ≤ source error + domain divergence + λ*, so minimizing divergence while keeping source error low bounds target error.
**Caveats:**
- aligning marginal feature distributions can **misalign classes** (conditional shift), so class-conditional variants (CDAN) help;
- it fails if label distributions differ greatly;
- adversarial training is unstable.

### DL03-198
**Meta-learning ("learning to learn")** trains across **many tasks** so the model can **adapt quickly** to a new task from a few examples.
- **Optimization-based (MAML):** learn an initialization from which a few gradient steps on a new task's support set give good performance. The outer loop optimizes the post-adaptation loss (second-order or first-order approximations such as Reptile).
- **Metric-based:** prototypical networks, matching networks, relation networks learn an embedding space where comparison works for new classes.
- **Model-based:** memory-augmented networks, black-box learners.

**Relation to transfer learning:** both reuse prior knowledge. Transfer learning pretrains on one big source task and fine-tunes once. Meta-learning explicitly optimizes for **fast adaptation** over a distribution of tasks, with episodic training matching the few-shot test setting. In practice, large-scale pretraining plus simple fine-tuning often matches meta-learning in few-shot benchmarks.

### DL03-199
This is **class-incremental (continual) learning**, where the risk is **catastrophic forgetting**.
- **Simplest robust option:** if the car data is still available, **retrain or fine-tune on cars plus trucks jointly**, with a new head covering all classes.
- **If old data is limited:**
  - **rehearsal / replay:** keep a small exemplar memory of car images (herding selection, as in iCaRL) and mix it with truck data;
  - **knowledge distillation (LwF):** keep the old model's outputs on new images as soft targets so car predictions do not drift;
  - **regularization (EWC):** penalize changes to weights important for cars (Fisher information);
  - **parameter isolation:** freeze the backbone and add new heads, adapters or a new branch for trucks;
  - **bias correction** for the classifier's preference toward new classes (BiC, weight aligning).
- **Evaluate** accuracy on old and new classes separately and overall (average incremental accuracy, forgetting measure).
- If trucks are a separate task, a separate head with a shared frozen backbone is simplest.

### DL03-200
**Approach:**
1. Start from the X-ray model (or ideally a general medical or self-supervised model).
2. Adapt the input: MRI is often 3D (multi-slice), multi-sequence (T1, T2, FLAIR) and has a different intensity range, so modify the stem (channel mapping, 2.5D slices or a 3D-inflated network), use MRI-specific intensity normalization (z-score per volume, bias-field correction) and resampling.
3. **Fine-tune** most layers (large domain gap) with a small learning rate; re-estimate normalization statistics; apply **self-supervised pretraining on unlabeled MRI** first if available.
4. Augment realistically (rotations, intensity and bias-field variation, noise).
5. Validate with patient-level splits and radiologist review.

**What can go wrong:**
- **negative transfer:** X-ray features (projection images, bone contrast) do not match MRI tissue contrast, so performance can fall below training from scratch or MRI-pretrained baselines;
- different anatomy and pathology appearance, 2D versus 3D mismatch;
- scanner and protocol shift;
- overfitting with small MRI data;
- hidden label or prevalence differences;
- spurious cues (markers, text overlays) learned from X-ray.

### DL03-201
- **Dataset bias:** ImageNet and web data over-represent certain geographies, skin tones, genders, Western objects and contexts, so models perform worse on under-represented groups (face recognition error disparities; household objects from low-income countries).
- **Stereotyped associations** (gender and occupation; CLIP linking demographics with offensive labels).
- **Shortcut features:** texture bias, background and context reliance.
- **Label noise and offensive categories** in source datasets (ImageNet person subtree issues).
- **Spurious correlations** transferred into downstream tasks (medical, hiring, policing) can cause unfair or harmful outcomes.
- **Privacy and consent** issues in scraped training data; licensing restrictions.

**Mitigation:** evaluate disaggregated metrics by subgroup, use balanced fine-tuning data, apply fairness constraints and audits, document models (model cards), choose pretraining data carefully, and keep humans in the loop for high-stakes use.

### DL03-202
**Why transfer works:**
- **Feature reuse:** early layers learn general, domain-agnostic features (edges, textures, Gabor-like filters), so lower layers transfer best (Yosinski et al.).
- **Better initialization:** pretrained weights land in a good basin of the loss landscape; fine-tuned models stay close to it (Neyshabur et al., "What is being transferred?"). Benefits come from both feature reuse and low-level statistics.
- **Theory:** domain-adaptation bounds (Ben-David), where target error ≤ source error + divergence + combined error; representation-learning views (shared low-dimensional structure across tasks).
- **Inductive bias and regularization** from large, diverse pretraining data.

**Negative transfer** occurs when:
- source and target domains or tasks are **dissimilar** (natural images versus spectrograms or medical images with different statistics);
- source features encode spurious or conflicting cues;
- the target dataset is large enough that the pretraining prior just constrains the model;
- the architecture or input mismatch is poorly adapted;
- there are optimization issues (too-high learning rate destroying features, BN statistics mismatch).

### DL03-203
- **Classification:** accuracy and top-k accuracy; precision, recall, F1 (macro and micro); confusion matrix; ROC-AUC and PR-AUC (imbalanced data); log loss; calibration (ECE, reliability diagrams); per-class and per-slice metrics.
- **Detection:** **mAP** (COCO AP@[.5:.95], AP50, AP75, AP_S/M/L), average recall, precision and recall at an operating threshold, per-class AP, FPS and latency.
- **Segmentation:** **mIoU** and per-class IoU, Dice (medical), pixel accuracy (with caution), boundary F1 and HD95; for instance and panoptic tasks, mask AP and **PQ** (SQ, RQ).
- **Always also:** robustness (corruption and shift tests), fairness across subgroups, and efficiency (latency, memory).

### DL03-204
- **Deduplicate first:** detect exact and near-duplicates with perceptual hashing (pHash, dHash) or **embedding similarity** (CLIP or DINO features, cosine above a threshold), and put each duplicate cluster in **one** split.
- **Group-aware splitting:** split by **patient ID**, scene, video, camera, location, session, photographer or product, never by image (GroupKFold / StratifiedGroupKFold), so correlated images cannot leak.
- **Video and burst data:** split by whole video, not frame; for time-dependent data, split **by time** (train on the past, test on the future).
- **Keep class stratification** within groups where possible, and verify after splitting: run embedding nearest-neighbor search from test to train and inspect the closest pairs.
- Hold out entire sites or hospitals and devices to measure generalization to new sources.

### DL03-205
**Finding noisy labels:**
- **confident learning / cleanlab:** use out-of-fold predicted probabilities to estimate the joint noise distribution and flag likely mislabeled samples;
- **high-loss samples** (or samples whose loss stays high, area under the margin), disagreement between models or folds;
- **embedding-based outliers:** an image whose nearest neighbors carry a different label;
- **annotator disagreement**, cross-checks against metadata.

**Handling:**
- **relabel** flagged samples with expert review (prioritize by confidence) or remove the worst;
- **noise-robust training:** label smoothing, symmetric or generalized cross-entropy, bootstrapping loss, Co-teaching or DivideMix (train on small-loss samples, treat others as unlabeled), early stopping (networks memorize noise late);
- improve labeling guidelines and add consensus labeling for ambiguous classes;
- keep a **clean, expert-verified test set**.

### DL03-206
Loop:
1. Train on the current labeled set.
2. Score the unlabeled pool with an **acquisition function**.
3. Send the top-k images (a batch) to annotators.
4. Add them and retrain; repeat until the budget is spent or performance plateaus.

**Acquisition strategies:**
- **Uncertainty:** least confidence, margin (top-1 minus top-2), entropy; for detection, aggregate box-level uncertainties; Monte Carlo dropout or ensembles for epistemic uncertainty (BALD).
- **Diversity / representativeness:** core-set selection (k-center greedy in embedding space), clustering, to avoid redundant batches.
- **Hybrid:** BADGE (gradient embeddings plus k-means++), uncertainty within diverse clusters.

**Practical points:** start with a random or diverse seed set; account for class imbalance and the cold start; check for outliers and noise (uncertainty sampling picks ambiguous or garbage images); compare against random sampling, which is a strong baseline; consider labeling cost (boxes and masks cost more).

### DL03-207
**Synthetic data helps when:**
- real data is scarce, expensive or dangerous to collect (rare defects, accidents, medical rarities);
- **perfect labels** are needed (depth, segmentation, pose, optical flow);
- rare edge cases or controllable variation are needed;
- privacy blocks real data.

**Sim-to-real gap:** differences in appearance (textures, lighting, noise), content and distributions.
**Closing it:**
- **Domain randomization:** heavily vary textures, lighting, camera parameters, backgrounds and distractors so that reality looks like "just another variation";
- **photorealistic rendering** (game engines, Omniverse) and accurate physical sensor models (noise, blur, lens distortion);
- **image translation:** GANs or diffusion models make synthetic images look real (CycleGAN), or style augmentation;
- **mix synthetic with a small amount of real data;** fine-tune on real data last;
- **domain adaptation** (adversarial feature alignment, AdaBN, pseudo-labeling on real data);
- validate on real held-out data and match the scene statistics (object scales, viewpoints).

### DL03-208
**Adversarial examples** are inputs with tiny, often imperceptible perturbations (e.g. ‖δ‖_∞ ≤ 8/255) crafted to cause misclassification. They exist because models are highly linear locally and rely on non-robust but predictive features.
**Attacks:**
- **FGSM:** x + ε·sign(∇_x L);
- **PGD:** iterated FGSM with projection;
- C&W, AutoAttack;
- black-box transfer and query attacks;
- physical attacks (adversarial patches, stickers on stop signs).

**Defenses:**
- **Adversarial training** (Madry et al.): train on PGD examples, i.e. solve min_θ E[max_(‖δ‖≤ε) L(x + δ, y)]. It is the most reliable empirical defense; costly (≈ 7–10× training time) and reduces clean accuracy (TRADES balances the two).
- **Certified defenses:** randomized smoothing, interval bound propagation, which give provable radius guarantees.
- Input preprocessing and denoising, detection of adversarial inputs, ensembles. Many were broken by adaptive attacks ("obfuscated gradients").
- Evaluate with strong adaptive attacks (AutoAttack), not just FGSM.

### DL03-209
**Shortcut learning:** the model exploits **spurious cues** that correlate with labels in the training data but not in deployment.
**Examples:**
- cows recognized by green pasture backgrounds;
- pneumonia predicted from hospital-specific X-ray markers or portable-scanner artifacts;
- watermarks or text tags;
- **texture over shape** (ImageNet CNNs classify a cat-shaped object with elephant texture as an elephant).

**Detection:**
- **saliency and Grad-CAM** showing the model attends to background or markers;
- **counterfactual and controlled tests:** swap backgrounds (ImageNet-9 background challenge), cue-conflict stimuli (stylized ImageNet), mask the object or the background, crop out markers;
- evaluate on **out-of-distribution splits** (new hospitals, locations), where performance drops reveal shortcuts;
- slice analysis by metadata;
- training a model on the **suspected cue alone** (e.g. background only): high accuracy means a shortcut is available.

**Mitigation:** diverse and balanced data, augmentation that breaks the cue (Stylized ImageNet, background randomization), group-robust training (GroupDRO, JTT), removing cues at the source.

### DL03-210
- **Corruption benchmarks:** ImageNet-C / CIFAR-10-C (15 corruptions: noise, blur, weather, digital such as JPEG and pixelate, at 5 severities). Report **mean Corruption Error (mCE)**, normalized by a baseline (AlexNet), and **relative mCE** (degradation from clean accuracy). ImageNet-P measures prediction stability under small perturbations (flip rate).
- **Distribution-shift test sets:** ImageNet-V2 (re-collected), ImageNet-R (renditions), ImageNet-Sketch, ImageNet-A (natural adversarial examples), ObjectNet (unusual poses and backgrounds), WILDS (real-world domain shifts).
- **Domain-specific stress tests:** simulate your deployment conditions (camera noise, low light, compression, rain, motion blur, sensor dropout) and **measure the accuracy curve against severity**; slice by metadata (device, location, time).
- Also: calibration under shift, OOD detection AUROC, adversarial robustness (AutoAttack).
- Improve with augmentation (AugMix, DeepAugment), larger pretrained models and diverse training data.

### DL03-211
**Why miscalibrated:** modern deep networks are **overconfident**: predicted confidence exceeds actual accuracy (Guo et al., 2017). Causes include high capacity and overfitting of the NLL (the network keeps increasing logit magnitude after accuracy saturates), weak weight decay and BN effects, and distribution shift, under which confidence remains high.
**Measuring:** reliability diagrams; **Expected Calibration Error** (ECE: bin by confidence, weighted |accuracy − confidence|); NLL; Brier score; class-wise and adaptive ECE.
**Calibrating:**
- **temperature scaling:** divide the logits by a scalar T > 1 fitted on validation NLL. Simple, keeps accuracy unchanged, very effective in-distribution;
- vector or matrix (Platt) scaling, isotonic regression, histogram binning, Dirichlet calibration;
- **training-time:** label smoothing, Mixup, focal loss, ensembles and MC dropout (better calibrated and better under shift);
- recalibrate after quantization and deployment changes; check calibration under shift too.

### DL03-212
1. **Capture:** cameras with suitable resolution, shutter speed (motion blur), IR illumination for night; region-of-interest (lanes, gates).
2. **Vehicle and plate detection:** a real-time detector (YOLO or SSD) for plates (optionally detect vehicles first), robust to angle, size, lighting and occlusion.
3. **Rectification:** perspective correction or keypoint-based alignment of plate corners; handle two-line plates and different country formats.
4. **Recognition (OCR):** a CRNN with CTC, or an attention or transformer OCR on the plate crop (segmentation-free); a region-specific character set.
5. **Post-processing:** validate against country and format regex rules, character confusion handling (0/O, 1/I, 8/B); **temporal voting across video frames** with tracking (SORT) to choose the most confident reading.
6. **Data:** diverse real plates plus synthetic plate generation; augment blur, low light, rain, glare and viewing angles.
7. **Deployment:** edge inference (Jetson, NPU) for latency and bandwidth; send events to a backend database; privacy and retention compliance.
8. **Metrics:** detection recall, character and plate-level accuracy, end-to-end read rate, FPS, and failure analysis by condition.

### DL03-213
**Sensors:** surround cameras, lidar, radar, ultrasonic sensors, GNSS and IMU.
**Perception tasks:**
- 2D and 3D object detection (vehicles, pedestrians, cyclists);
- tracking and motion prediction;
- lane, road-boundary and drivable-area segmentation;
- traffic light and sign recognition;
- depth and 3D occupancy;
- free-space estimation;
- localization against HD maps (or mapless online mapping).

**Architecture choice:** a **multi-task, multi-sensor BEV network**:
- per-camera backbones (RegNet, EfficientNet or ConvNeXt) with an FPN;
- a **view transformation into a shared BEV space** (LSS or BEVFormer), fused with lidar (voxel or pillar encoders) and radar features (BEVFusion);
- **temporal fusion** across frames;
- **multiple heads:** 3D detection (CenterPoint or DETR-style), map segmentation, 3D occupancy, motion forecasting, sharing the backbone for efficiency.

**Requirements:** real-time (≥ 10–30 Hz) on automotive SoCs, redundancy and safety (separate fallback pipelines, uncertainty estimates), rigorous evaluation across weather, night and long-tail scenarios, and data engines that mine hard cases from the fleet. Trends: end-to-end and occupancy networks.

### DL03-214
1. **Problem definition with clinicians:** task (classification, detection, segmentation), clinical endpoint, intended use and population, acceptable sensitivity and specificity at the operating point.
2. **Data:** multi-site, multi-scanner datasets; **expert labels** (multiple readers, adjudication, inter-rater agreement); DICOM handling, de-identification; **patient-level splits**; external test set from unseen hospitals.
3. **Preprocessing:** modality-specific normalization (CT windowing, MRI z-score), resampling to isotropic spacing, 2D, 2.5D or 3D patches.
4. **Model:** nnU-Net or U-Net-family networks for segmentation, CNN or ViT classifiers, pretrained on medical data (RadImageNet, self-supervised); class-imbalance losses (Dice + focal); appropriate augmentation.
5. **Evaluation:** AUC, sensitivity and specificity with CIs, Dice and HD95, calibration, subgroup analysis (age, sex, scanner), external validation, reader studies comparing against and with radiologists.
6. **Explainability and safety:** saliency maps, uncertainty estimates, OOD detection, human-in-the-loop workflow (triage or second reader, not autonomous).
7. **Deployment and regulation:** PACS integration, monitoring for drift (new scanners), FDA or CE approval, privacy (HIPAA, GDPR), post-market surveillance.

### DL03-215
1. **Ingestion:** decode RTSP or streams with hardware decoders (NVDEC); frame skipping or adaptive FPS; batch frames from multiple streams.
2. **Detector:** a real-time model (YOLO or RT-DETR) at an input size chosen for the speed and accuracy target; TensorRT FP16 or INT8; dynamic batching.
3. **Tracking:** ByteTrack or DeepSORT, for stable IDs, smoothing and fewer per-frame detections (detect every N frames and track in between).
4. **Post-processing:** NMS (GPU-based), zone rules, event logic (counting, intrusion).
5. **Pipeline:** an asynchronous producer–consumer design (DeepStream or GStreamer), with GPU-resident data to avoid copies and backpressure handling; latency budget per stage.
6. **Scaling:** edge devices near the cameras for latency and bandwidth, or a central GPU cluster; horizontal scaling per stream count; graceful degradation (lower FPS or resolution under load).
7. **Monitoring:** throughput, end-to-end latency (p95), dropped frames, detection quality on sampled frames, drift; retraining with hard examples from production.

### DL03-216
- **Recognition:** products are many (10k+ SKUs), fine-grained, frequently changing, with packaging updates. Use a **detector** for "product" or category-level boxes, then **embedding-based retrieval** (metric learning with ArcFace or contrastive loss, on product crops) against a reference gallery, so new SKUs are added by enrolling images without retraining. Use OCR on labels and barcodes when visible.
- **Data:** studio reference images plus in-store photos; synthetic shelf rendering; domain adaptation from studio to shelf images.
- **Shelf analytics:** planogram compliance, out-of-stock detection (empty-space detection), price-tag reading (OCR) and matching.
- **Tracking (checkout-free or shopper analytics):** multi-camera person tracking (re-ID), hand–product interaction detection (pick or put events), sensor fusion with weight shelves.
- **Deployment:** edge inference in-store, periodic shelf scans (robots or fixed cameras), privacy protection (no face storage).
- **Metrics:** top-1/top-5 retrieval accuracy, detection mAP, OOS detection precision and recall, latency.

### DL03-217
- **Data specifics:** multispectral or hyperspectral bands (beyond RGB: near-infrared, short-wave infrared), very large tiles (tile into 256–512 px patches with overlap), varying resolution (GSD), cloud cover, seasonal and atmospheric variation, georeferencing.
- **Preprocessing:** atmospheric correction, cloud masking, per-band normalization, co-registration; use indices (NDVI) as extra channels.
- **Models:**
  - scene classification with CNNs or ViTs (adapt the first conv to N bands);
  - semantic segmentation (U-Net or DeepLab) for land cover, buildings and roads;
  - detection for ships, planes and vehicles, with **rotated bounding boxes**;
  - **change detection** with Siamese or temporal models over image time series.
- **Pretraining:** remote-sensing foundation models (SatMAE, Prithvi, SSL4EO) rather than ImageNet.
- **Augmentation:** rotations and flips (no canonical orientation), radiometric jitter.
- **Evaluate** with spatially separated splits (avoid geographic leakage), per-region metrics.
- **Monitoring use-cases:** deforestation, crops, disasters, urban growth; deploy as batch pipelines over new acquisitions.

### DL03-218
- **Tracking and mapping (SLAM / VIO):** detect and track visual features (ORB, FAST, learned features) and fuse them with the IMU (visual-inertial odometry) to estimate the **6-DoF device pose** in real time, while building a sparse or dense map of the environment (ARKit, ARCore). Loop closure and relocalization correct drift.
- **Scene understanding:**
  - plane detection (floors, tables) for placing objects;
  - **depth estimation** (LiDAR, stereo, or monocular networks) for occlusion and physics;
  - **semantic segmentation** and object detection (people, furniture) for occlusion masks and interactions;
  - light estimation for realistic rendering.
- **Image and marker tracking:** recognize known images or objects and track their pose (homography or PnP).
- **Human-centric:** face meshes, hand tracking, body pose for filters and interaction.
- **Constraints:** very low latency (< 20 ms motion-to-photon), mobile power and compute, robustness to motion blur and low texture.

### DL03-219
1. **Query processing:** detect and crop the product in the user's photo (a detector or SAM-assisted crop), handle multiple items, normalize.
2. **Embedding model:** a CNN or ViT (fine-tuned CLIP, DINOv2 or a domain-trained model) trained with **metric learning** (contrastive or triplet, ArcFace on product IDs, or a multimodal image–text contrastive loss) so that the same or similar products cluster despite lighting, background and angle; train on street-to-shop pairs (user photos versus catalog images).
3. **Index:** embed all catalog images offline; store them in an **approximate nearest neighbor** index (FAISS, HNSW or IVF-PQ) for millisecond search at scale; update incrementally for new products.
4. **Retrieval and ranking:** top-k ANN candidates, then re-rank with a finer model and business signals (availability, price, popularity), category filters and attribute matching (color, pattern).
5. **Evaluation:** recall@k and mAP on street-to-shop test pairs, plus online CTR and conversion.
6. **Operations:** latency budget, embedding versioning (re-index on model updates), deduplication, monitoring.

### DL03-220
With very few defects, frame it mainly as **anomaly detection** (learn "normal"):
- **Data capture:** controlled imaging (fixed lighting, camera, triggering) to reduce nuisance variation; collect many normal samples.
- **Unsupervised anomaly detection:** methods trained only on good parts:
  - **PatchCore** (memory bank of pretrained patch features with nearest-neighbor distance);
  - PaDiM (Gaussian per patch location);
  - student–teacher, reconstruction-based (autoencoders, diffusion) or normalizing flows (FastFlow).

  They output an image-level score and a **pixel-level anomaly map** to localize defects.
- **Use the few defects you have** for validation and threshold setting, and for supervised or semi-supervised fine-tuning; **synthesize defects** (CutPaste, DRAEM-style synthetic anomalies, rendered scratches) for augmentation.
- **Thresholding:** choose an operating point that meets the miss-rate requirement (high recall); route borderline cases to human inspection.
- **Evaluate:** image AUROC, pixel AUROC and PRO, recall at a fixed false-positive rate; benchmark on MVTec AD-style splits.
- **Deployment:** inference within line takt time on edge GPUs or industrial PCs; monitoring for drift (lighting, new product variants); feedback loop to label new defect types.

### DL03-221
**Why detection breaks down:**
- extreme density and **heavy occlusion**: heads overlap and only fragments are visible;
- **tiny objects** (a few pixels per head) and large **scale variation** from perspective;
- NMS suppresses true neighbors;
- box annotations are impractical.

**Density-map regression instead:**
- annotate only **head points**, convolve each with a (geometry-adaptive) Gaussian kernel to get a **density map** whose **integral equals the count**;
- train a CNN (MCNN multi-column, CSRNet with dilated convs, or transformer-based) to regress the density map with a pixel-wise L2 loss, or a Bayesian or distribution-matching loss (DM-Count);
- the count is the sum of the predicted map, which also shows where people are.

**Alternatives:** point-based localization (P2PNet) to get counts plus locations. Handle perspective with multi-scale features. **Evaluate** with MAE and RMSE of counts (ShanghaiTech, UCF-QNRF), and check robustness to lighting and camera angle.

### DL03-222
**Export:**
1. Set the model to eval mode; **export to ONNX** (torch.onnx.export) with a fixed or dynamic input shape and the right opset; validate with ONNX Runtime and check for unsupported ops.
2. Build a **TensorRT engine** (trtexec or the Python API) for the target GPU, with FP16 and INT8 enabled, optimization profiles for dynamic shapes and layer fusion. INT8 needs **calibration** with a representative dataset (entropy or minmax calibrators, ~500–1000 diverse images in production-like conditions), or a QAT model with Q/DQ nodes.

**Accuracy checks after INT8:**
- compare outputs to the FP32 PyTorch model **layer-wise and end-to-end**: cosine similarity and max abs error of logits;
- task metrics on the full validation set: **top-1 and mAP drop** (typically < 1% is acceptable);
- **per-class and per-slice metrics** (small objects, rare classes, low-light images), where quantization errors concentrate;
- confidence calibration and **threshold re-tuning**, since score distributions shift;
- identical **preprocessing and post-processing** (NMS, decoding) in the deployed pipeline;
- sensitivity analysis: keep sensitive layers in FP16 (mixed precision) if accuracy drops;
- latency and throughput on the device.

### DL03-223
At 30 FPS the total budget is **≈ 33 ms per frame** (less if other workloads share the device; target ≤ 25 ms p95 for headroom).
1. **Measure each stage** on the device: capture and decode, preprocessing (resize, normalize, layout conversion), model inference, post-processing (decode boxes, NMS, tracking), output and rendering.
2. **Typical budget:** decode and preprocessing 3–5 ms (do them on GPU or ISP with hardware resize, avoid CPU copies), inference 15–20 ms, post-processing 2–5 ms, slack 3–5 ms.
3. **Optimize the model:** smaller backbone or input size, TensorRT or NPU compilation, INT8 or FP16, structured pruning, operator fusion.
4. **Optimize the pipeline:** **pipelining and parallelism** (preprocess frame t+1 while inferring frame t; overall throughput is limited by the slowest stage, while latency is the sum), zero-copy buffers, efficient or class-agnostic NMS, top-k pre-filtering before NMS.
5. **Reduce work:** run the detector every N frames and track in between; region-of-interest cropping.
6. **Validate:** p50, p95 and p99 latency, thermal throttling over long runs, power limits, and accuracy at the chosen settings.

### DL03-224
- **FP32:** 4 bytes per parameter, so 138 × 10⁶ × 4 ≈ **552 MB** (≈ 527 MiB). The torchvision VGG-16 checkpoint is ≈ 528 MiB.
- **FP16:** 2 bytes per parameter, so ≈ **276 MB** (≈ 263 MiB).
- INT8 would be ≈ 138 MB.

Most of this sits in the first FC layer (25,088 × 4,096 ≈ 103M parameters). This is why replacing FC heads with global average pooling shrinks models dramatically. Note that runtime memory also includes activations (and, during training, gradients and optimizer states).

### DL03-225
- **19 weight layers: 16 convolutional + 3 fully connected.**
- **Input:** 224×224×3 RGB; preprocessing subtracts the **mean RGB value** of the training set (per-channel mean subtraction).
- **Convolutions:** all **3×3**, **stride 1, padding 1** (spatial size preserved).
- **5 blocks** of convs with 2, 2, 4, 4, 4 conv layers and **64, 128, 256, 512, 512** channels, each block followed by **2×2 max pooling with stride 2** (5 pools total, 224 → 7).
- **ReLU** after every conv and FC (no batch norm in the original).
- **FC layers:** 4096 → 4096 → 1000, with **dropout (0.5)** between the first FCs, and **softmax** at the end.
- ≈ **144M parameters**, ≈ 19.6 GFLOPs per image.

### DL03-226
- **Early layers** (conv1–conv2): generic edges and colors; transferable but not discriminative enough on their own.
- **Middle to late conv layers** (e.g. conv4 or conv5, or the last conv block before pooling): a good balance of semantic content and generality; often the **best for transfer**, especially to domains different from ImageNet. Aggregate them with global average or max pooling (or GeM).
- **Penultimate FC layers** (fc6/fc7 in VGG; the pooled 2048-d vector in ResNet): semantic and compact, very good when the target domain resembles ImageNet.
- **Layers closest to the output** (logits or fc8) are **specialized to the source task's 1000 classes**: features become task-specific, invariant to details the target task may need (texture, fine structure, position), and lower-dimensional. They transfer worse to dissimilar tasks (medical, texture, fine-grained).

**Rule:** the more different the target domain, the earlier the layer. Choose by validation (linear probe per layer), or concatenate features from multiple layers.

### DL03-227
- **Multi-layer features from one network:** extract features from several layers (e.g. conv4, conv5 pooled with GAP or GeM, plus fc7), L2-normalize each, concatenate (optionally reduce with PCA), and train a linear classifier or SVM on top. This captures both low-level texture and high-level semantics (hypercolumns).
- **Multiple pretrained networks:** extract embeddings from different architectures or pretraining schemes (ResNet, EfficientNet, ViT, CLIP, DINOv2), which bring complementary errors. Then either:
  - **early fusion:** concatenate the normalized embeddings, then train one classifier; or
  - **late fusion:** train a separate classifier per extractor and average or vote their probabilities, or **stack** them with a meta-classifier trained on out-of-fold predictions.
- **Tips:** normalize per extractor so no single high-dimensional feature dominates; regularize (high-dimensional concatenation can overfit small data); measure each member's contribution; consider the inference cost of running several backbones.

### DL03-228
- **Cross-correlation:** (f ⋆ k)[i, j] = Σ_m Σ_n f[i + m, j + n] · k[m, n]. Slide the kernel as-is.
- **Convolution:** (f ∗ k)[i, j] = Σ_m Σ_n f[i − m, j − n] · k[m, n]. Equivalent to cross-correlation with the kernel **flipped by 180°**.

Convolution is commutative and associative (useful in signal processing, where filters are composed); correlation is a similarity or template-matching measure.
**Deep learning libraries** (PyTorch Conv2d, TensorFlow, cuDNN) actually compute **cross-correlation** but call it convolution. Since kernels are learned, the flip does not matter: the network would just learn the flipped kernel. The flip appears in the **backward pass** (the gradient with respect to the input uses the rotated kernel).

### DL03-229
For a w×h single-channel image and a K×K kernel (same-size output):
- **Direct convolution:** **w·h·K²** multiplications and w·h·(K² − 1) additions per channel.
- **Separable kernel** (rank 1: K = u·vᵀ, e.g. Gaussian, box, Sobel): two 1D passes (rows with a K×1 kernel, then columns with a 1×K kernel) need **2·w·h·K** multiplications, a K/2 speed-up (e.g. 15×15: 225 versus 30 multiplications per pixel, 7.5× faster).

The 2D Gaussian factorizes as G(x, y) = G(x)·G(y). Very large kernels can also use **FFT** convolution, O(wh·log(wh)) regardless of K. For C_in → C_out channels, multiply by C_in·C_out.

### DL03-230
- **Removes magnitude effects:** embedding norms vary with image contrast, size or "confidence" rather than identity or content. Normalizing puts all vectors on the unit hypersphere so comparisons depend only on **direction** (semantic similarity).
- **Cosine similarity becomes a dot product:** fast matrix-multiply and MIPS/ANN search; Euclidean distance on normalized vectors is monotonic in cosine (‖a − b‖² = 2 − 2·cos), so any metric index works consistently.
- **Consistent thresholds:** similarity is bounded in [−1, 1], so a single verification threshold works across all pairs (face matching).
- **Matches training:** metric-learning losses (ArcFace, CosFace, contrastive or InfoNCE with cosine similarity) are trained on normalized embeddings, so inference must normalize too.
- **Stability:** reduces the influence of outlier dimensions and scale drift across model versions or domains.

### DL03-231
VGG-11's feature extractor has 8 conv layers (3×3, padding 1, so spatial size is preserved), each followed by ReLU, and **5 max-pool layers** (2×2, stride 2), so the spatial size is divided by 32 (floored at each pool). The final channel count is 512. Its **last layer is a MaxPool2d.**
- **224×224 → [1, 512, 7, 7]** (224/32 = 7).
- **512×512 → [1, 512, 16, 16].**
- **704×1024 → [1, 512, 22, 32]** (704/32 = 22, 1024/32 = 32).

It accepts any input size because it contains **only convolutions, ReLUs and pooling**, which slide over whatever spatial extent they get (no layer has a fixed input dimension). Only the FC classifier needs a fixed 7×7×512 input, which torchvision handles with AdaptiveAvgPool2d((7, 7)). Inputs smaller than 32×32 would collapse to zero size.

### DL03-232
1. **Conv 7×7, 32 filters, padding 2, stride 1:** H_out = (224 + 2·2 − 7)/1 + 1 = **222**, giving **32 × 222 × 222**. BatchNorm, if present, does not change the shape.
2. **MaxPool 2×2, stride 2:** ⌊222/2⌋ = **111**, giving 32 × 111 × 111.
3. **MaxPool 2×2, stride 2:** ⌊111/2⌋ = **55** (floor), giving **32 × 55 × 55**.

Output tensor: **[N, 32, 55, 55]**; flattened, 32 × 55 × 55 = **96,800** features per image. The conv has 7·7·3·32 + 32 = 4,736 parameters.
