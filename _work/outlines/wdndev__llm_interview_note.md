# OUTLINE of wdndev__llm_interview_note


## FILE 01.大语言模型基础/README.md  (0 KB)
- 01.大语言模型基础
    - 1.1 大模型发展历程
    - 1.2 分词与词向量
    - 1.3 语言模型基础知识
    - 1.4 深度学习
    - 1.5 一些题目

## FILE 01.大语言模型基础/1.llm概念/1.llm概念.md  (7 KB)
- 1.llm概念
    - 1.目前 主流的开源模型体系 有哪些？
    - 2.prefix LM 和 causal LM 区别是什么？
    - 3.大模型LLM的 训练目标
    - 4.涌现能力是啥原因？
    - 5.为何现在的大模型大部分是Decoder only结构
    - 6.大模型架构介绍
    - 6.LLMs复读机问题
    - 7.LLMs输入句子长度理论上可以无限长吗？
    - 8.什么情况用Bert模型，什么情况用LLaMA、ChatGLM类大模型，咋选？
    - 9.各个专业领域是否需要各自的大模型来服务？
    - 10.如何让大模型处理更长的文本？

## FILE 01.大语言模型基础/1.分词/1.分词.md  (3 KB)
- 1.分词
  - **1.概述**
  - **2.中文分词难点**
    - 2.1 **分词标准**
    - 2.2 **切分歧义**
    - 2.3 **未登录词**
  - **3.中文分词算法**
    - **3.1 基于词典的分词算法**
    - **3.2 基于统计的分词算法**
  - **4.分词质量和性能**
  - **5.总结**

## FILE 01.大语言模型基础/1.激活函数/1.激活函数.md  (7 KB)
- 1.激活函数
    - 1.激活函数作用
    - 2.梯度爆炸和梯度消失
    - 3.Sigmoid
    - 4.Tanh
    - 5.ReLU系列
    - 6.GeLU
    - 7.Swish
    - 8.GLU

## FILE 01.大语言模型基础/1.语言模型/1.语言模型.md  (6 KB)
- 1.语言模型
  - 1.什么是语言模型
    - 1.1 自回归语言模型(Autoregressive language models)
    - 1.2总结
  - 2.大模型相关历史回顾
    - 2.1信息理论、英语的熵、n-gram模型
    - 2.2总结

## FILE 01.大语言模型基础/2.jieba分词用法及原理/2.jieba分词用法及原理.md  (22 KB)
- 2.jieba分词用法及原理
  - **1.概述**
    - 1.1 特点
    - 1.2 安装说明
    - 1.3 算法
  - **2.jieba分词用法**
    - **2.1 分词**
    - **2.2 添加自定义词典**
    - **2.3 调整词典**
    - **2.4 关键词提取**
    - **2.5 词性标注**
    - **2.6 并行分词**
    - **2.7 Tokenize：返回词语在原文的起止位置**
    - 2.8 命令模式
    - **2.9 延迟加载机制**
  - **3.jieba分词源码结构**
  - **4.jieba分词原理分析**
    - **4.1 初始化**
    - **4.2. 切分短语**
    - **4.3 构建DAG**
    - **4.4 构建节点最大路径概率，以及结束位置**
    - **4.5 构建切分组合**
    - **4.6 HMM新词处理**
    - **4.7 返回分词结果**
  - **5.总结**

## FILE 01.大语言模型基础/3.词性标注/3.词性标注.md  (8 KB)
- 3.词性标注
  - **1.概述**
  - **2.词性标注难点**
  - **3.词性标注算法**
    - **3.1 基于字符串匹配的字典查找算法**
    - **3.2 基于统计的词性标注算法**
  - **4.jieba词性标注原理**
    - **4.1 准备工作**
    - **4.2 遍历语句，进行分词和词性标注**
    - **4.3 未登录词，HMM隐马尔科夫模型处理**
  - **5.总结**

## FILE 01.大语言模型基础/4.句法分析/4.句法分析.md  (1 KB)
- 4.句法分析
  - **1.概述**
  - **2.句法分析分类**
    - **2.1 句法结构分析**
    - **2.2 语义依存关系分析**
  - **3.句法分析工具**
  - **4.深度学习和句法分析**
  - **5.总结**

## FILE 01.大语言模型基础/5.词向量/5.词向量.md  (9 KB)
- 5.词向量
  - **1.概述**
  - **2.词向量工具**
    - **2.1 模型训练**
    - **2.2 增量训练**
    - **2.3 求词语相似度**
    - **2.4 求与词语相近的多个词语**
  - **3.词向量训练算法**
  - **4.词向量训练代码实现**
  - **5.总结**

## FILE 01.大语言模型基础/LLM为什么Decoder only架构/LLM为什么Decoder only架构.md  (2 KB)
- LLM为什么Decoder only架构
    - 1.Encoder的低秩问题
    - 2.更好的Zero-Shot性能、更适合于大语料自监督学习
    - 3.效率问题

## FILE 01.大语言模型基础/NLP三大特征抽取器（CNN-RNN-TF）/NLP三大特征抽取器（CNN-RNN-TF）.md  (1 KB)
- NLP三大特征抽取器（CNN/RNN/TF）

## FILE 01.大语言模型基础/NLP面试题/NLP面试题.md  (6 KB)
- NLP面试题
    - 1.BERT
    - 2.文本嵌入
    - 3.对比BERT、OpenAI GPT、ELMo架构之间的差异
    - 4.Word2Vec中为什么使用负采样（negtive sample）？
    - 5.word2vec 相比之前的 Word Embedding 方法好在什么地方？
    - 6.NLP预训练发展史：从Word Embedding到BERT
    - 7.NLP三大特征抽取器（CNN/RNN/TF）
    - 8.常用参数更新方法

## FILE 01.大语言模型基础/Word2Vec/Word2Vec.md  (4 KB)
- Word2Vec
  - 1.Word2Vec概述
  - 2.Word2Vec原理
  - **3.CBOW**
  - **4.Skip-gram**
  - 5.Hierarchical Softmax
  - 6.Negative Sampling

