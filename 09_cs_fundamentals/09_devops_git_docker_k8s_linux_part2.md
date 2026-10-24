---
domain: cs
topic: devops_git_docker_k8s_linux
title: DevOps, Git, Docker, Kubernetes, Linux
tags: [git, docker, kubernetes, linux, devops]
count: 87
part: 2/2
---
# DevOps, Git, Docker, Kubernetes, Linux (part 2)

## Kubernetes core concepts
- [CS09-090] What is Kubernetes, and why is it used for container orchestration?
- [CS09-091] Why did Kubernetes win as the dominant orchestrator?
- [CS09-092] Describe the control plane and worker node components of a Kubernetes cluster.
- [CS09-093] What happens if etcd data is lost or the API server goes down?
- [CS09-094] How do Pods facilitate the management of containers in Kubernetes?
- [CS09-095] What is the difference between a pod and a container, and between a Deployment, a ReplicaSet and a pod?
- [CS09-096] How do ReplicaSets ensure pod availability?
- [CS09-097] Differentiate between Deployments, StatefulSets and DaemonSets.
- [CS09-098] What are Jobs and CronJobs in Kubernetes, and when would you use them?
- [CS09-099] What are Namespaces in Kubernetes used for?
- [CS09-100] How do Labels and Selectors work together?
- [CS09-101] What happens when a pod crashes? What does self-healing mean in Kubernetes?
- [CS09-102] What should liveness, readiness and startup probes each check?
- [CS09-103] What should you consider when performing a rolling update, and how do you roll back?
- [CS09-104] What is the difference between resource requests and limits, and what happens on OOMKill or CPU throttling?
- [CS09-105] How does the Horizontal Pod Autoscaler work, and what are its limitations?
- [CS09-106] How does the scheduler place pods? Explain taints, tolerations and node affinity.
- [CS09-107] What are PersistentVolumes, PersistentVolumeClaims and StorageClasses?
- [CS09-108] Walk through what happens from running kubectl apply -f deployment.yaml to pods running on nodes.

## Kubernetes networking, configuration and troubleshooting
- [CS09-109] Explain the Kubernetes Service types and when to use each.
- [CS09-110] How do Services route traffic to pods?
- [CS09-111] What is the purpose of Ingress, and what are its key components?
- [CS09-112] How does DNS resolution for Services work in Kubernetes?
- [CS09-113] What is the Container Network Interface (CNI), and how does it integrate with Kubernetes?
- [CS09-114] How do you implement Network Policies in Kubernetes, and what are their benefits?
- [CS09-115] What is the difference between a ConfigMap and a Secret, and how are they consumed by pods?
- [CS09-116] Are Kubernetes Secrets actually secure? How would you protect sensitive data in a cluster?
- [CS09-117] A pod is stuck in Pending, CrashLoopBackOff or ImagePullBackOff. How do you debug each case?
- [CS09-118] A Service has endpoints but clients still get connection errors. How do you troubleshoot?

## Linux commands, permissions and shell
- [CS09-119] What do the rwx permission bits mean for owner, group and others?
- [CS09-120] How do you read and set permissions with chmod in symbolic and octal notation?
- [CS09-121] What do setuid, setgid and the sticky bit do, and how does umask affect new files?
- [CS09-122] What does sudo do, and why is running everything as root dangerous?
- [CS09-123] How do stdin, stdout, stderr, pipes and redirection work, and what do 2>&1 and tee do?
- [CS09-124] What does the PATH variable do, and how does the shell search for commands?
- [CS09-125] How do grep, awk, sed, find and xargs differ, and how do you combine them to analyze log files?
- [CS09-126] How would you find the 10 most frequent IP addresses in a large access log with shell commands?
- [CS09-127] How do you compress and archive files on Linux, and how do tar, gzip and zip differ?
- [CS09-128] What do set -euo pipefail and exit codes do in a shell script?
- [CS09-129] How does SSH key-based authentication work?
- [CS09-130] How do you check logs and manage a service with systemd?

## Linux processes and troubleshooting
- [CS09-131] How do you inspect running processes and their CPU and memory use with ps, top and similar tools?
- [CS09-132] What do the process states R, S, D and Z mean in Linux?
- [CS09-133] What is the difference between a zombie process and an orphan process?
- [CS09-134] What is the difference between a foreground and a background process, and what do nohup and & do?
- [CS09-135] What is the difference between kill -15 and kill -9?
- [CS09-136] How do you find which process is listening on a given port and kill it?
- [CS09-137] How do you check CPU, memory and disk usage on a Linux server?
- [CS09-138] A Linux server is slow. Walk through the commands you would run to check CPU, memory, disk and network.
- [CS09-139] What does load average mean, and how does it differ from CPU utilization?
- [CS09-140] CPU usage is low but system load is high. Which thread states and system metrics do you check?
- [CS09-141] How do you handle a CPU spike in production, an OOM, and an IO read/write spike?
- [CS09-142] df shows the disk is full but du does not account for the space. What could be happening?
- [CS09-143] Applications fail with "too many open files" or "no space left on device" despite free disk space. How do you diagnose?

## Cloud computing basics
- [CS09-144] What is cloud computing, and how does it differ from a traditional data center?
- [CS09-145] What are the five NIST characteristics of cloud computing?
- [CS09-146] What is the difference between IaaS, PaaS and SaaS?
- [CS09-147] What is the difference between public, private and hybrid cloud?
- [CS09-148] What is virtualization, and what are the types of hypervisors?
- [CS09-149] What is the shared responsibility model in the cloud?
- [CS09-150] What are regions and availability zones, and how do they help design for high availability?
- [CS09-151] What is a VPC? Walk through its main components.
- [CS09-152] What is IAM, and how do you apply the principle of least privilege?
- [CS09-153] What are S3 storage classes, and why do they exist?
- [CS09-154] What is the difference between reserved, spot and on-demand instances?
- [CS09-155] What is serverless computing? What are its pros and cons?
- [CS09-156] What are cold starts in serverless, and how do you mitigate them?
- [CS09-157] How do Layer 4 and Layer 7 load balancers differ, and how does auto scaling use them?
- [CS09-158] What is vendor lock-in, and how do you reduce it?
- [CS09-159] How do you keep cloud costs under control?
- [CS09-160] How would you migrate an on-premises application to the cloud? What are the 6 Rs of migration?

## Infrastructure as code, monitoring and reliability
- [CS09-161] What is Infrastructure as Code, and what are its benefits?
- [CS09-162] What is idempotency, and why is it important in automation?
- [CS09-163] How does Terraform turn code into cloud infrastructure?
- [CS09-164] What is Terraform state, and why does it matter?
- [CS09-165] How do you manage Terraform state in a team (remote backend, locking)?
- [CS09-166] What is configuration drift, and how do you detect and prevent it?
- [CS09-167] Compare Terraform, CloudFormation and Ansible. When do you use each?
- [CS09-168] What is the difference between mutable and immutable infrastructure?
- [CS09-169] What are the DevOps practices of infrastructure as code and continuous monitoring?
- [CS09-170] What are the three pillars of observability (metrics, logs, traces)?
- [CS09-171] Explain the Prometheus and Grafana monitoring stack.
- [CS09-172] Does Prometheus pull or push metrics, and what are the tradeoffs?
- [CS09-173] What are SLIs, SLOs and SLAs, and how do they drive alerting?
- [CS09-174] What makes a good alert, and how do you avoid alert fatigue?
- [CS09-175] What are the four golden signals, and what would you monitor for a web service?
- [CS09-176] A production service suddenly shows elevated latency and errors. Walk through your incident response and investigation.
