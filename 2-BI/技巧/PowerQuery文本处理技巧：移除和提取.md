---
title: "PowerQuery文本处理技巧：移除和提取"
source: "https://zhuanlan.zhihu.com/p/64419762"
author:
  - "[[采悟​​]]"
published:
created: 2026-10-30
description: "每当拿到原始数据，不如意十有八九，快速准确的清洗数据也是必备技能，数据清洗正好是 PowerQuery 的强项，本文就来介绍两个常用的 M 函数：Text.Remove 和 Text.Select。 看到以 Text 开头的，就知道是文本处理函…"
tags:
  - "clippings"
---
[收录于 · Power BI星球](https://www.zhihu.com/column/powerbistar)

51 人赞同了该文章

每当拿到原始数据，不如意十有八九，快速准确的清洗数据也是必备技能，数据清洗正好是 [PowerQuery](https://zhida.zhihu.com/search?content_id=102444823&content_type=Article&match_order=1&q=PowerQuery&zhida_source=entity) 的强项，本文就来介绍两个常用的 M 函数： [Text.Remove](https://zhida.zhihu.com/search?content_id=102444823&content_type=Article&match_order=1&q=Text.Remove&zhida_source=entity) 和 [Text.Select](https://zhida.zhihu.com/search?content_id=102444823&content_type=Article&match_order=1&q=Text.Select&zhida_source=entity) 。

看到以 Text 开头的，就知道是文本处理函数，比如原始数据如下，



如果只想要中文名，就是把英文字母都去掉，可以用Text.Remove函数，添加自定义列，

> 姓名=Text.Remove(\[客户\],{"A".."Z"})



**Text.Remove 的参数有两个，第一个就是文本，第二个就是要移除的字符，可以是文本或者是文本的列表，{"A".."Z"}就是生成了一个从A到Z的列表，只要是大写字母，就从客户的信息中移除。**

如果有小写字母，需要把所有的字母都移除了，把大写的"Z"替换成小写的"z"就行了，

> 姓名=Text.Remove(\[客户\],{"A".."z"})

如果只想要英文名，要去掉中文名，可以这样写，

> 英文名=Text.Remove(\[客户\],{"一".."龟"})



**Powerquery 的中文字符以 Unicode 连续储存，"一"的 Unicode最小，正常使用的汉字中，"龟"的 Unicode 最大，因此{"一".."龟"}就包含了所有正常使用的汉字列表，正好利用这个特性，去除了所有的中文字符。**

如果有更多种类的文本数据不规则的堆放在一起，比如这样，



想把联系方式提取出来，第二个参数还可以这样写，

> 联系方式=Text.Remove(\[客户\],{"A".."z","一".."龟"})

把中文字符和英文字符的列表都放到第二个参数中，全部移除。



不过如果字符种类很多，像这样更加杂乱的，



要提取联系方式，用Text.Remove 就有点麻烦，各种奇怪的符号种类太多了，编码也不一定连续。还好有一个 Text.Select 函数专门用来提取的。

**Text.Select 函数和 Text.Remove 正好相反，Text.Select 只提取第二个参数中的字符，** 上图中提取联系方式，直接这样写，

> 联系方式=Text.Select(\[客户\],{"0".."9"})



直接就可以得到联系方式信息。

提取各种字符的列表如下，



这两个函数的都很简单，需要提取或者移除字符的情况直接套用就可以了。

*公众号:[PowerBI星球](https://zhida.zhihu.com/search?content_id=102444823&content_type=Article&match_order=1&q=PowerBI%E6%98%9F%E7%90%83&zhida_source=entity)*

发布于 2019-05-01 18:35[12项 Harness权益全包，超量尊享 8.8折](https://click.aliyun.com/m/20000000945/?cb=https%3A%2F%2Fsugar.zhihu.com%2Fplutus_adreaper_callback%3Fsi%3D721c4f13-e5e9-4852-a1b2-ae74e66131b8%26os%3D3%26zid%3D1629%26zaid%3D3803639%26zcid%3D3853334%26cid%3D3853334%26event%3D__EVENTTYPE__%26value%3D__EVENTVALUE__%26score%3D__EVENTSCORE__%26ts%3D__TIMESTAMP__%26cts%3D__TS__%26mh%3D58a672e29c479bca267e61bec1d98fa9%26adv%3D645640%26ocg%3D0%26cp%3D0%26ocs%3D0%26aic%3D0%26atp%3D0%26ct%3D0%26ed%3DGiBNJgVzfCMmUW9XFyEvRA8xBGxJICwkOhh0FlwxKw1YY0gnWzUoISkYdBZcPC1XVmNIJ1QwZ3BoUCcOVW19BVJ1CXgPcGp5fhJiVAZial8FIFAuBXFvcXsWZFAIZGpcHngLfwl2aXZ5HGZBQyUlDVImDHgIejlwYxdkUQh9eFVdfRRyCyJqbX1DM1EEaCgACnUMLB4iNidzAGUlFGJ-RAo3Xi9MHDk2PHo3H0F1fgJOdnhvCnFqZXwXd1B1Q3Ixdm4J1Jo%3D&spu=biz%3D0%26ci%3D3853334%26si%3D9c5209c0-2669-4e68-83a0-3fa658d0a05f%26ts%3D1793341622%26zid%3D1629)

[

多模态覆盖 18+旗舰模型、Harness 权益每月赠送、多 Agent 适配 生产力全面扩容

](https://click.aliyun.com/m/20000000945/?cb=https%3A%2F%2Fsugar.zhihu.com%2Fplutus_adreaper_callback%3Fsi%3D721c4f13-e5e9-4852-a1b2-ae74e66131b8%26os%3D3%26zid%3D1629%26zaid%3D3803639%26zcid%3D3853334%26cid%3D3853334%26event%3D__EVENTTYPE__%26value%3D__EVENTVALUE__%26score%3D__EVENTSCORE__%26ts%3D__TIMESTAMP__%26cts%3D__TS__%26mh%3D58a672e29c479bca267e61bec1d98fa9%26adv%3D645640%26ocg%3D0%26cp%3D0%26ocs%3D0%26aic%3D0%26atp%3D0%26ct%3D0%26ed%3DGiBNJgVzfCMmUW9XFyEvRA8xBGxJICwkOhh0FlwxKw1YY0gnWzUoISkYdBZcPC1XVmNIJ1QwZ3BoUCcOVW19BVJ1CXgPcGp5fhJiVAZial8FIFAuBXFvcXsWZFAIZGpcHngLfwl2aXZ5HGZBQyUlDVImDHgIejlwYxdkUQh9eFVdfRRyCyJqbX1DM1EEaCgACnUMLB4iNidzAGUlFGJ-RAo3Xi9MHDk2PHo3H0F1fgJOdnhvCnFqZXwXd1B1Q3Ixdm4J1Jo%3D&spu=biz%3D0%26ci%3D3853334%26si%3D9c5209c0-2669-4e68-83a0-3fa658d0a05f%26ts%3D1793341622%26zid%3D1629)

赞同 51