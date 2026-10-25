# SD-LR03 · 从脚边动作拉远到全程痕迹，并分开两类取景器
案例：[ little-rain-cloud ](../cases/little-rain-cloud.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

回望镜头的叙事收益取决于能否看见“刚才走过的路”，而不是只把相机移远。

## 实现与参数

交互C：smooth(0,6,cineT)，距离→70、高度→55、每秒旋转.04，平滑系数1-exp(-2.5dt)，视线仍中心对准当前主体。独立?scene=aerial：整段pathPts旋转到屏幕u/r轴，范围加8米，取水平/垂直FOV约束较大高度，再乘margin默认1.35。两者不是同一个算法。

## 审美细节

历史04-look-back可见暖沙、白云和曲折绿线；证明静帧能呈现路径，不证明C镜头自动框全程。长路径或偏离主体的路径尤其需要aerial拟合。

## 适用条件

- 存在值得回看的空间历史
- 轨迹采样有上限与简化策略
- 镜头拥有安全退出

## 相邻方案与区别

NexusCity关键帧轨道负责展示既定空间；此处镜头取决于用户已造成的空间变化。

## 失败模式

- 固定距离拉远不保证完整路径入画
- top-down高度按中心groundH估算，复杂地形仍可能遮挡
- 本仓pathPts只在AERIAL分支采集，不可假定C已有全路径

## Movie 裁决

- **verdict**：prototype
- **reason**：可建立特写行动→远景结果的短片结构，符合当前镜头先近后远方向。

## Frontend 裁决

- **verdict**：adapt
- **reason**：仅用户触发回望；保留退出和回到原控制状态。

## 最小对照

短直线、U形和横竖屏长曲线三例；所有重要痕迹进入安全框，主体可辨；退出时控制连续。地形脊遮挡或裁掉起点判失败。

## 源码证据

- [Repos/little-rain-cloud/main.js:676–697](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L676-L697)：aerialCamera将pathPts投影到屏幕地面轴，按水平/垂直FOV求所需高度
- [Repos/little-rain-cloud/main.js:975–999](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L975-L999)：C电影模式6秒拉至距离70/高度55；aerial另行每秒采2点并覆盖相机

## 项目效果图

![little-rain-cloud · observed_still](../assets/previews/little-rain-cloud-f483b6c2dde7.png)

已view_image shots/04-look-back.png：暖沙丘、白云、深湿痕与绿色曲线；它是历史静帧，只支持构图判断，不支持动画或当前运行验收。

来源：[原作者/出处](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/shots/04-look-back.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[CINE-02](../lenses/CINE-02.md) / [CINE-07](../lenses/CINE-07.md)

[MP-11](../patterns/MP-11.md)
