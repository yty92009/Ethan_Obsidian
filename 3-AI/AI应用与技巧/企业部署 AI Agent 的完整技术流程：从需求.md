---
title: "企业部署 AI Agent 的完整技术流程：从需求"
source: "https://mp.weixin.qq.com/s/gUb8CzcE25mS7LT6jZWKZQ"
author:
  - "[[洛洛讲网安]]"
published:
created: 2026-11-09
description: "公司想做个内部 IT 支持 Agent，员工问一句 VPN 怎么连，它就去查知识库，查不到直接建工单。演示时接几个工具、配个工作流就能跑通。\x0a\x0a真要上线，坑全在后面。知识库文档谁更新？销售和财务的权限在哪一层拦？Agent 调 API 用的是谁的账号？模型判断错了系统怎么兜底？\x0a\x0aFDE 干的活大半就在这几段里。他们得把业务需求翻译成能开发、能测试、能部署的方案。更要紧的是判断什么技术配什么业务——一个 RAG 问答就能解决的事，硬上多 Agent 架构，后面每一步都会变重。\x0a\x0a整套流程拆下来，从需求调研到监控交付，FDE 在每个环节都有明确的交付物。真正值钱的不是写代码，而是知道什么时候该用自动化、什么时候才需要上 Agent。\x0a\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-tq1nq3\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#FDE\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-s7ynz3\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#前沿部署工程师\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-vkhf9n\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#AI人才\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-rv57s3\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#AI工程师\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-32wzas\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#AI职业发展\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-plpaqu\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#企业AI转型\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-q5vzyz\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#AI项目交付\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-76a5yl\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#行业解决方案\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-22vrsu\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#能力模型\x26lt;/a\x26gt;\x26lt;a class=\x26quot;wx_topic_link\x26quot; topic-id=\x26quot;mvjiyqaf-wq1iuw\x26quot; style=\x26quot;color: #576B95 !important;\x26quot; data-topic=\x26quot;1\x26quot;\x26gt;#FDE前线\x26lt;/a\x26gt;"
tags:
  - "clippings"
---
 

1. 1
2. 2
3. 3
4. 4
5. 5
6. 6
7. 7
8. 8
9. 9
10. 10
11. 11
12. 12
13. 13

公司想做个内部 IT 支持 Agent，员工问一句 VPN 怎么连，它就去查知识库，查不到直接建工单。演示时接几个工具、配个工作流就能跑通。  
  
真要上线，坑全在后面。知识库文档谁更新？销售和财务的权限在哪一层拦？Agent 调 API 用的是谁的账号？模型判断错了系统怎么兜底？  
  
FDE 干的活大半就在这几段里。他们得把业务需求翻译成能开发、能测试、能部署的方案。更要紧的是判断什么技术配什么业务——一个 RAG 问答就能解决的事，硬上多 Agent 架构，后面每一步都会变重。  
  
整套流程拆下来，从需求调研到监控交付，FDE 在每个环节都有明确的交付物。真正值钱的不是写代码，而是知道什么时候该用自动化、什么时候才需要上 Agent。  
#FDE#前沿部署工程师#AI人才#AI工程师#AI职业发展#企业AI转型#AI项目交付#行业解决方案#能力模型#FDE前线

原文企业部署 AI Agent 的完整技术流程：从需求调研、架构设计到开发、评测、部署与交付，能看懂FDE在每一步到底负责什么