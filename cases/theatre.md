# theatre
实读关键帧插值的hold/Bezier分支与相机目标跟踪；这是编排工具的机制，不是现成场景美术。

## 案例档案

[来源仓库](https://github.com/theatre-js/theatre)
分析版本：`6ea82b938ea49609489f6377ded693ccc6ee8f5b`

模型归属未独立认证。

## 初始源码审计边界

未读编辑器UI、音频播放与Sequence完整控制；不建议整包升级。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [FM-013 · 用停顿段与曲线段分别表达观看和移动](../cards/FM-013.md)

停留本身应是编排的一段，而不是移动速度偶然变慢；适合先特写停顿再拉远。

停留本身应是编排的一段，而不是移动速度偶然变慢；适合先特写停顿再拉远。

**Movie：prototype** · 匹配特写→拉远场景SOP
**前端：adapt** · 可用于短暂过渡，必须可跳过

失败条件：- 时间曲线平滑不等于空间路径不过冲
- 全段都ease导致节奏拖沓

### [FM-014 · 分离镜头位置轨迹与注视目标轨迹](../cards/FM-014.md)

移动时保留物件为视觉锚点，离开镜头后恢复用户相机。

移动时保留物件为视觉锚点，离开镜头后恢复用户相机。

**Movie：adapt** · 适合特写拉远保持焦点
**前端：reference** · 不要持续强制自由探索相机朝向

失败条件：- 对象嵌套父变换时.position不是worldPosition
- 目标与镜头重合导致方向不稳定

## 项目效果与观察材料

![theatre · author_demo_frame](../assets/previews/ui-theatre-1.png)

作者GIF第1秒：火箭场景、编辑相机小窗、右侧相机参数以及底部关键帧与曲线编辑器同屏；不能由此帧验证编辑器交互。

来源：[原作者/出处](https://raw.githubusercontent.com/AriaMinaei/theatre-docs/main/docs/.vuepress/public/preview-3d-short.gif) · author_demo_frame。实际查看所采用的1秒抽帧；没有运行项目、没有连续播放或验证动态行为。

## 复用边界

- **status**：observed
- **evidence**：LICENSE Apache-2.0，迁移需保留NOTICE/许可并标修改
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
