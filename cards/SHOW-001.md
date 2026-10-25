# SHOW-001 · 按可见贡献分配灯位，保持实体光源与局部受光对应
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

设计推论：把有限动态光预算放在当前画面真正读到的灯笼、招牌与行动附近；封面可见暖窗和灯笼，不能由静帧证实切灯无跳变。

## 实现与参数

LightPool(scene,8,2,512)→update(sources,camX,catX,catY,t)；普通灯13.5到9.5距离淡入，阴影8.5到5.5，阴影强度0.85。

## 审美细节

设计推论：把有限动态光预算放在当前画面真正读到的灯笼、招牌与行动附近；封面可见暖窗和灯笼，不能由静帧证实切灯无跳变。

## 适用条件

- 来源有on/level/priority和稳定身份
- 距离度量按场景维度重写

## 相邻方案与区别

不是增加灯数；与烘焙光照互补，静态照明仍可保留。

## 失败模式

- 源码只按x距离，直接搬入自由3D走动会错选
- 槽位换灯仍可能跳变
- r170阴影属性需核对

## Movie 裁决

- **verdict**：adapt
- **reason**：电影路径已知可事先固定英雄灯，避免依赖运行时抢灯。

## Frontend 裁决

- **verdict**：adapt
- **reason**：自由走动适合按贡献选光，但须改为三维距离与遮挡感知。

## 最小对照

同一走廊沿灯列往返，录制槽位ID与亮度；交界处墙面闪一下或英雄灯被小灯替代即失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/catwalk/js/lights.js:10–91](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/catwalk/js/lights.js#L10-L91)：默认固定8灯/2阴影；阴影灯按parity选最近，普通灯按view×intensity×level×priority排序且保持槽位

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-d4e64693ab20.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/catwalk.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-03](../patterns/MP-03.md)
