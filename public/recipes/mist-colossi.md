# 雾水之间的巨像门

给 **Shrine 会面背景 / title 静态远景备选** 的构图配方：观众在普通船棚或门檐下，沿暗水望向两侧越框巨像。人物仍为现有2D层；配方不新增入场航线。

## 参考情绪板

| 主气氛与尺度 | 水面与空间连续性 |
|---|---|
| [![雾中巨像](../cards/fog-separates-depth/shots/01.jpg)](../cards/fog-separates-depth/shots/01.jpg) | [![江南水岸](../cards/water-continues-silhouette/shots/01.png)](../cards/water-continues-silhouette/shots/01.png) |
| 巨像图给出灰绿、近舟与亮雾；[原作](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) | 水岸图只负责水与岸物的延续；[原作](https://github.com/holooooo/webgl-seascape-video) |
| [![低机位石像](../cards/colossus-crosses-the-frame/shots/01.jpg)](../cards/colossus-crosses-the-frame/shots/01.jpg) | [![残柱框景](../cards/framed-distant-view/shots/01.jpg)](../cards/framed-distant-view/shots/01.jpg) |
| 石像图负责越框和近身视点，暖白色不整体照搬 | 残柱图负责有厚度的前框，石材细节只用于近景 |

这是四张原图组成的Markdown参考板，未合成新的作品效果图。各图出处、时间和许可见所链卡的SOURCE。

## 维度分工

以下均为 **Citadel试验起点**，不是原作已验证参数。

| 维度 | 负责卡 | 在此场景的具体决定 |
|---|---|---|
| A 光影 | [逆光露轮廓](../cards/backlight-reveals-silhouette/README.md) | 亮雾放在两像中央及外肩之后；不额外画一圈发光边。近框保留暗中间调。 |
| B 色彩 | [低彩分灰阶](../cards/low-chroma-value-steps/README.md) | 主灰绿约`#44564F`，辅浅雾约`#ACB6A9`；若要灯，仅一处低面积暖米`#E2BB79`。衣服颜色不自动套全局滤镜。 |
| C 构图 | [近框套远景](../cards/framed-distant-view/README.md) | 近框占20–30%，亮通道约1/4宽；人物脸和对话阅读区不被柱枝切过。 |
| D 尺度 | [巨像越画框](../cards/colossus-crosses-the-frame/README.md) | 保留手势/脸至少一组识别线；远大像与近小船或灯柱共同入镜。 |
| E 表面 | [镜面邻粗面](../cards/mirror-beside-roughness/README.md) | 石像哑面，水面反射软而连续；不把石像也抛光。 |
| F 大气 | [雾层分远近](../cards/fog-separates-depth/README.md)、[水面续轮廓](../cards/water-continues-silhouette/README.md) | 近棚最深、像中调、浮岩浅、远山近雾色；水中保留像脚/岸线的低频暗形。 |
| G 镜头 | [低机位入场](../cards/low-eye-entry/README.md) | 以普通站姿或舟上视高定静态相机，先避免畸变；不增加未经验证的自动飞行。 |
| H UI | [HUD细线叠层](../cards/thin-line-hud/README.md)的减量版本 | 最多边缘地点名与状态；无需雷达球、滚码与常驻锁定条。会面文字优先于装饰。 |

## 组合检查

1. **光源逻辑**：亮雾解释天空照明；若小灯发亮，灯壳、照亮的近物和水中对应亮点都应能指认。不要给巨像裂缝无缘由自发光。
2. **色彩逻辑**：灰绿主色、浅雾辅色、单一暖米点缀；不再加入青紫霓虹背景。角色自有色作为叙事物而非第二套环境灯。
3. **明暗结构**：暗近框约25%、中暗像/水约45%、雾与天约30%，强高光只占后者中的很小部分；百分比为构图预算。
4. **尺度**：近景船棚/灯柱，中景巨像，远景浮岩/山。若删掉所有普通物体，必须检查巨像是否退成两件摆件。
5. **冲突消解**：雾只削弱远层，不抬近框黑位；水反射保持低频，不叠密集焦散；HUD避开中央开口；人物层不被3D雾整体覆盖。

## 先验证什么

先灰模锁定主相机，检查识别轮廓和人物落点；再加入一层空气与一块水面。只做这两步就应能看出气氛，最后才补石刻、草与少量光点。400px预览若只剩一团灰，回到明暗与距离，不继续加粒子。
