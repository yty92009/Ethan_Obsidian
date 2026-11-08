---
title: "在 Power BI Desktop 中设置和使用日期表"
source: "https://learn.microsoft.com/zh-cn/power-bi/transform-model/desktop-date-tables"
author:
  - "[[kgremban]]"
published:
created: 2026-10-30
description: "了解什么是日期表、如何使用它们，以及可能想要在 Power BI Desktop 中将表设置为日期表的原因。"
tags:
  - "clippings"
---
Power BI Desktop 在后台工作，自动识别表示日期的列，然后代表用户为模型创建日期层次结构和其他启用元数据。 然后，用户可以在创建报表功能（如可视化效果、表、快速度量值、切片器等）时使用这些内置层次结构。 Power BI Desktop 通过代表用户创建隐藏表来生成此数据，然后用户可以将表用于报表和 DAX 表达式。

有关此自动行为的详细信息，请参阅 [在 Power BI Desktop 中应用自动日期/时间](https://learn.microsoft.com/zh-cn/power-bi/transform-model/desktop-auto-date-time) 。

许多数据分析师更倾向于创建其自己的日期表，这样做也可以。 在 Power BI Desktop 中，可以指定希望模型将其用作日期表的表，然后使用该表的日期数据创建与日期相关的视觉对象、表、快速度量值等。 指定自己的日期表时，可以控制在模型中创建的日期层次结构，并在快速措施和使用模型日期表的其他操作中使用它们。

![Power BI Desktop 的屏幕截图，其中显示了“标记为日期表”对话框。](https://learn.microsoft.com/zh-cn/power-bi/transform-model/media/desktop-date-tables/date-tables_01.png)

Power BI Desktop 的屏幕截图，其中显示了“标记为日期表”对话框。

## 您需要标记您的日期表的时机

如果在 [Power BI 中使用经典时间智能函数](https://learn.microsoft.com/zh-cn/power-bi/transform-model/desktop-time-intelligence#classic-time-intelligence) ，或者以下任一方案适用于你，则必须标记日期表：

- 日期表与模型中其他表之间的关系基于数据类型不同于日期/时间的列。 例如，如果从数据仓库等源加载数据，通常会提供表示日期的特定列。 这些列（也称为代理键）通常存储为整数，格式为 yyyy-mm-dd（例如： *20241231* 表示 2024 年 12 月 31 日）。 如果日期表与使用此类列的模型中的其他表之间存在关系，则需要设置自己的日期表才能使用时间智能功能。
- 如果要基于 Power BI 数据 [在 Excel 数据透视表或数据透视图中使用高级日期筛选器](https://support.microsoft.com/office/filter-dates-in-a-pivottable-or-pivotchart-571cc416-ba4d-4005-a01e-3d99306ccefc)

## 如何设置自己的日期表

若要设置 **日期表** ，请在字段窗格中选择要用作日期表的表，然后右键单击该表，在出现的菜单中选择标记为日期表标记为日期表，如下图所示。

![Power BI Desktop 的屏幕截图，其中显示了“字段”窗格中的“标记为日期表”选项。](https://learn.microsoft.com/zh-cn/power-bi/transform-model/media/desktop-date-tables/date-tables_02.png)

Power BI Desktop 的屏幕截图，其中显示了“字段”窗格中的“标记为日期表”选项。

还可以选择该表，然后从“表工具”功能区中选择“标记为日期表”，如此处所示。

![Power BI Desktop 的屏幕截图，其中显示了“标记为日期表”按钮和选项筛选器。](https://learn.microsoft.com/zh-cn/power-bi/transform-model/media/desktop-date-tables/date-tables_02b.png)

Power BI Desktop 的屏幕截图，其中显示了“标记为日期表”按钮和选项筛选器。

> !\[注意\]如果使用 [基于日历的时间智能](https://learn.microsoft.com/zh-cn/power-bi/transform-model/desktop-time-intelligence#calendar-based-time-intelligence-preview) ，屏幕的外观将有所不同，并且将在选择功能区中的 **“日历”选项** 或表格上的右键单击菜单后，在屏幕中找到“ **标记为日期表** ”选项。

指定自己的日期表时，Power BI Desktop 会对该列及其数据执行以下验证，以确保数据：

- 包含唯一值。
- 不包含任何 null 值。
- 包含连续的日期值（从开头到末尾）。
- 如果它是日期/时间数据类型，则它在每个值间具有相同的时间戳。

创建自己的日期表有两种可用方案，每种都是合理的方法：

- 第一种情况是当你使用规范或基本日期表和层次结构时。 此方案将在数据中使用符合前面所述的日期表验证条件的表。
- 第二种方案是指你使用来自 Analysis Services 的表（例如带有 dim date 字段的表），并希望将其用作日期表的情况。

指定日期表后，可以选择将该表中的哪一列作为日期列。 可以通过选择 **字段** 窗格中的表来指定要使用的列，然后右键单击该表并选择标记为日期表 日期表设置。 此时将出现以下窗口，可以从窗口的下拉列表中选择要用作日期表的列。

![Power BI Desktop 的屏幕截图，其中显示了“标记为日期表”对话框以及重要说明。](https://learn.microsoft.com/zh-cn/power-bi/transform-model/media/desktop-date-tables/date-tables_03.png)

Power BI Desktop 的屏幕截图，其中显示了“标记为日期表”对话框以及重要说明。

请务必注意，当你指定自己的日期表时， **Power BI Desktop** 不会自动为你在模型中创建它原本自身会生成的层次结构。 如果以后取消选择日期表（并且不再具有手动设置的日期表），Power BI Desktop 将针对表中的日期列为用户重新创建自动创建的内置日期表。

同样需要注意的是，当你将表标记为日期表时，Power BI Desktop 会删除内置（自动创建）的日期表。 之前基于这些内置表创建的任何视觉对象或 DAX 表达式不再正常工作。

## 将日期维度表标记为相应的数据类型

指定自己的日期表时，需要确保数据类型已正确设置。 你想要将 **数据类型** 设置为 **“日期/时间”** 或 **“日期** ”：

1. 从“字段”窗格中选择日期表，并根据需要将其展开，然后选择要用作日期的列。
	![Power BI Desktop 的屏幕截图，其中显示了“字段”窗格中的“日期”筛选器。](https://learn.microsoft.com/zh-cn/power-bi/transform-model/media/desktop-date-tables/date-tables_04.png)
	Power BI Desktop 的屏幕截图，其中显示了“字段”窗格中的“日期”筛选器。
2. 在“列工具”选项卡上，选择“数据类型”，然后选择下拉箭头以显示可用的数据类型。
	![Power BI Desktop 的屏幕截图，其中显示了“建模”选项卡并选择了“数据类型”筛选器。](https://learn.microsoft.com/zh-cn/power-bi/transform-model/media/desktop-date-tables/date-tables_05.png)
	Power BI Desktop 的屏幕截图，其中显示了“建模”选项卡并选择了“数据类型”筛选器。
3. 指定列的数据类型。

## 相关内容

有关本文的更多信息，请参阅以下资源：

- [在 Power BI 中实现基于时间的计算](https://learn.microsoft.com/zh-cn/power-bi/transform-model/desktop-time-intelligence)
- [在 Power BI Desktop 中应用自动日期/时间](https://learn.microsoft.com/zh-cn/power-bi/transform-model/desktop-auto-date-time)
- [Power BI Desktop 中日期表的设计指南](https://learn.microsoft.com/zh-cn/power-bi/guidance/model-date-tables)
- [Power BI Desktop 中的数据类型](https://learn.microsoft.com/zh-cn/power-bi/transform-model/desktop-data-types)
- 有问题？ [尝试咨询 Power BI 社区](https://community.powerbi.com/)
- 建议？ [提出改进 Power BI 的想法](https://ideas.powerbi.com/)

---

## 其他资源

培训

模块

[在 Power BI 语义模型中使用 DAX 时间智能函数 - Training](https://learn.microsoft.com/zh-cn/training/modules/dax-power-bi-time-intelligence/?source=recommendations)

通过 Power BI 中的 DAX 时间智能函数，用户能够分析和比较不同时间段的数据，从而支持实现对随时间推移的趋势、增长和性能的有见解报告。

认证

[Microsoft认证：Power BI数据分析师助理 - Certifications](https://learn.microsoft.com/zh-cn/credentials/certifications/data-analyst-associate/?source=recommendations)

演示与业务和技术要求一致的方法和最佳做法，以使用Microsoft Power BI对数据进行建模、可视化和分析。