---
title: "数据可视化之PowerQuery篇（四）二维表转一维表，看这篇文章就够了"
source: "https://www.shuzhiduo.com/A/QV5Zo4D7dy/"
author:
published:
created: 2026-10-30
description:
tags:
  - "clippings"
---
[https://zhuanlan.zhihu.com/p/69187094](https://zhuanlan.zhihu.com/p/69187094)

数据分析的源数据应该是规范的，而规范的其中一个标准就是数据源应该是一维表，它会让之后的数据分析工作变得简单高效。

在之前的文章中，我也经常强调一维表的易用性，也时常有人问我，什么是一维表，为什么要转为一维表呢，这篇文章就来帮你梳理清楚并告诉你如何将二维表转化为一维表。

## 什么是一维表

在Excel中常见的是二维表，你可能天天都在用，

![](https://pic1.zhimg.com/80/v2-b1242c72aec20697b073f5562c0430cc_720w.jpg)

而一维表是长这样的：

![](https://pic1.zhimg.com/80/v2-0d25f0df878a3753a30bfb528b654360_720w.jpg)

通过以上二维表和一维表的比较，你应该能分清楚什么是一维表、什么是二维表了，简单来说：

- 一维表的每一列就是一个维度，列名就是该列值的共同属性
- 一维表的每一行就是一条独立的记录

而这两点对于二维表，都不适合。

## 为什么要转为一维表

二维表更符合我们日常的阅读习惯，信息更浓缩，适合展示分析结果，但作为源数据进行数据分析时，就需要一维表。

一维表的每一列是一个独立的维度，列名或者字段名就是数据分析的基础，比如利用列名与其他表建立关系；编写DAX时直接使用列名；数据可视化时直接把字段拖入到某个属性框中等。

那么如何将二维表和一维表相互转换呢？

一维表变成二维表很简单，在Excel中都可以轻松做到，就是利用数据透视表，在PowerQuery中也有同样的透视功能，这里不再细说，下面主要介绍一下如何将二维表转换成一维表。

## 二维表转为一维表的方法

利用PowerQuery，二维表转为一维表十分方便，以Excel中常见的几种结构的表格为例，看看都是如何操作的。

## 第一种情形

简单的二维表，如本文的第一张图表，直接使用逆透视功能，就可以快速转为一维表，

![](https://pic2.zhimg.com/v2-929441ba16487b4b69cc52886686fe31_b.jpg)

可以选择需要透视的列进行“逆透视”，也可以选择不需要透视的列，然后点击“逆透视其他列”来完成。

提示：这些操作，生成的最终一维表的列名，需要自己手动更改一下，下同。

## 第二种情形

行标题带有层级结构的二维表，如下，

![](https://pic1.zhimg.com/80/v2-d680feee72cbf7cf0cf6452e4812ca04_720w.jpg)

这种结构很清晰，但做数据分析最让人头疼的就是合并单元格，不过在PowerQuery中处理也并不困难，只是多了一些步骤。

将上表导入到PowerQuery编辑器后，先把年度列向下填充，将年度数据补齐，然后再进行逆透视，

![](https://pic4.zhimg.com/v2-13d98b04bbe4b4b4c0bf3852f9b43c2f_b.jpg)

## 第三种情形

列标题带有层级结构的二维表，如下，

![](https://pic1.zhimg.com/80/v2-af26642e16b74b0de60598bb5fef1b70_720w.jpg)

这种表格可以先转置，转置以后，就是第二种情形，然后再进行逆透视就可以了，

![](https://pic1.zhimg.com/v2-1488a00545595e6b4c5da6840a50aa7c_b.jpg)

## 第四种情形

行标题和列标题均带有层次结构，如下图，

![](https://pic4.zhimg.com/80/v2-dfbfc8f4e3349785a55c3124d8a1db53_720w.jpg)

看起来更复杂是不是，其实同样是上述几个步骤灵活组合，

a. 将年度列向下填充，补齐数据

![](https://pic4.zhimg.com/80/v2-dae0cf692e38280fb9423de8a02aa94b_720w.jpg)

b. 将年度列和季度列合并，生成年度季度列，这种结构就变成第三种情形，

![](https://pic1.zhimg.com/80/v2-75c06d7cb9f4848ef75b087a92eb706c_720w.jpg)

c. 转置表、把第一列向下填充，并提升标题，就变成了很简单的结构，也就是第二种情形，

![](https://pic2.zhimg.com/80/v2-667184efda135ef05dbafab7a9d7be99_720w.jpg)

d. 选中前两列，逆透视其他列，就变成了一维表

![](https://pic4.zhimg.com/80/v2-cede99a992b9fa68efceb0cf68be127b_720w.jpg)

e. 为了和源数据维度一致，将年度季度列进行分列

![](https://pic2.zhimg.com/80/v2-8c218405455c046aa2f6a8618539c7c1_720w.jpg)

至此就得到了最终的一维表，看起来步骤很多，其实熟练掌握了也就分分钟的事。

## 总结

以上几种情形，基本包含了各种复杂结构的表格，如果有更复杂的表格，比如更多层级的行、列名，也同样可以按照以上的套路通过来分步完成：

1，将行层级先合并，转换成第三种情形

2，转置，变成第二种情形

3，逆透视

步骤中间熟练掌握填充、提升标题、分列等操作，关于转成一维表的问题，就没有什么表格能难倒你的了。

关于一维表的用处，不仅在PowerBI中，使用其他工具做数据分析时，同样需要这样的规范数据源。

下次再遇到二维表转一维表的问题，直接使用PowerQuery就行了。

## 数据可视化之PowerQuery篇（四）二维表转一维表，看这篇文章就够了的更多相关文章

1. [MVC5中使用jQuery Post 二维数组和一维数组到Action](https://www.shuzhiduo.com/A/E35pbpK8zv/)
	很久没有写了,最近在做一个MVC项目,这是我做的第一个MVC项目.之前可以说多MVC一点都不了解,今天把昨天遇到的一个问题记录下来.MVC大神就请飘过吧,跟我遇到同样问题的可以进来看看.遇到的第一个问...
2. [\[PHP\]快速实现：将二维数组转为一维数组](https://www.shuzhiduo.com/A/ZOJPVgV2dv/)
	如何将下面的二维数组转为一维数组. $msg = array( array( 'id'=>'45', 'name'=>'jack' ), array( 'id'=>'34', 'na...
3. [php - 二维数组转一维数组总结](https://www.shuzhiduo.com/A/WpdKWkKMdV/)
	二维数组转一维数组总结 例如将如下二位数组转以为以为一维数组 $records = \[ \[ 'id' => 2135, 'first\_name' => 'John', 'last\_name...
4. [numpy基础教程--将二维数组转换为一维数组](https://www.shuzhiduo.com/A/n2d9NwYVzD/)
	1.导入相应的包,本系列教程所有的np指的都是numpy这个包 1 # coding = utf-8 2 import numpy as np 3 import random 2.将二维数组转换为一维...
5. [个人永久性免费-Excel催化剂功能第16波-N多使用场景的多维表转一维表](https://www.shuzhiduo.com/A/MyJx2LZXdn/)
	Excel表的多维表数据结构转换为一维表的数据结构,以供更进一步对数据进行加工整理,生成另外格式的汇总表,这是Excel数据处理的一大刚需,几乎每个Excel表哥.表姐都会遇到这样的使用场景.很可惜,...
6. [数据可视化之PowerQuery篇（十四）产品关联度分析](https://www.shuzhiduo.com/A/E35pWo2YJv/)
	https://zhuanlan.zhihu.com/p/64510355 逛超市的时候,面对货架上琳琅满目的商品,你会觉得这些商品的摆放,或者不同品类的货架分布是随机排列的吗,当然不是. 应该都听说...
7. [数据可视化之PowerQuery篇（十八）Power BI数据分析应用：结构百分比分析法](https://www.shuzhiduo.com/A/kvJ3qrjXdg/)
	https://zhuanlan.zhihu.com/p/113113765 本文为星球嘉宾"海艳"的PowerBI数据分析工作实践系列分享之二,她深入浅出的介绍了PowerBI...
8. [数据可视化之powerBI技巧（二十四）Power BI初学者刚见的错误，帮你轻松处理](https://www.shuzhiduo.com/A/B0zqrBnnJv/)
	在学习PowerBI的过程中,尤其是刚接触的时候,不可避免的会遇到各种各样的错误,有时自己怎么检查都没法消除,不解决这个错误又没法进行下一步的工作,经常会搞的自己烦闷无比,不过最后通过自己的苦苦摸索....
9. [数据可视化之PowerQuery篇（十五）如何使用Power BI计算新客户数量？](https://www.shuzhiduo.com/A/kPzOnRyadx/)
	https://zhuanlan.zhihu.com/p/65119988 每个企业的经营活动都是围绕着客户而开展的,在服务好老客户的同时,不断开拓新客户是每个企业的经营目标之一. 开拓新客户必然要付...

## 随机推荐

1. [Java——八种基本数据类型（常用类）](https://www.shuzhiduo.com/A/o75NBwyD5W/)
	装箱和拆箱 装箱:基本数据类型转为包装类 拆箱:包装类转为基本数据类型 jdk1.5(即jdk5.0)之后的版本都提供了自动装箱和自动拆箱功能 基本数据类型的包装类 举两个例子,看一下 public...
2. [TensorFlow从0到1之TensorFlow Keras及其用法（25）](https://www.shuzhiduo.com/A/Vx5MKAWYzN/)
	Keras 是与 TensorFlow 一起使用的更高级别的作为后端的 API.添加层就像添加一行代码一样简单.在模型架构之后,使用一行代码,你可以编译和拟合模型.之后,它可以用于预测.变量声明.占位...
3. [BUAA\_OO\_2020\_Unit4\_总结博客](https://www.shuzhiduo.com/A/Ae5RaZNrJQ/)
	BUAA\_OO\_2020\_Unit4\_总结 2020年春季学期第十六周,OO第四单元即最终章落下帷幕,本单元是利用Java进行UML类图的解析,完成对类图.顺序图.状态图的内部查询操作与简单的规则判断...
4. [jmeter对数据库进行简单的压测](https://www.shuzhiduo.com/A/x9J2YKrEz6/)
	1.点击测试计划,再点击“浏览”,把JDBC驱动添加进来: 注:JDBC驱动一般的位置在java的安装地址下,路径类似于: \\java\\jre\\lib\\ext 文件为:mysql-connect...
5. [cc31a\_demo--CppPrimer\_静态成员与继承-在派生类中访问基类中的static成员的方法](https://www.shuzhiduo.com/A/WpdKW1oXdV/)
	//\*基类中的static成员,在整个继承层次中只有一个实例 //\*在派生类中访问基类中的static成员的方法 //1.基类名::成员名 //2.子类名::成员名 //3.对象.成员名 //4.指针...
6. [Jmeter工具环境搭建](https://www.shuzhiduo.com/A/nAJvyMNazr/)
	Jmeter工具什么 1 多线程框架-支持多并发操作 2 用于对服务器模拟负载 3 支持web,数据库,FTP服务器系统的性能测试 4 开源,可二次定制开发 下载Java JDK 下载地址: http...
7. [java 加密与解密艺术](https://www.shuzhiduo.com/A/qVdeEKkndP/)
	视频来自黑马程序员公开课 对称加密之后的密文可能存在乱码,这些乱码无法识别,信息经过加密后会变成一串毫无规律的二进制串,此时再选择一种编码方式来展示,通常是 BASE64 格式的编码. 为了解决这个问...
8. [Idea配置JRebel插件的详细配置及图解](https://www.shuzhiduo.com/A/xl56wN3odr/)
	Idea最新JRebel插件的详细配置及图解 地址:https://blog.csdn.net/nyotengu/article/details/80629631#commentBox Ⅰ安装jreb...
9. [tap4fun（成都尼必鲁）--2020春招实习](https://www.shuzhiduo.com/A/Ae5RaG28JQ/)
	笔试 可能是我做过最简单的笔试了,只有选择填空,而且难度都不是很大,没啥印象了,考点和其他公司的笔试都差不多. 一面(技术面) 具体的不太记得了,因为这是我很后面面的了,所以问题基本都是那几个问题,都...
10. [bug和测试报告思维导图](https://www.shuzhiduo.com/A/RnJWyXLRdq/)
	Bug定义: 1.不符合需求的 2.程序本身的报错 3.不符合用户使用习惯的 Bug生命周期: 当我们测试人员提交一个bug的时候,自始bug就有它的生命周期,从开始到结束, 把测试的过程和结果写成文...