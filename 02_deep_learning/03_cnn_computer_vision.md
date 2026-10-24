---
domain: dl
topic: cnn_computer_vision
title: CNNs and computer vision
tags: [cnn, computer-vision, detection, segmentation]
count: 119
---
# CNNs and computer vision

## CNN fundamentals
- [DL03-001] What is a convolutional neural network and how does it work?
- [DL03-002] Describe the architecture of a typical CNN and the role of each kind of layer in it.
- [DL03-003] Why are CNNs better suited to image tasks than fully connected networks applied to raw pixels?
- [DL03-004] What is the difference between a fully connected layer and a convolutional layer?
- [DL03-005] How does a CNN differ from a traditional neural network in computer vision?
- [DL03-006] What is a feature map in a CNN?
- [DL03-007] What do the filters in a CNN learn, and how do early-layer filters differ from deep-layer filters?
- [DL03-008] What is parameter sharing in a convolutional layer, and why does it matter?
- [DL03-009] How does convolution work on grayscale versus RGB inputs, and what determines the shape of the next layer?
- [DL03-010] What does the depth of a convolutional layer mean?
- [DL03-011] What role do fully connected layers play at the end of a classification CNN?
- [DL03-012] Can fully connected layers be replaced by convolutional layers, and what does that buy you at inference time?
- [DL03-013] Is it a good idea to use a CNN to classify one-dimensional signals such as audio or sensor data?
- [DL03-014] How do CNNs deal with overfitting?
- [DL03-015] How many learnable parameters does a conv layer with 3x3 kernels, 64 input channels and 128 output channels have?
- [DL03-016] Where does batch normalization go in a convolutional block, and what does it do for training?

## Convolution mechanics
- [DL03-017] What is padding in a CNN and why is it used?
- [DL03-018] What is stride, and how does it affect the output size of a convolution layer?
- [DL03-019] Given input size, kernel size, padding and stride, how do you compute the spatial output size of a convolution?
- [DL03-020] Explain the receptive field of a neuron in a CNN and how it grows with depth.
- [DL03-021] Why would you stack many small 3x3 kernels instead of using a few large kernels?
- [DL03-022] How do dilated convolutions differ from regular convolutions, and when are they useful?
- [DL03-023] What does a 1x1 convolution do, and why is it used in architectures like Inception and ResNet bottlenecks?
- [DL03-024] What is a depthwise separable convolution and what are its advantages?
- [DL03-025] How do the computation and parameter counts of a depthwise separable convolution compare to a standard convolution?
- [DL03-026] What is a transposed convolution, and why does it produce checkerboard artifacts?
- [DL03-027] How would you compute the FLOPs of a conv layer, and why can FLOPs be a poor predictor of real latency?

## Pooling and invariance
- [DL03-028] What is the purpose of pooling in a CNN, and what are the different types?
- [DL03-029] What is the difference between max pooling and average pooling, and when would you prefer each?
- [DL03-030] Why do classification CNNs use max-pooling?
- [DL03-031] What makes CNNs translation invariant, and how is that different from translation equivariance?
- [DL03-032] Are CNNs robust to rotations? What happens to a CNN's predictions if an image is rotated?
- [DL03-033] What is global average pooling and why has it replaced large fully connected heads in many architectures?
- [DL03-034] Can you replace pooling layers with strided convolutions, and what are the tradeoffs?
- [DL03-035] What is local response normalization, and why might it be used in a CNN?

## Classic architectures
- [DL03-036] What CNN architectures for image classification do you know?
- [DL03-037] What are the common pre-trained CNN models available in popular frameworks?
- [DL03-038] How did the VGG family simplify network design, and what are its main drawbacks?
- [DL03-039] What problem did Inception modules solve, and how do they use multiple filter sizes?
- [DL03-040] What is the significance of residual networks (ResNets)?
- [DL03-041] What are skip connections and residual blocks, and why do they make very deep networks trainable?
- [DL03-042] Why does accuracy degrade when you simply stack more layers in a plain CNN?
- [DL03-043] What is a bottleneck block in ResNet and why is it used?
- [DL03-044] What design ideas make MobileNet efficient for mobile devices?
- [DL03-045] What is compound scaling in EfficientNet and why is it better than scaling depth, width or resolution alone?
- [DL03-046] How would you choose a backbone for a latency-constrained deployment, and why do parameter count, FLOPs and latency disagree?

## Vision transformers and multimodal models
- [DL03-047] How can transformers be used for computer vision tasks and for tasks beyond NLP?
- [DL03-048] How does a Vision Transformer turn an image into a sequence of tokens?
- [DL03-049] What inductive biases do CNNs have that Vision Transformers lack, and what is the practical consequence?
- [DL03-050] Why do ViTs typically need more data or stronger regularization than CNNs to train well?
- [DL03-051] How does CLIP enable zero-shot image classification?
- [DL03-052] How do self-supervised methods like DINO, SimCLR or masked autoencoders learn visual features without labels?
- [DL03-053] When would a classic CNN classifier beat a vision-language model outright?
- [DL03-054] How would you automatically caption an image?

