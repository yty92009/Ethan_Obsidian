---
title: "Power Pivot&Power BI不连续日期的日环比"
source: "https://zhuanlan.zhihu.com/p/72893435"
author:
  - "[[焦棚子]]"
published:
created: 2026-10-30
description: "焦棚子的文章目录 请点击下载附件一、背景这两天有朋友在交流，dax中使用时间智能函数写日环比，一个 dateadd 就可以了。但是有些业务不是每天都连续发生的，比如股票，周末就没数据，要环比上一个日期就不太好使…"
tags:
  - "clippings"
---
[收录于 · power系列](https://www.zhihu.com/column/c_1214128947489050624)

26 人赞同了该文章

[焦棚子的文章目录](https://link.zhihu.com/?target=https%3A//jiaopengzi.com/75.html)

**[请点击下载附件](https://link.zhihu.com/?target=https%3A//jiaopengzi.com/377.html)**

## 一、背景

> 原文此处原配 2 张图床图片，已按图片策略转为文字（重要图片另行本地化备份）。


这两天有朋友在交流，dax中使用 [时间智能函数](https://zhida.zhihu.com/search?content_id=104327551&content_type=Article&match_order=1&q=%E6%97%B6%E9%97%B4%E6%99%BA%E8%83%BD%E5%87%BD%E6%95%B0&zhida_source=entity) 写日环比，一个 *dateadd* 就可以了。但是有些业务不是每天都连续发生的，比如股票，周末就没数据，要环比上一个日期就不太好使了。诸如此类业务不连续的业务如何写日环比呢？

## 二、数据源



**需求:**

计算: test表中每天value与上一日期的变化百分比；

说明: 由于日期是非连续, 有空值；

例如: 2019/6/10需要取2019/6/6号的值做除法运算。

感谢Q友 AlbertYc 提供素材。

## 三、DAX

1、基础度量total

```
total = SUM(Test[Value])
```

2、过程度量previous\_date，不连续日期的前一天，n可以控制前n天，实际操作不用写，案例演示需求写一下。

```
previous_date = 
//计算不连续日期的前n天date
var n=1
var date1=max('Test'[Date])
var date2=filter(all('Test'[Date]),'Test'[Date]<date1)
var date3=topn(n,date2,'Test'[Date],DESC)
return
date3
```

3、过程度量previous\_date（同上2）

```
previous_total = 
//计算不连续日期的前n天的值
var n=1
var date1=max('Test'[Date])
var date2=filter(all('Test'[Date]),'Test'[Date]<date1)
var date3=topn(n,date2,'Test'[Date],DESC)
var pt=calculate('calendar'[total],'calendar'[Date]=date3)
return
pt
```

4、最终需求日环比度量previous\_dod

```
previous_dod = 
//计算不连续日期的前n天占比
var n=1
var date1=max('Test'[Date])
var date2=filter(all('Test'[Date]),'Test'[Date]<date1)
var date3=topn(n,date2,'Test'[Date],DESC)
var pt=calculate('calendar'[total],'calendar'[Date]=date3)
return
if(pt=BLANK(),BLANK(),divide('calendar'[total],pt)-1)
```

5、结果图



## 四、总结

1、世上本无时间智能函数，大家用多了特定需求才有了时间智能函数（笔者自娱，该用还得用）；

2、万变不离其宗的业务需求转换为DAX上下文，有什么需求就构建什么上下文；

3、本案例中主要利用 *TOPN* ，虽然日期不连续，但是可排序。

by焦棚子

[焦棚子的文章目录](https://link.zhihu.com/?target=https%3A//jiaopengzi.com/377.html)

1 人已送礼物

编辑于 2020-03-03 13:41[12项 Harness权益全包，超量尊享 8.8折](https://click.aliyun.com/m/20000000945/?cb=https%3A%2F%2Fsugar.zhihu.com%2Fplutus_adreaper_callback%3Fsi%3D04fc8cb8-4326-405a-89df-556bc3578592%26os%3D3%26zid%3D1629%26zaid%3D3803639%26zcid%3D3853334%26cid%3D3853334%26event%3D__EVENTTYPE__%26value%3D__EVENTVALUE__%26score%3D__EVENTSCORE__%26ts%3D__TIMESTAMP__%26cts%3D__TS__%26mh%3D58a672e29c479bca267e61bec1d98fa9%26adv%3D645640%26ocg%3D0%26cp%3D0%26ocs%3D0%26aic%3D0%26atp%3D0%26ct%3D0%26ed%3DGiBNJgVzfCMmUW9XFyEvRA8xBGxJICwkOhh0FlwxKw1YY0gnWzUoISkYdBZcPC1XVmNIJ1QwZ3BoUCcOVW19BVJ1CXgPcGp5fhJiVAZial8FIFAuBXFvcXsWZFAIZGpcHngLfwl2aXZ5HGZBQyUlDVJ1D31ZdmpwY0NrUQR9eABbdhQrC3VvbS1HNFUIZHUAX3VafB4iNidzAGUlFGJ-RAo3Xi9MHDk2PHo3H0F1fgJOdnhvCnFqZXwXd1B1__GmjLVOJ34%3D&spu=biz%3D0%26ci%3D3853334%26si%3D9067a500-f965-4003-a365-cbf2949040c6%26ts%3D1793341093%26zid%3D1629)

[

多模态覆盖 18+旗舰模型、Harness 权益每月赠送、多 Agent 适配 生产力全面扩容

](https://click.aliyun.com/m/20000000945/?cb=https%3A%2F%2Fsugar.zhihu.com%2Fplutus_adreaper_callback%3Fsi%3D04fc8cb8-4326-405a-89df-556bc3578592%26os%3D3%26zid%3D1629%26zaid%3D3803639%26zcid%3D3853334%26cid%3D3853334%26event%3D__EVENTTYPE__%26value%3D__EVENTVALUE__%26score%3D__EVENTSCORE__%26ts%3D__TIMESTAMP__%26cts%3D__TS__%26mh%3D58a672e29c479bca267e61bec1d98fa9%26adv%3D645640%26ocg%3D0%26cp%3D0%26ocs%3D0%26aic%3D0%26atp%3D0%26ct%3D0%26ed%3DGiBNJgVzfCMmUW9XFyEvRA8xBGxJICwkOhh0FlwxKw1YY0gnWzUoISkYdBZcPC1XVmNIJ1QwZ3BoUCcOVW19BVJ1CXgPcGp5fhJiVAZial8FIFAuBXFvcXsWZFAIZGpcHngLfwl2aXZ5HGZBQyUlDVJ1D31ZdmpwY0NrUQR9eABbdhQrC3VvbS1HNFUIZHUAX3VafB4iNidzAGUlFGJ-RAo3Xi9MHDk2PHo3H0F1fgJOdnhvCnFqZXwXd1B1__GmjLVOJ34%3D&spu=biz%3D0%26ci%3D3853334%26si%3D9067a500-f965-4003-a365-cbf2949040c6%26ts%3D1793341093%26zid%3D1629)

赞同 26