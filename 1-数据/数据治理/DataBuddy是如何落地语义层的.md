---
title: "DataBuddy是如何落地语义层的"
source: "https://mp.weixin.qq.com/s/ng1hVg7HKiMREg2WtkqNuw"
author:
  - "[[点赞加关注]]"
published:
created: 2026-11-09
description: "如果你在弄智能问数项目，建议看看"
tags:
  - "clippings"
---
点赞加关注 数道至简 *2026年9月28日 07:30*

群里翻到一份腾讯云 TBDS DataBuddy 团队的内部分享《DataBuddy 语义层实践》，30 页，我连着读了两遍。它讨论的不是“怎么让大模型写 SQL”，而是怎么把企业语义做成 Agent 能消费、能验证、能回滚的工程资产。因为其含金量很高，本文原PPT放在文后给大家分享：

它的解法是把语义层当成一条产品线来做。

- 先定义业务本体：术语、业务对象及关系、指标、任务剧本 Playbook 四类语义资产，治理作为横切面管 Owner、权限、版本、审批和回滚；
- 再用 Git 当语义权威源，配五级 CI——从 Schema 合法性、引用一致性，到指标安全和权限兼容，再到行为与检索回归；
- 运行时按 S0–S8 的检索瀑布逐级收敛，显式锚定优先，全库向量搜索只是其中一级，命中且约束完整就早停；
- 中间用强类型中间态（意图 → 语义上下文 → 语义计划 → 执行计划 → 证据包）把“模型理解”和“最终执行”拆开，每一步可检查、可回放。

冷启动也给了路径：从上万张表里先按范围和硬约束缩小候选，再做多路召回和两阶段精评，产出自动、待审、拒绝三类决策。最后用 Benchmark、实体体检、线上 Badcase 三路信号汇成统一的进化建议池，一次反馈对应一处根因、一个 MR，Agent 只能提案，不能自己合并。

推荐它，是因为踩过的坑基本都被它说中了。这两年我在企业数据架构及智能分析Agent的时候，最深的体感有三条：口径不一致比没有指标更糟；规则塞进 Prompt 迟早失控；口径改了没有版本和回滚，出问题没人敢认账。

这份 PPT 给了几个能直接抄的做法——语义资产 Semantic-as-Code，口径变更走 MR 和评审；运行时固定版本，每个答案都能证明用的是哪一版定义、哪张表、哪条权限；把“拒答”设计成合法终态，而不是当失败处理。它还有一句我特别认同：在现有数仓之上补足业务语义，而不是重建数据底座。如果你关注语义层建议看看。

![图片](attachments/DataBuddy是如何落地语义层的/640) ![图片](attachments/DataBuddy是如何落地语义层的/640_f3160d) ![图片](attachments/DataBuddy是如何落地语义层的/640_9a3841) ![图片](attachments/DataBuddy是如何落地语义层的/640_c7d345) ![图片](attachments/DataBuddy是如何落地语义层的/640_7ff824) ![图片](attachments/DataBuddy是如何落地语义层的/640_01115d) ![图片](attachments/DataBuddy是如何落地语义层的/640_0289d4) ![图片](attachments/DataBuddy是如何落地语义层的/640_4a7a00) ![图片](attachments/DataBuddy是如何落地语义层的/640_f45d94) ![图片](attachments/DataBuddy是如何落地语义层的/640_97aa19) ![图片](attachments/DataBuddy是如何落地语义层的/640_f9dd8f) ![图片](attachments/DataBuddy是如何落地语义层的/640_b6e26b) ![图片](attachments/DataBuddy是如何落地语义层的/640_d16dad) ![图片](attachments/DataBuddy是如何落地语义层的/640_c5d719) ![图片](attachments/DataBuddy是如何落地语义层的/640_bc3a7b)

Data for AI · 目录