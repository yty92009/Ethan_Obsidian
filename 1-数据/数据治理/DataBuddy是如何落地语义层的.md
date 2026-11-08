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

![图片](https://mmbiz.qpic.cn/mmbiz_png/sooib80cYllj4hic0pCgDQbN0Od8yWxh7D0W2iaibh1wqXpazvvREXWU7Tn6JIRx2fJOVnc8QSuAxX0C6Z74ge0QzbqAwweSWy4KwBgRch5PDuU/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0) ![图片](https://mmbiz.qpic.cn/mmbiz_png/sooib80cYllia8eq8HA3kI9Yx1YoGZqlWpLnXOTWZlKAaiam756j8wolh2Jxx2dWwR5sNR68ZxcSNzTQ1ZBwDMgvAqia5EoaRhFoaXfxICspla4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYlliaibt3qpgbEM4RHx7M1vAFxsKmAte9szccRFM73dHjjAuVcAKA91CTmXW3tpVa3XU8dutM9IKiaCsPqXSyp73Ilaj3LVibceKvG6Q/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYlliaWYb1yNoQxtX3JpcWuYRxsDibBuROwG0ZBHRVxKLYibCYRMsQ9ibAx9l9z2QIKWQOZ7UXdp2X4hzk4SbNTNS6chLdtthrP7CETuU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6) ![图片](https://mmbiz.qpic.cn/mmbiz_png/sooib80cYllhxuepbBorKWpLOULWXlTW7a4KllYZjMI4qdicGriaicakGEsOEFODb79Jick8FhItrYcZa2ceBZblvUEmTAriaja92OAVYBpujW5JE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYlliapUMbru46kKhYO4rLLFgTEibDfIaUsYygaia0q1ozlp1D1DTyETJqyFeRpfhV6DGpluV8VSgumjf3K99Suzv9X6LibZ2p1C7MeXw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10) ![图片](https://mmbiz.qpic.cn/mmbiz_png/sooib80cYllg8gIpcT5XpwibOtPicwLgA7w4DiaxzXG67OD65ibNicC5FdQAnsTeuPdVfCiaEnFMRz1KU7DZOGwAxnRMrfmEwK7ibNxbMqJiapeNafTg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYlljP5nOGVvlwpLWrBS7UgR0NCj2fNdWfQtbwwg24D8fZnxaiaNg4HicDPBoIicT5u2MuPwCbKicFEXQvTFV4DgJIxHOrEDiakXwDLsMM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=14) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYllhH5502aRyzFogB7qJuIkhDic78MjeCFrClYicWZ72jTWbPfnMZWJfZBvE6nAjUuZWjIUtKxVz2rcQcoicIIpxW2KcavaTYPkBCnQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=16) ![图片](https://mmbiz.qpic.cn/mmbiz_png/sooib80cYlliac8p7icdpzfibrCVXCQfyW3SkWHv3RHGGKgcgUDgibYcsZGJQ7ibBLVjswtBlfjVFDo58KDo8Dqv0GFntE0MNnYhrJj3kfibgypnC0/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=18) ![图片](https://mmbiz.qpic.cn/mmbiz_png/sooib80cYllgkiamdWcrztWibqjTqWibll55iazpL5jsM1z3MUVUjz7iczUy3kXytG5rYqHopqf5sAgmGOxr5XibPhzR9CeepQQcuzQz6PCib7wwictw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=20) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYllg1cGQD2LXU0uEwS6UVjZWrgGKjVOoYMhFQULC0ozefnZUGrjfiay0GCjXl51yImibcB2mJs0D9sDJTfUmL1ibyyNnjOW3ZJQ0CUc/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=22) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYlliaLEHM8gIsia8wCJCkeBgqPqsfkOJic4XeFzltiaBS9X1pkLfzol0qm5lvh2bGuyEOc4JmsYEb0KU04yCicAaKyp9KYOVPqyTtfV3U/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=24) ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYllhpIOu30nPu8hMrsWHmnWNTTDH0YjIVtCNflRglscNe1sKWOFCp5k9cvC2JraBROtKXItQRSKcicpGACLzhbsqCfXxmNfqFwnG4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=26) ![图片](https://mmbiz.qpic.cn/mmbiz_png/sooib80cYllhgaJfFaibibIByv3yxMBKqn2bOPRbjGZsiawW5VsCSdcjcst9BZCFwuBj93IVEKJvCq913eVQlWTWTB3sfGd2Q8HF9ia7D7rCjpS4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=28)

Data for AI · 目录