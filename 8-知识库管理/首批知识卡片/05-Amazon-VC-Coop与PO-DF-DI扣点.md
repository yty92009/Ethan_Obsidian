---
type: summary
status: summarized
importance: S
review_priority: key
source_type: business_rule
knowledge_level: verified_in_vault
source_path: 4-数据分析/行业场景/跨境电商/Amazon VC Coop与PO-DF-DI扣点.md
related_notes:
  - 4-数据分析/行业场景/跨境电商/Amazon VC P&L利润链路.md
  - 4-数据分析/行业场景/跨境电商/跨境电商成本COGS归集方法.md
next_action: verify_rules
needs_human_review: true
---

# Amazon VC Coop 与 PO/DF/DI 扣点｜知识卡片

## 一句话结论

由于 VC 终端销售报告不能直接识别 DI、PO、DF 供货方式，Coop rate 需要用过去 12 个月供货结构加权估算，并对缺失情况使用可追溯的默认规则。

## 当前记录的规则

- PO：25.25%
- DF：19.25%
- DI：4.75%
- Jack 缺失默认 DF：19.25%
- Nicole 缺失默认 PO：25.25%
- 有销售额时不允许 `coop_rate = 0`

## 核心观点

1. 终端销售口径和供货结构口径必须分离。
2. Coop rate 是估算结果，应保留匹配状态和来源状态。
3. 默认值不能伪装成真实匹配。
4. `bi_vc_channel_mix` 和 `bi_vc_coop_rate` 都是 VC 专属事实。
5. 业务默认值必须有确认人、适用范围、版本和可回滚记录。

## 对我的价值

- 可转化为 Amazon VC 财务风控规则卡和异常检查清单。
- 适合面试中说明如何处理缺失数据和业务默认规则。
- 是 P&L 利润链路中“收入事实”和“费用估算”之间的关键桥梁。

## 需要验证的内容

- PO/DF/DI 当前固定扣点是否仍有效。
- Jack/Nicole 默认规则是否仍为 active，是否有规则编号和确认依据。
- 12 个月观察窗口的截止日期和缺失处理是否发生变化。
- `coop_matched_hj_alias` 等状态的实际定义。

## 最小实践任务

建立一张 Coop rate 规则登记表，至少包含：规则编号、扣点类型、百分比、来源、适用范围、缺失补救、状态、确认人、生效日期和验证 SQL。

验收标准：

- 任意一个 Coop rate 都能回答“真实匹配还是默认值”。
- 有销售但 Coop 为 0 能被质量检查发现。
- 规则变化时可追溯并支持历史复算判断。

## 我的最终判断

Coop 规则的核心不是记住几个百分比，而是建立“供货结构估算 + 默认规则 + 状态追溯 + 质量门禁”的完整控制链。当前数字属于知识库中的项目规则，继续使用前应由业务或数据库当前状态确认。
