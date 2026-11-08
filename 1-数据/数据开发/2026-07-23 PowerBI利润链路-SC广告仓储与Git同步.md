---
tags:
  - PowerBI
  - 数据仓库
  - Amazon-SC
  - 利润链路
  - Codex同步
created: 2026-07-23
source: Codex 对话同步
project_path: D:\powerbi项目
---

# 2026-07-23 PowerBI 利润链路更新同步

## 本次对话目标

把 Seller Central 广告费接入利润链路，并把仓储费从原来的 VC 分摊扩展到 SC MFN，同时检查记忆、SQL、存储过程、全链路刷新、性能和 Git 同步状态。

## 已完成更新

### 1. SC 广告费接入

- 原始文件目录：`D:\powerbi项目\资料\SC广告`
- `2501` 到 `2504` 文件按 `Date range` 拆成日维度，按区间天数求日均。
- 其他 SC 广告文件本身为日维度，直接按日匹配。
- SC 广告源表入库标签：`Amz SC`。
- 最终利润表不区分广告源里的 FBA/MFN，而是分摊到：
  - `Amz SC FBA`
  - `Amz SC MFN`
- 同一天同 ASIN 如果 FBA/MFN 都有销售，按销量分摊广告费。
- 如果某天某 ASIN 完全没有 SC 销售行，则补 `Amz SC FBA` 和 `Amz SC MFN` 零销售行，并均摊广告费。
- SC 广告源文件 Total cost 与最终分摊结果一致：`16,141.4000`。

### 2. SC 仓储费分摊规则

用户确认的业务规则：库存是海外仓库存，不区分渠道；但 `Amz SC FBA` 直接进入亚马逊仓，不经过海外仓，因此不参与海外仓仓储费分摊。

当前规则：

- 参与海外仓仓储费分摊：`Amz VC`、`Amz SC MFN`
- 不参与海外仓仓储费分摊：`Amz SC FBA`
- 仓储费池粒度：`date + physical_sku`
- 分摊逻辑：同日同 physical_sku 按销售额分摊；销售额为 0 时按行数均摊。
- 最终仓储费总额：`503,958.0448`
- `Amz SC FBA` 仓储费为 `0`。

渠道仓储费结果：

| 渠道 | 仓储费 |
| --- | ---: |
| Amz VC | 487,895.6761 |
| Amz SC MFN | 16,062.3687 |
| Amz SC FBA | 0.0000 |

### 3. 最终利润表口径更新

最终表：`data_market.bi_profit_calc_08_storage_fee_allocation`

当前最终粒度：`channel + date + asin`

当前正式利润渠道：

- `Amz VC`
- `Amz SC FBA`
- `Amz SC MFN`

VC PO/DF/DI 仍只是供货结构、Coop、加权成本口径，不直接和终端销售额相加。

### 4. SQL / 存储过程优化

曾尝试改写 Step08 仓储分摊 SQL，但执行计划退化，导致刷新超时。随后已回退到稳定逻辑。

最终采用低风险优化：删除最终表上重复的普通索引，只保留唯一索引 `channel + date + asin`。

结果：

- Step08 优化前稳定耗时约：`52.3 秒`
- 清理重复索引后 Step08：`42.8 秒`
- 单 Step08 节省：`9.5 秒`
- Step08 提升约：`18.2%`
- 折算全链路整体提升约：`2.8%`

### 5. 全链路刷新结果

完整 14 步全链路刷新已通过。

| 指标 | 数值 |
| --- | ---: |
| 全链路耗时 | 333.8 秒 |
| 最终表行数 | 530,068 |
| `channel + date + asin` 唯一数 | 530,068 |
| 重复键 | 0 |
| 日期范围 | 2025-01-01 至 2026-07-22 |
| SalesQty | 150,283 |
| SalesAmt | 13,559,212.2211 |
| Product Cost | 6,919,462.8028 |
| Coop | 3,117,630.5430 |
| Promo | 800,004.4800 |
| Ads | 316,907.8600 |
| Storage Fee | 503,958.0448 |

