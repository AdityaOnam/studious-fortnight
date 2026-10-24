# OUTLINE of guocong-bincai__ai-interview-guide


## FILE CONTENT_QUALITY.md  (2 KB)
- 面试题内容质量规范
  - 一、收录标准
  - 二、推荐答案结构
  - 三、数字与项目经历
  - 四、模块边界
  - 五、目录与排版
  - 六、插画质量
  - 七、提交前检查

## FILE ILLUSTRATION_GUIDE.md  (1 KB)
- 面试题插画生产规范
  - 一、从题目到图片的七步流程
  - 二、统一视觉体系
  - 三、每题生成卡
  - 四、嵌入格式
  - 五、验收清单

## FILE README.md  (17 KB)
  - ✨ 这份指南有什么不同
  - 🧠 看得懂，才能记得住、说得出
  - 📚 配套学习课件：Dive into LLMs
  - 🚀 快速开始
  - 🗺️ 选择你的 AI 岗位路线
  - 📚 题库导航
  - 🧭 高效使用这套题库
  - ☕ 支持项目
  - 🤝 内容质量与贡献
  - 📄 License

## FILE README_EN.md  (6 KB)
- AI Engineer Interview Handbook
  - Why this repository
  - Visual learning
  - Choose your path
  - Topic map
  - How to practice
  - Contributing
  - License

## FILE README_ES.md  (6 KB)
- Manual de Entrevistas para Ingeniería de IA
  - Por qué usar este repositorio
  - Aprendizaje visual
  - Elige tu ruta
  - Mapa de temas
  - Cómo practicar
  - Contribuir
  - Licencia

## FILE README_ID.md  (6 KB)
- Panduan Wawancara Engineer AI
  - Mengapa repositori ini berguna
  - Belajar secara visual
  - Pilih jalurmu
  - Peta topik
  - Cara berlatih
  - Berkontribusi
  - Lisensi

## FILE README_JA.md  (4 KB)
- AI エンジニア面接ハンドブック
  - このリポジトリの特徴
  - 図解で学ぶ
  - 職種別の学習ルート
  - トピック構成
  - 効果的な使い方
  - コントリビューション
  - ライセンス

## FILE README_KO.md  (4 KB)
- AI 엔지니어 면접 핸드북
  - 이 저장소의 특징
  - 그림으로 학습하기
  - 직무별 학습 경로
  - 주제 구성
  - 활용 방법
  - 기여하기
  - 라이선스

## FILE README_PT-BR.md  (6 KB)
- Manual de Entrevistas para Engenharia de IA
  - Por que usar este repositório
  - Aprendizado visual
  - Escolha sua trilha
  - Mapa de tópicos
  - Como praticar
  - Como contribuir
  - Licença

## FILE ai-books-online/README.md  (4 KB)
- AI / LLM 书籍与课件（在线阅读）
  - 版权边界
  - 文件清单

