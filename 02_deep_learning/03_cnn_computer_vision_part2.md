---
domain: dl
topic: cnn_computer_vision
title: CNNs and computer vision
tags: [cnn, computer-vision, detection, segmentation]
count: 113
part: 2/2
---
# CNNs and computer vision (part 2)

## CNN internals and training details
- [DL03-120] How does backpropagation work through convolutional and pooling layers?
- [DL03-121] What are the advantages of deep CNNs over shallow ones, and what makes very deep CNNs hard to train?
- [DL03-122] How do you choose the number and size of filters in a convolutional layer?
- [DL03-123] What are the differences between 1D, 2D and 3D convolutions, and what data is each suited to?
- [DL03-124] When would you choose a CNN over an RNN, and what are their typical use cases?
- [DL03-125] How is dropout applied in CNNs, and why is spatial dropout often preferred over standard dropout for conv features?
- [DL03-126] How do you normalize pixel values for a CNN, and why normalize with per-channel dataset mean and standard deviation?
- [DL03-127] How do you handle images with different aspect ratios during preprocessing: resizing, cropping or padding?
- [DL03-128] What techniques can reduce the computation time of a CNN at training and inference time?
- [DL03-129] How do attention modules such as squeeze-and-excitation or CBAM improve CNNs?
- [DL03-130] What are the limitations of CNNs in capturing global context, and how do dilated convolutions, non-local blocks or attention address them?
- [DL03-131] What are capsule networks, and how do they differ from standard CNNs?
- [DL03-132] How can you visualize what a convolutional layer has learned, for example with filter visualization, activation maps or Grad-CAM?
- [DL03-133] Why does batch normalization behave poorly with the small per-GPU batch sizes common in detection and segmentation, and what are the alternatives?
- [DL03-134] Why does a CNN trained at one resolution often do better when tested at a slightly higher resolution, and how do you fix the train-test resolution discrepancy?

## Modern backbones and vision transformers
- [DL03-135] How have CNN architectures evolved from LeNet and AlexNet through VGG and ResNet to EfficientNet?
- [DL03-136] What design changes turned ResNet into ConvNeXt, and what does ConvNeXt show about CNNs versus ViTs?
- [DL03-137] How does the Swin Transformer use shifted windows to make self-attention efficient for high-resolution images?
- [DL03-138] How does patch size affect a Vision Transformer's accuracy, sequence length and compute?
- [DL03-139] How does self-attention cost scale with image resolution in a ViT, and why does that matter for dense prediction tasks?
- [DL03-140] How do you fine-tune a ViT at a higher resolution than it was pre-trained at, and what happens to its positional embeddings?
- [DL03-141] What is the role of the CLS token in a ViT, and how does it compare to global average pooling of patch tokens?
- [DL03-142] When would you choose a CNN backbone over a ViT for a production vision system, and vice versa?
- [DL03-143] What are hybrid CNN-transformer architectures, and what does each part contribute?

## Self-supervised and vision-language representation learning
- [DL03-144] How does contrastive learning such as SimCLR learn image representations, and why does it need large batches or many negatives?
- [DL03-145] How do BYOL and DINO avoid representation collapse without negative pairs?
- [DL03-146] Why does a masked autoencoder use a very high masking ratio such as 75%, and why is the encoder applied only to visible patches?
- [DL03-147] How do you evaluate a self-supervised visual representation with linear probing, k-NN and fine-tuning, and why can they disagree?
- [DL03-148] How is CLIP trained, and what roles do the contrastive loss and the learned temperature play?
- [DL03-149] What are the known failure modes of CLIP, such as counting, spatial relations and typographic attacks?
- [DL03-150] What is zero-shot image recognition, and how does it differ from few-shot learning in computer vision?
- [DL03-151] What are the challenges of few-shot learning for image classification, and how do prototypical networks address them?

