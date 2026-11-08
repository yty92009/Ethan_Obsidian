---
title: ai agent 相关知识
tags:
  - AI Agent
  - RAG
  - n8n
  - DataAgent
  - 面试
created: 2026-09-04
---

# AI Agent 相关知识

> 这是一份面向业务分析、数据产品和 AI 应用实施岗位的 Agent 复习笔记。重点不是背概念，而是能够把业务问题拆成数据、知识、模型、工具、流程、状态和反馈闭环。

## 一、先用一句话理解 AI Agent

AI Agent 是以大语言模型 LLM 为推理核心，结合 Prompt、知识库、RAG、Memory、工具和工作流，围绕一个业务目标完成理解、判断、调用工具、执行动作和反馈闭环的应用系统。

~~~text
业务目标
→ Agent理解任务
→ 检索知识
→ 调用工具获取事实
→ LLM分析和决策
→ 执行动作
→ 保存状态和反馈
→ 持续评估和优化
~~~

Agent 不等于一个聊天机器人，也不等于“工作流里增加一个 AI 节点”。

## 二、Agent 与相关概念

| 概念 | 主要作用 | 在预警归因项目中的例子 |
| --- | --- | --- |
| LLM | 理解、推理、总结和生成内容 | OpenAI API |
| Agent | 以 LLM 为核心完成一项业务任务 | 数据质量专家、Amazon VC专家 |
| Workflow | 固定流程、条件分支和任务编排 | n8n 定时预警和通知 |
| Prompt | 规定角色、任务、输入、输出和限制 | 要求输出原因、证据和置信度 |
| Knowledge Base | 保存企业业务知识 | 指标定义、平台规则、历史案例 |
| RAG | 检索相关知识并提供给 LLM | 检索 Amazon VC费用规则 |
| Embedding | 将文本转换为向量 | 把异常案例转换成向量 |
| Vector Database | 保存向量并做相似检索 | Qdrant、RAGFlow内部向量引擎 |
| Context | 当前一次任务使用的信息 | 当前 SKU、异常值、SQL结果 |
| Memory | 保存对话和任务历史 | 已完成的质量检查、历史反馈 |
| State | 记录任务当前处于哪个阶段 | QUALITY_PASSED、WAITING_FEEDBACK |
| Tool | Agent能够调用的外部能力 | Hive查询、MySQL查询、钉钉Webhook |
| Router | 根据条件把任务分给不同Agent | Amazon VC、SC、Temu、TikTok分流 |
| Evaluation | 衡量结果是否准确、稳定和可解释 | 误报、漏报、归因准确率 |

## 三、完整 Agent 的组成

~~~mermaid
flowchart TB
    A[用户目标或系统触发]
    B[Agent控制层<br/>任务理解、计划、路由、状态]
    C[LLM<br/>理解和推理]
    D[Prompt<br/>角色、约束、输出格式]
    E[RAG<br/>检索业务知识]
    F[Memory<br/>保存上下文和历史]
    G[Tools<br/>查询数据和执行动作]
    H[Workflow<br/>重试、分支、审批和通知]
    I[业务结果<br/>报告、预警、任务、反馈]

    A --> B
    B --> C
    D --> C
    E --> C
    F --> C
    G --> C
    C --> H
    H --> G
    H --> I
    I --> F
~~~

在你的项目中，可以用“确定性系统保证事实，Agent负责理解和编排，RAG提供知识，工作流负责执行”概括。

## 四、LLM、Agent 和 Workflow 的区别

### LLM

LLM 是模型能力本身，擅长理解语言、归纳信息和生成回答，但默认不知道企业内部数据，也不能天然访问 Hive、MySQL 或钉钉。

~~~text
输入：异常数据 + 业务知识 + 工具结果
输出：归因结论、证据和建议
~~~

### Agent

Agent 是围绕业务目标搭建的应用层。它可以决定是否检索知识、调用哪个工具、是否需要人工复核和下一步执行什么动作。

~~~text
Agent = LLM + Prompt + RAG + Memory + Tools + 业务流程
~~~

### Workflow

Workflow 更偏确定性的流程编排。n8n 可以负责：

- 定时触发；
- SQL查询；
- 条件判断；
- 调用 Agent；
- 失败重试；
- 负责人映射；
- 调用钉钉 Webhook；
- 等待 ERP反馈；
- 更新状态。

