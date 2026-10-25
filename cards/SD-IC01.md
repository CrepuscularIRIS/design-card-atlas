# SD-IC01 · 固定材质语汇，让城市差异发生在结构关系上
案例：[ invisible-cities-opus-5.5 ](../cases/invisible-cities-opus-5.5.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

多场景统一感可以来自有限的材质触感和色域，而每个场景的独特性来自受力、层次与空间组织，避免只换accent色。

## 实现与参数

共享C色板与M材质：stone roughness.88、wood.8、metal roughness.32/metalness.9、glass .05/opacity.28；Builder以material为Map键聚集变换后的非索引几何，再mergeGeometries为每材质一mesh；不同城市build({rng,accent})使用同一套触感。

## 审美细节

ivory #efe4cf / plaster #f3e9d8为体量，terracotta #c26a43为屋顶，sea #2f6377为冷区，gold #e2b354 / lamp #ffc477作金属与暖光。Octavia靠悬挂空间，Eusapia靠剖面层叠产生区别。未看渲染，不能断言55城都达到一致质量。

## 适用条件

- 场景具备不同空间主题
- 颜色与材质角色已区分
- 共享shader与版本边界清楚

## 相邻方案与区别

Nexus通过楼体类型区分建筑；本卡提升到跨场景材质契约。与一套相同模型换色不同，语义结构仍独立。

## 失败模式

- 统一色板不能代替真实材质细节
- 全几何合并会失去局部拾取/独立变换粒度
- glass透明叠层有排序问题
- 缺根LICENSE和package许可，直接复用不可判允许

## Movie 裁决

- **verdict**：adapt
- **reason**：可为多个Place建立材质家族，同时保留各场景形态主题。

## Frontend 裁决

- **verdict**：reference
- **reason**：借统一设计约束，当前无明确许可不能直接搬代码。

## 最小对照

选3个已有场景同曝光比较：去掉accent后仍可识别结构差异，换入共用材质后不丢场景语义；只靠换色辨认即失败。

## 源码证据

- [Repos/invisible-cities-opus-5.5/src/kit.js:54–118](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/kit.js#L54-L118)：共享色板、stone/metal/glass等材质参数
- [Repos/invisible-cities-opus-5.5/src/kit.js:141–200](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/kit.js#L141-L200)：Builder将变换和顶点色写入几何
- [Repos/invisible-cities-opus-5.5/src/kit.js:299–316](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/kit.js#L299-L316)：按材质合并geometry并控制阴影
- [Repos/invisible-cities-opus-5.5/src/cities/octavia.js:8–19](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/octavia.js#L8-L19)：峡谷悬网结构
- [Repos/invisible-cities-opus-5.5/src/cities/eusapia.js:23–63](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/eusapia.js#L23-L63)：上下共用lots布局的双城结构

## 项目效果图

![invisible-cities-opus-5.5 · live_site_still](../assets/previews/live-invisible-cities-atlas.png)

小型城市按类别列与序号行放在棋盘上；瓷金造型和标签共用空间位置，分类导航在下方。

来源：[原作者/出处](https://p.migdal.pl/invisible-cities-opus-5.5/) · live_site_still。本轮线上默认Atlas静帧，线上版本未绑定本地HEAD；不证明全部55城细节。

![invisible-cities-opus-5.5 · live_site_still](../assets/previews/live-invisible-cities-journey.png)

选择Journey后保留城市身份，发光线路把叙述顺序联结起来。

来源：[原作者/出处](https://p.migdal.pl/invisible-cities-opus-5.5/) · live_site_still。切换后的单帧，不据此认证完整过渡或输入中断。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-08](../patterns/MP-08.md)
