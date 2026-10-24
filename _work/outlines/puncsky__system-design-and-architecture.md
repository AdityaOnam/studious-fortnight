# OUTLINE of puncsky__system-design-and-architecture


## FILE AGENTS.md  (3 KB)
- AGENTS.md
  - What this repo is
  - Commands
  - Structure
  - Chapter conventions
  - Agent skills and the `.pm` board

## FILE README.md  (11 KB)
  - How to use this book?
  - Who's Tian Pan?
  - Join us for further discussion!
  - License

## FILE SUMMARY.md  (4 KB)
- Summary
  - System Design Theories
  - Effective Interview Prep

## FILE awesome-system-design.md  (1 KB)
  - Tutorials and Blogs
  - Books

## FILE .agents/skills/dont-code-but-answer/SKILL.md  (1 KB)
- Task: Answer, don't change anything
  - Rules
  - Question

## FILE .agents/skills/loopx/SKILL.md  (5 KB)
- Task: Drain a `.pm` workstream item by item
  - Preconditions (once)
  - The loop
  - Handling a block
  - Exit
  - Guardrails
  - Arguments

## FILE .agents/skills/mermaid/SKILL.md  (2 KB)
  - Conventions
  - Verify (mandatory, before answering)
  - Output

## FILE .agents/skills/pm/SKILL.md  (8 KB)
- Task: Arrange the `.pm` board
  - Mission — the editor's lens
  - The `.pm` hierarchy
  - Rules (enforce every time)
  - Subcommands
  - Templates
  - Arguments

## FILE .agents/skills/pm-brainstorm/SKILL.md  (3 KB)
- Task: Propose milestones and tasks
  - Steps
  - Topic

## FILE .agents/skills/ship/SKILL.md  (2 KB)
- Task: Ship the current main branch
  - Session-aware mode
  - Step 1 — Verify branch
  - Step 2 — Inspect state
  - Step 3 — Pull latest with rebase
  - Step 4 — Stage and commit
  - Step 5 — Push
  - Step 6 — Report
  - Optional User Context

## FILE .pm/DO_NOT_DO.md  (1 KB)
- `.pm` anti-goals — do not do

## FILE .pm/README.md  (0 KB)
- `.pm` — book board

## FILE .pm/w1/README.md  (0 KB)
- w1 — General worker queue (worker1)
  - Milestones

## FILE drafts/fintech-sd-work-in-progress.md  (1 KB)
- Centralized Finance
- Decentralized Finance
- Case Study
  - Apple Pay

## FILE drafts/three-basic-topics.md  (7 KB)
  - Appendix: Three Basic Topics

## FILE en/120-designing-uber.md  (3 KB)
  - Requirements
  - Architecture
  - Why micro services?
  - Dispatch Service
  - Payment Service
  - UserProfile Service and Trip Service
  - Push Notification Service

## FILE en/121-designing-facebook-photo-storage.md  (2 KB)
  - Motivation & Assumptions
  - Solution
  - Architecture
  - Data Layout
  - Usecases

## FILE en/122-key-value-cache.md  (3 KB)
  - Regular Patterns
  - Cache-aside pattern
  - Where to put the cache?
  - What if data volume reaches the cache capacity? Use cache replacement policies
  - Who are the King of the cache usage?

## FILE en/123-ios-architecture-patterns-revisited.md  (3 KB)
  - Why bother with architecture?
  - Tight-coupling MVC
  - Cocoa MVC
  - MVP
  - MVVM
  - VIPER

## FILE en/136-fraud-detection-with-semi-supervised-learning.md  (5 KB)
  - Clarify Requirements
  - **High-level Architecture**
  - Core Components and Workflows
  - Serving

## FILE en/137-stream-and-batch-processing.md  (3 KB)
  - Why such frameworks?
  - Brief history of batch/stream processing
  - How?
  - Comparison

