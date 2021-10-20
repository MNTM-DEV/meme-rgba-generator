# meme-rgba-generator
生成在黑白背景下可以展示2张不同的灰度图的程序

## 原理

原理详见公众号原文：[透明度藏图的原理与实现](http://mp.weixin.qq.com/s?__biz=MzUyNjE3ODEzMA==&mid=2247484459&idx=1&sn=fa04297f76c62e13ab31dddbcdbe6ec4&chksm=fa138616cd640f00bda386693513f113059de40353ce90e71ca8855422f32ed6fff684cf456c&mpshare=1&scene=23&srcid=1019k7REqPLM3XpAoyJ2EaBi&sharer_sharetime=1634655127041&sharer_shareid=93b6ec3e4c659827f8b490f8270786f5#rd)

Reduce函数设计不唯一，有想法的hxd如果设计出效果更好的算法，可以issue、PR到本repo，提交你的算法原理(可以有证明步骤)、代码实现、测试结果。

## 程序验证

首先是一张我们期望白底色显示的图片：

![图片](pic/src1.jpg)

然后是我们期望黑底色显示的图片：

![图片](pic/src2.png)


生成的透明灰度图白色背景的情况如下：

![图片](pic/dst.png)

对比黑白背景的视觉效果可以 [点击此处](compare.html)