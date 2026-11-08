---
type: summary
status: summarized
importance: S
review_priority: key
source_type: clipping
source_path: 3-AI/AI应用与技巧/一篇文章讲清楚 AI Agent 的核心概念：从 Token、Skill、RAG 到 MCP、SDD 和 Harness 工程.md
source_url: "https://mp.weixin.qq.com/s/8xtOwZmoMO2_sHuKx1W2FA"
topic:
  - AI
  - 面试
created: 2026-11-09
updated: 2026-11-09
related_notes:
  - 8-知识库管理/首批知识卡片/06-AI-Agent相关知识.md
  - 3-AI/AI Agents 教程/21-Agent智能体.md
  - 3-AI/AI Agents 教程/20-MCP模型上下文协议.md
next_action: practice
needs_human_review: true
verification_status: unverified
---

# AI Agent 核心概念 13 讲｜知识卡片

## 一句话结论

用 13 个递进概念把 Agent 全景讲清：LLM 基座（预训练/微调/幻觉）→ Agent 四要素（规划/记忆/工具/ReAct）→ 工程化（MCP/Skill/Harness/SDD），适合作为 AI 岗位面试的概念底稿。

## 核心观点

- **Agent 定义**：以 LLM 为核心，具备规划、记忆、工具调用能力，自主拆解任务、循环执行直到完成的计算实体——从"文本生成"升级为"任务自主执行"。
- **基座三层**：预训练（自监督预测下一个 token）→ 微调（任务数据 SFT/指令微调）→ 幻觉治理（生成内容不默认为事实）。
- **Token**：分词器把文本切为 token 并映射数字 ID，模型推理全程基于 ID 计算。
- **MCP**：模型上下文协议，AI 应用连接外部数据源与工具的标准化接口，类比"TypeC 接口"。
- **RAG**：回答前先检索（开卷考试），解决模型没学过内部文档的问题。
- **记忆两层**：短期记忆用截断/摘要控制 prompt 长度；长期记忆用向量召回历史按需回填上下文。
- **Skill**：结构化本地文件夹（skill.md + 规则/模板/脚本/参考资料），面向大模型的能力封装。
- **ReAct**：Reason+Act 循环——信息不够就调工具拿结果，再继续推理。
- **自我反思**：生成后评估再修正；自我反馈查一致性，外部反馈（真实工具验证）适合代码/计算类硬任务。
- **Harness 工程**：为 Agent 设计工作环境——上下文管理、沙箱、权限、测试、日志、评审、反馈回路，让 Agent 在真实工程中可靠可控。
- **SDD 规格驱动开发**：编码前先用规格文档锁定目标/范围/行为/约束/任务拆分，再让 AI 按文档开发，减少猜需求与跑偏。

## 对我的价值

面试向知识密度高，且与面试储备里"ai agent 相关知识"互补：这 13 个概念就是 AI 应用岗面试高频题的标准答题骨架（作者本身就是面试题系列）。结合自己的 Power BI + Agent 实践（Obsidian 资料筛选 Agent），每个概念都能挂一个自己的案例。

## 关联已有笔记

- [[6-面试与职业发展/10-面试-职业发展/ai agent 相关知识]]
- [[3-AI/AI Agents 教程/21-Agent智能体]]、[[3-AI/AI Agents 教程/20-MCP模型上下文协议]]、[[3-AI/AI Agents 教程/27-Skills技能与AI编程工具实践]]
- [[5-正式知识资产/AI/Obsidian资料筛选Agent设计说明]]

## 建议动作

把 13 个概念对照教程章节补深度（MCP→20 章、RAG→19 章、LangGraph 记忆→16/26 章），再为每个概念写一句"我自己的项目例子"，形成面试答题卡。

## 最小实践与验收

选 3 个概念（MCP、Skill、SDD）在 Obsidian 资料筛选 Agent 语境下各写一段 200 字面试答案，包含定义+我的实践+踩坑。验收：能脱稿讲清且例子与实际项目一致。

## 需验证

概念定义属通识无外部数据风险；Harness/SDD 概念较新，最佳实践以目标岗位 JD 与实际工程为准；文末推荐链接为同一作者营销内容，按需取用。

## 阅读建议

面试准备期完整阅读并做题卡化；平时作概念速查。
