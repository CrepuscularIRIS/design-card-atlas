# 巨字随景退场

分组：排版 UI · 主维度：H 字级与退场、C 负空间、G 机位切换、A 文字亮度、I 从命名到观看 · 情绪：克制、肃穆

## 一句话

全景用大字命名世界，进入近景后让标题退场，保留足够轻的导航。

[![黑沙之境 · 海岸全景](shots/01.jpg)](shots/01.jpg)
[黑沙之境 · 海岸全景](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/kimi/iceland-black-sand/dist/index.html) · 全景左侧留出标题区，右柱壁与中远礁仍可读。

| 参考 | 参考 |
|---|---|
| [![黑沙之境 · 玄武岩柱](shots/02.jpg)](shots/02.jpg) | [![雷尼斯黑沙滩 · 海滩](shots/03.jpg)](shots/03.jpg) |
| [黑沙之境 · 玄武岩柱](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/kimi/iceland-black-sand/dist/index.html) · 点击近柱后巨字消退，四周细标注保留方向。 | [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) · 另一海滩把标题从一开始压到左上，作为无需巨字的对照方案。 |
## 看哪里

1. 黑沙之境 · 海岸全景：全景左侧留出标题区，右柱壁与中远礁仍可读。
2. 黑沙之境 · 玄武岩柱：点击近柱后巨字消退，四周细标注保留方向。
3. 雷尼斯黑沙滩 · 海滩：另一海滩把标题从一开始压到左上，作为无需巨字的对照方案。

## 拆解

百分比与颜色为画面目估，非渲染器测量。

- H：Kimi全景衬线标题约为正文7–9倍，左起约7%画宽；近景后该标题完全退出，只留小号机位名与编号。
- C：全景右壁重、左字亮，形成左右平衡；近柱占据中央后，若仍保留同等大字，左右平衡将变成两主体争夺。
- G：实际点击02时先见标题变淡，之后到达柱壁近机位。标题和观看任务一起变化；未实测浏览器动画时长。
- A：浅白字近#F1F0E9，暗石接近#171D20；大字天然是最高对比物，因此退场比降低石壁亮度更直接。
- I：开场回答“这是哪里”，近景回答“我要看什么”。Opus海滩小标题证明常驻命名也可以足够，但不要再给它一次巨大的视觉权重。

## 做法

将场景身份标题与常驻导航分层。只有建立场景时出现大标题，进入细节机位后淡出身份层，导航与返回保持可用。

源码事实：Kimi index!==0启用detail-view；CSS hero-copy transition为opacity/transform各0.6s，detail-view透明度0、translateX(-20px)；h1 clamp(70px,7.5vw,118px)。这些参数不等于通用最佳值。

源码：[按机位切换信息层](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/kimi/iceland-black-sand/src/iceland/main.js#L137-L149)；[压缩CSS中hero-copy与detail-view规则](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/kimi/iceland-black-sand/src/iceland/style.css#L1)。只借思路，不复制未授权代码。

## 迁移到博客

title页保留一次有力度的名称，进入BlackCityHall或Shrine近景后消退；hIE会面背景只保留轻量地点名，不让标题和人物争夺第一眼。

建议先用0.4–0.7秒文字退场，机位另按距离安排；保留返回按钮，避免全UI一起消失导致用户失去方向。减少动画偏好时直接切换可见状态。

搭配分级机位靠近与低对比角标；冲突是巨字压画面卡的永久版本，以及相机到达后又弹出一大块说明面板。

## 反例

远征页的白实字和描边字占左约30%画宽、40%画高，第一眼读广告，再看到山谷。若迁入Citadel，应把这类标题限制在开场，而不是让它常驻于探索或会面画面。

[![水牛远征 · 大字与山谷](shots/04.jpg)](shots/04.jpg)
[水牛远征 · 大字与山谷](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/buffalo/01-expedition.html) · 广告巨字在山谷前常驻，目标小帐篷很难与之争夺第一眼。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