## FILE docs/01-basic-concepts/README.md  (99 KB)
- 📌 LLM 基础概念
  - 📋 目录
  - 1. Token 是什么？
  - 2. Temperature、Top-P、Top-K
  - 3. Context Window（上下文窗口）
  - 4. LLM 和传统机器学习模型有什么区别？为什么是“大”语言模型？
  - 5. 幻觉（Hallucination）
  - 📝 面试题
  - 6. 什么是涌现能力（Emergent Abilities）？“突然出现”一定是真的吗？
  - 7. LLM 为什么是概率模型？为什么同样的输入输出会不一样？
  - 8. LLM的幻觉(Hallucination)与偏见(Bias)
  - 9. 如何评估LLM的输出质量?
  - 10. Tokenization分词算法:BPE vs SentencePiece
  - 11. 长文本处理:超出Context Window怎么办?
  - 12. 如何给 LLM 选型？质量/速度/成本怎么权衡？（方法论）
  - 13. 什么是推理模型（Reasoning Model）？o3/R1/QwQ 和普通模型有什么区别？
  - 14. 什么是 Test-Time Compute（测试时算力）？Thinking Budget 如何控制 AI 的思考量？
  - 15. 什么是 Logits？LLM 是如何一步步生成下一个 Token 的？
  - 16. 解码策略对比：贪心解码 vs Beam Search vs 采样
  - 17. 为什么 Temperature=0 时输出依然不完全确定？
  - 18. 什么是重复惩罚（repetition_penalty）？如何防止复读机？
  - 19. 什么是停止符（EOS / Stop Token）？生成是如何终止的？
  - 20. 为什么主流 LLM 都是 Decoder-only 架构？
  - 21. Embedding（嵌入向量）是什么？和 Token 有什么关系？
  - 22. 什么是 In-Context Learning（上下文学习）？Zero-shot / Few-shot 有什么区别？
  - 23. LLM 是怎么训练出来的？预训练 → SFT → 对齐（RLHF/DPO）三阶段流程？
  - 24. 什么是 Scaling Law（规模定律）？Chinchilla 法则修正了什么？
  - 25. KV Cache 是什么？为什么能大幅加速 LLM 推理？（基础概念版）
  - 26. RLHF 和 DPO 有什么区别？（入门对比版）
  - 27. 7B 模型需要多少显存？参数量如何换算显存？（高频估算题）
  - 28. 什么是 Chat Template（对话模板）？为什么用错模板效果会暴跌？
  - 29. 什么是 MoE（混合专家模型）？为什么 DeepSeek V3 / Qwen3 都用它？（高频）
  - 30. 为什么说 LLM API 是无状态的？多轮对话的"记忆"到底存在哪？（应用开发第一性原理）
  - 31. 什么是 Prompt Caching（提示词缓存）？怎样评估它能否真正降本？（API 层高频）
  - 32. 大模型量化是什么？INT8 / INT4 / AWQ / GPTQ 怎么选？（基础概念版）
  - 33. 为什么 LLM 数学能力差？怎么缓解？（高频追问）
  - 34. Transformer 中的 Attention 机制是什么？为什么它是 LLM 的核心？（必考）
  - 35. 为什么 Transformer 需要 Position Encoding？RoPE 和绝对位置编码有什么区别？（高频）
  - 36. LLM 预训练用什么损失函数？Cross-Entropy Loss 和 Perplexity 有什么关系？（常见追问）
  - 37. LayerNorm 和 RMSNorm 有什么区别？为什么现在的 LLM 大多用 RMSNorm？（高频）
  - 38. Decoder-only 模型中的因果掩码（Causal Mask）是怎么工作的？为什么必须有它？（高频）
  - 39. 预训练数据去重（Deduplication）有什么重要性？MinHash 和 SimHash 怎么做的？（进阶高频）
  - 40. 什么是 Catastrophic Forgetting（灾难性遗忘）？微调时怎么缓解？（实战必考）
  - 41. FlashAttention 是什么？为什么它比标准 Attention 快很多？（高频）
  - 42. MHA、MQA、GQA 有什么本质区别？为什么行业转向了 GQA？（高频）
  - 43. Continuous Batching（连续批处理）是怎么工作的？为什么吞吐量能大幅提升？（实战必考）
  - 44. ALiBi 位置编码是什么？和 RoPE 有什么区别、各适用于什么场景？（进阶高频）
  - 45. Logit Bias 和采样控制：如何精准控制 LLM 的输出？（实战必考）
  - 46. 什么是合成数据（Synthetic Data）？为什么现在大模型训练越来越依赖它？（高频）
  - 47. 什么是 Function Calling（函数调用）？它是如何工作的？为什么重要？（应用开发第一性原理）
  - 48. 为什么 Transformer 不只是 Decoder-only？Encoder-Decoder（T5/BART）架构有什么独特价值？（进阶必考）
  - 📝 速记卡片
  - 49. 🚀 什么是思维链推理（Chain-of-Thought, CoT）？为什么它能大幅提升模型表现？（面试必考）
  - 50. 🔧 什么是PEFT（参数高效微调）？LoRA/QLoRA/P-Tuning有什么区别？（必考）
  - 51. 📝 少样本学习（Few-Shot Learning）的最佳实践是什么？什么时候用ICL替代微调？（实战高频）
  - 52. ⏰ 什么是知识截止期（Knowledge Cutoff）？模型遇到"不知道"的事该怎么办？（必考题）
  - 53. 🎯 幻觉有哪些不同类型？如何在工程中系统性地检测和处理？（进阶必考）
  - 54. 📊 Perplexity（困惑度）是什么？如何用它评估语言模型的好坏？（常见补充）
  - 📚 数据更新（v3.131 - 2026-08-25）

## FILE docs/02-prompt-engineering/README.md  (130 KB)
- ✍️ Prompt Engineering 面试题
  - 📋 目录
  - 📋 必背概念
  - 📝 Prompt 设计最佳实践
  - 📝 进阶Prompt技巧
  - 📝 速记卡片
  - 更新记录