## FILE 02.大语言模型架构/README.md  (1 KB)
- 02.大语言模型架构
    - 2.1 Transformer模型
    - 2.2 注意力
    - 2.3 解码部分
    - 2.4 BERT
    - 2.5 常见大模型
    - 2.6 MoE

## FILE 02.大语言模型架构/1.attention/1.attention.md  (18 KB)
- 1.attention
    - 1.Attention
    - 2.Transformer
    - 3.BERT
    - 4.MHA & MQA & MGA
    - 5.Flash Attention&#x20;
    - 6.Transformer常见问题

## FILE 02.大语言模型架构/1.MoE论文/1.MoE论文.md  (6 KB)
- 1.MoE论文
  - 1.摘要
  - 2.介绍和相关工作
    - 2.1 条件计算
    - 2.2 本文方法：稀疏门控专家混合层
  - 3.混合专家层的结构
    - 3.1 MoE层
    - 3.2 层次化MoE
    - 3.3 门控网络
    - 3.4训练门控网络
  - 4.解决性能挑战
    - 4.1 批量减小问题（The Shrinking Batch Problem）
    - 4.2 网络带宽
  - 5.平衡专家的利用率
  - 6.实验
    - 6.1 10 亿词汇的语言建模基准
    - 6.2 1000 亿词汇的谷歌新闻语料库
    - 6.3 机器翻译
  - 7.结论

## FILE 02.大语言模型架构/2.layer_normalization/2.layer_normalization.md  (6 KB)
- 2.layer\_normalization
    - 1.**Normalization**
    - 2. BN & LN & IN & GN
    - 3.Post-LN 和 Pre-LN

## FILE 02.大语言模型架构/2.MoE经典论文简牍/2.MoE经典论文简牍.md  (15 KB)
- 2.MoE经典论文简牍
  - 1.开创工作
    - 1.1 Adaptive mixtures of local experts, Neural Computation'1991
    - 1.2 Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer, ICLR'17
  - 2.使用 MoE 开发超大模型
    - 2.1 GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding, ICLR'21
    - 2.2 Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity, JMLR'22
    - 2.3 GLaM: Efficient Scaling of Language Models with Mixture-of-Experts, 2021
    - 2.4 小结
  - 3.使用 MoE 来使模型轻量化
    - 3.1 Go Wider Instead of Deeper, AAAI'22
    - 3.2 MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation, NAACL'22
  - 4.ST-MOE
    - 4.1 用 Router z-loss 稳定模型训练
    - 4.2 专家如何学习？
    - 4.3 专家的数量对预训练有何影响？
    - 4.4 Fine-Tuning MoE 模型
  - 5.结语

## FILE 02.大语言模型架构/3.LLM MoE ：Switch Transformers/3.LLM MoE ：Switch Transformers.md  (12 KB)
- 3.LLM MoE ：Switch Transformers
  - 0.前言
  - 1.什么是MoE大模型？
  - 2.MoE大模型具备哪些优势？
  - 3.Switch Transformers
    - 3.1 Switch Transformer 主要优化
    - 3.2 Switch Routing
    - 3.3 不同的负载均衡损失
    - 3.4 稀疏路由和负载均衡loss的合并效果
    - 3.5 改进训练和Fine-Tuning技术
    - 3.6 高效训练：数据、模型、专家并行
  - 4.总结

## FILE 02.大语言模型架构/3.位置编码/3.位置编码.md  (18 KB)
- 3.位置编码
    - 1.位置编码
    - 2.旋转位置编码 RoPE篇
    - 3.ALiBi (Attention with Linear Biases)篇
    - 4.长度外推问题篇

## FILE 02.大语言模型架构/4.tokenize分词/4.tokenize分词.md  (6 KB)
- 4.tokenize分词
    - 0.总览
    - 1.背景与基础
    - 2.常用的tokenize算法

## FILE 02.大语言模型架构/5.token及模型参数/5.token及模型参数.md  (5 KB)
- 5.token及模型参数
    - 1.**预训练模型表现影响因素**
    - 2.预训练数据 Token 重复 是否影响 模型性能？
    - 3.SFT需要训练Token数？
    - 4.为什么要考虑在重复的数据集上做多次训练？
    - 5.预训练数据集重复的影响是什么？
    - 6.影响多次Epochs训练效果下降的原因是什么？
    - 7.正则化可以降低多epochs的影响吗
    - 8.多epochs训练对大语言模型性能影响的总结

## FILE 02.大语言模型架构/6.激活函数/6.激活函数.md  (4 KB)
- 6.激活函数
    - 1.介绍一下 FFN 块 计算公式？
    - 2.介绍一下 GeLU 计算公式？
    - 3.介绍一下 Swish 计算公式？
    - 4.介绍一下 使用 GLU 线性门控单元的 FFN 块 计算公式？
    - 5.介绍一下 使用 GeLU 的 GLU 块 计算公式？
    - 6.介绍一下 使用 Swish 的 GLU 块 计算公式？

## FILE 02.大语言模型架构/bert变种/bert变种.md  (7 KB)
- bert变种
    - 1.RoBERTa
    - 2.ALBERT
    - 3.spanBERT
- 4.XLNet
    - 5.AR和AE

## FILE 02.大语言模型架构/bert细节/bert细节.md  (10 KB)
- bert细节
  - 1.背景结构
    - 1.1 基础知识
    - 1.2 BERT与其他模型相比
    - 1.3 BERT，GPT，ELMo
    - 1.4 与Transformer区别
    - 1.5 word2vec到BERT改进了什么
  - 2.模型结构
    - 2.1 两个任务
    - 2.2 Embedding
  - 3.模型细节
    - 3.1 BERT在第一句前会加一个\[CLS]标志
    - 3.2 BERT的三个Embedding直接相加会对语义有影响吗
    - 3.3 BERT如何区分一词多义？
    - 3.4 BERT中Normalization结构：**LayerNorm**
    - 3.5 为什么说ELMO是伪双向，BERT是真双向？
    - 3.6 BERT和Transformer Encoder的差异有哪些？
    - 3.7 Scaled Dot Product:为什么是缩放点积，而不是点积模型？
    - 3.8 FFN的作用？
    - 3.9 BERT非线性的来源
    - 3.10 MLM任务，对于在数据中随机选择 15% 的标记，其中80%被换位\[mask]，10%不变、10%随机替换其他单词，原因是什么？
    - 3.11其mask相对于CBOW有什么异同点？
    - 3.12 对于长度较长的语料，如何训练？
  - 4.BERT损失函数
  - 5.模型优缺点和局限性
    - 5.1 BERT优点
    - 5.2 BERT缺点
    - 5.3 BERT局限性

