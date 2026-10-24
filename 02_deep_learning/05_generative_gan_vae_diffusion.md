---
domain: dl
topic: generative_gan_vae_diffusion
title: Generative models: GAN, VAE, diffusion
tags: [gan, vae, diffusion, generative]
count: 143
---
# Generative models: GAN, VAE, diffusion

## Autoencoder fundamentals
- [DL05-001] What is an autoencoder, and what does it "auto-encode"?
- [DL05-002] Explain the architecture of a basic autoencoder, including the roles of the encoder, the bottleneck and the decoder.
- [DL05-003] What is the latent space of an autoencoder, and how does the size of the bottleneck layer affect what is learned?
- [DL05-004] What are some key practical applications of autoencoders?
- [DL05-005] Why is an autoencoder trained with a reconstruction objective considered unsupervised learning?
- [DL05-006] How can autoencoders be used for unsupervised representation learning?
- [DL05-007] Which loss functions are used to train autoencoders, and when would you choose each?
- [DL05-008] What were autoencoders traditionally used for, and why has there been a resurgence of interest in them for generative modeling?
- [DL05-009] What is an undercomplete autoencoder, and what is it typically used for?
- [DL05-010] What problems might a nonlinear undercomplete autoencoder face?
- [DL05-011] How would you use an autoencoder for anomaly detection, and how would you set the decision threshold?
- [DL05-012] An autoencoder reaches near-zero reconstruction loss, yet its latent codes perform poorly on downstream tasks. What could have gone wrong?
- [DL05-013] Compare the reconstruction quality of a deep autoencoder with that of PCA at the same code size.
- [DL05-014] What is a linear autoencoder? Can it achieve the lowest training reconstruction error, and under what conditions?
- [DL05-015] How does a linear autoencoder with MSE loss relate to PCA, and why does the learned basis not have to be orthogonal?

## Regularized and structured autoencoders
- [DL05-016] What is a sparse autoencoder, and how is sparsity enforced on the hidden representation?
- [DL05-017] What is a denoising autoencoder? How does it work, what are its advantages, and how does it prevent trivially learning the identity function?
- [DL05-018] How does the choice of corruption process (Gaussian noise, masking, dropout) in a denoising autoencoder affect the learned features?
- [DL05-019] What is a contractive autoencoder, and what benefits does it offer?
- [DL05-020] Why is a contractive autoencoder called "contractive"?
- [DL05-021] Discuss the role of regularization in training autoencoders.
- [DL05-022] What is the difference between a stacked autoencoder and a deep autoencoder? Compare and contrast.
- [DL05-023] What are convolutional autoencoders, and in what cases are they preferred over fully connected ones?
- [DL05-024] How do recurrent autoencoders differ from feedforward autoencoders, and when might they be useful?
- [DL05-025] Compare an L1 activity penalty, a KL-divergence sparsity penalty and a k-sparse (top-k) constraint for sparse autoencoders.
- [DL05-026] What are overcomplete autoencoders and what problems might they face? Does the answer change for linear overcomplete autoencoders?
- [DL05-027] What are the practical issues with contractive autoencoders, and how can they be tackled?
- [DL05-028] What is manifold learning, and how are denoising and contractive autoencoders equipped to do it?
- [DL05-029] What is score matching, and how does it connect to denoising autoencoders?
- [DL05-030] Are there any connections between autoencoders and restricted Boltzmann machines?
- [DL05-031] Sparse autoencoders are used to interpret LLM activations. Why use an overcomplete sparse dictionary, and what failure modes such as dead features or feature splitting arise?

## Variational autoencoders
- [DL05-032] What is a variational autoencoder, and how does it differ from a traditional autoencoder?
- [DL05-033] How do you generate new samples from a trained VAE, and what does interpolating in its latent space show?
- [DL05-034] How does a VAE impose a probabilistic structure on the latent space, and why is that important?
- [DL05-035] Write down the VAE training objective (ELBO) and explain the reconstruction term and the KL term.
- [DL05-036] What is the reparameterization trick, and why is it needed to train a VAE?
- [DL05-037] Why do VAEs tend to produce blurrier samples than GANs?
- [DL05-038] Why is a standard normal prior typically used, and what happens if the aggregate posterior does not match it?
- [DL05-039] What does beta control in a beta-VAE, and how does it trade reconstruction quality against disentanglement?
- [DL05-040] How does a conditional VAE work, and how would you use it to control what is generated?
- [DL05-041] What is KL annealing, and when do you need it?
- [DL05-042] Why do generative autoencoders such as VAEs not require additional regularization the way ordinary autoencoders do?
- [DL05-043] What is posterior collapse in VAEs, why does it happen with powerful decoders, and how can you mitigate it?
- [DL05-044] Why is the ELBO a lower bound on the log likelihood, and what does the gap between them represent?
- [DL05-045] What is a VQ-VAE, how does it differ from a Gaussian VAE, and what causes codebook collapse?