## FILE docs/03-rag-system/README.md  (77 KB)
- 📚 RAG 系统面试题
  - 📋 目录
  - 一、基础概念题
  - 二、架构设计题
  - 三、优化策略题
  - 四、高分实战案例
  - 📝 速记卡片
  - 高频追问：RAG 效果如何提升？出现幻觉怎么办？
  - 🆕 补充高频题（2025-2026 全网最新）

## FILE docs/04-transformer-architecture/README.md  (76 KB)
- 🏗️ Transformer架构与注意力机制面试题
  - 📋 目录
  - 一、Transformer基础
  - 二、注意力机制
  - 三、BERT与GPT
  - 四、优化技巧
  - 五、速记卡片
  - 六、进阶架构：Transformer + SSM 混合模型（Mamba）
- 生产系统中的典型实现
- 短序列场景（N << d）
- 例如: N=128, d=4096, B=4
- Attention: 6×4×128×(4096² + 128×512) ≈ 6.4×10¹⁰ FLOPs
- FFN: 16×4×128×4096² ≈ 1.7×10¹¹ FLOPs
- FFN占比: ~73%
- 长序列场景（N >> d）
- 例如: N=8192, d=4096, B=1
- Attention: 6×1×8192×(4096² + 8192×512) ≈ 1.3×10¹¹ FLOPs
- FFN: 16×1×8192×4096² ≈ 2.2×10¹¹ FLOPs
- FFN占比: ~63%
- 超长期场景（N >> d，如 32K）
- 例如: N=32768, d=4096, B=1
- Attention: 6×1×32768×(4096² + 32768×512) ≈ 9.0×10¹¹ FLOPs
- FFN: 16×1×32768×4096² ≈ 8.8×10¹¹ FLOPs
- Attention占比反而超过 FFN！~50%

## FILE docs/05-ai-agent-basics/README.md  (140 KB)
- 🤖 AI Agent 面试题
  - 📋 目录
  - 一、基础概念题
  - 二、设计模式题
  - 三、工程实践题
  - 四、高分回答模板
  - 📝 速记卡片
  - 高频面试追问（一面/二面真题补充）
  - 五、进阶 Agent 机制（补充 Q10-Q12）
  - 六、2026年Claude Opus 4.6核心能力：Inter-tool Thinking与自适应思考（Q13）
  - 2026 年 Agent 岗位分化与面试趋势
  - 七、2026年AI Agent长期记忆与持续学习：ALTK-Evolve（Q14）
  - 八、Anthropic 可信 Agent 框架：Model/Harness/Tools/Environment 四组件
  - 🆕 补充高频题（2025-2026 全网最新）
  - 总结

## FILE docs/06-vector-index-optimization/README.md  (52 KB)
- 🔍 向量数据库索引详解
  - 📋 目录
  - 📋 核心面试题
  - 📊 性能对比总结
  - 🎯 选型指南
  - 💡 面试话术
  - 📝 速记卡片
  - 📊 更新记录
  - 专题：向量数据库选型深度对比（Pinecone / Milvus / Qdrant / Weaviate）
  - 专题：向量索引生产运维与监控
  - 专题：托管与自建向量数据库选型
  - 专题：Late Interaction 检索（ColBERTv2、ColPali、ColQwen）
  - 🆕 补充高频题（2025-2026 全网最新）
  - 🆕 高频补充题（2026 年新增）

## FILE docs/07-model-training/README.md  (49 KB)
- 🎓 大模型微调与训练面试题
  - 📋 目录
  - 一、微调基础概念
  - 二、LoRA与PEFT
  - 三、对齐技术：RLHF与DPO
  - 四、训练优化
  - 五、速记卡片
  - 六、后训练与分布式训练进阶
  - 七、知识编辑与推理蒸馏
  - 八、推理模型训练进阶
  - 📝 更新记录

## FILE docs/08-inference-optimization/README.md  (67 KB)
- ⚡ LLM 推理优化面试题
  - 📋 目录
  - 一、推理基础
  - 二、KV Cache优化
  - 三、模型量化
  - 四、推理加速
  - 五、PD 分离架构与 KV Cache 跨节点传输
  - 六、分布式推理与结构化生成

