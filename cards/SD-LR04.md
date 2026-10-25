# SD-LR04 · 湿润同时改变颜色、粗糙度与微表面纹理
案例：[ little-rain-cloud ](../cases/little-rain-cloud.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

地表状态应在多个材质线索上自洽：湿沙变深变光滑，水膜还弱化微细起伏，而非只刷一层蓝色。

## 实现与参数

wetK=smoothstep(.02,.5,wm.r)，grnK=smoothstep(.05,.8,wm.g)；沙色乘mix(1,.62,wetK)，混入(.20,.31,.07)*grnK*.85，roughness由.93向.38随wetK*(1-grnK*.6)过渡，ripple强度随湿润减弱。草底深绿/尖黄绿，tip²调制逆光。

## 审美细节

沙基色在(.62,.37,.17)和(.88,.58,.31)间变化，绿色也压在暖场景亮度关系中。这里是材质参数与假微表面的协同，尚未建立积水流动。

## 适用条件

- 同一mask坐标与网格匹配
- 曝光固定
- 材质有可控roughness/normal通道

## 相邻方案与区别

与后期整屏调色不同只改发生接触的表面；与Tidewater湿岸共享状态材质耦合，可跨仓归并。

## 失败模式

- 把近景沙纹公式用于大理石会失真
- mask分辨率仅1米/格，靠平滑掩饰边界
- shader字符串替换仍依赖具体材质与版本

## Movie 裁决

- **verdict**：adapt
- **reason**：适合地面近景的连续状态变化。

## Frontend 裁决

- **verdict**：prototype
- **reason**：优先验证一个已有PBR地材，不换整套渲染器。

## 最小对照

锁相机/曝光/灯光，干/湿/长草三态对照；湿区高光连续、绿区不过亮、纹理无突变；只剩色块或越界接缝则失败。

## 源码证据

- [Repos/little-rain-cloud/main.js:174–220](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L174-L220)：onBeforeCompile采湿图，控制沙色、绿化、roughness和ripple normal
- [Repos/little-rain-cloud/main.js:269–306](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L269-L306)：草1.4秒生长、叶尖色差、逆光与随高度变化的摇摆

## 项目效果图

![little-rain-cloud · observed_still](../assets/previews/little-rain-cloud-f483b6c2dde7.png)

已view_image shots/04-look-back.png：暖沙丘、白云、深湿痕与绿色曲线；它是历史静帧，只支持构图判断，不支持动画或当前运行验收。

来源：[原作者/出处](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/shots/04-look-back.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[CINE-03](../lenses/CINE-03.md)

[MP-06](../patterns/MP-06.md)
