---
title: "Python + Airflow：让企业级 ETL 系统从 “繁琐” 到 “丝滑” 的蜕变指南"
source: "https://mp.weixin.qq.com/s/kABXGfsiqHA32_uqQZJohg"
author:
  - "[[petter guo]]"
published:
created: 2026-07-27
description: "本文聚焦 Python 与 Airflow 在企业级 ETL 系统搭建中的实践，解析如何用 Python 的灵活性结合 Airflow 的任务调度能力，构建高效、可监控的数据管道。"
tags:
  - "clippings"
---
petter guo 全栈派森 *2025年7月28日 08:00*

大家好,我是 `Petter Guo`

一位热爱 `探索` 的 `全栈工程师` 。在这里，我将分享 `个人` 的 `Technical essentials` ，带你玩转 `前端` 、 `后端` 到 `DevOps` 的硬核技术，解锁 `AI` ，助你打通技术任督二脉，成为真正的 `全能玩家`!！

如果对你有帮助, 请 `点赞` + `收藏` + `关注` 鼓励下, 学习公众号为 `全栈派森` 。

### 本节你将学习到:

1

Airflow的用途, 执行器的使用, 数据源的选择

2

ETL的扩展知识

3

Docker部署Airflow实战

#### Airflow 概念

用最简单的话来说，Airflow 让数据工程师能够用 Python 代码来定义一系列任务，以及这些任务之间的依赖关系，形成一个「有向无环图」（DAG - Directed Acyclic Graph）。

1

DAG：就是你的工作流程。它由一系列的任务组成，这些任务有明确的执行顺序，且没有循环（不能形成一个无限循环）。

2

任务（Task）：DAG中的每一个节点都是一个任务，代表一个独立的工作单元，例如:

•

从数据库中提取数据。

•

运行一个 Python 脚本进行数据清洗。

•

将数据加载到数据仓库。

•

发送邮件通知。

•

触发一个机器学习模型的训练。

Airflow 最核心的组件包括:

•

Scheduler(调度器)：负责监控所有的 DAGs，并根据它们的调度（时间、事件）来触发任务运行。

•

Webserver（网络服务器）：提供一个用户界面 (UI)，让你可视化 DAG 的运行状态、查看日志、手动触发任务、管理连接和用户等。

•

Executor（执行器）：实际执行任务的机制，可以是单机执行的 LocalExecutor，也可以是分布式执行的 CeleryExecutor 或 KubernetesExecutor。

•

元数据数据库（Metadata Database）：存储 Airflow 的所有状态信息，如 DAG 的运行历史、任务状态、连接配置等

#### Airflow的用途

Airflow 的主要用途是自动化和管理复杂的数据流程（Data Pipelines），特别是在数据工程、ETL (Extract, Transform, Load)、机器学习运营 (MLOps) 等领域

具体来说，它解决了以下痛点：

1

批处理任务自动化：许多数据任务需要定期运行（例如每天凌晨同步一次数据）。Airflow 可以设置精确的排程，确保这些任务准时自动执行。

2

管理复杂依赖关系：许多任务不是独立的，它们的执行必须依赖于前一个任务的完成。Airflow 让你清晰地定义这些上下游关系，确保任务按照正确的顺序执行。

3

监控和可视化： 当你有多个复杂的数据管道时，很难知道它们的运行状况。Airflow 的 Web UI 提供了一个中央仪表板，让你一目了然地看到每个任务的成功、失败、运行时间、日志等。

4

错误处理和重试：数据任务常常会因各种原因失败（网络问题、数据格式错误）。Airflow 内置了强大的错误处理和重试机制，可以自动重试失败的任务，并在多次失败后发送通知。

5

可扩展性：从小规模的个人项目到大型企业级数据平台，Airflow 都可以通过更换 Executor（例如从 LocalExecutor 升级到 CeleryExecutor 或 KubernetesExecutor）来支持不断增长的任务量和并发需求。

6

代码即基础设施（Code-as-Infrastructure）：用 Python 代码来定义工作流程，这使得你的数据管道可以像应用程序代码一样被版本控制、测试和审查。

#### ETL 定义

ETL 是数据集成领域的一个核心概念，它代表三个关键步骤：提取 (Extract)、转换 (Transform) 和加载 (Load)。这个过程的目的是将来自不同来源的数据汇集起来，经过处理后，最终存储到一个统一的目标系统中，以便于分析、报告和商业决策。

1

提取 (Extract)

这是 ETL 过程的第一步，目标是从各种数据源中获取原始数据。数据源可以非常多样化，包括：

•

关系型数据库（例如：MySQL，PostgreSQL，SQL Server，Oracle）。

•

非关系型数据库 (例如：MongoDB, Cassandra)

•

云服务（例如：Salesforce CRM，Google Analytics，Facebook 广告）

•

文件（例如：CSV，JSON，XML，Parquet，日志文件）

•