## FILE 02.大语言模型架构/chatglm系列模型/chatglm系列模型.md  (10 KB)
- chatglm系列模型
- 1.ChatGLM
  - 1.1 背景
  - 1.2 GLM预训练框架
    - （1）自回归空格填充任务
    - （2）多目标预训练
    - （3）模型结构
    - （4）GLM微调
- 2.ChatGLM-2
  - 2.1 主要创新
  - 2.2 与ChatGLM的变化
- 3.ChatGLM-3
- 4.模型架构比较

## FILE 02.大语言模型架构/llama 2代码详解/llama 2代码详解.md  (21 KB)
- llama 2代码详解
  - **0.前言**
  - **1.处理流程**
    - 1.1 常见大模型处理流程
    - **1. 2 Code**
  - **2.模型结构**
    - **2.1 RMSNorm**
    - **2.2.RoPE**
    - **2.3.KV Cache & GQA**
    - **2.4 FeedForward**
    - **参考资料**

## FILE 02.大语言模型架构/llama 3/llama 3.md  (4 KB)
- llama 3
  - 0.简介
  - 1.改进亮点
  - 2.模型架构
    - 2.1 通用GPT架构
    - 2.2 llama3改进
  - 3.数据工程
  - 4.训练方法
  - 5.指令微调优化
  - 6.性能
    - 6.1 预训练模型性能
    - 6.2 指令微调模型性能
    - 6.3 人工评估结果
  - 7.LLaMA3-400B 正在训练中

## FILE 02.大语言模型架构/llama系列模型/llama系列模型.md  (9 KB)
- llama系列模型
- 1.LLama
  - 1.1 简介
  - 1.2 RMSNorm归一化函数
  - 1.3 SwiGLU激活函数
  - 1.4 旋转位置嵌入（RoPE）
- 2.Alpaca
  - 2.1 简介
  - 2.2 微调方法
  - 2.3 Self-instruct数据构造
  - 2.4 指令数据格式
- 3.Llama-2
  - 3.1 简介
  - 3.2 GQA
  - 3.3 源码
- 4.Code Llama
  - 4.1 简介
  - 4.2 模型训练流程
  - 4.3 Code Infilling Task （7B/13B only）
- 5.总结

## FILE 02.大语言模型架构/MHA_MQA_GQA/MHA_MQA_GQA.md  (7 KB)
- MHA\_MQA\_GQA
  - 1.总结
  - 2.代码实现
    - 2.1 MHA
    - 2.2 MQA
    - 2.3 GQA

## FILE 02.大语言模型架构/Transformer架构细节/Transformer架构细节.md  (12 KB)
- Transformer架构细节
  - 1.Transformer各个模块的作用
    - （1）Encoder模块&#x20;
    - （2）Decoder模块 &#x20;
    - （3）Add & Norm模块 &#x20;
    - （4）位置编码器Positional Encoding &#x20;
  - 2.Decoder端训练和预测的输入
  - 3.Self-attention
    - （1）self-attention的机制和原理
    - （2）关于self-attention为什么要使⽤(Q, K, V)三元组⽽不是其他形式
  - 4.Self-attention归一化和放缩
    - （1）self-attention中的归⼀化概述
    - （2）softmax的梯度变化
    - （3）维度与点积大小的关系
  - 5.Multi-head Attention
    - （1）采⽤Multi-head Attention的原因 &#x20;
  - 6.Transformer和RNN
    - （1）Transformer的并行计算 &#x20;
    - （2）Transformer的特征抽取能力&#x20;
  - 7.Transformer代替seq2seq？
    - （1）seq2seq的两大缺陷 &#x20;
    - （2）Transformer的改进 &#x20;
  - 8.Transformer并行化
    - （1）Encoder并行化
    - （2）Decoder的并行化
    - （3）总结

## FILE 02.大语言模型架构/解码策略（Top-k & Top-p & Temperatu/解码策略（Top-k & Top-p & Temperature）.md  (7 KB)
- 解码策略（Top-k & Top-p & Temperature）
  - 0.简介
  - 2.top-k采样
  - 3.top-p采样
  - 3.Temperature采样
  - 4.联合采样（top-k & top-p & Temperature）

## FILE 03.训练数据集/README.md  (0 KB)
- 03.训练数据集
    - 3.1 数据集
    - 3.2 模型参数

## FILE 03.训练数据集/数据格式/数据格式.md  (4 KB)
- 数据格式
    - 1.SFT（有监督微调）的数据集格式？
    - 2.RM（奖励模型）的数据格式？
    - 3.PPO（强化学习）的数据格式？
    - 4.找数据集哪里找？
    - 5.微调需要多少条数据？
    - 6.有哪些大模型的训练集？
    - 7.进行领域大模型预训练应用哪些数据集比较好？

## FILE 04.分布式训练/README.md  (1 KB)
- 04.分布式训练
    - 4.1 基础知识
    - 4.2 DeepSpeed
    - 4.3 Megatron
    - 4.4 训练加速
    - 4.5 一些有用的文章
    - 4.6 一些题目
    - 4.7 参考资料：

