# Amazon VC P&L利润链路

## 当前定位

当前 P&L 链路用于计算 Amazon VC terminal / endpos 口径下的利润结果。最终表为 `data_market.bi_profit_calc_08_storage_fee_allocation`，粒度是 `date + asin`，所有行当前均为 `channel = 'Amz VC'`。

这条链路的关键点是：它不是单纯销售事实表，而是一个利润承载 spine。没有销售但有广告或促销费用的标准 ASIN，也需要进入最终表。

## 主表骨架

主表 ASIN 来源包括：

- `public.report_vendor_sales.asin`
- `data_market.bi_ads.advertised_product_id`
- `data_market.bi_promo_spend.asin`

清洗规则：

- 只保留标准 ASIN：`^[A-Z0-9]{10}$`
- Ads / Promo 只吸收 `channel = 'Amz VC'`
- Promo 中金额、日期等脏 ASIN 不进入主表

## 14步刷新顺序

1. `refresh_bi_amz_vc_sales_spine`
2. `refresh_bi_profit_calc_01_sales_mapping`
3. `refresh_bi_sku_channel_mapping`
4. `refresh_bi_vc_channel_mix`
5. `refresh_bi_vc_weighted_cost`
6. `refresh_bi_vc_coop_rate`
7. `refresh_bi_profit_calc_02_cost`
8. `refresh_bi_profit_calc_03_coop`
9. `refresh_bi_profit_calc_04_promo`
10. `refresh_bi_profit_calc_05_ads`
11. `refresh_bi_inventory_daily`
12. `refresh_bi_profit_calc_06_inventory_dimension`
13. `refresh_bi_profit_calc_07_storage_fee`
14. `refresh_bi_profit_calc_08_storage_fee_allocation`

## 关键设计判断

### VC终端销售和供货结构不能混算

Amazon VC 的终端销售表现和公司向 Amazon 的供货结构属于两个不同口径。终端销售用于 SalesAmt 主事实，PO / DF / DI 供货结构用于 Coop rate 和 weighted cost 估算。

### 利润表必须有渠道隔离

当前虽然只做 `Amz VC`，但未来如果接入 `Amz SC` 或 `Walmart`，统一事实表业务键至少要包含 `channel + date + product_key`，不能沿用单渠道时代的隐含假设。

### Ads/Promo先聚合再Join

广告和促销必须先按 `channel + date + asin` 聚合，再 join 到利润 spine，避免明细 join 导致金额放大。

## 验收关注点

- `date + asin` 是否唯一。
- SalesAmt 是否守恒。
- PL 是否为空。
- 有销售额但 Coop rate 是否为 0。
- Ads / Promo 标准 ASIN 源表金额是否等于最终表金额。
- 仓储费分摊后金额是否与 physical SKU 库存池一致。
- VC 专属表是否全部为 `channel = 'Amz VC'`。

## 来源

- `D:\powerbi项目\项目记忆\memory_system\modules\02_profit_chain.md`
- `D:\powerbi项目\项目记忆\memory_system\04_口径与术语字典.md`
- `D:\powerbi项目\sql\01_amz_vc_sales_spine.sql`

