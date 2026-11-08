# 跨境电商成本COGS归集方法

## 核心判断

跨境电商成本不是单一 COGS 表就能解决的问题。尤其在同时经营自有产品和外部供应商 / 货盘产品时，成本需要从内部成本表、外部供应商对账、订单、出货账单和多个 Mapping 逐月归集。

## 当前项目成本定位

- 成本结果表：`data_market.bi_vc_weighted_cost`
- 利润链路成本步骤：`data_market.bi_profit_calc_02_cost`
- 成本按月计算
- 主键：`year + month + main_sku`
- 成本基础表是跨渠道共享数据，不在源表层强贴 `Amz VC`
- 生成 VC 利润成本时，再结合 VC PO / DF / DI 结构生成渠道专属结果

## 主要成本来源

- 内部成本表：`AA - HEXAGO - MASTER PO LOG - 仅限HEXAGO内部`
- Giga 对账单
- 恒建订单
- 粤强产品成本
- 其他外部产品发货或出货账单

内部成本表不完整，因此不能单独代表全量成本。

## 成本来源归集原则

1. 保留各成本来源的原始文件、来源批次、月份、产品 ID、数量、金额和成本口径。
2. 内部成本表和外部发货 / 对账 / 订单来源先进入共享成本基础。
3. 按月计算移动平均成本。
4. 同一月份同一产品 ID 多来源时，必须保留来源血缘并做数量、金额守恒检查。
5. 外部产品成本不能只靠内部 SKU 直接匹配，应先识别源产品 ID，再用 NS mapping 回到内部 SKU。
6. 渠道利润成本在最后一层根据具体渠道上下文计算。

## 成本匹配逻辑

推荐优先级：

1. 直接按 `main_sku` 匹配。
2. main_sku 取不到，尝试该 main_sku 的 `channel_sku`。
3. Kit 父 SKU 按 Kit mapping 回到子 SKU。
4. NS / 外部产品 ID 按 NS mapping 反向找我方 SKU。

## DI与非DI成本

Amazon VC 中 DI 和非 DI 成本结构不同：

- DI 没有海运费和关税。
- 非 DI 有海运费和关税。
- 终端销售无法直接识别 DI / 非 DI，需要用 VC 过去 12 个月供货结构估算。

如果 VC channel mix 已有目标 SKU 月份但 `data_source = 'no_data'`，weighted cost 应默认 `non_di_pct = 1`、`di_pct = 0`，不能让已命中的成本被 0 比例清空。

## Kit成本

Kit 产品不应简单寻找父 SKU 成本。更稳妥的方式是：

- 识别 Kit 父子件关系。
- 按子 SKU 成本乘以数量。
- 子件成本完整时，才生成可靠的 Kit 父 SKU 成本。

## 特殊规则管理

成本项目中不可避免会出现特殊规则，例如 SKU 在不同月份使用不同外部产品 ID，或者某个 SKU 某月经业务确认可用前后月成本填充。

这些规则必须：

- 有规则编号。
- 有生效范围。
- 有关联变更单。
- 有验证记录。
- 不升级成未经验证的通用规则。

## 来源

- `D:\powerbi项目\项目记忆\memory_system\modules\03_cost.md`
- `D:\powerbi项目\项目记忆\memory_system\modules\09_special_rules.md`
- `D:\powerbi项目\sql\06_refresh_bi_vc_weighted_cost.sql`