## FILE 04.分布式训练/1.显存问题/1.显存问题.md  (1 KB)
- 1.显存问题
    - 1. 大模型大概有多大，模型文件有多大?
    - 2. 能否用4 \* v100 32G训练vicuna 65b？
    - 3.如何评估你的显卡利用率?
    - 4. 如何查看多机训练时的网速？
    - 5. 如何查看服务器上的多卡之间的NVLINK topo？
    - 6. 如何查看服务器上显卡的具体型号?
    - 7. 如何查看训练时的 flops？（也就是每秒的计算量）
    - 8. 如何查看对 deepspeed 的环境配置是否正确？
    - 9. TF32 格式有多长？

## FILE 04.分布式训练/1.概述/1.概述.md  (3 KB)
- 1.概述
    - 1.数据并行
    - 2.模型并行
    - 3.优化器相关的并行
    - 4.异构系统并行
    - 5.多维混合并行
    - 6.自动并行
    - 7.MOE并行/专家并行

## FILE 04.分布式训练/2.数据并行/2.数据并行.md  (10 KB)
- 2.数据并行
    - 1.简述
    - 2.数据并行（PyTorch DP）
    - 3.分布式数据并行 **（PyTorch DDP）**
    - 4.完全分片数据并行 **(PyTorch FSDP)**
    - 5.总结

## FILE 04.分布式训练/3.流水线并行/3.流水线并行.md  (11 KB)
- 3.流水线并行
    - 1.简介
    - 2.朴素流水线并行
    - 3.微批次流水线并行
    - 4.GPipe
    - 5.流水线并行策略
    - 6.PipeDream（非交错式1F1B）-DeepSpeed
    - 7.PipeDream-2BW
    - 8.PipeDream-Flush（1F1B）
    - 9.1F1B 调度（schedule）模式
    - 10.PipeDream（交错式1F1B）-Megatron-LM
    - 11.分布式训练框架流水线并行方案
    - 12.总结

## FILE 04.分布式训练/4.张量并行/4.张量并行.md  (14 KB)
- 4.张量并行
    - 1.简述
    - 2.张量并行方式
    - 2.2 列并行
    - 3. 1维（1D）张量并行（Megatron-LM）
    - 4.多维张量并行
    - 5.Pytorch中的张量并行
    - 6.总结

## FILE 04.分布式训练/5.序列并行/5.序列并行.md  (4 KB)
- 5.序列并行
    - 1.序列并行（Colossal-AI）
    - 2.序列并行
    - 3.Pytorch中的序列并行
    - 4.总结

## FILE 04.分布式训练/6.多维度混合并行/6.多维度混合并行.md  (5 KB)
- 6.多维度混合并行
    - 1.常见的分布式并行技术组合
    - 2.业界大模型混合并行策略
    - 3.总结

## FILE 04.分布式训练/7.自动并行/7.自动并行.md  (10 KB)
- 7.自动并行
    - 1.**简述**
    - 2.**Mesh-TensorFlow**
    - 3.**GSPMD**
    - 4.**Flexflow**
    - 5.**Alpa**

## FILE 04.分布式训练/8.moe并行/8.moe并行.md  (8 KB)
- 8.moe并行
    - 1.MOE
    - 2.MOE分布式并行策略
    - 3.业界大模型的MOE并行方案
    - 4.AI训练框架中的MOE并行训练
    - 5.总结

## FILE 04.分布式训练/9.总结/9.总结.md  (4 KB)
- 9.总结
    - 1.数据并行
    - 2.流水线并行
    - 3.张量并行
    - 4.序列并行
    - 5.多维混合并行
    - 6.自动并行
    - 7.MOE并行
    - 8.分布式训练并行策略选择
    - 9.大模型混合进度训练FP16 与 BF16 的对比

## FILE 04.分布式训练/deepspeed介绍/deepspeed介绍.md  (24 KB)
- deepspeed介绍
  - 1.为什么需要Deepspeed
    - **1.1 基本概念**
    - **1.2 通信策略**
    - 1.3 DeepSpeed训练介绍
  - **2. Zero（3D优化与卸载）**
    - **2.1 三个级别**
    - **2.2 混合精度**
    - **2.3 显存占用分析**
  - **3.ZeRO-DP**
    - **3.1 ZeRO-DP的细节**
    - 3.2 **ZeRO-DP通信量**
  - **4.DeepSpeed训练**
    - 4.1 基本训练的介绍
    - 4.2 训练实战介绍
    - 4.3 deepspeed加速Bloom lora微调

## FILE 04.分布式训练/分布式训练题目/分布式训练题目.md  (13 KB)
- 分布式训练题目
    - 1. 理论篇
    - 2. 实践篇
    - 3. 并行化策略选择篇

## FILE 05.有监督微调/README.md  (0 KB)
- 05.有监督微调
    - 5.1 理论
    - 5.2 微调实战
    - 5.3 一些题目

## FILE 05.有监督微调/1.基本概念/1.基本概念.md  (3 KB)
- 1.基本概念
    - 1.微调方法是啥？如何微调？
    - 2.为什么需要 PEFT？
    - 3.微调和参数高效微调之间的区别是什么?
    - 4.PEFT 有什么优点？
    - 5.多种不同的高效微调方法对比
    - 6.当前高效微调技术存在的一些问题
    - 7.高效微调技术最佳实践

## FILE 05.有监督微调/1.微调/1.微调.md  (13 KB)
- 1.微调
    - 1.如果想要在某个模型基础上做全参数微调，究竟需要多少显存？
    - 2.为什么SFT之后感觉LLM傻了?
    - 3.SFT 指令微调数据 如何构建?
    - 4.领域模型Continue PreTrain 数据选取？
    - 5.领域数据训练后，通用能力往往会有所下降，如何缓解模型遗忘通用能力？
    - 6.领域模型Continue PreTrain ，如何 让模型在预训练过程中就学习到更多的知识？
    - 7.进行SFT操作的时候，基座模型选用Chat还是Base?
    - 8.领域模型微调 指令 & 数据输入格式 要求？
    - 9.领域模型微调 领域评测集 构建？
    - 10.领域模型词表扩增是不是有必要的？
    - 11.如何训练自己的大模型？
    - 12.指令微调的好处？
    - 13.预训练和微调哪个阶段注入知识的？
    - 14.想让模型学习某个领域或行业的知识，是应该预训练还是应该微调？
    - 15.多轮对话任务如何微调模型？
    - 16.微调后的模型出现能力劣化，灾难性遗忘是怎么回事？
    - 17.预训练和SFT操作有什么不同
    - 18.样本量规模增大，训练出现OOM错
    - 19.大模型LLM进行SFT 如何对样本进行优化？
    - 20.模型参数迭代实验