## Data augmentation and transfer learning
- [DL03-055] What are augmentations and why do we need them?
- [DL03-056] What kinds of image augmentations do you know?
- [DL03-057] How does data augmentation improve the performance of a vision model, and what techniques can be used?
- [DL03-058] Which augmentations would be harmful for a specific task, such as digit recognition or medical imaging, and why?
- [DL03-059] How do Mixup, CutMix and Cutout work, and why do they help generalization?
- [DL03-060] What is transfer learning and how is it used in practice?
- [DL03-061] What role do pre-trained models play in transfer learning?
- [DL03-062] What are feature extractors in the context of transfer learning?
- [DL03-063] How do you implement transfer learning for an image classification task?
- [DL03-064] In what situations is transfer learning recommended, and when is it not?
- [DL03-065] How do you decide how many layers to freeze when fine-tuning a pre-trained CNN?
- [DL03-066] Why use a smaller learning rate or discriminative learning rates when fine-tuning a pre-trained backbone?
- [DL03-067] How does domain shift between ImageNet and your target domain, such as medical or satellite images, affect fine-tuning?
- [DL03-068] Given only the CIFAR-10 dataset, how would you build a model that recognizes whether an image belongs to one of its 10 classes or not?

## Object detection
- [DL03-069] What is object detection, and how does it differ from image classification?
- [DL03-070] How do two-stage detectors such as Faster R-CNN compare to one-stage detectors such as YOLO or SSD in accuracy, speed and use cases?
- [DL03-071] How does the R-CNN family evolve from R-CNN to Fast R-CNN to Faster R-CNN?
- [DL03-072] What is a region proposal network and how does it work?
- [DL03-073] What are anchor boxes and how are they assigned to ground-truth objects during training?
- [DL03-074] What is non-maximum suppression and why is it needed in object detection?
- [DL03-075] How does the DETR model differ from anchor-based detectors?
- [DL03-076] Why is focal loss useful for one-stage detectors, and what problem does it solve?
- [DL03-077] How do feature pyramid networks help detect objects at different scales?
- [DL03-078] How would you improve a detector's performance on small objects?
- [DL03-079] What is intersection over union (IoU) and how is it used in training and evaluating detectors?
- [DL03-080] How would you evaluate an object detector using IoU and mean average precision?
- [DL03-081] Your detector has high mAP at IoU 0.5 but low mAP at 0.75. What does that tell you and how would you improve it?
- [DL03-082] How do 3D object detectors working on point clouds differ from 2D image detectors, and why are they computationally heavy?
- [DL03-083] How would you design the neural network architecture for multi-camera 3D object detection without lidar?
- [DL03-084] Why might a self-driving system use lidar, radar and cameras together rather than cameras alone, and where would you fuse them?
- [DL03-085] How do Google and Apple Maps blur license plates and faces?

## Segmentation
- [DL03-086] What is image segmentation, and what are its applications?
- [DL03-087] What is the difference between semantic segmentation and instance segmentation?
- [DL03-088] What segmentation architectures do you know?
- [DL03-089] Why do segmentation CNNs typically have an encoder-decoder structure?
- [DL03-090] How does U-Net use skip connections, and why are they important for localization?
- [DL03-091] How does Mask R-CNN extend Faster R-CNN, and what does RoIAlign fix compared to RoIPool?
- [DL03-092] How do fully convolutional networks make dense per-pixel predictions from arbitrary-sized input?
- [DL03-093] Why is plain pixel-wise cross-entropy a poor loss for heavily imbalanced segmentation masks, and what are alternatives such as Dice loss?
- [DL03-094] How do you evaluate a segmentation model with IoU, mean IoU and Dice coefficient?

## Classical vision, OCR and video
- [DL03-095] What is computer vision, and how does it relate to human vision?
- [DL03-096] What is the difference between image processing and computer vision?
- [DL03-097] What are the common image preprocessing steps in a computer vision pipeline?
- [DL03-098] How does image resizing affect model performance?
- [DL03-099] What techniques can reduce noise in an image?
- [DL03-100] How does edge detection work in image analysis, for example with Sobel or Canny?
- [DL03-101] What are color spaces and why do they matter in image processing?
- [DL03-102] What is feature extraction in computer vision?
- [DL03-103] What are feature descriptors, and why are they important in computer vision?
- [DL03-104] Explain the SIFT algorithm and the invariances it provides.
- [DL03-105] How would you remove outliers when estimating a flat plane from noisy samples?
- [DL03-106] How does image registration work, and how do sparse and dense optical flow compare?
- [DL03-107] What is OCR and what are its main applications?
- [DL03-108] How would you build a modern OCR pipeline that handles text detection and text recognition?
- [DL03-109] How does multi-object tracking work with Kalman filters or deep association methods like DeepSORT?
- [DL03-110] What are the challenges in real-time object tracking?
- [DL03-111] How would you preprocess video for a model, including frame sampling, resizing and normalization?

## Applied design and debugging
- [DL03-112] What are the steps to build an image recognition system?
- [DL03-113] Describe how you would implement an image classification system end to end.
- [DL03-114] How would you create a model to recognize whether an image is a triangle, a circle or a square?
- [DL03-115] What makes object recognition hard under varied lighting, viewpoints and orientations?
- [DL03-116] Your image classifier achieves 99% on validation but fails in production. What are the likely causes and how would you debug it?
- [DL03-117] How would you handle a severely class-imbalanced image classification dataset?
- [DL03-118] How would you build a vision model with very few labeled images?
- [DL03-119] How would you quantize, prune or distill a CNN for deployment on an edge device, and what accuracy risks do you watch for?
