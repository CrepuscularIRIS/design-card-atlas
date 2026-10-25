# SD-OT03 · 保留编辑部件，只按装配与材质生成网页交付批次
案例：[ offshore-tower ](../cases/offshore-tower.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

美术源文件需要细部件可改，网页资产需要一致的落地几何；两种需求通过独立导出副本衔接。

## 实现与参数

生成器用evaluated_depsgraph得到含modifier网格，保留所有数据层、matrix_world，再按(collection.name,material.name)聚组，源细件不直接并掉；GLB只选副本，Y-up、extras=true、无动画/灯/相机。当前GLB只读解析核对：51 meshes/51 nodes、149104三角、14材质、15张内嵌图、10450464字节、0动画。

## 审美细节

批次保持基础/塔身/屋顶/通信/吊臂等装配可追踪；manifest的111080是导出modifier前基础网格数，不应拿它当最终渲染三角数。当前检查只确认资产结构，未执行Blender或渲染。

## 适用条件

- 需要维护可编辑源
- 导出副本不会覆盖源部件
- 选择装配粒度前确定交互需求

## 相邻方案与区别

Invisible Cities按材质合并用于运行时生成；本卡在离线导出副本中保留装配层次，适合本项目既有GLB方向。

## 失败模式

- join后丢单螺栓/窗扇拾取粒度
- 当前脚本只取material_slots[0]，不能泛化到多材质对象
- 无动画导出不适用于活动门和角色
- mesh.data.validate不是视觉验收

## Movie 裁决

- **verdict**：adapt
- **reason**：多视角电影镜头可复用同一交付模型，源部件仍便于返工。

## Frontend 裁决

- **verdict**：reference
- **reason**：当前性能后置；先保留交付一致性，再根据实际场景决定是否合批。

## 最小对照

导出前后比对bounds、材质槽、法线/UV及关键轮廓，逐装配隐藏检验内部结构；每个导出图像有内嵌buffer或明确本地路径。线框与实体不一致则失败。

## 源码证据

- [Repos/offshore-tower/Offshore_Tower_Generator.py:1325–1350](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L1325-L1350)：曲线/文字转mesh，附加assembly/units元数据
- [Repos/offshore-tower/Offshore_Tower_Generator.py:1352–1405](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L1352-L1405)：求值modifier副本，按assembly/material join并导GLB
- [Repos/offshore-tower/Tower_Asset_Manifest.json:1–26](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Tower_Asset_Manifest.json#L1-L26)：作者输出清单给物件、三角数、大小及装配名

## 项目效果图

![offshore-tower · observed_still](../assets/previews/offshore-tower-a3430d9d43f1.png)

已view_image Tower_Verification_Views.png六视图拼图：橙色收分塔、深骨架、多层维护平台、后侧窗组、底部交叉支撑、顶部天线与吊臂。历史离线渲染，不是当前网页截图或实时性能证据。

来源：[原作者/出处](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Tower_Verification_Views.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
