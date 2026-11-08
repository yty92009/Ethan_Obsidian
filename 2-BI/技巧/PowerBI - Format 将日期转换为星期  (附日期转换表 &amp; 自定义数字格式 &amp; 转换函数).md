---
title: "PowerBI - [Format] 将日期转换为星期  (附日期转换表 &amp; 自定义数字格式 &amp; 转换函数)"
source: "https://www.cnblogs.com/xiaopc/p/14155434.html"
author:
  - "[[未必是小小]]"
published: 2020-12-18
created: 2026-10-30
description: "日期格式转换表： 自定义格式转换： =FORMAT(SUM(Table[Field]),\"0.00%\") 基础函数之转换函数： 实践 #1： 表：表有字段From_Date，Week_Code (1-7) 需求：添加切片器WEEKDAY显示值Monday，Sunday，Monda"
tags:
  - "clippings"
---
日期格式转换表：

---

自定义格式转换：

\=FORMAT(SUM(Table\[Field\]),"0.00%")



---

基础函数之转换函数：  


---

实践 #1：

表：表有字段From\_Date，Week\_Code (1-7)

需求：添加切片器WEEKDAY显示值Monday，Sunday，Monday，Tuesday，Wednesday，Thursday，Friday，Saturday。  
　　选择Monday时，显示每月最后一个礼拜一的数据。

实现方式一：

1，SQL只提取每月最后一周的数据  
2，添加计算列 weekday1，表达式如下：

```
Weekday1 = IF('Bonus'[WEEK_CODE]="7","Sunday",
IF('Bonus'[WEEK_CODE]="6","Saturday",
IF('Bonus'[WEEK_CODE]="5","Friday",
IF('Bonus'[WEEK_CODE]="4","Thursday",
IF('Bonus'[WEEK_CODE]="3","Wednesday",
IF('Bonus'[WEEK_CODE]="2","Tuesday",
IF('Bonus'[WEEK_CODE]="1","Monday",
"Blank"
)))))))
```

　3， 将weekday1 设置为切片器后，排序乱了

　　解决：选择字段，点击按列排序，选择Week\_Code，保存后切片器按1-7排序

---

实现方式二：

添加计算列weekday2，表达式如下：

```
weekday2 = Format('Bonus'[FROM_DATE],"DDDD")
```

　　效果与方式一一样。

　　但是这个表达式不适用于直连模式



---

实践 #2 - 历史周显示每周最后一天的数据，本周显示所有天的数据  
需求： 添加WeekFilter，过去周显示每周最后一天的数据，本周显示所有天的数据  
  
实现步骤：  
Step1 - 写SQL在D\_Date表里添加Week\_code

```
CASE
 WHEN DAY_OF_WEEK = 'Sunday' THEN 1
 WHEN DAY_OF_WEEK = 'Monday' THEN 2
 WHEN DAY_OF_WEEK = 'Tuesday' THEN 3
 WHEN DAY_OF_WEEK = 'Wednesday' THEN 4
 WHEN DAY_OF_WEEK = 'Thursday' THEN 5
 WHEN DAY_OF_WEEK = 'Friday' THEN 6
 WHEN DAY_OF_WEEK = 'Saturday' THEN 7 --Saturday 为每周最后一天
END AS WEEK_CODE
```

Step2 - 在D\_Date表添加计算列，将本周的weekcode置为 7

```
Week_Filter =
Var dateweek = YEAR('D_DATE'[DAY_DATE])*100 + WEEKNUM('D_DATE'[DAY_DATE])
Var thisweek= YEAR(NOW()) *100 + WEEKNUM(NOW())
RETURN
IF(dateweek = thisweek,7,'D_DATE'[WEEK_CODE])
```

Step3 - 在视图页面添加Filter ，Week\_code = 7  
实现结果：  


感谢所有指点小萌新的大神们。。。