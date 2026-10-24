---
domain: mlsd
topic: mlops_deployment_monitoring
title: MLOps, deployment and monitoring
tags: [mlops, deployment, monitoring, drift]
count: 148
---
# MLOps, deployment and monitoring

## MLOps fundamentals and lifecycle
- [MS01-001] What is MLOps, and how does it differ from traditional DevOps?
- [MS01-002] What are the main benefits of adopting MLOps practices in a machine learning project?
- [MS01-003] Describe the typical stages of the ML lifecycle, from problem framing and data collection through deployment and monitoring.
- [MS01-004] Why should you build a simple baseline model before a complex one, and how does it fit into the ML lifecycle?
- [MS01-005] What are the three levels of MLOps maturity (manual, ML pipeline automation, CI/CD pipeline automation), and what distinguishes them?
- [MS01-006] What are the key components of a robust MLOps infrastructure?
- [MS01-007] What are the common challenges in deploying ML models, and how does MLOps address them?
- [MS01-008] What makes an ML system harder to test, debug and maintain than a conventional software service?
- [MS01-009] What has to change before notebook or monolithic experiment code can run in production, and how would you restructure it?
- [MS01-010] How does LLMOps differ from classic MLOps in artifacts, evaluation, cost and release management?

## Reproducibility and experiment tracking
- [MS01-011] Why is experiment tracking important, and what does it let a team do?
- [MS01-012] What is the difference between an experiment tracker, an artifact store and a model registry?
- [MS01-013] What should a training run log so that it can be compared, audited and reproduced later?
- [MS01-014] How does MLOps facilitate reproducibility in machine learning projects?
- [MS01-015] What practices would you use to improve experiment reproducibility across a team?
- [MS01-016] What makes environment reproducibility hard for ML, and how do you address it?
- [MS01-017] Which sources of non-determinism (seeds, data loader order, GPU kernels, distributed reductions) prevent bit-exact reproducibility, and how do you control them?
- [MS01-018] How do you version large datasets and tie a dataset snapshot to a specific model version?
- [MS01-019] How do you version datasets, prompts, models and LLM judges so that an old result can be reproduced?
- [MS01-020] What is data and model lineage, and why does it matter for debugging and audits?
- [MS01-021] You cannot reproduce a model that was trained six months ago. What was most likely not captured?
- [MS01-022] How would you use MLflow Tracking to compare runs, and what do you store as params, metrics and artifacts?
- [MS01-023] How do you organise tracking for hundreds of concurrent hyperparameter-sweep runs without overwhelming the tracking backend or the team?

## Containers, infrastructure and tooling
- [MS01-024] What tools and platforms are commonly used to implement MLOps, and how do they fit together?
- [MS01-025] What role does cloud computing play in MLOps?
- [MS01-026] How do containerization technologies like Docker contribute to MLOps practices?
- [MS01-027] How do you keep Docker images for GPU ML workloads small, reproducible and secure?
- [MS01-028] How does infrastructure as code support machine learning operations?
- [MS01-029] What considerations matter when choosing compute resources for training machine learning models?
- [MS01-030] What problem does Kubeflow solve compared with running training jobs on Kubernetes by hand?
- [MS01-031] When would you choose MLflow, Kubeflow, or a managed platform such as SageMaker or Vertex AI, and what are the build-versus-buy tradeoffs?
- [MS01-032] How do you schedule GPU workloads on Kubernetes (device plugins, node pools, requests and limits, bin-packing)?
- [MS01-033] When do you use spot GPUs, and how do you run workloads on them without getting burned?
- [MS01-034] How would you design a scalable machine learning infrastructure?
- [MS01-035] How do you handle a multi-node training job running on spot capacity?
- [MS01-036] Five teams share a 64-GPU cluster. One team requests 16 GPUs for a deadline and uses 3. What does the system do about it?
- [MS01-037] How do you decide between one reserved H100 node and three spot A100 nodes for the same budget?
- [MS01-038] Spot capacity for your GPU type dries up region-wide for a day. What happens to your training queue?