## FILE en/140-designing-a-recommendation-system.md  (8 KB)
  - What are we optimizing for? User Satisfaction
  - How to evaluate the satisfaction?
  - How to optimize for those goals? Machine Learning Models
  - How do models observe and measure the reality? Feature engineering
  - Large-scale Training in Realtime
  - How to further reducing the latency? Recall Strategy
  - Data Dependencies
  - What is the content analysis?
  - Why are we analyzing those raw data?
  - Case Study: Analysis Result of an Article
  - Article features are important
  - More on Semantic Tags
  - Document classification
  - Calculating relevance

## FILE en/145-introduction-to-architecture.md  (4 KB)
  - What is architecture?
  - Why do we need architecture?
  - 1. Layered Architecture
  - 2. Event-Driven Architecture
  - 3. Micro-kernel Architecture (aka Plug-in Architecture)
  - 4. Microservices Architecture
  - 5. Space-based Architecture

## FILE en/161-designing-stock-exchange.md  (41 KB)
  - Requirements
  - Architecture
  - Components and How do they interact with each other.

## FILE en/162-designing-smart-notification-of-stock-price-changes.md  (39 KB)
  - Requirements
  - Sketching out the Architecture
  - What are those components and how do they interact with each other?

## FILE en/166-designing-payment-webhook.md  (4 KB)
  - 1. Clarifying Requirements
  - 2. Sketch out the high-level design
  - 3. Features and Components

## FILE en/167-designing-paypal-money-transfer.md  (54 KB)
  - Clarifying Requirements
  - Architecture
  - Features and Components

## FILE en/168-designing-a-metric-system.md  (40 KB)
  - Requirements
  - Architecture
  - Features and Components

## FILE en/174-designing-memcached.md  (2 KB)
  - Requirements
  - Architecture
  - How does the client determine which server to query?
  - How to use cache?
  - How to further optimize?

## FILE en/177-designing-Airbnb-or-a-hotel-booking-system.md  (4 KB)
  - Requirements
  - Architecture
  - Components

## FILE en/178-lyft-marketing-automation-symphony.md  (4 KB)
  - Acquisition Efficiency Problem：How to achieve a better ROI in advertising?
  - Solution: Automation
  - Architecture
  - Main components

## FILE en/179-designing-typeahead-search-or-autocomplete.md  (2 KB)
  - Requirements
  - Architecture
  - Result Aggregator
  - Performance

## FILE en/182-designing-l7-load-balancer.md  (5 KB)
  - Requirements
  - Challenges
  - Solutions
  - Results: requests are more balanced

## FILE en/2016-02-13-crack-the-system-design-interview.md  (16 KB)
- Design Pinterest
  - Step 1. Clarify requirements and make assumptions
  - Step 2. Sketch out the high-level design
  - Step 3. Dive into individual components and how they interact with each other
  - Step 4. Wrap up with blindspots or bottlenecks.

## FILE en/2018-07-10-cloud-design-patterns.md  (2 KB)
  - Availability patterns
  - Data Management patterns
  - Security Patterns

## FILE en/2018-07-20-experience-deep-dive.md  (3 KB)
  - Intended Audience
  - Question Description
  - Interviewer tips
  - Scoring

## FILE en/2018-07-21-data-partition-and-routing.md  (1 KB)
  - Why data partition and routing?
  - How to do data partition and routing?

## FILE en/2018-07-24-replica-and-consistency.md  (2 KB)
  - Why replica and consistency?
  - Consistency trade-offs for CAP theorem
  - "2 of 3" is mis-leading

## FILE en/2026-10-21-designing-always-on-agent.md  (16 KB)
  - Requirements
  - Architecture
  - Components
  - Wrap-up: bottlenecks and open problems

## FILE en/2026-10-22-agent-system-layers-and-logical-components.md  (5 KB)
  - The stack (layers)
  - Logical components (inside one agent)
  - Why agents are a systems problem
  - Flexibility is risk
  - Cheat sheet

## FILE en/38-how-to-stream-video-over-http.md  (1 KB)
  - Motivation
  - Solution
  - Architecture

## FILE en/45-how-to-design-netflix-view-state-service.md  (1 KB)
  - Motivation
  - Architecture

## FILE en/49-facebook-tao.md  (2 KB)
  - What are the challenges?
  - Data Model
  - Solutions: TAO
  - TAO's Architecture

