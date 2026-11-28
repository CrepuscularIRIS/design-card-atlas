# Citadel 视觉场景 — cognitive lenses
Source: ~/Blog/design-card-atlas public/docs/DIMENSIONS.md（A–I 九组拆解维度）· 25 张正式卡 README 的 impl 表 · public/recipes；atlas main 0009b5e（2026-11-28）。卡是索引：打磨方案只引用 card:<id> / recipe:<id>，实现索引以各卡 README 的 impl 表为准（本地 Repos/ file:line、许可、Citadel 落点）。
D01 backlight-reveals-silhouette：逆光分轮廓——主体边缘一圈光把它从背景里分出来，颜色与亮度给数值。
D02 broken-form-remains-legible：破损可读——断口、磨损、残骸不毁掉形体的可辨认性；完整与破损对照。
D03 caustics-on-receivers：焦散落在接收面上——高光分工与局部色散，不是全屏加亮（水族馆/浅水/水面下）。
D04 cold-world-warm-refuge：冷世界暖避难——冷暖分区把视觉重心给发光的居住暗示（暖窗对冷夜）。
D05 colonnade-rhythm：柱廊节奏——重复与尺度、消失点、侧光下的仪式感。
D06 colossus-crosses-the-frame：巨物过框——局部可识别 + 果断裁切 + 近身透视 = 压迫（巨构/史诗感）。
D07 diagonal-mass-balance：对角体量平衡——不对称张力靠亮暗配重与透视方向。
D08 emptiness-isolates-landmark：空场孤立地标——负空间与高光预算只给一个单体。
D09 fog-separates-depth：雾分层次——距离雾/高度雾切出前中后景，雾色取自天光。
D10 framed-distant-view：框中远景——画中框、近远尺度对照、观察位置。
D11 gold-accents-matte-mass：金点缀哑面体——小面积光泽只放结构节点。
D12 high-view-reads-hierarchy：高视点读层级——布局、通路、高低层级与标注空间。
D13 low-chroma-value-steps：低饱和明度阶——大色块靠明暗层级而不是饱和度。
D14 low-eye-entry：低视点入境——通道引导线、前景裁切、雾中纵深。
D15 mirror-beside-roughness：镜面傍粗面——粗糙度对照与接触边界保存形体（湿地面倒影）。
D16 networks-link-industrial-masses：网络连接工业体量——设备层级、线路、表面因果。
D17 ordered-frame-wild-growth：规则框住野生生长——藤蔓/荒草只在规则体上生长（复绿）。
D18 scale-by-familiar-objects：熟悉物显尺度——人、车、窗格、云做参照。
D19 side-light-carves-stone：侧光刻石——主光与阴影把凹凸层级读出来。
D20 staged-camera-approach：分镜式接近——机位切换、前中后景、重复节奏（停顿—加速—缓停）。
D21 terraces-carry-the-temple：层台承殿——层台与主殿、路径层级、面转折。
D22 thin-line-hud：细线 HUD——等宽与边栏、发光面积克制、状态色。
D23 type-yields-to-scene：字让位于景——字级与退场、负空间、文字亮度。
D24 water-continues-silhouette：水延续剪影——反射连续性、水平分界、波面。
D25 weathering-follows-form：风化随形——表面状态与破损层级由形体决定（锈、尘、湿）。
Group cues: A 光影（主光方向/光源类型/光比/边缘光/接触阴影与 AO/bloom 阈值/光叙事/反射高光）· B 色彩（主辅色 hex/冷暖分区/饱和度分布/明度阶梯/调色/点缀色）· C 构图重心（第一眼落点/主体位置/负空间/引导线/前中后景/平衡）· D 造型尺度（剪影/尺度对比/体块组织/细节密度/重复节奏/风格语汇）· E 材质（粗糙度/金属感/湿干尘锈/微结构/透明半透/发光材质）· F 水流体大气（水面/湿地面/雾/体积光/粒子/天空背景）· G 镜头运动（焦距透视/景深/运动/节奏曲线/转场/场景动态）· H 排版 UI（字体性格/字级/字与画面/网格/HUD 语汇/信息密度/交互反馈）· I 氛围叙事（情绪词 1–3 个/时间天气/世界观暗示/克制）。
Paradigm cues: 当前站点 = 风格化低多边形 + 烘焙光照（baked GLB，昼夜变体）+ 少量实时层（placeRain 雨/湿反射、fx 粒子涟漪脚印、霓虹、keeper lamp、verbScene 贴花）。集成优先：先复用项目内套路（src/world/fx、places、worlds/cardfx、audio 全合成）与 ~/Blog/Repos 带许可资产/手法（navis、gremlin-church、stanford-torus、three-gpu-pathtracer 等 MIT 可读码；画师静帧只借构图/光/雾手法，不搬资产），从零手写须说明理由。目标 = card 宣传片级；已知差距：远景世界感 / 主角材质 / 光照接触 / 后处理遮罩 / 细节成因。43 个 place 场景 id 见 citadel/src/world/places/manifest。
Anti-patterns: 禁紫渐变、Inter、玻璃拟态、"Scroll ↓"、可见 em-dash、Google Fonts link；不开第二条后期链；不升 three.js；普通交互不震屏、不 FOV 冲击、不全屏闪；物件只在声明时动；减少动态下不做自动位移/转向/FOV；title 与 atlas（地图）的 3D 观感不动；hIE 只用 2D 立绘；不为谜题改已上线台词。
Evaluation: 以截图本身为准不以读数为准——同机位 before/after 成对，自己看图；headless 六坑（等 placeApi.scene 与 loadingCard 落下、__noPostcard、setFixedTime 不用 URL t=、goView 等两帧、keeper lamp 到场冷染相位、readableArrival lift 覆盖夜色、不直调 render）；参考标尺 4.4–5.0 与及格线双口径，已上线版本是基线不回退；Low/Software 档必须不坏；音量与配乐只能真人戴耳机验收。
Failure boundaries: baked 合并网格里的物件不能单独动（先普查再声明 movable）；SwiftShader 帧率不代表真机；NVMe 未挂载时 cacheDir/截图走 /tmp；gameplay/refactor 分支是用户暂停的玩法候选，视觉线不依赖它。
绑定项目：~/Blog（Crepuscular Citadel）。原始卡、DIMENSIONS、recipes 按需读取，domainCards 是当前命中的真实卡片；引用卡片编号与图上位置。卡是参考不是实施承诺。