API 接口

•

实时数据流（例如：Kafka）在提取阶段，数据通常会被复制到一个临时的“暂存区”（staging area）或“登录区”（landing zone），以供后续处理。

1

转换 (Transform)

这是 ETL 过程中的最关键且通常最复杂的一步。在这个阶段，提取到的原始数据会根据业务规则和目标系统的要求进行 `清洗` 、 `标准化` 和 `重构` 。转换的目的是确保数据的 `质量` 、 `一致性` 和 `可用性` 。常见的转换操作包括：

•

数据清洗（Data Cleansing）：处理缺失值、重复数据、不一致的格式、无效的数据点（例如，年龄为负数）。

•

数据格式转换：将不同数据类型（如日期字符串转为日期对象，数字字符串转为数值）。

•

数据规范化/去规范化：调整数据结构以适应目标数据库模式或分析需求。

•

数据聚合/汇总：将多条记录汇总成摘要数据（例如，计算每日总销售额）。

•

数据联结/合并：将来自不同数据源的相关数据整合在一起。

•

数据丰富/增强：添加额外的信息，例如通过邮政编码查找城市名称。

•

应用业务逻辑：根据特定的业务规则计算新字段。

1

加载 (Load)

这是 ETL 过程的最后一步，将经过转换和清洗的数据写入最终的目标系统。这个目标系统通常是：

•

数据仓库 (Data Warehouse)：用于存储结构化、历史性的数据，支持复杂的分析和报告。

•

Data Lake：存储原始或半结构化数据，通常用于大数据分析和机器学习。

•

数据集市（Data Mart）：为特定业务部门设计的小型数据仓库。

•

运营数据库：将清洗后的数据推送回业务应用  
加载可以是 `全量加载` （每次加载所有数据）或 `增量加载` （只加载自上次运行以来新增或修改的数据）。

#### ETL的用途

ETL 的核心用途是整合、清洗和准备数据，使其可用于业务智能 (BI)、分析和机器学习。它将分散在企业各处的异构数据转化为一个统一、高质量、有价值的资产。

具体用途包括：

1

数据整合：将来自多个系统（如销售、营销、财务、运营）的数据整合到一个中央数据库或数据仓库中，打破数据孤岛，提供企业级的统一视图。

2

商业智能和报告：为 BI 工具（如 Tableau、Power BI）提供干净、结构化的数据，以便生成精确的报告、仪表板和深入的商业洞察。

3

数据质量和一致性：通过转换步骤，ETL 过程可以清理错误数据、处理缺失值、统一数据格式，从而显著提高数据的整体质量和一致性。

4

机器学习和人工智能：为机器学习模型提供高质量、预处理过的训练数据。干净的数据是构建准确和有效 ML 模型的基石。

5

历史数据分析：将来自旧系统的历史数据整合到新平台，为数据提供更长期的上下文，帮助企业了解趋势和模式。

6

合规性与审计：许多行业要求数据必须符合特定的标准和规范。ETL 过程中的转换和清洗步骤有助于确保数据的合规性，并可以生成审计报告。

#### AirFlow部署实战

在实战之前, 先给出一个Airflow结构比较总结:

| 特性(Executor) | LocalExecutor | CeleryExecutor | KubernetesExecutor |
| --- | --- | --- | --- |
| 部署复杂度 | 最低 | 中等(需消息队列) | 最高(需k8s集群) |
| 扩展性 | 无(单机) | 高(水平扩展worker) | 极高（Pod 动态创建） |
| 高可用性 | 无（单点故障） | 高（多個 Scheduler/Worker） | 极高（K8s 自愈能力） |
| 任务隔离性资源控制 | 差（共享进程/机器） | 中等（Worker 进程隔离） | 极佳（每个任务一个 Pod） |
| 资源控制 | 粗略（整机） | 粗略（Worker） | 精细（每个 Pod 独立） |
| 成本效益 | 最低（单机固定成本） | 中等 | 灵活（按需付费） |
| 适用场景 | 开发测试、极小型生产 | 中大型生产，通用型 ETL | 大规模生产，数据密集型，微服务化 |

目前我们部署的是 LocalExecutor, 如果有需要可以进行升级到 CeleryExecutor 。

•

环境搭建

1

docker desktop 安装