## FILE docs/09-ai-safety-evaluation/README.md  (96 KB)
- 🔥 AI 应用安全与评估面试题
  - 📋 目录
  - 一、AI 安全与合规
  - 二、评估与测试
  - 三、成本优化实战
  - 四、RAG 评估工具深度对比（RAGAS / TruLens / DeepEval / UpTrain）
  - 五、速记卡片
  - 📝 更新记录
  - 六、Agent Harness Engineering：AI Agent 评估与安全测试
  - 七、神经符号融合：2026年幻觉控制新范式
  - 八、行为对齐评估：自我报告与真实行为
  - 九、Prompt Injection 与 RAG 投毒防御
  - 十、Agent 评估平台选型
  - 十一、RAG 评估生命周期：从离线评测到生产监控
  - 十二、模型溯源与自动化红队

## FILE docs/10-production-deployment/README.md  (86 KB)
- 🔥 AI 应用开发进阶面试题
  - 📋 目录
  - 一、工程架构题
  - 二、评估与监控题
  - 三、多模态与高级应用题
  - 四、安全与合规题
  - 五、成本优化题
  - 📝 速记卡片

## FILE docs/11-multimodal-ai/README.md  (61 KB)
- 🎨 多模态大模型面试题
  - 📋 目录
  - 一、多模态基础
  - 二、CLIP模型
  - 三、BLIP模型
  - 四、应用实战
  - 五、Gemma 4 架构案例
  - 六、速记卡片
  - 七、生成模型与评估高频追问
  - 📝 更新记录
  - 八、Vision-Language Agent 评估
  - 九、全模态模型案例

## FILE docs/12-frameworks-tools/README.md  (89 KB)
- 🛠️ AI 框架与运维面试题
  - 📋 目录
  - 一、框架使用题
  - 二、向量数据库题
  - 三、测试评估题
  - 四、部署运维题
  - 📝 速记卡片
  - 📊 更新记录
  - 五、LangGraph 生产调试与状态管理
  - 六、Agent 框架选型

## FILE docs/13-multi-agent-systems/README.md  (72 KB)
- 🤖 AI Agent 面试题
  - 📋 目录
  - 一、基础概念题
  - 前置知识
  - 📝 速记卡片
  - 二、A2A + MCP 混合架构
  - 三、多 Agent 协作模式
  - 四、多 Agent 研究的工程判断
  - 五、Critic / Verifier 双 Agent 模式
  - 六、Agent Skills 与 Tools
  - 七、多 Agent 职责划分与层级任务分解
  - 十九、生产环境多 Agent 编排：反模式与场景设计（Q18）

## FILE docs/14-mcp-skill-systems/README.md  (131 KB)
- 🔥 MCP（Model Context Protocol）协议与工具系统面试题
  - 📋 目录
  - 一、MCP基础概念
  - 二、MCP核心架构与原理
  - 三、MCP Server开发实战
  - 四、MCP Client集成与配置
  - 五、MCP vs Function Calling vs Tools API
  - 六、MCP安全机制与权限管理
  - 七、企业级MCP部署与最佳实践
  - 八、2026年MCP生态最新动态
  - 九、高频面试话术
  - 📝 更新记录
  - 十、OWASP MCP Top 10 安全风险（2026 Beta）
  - 十一、MCP 边界与常见误区
  - 📝 更新记录
  - 十二、Agent 身份与持续授权
  - 十、RAG vs Skill 选型（知识供给 vs 行为供给）

## FILE docs/15-advanced-topics/README.md  (49 KB)
- 🔥 AI 应用开发高级专题面试题
  - 📋 目录
  - 一、多模态 AI 应用
  - 二、自主 Agent 与 Agentic Workflow
  - 三、AI 产品思维与架构设计
  - 四、AI 应用调试与问题排查
  - 五、前沿技术趋势
  - 六、速记卡片
  - 📝 更新记录
  - 七、Extended Thinking / Reasoning Token Budget
  - 八、AI Agent 框架选型

## FILE docs/16-resume-interview-tips/README.md  (34 KB)
- 📝 简历与面试技巧
  - 📋 目录
  - 📋 简历撰写技巧
  - 🎯 面试准备策略
  - 💰 谈薪技巧
  - 🚀 职业规划
  - 📝 面试常见问题
  - 🎯 面试前 Checklist
  - 📚 参考资料
  - 📄 示例简历
- 📄 个人简历示例
  - 👤 基本信息
  - 🎯 个人总结
  - 💼 工作经历
  - 🚀 AI 项目经验
  - 💻 技术栈
  - 🏆 所获成就
  - 🎓 教育背景
  - 📝 项目介绍话术（面试用）
  - 📄 简历文件
  - 🌟 个人特长

