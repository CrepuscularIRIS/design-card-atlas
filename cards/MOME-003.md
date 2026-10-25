# MOME-003 · 以粒子年龄闭式求值保留烟羽形态，同时支持任意帧重放
案例：[ map-of-middle-earth ](../cases/map-of-middle-earth.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

mount-doom图显示暗烟柱、顶部大范围烟团和熔岩亮核。机制不是随机透明球堆：烟柱升高、扩散、顺风、顶棚合并各有阶段；重放能力由代码结构支持但本轮未验随机帧像素一致。

## 实现与参数

每个粒子12个常量；a=fract(tFx/life+phase)，湍流valueNoise(a*2.6+nz,...,seed)。伞盖顺风拉长1+.8*sh，横风缩至1-.2*sh；主体淡入smooth(0,.05,a)，自由烟羽末段.75→1淡出。tFx=at*film.tFxScale。

## 审美细节

mount-doom图显示暗烟柱、顶部大范围烟团和熔岩亮核。机制不是随机透明球堆：烟柱升高、扩散、顺风、顶棚合并各有阶段；重放能力由代码结构支持但本轮未验随机帧像素一致。

## 适用条件

- 效果可接受闭式/美术轨迹
- 时间、风和seed在所有样本间有确定来源

## 相邻方案与区别

与真实流体仿真不同，是可控的镜头烟羽；可把复杂模拟烘焙为体积序列作为近景替代。

## 失败模式

- 循环年龄重置处淡出不足会跳变
- 实时骤变风向会整体瞬移，因为无历史惯性
- 不适合要求精确碰撞/流体守恒的物理烟

## Movie 裁决

- **verdict**：prototype
- **reason**：适合离线随机帧、补帧和快门采样，也便于A/B。

## Frontend 裁决

- **verdict**：adapt
- **reason**：暂停恢复/拖时间可用；用户控制风时需过渡或重新定义局部时钟。

## 最小对照

顺序播放和随机访问同一组时间点比对；出现不同烟形、循环跳变、暂停后跳帧则失败。

## 源码证据

- [Repos/map-of-middle-earth/src/effects/particles.ts:86–125](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/effects/particles.ts#L86-L125)：seed/k/j生成固定粒子常量，寿命抖动.8–1.2，图集16格
- [Repos/map-of-middle-earth/src/effects/particles.ts:185–254](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/effects/particles.ts#L185-L254)：age来自fract(tFx/life+phase)，按高度弯曲并在顶棚下形成顺风非对称伞盖
- [Repos/map-of-middle-earth/src/effects/particles.ts:255–320](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/effects/particles.ts#L255-L320)：灰尘与水雾各用不同轨迹/消隐，靠近顶棚透明度衰减
- [Repos/map-of-middle-earth/src/tour/compile.ts:156–215](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/tour/compile.ts#L156-L215)：SceneState包含绝对tFx、camera、weather、events

## 项目效果图

![map-of-middle-earth · historical_still_viewed](../assets/previews/map-of-middle-earth-9732ef806c0e.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/docs/images/lake-town.jpg) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

![map-of-middle-earth · historical_still_viewed](../assets/previews/map-of-middle-earth-c4a392f4439d.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/docs/images/mount-doom.jpg) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[CINE-06](../lenses/CINE-06.md)

[MP-19](../patterns/MP-19.md)