## Detection deep dive
- [DL03-152] What algorithms would you choose for real-time object detection, and why?
- [DL03-153] How does YOLO perform detection in a single forward pass, and what changed across later YOLO versions?
- [DL03-154] How do Haar cascades and the Viola-Jones detector work, and why were they replaced by CNN detectors?
- [DL03-155] How do anchor-free detectors such as FCOS or CenterNet work, and what problems with anchors do they avoid?
- [DL03-156] How does DETR use Hungarian matching to remove the need for NMS, and why does it converge slowly?
- [DL03-157] What is soft-NMS, and when does it beat standard non-maximum suppression?
- [DL03-158] How is COCO mAP computed across IoU thresholds and object sizes, and how is it different from PASCAL VOC mAP?
- [DL03-159] How does label assignment, deciding which predictions are positives during training, affect detector quality?
- [DL03-160] How do detection models deal with occlusion and partially visible objects?
- [DL03-161] How do open-vocabulary detectors such as OWL-ViT or Grounding DINO detect classes never seen in the detection training set?
- [DL03-162] How would you handle a long-tailed detection dataset where a few classes have only a handful of boxes?
- [DL03-163] How does test-time augmentation work for detection, and how do you merge the resulting boxes?

## Segmentation deep dive
- [DL03-164] What is panoptic segmentation, and how is panoptic quality (PQ) computed?
- [DL03-165] How do DeepLab's atrous convolutions and ASPP capture multi-scale context?
- [DL03-166] How does Mask2Former unify semantic, instance and panoptic segmentation with mask classification?
- [DL03-167] What does the Segment Anything Model (SAM) do, and how does promptable segmentation differ from class-specific segmentation?
- [DL03-168] How can depth information from RGB-D sensors be used to improve semantic segmentation?
- [DL03-169] Why do segmentation models often produce poor boundaries, and how would you improve boundary quality?
- [DL03-170] Pixel-level labels are expensive. How would you train a segmentation model with weak labels such as boxes, points or image tags?

## Classical vision and geometry
- [DL03-171] How does the Histogram of Oriented Gradients (HOG) descriptor work?
- [DL03-172] Compare SIFT, SURF, ORB and HOG as hand-crafted feature extractors in speed, invariance and typical use.
- [DL03-173] How does the Hough transform detect lines and circles?
- [DL03-174] What are morphological operations such as erosion, dilation, opening and closing, and when are they used?
- [DL03-175] What is histogram equalization, and when would you use CLAHE instead?
- [DL03-176] What are image pyramids, and how are they used in multi-scale detection and blending?
- [DL03-177] What is a homography, and how do you estimate it robustly with RANSAC for panorama stitching?
- [DL03-178] What are a camera's intrinsic and extrinsic parameters, and how is a camera calibrated?
- [DL03-179] What is epipolar geometry, and how are the fundamental and essential matrices used in stereo vision?
- [DL03-180] How does neural style transfer use content and style losses, and why does the Gram matrix capture style?

## Video, tracking, pose and 3D
- [DL03-181] How can CNNs be used for human activity recognition in video, and how do two-stream networks, 3D convolutions and video transformers compare?
- [DL03-182] How can CNNs be combined with RNNs, as in CNN-LSTM models, to model video or image sequences?
- [DL03-183] How do (2+1)D convolutions factor a 3D convolution, and why can they train better?
- [DL03-184] How are multi-object tracking systems evaluated with metrics such as MOTA, IDF1 and HOTA?
- [DL03-185] What is pose estimation, and how do top-down and bottom-up approaches differ?
- [DL03-186] How does stereo depth estimation work, and why is monocular depth estimation fundamentally ambiguous?
- [DL03-187] How does PointNet process unordered point clouds, and how does it achieve permutation invariance?
- [DL03-188] What is a bird's-eye-view (BEV) representation, and why do autonomous driving stacks use it?
- [DL03-189] How do NeRF and 3D Gaussian splatting represent a scene, and what are their tradeoffs in quality and rendering speed?

