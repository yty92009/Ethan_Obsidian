---
title: "一篇文章讲清楚 AI Agent 的核心概念：从 Token、Skill、RAG 到 MCP、SDD 和 Harness 工程"
source: "https://mp.weixin.qq.com/s/8xtOwZmoMO2_sHuKx1W2FA"
author:
  - "[[AgentGuide]]"
published:
created: 2026-11-05
description: "一篇文章讲清楚 AI Agent 的核心概念：从 Token、Skill、RAG 到 MCP、SDD 和 Harness 工程"
tags:
  - "clippings"
---
AgentGuide AgentGuide *2026年5月18日 09:10*

## 1、Agent

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmeYd3ibOSCPLjYibElxd00GBKWQHZvAib1QkArGawXS2crpqHVe4osResuIubdnydrjkjwAk9ykxnYQzmPmLMIQxXeibOtNEGjC4wE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

Agent是以 LLM 为核心，具备规划（Planning）、记忆（Memory）和工具调用（Tool Use）能力，能够自主拆解复杂任务、循环执行、感知反馈并持续推进任务直到完成的计算实体，实现从“文本生成”到“任务自主执行”，不再只是被动响应指令，而是能像人类员工一样，自主实现任务闭环。

## 2、大模型预训练

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nkicicwORVWmfX5InibqdvRTZHeiaetvCehbZoBTlrnmTiaTfvRvo2DFxDtXq4Ma1Op91u03Sz3betedibEeuFpYmKYIibCvNcf6icmZ6sasYCiaDBvM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

预训练是在海量通用数据上训练模型，让它先学会语言规律、通用知识和基础能力，训练出一个可以复用的基座模型，训练方式是自监督学习，对大语言模型来说，最常见的做法就是不断预测下一个token。

## 3、大模型微调

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmfk1zCaUbtta2tcK4t7ydQ2tVfEy4yhRlncicKG1IgzGSl82aNuCMZ3FiclDeBILVkOFxbbqP04nXYQ1CLA3kOfSt5l9rnQWr3TA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

微调是在这个预训练生成的基座模型之上，用更小规模、更贴近任务的数据继续训练，让模型更适合某个具体场景，训练方式通常是监督微调或者指令微调。

## 4、大模型幻觉

幻觉就是大模型生成看似合理但实际是错误的回答，它会把虚假的信息当做事实来回答，所以我们不要认为大模型的回答就一定是正确的。

## 5、MCP协议

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmf7oV9AOneIjN828bTSIfstIIuanefO29hpu2EkSnhSwTQKRhoWe7gXYEWkIFGXVwFkNicBI7OKqibiaOnePia1MDuLqxVXW9mGTmE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

MCP（Model Context Protocol）是模型上下文协议，目的是为AI应用提供一个标准化接口，使其能够连接外部数据源和工具。例如，AI应用可以通过MCP连接到本地文件或数据库、搜索引擎或计算器、工作流或专业提示词等，从而获取到上下文信息并执行实际任务，可以把 MCP 理解为 AI 应用的"TypeC 接口"。

## 6、Token

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmd2CficF71dcREwiaVSEmqGb6ugaJIWfUicXkzC0zA8gH0Vv7qw16rZGld3ic8Y00udBVgbCCE9hxcoyYqEUkVgLnRHdLk4mFicHyEo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

Token中文翻译为词元，对于大模型来说，因为它只能处理数字，所以要找到一种方式把原始输入的文本转换为数字，这个就是分词器（tokenizer）所做的任务。分词器会按照分词算法把输入文本切分为多个token，然后用一个数字ID来表示token，后续大模型推理过程中都是使用这个数字ID来进行计算。

## 7、RAG-检索增强生成

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nkicicwORVWmcxgS5Qy0ib9s65oUpx501HbTolF3m2F9Y1hgpXudn3MUgLz4E2mUibDOHFSS9rZGHfanH2OTXMmLiaTCIxibd035opw9rtPTClqu4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

Retrieval-Augmented Generation：RAG全称检索增强生成，就是让大模型在回答问题前先去“查资料”（检索），相当于让它开卷考试：模型本身可能没学过公司的内部文档，但只要把相关内容找出来给它，它就能结合这些资料给出靠谱的答案（生成）。

