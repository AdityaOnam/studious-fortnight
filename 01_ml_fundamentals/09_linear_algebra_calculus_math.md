---
domain: ml
topic: linear_algebra_calculus_math
title: Linear algebra, calculus and math for ML
tags: [math, linear-algebra, calculus, information-theory]
count: 154
---
# Linear algebra, calculus and math for ML

## Vectors, matrices and tensors
- [ML09-001] What are scalars, vectors, matrices and tensors, and how does each show up in a machine learning pipeline?
- [ML09-002] How do matrix addition and subtraction work, and what shape constraints apply?
- [ML09-003] What are the key properties of matrix multiplication (associativity, distributivity, commutativity), and which of them fail in general?
- [ML09-004] Define the transpose of a matrix and state how it interacts with products and inverses, i.e. (AB)^T and (AB)^-1.
- [ML09-005] What is the Hadamard (element-wise) product of two matrices, and how does it differ from the ordinary matrix product?
- [ML09-006] What is broadcasting, and what rules decide whether two arrays of different shapes can be combined?
- [ML09-007] What is a symmetric matrix? Give two places where symmetric matrices appear in ML.
- [ML09-008] What is a diagonal matrix, and why is multiplying by one computationally cheap?
- [ML09-009] How does multiplication by a diagonal matrix differ for a square versus a non-square diagonal matrix?
- [ML09-010] What is the difference between an affine transformation and a linear transformation?
- [ML09-011] Why is a fully connected layer without a nonlinearity just an affine map, and what happens if you stack several of them?
- [ML09-012] Interpret a matrix as a linear map: what do the columns of A tell you about where the basis vectors go?
- [ML09-013] How would you compute a batch of pairwise dot products between two sets of vectors using one matrix multiplication? Give the shapes involved.
- [ML09-014] Matrix multiplication of an (m x n) by an (n x p) matrix costs how many floating-point operations, and why does the order of multiplying a chain of matrices matter?
- [ML09-015] What is the outer product of two vectors, and what is the rank of the resulting matrix?

## Inner products, orthogonality and norms
- [ML09-016] What is the dot product of two vectors, and why is it significant in machine learning?
- [ML09-017] How is the dot product related to the angle between two vectors, and how does that lead to cosine similarity?
- [ML09-018] What is the cross product of two vectors, and when is it used?
- [ML09-019] What is a unit vector, and how do you normalize an arbitrary vector?
- [ML09-020] When are two vectors orthogonal, and when are they orthonormal?
- [ML09-021] In R^n, what is the maximum number of mutually orthogonal vectors with non-zero norm?
- [ML09-022] What is an orthogonal matrix? List its key properties and explain why it is computationally preferred.
- [ML09-023] What is a norm, and what are the L1, L2 and L-infinity norms of a vector?
- [ML09-024] What conditions must a function satisfy to be a norm?
- [ML09-025] Why is the squared L2 norm often preferred over the plain L2 norm in ML objectives?
- [ML09-026] When is the L1 norm preferred over the L2 norm, and what geometric picture explains sparsity?
- [ML09-027] Can the number of non-zero entries in a vector be called the L0 norm? If not, why?
- [ML09-028] What is the Frobenius norm of a matrix?
- [ML09-029] What is the spectral (operator 2-) norm of a matrix, and how does it relate to the Frobenius norm?
- [ML09-030] Why is the spectral norm of a weight matrix relevant to Lipschitz bounds of a neural network?
- [ML09-031] How does spectral normalization of weights work, and why is it used to stabilize GAN training?
- [ML09-032] State the Cauchy-Schwarz inequality and give one use of it in an ML proof.
- [ML09-033] What is the Mahalanobis distance, and how does it differ from Euclidean distance?
- [ML09-034] Why does Euclidean distance become less informative in very high dimensions, and how does the concentration of norms explain this?