## FILE 05.有监督微调/2.prompting/2.prompting.md  (6 KB)
- 2.prompting
    - 1.BitFit
    - 2.Prefix Tuning
    - 3.Prompt Tuning
    - 4.**P-Tuning**
    - 5.**P-Tuning** v2

## FILE 05.有监督微调/2.预训练/2.预训练.md  (1 KB)
- 2.预训练
    - 1. 为什么要增量预训练？
    - 2. 进行增量预训练需要做哪些准备工作？
    - 3. 增量预训练所用训练框架？
    - 4. 增量预训练数据选取思路有哪些？
    - 5. 增量预训练训练流程是怎么样？

## FILE 05.有监督微调/3.adapter-tuning/3.adapter-tuning.md  (6 KB)
- 3.adapter-tuning
    - 1.Adapter Tuning
    - 2.AdapterFusion
    - 3.AdapterDrop
    - 4.MAM Adapter
    - 5.UniPELT

## FILE 05.有监督微调/4.lora/4.lora.md  (4 KB)
- 4.lora
    - 1.LoRA
    - 2.AdaLoRA
    - 3.QLoRA

## FILE 05.有监督微调/5.总结/5.总结.md  (2 KB)
- 5.总结
    - 1.**当前高效微调技术的简述**
    - 2.**BitFit**
    - 3.**Prefix Tuning**
    - 4.**Prompt Tuning**
    - 5.**P-Tuning**
    - 6.**P-Tuning v2**
    - 7.**Adapter Tuning**
    - 8.**AdapterFusion**
    - 9.**AdapterDrop**
    - 10.**LoRA**
    - 11.**AdaLoRA**
    - 12.**QLoRA**
    - 13.**MAM Adapter**
    - 14.**UniPELT**
    - 15.**多种不同的高效微调方法对比**
    - 16.**总结**

## FILE 05.有监督微调/ChatGLM3微调/ChatGLM3微调.md  (0 KB)
- ChatGLM3微调

## FILE 05.有监督微调/llama2微调/llama2微调.md  (0 KB)
- llama2微调

## FILE 06.推理/README.md  (0 KB)
- 06.推理
    - 6.1 推理框架
    - 6.2 推理优化技术
    - 6.3 量化
    - 6.4 vLLM
    - 6.5 一些题目

## FILE 06.推理/0.llm推理框架简单总结/0.llm推理框架简单总结.md  (12 KB)
- 0.llm推理框架简单总结
    - **1.vLLM**
    - **2.Text generation inference**
    - **3.CTranslate2**
    - 3.1 使用
    - **4.DeepSpeed-MII**
    - **5.OpenLLM**
    - **6.Ray Serve**
    - **7.MLC LLM**

## FILE 06.推理/1.vllm/1.vllm.md  (8 KB)
- 1.vllm
    - 1.Overview
    - 2.LLM Decoder推理基础
    - 3.LLM batching
    - 4.continus batching
    - 5.PagedAttention
    - 6.vLLM源码学习

## FILE 06.推理/1.推理/1.推理.md  (4 KB)
- 1.推理
    - 1.为什么大模型推理时显存涨的那么多还一直占着？
    - 2.大模型在GPU和CPU上推理速度如何？
    - 3.推理速度上，INT8和FP16比起来怎么样？
    - 4.大模型有推理能力吗？
    - 5.大模型生成时的参数怎么设置？
    - 6.有哪些省内存的大语言模型训练/微调/推理方法？
    - 7.如何让大模型输出合规化
    - 8.应用模式变更

## FILE 06.推理/2.text_generation_inference/2.text_generation_inference.md  (5 KB)
- 2.text\_generation\_inference
    - **1.简介**
    - 2.**主要特性**
    - 3.**支持的模型**
    - 4.**适用场景**
    - 5.项目架构

## FILE 06.推理/3.faster_transformer/3.faster_transformer.md  (3 KB)
- 3.faster\_transformer
    - 1.**简介**
    - 2.**FasterTransformer 中的优化技术**
    - 3.**支持的模型**
    - 4.**存在的问题**

## FILE 06.推理/4.trt_llm/4.trt_llm.md  (0 KB)
- 4.trt\_llm

## FILE 06.推理/llm推理优化技术/llm推理优化技术.md  (10 KB)
- llm推理优化技术
- 1.理解LLM推理
  - 1.1 预填充阶段或处理输入
  - 1.2 解码阶段或生成输出
  - 1.3 批处理（Batching）
  - 1.4 KV缓存
  - 1.5 LLM内存需求
- 2.模型并行化扩展LLM
  - 2.1 Pipeline并行
  - 2.2 Tensor并行
  - 2.3 Sequence并行
- 3.注意力机制优化
  - 3.1 多头注意力（MHA）
  - 3.2 多查询注意力（MQA）
  - 3.3 分组注意力（GQA）
  - 3.4 Flash attention
- 4.KV缓存的分页高效管理
- 5.模型优化技术
  - 5.1 量化（Quantization）
  - 5.2 稀疏（Sparsity）
  - 5.3 蒸馏（Distillation）
- 6.模型服务技术
  - 6.1 动态批处理（**In-flight batching**）
  - 6.2 预测推理（**Speculative inference**）
- 7.结论

## FILE 06.推理/LLM推理常见参数/LLM推理常见参数.md  (9 KB)
- LLM 推理常见参数
  - 1.引言 &#x20;
  - 2.背景介绍
  - 3.Greedy Search
  - 4.Beam Search
  - 5.top\_k
  - 6.top\_p
  - 7.temperature
  - 8.repetition\_penalty（重复惩罚）
  - 9.总结