## 8、记忆模块

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmdP4CqwENy96GVD1pwvuWykmDDqiaicl4pjxnQk2WH8E2Odng7cUR6lVEjiaHicBBwibFq0AVzya6fg15RmE23oGDs2NvgtguaEnSibM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

Agent的记忆通常拆成两层：第一层是短期记忆，用于当前会话，用截断对话或者总结摘要的方式去控制prompt长度，同时需要保持语义连贯。第二层是长期记忆，用于跨会话场景，用向量召回最相关的历史信息，再按需放回上下文。

## 9、Skill

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmf9mSiaunJNFy2MJyzyT6mC7QyTEWicaf6ujY1ZPriabW5CgXicftUq5krdg9oqobmcLNhoyJP9tHCxxnuFeoC8WJYUFvHicMW37xfA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

Skill本质是结构化的本地文件夹，用来补充某个领域的流程、知识和工具，让模型在相关场景下自动或按需调用，是面向大模型的能力封装，由主说明文件skill.md、规则/流程文档、模板/示例、脚本/工具文件、参考资料等内容组成。

## 10、ReAct

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nkicicwORVWmcwRhQ4G8hl9EGNMUQmeeiaHeCvc7VjUTII7EZOt7VJw0Km4gaibVx0Ribm0hk7xDXfzkwb87TfZ8P06czc1Hu8BCn621CFzPLLbU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

ReAct就是Reason（推理）和Act（行动），它在做任务的时候，会先判断当前的信息够不够完成任务，如果不够，就去调用工具、执行某个动作，等结果回来之后，再继续推理下一步该怎么做，直到把任务走完。

## 11、Agent的自我反思

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmfMLMEemqMDlbyXibtFERtWMXf2iaJhUXua2mSLaGfdca35SoMUE8FJGPEicRlkdVGrcHoB1yBia8EXrYRTdNV2cZwxlOEmk44KjKo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

Agent 的反思机制，本质上是“生成后再评估，然后根据反馈修正结果”。常见有两类：自我反馈和外部反馈，自我反馈靠大模型自己审查输出，适合查文案一致性、约束遵循、有没有误改内容；外部反馈是把结果放进真实工具里验证，适合代码、计算、JSON、图表这类必须拿事实说话的任务。

## 12、Harness工程

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmcU6KicgRibaP5vlGZrOhqEXa4R4FgMXJAcVPL7r3vKicEic6v3cPHpUpw8eQN2SvDRicjxpm4kpTWVlvdufoChgMNs95bHY4pLN5Dg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10)

Harness Engineering，中文是翻译为驾驭工程，是给 AI Agent 设计工作环境的一套工程方法，包括上下文管理、工具调用、沙箱环境、权限控制、测试验证、日志观测、评审机制和反馈回路，目的是为了让Agent在真实工程系统中更可靠、更可控，并持续完成任务。

## 13、SDD-规格驱动开发

![图片](https://mmbiz.qpic.cn/mmbiz_png/nkicicwORVWmc5HDTyyOk622KLzXbv8kElhvBnFTJcW1vGtiaGzhK0iceCNA9Xn5cS1lmJBMVgBT1qK8sb98nY0OAcyIsU7V3ib3rib34bJnrnrqI/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

Spec-Driven Development，中文叫规格驱动开发，是在正式编码之前，先把需求变更的目标、范围、系统行为、设计约束和任务拆分通过文档（规格文档）确定下来，再让AI按照这些文档去开发，能够把模糊需求变成稳定的工程上下文，从而减少AI自己猜需求、误改历史逻辑和实现跑偏的问题。

\-----------------------------------------------------

我是 AgentGuide，大厂在职资深开发，后端转 AI Agent 开发。

持续分享 Agent / 大模型应用的优质面试题和答案解析。

如果你也在准备 AI 应用开发、大模型工程相关面试，可以继续关注后续系列。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nkicicwORVWmfbgxKicx2OhdCfX5AKthslXJqCCvicqT3C2tSlEQ2vOcic9LVnFbX5ic1Hb7fdBBtiab9wLE8hesJBYHD0S3ia65KdDxIFC6SribywXk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12)