## Linear systems, rank and inverses
- [ML09-035] What is the determinant of a square matrix, and what information does it provide?
- [ML09-036] How is the determinant computed (for example by Laplace expansion), and how is it related to the eigenvalues?
- [ML09-037] What does a determinant of zero mean geometrically and for invertibility?
- [ML09-038] What is an inverse matrix, and how do you compute it when it exists?
- [ML09-039] When does the inverse of a square matrix A exist?
- [ML09-040] Define span, linear independence and basis.
- [ML09-041] What is the rank of a matrix, and how is it related to the column space and null space?
- [ML09-042] State the rank-nullity theorem and explain what it says about the solutions of Ax = 0.
- [ML09-043] For Ax = b, when does a unique solution exist?
- [ML09-044] For Ax = b, what happens when A is fat (underdetermined) versus tall (overdetermined)?
- [ML09-045] Derive the normal equations for ordinary least squares, and say when X^T X is not invertible.
- [ML09-046] Why is explicitly computing the inverse of a matrix to solve Ax = b discouraged in practice? What do you use instead?
- [ML09-047] How does ridge regression make X^T X + lambda I invertible, and what does lambda do to its eigenvalues?
- [ML09-048] How does multicollinearity show up in the linear algebra of a design matrix?
- [ML09-049] What is a low-rank approximation of a matrix, and why is the best rank-k approximation under the Frobenius norm given by truncated SVD?
- [ML09-050] What are LU, QR and Cholesky decompositions, and when would you choose each one to solve a linear system?
- [ML09-051] What is the rank of an outer-product-based update such as the LoRA update BA, and why does that bound make fine-tuning cheap?

## Eigendecomposition and definiteness
- [ML09-052] What are eigenvalues and eigenvectors, and what do they mean geometrically?
- [ML09-053] How do you find the eigenvalues and eigenvectors of a matrix?
- [ML09-054] Write the eigendecomposition of a matrix. How does it change if the matrix is real symmetric?
- [ML09-055] Is the eigendecomposition unique? If not, how do we represent it?
- [ML09-056] Which matrices can be decomposed by eigendecomposition?
- [ML09-057] State the spectral theorem for real symmetric matrices and why it matters for covariance matrices.
- [ML09-058] What are positive definite, negative definite, positive semi-definite and negative semi-definite matrices?
- [ML09-059] Why is every covariance matrix positive semi-definite?
- [ML09-060] How do you test whether a symmetric matrix is positive definite (eigenvalues, Cholesky, leading minors)?
- [ML09-061] What is the trace of a matrix, and how is it related to the eigenvalues?
- [ML09-062] Express the Frobenius norm of a matrix in terms of the trace.
- [ML09-063] Why is the trace of a product of matrices invariant under cyclic permutations?
- [ML09-064] What is the importance of the trace of the covariance matrix in PCA?
- [ML09-065] How do the eigenvalues of A^k and of A^-1 relate to those of A, and why does this matter for the stability of a recurrent network?
- [ML09-066] How does the largest eigenvalue of the recurrent weight matrix relate to exploding and vanishing gradients in RNNs?
- [ML09-067] What is the power iteration method, and how does it find the dominant eigenvector?
- [ML09-068] How is the PageRank vector related to an eigenvector of the transition matrix?
- [ML09-069] What is the matrix exponential or a low-order polynomial of a matrix, and how does eigendecomposition make computing it easy?
- [ML09-070] When is a matrix diagonalizable, and what happens for a defective matrix such as a Jordan block?