## FILE en/61-what-is-apache-kafka.md  (4 KB)
  - Why use Apache Kafka?
  - Why is Kafka so fast?
  - Architecture
  - How to tolerate fault?
  - Is Kafka an AP or CP system in CAP theorem?

## FILE en/63-soft-skills-interview.md  (1 KB)
  - What is an interview?
  - Why is soft skill so important?
  - Generic answers (stories) to prepare

## FILE en/78-four-kinds-of-no-sql.md  (3 KB)
  - Key-value Store
  - Document Store
  - Column-oriented Store
  - Graph Database

## FILE en/80-relational-database.md  (1 KB)
  - Schema Design and 3rd Normal Form (3NF)
  - Db Proxy

## FILE en/83-lambda-architecture.md  (1 KB)
  - Why lambda architecture?
  - What is lambda architecture?

## FILE en/84-designing-a-url-shortener.md  (5 KB)
  - Assumptions
  - Encode Url
  - KV store
  - Followup

## FILE en/97-designing-a-kv-store-with-external-storage.md  (2 KB)
  - Requirements
  - Solution
  - Components
  - Operations

## FILE zh-CN/120-designing-uber.md  (1 KB)
  - 需求
  - 架构
  - 为什么选择微服务？
  - 调度服务
  - 支付服务
  - 用户资料服务和行程服务
  - 推送通知服务

## FILE zh-CN/121-designing-facebook-photo-storage.md  (1 KB)
  - 动机与假设
  - 解决方案
  - 架构
  - 数据布局
  - 用例

## FILE zh-CN/122-key-value-cache.md  (1 KB)
  - 常规模式
  - 旁路缓存模式
  - 缓存放在哪里？
  - 如果数据量达到缓存容量怎么办？使用缓存替换策略
  - 谁是缓存使用的王者？

## FILE zh-CN/123-ios-architecture-patterns-revisited.md  (2 KB)
  - 为什么要关注架构？
  - 紧耦合 MVC
  - Cocoa MVC
  - MVP
  - MVVM
  - VIPER

## FILE zh-CN/136-fraud-detection-with-semi-supervised-learning.md  (2 KB)
  - 明确需求
  - **高级架构**
  - 核心组件和工作流程
  - 服务

## FILE zh-CN/137-stream-and-batch-processing.md  (2 KB)
  - 为什么需要这样的框架？
  - 批处理/流处理的简史
  - 如何？
  - 比较

## FILE zh-CN/140-designing-a-recommendation-system.md  (3 KB)
  - 我们优化的目标是什么？用户满意度
  - 如何评估满意度？
  - 如何优化这些目标？机器学习模型
  - 模型如何观察和测量现实？特征工程
  - 实时大规模训练
  - 如何进一步减少延迟？召回策略
  - 数据依赖
  - 什么是内容分析？
  - 我们为什么要分析这些原始数据？
  - 案例研究：一篇文章的分析结果
  - 文章特征的重要性
  - 更多关于语义标签
  - 文档分类
  - 计算相关性

## FILE zh-CN/145-introduction-to-architecture.md  (2 KB)
  - 什么是架构？
  - 我们为什么需要架构？
  - 1. 分层架构
  - 2. 事件驱动架构
  - 3. 微内核架构（即插件架构）
  - 4. 微服务架构
  - 5. 基于空间的架构

## FILE zh-CN/161-designing-stock-exchange.md  (38 KB)
  - 需求
  - 架构
  - 组件及其相互作用

## FILE zh-CN/162-designing-smart-notification-of-stock-price-changes.md  (37 KB)
  - 需求
  - 构建架构草图
  - 这些组件是什么，它们如何相互作用？

## FILE zh-CN/166-designing-payment-webhook.md  (2 KB)
  - 1. 澄清需求
  - 2. 概述高层设计
  - 3. 功能和组件

## FILE zh-CN/167-designing-paypal-money-transfer.md  (51 KB)
  - 澄清需求
  - 架构
  - 功能和组件

## FILE zh-CN/168-designing-a-metric-system.md  (39 KB)
  - 需求
  - 架构
  - 特性与组件

