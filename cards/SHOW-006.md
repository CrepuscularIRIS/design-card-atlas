# SHOW-006 · 限制Bloom输入峰值以保留爆发的局部性
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

爆炸和发光核心允许很亮，送入模糊的能量被限制，减少全屏白雾；封面中心依然强烈过曝，不能声称问题已彻底解决。

## 实现与参数

createPost→bloom.materialHighPassFilter字符串注入→texel.rgb×min(1,6/maxChannel)→bloom→OutputPass→FinalShader。

## 审美细节

爆炸和发光核心允许很亮，送入模糊的能量被限制，减少全屏白雾；封面中心依然强烈过曝，不能声称问题已彻底解决。

## 适用条件

- HDR管线且明确bloom分支
- 保留现有tone mapping顺序

## 相邻方案与区别

不同于整体降曝光：仅控制扩散而非削弱所有受光。

## 失败模式

- 字符串替换随Three版本失效
- 硬上限可能压平英雄光晕
- 封面仍有大面积中心炫光

## Movie 裁决

- **verdict**：prototype
- **reason**：高亮高潮与镜头逆光可做单独A/B。

## Frontend 裁决

- **verdict**：adapt
- **reason**：交互物轮廓与文字必须在爆发时可读。

## 最小对照

保持曝光，比较上限无/6/3；主体轮廓和招牌可读性不改善或高光发灰即失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/warp-shooter/src/post.js:66–82](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/warp-shooter/src/post.js#L66-L82)：Bloom=.75/.42/.86；高通输入RGB最大通道限制6，OutputPass后加最终效果

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-3656ae17e6b9.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/warp-shooter.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-02](../patterns/MP-02.md)