n8n 可以作为 Agent 的编排底座，但 n8n 本身不等于 Agent。

## 五、RAG 是什么

RAG 是 Retrieval-Augmented Generation，即“检索增强生成”。

~~~text
用户问题或异常事件
→ 检索相关知识
→ 将知识片段放入Prompt
→ LLM根据知识进行回答或分析
~~~

RAG 解决的是：

> Agent 当前应该参考哪些企业知识？

它不能替代实时数据库，也不能自动让模型学习企业业务。

### RAG 的知识入库流程

~~~text
纯文本、Markdown、ERP反馈、数据规则
→ 文档读取
→ 文本切分
→ Embedding
→ 写入向量知识库
→ 保存知识类型、平台、版本和审核状态
~~~

### RAG 的查询流程

~~~text
当前异常：Amazon VC利润率从21%下降到12%
→ 生成检索问题
→ 向量检索相关知识
→ 返回利润口径、费用规则、历史案例
→ 与Hive实时数据一起发送给LLM
→ 生成归因结果
~~~

## 六、RAG、数据字典、数据血缘和业务知识

这是本次面试中最需要修正的地方。

### 数据字典

解决：

~~~text
指标是什么
字段是什么意思
指标怎么算
数据来自哪张表
~~~

### 数据血缘

解决：

~~~text
数据从哪里来
经过哪些表和字段
影响哪些下游指标和BI看板
~~~

### 业务知识

解决：

~~~text
业务为什么变化
哪些指标需要优先检查
不同平台的业务规则是什么
原因如何验证
应该采取什么动作
~~~

准确的架构应该是：

~~~text
数据字典 + 数据血缘
→ 数据质量判断、数据定位、影响范围分析

平台业务规则 + 指标关联逻辑 + 历史案例
→ 业务异常归因

Hive实时数据
→ 当前业务事实和验证证据
~~~

不能说：

> 把数据字典和血缘喂给 AI，就可以直接完成业务归因。

应该说：

> 数据字典和血缘属于数据治理知识，主要用于理解口径、确认数据可信度和定位影响范围；业务规则、指标关联、历史案例和实时数据共同支撑业务归因。

## 七、Embedding 和向量数据库

### Embedding

Embedding 是把一段文本转换成一组数字向量，使系统能够按照“语义相似度”搜索内容。

~~~text
“物流费用上涨导致利润下降”
→ [0.12, -0.31, 0.88, ...]
~~~

### 向量数据库

向量数据库保存文本片段、向量和元数据，并根据问题查找语义相似的知识。

~~~text
用户问题
→ Embedding
→ 向量相似度检索
→ 返回相关知识片段
~~~

向量数据库不适合替代 Hive 查询实时指标：

~~~text
今天利润率是多少
→ 查询Hive

利润率怎么算、哪些因素会影响利润率
→ 查询RAG知识库
~~~

## 八、Memory、Context 和 State

### Context：当前上下文

Context 是当前一次任务中送给 LLM 的信息：

~~~text
当前平台：Amazon VC
当前SKU：ABC001
利润率：12%
质量检查：通过
已查询指标：销售、广告、库存、物流
~~~

### Memory：可保存的历史

Memory 保存过去的对话、工具结果、任务过程和用户反馈。

~~~text
业务人员之前确认过：
这个SKU的问题是物流费用配置错误
~~~

### State：流程状态

State 记录任务当前在哪个阶段：

~~~text
NEW
→ QUALITY_CHECKING
→ QUALITY_PASSED
→ BUSINESS_ANALYZING
→ WAITING_FEEDBACK
→ CLOSED
~~~

在你的项目中，重要状态可以保存到 MySQL：

~~~text
alert_event
agent_run
agent_step
tool_call_log
retrieval_log
agent_result
erp_feedback
validated_case
~~~

### 最简单的记忆方式

~~~text
RAG = 查资料
Memory = 记事情
Context = 当前正在处理的信息
State = 当前流程进行到哪一步
~~~

在你的项目中：

| 内容 | 应该放在哪里 |
| --- | --- |
| 当前利润率、广告花费、库存数量 | Hive |
| 指标定义和数据口径 | RAG知识库 |
| Amazon VC费用规则 | 平台业务RAG |
| 已确认的异常案例 | 异常案例RAG |
| 当前异常快照和工具结果 | Context / State |
| ERP提交的原始反馈 | MySQL反馈表 |
| 审核后的反馈案例 | 异常案例RAG |

