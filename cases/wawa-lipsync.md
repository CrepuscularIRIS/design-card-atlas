# wawa-lipsync
小库以频带启发式和时间惯性驱动嘴形。发现默认maxVisemeDuration=100与注释100–300ms渐变不一致，不能只引用README称高质量口型。

## 案例档案

[来源仓库](https://github.com/wass08/wawa-lipsync)
分析版本：`312dc31a1ee998248aae3431474f455bfc3ae3e1`

模型归属未独立认证。

## 初始源码审计边界

已读核心Lipsync主要链路与viseme枚举；未穷尽computeVisemeScores每个阈值、R3F示例与音频运行。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [CN-020 · 从音频频带估计有限嘴形再用短时惯性减抖](../cards/CN-020.md)

从音频频带估计有限嘴形再用短时惯性减抖。这是由该仓实现提炼的候选操作，跨项目效果待验证。

有限嘴形适合2D分层嘴部映射；它是启发式声学分类，并非可靠音素识别或有字幕对齐。

**Movie：reference** · 离线影片宜用人工/文本对齐；本库可作预览
**前端：defer** · 当前2D静图没有嘴部层则无直接收益

失败条件：- 注释说100–300ms渐变，但maxVisemeDuration=100使中段分支不可达
- 静音不入history导致旧特征可能残留，需先测收口

## 项目效果与观察材料

![wawa-lipsync · promotional_reference](../assets/previews/ui-wawa-lipsync-1.jpg)

README链接的作者教程封面：两种角色面孔与Real-Time Lipsync标题。它是宣传参考图，不是运行截图或口型同步证据。

来源：[原作者/出处](https://img.youtube.com/vi/GXU1amqvJF8/maxresdefault.jpg) · promotional_reference。已实际查看作者教程缩略图；不能作为效果主图，不能证明模型发声、口型正确或实时性能。

![wawa-lipsync · live_site_still](../assets/previews/live-wawa-lipsync.png)

粉色背景中角色正面占右侧；左侧频谱、viseme、音量与质心读数并列，底部为样本发音按钮。

来源：[原作者/出处](https://wawa-lipsync.wawasensei.dev/) · live_site_still。本轮只看静默初始角色与仪表；未播放声音，未证明口型同步或频谱判定准确。

## 复用边界

- **status**：observed
- **evidence**：LICENSE: MIT
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