渠道拆分：

| 渠道 | 行数 | SalesQty | SalesAmt | Ads | Storage Fee |
| --- | ---: | ---: | ---: | ---: | ---: |
| Amz VC | 523,128 | 138,690 | 12,210,476.5300 | 300,766.4600 | 487,895.6761 |
| Amz SC FBA | 3,689 | 8,003 | 734,365.0995 | 11,542.2203 | 0.0000 |
| Amz SC MFN | 3,251 | 3,590 | 614,370.5916 | 4,599.1797 | 16,062.3687 |

对账结果：

- 总广告源表标准 ASIN 金额：`316,907.8600`
- 最终表广告金额：`316,907.8600`
- SC 广告源表金额：`16,141.4000`
- 最终 SC FBA + MFN 广告金额：`16,141.4000`
- VC 促销源表标准 ASIN 金额：`800,004.4800`
- 最终表促销金额：`800,004.4800`

质量检查：

- `DQ-PROFIT-001` PASS
- `DQ-PROFIT-002` PASS
- `DQ-COOP-001` PASS
- `DQ-STORAGE-001` PASS
- `DQ-CHANNEL-001` PASS
- `DQ-ADS-001` PASS
- `DQ-PROMO-001` PASS
- `DQ-MAPPING-001` PASS
- `DQ-MAPPING-002` PASS
- `DQ-COST-001` WARN：成本缺失 35 行，影响销售额 `6,688.4700`

## Git 同步情况

已提交并推送到 GitHub：

- `19e7c7a Integrate SC ads and storage allocation`
- `0001f9a Stop tracking generated output files`

第二个提交用于纠正：`output/` 下的 CSV 属于生成结果/源数据快照，不应进入 Git。当前已：

- 将 `output/` 加入 `.gitignore`
- 从 Git 跟踪中移除 `output/*.csv`
- 保留本地文件，不删除
- 本地 `main` 与 `origin/main` 已对齐

注意：`19e7c7a` 历史提交中曾短暂包含过 `output/*.csv`；当前最新版本已经不再跟踪。如果后续要求从 Git 历史中彻底抹除，需要单独做历史重写，风险更高。

## 项目记忆同步

已更新项目内正式记忆：

- `项目记忆/memory_system/modules/02_profit_chain.md`
- `项目记忆/memory_system/modules/05_ads_promo.md`
- `项目记忆/memory_system/modules/06_inventory_storage.md`
- `项目记忆/memory_system/modules/08_quality_checks.md`
- `项目记忆/memory_system/00_主记忆索引.md`
- `项目记忆/memory_system/04_口径与术语字典.md`
- `项目记忆/memory_system/05_规则总表.md`
- `项目记忆/当前有效规则.md`
- `docs/利润主表计算规则.md`

已新增变更单：

- `CR-20260722-001_SC广告接入.md`
- `CR-20260722-002_SC_MFN仓储费分摊.md`

## 后续注意事项

1. `output/`、原始业务文件、成本报告、临时文件不应同步到 Git。
2. SC FBA 不参与海外仓仓储费分摊，这条规则后续不要被普通库存分摊逻辑覆盖。
3. SC 广告源标签为 `Amz SC`，最终利润渠道为 `Amz SC FBA` / `Amz SC MFN`。
4. 后续若新增 Walmart 或其他渠道，最终表唯一键仍必须包含 `channel`。
5. 当前唯一已知 WARN 是成本缺失 35 行，影响销售额 `6,688.4700`。

## 相关 Obsidian 笔记

- [[跨境电商数据治理与多渠道基础模型]]
- [[数据刷新与质量检查机制]]
- [[Amazon VC P&L利润链路]]
- [[Amazon SC SP-API凭证申请待办]]