## SVD and pseudo-inverse
- [ML09-071] What is the SVD, and why do we use it rather than just eigendecomposition?
- [ML09-072] What are singular values, left singular vectors and right singular vectors?
- [ML09-073] Given a matrix A, how would you calculate its SVD?
- [ML09-074] Which matrices can be decomposed by SVD?
- [ML09-075] Why are singular values always non-negative?
- [ML09-076] What is the relationship between the SVD and eigendecomposition?
- [ML09-077] What is the relationship between PCA and SVD? Which is numerically preferred and why?
- [ML09-078] What is the Moore-Penrose pseudo-inverse and how do you compute it from the SVD?
- [ML09-079] Which solution does the pseudo-inverse give for Ax = b when A is fat, and which when A is tall?
- [ML09-080] State the Eckart-Young theorem and explain how it justifies truncated SVD for compression.
- [ML09-081] Explain the SVD and give two places it shows up in modern deep learning.
- [ML09-082] What does a full SVD of a 4096x4096 matrix cost, and what would you use if you only need the top 10 singular vectors?
- [ML09-083] How does truncated SVD relate to latent semantic analysis and to matrix-factorization recommenders?
- [ML09-084] How does the singular value spectrum of a matrix tell you its numerical rank and how compressible it is?
- [ML09-085] How does the SVD of a weight update motivate low-rank adaptation methods such as LoRA?
- [ML09-086] How does SVD whitening differ from PCA whitening, and when is each useful?

## Numerical stability and conditioning
- [ML09-087] What are underflow and overflow in floating-point arithmetic?
- [ML09-088] How do you avoid overflow and underflow in the softmax and log-softmax functions?
- [ML09-089] Explain the log-sum-exp trick and derive why subtracting the maximum leaves the result unchanged.
- [ML09-090] What is the condition number of a matrix?
- [ML09-091] What is poor conditioning, and what are its practical consequences when solving linear systems?
- [ML09-092] How is the condition number of a symmetric matrix related to its eigenvalues, and to its singular values in general?
- [ML09-093] Why does squaring the condition number when forming X^T X make the normal equations numerically risky, and how do QR or SVD help?
- [ML09-094] How does the condition number of the Hessian affect the convergence rate of gradient descent?
- [ML09-095] Why do deep learning systems use bfloat16 or mixed precision, and what numerical issues does loss scaling address?
- [ML09-096] Why is adding a small epsilon (for example in layer norm or Adam) needed, and how does its size affect numerical behaviour?
- [ML09-097] Why is computing a log-determinant via a Cholesky factor preferable to taking the log of the determinant directly?

## Calculus and matrix calculus
- [ML09-098] Write the logistic (sigmoid) and softplus functions and their derivatives, and explain how they are related.
- [ML09-099] What are the gradient, divergence and curl, and which of them appears in machine learning?
- [ML09-100] What is the gradient of a scalar function, and why does it point in the direction of steepest ascent?
- [ML09-101] What is the chain rule, and how does it underlie backpropagation?
- [ML09-102] What is a directional derivative, and how is it related to the gradient?
- [ML09-103] What is a Jacobian matrix?
- [ML09-104] What is a Hessian matrix?
- [ML09-105] What are critical or stationary points in multiple dimensions, and how are they classified?
- [ML09-106] How do the eigenvalues of the Hessian distinguish a local minimum, a local maximum and a saddle point?
- [ML09-107] Why are saddle points considered a bigger obstacle than local minima in high-dimensional neural network loss surfaces?
- [ML09-108] Derive the gradient of the mean squared error with respect to the weights in linear regression, in matrix form.
- [ML09-109] Derive the gradient of the binary cross-entropy loss with a sigmoid output with respect to the logit.
- [ML09-110] Derive the gradient of cross-entropy loss with softmax inputs, and explain why the two are fused numerically.
- [ML09-111] What is the Jacobian of the softmax function, and what structural property does it have?
- [ML09-112] What is the gradient of x^T A x with respect to x, and how does it simplify when A is symmetric?
- [ML09-113] In reverse-mode automatic differentiation, why is the vector-Jacobian product used rather than materializing the full Jacobian?
- [ML09-114] Why is reverse-mode differentiation efficient for functions with many inputs and one output, and when would forward mode win?
- [ML09-115] What is the Hessian-vector product, and how can it be computed without forming the Hessian?
- [ML09-116] A layer maps R^n to R^m. How large is its Jacobian, and what are the memory implications for per-example gradients?
- [ML09-117] Why do the gradients of a deep network explode or vanish? Express this as a product of Jacobians.
- [ML09-118] State Taylor's theorem for a multivariate function up to second order, and say how it motivates gradient descent and Newton's method.
- [ML09-119] What is the change-of-variables formula for densities, and why does a normalizing flow need the Jacobian determinant?