## CI/CD, pipelines and model registry
- [MS01-039] What is a model registry, and what role does it play in MLOps?
- [MS01-040] What are the three things you need to test in an ML project (code, data, model), and how do the tests differ?
- [MS01-041] Explain continuous integration and continuous delivery in the context of machine learning, and how you would implement them for models.
- [MS01-042] What is the difference between CI, CD and continuous training (CT) in an ML system?
- [MS01-043] How does the Pipelines design pattern help structure ML workflows?
- [MS01-044] What would trigger a training pipeline: a schedule, new data, a drift alert, a code change? How do you choose?
- [MS01-045] How do you validate input data in a pipeline (schema checks, range checks, distribution checks) before training starts?
- [MS01-046] What model quality gates would you require before a candidate is promoted to production?
- [MS01-047] Compare orchestrators such as Airflow, Kubeflow Pipelines, Argo and Prefect for ML workflows.
- [MS01-048] How do you make pipeline steps idempotent and cacheable so that reruns and backfills are safe?
- [MS01-049] What metadata should a model registry entry hold (lineage, metrics, signature, data version, owner)?
- [MS01-050] How would you design stage transitions (staging, production, archived) and an approval workflow for promoting models?
- [MS01-051] How is the Evaluation Store pattern used to keep track of model performance across versions?
- [MS01-052] How do you build eval-gated CI/CD for LLM systems, including golden-set rotation and judge-drift detection?
- [MS01-053] What per-PR eval budget and caching strategies keep CI evals affordable?
- [MS01-054] How do you build a model lifecycle process that survives provider deprecations?
- [MS01-055] A provider retires your model version in 30 days, or deprecates it mid-rollout. What is the plan?
- [MS01-056] What happens when a vendor retires a model mid-quarter and your evals depend on it as the judge?
- [MS01-057] Design a model platform that serves hundreds of production ML models with versioning, monitoring and feature access.
- [MS01-058] How would you operate and govern a portfolio of hundreds of models with consistent evaluation and ownership?

## Serving and inference deployment
- [MS01-059] What is the difference between online (real-time) and batch prediction, and how do you choose between them?
- [MS01-060] How do you deploy an ML model in production?
- [MS01-061] Should model serving be synchronous (chat), asynchronous (queue), batch (nightly), or streaming? How do you decide?
- [MS01-062] What is the Batch Serving design pattern, and where is it applied?
- [MS01-063] When is streaming inference (for example on Kafka or Flink) justified over request-response serving?
- [MS01-064] How can PyTorch support real-time inference?
- [MS01-065] When would you convert a model to ONNX, and what can go wrong?
- [MS01-066] What is training-serving skew, and how do you prevent it?
- [MS01-067] Where in a PyTorch serving path would you put the feature scaler so it cannot drift from training?
- [MS01-068] What is a feature store, and how do the offline and online stores differ?
- [MS01-069] What do model servers such as Triton, TorchServe or TF Serving give you over a hand-written Flask endpoint?
- [MS01-070] How does dynamic batching trade latency for throughput in a model server?
- [MS01-071] How would you deploy a model with strict low-latency requirements?
- [MS01-072] How do you ensure your serving stack is scalable and performs well with large datasets and traffic?
- [MS01-073] What is the Workload Isolation pattern, and why is it important?
- [MS01-074] You configure autoscaling for a vLLM deployment on GKE. Which scaling signal should you use, and why not CPU?
- [MS01-075] How do you handle cold starts when a large model takes minutes to load onto a new replica?
- [MS01-076] How do you decide between self-hosted inference and managed APIs for infrastructure reasons?
- [MS01-077] How do you choose an inference engine and orchestration layer for a given workload?
- [MS01-078] What is a queue-based architecture for LLM requests, and when do you need one?
- [MS01-079] How do you design an AI task queue that avoids timeouts and preserves ordering guarantees?
- [MS01-080] When would you run agent workloads in containers rather than directly on a host?
- [MS01-081] How do you plan disaster recovery for an LLM application that relies on multiple providers?
- [MS01-082] How would you deploy a model as a REST API, and what do you add to make it production grade?
- [MS01-083] A model needs 20 ms per request at batch size 1 and must handle 2,000 QPS with p99 under 100 ms. How do you estimate replica count?

## Rollout strategies: shadow, canary and rollback
- [MS01-084] What is the difference between shadow deployment, canary release, A/B testing and blue-green deployment for models?
- [MS01-085] What is the Shadow Model design pattern, and when should you use it?
- [MS01-086] You want to measure a new model or agent version on real traffic with zero user risk before serving any of its output. Which rollout stage fits?
- [MS01-087] What rollout order (shadow, canary, full) and which rollback layers (model, config, feature) would you use for an LLM system?
- [MS01-088] What metrics and guardrails would automatically halt a canary rollout?
- [MS01-089] How do you choose canary traffic share and duration so that you can detect a given regression with statistical confidence?
- [MS01-090] How would you use feature flags or a model router to roll out and roll back model versions independently of code?
- [MS01-091] A new model version rolled out and quality is bad. Walk through the rollback. What is different from rolling back code?
- [MS01-092] You roll back a bad model by swapping weights to the previous version, but predictions stay degraded for several minutes. What is the most likely cause?
- [MS01-093] What is your rollout plan for a new ASR model across hundreds of health systems?
- [MS01-094] What is your rollback story if a bad model version wrote thousands of records overnight?
- [MS01-095] How do you run a controlled rollout of a retrieval or prompt change with explicit rollback criteria?
- [MS01-096] How do you keep feature schemas backward compatible when old and new model versions run side by side?
- [MS01-097] Quality regressed after a rollout but only for one language. Does your canary design catch that?
- [MS01-098] How would you A/B test a new robot policy across a fleet without exposing customers to a regression?

