---
type: summary
status: summarized
importance: B
review_priority: spot_check
source_type: synthesized_from_vault
source_path: 2-BI/技巧/在 Power BI Desktop 中设置和使用日期表.md
topic:
  - BI
  - PowerBI
created: 2026-11-09
updated: 2026-11-09
related_notes:
  - 8-知识库管理/Clippings处理/03-PBI隐藏列.md
next_action: none
needs_human_review: false
verification_status: unverified
---

# PBI / PQ 技巧合集（11 篇合并）｜知识卡片

> 合并卡：11 篇 Power BI / Power Query 操作技巧（B 级用时查，均为完整正文），原文已迁入 `2-BI/技巧/` 与 `2-BI/可视化/`。做报表卡壳时先查本卡索引再点原文。

## 技巧索引

**日期与时间智能（5 篇）**

| 原文 | 要点 |
| --- | --- |
| [[2-BI/技巧/在 Power BI Desktop 中设置和使用日期表]] | 日期表的作用、自动识别与手动设置的取舍 |
| [[2-BI/技巧/非标准日历的同比环比，如何用Power BI计算？]] | 业务月（如 26 号～次月 25 号）自建周期字段 + VAR 定位上一期，解决非自然月对比 |
| [[2-BI/技巧/Power Pivot&Power BI不连续日期的日环比]] | 业务非每日发生（如股票交易日）时，dateadd 拿不到上一期——需按"上一个存在的日期"做日环比 |
| [[2-BI/技巧/PowerBI - Format 将日期转换为星期  (附日期转换表 &amp; 自定义数字格式 &amp; 转换函数)]] | FORMAT 自定义格式代码表 + WEEKDAY 显示星期几的实践 |
| [[2-BI/技巧/Power Query之二 可视化数据处理_power query 编辑器中原表有日期导入后不显示]] | PQ 中日期导入后不显示的原因与处理（PQ 日期/合并查询入门） |

**分析与可视化（4 篇）**

| 原文 | 要点 |
| --- | --- |
| [[2-BI/技巧/PowerBI中帕累托图的制作（一）]] | 帕累托（二八效应）图原理与做法——SKU 销售贡献分析可直接复用 |
| [[2-BI/可视化/67 个组件！Vue3 又一款宝藏图表库火了！]] | Vue Data UI 图表库概览（配套整理笔记同目录） |
| [[2-BI/技巧/利用这个技巧，为Power BI页面批量插入背景图片]] | 页面背景图批量设置技巧 |
| [[2-BI/技巧/推荐多款好看的报表图表配色方案（适用于PPT，大屏可视化分析）_ppt报表怎么放好看图片]] | 20 种大屏/PPT 配色方案 + 取色技巧（QQ/微信截图取色值） |

**数据清洗（2 篇 + 官方导航）**

| 原文 | 要点 |
| --- | --- |
| [[2-BI/技巧/PowerQuery文本处理技巧：移除和提取]] | Text.Remove / Text.Select 两个 M 函数做文本清洗 |
| [[2-BI/技巧/数据可视化之PowerQuery篇（四）二维表转一维表，看这篇文章就够了]] | 一维表是规范数据源的标准；二维表转一维表做法 |
| [[2-BI/技巧/Power BI 网站导航  学习资料大全 - PowerBI极客]] | Power BI 官方文档/博客/学习路径导航站 |

## 对我的价值

跨境电商报表高频痛点全覆盖：业务月对比（亚马逊月结口径常非自然月）、SKU 帕累托、文本清洗（SKU/ASIN 字段）、一维表规范。非标准日历与不连续日期两篇与 [[4-数据分析/行业场景/跨境电商/Amazon VC P&L利润链路]] 的日期口径问题直接相关。

## 需验证

技巧涉及 DAX/M 函数版本差异，按当前 Power BI Desktop 版本复核；配色方案审美向，无对错。

## 阅读建议

不精读；做报表遇到具体问题时按索引点入。