## GAN fundamentals and training
- [DL05-046] What are Generative Adversarial Networks?
- [DL05-047] Describe the architecture of a basic GAN and the roles of the generator and the discriminator.
- [DL05-048] How do GANs generate new, unseen data without ever modeling the data density explicitly?
- [DL05-049] Write the GAN minimax objective. What divergence does it minimize when the discriminator is optimal?
- [DL05-050] What loss functions are commonly used in GANs, and why?
- [DL05-051] Why is the non-saturating generator loss used instead of the original minimax loss?
- [DL05-052] How does the training process differ for the generator and the discriminator, and why are they updated alternately?
- [DL05-053] What is mode collapse in GANs, why is it problematic, and how can it be mitigated?
- [DL05-054] What makes GANs hard to train, and which practical techniques help stabilize training?
- [DL05-055] How can we evaluate the performance and quality of a GAN?
- [DL05-056] Why are GAN training losses often uninformative about sample quality, and how do you tell whether training is going well?
- [DL05-057] What happens to the generator's gradients if the discriminator becomes too strong too early?
- [DL05-058] Can you describe the concept of Nash equilibrium in the context of GANs, and why gradient descent may fail to converge to it?
- [DL05-059] What do spectral normalization, gradient penalties and the two time-scale update rule each do to stabilize GAN training?
- [DL05-060] A GAN discriminator memorizes the training set when data is scarce. What techniques reduce this overfitting?

## GAN variants and applications
- [DL05-061] Explain the idea behind Conditional GANs (cGANs) and their uses.
- [DL05-062] What are Deep Convolutional GANs (DCGANs), and how do they differ from basic GANs?
- [DL05-063] Describe CycleGAN and its application to image-to-image translation. What is the cycle-consistency loss?
- [DL05-064] How are GANs used for image synthesis and image-to-image translation tasks?
- [DL05-065] How are GANs used for super-resolution (SRGAN), and why is a perceptual or adversarial loss used instead of pixel-wise MSE?
- [DL05-066] When would you use pix2pix instead of CycleGAN?
- [DL05-067] What is the truncation trick in BigGAN-style models, and what does it trade off?
- [DL05-068] Can you discuss the architecture and benefits of Wasserstein GANs (WGANs)?
- [DL05-069] How do WGAN-GP and weight clipping differ, and why is a gradient penalty preferred?
- [DL05-070] What architectural ideas made StyleGAN's latent space more controllable, and what is style mixing?
- [DL05-071] Why did diffusion models largely overtake GANs for image generation, and where do GANs still win?

## Normalizing flows and evaluating generative models
- [DL05-072] What is a normalizing flow, and how does it differ from VAEs and GANs?
- [DL05-073] What does the change-of-variables formula do in a normalizing flow, and why must the transformations be invertible with tractable Jacobians?
- [DL05-074] How do coupling layers, such as RealNVP, keep the Jacobian determinant cheap to compute?
- [DL05-075] Compare GANs, VAEs, normalizing flows and diffusion models on sample quality, likelihood evaluation, sampling speed and mode coverage.
- [DL05-076] How do VAEs, flows and diffusion models each give (or approximate) a likelihood, and why is bits per dimension not comparable across all of them?
- [DL05-077] What is the Frechet Inception Distance (FID), and how is it computed?
- [DL05-078] What does Inception Score measure, and why is FID generally preferred?
- [DL05-079] What are the limitations of FID, such as sample-size bias and sensitivity to the feature extractor?
- [DL05-080] How do precision and recall metrics for generative models capture fidelity versus diversity?
- [DL05-081] How would you evaluate text-to-image alignment, for example with CLIP score, and what are its weaknesses?
- [DL05-082] When is human evaluation necessary for generative models, and how would you design it?
- [DL05-083] A model improves its FID but human raters prefer the old model. What could explain this, and how would you investigate?

## Diffusion models and latent diffusion
- [DL05-084] Give the intuition for how diffusion models generate images, and how image generation works in systems like Stable Diffusion, DALL-E or Flux.
- [DL05-085] Describe the forward and reverse processes of a DDPM. Why does the forward process admit a closed-form sample at any timestep?
- [DL05-086] What is a diffusion network trained to predict (noise, clean image, velocity), and does the choice matter?
- [DL05-087] Why can diffusion samplers skip most of the 1000 training steps?
- [DL05-088] What does the noise schedule in a diffusion model trade off?
- [DL05-089] What training loss is used in a DDPM, and why is the simplified noise-prediction loss a reasonable choice?
- [DL05-090] How do DDPM and DDIM sampling differ, and what does determinism buy you?
- [DL05-091] Why do diffusion models add Gaussian noise rather than another kind of corruption?
- [DL05-092] How do the score-based (SDE) and DDPM views of diffusion relate to each other?
- [DL05-093] Why does a diffusion model need a timestep embedding, and how is it injected into the network?
- [DL05-094] Why do many default noise schedules leak information at the final step, and what do zero-terminal-SNR and v-prediction fix?
- [DL05-095] Why does the optimal noise schedule change with image resolution?
- [DL05-096] Why do latent diffusion instead of pixel-space diffusion? Walk through the components of a Stable-Diffusion-style system.
- [DL05-097] How does a text prompt condition the denoiser in Stable Diffusion, and what is the role of cross-attention?
- [DL05-098] What does moving from a U-Net to a Diffusion Transformer (DiT) buy in a diffusion model?
- [DL05-099] Explain latent diffusion, diffusion transformers and classifier-free guidance at a high level.
- [DL05-100] What can go wrong with the autoencoder in latent diffusion, such as fine detail or text artifacts, and how does it cap overall quality?
- [DL05-101] Why use 4 (or 16) latent channels in latent diffusion rather than compressing harder?
- [DL05-102] Where does ControlNet-style conditioning hook into a latent diffusion architecture?
- [DL05-103] How would you choose the text encoder (CLIP, T5, an LLM) for a text-to-image model, and what does each change?

