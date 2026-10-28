# 焦散落在表面

分组：材质 · 主维度：E 透明与折射、A 高光分工、B 局部色散、C 留白、F 浅水层次 · 情绪：澄澈、精密

## 一句话

把透光的物体、表面高光和投到周围的光斑分开组织，透明材质才有空间关系。

[![Clearwater](shots/01.jpg)](shots/01.jpg)
[Clearwater](https://aureliengmz.github.io/clearwater/) · 浅绿光网落在可见水底石粒上，白色表面反光另处于上中部。

| 参考 | 参考 |
|---|---|
| [![Glass goblets · 12s](shots/02.jpg)](shots/02.jpg) | [![Glass goblets · 21s](shots/03.jpg)](shots/03.jpg) |
| [Glass goblets · 12s](https://x.com/liambraus/status/2113724051332194589) · 透明棱面集中在杯腹，彩色光斑投到左侧地面，背景留得很安静。 | [Glass goblets · 21s](https://x.com/liambraus/status/2113724051332194589) · 换一视角后仍能区分实体轮廓、折射碎色和投地光斑。 |

<a href="shots/05.png"><img src="shots/05.png" width="420" alt="清流 · 浅滩河床"></a>
[清流 · 浅滩河床](https://seiryu.miraicode.one/) · 近水石床仍可辨认，细焦散贴在水底，岸上白岩与暗叶另成层次。
## 看哪里

1. Clearwater：浅绿光网落在可见水底石粒上，白色表面反光另处于上中部。
2. Glass goblets · 12s：透明棱面集中在杯腹，彩色光斑投到左侧地面，背景留得很安静。
3. Glass goblets · 21s：换一视角后仍能区分实体轮廓、折射碎色和投地光斑。
4. 清流 · 浅滩河床：近水石床仍可辨认，细焦散贴在水底，岸上白岩与暗叶另成层次。

## 拆解

玻璃两图属于同一作品；与Clearwater、后续版清流构成三个独立作品来源。只讨论可见的焦散线索，不宣称物理模拟正确。

- **E · 透明层**：Clearwater能同时读到近表面的波纹和底下的圆石；杯子上段近透明，下段棱面折成明暗色块。不能把玻璃简单当作降低不透明度。
- **A · 光斑分工**：水面白日光在上中部形成一条短亮链，底部浅绿光网更细；玻璃地面彩斑偏左，杯口白高光仍在物体上，二者位置分离。
- **B · 色散预算**：玻璃图大面是低饱和冷蓝约`#344B76`，彩色集中杯腹和左下约25%的地面；背景不再铺第二层彩虹渐变。
- **C · 安静背景**：杯子12s帧主体高约75%，21s帧相近，但外围仍有约50–60%低细节背景。这让细碎折射能被看清。
- **F · 水底可读性**：Clearwater较暗石粒被亮网覆盖，仍保留大致边界；最强白高光没有铺满水底，浅水才有“深度”。

清流辅图把同一判断放回有岸线的场景：中央浅青水道约占裁切画宽1/3，白岩、暗叶与水底石块分别承担干岸、遮挡和接收面。裁切丢失上方林冠与下方近景，不能用它评价完整构图。

## 做法

先设计主光大小和接收面，再调透明物的形体；接收面若全黑或过亮，焦散都没有阅读空间。光栅场景可用近似投射，但在卡中标明它是视觉近似。

- **实现边界**：玻璃视频未提供本轮可核的渲染参数，不编IOR或焦散采样数；[Clearwater作品](https://aureliengmz.github.io/clearwater/)是观察入口，不等于已审过其shader。
- **迁移试验值**：先将彩色强焦散限制在画面10–25%，白高光小于5%；用正常曝光让接收面的石纹或平面边界仍可辨认。比例为设计预算。

### 实现索引

2026-10-28 源码阅读补索引；不新增截图、不改上方视觉判断。上方“不能由截图推出/尚未审 shader”等界限指原视觉阶段，本节另列本批核过的源码。`Repos/` 相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。本批未运行这些源码测量参数，标为“源码”的值不得当作实测。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| Clearwater | `Repos/clearwater/index.html:283-347,508-522` | WebGL2 水面梯度折射光线到水底，导数面积计算聚光，RGB 三通道累积到浮点 caustic RT，再采样调制河床 Esun；确为接收面受光，不是水面闪点。移植需连同水面场、RT/FBO、sun/深度和接收材质接口适配 Three.js，不能直接粘贴主循环。Citadel lab/src/scenes/Beach/shore.js:113-118,131-139 仅 BLUE 沙底视觉近似，可先复用，非物理折射。 | caustic mesh G / target C=256 / 1024（源码）；RGB water IOR=[1.3315,1.3335,1.3365]，不是玻璃 IOR（源码）；intensity clamp=40.0（源码）；white highlight area=小于画面 5%（建议迁移值） | MIT；版权 2026 Lumaris，移植保留声明 / integrate | `lab/src/scenes/Beach/shore.js` |
| Glass goblets · 12s | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/clearwater/index.html:297-339,508-522：可借折射→聚光纹理→接收面的分层，但 Clearwater 是水，不是棱面杯色散。Platform/cafe-1 器物可先复用 Citadel lab/src/scenes/Bar/index.js:143-165,177-185 的离光源侧静态月牙 decal；它不随折射求解、没有真实色散，杯体透射和投影方向需另接并验证，不编玻璃 IOR；不是原作实现，画面一致性待验证。 | strong colored caustic area=画面 10–25%（建议迁移值）；citadel static decal opacity / emissive=0.6 / 0.4（源码） | 原作待验证；邻接源 MIT，原作资产不可据此复制 / reference | `lab/src/scenes/Bar/index.js` |
| Glass goblets · 21s | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/clearwater/index.html:297-339,508-522：可借折射→聚光纹理→接收面的分层，但 Clearwater 是水，不是棱面杯色散。Platform/cafe-1 器物可先复用 Citadel lab/src/scenes/Bar/index.js:143-165,177-185 的离光源侧静态月牙 decal；它不随折射求解、没有真实色散，杯体透射和投影方向需另接并验证，不编玻璃 IOR；不是原作实现，画面一致性待验证。 | strong colored caustic area=画面 10–25%（建议迁移值）；citadel static decal opacity / emissive=0.6 / 0.4（源码） | 原作待验证；邻接源 MIT，原作资产不可据此复制 / reference | `lab/src/scenes/Bar/index.js` |
| 清流 · 浅滩河床 | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/clearwater/index.html:297-339,508-522：借水面法线折射到可见河床后调制入射光；Seiryu 原作实现未知。Citadel lab/src/scenes/Beach/shore.js:113-118,131-139 可先复用局限在近岸浅层的程序光网，当前只在 BLUE 有增益；不是物理焦散，不直接套到 Platform 玻璃杯；不是原作实现，画面一致性待验证。 | citadel sand pattern scales / speeds=2.2,3.7 / 0.16,-0.12（源码）；strong caustic area=画面 10–25%（建议迁移值） | 原作待验证；邻接源 MIT，原作资产不可据此复制 / reference | `lab/src/scenes/Beach/shore.js` |

第八张由现有卡明确的 Platform 展示道具用途选入，不是匹配表直接命中。优先 platform-1 / cafe-1 的小面积器物试验；水焦散与杯焦散分路线，性能、光向同步及最终画面均待验证。

源码快照（本批读取，不是新增截图来源）：
- `clearwater@4bc826134321043a25df3c2b6fed16fb7b9241e8`

已检索 `citadel/src`（含 `src/world/worlds/`）与 `lab/src`；本批未发现 `src/world/worlds/cardfx/` 目录或本卡同名预制模块。以上入口只表示可复用部分；首次完整落地才由执行者沉淀 cardfx，不在此虚构文件。title / atlas locked，任何队列用途均不解除锁定。

## 迁移到博客

Beach浅水只在近岸可看见底部的区域用细光网；Shrine器物与Platform展台可用小面积棱面材质。不要把透明器物的做法迁移成玻璃拟态UI。

搭配低细节背景、侧光和冷暖局部焦点；与全场高bloom、密集雨粒和大面积彩灯冲突。先关闭其余发光元素，确定透明物是否仍有体积。

## 反例

Cosmos图里远近水纹同时发亮，亮环、太阳和水面没有明确高光级别。材质特效的密度超过空间信息后，观众很难判断哪些亮点来自表面、哪些来自背景。


[![Shader & Cosmos · 吸积盘](shots/04.png)](shots/04.png)
[Shader & Cosmos · 吸积盘](https://github.com/holooooo/webgl-seascape-video) · 只有水面闪点，未展示可辨水底受光面，不能当作焦散落地正例。 仅评价本次画面。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
