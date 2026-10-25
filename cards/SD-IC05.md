# SD-IC05 · 让关系残留成为建筑消失后的可见结构
案例：[ invisible-cities-opus-5.5 ](../cases/invisible-cities-opus-5.5.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

表达记忆或关系可以保留原物之间的连接，删去物本身，使空白区域也有明确设计含义。

## 实现与参数

节点按live/ghost分区；候选距离ghost≤4.2、live≤3.4，排序距离加0–1.5扰动，每点最多取7/3邻居并去重。绳10段、抛物线下垂d*.025；白#f4efe6、黑#18181c、灰#8d8a86和黑白交替编码类别。

## 审美细节

废弃区域连接更密、房屋更少；这是作者构造的关系视觉隐喻，随机近邻并不是真实社会网络。代码“head height”实际阈值为.75，仅微缩比例。

## 适用条件

- 有明确原物与关系语义
- 保留足够负空间
- 镜头可辨认细线端点

## 相邻方案与区别

与小雨云的行动留下新痕迹相对，本卡用消失对象的残留痕迹；跨仓可归入环境记忆，但操作不同应保留子卡。

## 失败模式

- 密线远景产生闪烁
- 随机近邻不支持真实关系推断
- 连接的种类若无图例会退化为装饰

## Movie 裁决

- **verdict**：reference
- **reason**：可借少量遗留连接表达一个旧空间的记忆。

## Frontend 裁决

- **verdict**：defer
- **reason**：没有真实关系语义时，不给日常前端加一片装饰连线。

## 最小对照

去掉说明文字，观察者仍能区分被使用与被遗弃两区；连线是否遮挡主物件、能否辨出端点；只有线团噪声则弃用。

## 源码证据

- [Repos/invisible-cities-opus-5.5/src/cities/ersilia.js:130–155](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/ersilia.js#L130-L155)：废弃区只留杆与节点，居住区保留房屋附近节点
- [Repos/invisible-cities-opus-5.5/src/cities/ersilia.js:157–197](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/ersilia.js#L157-L197)：白/黑/灰关系绳，邻接筛选、密度差和去重

## 项目效果图

![invisible-cities-opus-5.5 · live_site_still](../assets/previews/live-invisible-cities-atlas.png)

小型城市按类别列与序号行放在棋盘上；瓷金造型和标签共用空间位置，分类导航在下方。

来源：[原作者/出处](https://p.migdal.pl/invisible-cities-opus-5.5/) · live_site_still。本轮线上默认Atlas静帧，线上版本未绑定本地HEAD；不证明全部55城细节。

![invisible-cities-opus-5.5 · live_site_still](../assets/previews/live-invisible-cities-journey.png)

选择Journey后保留城市身份，发光线路把叙述顺序联结起来。

来源：[原作者/出处](https://p.migdal.pl/invisible-cities-opus-5.5/) · live_site_still。切换后的单帧，不据此认证完整过渡或输入中断。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