## FILE zh-CN/174-designing-memcached.md  (1 KB)
  - 需求
  - 架构
  - 客户端如何确定查询哪个服务器？
  - 如何使用缓存？
  - 如何进一步优化？

## FILE zh-CN/177-designing-Airbnb-or-a-hotel-booking-system.md  (2 KB)
  - 需求
  - 架构
  - 组件

## FILE zh-CN/178-lyft-marketing-automation-symphony.md  (2 KB)
  - 获取效率问题：如何在广告中实现更好的投资回报率？
  - 解决方案：自动化
  - 架构
  - 主要组件

## FILE zh-CN/179-designing-typeahead-search-or-autocomplete.md  (1 KB)
  - 需求
  - 架构
  - 结果聚合器
  - 性能

## FILE zh-CN/182-designing-l7-load-balancer.md  (3 KB)
  - 需求
  - 挑战
  - 解决方案
  - 结果：请求更加均衡

## FILE zh-CN/2016-02-13-crack-the-system-design-interview.md  (7 KB)
- 设计 Pinterest
  - 第一步：澄清需求并做出假设
  - 第二步：勾勒出高层设计
  - 第三步：深入各个组件及其相互作用
  - 第四步：总结盲点或瓶颈。

## FILE zh-CN/2018-07-10-cloud-design-patterns.md  (2 KB)
  - Availability patterns
  - Data Management patterns
  - Security Patterns

## FILE zh-CN/2018-07-20-experience-deep-dive.md  (1 KB)
  - 目标受众
  - 问题描述
  - 面试官提示
  - 评分

## FILE zh-CN/2018-07-21-data-partition-and-routing.md  (0 KB)
  - 为什么要进行数据分区与路由？
  - 如何进行数据分区与路由？

## FILE zh-CN/2018-07-24-replica-and-consistency.md  (1 KB)
  - 为什么副本和一致性？
  - CAP定理的一致性权衡
  - “2 of 3”是误导性的

## FILE zh-CN/2026-10-21-designing-always-on-agent.md  (7 KB)
  - 需求
  - 架构
  - 组件
  - 总结：瓶颈与开放问题

## FILE zh-CN/2026-10-22-agent-system-layers-and-logical-components.md  (2 KB)
  - 技术栈（分层）
  - 逻辑组件（单个智能体内部）
  - 为什么智能体是系统问题
  - 灵活性即风险
  - 速记表

## FILE zh-CN/38-how-to-stream-video-over-http.md  (0 KB)
  - 动机
  - 解决方案
  - 架构

## FILE zh-CN/45-how-to-design-netflix-view-state-service.md  (1 KB)
  - 动机
  - 架构

## FILE zh-CN/49-facebook-tao.md  (1 KB)
  - 面临的挑战是什么？
  - 数据模型
  - 解决方案：TAO
  - TAO 的架构

## FILE zh-CN/61-what-is-apache-kafka.md  (2 KB)
  - 为什么使用 Apache Kafka？
  - 为什么 Kafka 这么快？
  - 架构
  - 如何容错？
  - Kafka 是 CAP 定理 中的 AP 还是 CP 系统？

## FILE zh-CN/63-soft-skills-interview.md  (0 KB)
  - 什么是面试？
  - 为什么软技能如此重要？
  - 准备的通用回答（故事）

## FILE zh-CN/78-four-kinds-of-no-sql.md  (1 KB)
  - 键值存储
  - 文档存储
  - 列式存储
  - 图数据库

## FILE zh-CN/80-relational-database.md  (0 KB)
  - 模式设计和第三范式 (3NF)
  - 数据库代理

## FILE zh-CN/83-lambda-architecture.md  (1 KB)
  - 为什么选择 Lambda 架构？
  - 什么是 Lambda 架构？

## FILE zh-CN/84-designing-a-url-shortener.md  (1 KB)
  - 假设
  - 编码网址
  - KV 存储
  - 后续问题

## FILE zh-CN/97-designing-a-kv-store-with-external-storage.md  (1 KB)
  - 需求
  - 解决方案
  - 组件
  - 操作

## FILE zh-CN/README.md  (6 KB)
  - 系统设计与构架 - 中文版