## Monitoring production models
- [MS01-099] Why are monitoring and logging important in MLOps?
- [MS01-100] What are the three layers to monitor for a deployed model: system health, data quality and model quality?
- [MS01-101] How do you monitor a model's performance in production, for example a ranking model?
- [MS01-102] How do you evaluate model quality in production when ground-truth labels arrive late or never?
- [MS01-103] Which operational metrics (latency percentiles, throughput, error rate, GPU utilisation, cost per request) belong on an ML serving dashboard?
- [MS01-104] What do you log for each prediction so that you can later debug, label and retrain, and what privacy limits apply?
- [MS01-105] Why do slice-level metrics matter more than aggregate metrics when monitoring a model?
- [MS01-106] How do you set alert thresholds for model monitoring so that you avoid both missed incidents and alert fatigue?
- [MS01-107] What would you monitor after deploying a fine-tuned model?
- [MS01-108] What changes about evaluation and observability when inference runs on the user's device?
- [MS01-109] What is the business KPI for a deployed LLM system, and what proxy signals fire before labels arrive (prediction-distribution drift, calibration, staleness, cost per request)?
- [MS01-110] Design the monitoring stack for a fraud model whose labels (chargebacks) arrive weeks after prediction.

## Data drift and distribution shift
- [MS01-111] What is model drift, and how do you handle it?
- [MS01-112] What is the difference between concept drift and data drift, and how do you overcome each?
- [MS01-113] What kinds of distribution shift exist (covariate, label, concept), and how do you statistically detect each in a deployed model?
- [MS01-114] Compare PSI, KS test, chi-square and Jensen-Shannon divergence for drift detection. When would you use each?
- [MS01-115] A Kolmogorov-Smirnov drift test on a feature with about 200,000 daily samples fires almost every day. What is going on and what is the fix?
- [MS01-116] How do you detect and handle distribution shift between fleet data and your training set?
- [MS01-117] How do you detect data drift for an LLM application in production?
- [MS01-118] How would you detect drift in embeddings or other unstructured inputs such as images and text?
- [MS01-119] How do you distinguish concept drift from a data-pipeline bug?
- [MS01-120] Your PSI alert fires on one feature. How do you tell a real upstream change from a broken pipeline?
- [MS01-121] If only the label prior has shifted, can you fix it without retraining?
- [MS01-122] Feature drift alerts fire but model accuracy is unchanged. What do you do, and what does that imply about your monitoring design?

## Retraining and production incidents
- [MS01-123] A model's performance degrades after deployment. What are the first things you check?
- [MS01-124] What would you do if a model performs well in testing but poorly in production?
- [MS01-125] How would you handle a situation where your AI system's quality degrades over time?
- [MS01-126] How would you monitor model health in production, and what signals would trigger retraining?
- [MS01-127] How often would you retrain a fraud model, and how do you justify the cadence?
- [MS01-128] What is the difference between stateless retraining from scratch and warm-start or incremental training, and how does historical data feed adaptation?
- [MS01-129] When would you use scheduled retraining rather than drift-triggered retraining?
- [MS01-130] What can go wrong with fully automated retraining (feedback loops, poisoned data, silent regressions), and what guardrails do you add?
- [MS01-131] How do you validate a retrained model before it is automatically promoted?
- [MS01-132] An upstream team silently changes a column's units or schema. How does your system catch it before it corrupts the model?
- [MS01-133] How would you debug a production LLM service whose behaviour changed overnight with no code deploy?
- [MS01-134] How would you explain to a non-technical stakeholder why a model aced the demo but failed in production?
- [MS01-135] A model loses about 0.5% AUC per month and retraining costs a fixed amount per run. How would you decide the retraining frequency?
- [MS01-136] Your LLM pilot succeeded. What changes when you take it to production for 5,000 users?
- [MS01-137] How do you keep a safety or compliance case current when the model is retrained every few weeks?

## Edge, on-device and air-gapped deployment
- [MS01-138] When does on-device or edge inference make sense, and what actually constrains it?
- [MS01-139] Your PM wants AI-powered summarisation in the app. Walk through the on-device versus cloud decision.
- [MS01-140] What usage or cost data would flip your decision between on-device and cloud inference?
- [MS01-141] How do you decide where the local-versus-cloud routing boundary sits for on-device inference?
- [MS01-142] What model optimisation techniques (quantisation, pruning, distillation, TFLite, Core ML, ONNX Runtime) do you apply for edge deployment, and what do they cost in accuracy?
- [MS01-143] If an on-device model is noticeably worse than the cloud model, what do you do?
- [MS01-144] Your on-device model file is 800 MB. How does it get onto users' devices?
- [MS01-145] How do you design over-the-air model updates with integrity verification, versioning and staged rollout?
- [MS01-146] What changes when a customer wants an enterprise workflow agent deployed air-gapped?
- [MS01-147] How do you handle model updates in an on-prem LLM deployment without regressions?
- [MS01-148] How do you roll back a bad model that is already deployed on 10 million devices?