## FILE 07.强化学习/README.md  (0 KB)
- 07.强化学习
    - 7.1 强化学习原理
    - 7.2 RLHF
    - 7.3 一些题目

## FILE 07.强化学习/1.rlhf相关/1.rlhf相关.md  (7 KB)
- 1.rlhf相关
    - 1.简单介绍强化学习？
    - 2.简单介绍一下 RLHF？
    - 3.奖励模型需要和基础模型一致吗？
    - 4.RLHF 在实践过程中存在哪些不足？
    - 5.如何解决 人工产生的偏好数据集成本较高，很难量产问题？
    - 6. 如何解决三个阶段的训练（SFT->RM->PPO）过程较长，更新迭代较慢问题？
    - 7. 如何解决 PPO 的训练过程同时存在4个模型（2训练，2推理），对计算资源的要求较高 问题？
    - 8.基于人类反馈的强化学习流程
    - 9. 什么是 LLM Agent?
    - 10. LLM Agent 有什么关键能力？
    - 11. 怎样构建基于 LLM 的 Agents？
    - 12. LLM Agents 有哪些类型？
    - 13. 是什么让Agent有了自制的能力？
    - 14.如何给LLM注入领域知识？

## FILE 07.强化学习/2.强化学习/2.强化学习.md  (19 KB)
- 2.强化学习
  - 1.RL基础
  - 2.马尔可夫决策过程
  - 3.表格型方法
  - 4.DQN
  - 5.策略梯度
  - 6.演员-评论家算法
  - 7.DDPG算法
  - 8.PPO算法
  - 9.稀疏奖励
  - 10.模仿学习

## FILE 07.强化学习/DPO/DPO.md  (5 KB)
- DPO
    - 1.简介
    - 2.RLHF pipeline
    - 3.直接偏好优化（DPO）
    - 4.实验
    - 5.结论

## FILE 07.强化学习/大模型RLHF：PPO原理与源码解读/大模型RLHF：PPO原理与源码解读.md  (22 KB)
- 大模型RLHF：PPO原理与源码解读
  - 1.强化学习概述 &#x20;
    - 1.1 强化学习整体流程 &#x20;
    - 1.2 价值函数
  - 2.NLP中的强化学习
  - 3.RLHF中的四个重要角色
    - 3.1 Actor Model (演员模型)
    - 3.2 Reference Model（参考模型）
    - 3.3 Critic Model（评论家模型）
    - 3.4 Reward Model（奖励模型）
  - 4.RLHF中的loss计算
    - 4.1 Actor loss
    - （1）直观设计
    - （2）引入优势（Advantage）
    - （3）重新设计 $R_{t}$
    - （4）重新设计优势
    - （5）PPO-epoch: 引入新约束
    - （6）Actor loss小结
    - 4.2 Critic loss
    - （1）实际收益优化
    - （2）预估收益优化

## FILE 07.强化学习/策略梯度（pg）/策略梯度（pg）.md  (14 KB)
- 策略梯度（pg）
  - 0.引言
  - 1. 蒙特卡罗
  - 2. 策略梯度算法
    - 2.1 简介
    - 2.2 算法内容
    - 2.3 技巧
  - 3.代码实现
  - 4.总结
  - 5.参考文献

## FILE 07.强化学习/近端策略优化(ppo)/近端策略优化(ppo).md  (18 KB)
- 近端策略优化(ppo)
  - 0.引言
  - 1. 同策略的不足之处
  - 2. 改进同策略的思路
  - 3. 同策略到异策略的具体实现
  - 4. PPO
    - 4.1 TRPO
    - 4.2 PPO算法的两个主要变种
  - 5. 代码实现
  - 6. 总结
  - 7. 参考文献

## FILE 08.检索增强rag/README.md  (0 KB)
- 08.检索增强rag
    - 8.1 RAG
    - 8.2 Agent

## FILE 08.检索增强rag/rag（检索增强生成）技术/rag（检索增强生成）技术.md  (4 KB)
- rag（检索增强生成）技术
- 1.基本概念
- 2.RAG解决的问题
    - （1）长尾知识：
    - （2）私有数据
    - （3）数据新鲜度
    - （4）来源验证和可解释性
- 3.RAG关键模块
- 4.几种RAG的调用模式
- 5.RAG vs. SFT

## FILE 08.检索增强rag/大模型agent技术/大模型agent技术.md  (22 KB)
- 大模型agent技术
  - 1. LLM Agents综述
    - 1.1 Prompt工程
    - 1.2 Prompt外挂
    - 1.3 分解与组合
    - 1.4 反馈
    - 1.5 Agent
    - 1.6 Multi-Agent
    - 1.7 简单的难题
  - 2. 通用智能基本原理
  - 3. 面向目标架构
  - 4. 前瞻性分析
    - 4.1 Central Executive
    - 4.2 Memory
    - 4.3 Sensory
    - 4.4 Motor
    - 4.5 Learning
    - 4.6 World Models
  - 参考文章

## FILE 08.检索增强rag/检索增强llm/检索增强llm.md  (26 KB)
- 检索增强llm
- 1.RAG基本概念
  - 1.1 什么是检索增强 LLM
  - 1.2 检索增强 LLM 解决的问题
    - （1）长尾知识
    - （2）私有数据
    - （3）数据新鲜度
    - （4）来源验证和可解释性
- 2.关键模块
  - 2.1 数据和索引模块
    - （1）数据获取
    - （2）文本分块
    - （3）数据索引
  - 2.2查询和检索模块
    - （1）查询变换
    - （2）排序和后处理
  - 2.3 回复生成模块
    - （1）回复生成策略
    - （2）回复生成 Prompt 模板
- 3.案例分析和应用
  - 3.1 ChatGPT 检索插件
  - 3.2 LlamaIndex 和 LangChain
  - 3.3 Github Copilot 分析
  - 3.4 文档和知识库的检索与问答
- 4.参考