## FILE docs/16-resume-interview-tips/resume-ai.md  (3 KB)
- 张×× - AI 应用开发工程师
  - 🎯 求职意向
  - 💡 核心优势
  - 🤖 AI 项目经历
  - 💼 传统开发经历（工程能力背书）
  - 🏆 荣誉与影响力
  - 🛠️ 技术栈
  - 🌟 为什么选择我
  - 📝 自我评价

## FILE docs/16-resume-interview-tips/resume-go.md  (8 KB)
- 张×× - Golang 后端开发工程师
  - 🎯 求职意向
  - 💡 核心优势
  - 💼 工作经历
  - 🚀 个人项目
  - 🏆 荣誉与影响力
  - 🛠️ 技术栈
  - 🌟 个人特质
  - 📝 Go 后端高频面试题（真题补充）

## FILE docs/17-ai-coding-tools/README.md  (121 KB)
- 🔥 AI 编程工具与自主 Coding Agent 面试题
  - 📋 目录
  - 一、 AI 编程工具生态
  - 二、 Claude Code vs Cursor vs Copilot
  - 三、 自主 Coding Agent
  - 四、 代码智能核心技术
  - 五、 工程实践与面试话术
  - 六、低频拓展：产品与版本案例（Q12-Q49）
  - 七、新兴 AI 编程工具
  - 八、AI 编程工具评测与选型
  - 九、Claude Code 核心能力
  - 十、Claude Code 与 Cursor 的可复现对比方法
  - 十一、SWE-bench Multimodal 与 Terminal-Bench
  - 十二、Claude Code 与 Cursor 组合工作流
  - 十三、主流 AI 编程工具选型
  - 十四、AI 编程助手采用率与选型证据
  - 十五、跨会话记忆与团队上下文
  - 十六、Cline 与 Amazon Q Developer
  - 十七、Claude Code 工具结果与无头运行
  - 十八、Claude Code 与 MCP 工具生态
  - 十九、托管 Agent 与 Agent SDK
  - 二十、AI 编程工具与向量检索集成
  - 二十一、可复用的 AI 编程工作流
  - 二十二、浏览器自动化 Agent
  - 高频工程实践
  - 九、前沿评测与基准（Q52-Q56）

## FILE docs/18-big-tech-interview-questions/README.md  (78 KB)
- 🏢 国内大厂 AI 工程师面试考点整理
  - 📋 目录
  - 一、字节跳动
  - 二、阿里巴巴
  - 三、美团
  - 四、百度
  - 五、通用准备建议
  - 六、腾讯 AI 应用工程师常见考点
  - 七、公司题补充
  - 七、石头科技 AI Agent 工程题（公开面经精编）

## FILE docs/19-inference-frameworks/README.md  (47 KB)
- 🔥 大模型推理框架面试题（vLLM / SGLang / TensorRT-LLM）
  - 📋 目录
  - 一、三大推理框架概述
  - 二、核心技术对比
  - 三、性能基准对比
  - 四、选型与落地实践
  - 五、高频面试题
  - 六、推理引擎选型更新
  - 七、推理框架基准测试方法
  - 八、更多推理框架与硬件选型
  - 九、推理基础设施安全

## FILE docs/20-rag-advanced-optimization/README.md  (75 KB)
- 🚀 RAG 高级优化面试题（GraphRAG / HyDE / Semantic Chunking）
  - 📋 目录
  - 一、RAG 优化进阶概念
  - 二、语义分块与文档处理
  - 三、GraphRAG 知识图谱增强
  - 四、检索结果重排序与压缩
  - 五、RAG 评估与调优
  - 六、2026年RAG评估新趋势（新增考点）
  - 七、检索结果冲突处理
  - 八、企业知识库权限隔离
  - 九、RAG 架构演进
  - 十、RAG 前沿研究的工程价值
  - 十一、多模态 Embedding 与跨模态 RAG
  - 十二、自愈 RAG：检测与恢复
  - 十三、混合检索：BM25 + Dense 向量 + RRF 融合
  - 十四、RAG 生产实践：排查、评估、灰度与复盘
  - 十五、最新高频工程面试题（2026年新增）

