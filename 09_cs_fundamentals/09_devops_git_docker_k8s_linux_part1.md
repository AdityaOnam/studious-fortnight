---
domain: cs
topic: devops_git_docker_k8s_linux
title: DevOps, Git, Docker, Kubernetes, Linux
tags: [git, docker, kubernetes, linux, devops]
count: 89
part: 1/2
---
# DevOps, Git, Docker, Kubernetes, Linux (part 1)

## DevOps fundamentals and culture
- [CS09-001] What is DevOps, and is it a role, a tool or a culture?
- [CS09-002] What are the key principles and benefits of DevOps?
- [CS09-003] Explain the stages of the DevOps lifecycle.
- [CS09-004] How does DevOps differ from Agile?
- [CS09-005] What is the difference between DevOps and NoOps?
- [CS09-006] What does "Shift Left" mean in DevOps, and what practices does it imply?
- [CS09-007] What role does automation play in DevOps, and how do you decide what to automate?
- [CS09-008] How does version control support DevOps practices?
- [CS09-009] Name the main categories of tools in a DevOps toolchain (version control, CI/CD, containers, configuration management, monitoring) with examples of each.
- [CS09-010] What are the DORA metrics, and how else would you measure DevOps success?
- [CS09-011] How do companies ship code to production, from commit to running service?
- [CS09-012] Monorepo vs multiple repositories: what are the tradeoffs?
- [CS09-013] How does SRE relate to DevOps, and what are error budgets?
- [CS09-014] What is a blameless postmortem and why does it matter?
- [CS09-015] What is GitOps and how does it differ from a push-based deployment pipeline?
- [CS09-016] A team deploys manually once a quarter and has frequent outages. How would you introduce DevOps practices step by step?

## Git fundamentals
- [CS09-017] What is Git and why is it used?
- [CS09-018] What is the difference between centralized and distributed version control, and why is Git considered distributed?
- [CS09-019] What is the difference between Git and GitHub?
- [CS09-020] What is a repository in Git, and how do you initialize or clone one?
- [CS09-021] What is a commit in Git, and how do you create one?
- [CS09-022] What is HEAD in Git?
- [CS09-023] What do git status and git add do?
- [CS09-024] What is the difference between the working directory, staging area and repository, and which commands move changes between them?
- [CS09-025] How does Git store information internally (blobs, trees, commits)?
- [CS09-026] What information does a commit object contain?
- [CS09-027] What is a detached HEAD state and how do you get out of it without losing work?
- [CS09-028] What does git reflog record, and when has it saved you?

## Branching, merging and undoing changes
- [CS09-029] What is branching in Git and why is it important?
- [CS09-030] How do you make a pull request, and what makes a good one?
- [CS09-031] How is a Git branch implemented, and why is branching cheap?
- [CS09-032] What is the difference between git merge and git rebase, and when would you use each?
- [CS09-033] When should you avoid rebasing, and why does rebasing rewrite history?
- [CS09-034] What is a fast-forward merge, and when does Git create a merge commit instead?
- [CS09-035] How do you resolve merge conflicts, and what do the conflict markers mean?
- [CS09-036] How does git fetch differ from git pull?
- [CS09-037] When would you use git stash, and what happens to untracked files?
- [CS09-038] How do git reset (soft, mixed, hard), git revert and git checkout differ when undoing changes?
- [CS09-039] What does git cherry-pick do, and when is it appropriate?
- [CS09-040] How does .gitignore work, and why does it not affect files that are already tracked?
- [CS09-041] Compare Git Flow, GitHub Flow and trunk-based development.
- [CS09-042] Squash merge, merge commit and rebase merge on a pull request: what are the tradeoffs?
- [CS09-043] What is the difference between git push --force and --force-with-lease?
- [CS09-044] How would you undo a bad commit that has already been pushed to a shared main branch?
- [CS09-045] You accidentally committed a secret and pushed it. What do you do?
- [CS09-046] How would you find which commit introduced a bug using Git?
- [CS09-047] A teammate rebased and force-pushed a shared branch, and others' commits disappeared. How do you recover?

## CI/CD pipelines
- [CS09-048] How do CI/CD relate to DevOps?
- [CS09-049] What is a build tool and what role does it play in a pipeline?
- [CS09-050] What are the stages of a CI/CD pipeline, and what does each automate?
- [CS09-051] What belongs in a CI pipeline, and what should be left out?
- [CS09-052] What is a build artifact, and why store it in an artifact repository?
- [CS09-053] What are the benefits of defining pipelines as code (Jenkinsfile, GitHub Actions workflows)?
- [CS09-054] How do you integrate API testing and API mocks into a CI/CD pipeline?
- [CS09-055] Compare blue-green, canary and rolling deployments.
- [CS09-056] How do feature flags decouple deployment from release?
- [CS09-057] How do you roll back a bad deployment quickly and safely?
- [CS09-058] How should secrets be handled in CI/CD pipelines?
- [CS09-059] Your pipeline takes 45 minutes. How do you make it faster?
- [CS09-060] Tests pass locally but fail intermittently in CI. How do you diagnose and handle flaky tests?
- [CS09-061] How would you secure the software supply chain in a pipeline (dependency scanning, image signing)?
- [CS09-062] How do you apply database schema changes in a continuous deployment setup with zero downtime?
- [CS09-063] How would you design CI/CD for a monorepo containing many services so that only affected services are built and deployed?

## Docker and containers
- [CS09-064] Why do we need containers?
- [CS09-065] What problems does Docker solve, and how does it work?
- [CS09-066] Virtual machine vs container: how do they differ under the hood?
- [CS09-067] Compare containers and virtual machines on startup time, resource usage, isolation and security.
- [CS09-068] How do containers isolate processes from each other?
- [CS09-069] What do Linux namespaces and cgroups each provide for containers?
- [CS09-070] What is a Docker image?
- [CS09-071] What is the difference between a Docker image and a container?
- [CS09-072] How does Docker use layers to build images, and how does layer caching work?
- [CS09-073] What is Docker Hub, and what is it used for?
- [CS09-074] What is a Dockerfile, and how do you build an image and run a container from it?
- [CS09-075] What is the difference between COPY and ADD in a Dockerfile?
- [CS09-076] What is the difference between CMD and ENTRYPOINT?
- [CS09-077] What is the purpose of the .dockerignore file?
- [CS09-078] How would you create a Docker image from an existing container, and is that good practice?
- [CS09-079] How do you reduce Docker image size and speed up builds?
- [CS09-080] What are multi-stage builds, and why use them?
- [CS09-081] What is a Docker volume, and what is the difference between volumes and bind mounts?
- [CS09-082] What is docker-compose, and when would you use it?
- [CS09-083] Can containers on the same host communicate by default? Explain Docker network modes.
- [CS09-084] How do containers help continuous integration and microservice deployment?
- [CS09-085] Why is using the latest tag in production risky, and how do image digests help?
- [CS09-086] Why should containers not run as root, and how would you harden a container?
- [CS09-087] A container exits immediately after starting. How do you debug it?
- [CS09-088] A container is killed with exit code 137. What happened and how do you investigate?
- [CS09-089] What is the PID 1 problem in containers and how do you handle signals and zombie processes?
