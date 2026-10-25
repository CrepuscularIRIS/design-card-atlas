# SD-OT02 · 把程序材质变成可携带的颜色、粗糙度和法线资产
案例：[ offshore-tower ](../cases/offshore-tower.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

程序节点在制作软件里成立还不够；把设计关系转成明确贴图通道，网页才能保留同一材质意图。

## 实现与参数

broad Noise scale4.2/detail5，streak UV×(8*streakiness,.38)，fine scale175；调色ramp→BaseColor，rough映射→ORM.G，metal常数→B，R恒1。EMIT烘焙不包含现场灯光；height中心差分×3.2→切线法线，NormalMap strength=.7，重建可导出的image材质。网页再加.91–1.055大块、.89–1.025纵向乘色与≤.13铜锈mask。

## 审美细节

橙钢#48251A/#B54814/#EB6D1C/#F58C3B，roughness .5–.84/metal .28；深钢metal .78，锈接缝roughness .72–.96，基础盐蚀混凝土.84–.98。灰绿背景中橙塔成为焦点，深骨架保留层次。ORM名字不意味着烘过AO，此处O恒1。

## 适用条件

- 明确sRGB与non-color通道
- 导出器确实使用图像材质
- 能禁用二次shader对照

## 相邻方案与区别

Tidewater主要用扫描底材与涂层；此卡以程序材质烘焙为来源。两者共享米制/通道规范，但不能把扫描质感与程序噪声视为同等证据。

## 失败模式

- np.roll只包裹法线差分，不证明底色/高度贴图天然无缝
- 贴图名ORM不能当AO存在证明
- 常数metal仍是艺术参数，不代表锈层物理混合
- TSL fromMaterial和本站r170不直接兼容

## Movie 裁决

- **verdict**：adapt
- **reason**：适合保证Blender素材向电影预览的材质可携带性。

## Frontend 裁决

- **verdict**：adapt
- **reason**：提取通道约定与验证办法，不迁移r180 TSL管线。

## 最小对照

同资产Blender/本站固定灰光对照，金属与绝缘层仍可分；断网仍加载全部贴图。检查重复边缘、法线方向和凹凸强度；若调色偏移只能靠额外噪声掩盖则失败。

## 源码证据

- [Repos/offshore-tower/Offshore_Tower_Generator.py:116–207](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L116-L207)：UV平面烘broad/streak/fine噪声，ORM的R恒1
- [Repos/offshore-tower/Offshore_Tower_Generator.py:210–257](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L210-L257)：高度图差分法线、重建image-based Principled并pack
- [Repos/offshore-tower/Offshore_Tower_Generator.py:262–273](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L262-L273)：五类材质色板/粗糙度/金属参数
- [Repos/offshore-tower/app/src/scene.js:65–90](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/app/src/scene.js#L65-L90)：网页另加world-space条纹与patina，属于额外视觉层

## 项目效果图

![offshore-tower · observed_still](../assets/previews/offshore-tower-a3430d9d43f1.png)

已view_image Tower_Verification_Views.png六视图拼图：橙色收分塔、深骨架、多层维护平台、后侧窗组、底部交叉支撑、顶部天线与吊臂。历史离线渲染，不是当前网页截图或实时性能证据。

来源：[原作者/出处](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Tower_Verification_Views.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
