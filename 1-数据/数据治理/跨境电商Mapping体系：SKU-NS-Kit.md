# 跨境电商Mapping体系：SKU-NS-Kit

## 为什么Mapping是利润项目的核心

跨境电商利润分析中，销售、广告、促销、成本、库存和供应商数据经常使用不同产品编码。如果不先治理 Mapping，利润表会出现 PL 缺失、成本缺失、费用串 SKU、行数放大等问题。

这个项目中至少有三类核心 Mapping，不能混用。

## 三类核心Mapping

| Mapping | 解决的问题 | 典型对象 | 当前表 |
| --- | --- | --- | --- |
| SKU mapping | 销售、广告、促销、渠道上架 SKU 回到内部分析 SKU、ASIN、PL/PM | ASIN、Main-SKU、ChannelSKU、Channel、PL | `bi_sku_mapping`、`bi_sku_channel_mapping` |
| NS mapping | 成本源、NetSuite/SRP、外部产品 ID 回到内部 SKU | NS Item、SRP、外部产品 ID | `bi_hj_mapping` |
| Kit mapping | Kit 父 SKU 和子 SKU 的成本、库存关系 | parent_sku、child_sku、child_qty | `bi_kit_mapping` |

## NS mapping 的准确理解

`bi_hj_mapping` 是历史表名，但业务上更准确应理解为 NS / SRP 映射表。

它不是只服务恒建或 HJ 产品，而是覆盖自有产品和外部产品：

- 自有产品：内部 SKU 与 NS/SRP SKU 通常相同。
- 外部产品：内部 SKU 与外部产品 ID / NS Item 需要通过映射桥接。
- 成本源来自外部账单、出货、订单或对账单时，往往要先识别源产品 ID，再通过 NS mapping 回到内部 SKU。

## SKU mapping 标准流程

不能直接把原始人工录入 sheet 导入数据库。标准流程是：

1. 原始表放入 `map/handoff_package/01_原始人工录入表`。
2. 读取 `map/handoff_package/MEMORY.md`。
3. 运行 `mapping_processor/analyze_mapping.py`。
4. 运行 `mapping_processor/build_core_three_tables.py`。
5. 使用 `03_数据库上传表/bi_sku_mapping_ready.xlsx` 入库。
6. 刷新 `bi_sku_channel_mapping`。
7. 重跑利润链路。

## 去重原则

允许：

- 同一个 `ChannelSKU` 在 `Amz VC` 下对应多个不同 ASIN。

必须消除：

- 同一个 ASIN 在 ready 表中出现多条可 join 记录。

原因：

- 利润链路 Step01 使用 ASIN join。
- 如果同一个 ASIN 多行，最终表可能按 `date + asin` 被放大。
- 但同一个产品多 ASIN 是真实业务场景，不能按 `Channel + ChannelSKU` 简单压缩。

## Step01利润链路规则

- 只取 `Channel = Amz VC`。
- 当前不按 `UsedStatus = Yes` 过滤。
- Join key = ASIN。
- 如果同一 ASIN 多行，用 `row_number()` 兜底只取一行。
- 最终表必须保持 `date + asin` 唯一。

## 可沉淀经验

Mapping 项目不要从“字段怎么导入”开始，而要先回答：

- 哪个 Mapping 服务销售侧？
- 哪个 Mapping 服务成本侧？
- 哪个 Mapping 服务库存和 Kit 侧？
- 哪些重复是业务允许的？
- 哪些重复会造成事实表放大？
- 哪个字段才是当前链路的 join key？

## 来源

- `D:\powerbi项目\项目记忆\memory_system\modules\01_mapping.md`
- `D:\powerbi项目\map\handoff_package\MEMORY.md`

