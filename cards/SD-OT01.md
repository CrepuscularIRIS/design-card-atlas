# SD-OT01 · 让主轮廓同时约束外板、接缝、开口与附属结构
案例：[ offshore-tower ](../cases/offshore-tower.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

模型打磨首先使主次构件彼此对得上；以少量真实结构数据派生细节，比逐个摆装饰件更不容易悬空或错位。

## 实现与参数

Z_LEVELS=[4.42,6.85,10.55,14.98]与R_LEVELS=[2.12,1.98,1.55,1.18]→radius_at/face_frame→8面×3段外板；每道波纹6个横向采样，位移.025+.024*(cos+0.28cos2)，板厚.045。强化梁/螺栓沿相同面坐标，窗先boolean_cut再放玻璃与外框；板缝避让window_layout。

## 审美细节

玻璃相对center后退.035，外框前出.105，窗台再前出.035，形成厚度而非黑色贴方块。看过六视图拼图：橙色塔身收分、深色平台与架腿分层，背面亦有窗和设备，底视图可见斜撑。

## 适用条件

- 统一单位与坐标
- 开口数据先于装饰缝线
- 近景可见轮廓细节值得真实建模

## 相邻方案与区别

与Invisible Cities受力路径卡互补，此卡进一步给出共享截面和开口数据；与单纯细分面数不同，细节来自结构约束。

## 失败模式

- 几何波纹远处可能产生闪烁
- boolean与solidify须在导出后检查
- 微细螺栓不该替代主轮廓质量
- 源模型含品牌标记，不能直接把标记带到本站

## Movie 裁决

- **verdict**：prototype
- **reason**：适合现有hero建筑从特写到远景的结构连续性打磨。

## Frontend 裁决

- **verdict**：reference
- **reason**：方法可自写，源仓未找到许可，不能直接搬生成器/GLB。

## 最小对照

同一资产改一个高度/半径后导出六方向截图；开口/接缝/梯子随形体更新，窗框无悬浮，平台支点落在主结构；正面好看但背面无连接则失败。

## 源码证据

- [Repos/offshore-tower/Offshore_Tower_Generator.py:499–534](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L499-L534)：窗玻璃后退、外框/窗台前出，栏杆按段生成
- [Repos/offshore-tower/Offshore_Tower_Generator.py:707–802](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L707-L802)：共享高度/半径控制波纹锥面、接缝、螺栓、角柱与梯子
- [Repos/offshore-tower/Offshore_Tower_Generator.py:869–914](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L869-L914)：维护平台、三角托架、楼梯踏步/扶手共用端点
- [Repos/offshore-tower/Offshore_Tower_Generator.py:942–977](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L942-L977)：立面开洞后置窗，面板缝主动避开开口

## 项目效果图

![offshore-tower · observed_still](../assets/previews/offshore-tower-a3430d9d43f1.png)

已view_image Tower_Verification_Views.png六视图拼图：橙色收分塔、深骨架、多层维护平台、后侧窗组、底部交叉支撑、顶部天线与吊臂。历史离线渲染，不是当前网页截图或实时性能证据。

来源：[原作者/出处](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Tower_Verification_Views.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-05](../patterns/MP-05.md)