## FILE docs/21-multimodal-agents/README.md  (58 KB)
- 🔥 多模态Agent面试题（Vision-Language Agent）
  - 📋 目录
  - 一、多模态Agent基础概念
  - 二、视觉语言模型核心原理
  - 三、视觉工具与Agent设计
  - 四、文档理解与OCR-Agent
  - 五、视频理解与时序Agent
  - 六、企业级实战案例
  - 七、速记卡片
  - 八、NVIDIA Nemotron 3与GTC 2026多模态Agent新突破（2026年4月新增）
  - 九、Qwen3-VL 架构案例
  - 十、GUI Agent 与 Computer Use
  - 十一、GUI Agent 数据与自适应执行
  - 十二、视觉幻觉与可信度
  - 十三、图像生成与编辑 Agent
  - 十四、空间定位与几何理解
  - 十五、音频与 VLA 整合
  - 十六、多模态评测基准与评估
  - 版本记录与更新

## FILE docs/22-agent-planning-reflection/README.md  (38 KB)
- 🧠 Agent 规划与反思深度面试题（ReAct 优化 / Reflexion / LATS）
  - 📋 目录
  - 一、从 Copilot 到 Agent：范式转变
  - 二、规划模式：ReAct 局限与优化
  - 三、反思模式：自我修正架构
  - 四、高阶架构：LATS 与 Reflexion
  - 五、工程实践与面试总结
  - 六、2026年新型 Agent 架构：Voyager 与 AutoGen v3（Q11-Q12）
  - 七、Tree of Thoughts：为什么"搜索树"是 2026 年 Agent 规划的新范式（Q15）
  - 八、生产工程：LangGraph 与 Agent 运维（Q16-Q20）

## FILE docs/23-agent-observability/README.md  (78 KB)
- 🔥 Agent 可观测性与生产监控面试题
  - 📋 目录
  - 一、为什么 Agent 需要独立的可观测性体系？
  - 二、核心监控指标体系
  - 三、面试高频追问
  - 四、速记卡片
  - 五、面试话术模板
  - 六、Voice Agent 评估新框架：EVA（Q9）
  - 七、Agent 可观测性平台选型
  - 十一、Agent 可观测性进阶专题（Q19-Q25）

## FILE docs/24-python-engineering/README.md  (40 KB)
- 📌 Python 工程基础
  - 📋 目录
  - 更新记录

## FILE docs/25-system-design-ai/README.md  (43 KB)
- 📌 AI 场景系统设计
  - 📋 目录
  - 更新记录

## FILE docs/26-forward-deployed-engineer/README.md  (25 KB)
- 🧭 FDE（Forward Deployed Engineer）面试题
  - 来源与适用范围
  - 常见考察结构
  - 目录
  - 一、岗位理解与需求发现
  - 二、问题拆解与方案设计
  - 三、AI 生产系统与评测
  - 四、编码、数据与现场调试
  - 五、客户沟通、交付与行为面试
  - 准备建议
  - 参考资料

## FILE docs/27-project-experience/README.md  (49 KB)
- 💼 AI 项目经验与深挖面试题
  - 📋 目录
  - 一、RAG系统项目
  - 二、AI Agent项目
  - 三、成本优化项目
  - 四、数据与冷启动项目
  - 五、项目回答技巧
  - 📝 速记卡片
  - 六、大厂项目架构设计（2026新增）
  - 更新记录

## FILE docs/28-test-harness-evaluation/README.md  (21 KB)
- 🧪 测试 Harness 与 LLM 评测面试题（Test Harness / Mock & Stub / Eval Harness）
  - 📋 目录
  - 一、Test Harness 基础认知
  - 二、Test Harness 工程实践 10 问（Q1-Q10）
  - 三、LLM 评测 Harness（Q11-Q16）
  - 四、Agent 运行治理与回归评测（Q17-Q19）
  - 五、加分话术与简历写法
  - 更新记录

## FILE docs/references/dive-into-llms-reading-list.md  (5 KB)
- 《动手学大模型》课件与实验阅读索引
  - 使用与版权说明
  - 1. 微调与部署（已有覆盖，按需阅读）
  - 2. Prompt 与思维链（已有覆盖，按需阅读）
  - 3. 知识编辑（高优先级）
  - 4. 数学推理蒸馏（高优先级）
  - 5. 模型水印（高优先级）
  - 6. 越狱攻击与防御评测（高优先级）
  - 7. LLM 文本隐写（选修）
  - 8. 多模态大模型（已有覆盖，按需阅读）
  - 9. GUI Agent 构建（高优先级）
  - 10. Agent 安全评测（高优先级）
  - 11. RLHF 实验（已有覆盖，按需阅读）
  - 推荐学习顺序