## FILE 09.大语言模型评估/README.md  (0 KB)
- 09.大语言模型评估
    - 9.1 模型评估
    - 9.2 LLM幻觉

## FILE 09.大语言模型评估/1.大模型幻觉/1.大模型幻觉.md  (3 KB)
- 1.大模型幻觉
    - 1.什么是大模型幻觉？
    - 2.为什么需要解决LLM的幻觉问题？
    - 3.幻觉一定是有害的吗？
    - 4.幻觉有哪些不同类型？
    - 5.为什么LLM会产生幻觉？
    - 6.如何度量幻觉？
    - 7.如何缓解LLM幻觉？
    - 8.LLMs什么时候最容易产生幻觉？

## FILE 09.大语言模型评估/1.评测/1.评测.md  (1 KB)
- 1.评测
    - 1. 大模型怎么评测？
    - 2. 大模型的 honest 原则是如何实现的？模型如何判断回答的知识是训练过的已知的知识，怎么训练这种能力？
    - 3. 如何衡量大模型水平？
    - 4. 大模型评估方法有哪些？
    - 5. 大模型评估工具有哪些？

## FILE 09.大语言模型评估/2.幻觉来源与缓解/2.幻觉来源与缓解.md  (4 KB)
- 2.幻觉来源与缓解
  - 1.幻觉分类
    - 1.1 事实性问题（Factuality）
    - 1.2 忠诚度问题（Faithfulness）
    - 1.3 自我矛盾（self-Contradiction）
  - 2.幻觉检测
    - 2.1 事实性检测
    - 2.2 忠诚度检测
  - 3.幻觉来源
    - 3.1 来自数据的幻觉
    - 3.2 来自训练的幻觉
    - 3.3 来自推理的幻觉
  - 4.幻觉缓解
    - 4.1 数据幻觉
    - 4.2 训练幻觉
    - 4.3 推理幻觉

## FILE 10.大语言模型应用/README.md  (0 KB)
- 10.大语言模型应用
    - 10.1 思维链提示
    - 10.2 LangChain框架

## FILE 10.大语言模型应用/1.langchain/1.langchain.md  (13 KB)
- 1.langchain
    - 1.什么是 LangChain?
    - 2. LangChain 包含哪些核心模块
    - 3.一些核心概念
    - 4.什么是 LangChain Agent?
    - 5. 什么是 LangChain model?
    - 6. LangChain 包含哪些特点?
    - 7.LangChain 如何使用?
    - 8.LangChain知识问答实践

## FILE 10.大语言模型应用/1.思维链（cot）/1.思维链（cot）.md  (4 KB)
- 1.思维链（cot）
    - 1.什么是思维链提示？
    - 2.思维链提示本质是什么？
    - 3.思维链提示 与 标准的提示学习方法有什么不同?
    - 4.思维链提示 为什么可以提高语言模型的复杂推理能力?它的优势在哪里?
    - 5.思维链提示 适用场景 有 哪些？
    - 6.思维链提示 目前还存在哪些不足点？
    - 7.思维链提示 对推动语言模型复杂推理能力研究有哪些启发和影响?
    - 8.如何通过增加模型规模来获得语言模型强大的思路链推理能力的?这与模型获得的哪些能力有关?
    - 9.你认为可以在哪些其他方面应用“思路链提示”这一思路来提升语言模型的能力?
    - 10.这篇论文仍有哪些可以改进之处
    - 11.你认为关键的未来研究方向是什么?

## FILE 98.相关课程/README.md  (0 KB)
- 98.相关课程

## FILE 98.相关课程/清华大模型公开课/清华大模型公开课.md  (0 KB)
- 清华大模型公开课
  - 大模型基础知识
  - 大模型关键技术

## FILE 98.相关课程/清华大模型公开课/1.NLP&大模型基础/1.NLP&大模型基础.md  (4 KB)
- 1.NLP&大模型基础
- 1.自然语言处理
  - 1.1 基础与应用
    - （1）图灵测试
    - （2）NLP任务
  - 1.2 词表示
    - （1）词表示
    - （2）用一组相关的词表示
    - （3）one-hot表示
    - （4）上下文表示
    - （5）词嵌入
  - 1.3 语言模型
  - 1.4 N-gram Model
  - 1.5 神经语言模型
- 2.大模型基础
  - 2.1 大模型之旅
    - （1）预训练大模型PLM
    - （2）大模型的特点
  - 2.2 大模型背后的范式
    - （1）预训练 + 微调
    - （2）词嵌入Word2Vec
    - （3）解决一词多义：ELMo
    - （4）Transformer

## FILE 98.相关课程/清华大模型公开课/2.神经网络基础/2.神经网络基础.md  (9 KB)
- 2.神经网络基础
- 1.神经网络组成部分
  - 1.1 神经网络
    - （1）神经元
    - （2）单层神经网络
    - （3）多层神经网络
  - 1.2 激活函数
    - （1）Sigmoid
    - （2）Tanh
    - （3）ReLU
  - 1.3 输出层
- 2.训练方式
  - 2.1 训练目标
    - （1）均方根误差
    - （2）交叉熵
  - 2.2 随机梯度下降
    - （1）梯度
    - （2）链式求导法则
  - 2.3 反向传播
    - （1）计算图
    - （2）单个结点
    - （3）示例
- 3.词表示：Word2Vec
  - 3.1 Word2Vec
  - 3.2 滑动窗口
  - 3.3 CBOW（Continuous Bag-of-Words）
  - 3.4 Continuous Skip-Gram
  - 3.5 Softmax存在问题
  - 3.6 负采样
  - 3.7 其他一些细节
    - （1）Sub-Sampling
    - （2）Soft sliding window
- 4.通用神经网络
  - 4.1 RNN
    - （1）顺序记忆
    - （2）RNN
    - （3）RNN单元
    - （4）RNN语言模型
    - （5）优缺点
    - （6）梯度问题
    - （7）RNN变种
  - 4.2 GRU（Gated Recurrent Unit）
  - 4.3 LSTM（Long Short-Term Memory network）
    - （1）状态单元 $C_t$
    - （2）遗忘门$f_t$
    - （3）输入门 $i_t$
    - （4）输出门$o_t$
  - 4.4 双向RNN
  - 4.5 CNN

