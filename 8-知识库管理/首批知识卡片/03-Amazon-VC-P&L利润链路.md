---
type: summary
status: summarized
importance: S
review_priority: key
source_type: method
knowledge_level: verified_in_vault
source_path: 4-数据分析/行业场景/跨境电商/Amazon VC P&L利润链路.md
related_notes:
  - 2-BI/项目案例/PowerBI利润数据底层化项目.md
  - 4-数据分析/行业场景/跨境电商/跨境电商成本COGS归集方法.md
  - 4-数据分析/行业场景/跨境电商/Amazon VC Coop与PO-DF-DI扣点.md
next_action: practice
needs_human_review: true
---

# Amazon VC P&L 利润链路｜知识卡片

## 一句话结论

Amazon VC 利润链路以标准 ASIN 合集构建 profit spine，按固定刷新顺序逐步叠加销售、成本、Coop、促销、广告、库存和仓储费，并通过粒度、守恒和渠道检查保证结果可靠。

## 核心观点

1. 最终利润表不是普通销售表，而是利润承载表；即使没有销售但有广告或促销费用的 ASIN，也可能需要进入主表。
2. 当前粒度是 `date + asin`，当前渠道是 `Amz VC`。
3. VC terminal/endpos 代表终端销售；PO/DF/DI 代表供货结构，不能直接混算。
4. Ads/Promo 必须先按 `channel + date + asin` 聚合，再 Join 到利润 spine，避免金额放大。
5. 刷新顺序本身是业务链路的一部分，不能只看最终表。

## 14 步链路摘要

销售 spine → 销售 Mapping → SKU 渠道 Mapping → VC mix → weighted cost → Coop rate → 成本 → Coop → Promo → Ads → 库存 → 库存维度 → 仓储费 → 仓储费分摊。

## 对我的价值

- 是 P&L 主题的主流程卡片。
- 可以转化成刷新 Runbook、面试白板图和质量检查清单。
- 可帮助 AI 理解利润链路中的顺序依赖和口径边界。

## 需要验证的内容

- 14 个刷新过程当前是否有变更。
- 当前表名、字段名、粒度和渠道值是否仍然有效。
- 每一步的输入输出及失败处理是否已登记到正式 Runbook。

## 最小实践任务

制作一张利润链路验收表，逐步列出：输入表、输出表、粒度、关键 Join、金额守恒规则、失败时应查看的字段。

验收标准：

- 能解释 profit spine 为什么要吸收 Ads/Promo ASIN。
- 能解释先聚合再 Join 的原因。
- 能列出 `date + asin` 唯一性、SalesAmt 守恒、Ads/Promo 守恒和渠道隔离检查。

## 我的最终判断

这条链路的关键不是记住 14 个过程名，而是理解“先确定事实骨架，再按依赖关系叠加费用和成本，最后验收金额与粒度”。
