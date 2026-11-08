---
title: "腾讯DataBuddy语义层架构及工程落地-这次是真的领先阿里了"
source: "https://mp.weixin.qq.com/s/xsX_YPXoQEk1FSYLuzISgw"
author:
  - "[[点赞加关注]]"
published:
created: 2026-11-09
description: "一文彻底搞懂腾讯DataBuddy到底怎么设计的？为什么靠谱！"
tags:
  - "clippings"
---
点赞加关注 数道至简 *2026年11月4日 07:30*

上次我分享了腾讯DataByddy语义层实战： [DataBuddy是如何落地语义层的](https://mp.weixin.qq.com/s?__biz=MzU0MTY5NTU4Mw==&mid=2247485110&idx=1&sn=c0de0aea1a17a3655e38d03011ad6843&scene=21#wechat_redirect) 大家交流的都很热烈，需要PPT的也很多。需要的可以私信我加好友我私发您。

但大多数朋友看完还是一头雾水：到底是怎么建的？我只能说这个材料是有点抽象，没点领域基础和实践经验的很难理解。

正好上周参加了腾讯的2026数据生态大会，现场也跟一些专家进行了交流。我今天结合线下交流的一些心得和一些开发材料，给大家换个思路总结下。保证你能看得懂，个人觉得很值得学习，毕竟工程落地的真不多。

先介绍官方的语义层架构

来看看DataBudy的架构图，语义层只是其一关键部分：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/sooib80cYllj0ehcq1ia45fAOFsNlyiaibc4iahmiceDpLMJ9yUnBAMrQydFFT9bGb9E1ibzFDg3HrFibn6YmuvkrYPDX9JkKoaTkTsuzbHYggz3eX0/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

语义层具体架构图见下面的图：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sooib80cYllgkicMlLezEiatgo4Sfnbo76vD5Dt1va22VpibfU9RHsovnz6n0ajUH178SMggQyibmJic7Dvgpgfhx7uw6Jw6Qj3J0OuIhJVR5Oj58/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

- Catalog统一资产目录，摸清数据底账，搞清表、字段、来源和上下游依赖。它是另外两层的地基，得先把「这张表这个字段是什么、从哪来」摸清楚，字段来源说不清，上面就没法定口径，更没法挂进骨架。
- Semantic Model语义模型，统一指标口径，定义销售额含不含税、怎么拆分维度。它回答「过去有多少」
- Ontology Model本体模型，把数字放回业务关系里，定义客户、订单、预警规则和应对动作。它回答「是什么、为什么、会怎样、该怎么办」。

一句话总结：用语义模型管住“怎么算”，用本体模型定住“算的是谁”，并以三层架构和双翼治理将其落地为可执行、可审计的工程系统。

接下来用企业常见的DAU指标这个具体问题串联起DataBuddy 对企业 AI 语义架构的设计思路。

简单说用户问：“上个月华东区客户的 DAU 是多少？”

![image](https://mmbiz.qpic.cn/mmbiz_jpg/sooib80cYllhwiarBuxibaaO701dYzkUWlmpgo1dFRKfB1DKIBwl5VwfWzWLgb5ov1105FSg6u4I8wmmS6te4vvBYiaBWJnpzeTm9iaib8EkYicHeU/640?wx_fmt=webp&from=appmsg&watermark=1#imgIndex=2)

这个问题其实触及了两个重要方面：DAU指标口径咋定义的？啥是客户？这里的“华东地区”在企业一般是维度或者放在业务关系中。

（另外语义层的Catalog本次先不详细论证，你理解大家此前数据治理留下的数据目录、血缘、元数据等即可，感兴趣后面详聊。）

“DAU 怎么算”归语义模型：按账号、自然人还是设备去重？登录即活跃还是有效操作才算？口径不统一，同一个问题就有多个答案。

语义模型要做的，是把“DAU”固定成唯一一段计算逻辑，可预览 SQL、可追血缘。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sooib80cYllgkVKQLicG8wfMHGL1ocI3ukNylYeWOL7eA2MVThY8z6dDAFoMGss8icEXvicQQ1ap4atOsaZnLd1iaeGesSyY9onpnN8ZqL6CPdz4/640?wx_fmt=webp&from=appmsg&watermark=1#imgIndex=3)

“客户指的是谁”归本体模型：销售部认为有转化的才叫客户，市场部认为有需求但没下单的也算。同一批账号，在业务上其实是“客户”与“商机”两个不同对象。口径错了，得到一个错的数字；对象错了，那就错的离谱了。

大多数团队只做了口径统一，结果只能获取到“算得越来越准、却始终不知道自己在算谁”的助手。

放回那句提问里看，它们在语义层位置是这样的：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sooib80cYllgCibXOoFPy5Uq3YwVAmfpXZFEDFgxsoicsiaMqWchkbNOXffAGkqpzAVbaferQaT1ibwEXGibEVuE3yZeYtM826U9Mibjl3t7MV85XM/640?wx_fmt=webp&from=appmsg&watermark=1#imgIndex=4)

接下来分别解决这两个问题

1，先通过语义建模解决“DAU”是什么？

语义模型：把口径收拢成唯一可执行定义。

语义建模在 DWD/DIM 明细层之上做两件事：

![image](https://mmbiz.qpic.cn/mmbiz_jpg/sooib80cYllgqxydzZ1W2qczIdaUfZeQy8RTG1qeUc23vrOibYDsZINd1LvORuY95bcv5Mpr0bv4IOicRsHZ7ODUUuXhc4NbbgtjxbUicqCLeWg/640?wx_fmt=webp&from=appmsg&watermark=1#imgIndex=5)

- 搭模型：以事实表为中心连接维度表，固定 JOIN 路径和可用维度，不再让 Agent 每次猜。
- 定指标：先定原子指标，再派生衍生指标，指标挂在模型上，天然知道能按哪些维度拆、从哪张底表来。

这一做法还改变了传统数仓的建法：只需建好 DWD/DIM 两层，往上的 DWS/ADS 不再靠 ETL 逐场景堆表。下游怎么用被挪到语义层用声明表达，换个维度看数，不是加一张表，而是换一个 group\_by。这个放在后续详细的聊。

2，再通过本体建模解决“客户”是什么？

本体模型：给 AI 一幅业务架构

![image](https://mmbiz.qpic.cn/mmbiz_jpg/sooib80cYllhLdrk5OEG1p1RZv3B4hR3TwviaE8FRc54RCeGxSksrg18sXLEH1QU97k17onRXKham7TfZXrLbvzf8otK7ArlcJygCAlLCNNd8/640?wx_fmt=webp&from=appmsg&watermark=1#imgIndex=6)

本体模型补的不是数据，而是那句从没被记录下来的业务声明。它由五个要素构成：

![image](https://mmbiz.qpic.cn/mmbiz_jpg/sooib80cYllgPKVialriawK2ZaWQlXoIzMOdHn2uY5mT5JqN2OSL32AlWF8vDWiaicpVcVLsFgC4DibFz16jaqI2IicFNGDcEzW3mEj46M0Ax6WsMM/640?wx_fmt=webp&from=appmsg&watermark=1#imgIndex=7)

- 对象：客户、商机、订单等业务实体；
- 属性：对象的画像，如累计消费额、意向评分；
- 关系：对象之间的语义连线，如“商机可以转化为客户”；
- 规则：骨架上的约束，如“累计消费额 > 50 万的客户，流失预警须同步客户成功团队”；
- 动作：可执行的操作，如派跟进任务、发起挽留。

前三个划定 AI 面对的是什么样的世界，后两个规定它能做什么、该怎么做。对象和关系让 AI 知道“算的是谁”，规则和动作让它从“会算”走到“会办”。

语义架构中横向“两翼”是质量治理与安全治理：质量治理防腐化，安全治理防失控，贯穿全部三层。

权限在查询编译期就生效，模型根本看不到无权看的数据。

接下来要论证：为什么DataBuddy团队的这套语义方案是可信的？

- 第一，执行是确定的：Agent 只负责检索语义、匹配指标，从语义查询翻译到物理 SQL 的全过程发生在引擎内部，没有一步经过 LLM。同一个语义查询，任何时候执行都得到同一个结果。
- 第二，结果可溯源：每次查询带来源与 QueryId，可回放、可审计；Agent 的每一次动作也留痕——命中了哪条规则、用的哪个口径、谁有权执行。
- 第三，准确率经过实测：同一批业务问题，走语义层准确率 95.9%，裸 NL2SQL 仅 83.5%；而且两条路径用的是同一个模型，差别只在于有没有把表怎么连、维度有哪些、指标怎么算写下来。准确率的天花板不在模型那一侧，而在你有没有把业务定义交给它。

总结：

回到开篇：再问“上个月华东区客户的 DAU 是多少”，链路变成：

- 本体先答“算的是谁”：客户是有成交转化的对象，与商机严格区分；
- 语义再答“怎么算”：DAU 按自然人去重、有效操作即活跃、自然月口径。

Agent给出的不再是孤立的 12.7 万，而是客户 DAU 8.3 万（留存看这个）和商机 DAU 4.4 万（转化潜力看这个），并顺带回答上月有多少商机转成了客户。再往下，Agent 还能按规则对客户侧活跃度下滑的大客户同步客户成功团队、对超 7 天未跟进的高意向商机派发跟进任务写回 CRM——从“答一个数”走到“据此办一件事”。

到这一整套语义层的架构及细节通过精简的阐述已经介绍完了，这东西落地你我都知道是一个系统性工程，但腾讯已经替你想好了，他们为此设计了通过自然语言的语义和本体建模，通过AI设计，人工审核校验的方式帮你的业务迅速落地。

最后：

我暂时还没有DataBuddy的账号进行具体测试验证，产品的成熟度还没发下定义，从现场其客户分享用DataBuddy的实践来看，效果还可以。

现场我了解到腾讯内部早就酝酿几个DataAgent产品，最后DataAgent先走到前台，并且，这套产品已经在很多大型，中小型企业及个人应用。腾讯围绕WorkBuddy的AI应用生态正在迅速构建，这不也是他最熟悉的领域么。

最后的最后，说点题外话：语义层和本体论在国内提了很久很久，落地的或者说有客户背书的寥寥无几。腾讯DataByddy团队牛X!!!!!在大数据领域在业内腾讯一直被阿里甚至是百度甩在身后，但由CodeBuddy为起点，顺手做的WorkBuddy却成了银弹，再到近期的DataBuddy,，uddyOne。腾讯用90天100个大版本迭代让他在AI领域的应用目前在国内甚至是国际上都是绝对领先。

古法搓文章比较辛苦，欢迎大家批评指正，也欢迎关注、私信、交流。后续有机会拿到DataBuddy体验账号再给大家分享。

Data for AI · 目录