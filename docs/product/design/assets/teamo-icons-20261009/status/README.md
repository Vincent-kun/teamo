# Teamo 状态图标库 · status/

> 入库：2026-10-13 ｜ 来源：用户提供的状态图标参考图（黑底图标_sheet 抠图）
> 预览：`_preview_status.html`（深底 = 设备屏 #0E1210 实际效果）

## 彩色 PNG（源图直接抠图，含轻微彩色溢边，作屏内彩色元素用）

| 文件 | 内容 | 对应 PRD 模块 / 用途 |
|---|---|---|
| st-trophy.png | 奖杯（橙） | 4.14 运动星 / 排行榜第一（4.x rank） |
| st-star.png | 星星（黄） | 4.14 运动星奖励主图标 |
| st-medal.png | 勋章绶带（绿） | 4.14 成就 / 连续打卡 |
| st-check-circle.png | 圆形对勾（绿） | 4.13 总结页「已完成」徽标 |
| st-chip-ai.png | AI 芯片（绿） | 4.6 AI 识别能力 · 就绪 |
| st-chip-ai-active.png | AI 芯片+点阵（绿） | 4.6 AI 识别中（可作动效帧） |
| st-chip-ai-error.png | AI 芯片+!（红） | 4.6 / 4.27.4 AI 识别异常 |
| st-dots-ring.png | 圆点环（绿） | 加载 / 同步中（4.17 syncing 占位） |
| st-battery.png | 电池（绿） | 4.21 电量能力状态 |

## 白线 SVG（手绘重制；源图白剪影噪点过重不达标，按 Rev4 惯例改 SVG）

统一规格：viewBox 96×96、stroke 6.5、圆头圆角，与屏内既有手绘 SVG 同语言。

| 文件 | 内容 | 用途 |
|---|---|---|
| st-camera.svg | 摄像头 | 4.24 摄像头状态（Available/Running） |
| st-camera-off.svg | 摄像头+斜杠 | 4.24 / 4.20 隐私关闭 |
| st-camera-error.svg | 摄像头+红!徽标 | 4.24 摄像头异常 |
| st-wifi-on.svg | WiFi 满格（白） | 4.23 网络已连接 |
| st-wifi-off.svg | WiFi 弱+斜杠（灰 #B9C2BB） | 4.23 离线态 |
| st-signal.svg | 信号柱×4 | 4.22 信号强度 |
| st-home.svg | 主页 | 4.2 首页导航 |
| st-back.svg | 左箭头 | 屏内返回 |
| st-play / st-pause / st-stop / st-refresh.svg | 播放/暂停/停止/刷新 | 运动控制（4.9–4.10） |

## 质量备注

- 彩色 PNG 边缘有 1–2px 彩色溢边（源图为黑底压缩图），深底上不可见，浅底使用前建议再过一遍 alpha 收边。
- 源图白色剪影（摄像头/WiFi/播放控制）噪点严重，抠图两轮（连通域过滤+谷点切分）仍达不到 Rev4 质量线，最终按 Rev4 决策改手绘 SVG；失败中间产物已删除。
- 切分脚本已清理；如需复现抠图，源图：`clipboard-2026-10-13T09-40-45-056Z-2a58d702.png`。