## Guidance, conditioning and control
- [DL05-104] What is classifier-free guidance?
- [DL05-105] Explain classifier-free guidance. What actually happens when you turn the guidance scale up?
- [DL05-106] How is a model trained so that classifier-free guidance can be used at inference, and what does it cost at sampling time?
- [DL05-107] How does classifier guidance differ from classifier-free guidance?
- [DL05-108] How do negative prompts work mechanically in diffusion models?
- [DL05-109] Your diffusion model generates sharp but repetitive images. How do you balance quality against diversity?
- [DL05-110] What are the differences between ControlNet, IP-Adapter and LoRA for steering a pretrained diffusion model?
- [DL05-111] How would you fine-tune a diffusion model on a new concept or style with few images, for example with DreamBooth or LoRA, and what risks arise?
- [DL05-112] Why does high classifier-free guidance hurt diversity specifically?
- [DL05-113] Your diffusion model ignores precise control requirements in text prompts. How do you improve controllability?
- [DL05-114] High guidance scales produce oversaturated, burnt-looking images. Why, and what fixes exist such as dynamic thresholding or guidance rescaling?
- [DL05-115] Why do guidance-distilled diffusion models generate at a CFG of about 1?
- [DL05-116] An open-source image model has been post-trained so a user's character stays recognisable across art styles. How would you build and evaluate that identity consistency?
- [DL05-117] How would you detect the copy-through failure of an identity-preserving image model in production without a human reviewing every image?

## Fast sampling and flow matching
- [DL05-118] Your diffusion model takes too long per image. How do you speed up sampling?
- [DL05-119] What are higher-order ODE solvers such as DPM-Solver, and why do they need far fewer steps than ancestral sampling?
- [DL05-120] What is the difference between ancestral (stochastic) sampling and deterministic ODE sampling in diffusion models?
- [DL05-121] What is flow matching or rectified flow, and how does it reduce the number of sampling steps?
- [DL05-122] What is consistency modeling or distillation for diffusion, and how does it enable one-to-four-step generation?
- [DL05-123] Compare DDPM and flow matching: what are their sampling efficiency, advantages and disadvantages?
- [DL05-124] Compare progressive distillation, latent consistency models and adversarial distillation in terms of quality and diversity lost.
- [DL05-125] If you needed 100 ms image generation for a live preview feature, which model family would you pick and which tricks would you apply?
- [DL05-126] How does rectified flow's straight-path objective differ from the DDPM objective, and why do straighter trajectories help few-step sampling?
- [DL05-127] What is the quality-versus-step-count tradeoff curve for distilled diffusion models, and where do artifacts show up first?

## Autoregressive models, video and applied scenarios
- [DL05-128] Diffusion versus autoregressive generation: how do they differ, and when is each used for image, video, audio and text?
- [DL05-129] Compare diffusion and autoregressive approaches to image generation. Why did autoregressive approaches come back?
- [DL05-130] How does a VQGAN-style tokenizer enable autoregressive image generation, and what limits its fidelity?
- [DL05-131] What is masked generative modeling (MaskGIT-style), and how does it sit between autoregressive and diffusion approaches?
- [DL05-132] What is text-to-video generation, and what are the current state-of-the-art approaches?
- [DL05-133] How do text-to-image models risk memorizing training images, and how would you measure and reduce it?
- [DL05-134] How would you detect or watermark AI-generated images at scale, and what are the limits of each approach?
- [DL05-135] Why does diffusion work better than autoregression for images?
- [DL05-136] Why do omni-models with autoregressive image heads render text inside images so much better?
- [DL05-137] What does the discrete tokenizer bottleneck in autoregressive image generation depend on?
- [DL05-138] How do Diffusion Language Models work, and what are their trade-offs compared with autoregressive LLMs?
- [DL05-139] How do text-to-video models like Veo or Sora work, and why is video generation so much more expensive than image generation?
- [DL05-140] Why does a causal 3D VAE make joint image and video training possible?
- [DL05-141] You must cut video generation cost 10x for a preview feature. Which levers do you pull first, and what quality do you lose?
- [DL05-142] How would you measure temporal consistency in generated video, and what are the weaknesses of metrics such as FVD?
- [DL05-143] What changes in an identity-preserving image model if creators want their character's identity locked so other users cannot restyle it?