## 九、Tools 工具调用

工具是 Agent 能够调用的外部能力。你的项目中包括：

~~~text
Hive查询工具
→ 查询销售、广告、库存、利润和费用

MySQL查询工具
→ 查询规则、负责人、预警状态和ERP反馈

数据质量检查工具
→ 检查延迟、缺失、重复、映射和口径

元数据查询工具
→ 查询表、字段和指标定义

数据血缘查询工具
→ 查询上下游关系和受影响看板

负责人映射工具
→ SKU、平台、业务类型 → 负责人 → 钉钉UserID

钉钉Webhook工具
→ 推送消息并@负责人
~~~

准确表达是：

> 工具负责执行查询或检查，Agent负责理解工具结果并做判断。

## 十、Agent 路由器和子 Agent

Agent 路由器是一个分流中枢，根据平台、业务类型、任务状态等条件，把任务交给合适的 Agent。

~~~text
数据质量通过
        ↓
平台路由器
        ↓
Amazon → Amazon总控Agent
          ↓
          VC → Amazon VC专家Agent
          SC → Amazon SC专家Agent

Temu → Temu专家Agent
TikTok → TikTok专家Agent
~~~

你的路由器更适合用确定性规则实现：

~~~text
platform = Amazon and business_type = VC
→ Amazon_VC_Agent

platform = Amazon and business_type = SC
→ Amazon_SC_Agent

platform = Temu
→ Temu_Agent

platform = TikTok
→ TikTok_Agent
~~~

平台和业务模式明确时，n8n 的 Switch、IF 或 Code 节点通常比让 LLM自由决定更稳定、可解释。

## 十一、以 n8n 为主体的 Agent 框架

~~~mermaid
flowchart TB
    A[Schedule Trigger]
    B[Hive查询实时数据]
    C[SQL和规则引擎]
    D[异常事件中心]
    E[数据质量检查工具]
    F[数据质量专家Agent]
    G{平台路由器}
    H[Amazon VC专家Agent]
    I[Amazon SC专家Agent]
    J[Temu专家Agent]
    K[TikTok专家Agent]
    L[RAGFlow知识检索]
    M[业务工具<br/>Hive、MySQL、血缘、负责人]
    N[OpenAI Chat API]
    O[n8n执行层]
    P[钉钉Webhook]
    Q[ERP反馈]
    R[MySQL反馈表]

    A --> B --> C --> D
    D --> E --> F
    F -->|质量异常| O
    F -->|质量正常| G
    G -->|Amazon VC| H
    G -->|Amazon SC| I
    G -->|Temu| J
    G -->|TikTok| K
    H --> L
    I --> L
    J --> L
    K --> L
    H --> M
    I --> M
    J --> M
    K --> M
    L --> N
    M --> N
    N --> O --> P --> Q --> R
    R --> L
~~~

## 十二、你的 Hive + MySQL + RAGFlow 架构

### 数据层职责

~~~text
Hive
→ 保存销售、广告、库存、利润、费用等经营事实数据

MySQL
→ 保存负责人映射、预警状态、规则配置、ERP反馈和任务状态

RAGFlow
→ 管理指标定义、数据规则、平台规则和异常案例

n8n
→ 编排查询、质量判断、路由、通知和反馈流程

OpenAI API
→ Embedding和LLM推理
~~~

### 推荐流程

~~~text
服务器纯文本文件夹
→ n8n同步到RAGFlow
→ RAGFlow解析、切分、Embedding和索引
→ Agent运行时通过HTTP API检索
→ n8n把检索结果和Hive实时数据交给OpenAI
~~~

RAGFlow 更适合承担文档管理、Dataset管理、文档切分、Embedding、混合检索、重排序和引用；n8n继续承担 Hive/MySQL 查询、数据质量检查、Agent路由、任务状态、钉钉通知、ERP反馈和重试。

如果 RAGFlow 与 n8n 都运行在 Docker 中，可以通过同一 Docker 网络连接：

~~~text
n8n容器
→ http://ragflow:9380
→ RAGFlow HTTP API
~~~

如果是不同的 Docker Compose 项目，也可以通过服务器 IP 和映射端口访问。知识文件夹可以挂载到 n8n 容器，由 n8n 检测新增或修改文件，再通过 API 上传到 RAGFlow。

