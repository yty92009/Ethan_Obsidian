---
type: summary
status: summarized
importance: A
review_priority: spot_check
source_type: synthesized_from_vault
source_path: 3-AI/AI应用与技巧/AI Agent8大主流架构从ReAct到自主智能体.md
topic:
  - AI
  - Agent
created: 2026-11-09
updated: 2026-11-09
related_notes:
  - 8-知识库管理/Clippings处理/17-AI-Agent核心概念.md
next_action: none
needs_human_review: false
verification_status: incomplete_source
---

# AI Agent 落地架构（3 篇合并，1 篇占位）｜知识卡片

> 合并卡：Agent 从概念到企业落地的架构与流程（A 级）。原文已迁入 `3-AI/AI应用与技巧/`。

## 覆盖原文与要点

| 原文 | 要点 |
| --- | --- |
| [[3-AI/AI应用与技巧/AI Agent8大主流架构从ReAct到自主智能体]] | 8 种架构一句话选型：ReAct（想→做→看反馈，费钱慢）／Plan-and-Execute（先规划后执行，全局视野）／Multi-Agent（主管+专职分工，协调易冲突）／Reflective（自检自改，Token 消耗大）／Tool-Augmented（大脑配手脚，前提工具靠谱）／Memory-Augmented（分层记忆防失忆）／RAG Agent（先查再答，企业落地最刚需）／Autonomous Loop（自动驾驶跑批，需人盯着） |
| [[3-AI/AI应用与技巧/企业部署 AI Agent 的完整技术流程：从需求]] | FDE（前沿部署工程师）视角的企业 Agent 落地：需求调研→架构设计→开发→评测→部署→交付，每环节有明确交付物；真实坑在上线后（知识库谁更新、权限在哪层拦、API 用谁的账号、模型错了怎么兜底）；**核心判断力：RAG 问答能解决的事别硬上多 Agent**——知道什么时候用自动化、什么时候才上 Agent |
| [[3-AI/AI应用与技巧/Embedding 向量嵌入：AI世界的经纬度]] | **incomplete_source 占位**：正文仅存一句"向量是语义的经纬度，Embedding 是 AI 世界的 GPS"，实质内容在图片/视频中未抓取。补证后重写 |

## 对我的价值

与 [[8-知识库管理/Clippings处理/17-AI-Agent核心概念]]（概念层）衔接：17 讲"是什么"，本卡讲"怎么选、怎么落"。8 架构是面试答题的选型框架（结合自家 Obsidian 资料筛选 Agent 属 RAG+Tool 增强型）；FDE 的"上线后的坑"清单（权限/账号/兜底）与筛选 Agent 设计说明的受控边界互相印证。

## 关联已有笔记

- [[8-知识库管理/Clippings处理/17-AI-Agent核心概念]]
- [[5-正式知识资产/AI/Obsidian资料筛选Agent设计说明]]
- [[3-AI/AI Agents 教程/21-Agent智能体]]

## 需验证

8 架构为通识归纳无数据风险；FDE 流程为个人经验总结；Embedding 占位待补证。

## 阅读建议

面试选型题用 8 架构；做 Agent 立项评估用 FDE 清单。
