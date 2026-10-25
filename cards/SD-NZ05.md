# SD-NZ05 · 以行业身份组织招牌配色和横竖版式
案例：[ neon-zenith ](../cases/neon-zenith.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

让街道广告成为世界叙事，而不是无内容的彩色矩形。

## 实现与参数

ADS回调依W/H的tall分支排版，短边s统一字号与线宽；maxW测量后压缩文字；一套虚构品牌生成横竖版本。

## 审美细节

招牌主体大字、次级英文、最小服务说明三层；可用黑红/深蓝金/白绿，不复制大面积紫渐变。

## 适用条件

- 有内容预算
- 字体/标识权利可用

## 相邻方案与区别

比随机霓虹汉字多一层世界含义；比单张图片更容易系统改语言与版式。

## 失败模式

- 原源码部分广告紫渐变不符合本站约束
- 未检查完整atlas装配和动态wipe实现
- 压字过度损害可读性

## Movie 裁决

- **verdict**：prototype
- **reason**：中近景有语义招牌可提供尺度和生活感。

## Frontend 裁决

- **verdict**：adapt
- **reason**：供手机品牌卡或场景标牌，但文字需可读而非只装饰。

## 最小对照

主镜头能读行业和一条信息；不同纵横比例不裁字；bloom后主字仍区分。

## 源码证据

- [Repos/neon-zenith/src/city/adscreens.js:22–35](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/adscreens.js#L22-L35)：文字测宽与竖排字符
- [Repos/neon-zenith/src/city/adscreens.js:47–80](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/adscreens.js#L47-L80)：义体黑红、饮料荧光绿、银行蓝金三类视觉身份
- [Repos/neon-zenith/src/city/adscreens.js:113–143](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/adscreens.js#L113-L143)：点心红金、制造业灰白红、药店白绿

## 项目效果图

![neon-zenith · observed_still](../assets/previews/neon-zenith-a855ac555caa.jpg)

已view_image docs/media/market.jpg：黑色楼峡、横竖霓虹、暖路灯与湿地纵向反光；历史静帧不证明动态。

来源：[原作者/出处](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/docs/media/market.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