## Information theory
- [ML09-120] Define self-information. What are its units?
- [ML09-121] What are Shannon entropy and differential entropy, and how do they differ?
- [ML09-122] Which distribution over a discrete set of K outcomes maximizes entropy, and why?
- [ML09-123] Explain Kullback-Leibler divergence intuitively and give its formula.
- [ML09-124] Can KL divergence be used as a distance measure? Which properties does it lack?
- [ML09-125] Compute the KL divergence between two univariate Gaussians. What does it reduce to when the variances are equal?
- [ML09-126] What is mutual information, and how is it related to KL divergence and entropy?
- [ML09-127] Define cross-entropy, and explain how it decomposes into entropy plus KL divergence.
- [ML09-128] How are cross-entropy, KL divergence and perplexity related, and why is cross-entropy the training loss for language models?
- [ML09-129] Why does maximum likelihood estimation minimize KL(p||q) rather than KL(q||p), and how do the two differ in behaviour (mode-covering versus mode-seeking)?
- [ML09-130] How is the KL divergence loss different from cross-entropy loss, and from contrastive loss?
- [ML09-131] Why is KL divergence non-negative? Sketch the proof using Jensen's inequality.
- [ML09-132] What is the Jensen-Shannon divergence, and why is it preferable to KL when supports do not overlap?
- [ML09-133] Where does a KL term appear in a VAE objective, and what does it regularize?
- [ML09-134] Why do we use KL(pi_old || pi_new) as a trust-region constraint in policy optimization, and what does it measure?
- [ML09-135] What is the information bottleneck principle, and how is mutual information used in it?
- [ML09-136] What is the Fisher information matrix, and how is it related to the Hessian of the KL divergence?
- [ML09-137] Why is the Wasserstein distance sometimes preferred over KL or JS divergence for training generative models?

## Optimization math
- [ML09-138] What is a convex function, and why does convexity make optimization easier?
- [ML09-139] How do you check whether a twice-differentiable function is convex, using the Hessian?
- [ML09-140] Write the gradient descent update rule and explain the role of the learning rate.
- [ML09-141] For a quadratic loss, how does the choice of step size relate to the largest eigenvalue of the Hessian, and what happens if it is too large?
- [ML09-142] Derive the Newton update and explain why it is rarely used directly in large-scale deep learning.
- [ML09-143] What are quasi-Newton methods like BFGS and L-BFGS, and what problem do they solve?
- [ML09-144] How does the Lagrange multiplier method solve a constrained optimization problem? Give a worked ML example.
- [ML09-145] What are the KKT conditions, and where do they appear in SVMs?
- [ML09-146] Why does L1 regularization yield sparse solutions while L2 does not? Answer using the geometry or the subgradient.
- [ML09-147] What is a subgradient, and how is it used to optimize non-differentiable functions like the hinge loss or ReLU?
- [ML09-148] What is Lipschitz continuity of the gradient (L-smoothness), and how does it set a safe step size?
- [ML09-149] What is strong convexity, and how does it change the convergence rate of gradient descent from sublinear to linear?
- [ML09-150] Why does momentum accelerate gradient descent on ill-conditioned quadratics? Describe it in terms of Hessian eigenvalues.
- [ML09-151] How does Adam's per-parameter scaling relate to a diagonal approximation of preconditioning by the Hessian or Fisher matrix?
- [ML09-152] What is natural gradient descent, and how does it differ from ordinary gradient descent?
- [ML09-153] Why is the loss landscape of a neural network non-convex, and why does gradient descent still work well in practice?
- [ML09-154] What is duality in optimization, and what does the dual of an SVM buy you?