## Transfer learning, few-shot and domain adaptation
- [DL03-190] What are Siamese networks, how are they trained, and where are they applied in computer vision?
- [DL03-191] How do triplet loss and hard-negative mining work for metric learning, and why does mining strategy matter?
- [DL03-192] How do face recognition systems use margin-based losses such as ArcFace, and how do face verification and identification differ?
- [DL03-193] How would you approach transfer learning when the target dataset is heavily imbalanced?
- [DL03-194] How can you adapt a pre-trained model from one domain to a different but related domain?
- [DL03-195] How can you measure how similar the source and target domains are before attempting transfer?
- [DL03-196] How can knowledge distillation be used as a form of transfer learning?
- [DL03-197] How does adversarial training, as in domain-adversarial neural networks, help with unsupervised domain adaptation?
- [DL03-198] What is meta-learning, and how does it relate to transfer learning?
- [DL03-199] How would you extend a model trained to recognize car models so that it also recognizes trucks without forgetting cars?
- [DL03-200] How would you transfer knowledge from a model trained on X-ray images to MRI images, and what could go wrong?
- [DL03-201] What risks of inherited bias come with using pre-trained vision models?
- [DL03-202] What theories explain why transfer learning works, and when does it give negative transfer?

## Data, robustness and evaluation in vision
- [DL03-203] What metrics would you use to evaluate a vision model for classification, detection and segmentation?
- [DL03-204] How would you split an image dataset to avoid leakage from near-duplicates, the same patient or the same scene?
- [DL03-205] How do you find and handle label noise in a large image dataset?
- [DL03-206] How would you use active learning to decide which images to label next?
- [DL03-207] When does synthetic data or domain randomization help a vision model, and how do you close the sim-to-real gap?
- [DL03-208] What are adversarial examples for CNNs, and what defenses such as adversarial training work against them?
- [DL03-209] What is shortcut learning in vision models, such as relying on backgrounds or textures, and how would you detect it?
- [DL03-210] How would you measure a vision model's robustness to corruptions and distribution shift, for example with ImageNet-C-style tests?
- [DL03-211] Why are vision classifiers often miscalibrated, and how do you calibrate them?

## Applied vision system design and deployment
- [DL03-212] How would you design a computer vision system for automatic license plate recognition?
- [DL03-213] What vision technologies does an autonomous vehicle perception stack use, and what neural network architecture would you choose for it?
- [DL03-214] How would you design a deep learning system for medical image diagnosis?
- [DL03-215] How would you design a real-time object detection system for video streams?
- [DL03-216] How would you build a product recognition and tracking system for retail stores?
- [DL03-217] How would you use CNNs to monitor and classify satellite imagery?
- [DL03-218] How do augmented reality applications use computer vision for tracking, mapping and scene understanding?
- [DL03-219] How would you design a visual search system that finds similar products from a user's photo?
- [DL03-220] How would you design a defect detection system for a factory line where defective samples are very rare?
- [DL03-221] How would you count people in dense crowd images, and why does detection-based counting break down there?
- [DL03-222] How do you export a vision model with ONNX or TensorRT, and what accuracy checks do you run after INT8 calibration?
- [DL03-223] Your detector must run at 30 FPS on an edge device. How do you budget latency across preprocessing, model and post-processing?

## CNN arithmetic and feature extraction
- [DL03-224] VGG-16 has about 138 million parameters. How much storage does it need in fp32, and in fp16?
- [DL03-225] Describe the VGG-19 architecture: the number of convolutional and fully connected layers, kernel sizes, pooling, input size and preprocessing.
- [DL03-226] Which layers of a pretrained CNN make the best fixed feature extractors, and why are the layers closest to the output not always the best choice?
- [DL03-227] How can you build an ensemble of fixed feature extractors from different layers or different pretrained CNNs?
- [DL03-228] What is the difference between convolution and cross-correlation, and which one do deep learning libraries actually compute?
- [DL03-229] How many multiplications does convolving a w×h image with a K×K kernel take, and how does a separable kernel such as a Gaussian reduce that cost?
- [DL03-230] Why do you L2-normalize CNN image embeddings before similarity search or face matching?
- [DL03-231] What output shapes does the VGG-11 feature extractor produce for 224×224, 512×512 and 704×1024 inputs, and why can it accept any input size?
- [DL03-232] For a 224×224×3 input, a 7×7 convolution with 32 filters and padding 2, followed by two 2×2 max-pools with stride 2, what is the output shape?
