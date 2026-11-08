---
type: summary
status: summarized
importance: S
review_priority: key
source_type: learning
knowledge_level: learning_reference
source_path: 6-面试与职业发展/10-面试-职业发展/ai agent 相关知识.md
related_notes:
  - 3-AI/AI对话沉淀/Codex项目记忆系统实践.md
  - 2-BI/可视化/Vue Data UI图表库学习整理.md
next_action: practice
needs_human_review: true
---

# AI Agent 相关知识｜知识卡片

## 一句话结论

AI Agent 是围绕业务目标，将 LLM、Prompt、RAG、Memory、工具和工作流组合起来的应用系统；确定性系统负责事实和执行，Agent 负责理解、编排、分析和反馈闭环。

## 核心观点

1. LLM、Agent、Workflow、RAG、Memory、Context、State、Tool、Router、Evaluation 各有不同职责。
2. RAG 解决“当前应该参考哪些知识”，不能替代实时数据库，也不会自动让模型学会企业业务。
3. 数据字典和血缘主要支撑口径理解、质量判断和影响范围分析；业务归因还需要平台规则、指标关系、历史案例和实时数据。
4. Hive / 数据库负责事实计算，RAG 负责知识检索，n8n 负责流程编排，LLM 负责理解、组织证据和生成建议。
5. 路由和质量闸门优先使用确定性规则，避免把平台分流和关键事实判断完全交给 LLM。
6. 反馈经过人工审核后沉淀为案例，再用于 RAG、规则、Prompt 和评估集的迭代。

## 对我的价值

- 这篇笔记可作为个人 AI Agent 面试和项目设计总纲。
- 与当前知识库管理项目高度相关：Obsidian 是知识存储层，AI 是筛选和归纳层，实践任务是执行层。
- 可帮助设计未来的经营异常归因、知识检索和项目记忆助手。

## 需要验证的内容

- 文中提到的 Hive、MySQL、RAGFlow、n8n 架构哪些已实际部署，哪些属于工程化方案。
- 面试表达中必须区分“已完成”“正在设计”和“可迁移方案”。
- RAGFlow、Embedding 和模型 API 的当前版本及部署状态。

## 最小实践任务

为当前 Obsidian 知识库设计一个“资料筛选 Agent”流程：

1. 读取新资料。
2. 判断主题和优先级。
3. 检索相似笔记。
4. 生成知识卡片草稿。
5. 标记需要人工确认的内容。
6. 生成实践任务。

验收标准：

- AI 不直接修改正式笔记。
- 每个结论可追溯到来源文件。
- 外部观点、个人经验和正式规则被明确区分。
- 处理结果可重复、可复核。

## 我的最终判断

当前最适合自己的 Agent，不是让模型自由管理整个 Vault，而是先做“受控的资料筛选与知识卡片生成”。关键事实、文件写入和正式规则仍由确定性程序和人工确认控制。