推荐阅读：

[字节面试官：别再直接让 AI写代码了，去学习一下 SDD 规格驱动开发](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483895&idx=1&sn=d631b4abf9525ec92f3a6ea650826bf2&scene=21#wechat_redirect)

[面试官问：什么是 Harness 工程？可以这样回答](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483882&idx=1&sn=63d1107a48a845f08b44a5ddd46dde9b&scene=21#wechat_redirect)

[面试官问：Agent 怎么评测？别再只答“看准确率”了](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483869&idx=1&sn=2fe630ea24217451d2a7f31632c2d5b7&scene=21#wechat_redirect)

[字节面试官：不用看复杂公式，能把大模型训练原理讲清楚吗？一文通俗易懂讲清大模型训练原理](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483862&idx=1&sn=3d63465be6113a053b616ae1bb2165c5&scene=21#wechat_redirect)

[字节面试官：大模型预训练和微调的区别是什么？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483849&idx=1&sn=627a983c6def76729e037eb4a63286d6&scene=21#wechat_redirect)

[字节面试官：你的Agent系统里面Skill是怎么编写的？如何保证高质量的Skill？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483841&idx=1&sn=097134b0d07f981ef96ac819226dff39&scene=21#wechat_redirect)

[字节面试官：Agent的记忆系统是什么？短期和长期记忆方案怎么设计？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483832&idx=1&sn=6297fb2233ffbb0e57d26c8a2ff2ed7f&scene=21#wechat_redirect)

[字节面试官：混合专家模式（MOA）是什么？为什么MOA能够提升效果？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483827&idx=1&sn=6f10d0c6c68ec290f952db03441973c0&scene=21#wechat_redirect)

[字节面试官：Token到底是什么？有哪些分词算法？一篇文章讲清！](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483817&idx=1&sn=b997c2e26eeea250b14b3ad2b742f238&scene=21#wechat_redirect)

[字节面试官：RAG系统怎么进行效果调优？一文讲清评价指标到优化方式！](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483798&idx=1&sn=a5feead53cbc8fbf95c0540b24f9074e&scene=21#wechat_redirect)

[字节面试官：如何评估RAG系统？你项目有哪些测评指标？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483791&idx=1&sn=e3b5b08e2ebfe04387f32b56a9ac07fd&scene=21#wechat_redirect)

[字节面试官：ReAct的工作原理是什么？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483782&idx=1&sn=ab3d2be8ddc01a2a212bff92464b51f6&scene=21#wechat_redirect)

[面试官：什么是Multi-Agent，有哪些工作模式？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483763&idx=1&sn=76a8a4a9896c83b54f93019467858790&scene=21#wechat_redirect)

[面试官：Skills是什么？讲一讲它的工作原理](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483738&idx=1&sn=6f840392543af5e298c77411f921cf7f&scene=21#wechat_redirect)

[面试官：什么是RAG？为什么大模型要先“查资料”，再回答问题？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483721&idx=1&sn=4c2dc4810ca3c97a8b0924cdea352810&scene=21#wechat_redirect)

[面试官：你项目里面的提示词工程是怎么做的？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483705&idx=1&sn=d296462bc728de1fcdf0aa00c47d3f2d&scene=21#wechat_redirect)

[字节面试官：你是怎么理解MCP协议的？](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483688&idx=1&sn=8a99ab6774f3ef448dc1544106e8039a&scene=21#wechat_redirect)

[面试官：Agent的本质是什么？一文讲透！](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483678&idx=1&sn=b049a102946533f53a9d5b0e3525b6a9&scene=21#wechat_redirect)

[大厂Agent开发工程师亲测：从入门到胜任高级岗，核心技术学习路线](https://mp.weixin.qq.com/s?__biz=MzkzMzQyNzI5MQ==&mid=2247483655&idx=1&sn=07b46a1298cdf804fe509aa333e7f82d&scene=21#wechat_redirect)

内容无AI创作、润色