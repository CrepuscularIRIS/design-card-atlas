# realism-effects
实读SSGI配置/入口、重投影和运动模糊。源码SSGIEffect(composer,scene,camera,options)与README示例签名不一致；preset有两个medium分支。不可把复制示例当集成完成。

## 案例档案

[来源仓库](https://github.com/0beqz/realism-effects)
分析版本：`061daeaefb7773d8a1a8e10fa95a184fbcda1fb7`

模型归属未独立认证。

## 初始源码审计边界

未跑；SSGI完整采样/合成后半未穷尽；贴图模型和AO demo未看图；r.151 peer与本站r.170不匹配。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [REN-009 · 让屏幕可见表面参与二次光色交换](../cards/REN-009.md)

邻近红灯与青屏的颜色应落在物件上；屏幕空间只能使用可见信息，无法保证屏外光源贡献。

邻近红灯与青屏的颜色应落在物件上；屏幕空间只能使用可见信息，无法保证屏外光源贡献。

**Movie：reference** · 用作GI参考图和镜头边界检查
**前端：defer** · 先精修实际灯光；不默认接老库

失败条件：- 屏外信息缺失导致反射消失
- 过厚thickness让光穿墙
- 源码preset两个medium，README构造签名陈旧
- 项目three0.170不在^0.151.3 peer范围

### [REN-010 · 把历史颜色限制在当前邻域和几何一致性内](../cards/REN-010.md)

能防止历史高亮尾迹拖过新露出的暗墙，但邻域夹紧也可能吞细招牌。

能防止历史高亮尾迹拖过新露出的暗墙，但邻域夹紧也可能吞细招牌。

**Movie：adapt** · 离线预览时间稳定性值得借鉴
**前端：reference** · 若将来新增temporal effects再用；当前不新建整套缓冲

失败条件：- 位移shader未写velocity时拖影
- 细霓虹被过强裁剪
- 硬切不重置留下旧场景

### [REN-011 · 沿像素运动方向模糊并按帧时间归一](../cards/REN-011.md)

运动体保持方向性，静止UI应在后期之后合成；不是把阅读内容一起拉糊。

运动体保持方向性，静止UI应在后期之后合成；不是把阅读内容一起拉糊。

**Movie：adapt** · 列车/物体运动镜头可借
**前端：reference** · Ride已有速度特效，不重复加全局blur

失败条件：- 细杆前景会采到后景颜色
- deltaTime过小导致超长模糊
- 镜头摇动时整幅难读

## 项目效果与观察材料

![realism-effects · author_demo_screenshot](../assets/previews/lib-realism-effects-ssgi2.webp)

粉红衣黑面罩角色位于竹林园景，角色受光与背景石/水/白墙形成明暗层次。

来源：本轮已观察的历史截图 · author_demo_screenshot。README标为SSGI示例；单张图不分离SSGI与环境照明、贴图和模型贡献。角色形象和背景权利未独立核验。

![realism-effects · author_demo_screenshot](../assets/previews/lib-realism-effects-motion_blur.webp)

岩壁环境中的粉红衣角色；面罩方框和轮廓可见拖叠/模糊，背景保留石纹。

来源：本轮已观察的历史截图 · author_demo_screenshot。README标为motion blur示例；静帧可见模糊，不能证明运动过程中稳定、遮挡正确或无ghosting。

## 复用边界

- **status**：observed
- **evidence**：LICENSE.md:1-21 MIT；保留版权和许可，示例资产另查。
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