## 十三、反馈机制和持续改进

业务人员在 ERP 中填写：

~~~text
是否确认异常
实际原因
处理措施
处理结果
~~~

数据先写入 MySQL 反馈表，再经过审核：

~~~text
ERP反馈
→ MySQL保存
→ 关联异常ID
→ 人工审核
→ 标准化异常案例
→ 同步到RAGFlow
→ 后续检索复用
~~~

持续改进不是直接修改 OpenAI 基础模型，而是：

~~~text
误报、漏报和人工反馈
→ 发现知识缺口
→ 优化规则、Prompt、知识片段和路由
→ 离线评估
→ 人工审核
→ 发布新版本
~~~

## 十四、面试中的项目边界

如果只完成了纯文本文件夹和 OpenAI API，不要直接说已经有完整的向量 RAG。

可以说：

> 当前已经建立了结构化业务知识目录，并完成了指标、数据规则、平台规则和异常案例的知识分类。工程化方案是由 n8n 将知识同步到 RAGFlow，经过切分和 Embedding 后建立检索索引，再供 Agent运行时调用。

如果已经真正部署 RAGFlow，则可以说：

> 纯文本目录是原始知识源，RAGFlow承担知识库管理、解析、切分、Embedding和检索，n8n通过 HTTP API 调用检索服务，结合 Hive实时数据和 MySQL 任务上下文，调用 OpenAI API 完成归因。

## 十五、常见面试问题

### 1. Agent 和普通工作流有什么区别？

普通工作流通常是预先固定的步骤；Agent 可以利用 LLM 理解任务、选择知识、调用工具和决定下一步。企业项目通常是确定性工作流与 Agent 能力结合，而不是完全自由运行。

### 2. 为什么不让 LLM 直接计算利润？

利润计算需要准确、可复现和可审计，应该由 Hive、SQL和规则引擎完成。LLM更适合做指标解释、证据组织、原因分析和建议生成。

### 3. RAG 和 Fine-tuning 有什么区别？

RAG 是运行时检索外部知识，知识更新快、可追溯；Fine-tuning 是调整模型参数，更适合固定格式和特定任务风格。企业规则和异常案例优先考虑 RAG。

### 4. Memory 和 RAG 有什么区别？

RAG 是查企业知识，Memory 是保存当前任务、历史对话和执行状态。RAG回答“应该参考什么”，Memory回答“之前发生了什么”。

### 5. 数据字典能不能直接用于归因？

不能单独完成。数据字典和血缘主要支撑数据口径、质量检查和影响范围分析；业务归因还需要平台业务规则、指标关系、历史案例和实时数据。

### 6. 为什么要先做数据质量判断？

如果数据延迟、缺失、重复或映射错误，Agent可能把数据问题误判成业务问题，进而输出错误建议。数据质量闸门可以先判断数据是否可信。

### 7. n8n 在项目中扮演什么角色？

n8n 是工作流和 Agent 编排层，负责触发任务、调用 Hive/MySQL、执行质量检查、路由 Agent、处理重试、调用钉钉 Webhook 和接收 ERP反馈。

### 8. RAGFlow 是否替代 n8n？

不替代。RAGFlow主要承担知识解析、索引和检索；n8n仍然负责数据查询、Agent路由、业务流程、通知、反馈和状态管理。

### 9. Agent 如何持续改进？

通过 ERP 收集人工确认结果，将审核后的反馈沉淀为异常案例，进入 RAGFlow案例库；同时统计误报、漏报和知识缺口，优化规则、Prompt、知识和路由，并通过离线评估和人工审核发布。

## 十六、一段完整面试回答

> 我理解的 AI Agent 不是单独的大模型，而是围绕业务目标，将 LLM、Prompt、RAG、Memory、工具和工作流组合起来的应用系统。在我的经营异常预警项目中，Hive负责保存销售、广告、库存和利润等事实数据，MySQL保存负责人、规则、反馈和任务状态，n8n负责调度、数据质量检查、Agent路由和钉钉通知。数据质量专家 Agent先结合指标口径、元数据和血缘判断数据是否可信；数据通过后，平台业务专家 Agent再检索对应平台规则、指标关联关系和历史异常案例，并调用 Hive 查询实时证据，最后由 OpenAI API完成归因。ERP反馈经过审核后沉淀为案例，进入RAGFlow知识库，用于后续检索和应用层持续优化。

