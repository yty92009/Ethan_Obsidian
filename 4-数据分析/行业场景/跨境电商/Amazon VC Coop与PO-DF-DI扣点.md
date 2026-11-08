# Amazon VC Coop与PO-DF-DI扣点

## Coop的业务问题

Amazon VC 终端销售报告无法直接看出商品是 DI、PO 还是 DF 方式进货。因此，Coop rate 不能直接从终端销售表读取，而要借助供货口径销售表中过去 12 个月 DI / PO / DF 金额比例进行加权估算。

## 当前固定扣点

- PO：25.25%
- DF：19.25%
- DI：4.75%

## 当前表

- Coop rate 表：`data_market.bi_vc_coop_rate`
- 利润链路步骤：`data_market.bi_profit_calc_03_coop`
- `bi_vc_channel_mix` 和 `bi_vc_coop_rate` 都是 VC 专属事实
- 当前统一渠道：`channel = 'Amz VC'`

## 缺失补救规则

当 Coop rate 缺失时，当前已批准的业务默认规则为：

- Jack 缺失默认 DF：19.25%
- Nicole 缺失默认 PO：25.25%
- 不允许有销售额但 `coop_rate = 0`

这类默认值必须保留来源状态，不能伪装成真实匹配。

## 常见状态

- `coop_matched`
- `coop_matched_hj_alias`
- `coop_default_df_by_pl`
- `coop_default_po_by_pl`

## 可复用经验

Amazon VC 扣费、Coop、供货结构和终端销售之间存在口径差异。做利润模型时，不应该为了凑齐字段直接把供货口径和终端销售口径合并，而应该明确：

- 哪张表代表终端销售？
- 哪张表代表 PO / DF / DI 结构？
- 加权比例的观察窗口是什么？
- 默认值是谁确认的？
- 默认值是否可追溯？

## 来源

- `D:\powerbi项目\项目记忆\memory_system\modules\04_coop.md`
- `D:\powerbi项目\sql\02_refresh_bi_vc_coop_rate.sql`
- `D:\powerbi项目\sql\09_refresh_bi_profit_calc_03_coop.sql`

