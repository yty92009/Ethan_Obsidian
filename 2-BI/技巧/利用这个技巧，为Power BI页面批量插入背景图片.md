---
title: "利用这个技巧，为Power BI页面批量插入背景图片"
source: "https://zhuanlan.zhihu.com/p/370198745"
author:
  - "[[采悟​​]]"
published:
created: 2026-10-30
description: "我的新书也已上市，《PowerBI商业数据分析》帮你从0到1轻松上手Powre BI, 有需要的朋友可以下单购买：分享一个PowerBI页面设计小技巧。 PowerBI的页面背景可以插入图片，不过只能一页一页的添加，如果报表的页面很…"
tags:
  - "clippings"
---
[收录于 · Power BI星球](https://www.zhihu.com/column/powerbistar)

10 人赞同了该文章

[我的新书也已上市](https://zhuanlan.zhihu.com/p/357981152) ，《 [PowerBI商业数据分析](https://zhida.zhihu.com/search?content_id=170396034&content_type=Article&match_order=1&q=PowerBI%E5%95%86%E4%B8%9A%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&zhida_source=entity) 》帮你从0到1轻松上手Powre BI, 有需要的朋友可以下单购买：

---

分享一个PowerBI页面设计小技巧。

PowerBI的页面背景可以插入图片，不过只能一页一页的添加，如果报表的页面很多，这样添加起来也会比较麻烦，能不能一次性为所有的页面批量添加背景图片呢？

通过页面设置无法做到批量添加，不过利用PowerBI的主题设置，通过修改主题代码的方式可以实现。

关于主题的设置以前也介绍过，比如：

[如何在Power BI中随心所欲的搭配色彩？](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzA4MzQwMjY4MA%3D%3D%26mid%3D2484068978%26idx%3D1%26sn%3D33c435da5b89e10b7ba3a2a908746aec%26chksm%3D8e0c48a5b97bc1b3d5be5769b95d148813985a7c13ab3f3f5b294abc4e8a5829dec2719deb90%26scene%3D21%23wechat_redirect)

[Power BI切片器搜索框背景色缺陷的解决方案](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzA4MzQwMjY4MA%3D%3D%26mid%3D2484071291%26idx%3D1%26sn%3Db65803396a44d2ea664b7e83adf96d58%26chksm%3D8e0c41acb97bc8bae4bfa653771ff75bed793476befc641415ea0e173340552bca43a7bab83e%26scene%3D21%23wechat_redirect)

几乎所有的格式设置都可以通过主题来调整，这里我们不涉及其他的主题代码，只看关于背景设置的代码，不过首先需要将图片转化为Base64代码。

Base64是一种基于64个可打印字符来表示二进制数据的方法，各种文件均可以转换为base64代码来表示，关于如何将图片转为base64代码，有很多在线转换工具可以使用，大家可以自行百度搜索，比如： [fly63.com/tool/base64/](https://link.zhihu.com/?target=http%3A//www.fly63.com/tool/base64/)

![](https://pic3.zhimg.com/v2-315c94c34eb270744fd7b269b7209a0a_1440w.jpg)

假如我们想以这个图片作为页面背景：

![](https://pic3.zhimg.com/v2-f6b7af2553ddeea34ea9d2650ce70d5a_1440w.jpg)

可以先将这个图片利用在线转换工具转换为base64代码，然后将base64粘贴到下面主题中的相应位置：

{"name":" [PowerBI星球](https://zhida.zhihu.com/search?content_id=170396034&content_type=Article&match_order=1&q=PowerBI%E6%98%9F%E7%90%83&zhida_source=entity) "

,"visualStyles": {

"page": {

"\*": {

"background": \[

{

"image": {

"name": "image",

"scaling": "Fit",

"url": " **粘贴图片的base64代码** "

},

"transparency": 0

}

\]

}

}

}

}

主题的代码可以先在txt文本中编辑，保存后，再将后缀改为json即可生成一个主题。

将这个主题导入到PowerBI中，效果是这样的：

![动图封面](https://picx.zhimg.com/v2-adf81aed2ad8cd29ebd1b43076b1149b_b.jpg)

这样就可以一键更改所有页面的背景，并且，新建页面，自动也是这个图片的背景，是不是相当于PPT的母版呢？

当然，利用主题代码来设计依然太笨重，期待PowerBI能够真的像PPT一样，更方便无代码的更改报表的主题。

## 更多推荐：

喜欢别忘了点赞哦~

```
掌握一个技能
专研一个领域
成为更好的自己
```

发布于 2021-05-06 19:58[Power BI](https://www.zhihu.com/topic/20049875)[Power BI 商业数据分析（书籍）](https://www.zhihu.com/topic/21687810)

![HR赫莲娜京东自营旗舰店](https://pgdt.ugdtimg.com/141/20204/snscosdownload/SZ/reserved/6a8fff7000003fe40cc99ed88e6cbc1e0000008d00004eec?ck=12cd0c30a593779f0610ab9cfc41bb73&m=12cd0c30a593779f0610ab9cfc41bb73&sha256=6fa05b9e9487084a24cd446b2a45464bf52b1b856b159582bca459eab2fc3c8c&imageView2/format/webp=)

HR赫莲娜京东自营旗舰店

赫莲娜全新黑绷带小露珠套组，紧提外轮廓 鲜活透光好状态

赞同 10