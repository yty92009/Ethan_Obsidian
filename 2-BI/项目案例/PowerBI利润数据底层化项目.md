# Power BI 利润数据底层化项目

## 项目一句话

把原来压在 Power BI 里的 Amazon VC 利润重计算逻辑，逐步迁移到 PostgreSQL 数据底层，形成可复用、可排查、可长期维护的利润计算链路。

## 项目背景

这个项目服务于跨境电商经营分析场景。原始利润计算逻辑主要散落在 Power BI、人工文件、数据库源表和业务口径中，问题不只是“写 SQL”，而是要把销售、成本、广告、促销、Coop、库存、尺寸、仓储费、SKU mapping 等数据在数据库层完成清洗、匹配、分摊和校验。

当前核心业务范围是 Amazon Vendor Central 的 terminal / endpos 终端销售口径。后续计划扩展到 Amazon Seller Central、Walmart 等渠道，因此项目设计时必须保留渠道隔离能力。

## 当前最终成果

- 最终利润表：`data_market.bi_profit_calc_08_storage_fee_allocation`
- 当前粒度：`date + asin`
- 当前渠道：`channel = 'Amz VC'`
- 当前销售口径：Amazon VC terminal / endpos
- 主表骨架：销售 ASIN + 广告 ASIN + 促销 ASIN 的标准 10 位 ASIN 合集

最终表不是普通销售表，而是利润计算承载表，也可以理解为 `profit spine`。

## 核心业务边界

- `VC terminal/endpos` 是面向终端消费者的零售表现，是当前 SalesAmt 主事实。
- `VC supply/order` 是公司向 Amazon 的供货、采购或订单视角。
- PO / DF / DI 是 Amazon VC 内部供货或履约模式，不是顶层渠道。
- PO / DF / DI 当前用于 Coop 和成本结构估算，不与终端销售额直接相加。
- 库存、尺寸、Kit、NS 映射、原始 COGS 是跨渠道共享基础数据，不整表贴 `Amz VC` 标签。
- 销售、广告、促销、VC mix、VC weighted cost、VC coop 和利润结果按渠道隔离。

## 项目价值

这个项目的价值不是把报表换一个地方展示，而是把利润分析从“报表层手工拼接”升级为“数据底层可治理的计算链路”。

它解决的核心问题包括：

- 多来源数据口径不一致。
- 手工 Mapping 表直接入库导致重复、放大和污染。
- 成本来源不完整，需要多来源逐月归集。
- Amazon VC 终端销售和供货结构容易混用。
- 广告、促销、库存和仓储费需要进入利润链路并保持金额守恒。
- 数据刷新后需要有质量检查和状态快照，而不是只看报表有没有出数。

## 可复用方法论

1. 先定义业务口径，再做技术实现。
2. 区分事实口径、来源口径、分摊口径和报表口径。
3. 对手工文件建立清洗、去重、批次和血缘机制。
4. 对共享基础数据和渠道专属事实分层建模。
5. 用质量规则验证金额守恒、唯一键、缺失、渠道标签和分摊结果。
6. 把项目记忆、规则变更和状态快照作为数据项目的一部分维护。

## 相关笔记

- [[Amazon VC P&L利润链路]]
- [[跨境电商Mapping体系：SKU-NS-Kit]]
- [[跨境电商成本COGS归集方法]]
- [[Amazon VC Coop与PO-DF-DI扣点]]
- [[跨境电商数据治理与多渠道基础模型]]
- [[数据刷新与质量检查机制]]

## 来源

- `D:\powerbi项目\README.md`
- `D:\powerbi项目\项目接续说明_给新Codex账号.md`
- `D:\powerbi项目\项目记忆\项目背景.md`
- `D:\powerbi项目\项目记忆\memory_system\00_主记忆索引.md`