![docker](https://mmbiz.qpic.cn/mmbiz_png/AibicsqrwWIbN2sV2AlNftepUfbWI4aSs02dIyvDvvNWic8uyUs4icsf7mE5fC2u6l8BlTwOkCbugJA8N7ptia5DrtA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

docker

1

docker compose 安装

![docker compose](https://mmbiz.qpic.cn/mmbiz_png/AibicsqrwWIbN2sV2AlNftepUfbWI4aSs0ic5MUBTe0kQkz9GIt7TfpG5UibtkfYObAl6CntDVIQ3lxgJYwBGVGIGg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

docker compose

1

mysql 镜像拉取

```
docker pull mysql:8.0.41
```

1

python镜像拉取

```
docker pull python:3.9-slim
```

1

编写 docker-compose.yml 文件 (已生成)

```
# docker-compose.yml
version: '3'

# 定义一个共享的配置块，避免重复
x-airflow-common: &airflow-common
  image: airflow-test3
  environment:
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: mysql+mysqldb://root:rootpassword@mysql:3306/airflow

services:
  mysql:
    image: mysql:8.0.41
    container_name: airflow_mysql
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: airflow
      MYSQL_USER: airflow
      MYSQL_PASSWORD: airflowpassword
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
    # 添加健康检查，确保数据库完全就绪
    healthcheck:
      test: ["CMD-SHELL", "mysqladmin ping -h localhost -u $$MYSQL_USER -p$$MYSQL_PASSWORD"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s # 数据库启动的宽限期

  # --- Airflow 初始化服务 (airflow-init) ---
  airflow-init:
    <<: *airflow-common # 继承 common 配置
    command: >
      bash -cx "
      exec airflow db migrate &&
      exec airflow users create --username airflow --password airflow --firstname Airflow --lastname User --role Admin --email admin@example.com
      "
    depends_on:
      mysql:
        condition: service_healthy # 确保数据库健康后才执行初始化

  airflow:
    image: airflow-test3
    environment:
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: mysql+mysqldb://root:rootpassword@mysql:3306/airflow
      AIRFLOW__WEBSERVER__AUTH_ROLES_MAPPING: '{"user_name_from_external_system": "Admin"}'
      AIRFLOW__CORE__EXECUTOR: airflow.executors.local_executor.LocalExecutor
      IRFLOW__CORE__DAGS_FOLDER: /usr/local/airflow/dags
    ports:
      - "8081:8080"
    volumes:
      - ./:/usr/local/airflow/
    depends_on:
      airflow-init:
        condition: service_completed_successfully
      mysql:
        condition: service_healthy # 确保数据库健康后才启动 Airflow

  # --- Airflow Scheduler 服务 ---
  airflow-scheduler:
    <<: *airflow-common
    environment:
      IRFLOW__CORE__DAGS_FOLDER: /usr/local/airflow/dags
    command: ["airflow", "scheduler"]
    volumes:
      - ./:/usr/local/airflow/
    depends_on:
      airflow-init:
        condition: service_completed_successfully
      mysql:
        condition: service_healthy

networks:
  backend:
    driver: bridge
  frontend:
    driver: bridge
volumes:
  mysql_data:
```

1

编写 dockerfile 文件 (已生成)

```
# 基于官方 Python 镜像构建
FROM python:3.9-slim

# 设置环境变量
ENV AIRFLOW_HOME=/usr/local/airflow

# 创建工作目录
WORKDIR ${AIRFLOW_HOME}

# 安装依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libmariadb-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# 拷贝 requirements.txt
COPY requirements.txt .

# 安装 Python 依赖，包括 mysqlclient
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Airflow Web 端口
EXPOSE 8081

# 初始化数据库并启动
# CMD ["airflow", "standalone"]
CMD ["airflow", "webserver"]
```

1

执行 docker build -t airflow-test3(名字要和dockercompose文件里的保持一致).

2

执行 docker-compose up -d

![服务启动](https://mmbiz.qpic.cn/mmbiz_png/AibicsqrwWIbN2sV2AlNftepUfbWI4aSs0mN0P0k2lAvgQRNIIQkSQgn8HLnicAMIQs2Kh6XmYqFSXwqFDZ1WktTA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

服务启动

![服务启动成功](https://mmbiz.qpic.cn/mmbiz_png/AibicsqrwWIbN2sV2AlNftepUfbWI4aSs0Cmlt757nv2uRjCpkWkSiaib95P7blxzVvffW2d3O8OxMfic42mDwQPyVQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

服务启动成功

1

执行 docker exec -it airflow-test3 bin/bash

2

初始化mysql

```
初始化mysql：
- airflow db init
- airflow users create \
  --username admin \
  --password admin \
  --firstname admin \
  --lastname admin \
  --role Admin \
  --email admin@example.com
```

访问127.0.0.1:8081 用户密码: admin/admin

![web UI](https://mmbiz.qpic.cn/mmbiz_png/AibicsqrwWIbN2sV2AlNftepUfbWI4aSs0FhUpcnJjhQkrt8dl1nG7iaLdp6Qic2JUNMmTd2DTUiam17Aj74InYFoWw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

web UI

#### 注意

上面所讲皆为我研究 `3天` 的 `成果`, 如果按照我的流程操作, 可以少走弯路, 当然, 你在实操的过程可能会遇到一些其他问题, 需要自行解决(途径有很多), 也可以进行留言, 一起进行技术交流。

`如果你也想搭建自己的ETL系统, 那就赶紧实操起来吧 !!!`