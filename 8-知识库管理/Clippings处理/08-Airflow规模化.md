---
type: summary
status: summarized
importance: S
review_priority: key
source_path: "1-数据/数据开发/大规模运行 Apache Airflow 的经验和教训.md"
needs_human_review: true
verification_status: unverified
---

# 大规模运行 Apache Airflow：经验与教训

原文：[[1-数据/数据开发/大规模运行 Apache Airflow 的经验和教训]]

## 一句话结论
Shopify 的大规模实践表明，Airflow 扩展关键不只在 Executor，还在文件分发、元数据保留、DAG 所有权与策略、调度错峰和资源隔离。

## 核心观点
- GCSFuse 在大规模 DAG 访问下可能成为瓶颈，文章采用 Kubernetes NFS 作为快速卷并与 GCS 同步。
- 元数据持续膨胀会拖慢数据库、UI 和迁移，可设保留策略清理，但会牺牲长期回填与历史能力。
- 清单文件把 DAG 映射到团队、仓库、命名空间和约束，策略可阻止越权队列、池和 Kubernetes 命名空间。
- 对自动生成 DAG 使用确定性随机调度，能够错开峰值、平滑负载。
- Pool、priority_weight、Celery 队列和隔离 Worker 可处理资源争用，但调度器、数据库和 Kubernetes IP 仍可能是全局瓶颈。

## 个人价值
为从单机 ETL 升级企业级、多租户数据平台提供架构与运维检查清单，尤其适用于 BI 刷新、机器学习、Iceberg/dbt 等混合负载。

## 关联已有笔记
- [[1-数据/数据开发/Python + Airflow：让企业级 ETL 系统从 “繁琐” 到 “丝滑” 的蜕变指南]]
- [[1-数据/数据治理/AI时代，数据治理到底应该怎么做？]]

## 推荐动作
按现有 DAG 数、并发、峰值、SLO 和历史保留测算瓶颈；先建立 owner/namespace、pool/queue、权限策略、元数据清理和监控，再评估 Celery/Kubernetes 或多实例隔离。

## 最小实践及验收
为现有 DAG 增加 owner、namespace、资源池、队列和保留策略，模拟高峰错峰运行。验收：任务峰值下降、关键任务 SLO 达标、越权 DAG 被拒绝、历史清理可回滚且审计要求仍满足。

## 需验证
文章基于 Airflow 2.2/2022，需核对当前版本架构和官方推荐；NFS+GCS 的一致性、故障恢复和安全；28 天保留对审计/回填的影响；文中代码有排版或语法损坏，不可直接复制。

## 阅读建议
把它当作规模化设计原则，而不是现成部署脚本；先用压测和容量数据验证，再引入复杂基础设施。