## FILE 98.相关课程/清华大模型公开课/3.Transformer基础/3.Transformer基础.md  (7 KB)
- 3.Transformer基础
- 1.Transformer
  - 1.1 注意力机制
    - （1）Seq2Seq注意力
    - （2）Seq2Seq注意力机制
    - （3）注意力机制的变体
    - （4）注意力通用定义
    - （5）注意力机制的特点
  - 1.2 Transformer结构
    - （1）总览
    - （2）Input Encoding
    - （3）Transformer Block
    - （4）Trick
    - （5）优缺点
- 2.PLM（Pretrained Language Models）
  - 2.1 语言模型
  - 2.2 PLMs（Pre-trained Langue Models）
    - （1）GPT
    - （2）BERT
  - 2.3 Masked LM的应用
    - （1）跨语言LM预训练
    - （2）跨模态LM预训练
  - 2.5 PLMs前沿技术
    - （1）GPT-3
    - （2）T5
    - （3）MoE
- 3.Transformers API教程

## FILE 98.相关课程/清华大模型公开课/4.Prompt Tuning & Delta Tuning/4.Prompt Tuning & Delta Tuning.md  (30 KB)
- 4.Prompt Tuning & Delta Tuning
- 1.Background
  - 1.1 Fine Tuning : BERT
  - 1.2 GPT
  - 1.3 T5
  - 1.4 GPT-3
  - 1.5 An Irreversible Trend
    - （1）Model Scaling
    - （2）Difficult Tuning
  - 1.6 Effective Model Adaptation
- 2.Prompt learning
  - 2.1 基本组成与流程介绍
    - （1）Prompt-learning
    - （2）Template vs Verbalizer
    - （3）Template ：情绪分类
    - （4）Prompt-learning ：注意事项
  - 2.2 PTM选取
    - （1）生成式模型
    - （2）MLM：分类模型，语言理解
    - （3）Encoder-Decoder：T5
  - 2.3 Template构造
    - （1）根据任务特点人为设计
    - （2）结构化，与规则相结合
    - （3）自动生成与搜索优化
    - （4）连续提示优化
  - 2.4 Verbalizer构造
    - （1）人工构造Verbalizer
  - 2.5训练新范式
    - （1）Pre-trained Prompt Tuning
    - （2）多任务预训练和人工prompts
  - 2.6 应用
- 3.Delta Tuning
  - 3.1 Addition-based (增量式)
  - 3.2 Specification-based (指定式)
  - 3.3 Reparameterization-based (重参数化)
  - 3.4 统一tuing
  - 3.5 总结
- 4.OpenPrompt
  - 4.1 OpenPrompt
  - 4.2 OpenPrompt demo
- 5.OpenDelta介绍

## FILE 98.相关课程/清华大模型公开课/5.高效训练&模型压缩/5.高效训练&模型压缩.md  (13 KB)
- 5.高效训练&模型压缩
- 1.背景介绍
  - 1.1 CPU & GPU
  - 1.2 显存组成
- 2.模型训练优化方式
  - 2.1 数据并行
    - (1）协作通信
    - （2）数据并行
    - （3）分布式数据并行
  - 2.2模型并行
  - 2.3 ZeRO
    - （1）ZeRO-Stage 1 &#x20;
    - （2）ZeRO-Stage 2 &#x20;
    - （3）ZeRO-Stage 3
    - （4）总结
  - 2.4 Pipeline并行
  - 2.5 优化技术细节
    - （1）混合精度
    - （2）Offloading
    - （3）Overlapping
    - （4）Checkpointing
  - 2.6 BMTrain——使用介绍
- 3.模型压缩
  - 3.1 知识蒸馏（Knowledge Distillation）
    - （1）PKD
    - （2）TinyBERT
  - 3.2 模型剪枝
  - 3.3 模型量化
  - 3.4 其他方法
    - （1）权重共享
    - （2）低阶近似（Low-rank Approximation）
    - （3）Architecture Search
- 4.BMCook
- 5.BMInf
  - 5.1 深入理解Transformer
  - 5.2 量化
  - 5.3 内存分配
  - 5.4 使用介绍

## FILE 98.相关课程/清华大模型公开课/6.文本理解和生成大模型/6.文本理解和生成大模型.md  (14 KB)
- 6.文本理解和生成大模型
- 1.简介
  - 1.1 NLP的主要应用
  - 1.2 信息检索
  - 1.3 机器问答
  - 1.4文本生成
- 2.信息检索
  - 2.1 背景
  - 2.2 IR定义和评价
    - （1）IR定义
    - （2）IR评价指标
  - 2.3 传统方法
    - （1）BM25
    - （2）缺点
  - 2.4 神经网络方法
    - （1）简介
    - （2）Cross-Encoder架构
    - （3）Dual-Encoder架构
  - 2.5 前沿热点
    - （1）Negative-enhanced Fine-tuning
    - （2）IR-oriented Pretraining
    - （3）Few/Zero-Shot IR
- 3.QA
  - 3.1 机器阅读理解
    - （1）RC定义与类型
    - （2）Traditional Pipeline
    - （3）Big-model-based Methods
  - 3.2 开放式QA
    - （1）生成式QA
    - （2）检索式QA
    - （3）REALM
    - （4）WebGPT
- 4.文本生成
  - 4.1 文本生成任务
  - 4.2 神经网络文本生成
    - （1）语言模型
    - （2）Seq2seq
    - （3）Autoregressive models
    - （4）Non-autoregressive models
    - （5）Decoding strategy
  - 4.3 受控文本生成
    - （1）Prompt methods
    - （2）Modifying probability distribution
    - （3）Reconstructing model architecture
  - 4.4 文本生成评估
    - （1）通用方法
    - （2）其他方法
  - 4.5 挑战

## FILE 99.参考资料/README.md  (0 KB)
- 99.参考资料