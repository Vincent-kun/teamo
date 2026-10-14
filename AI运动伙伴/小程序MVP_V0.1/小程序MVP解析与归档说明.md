# 儿童 AI 运动陪伴机器人 · 微信小程序 MVP V0.1 — 解析与归档说明

> 归档日期：2026-10-08
> 归档人：Claw（WorkBuddy）
> 原始来源：`D:/OneDrive/Documents/WXWork/1688855634881425/Cache/File/2026-10/儿童AI运动陪伴机器人_微信小程序_MVP_V0.1 (2).zip`
> 归档位置：`D:/work/sportmate/AI运动伙伴/小程序MVP_V0.1/`（已完整解包，未改动任何源码）

---

## 1. 这是什么

家长端微信小程序 MVP 工程（代号 **Teamo**），对应《儿童AI运动陪伴机器人 完整产品 UE Demo V7.3》。可直接导入微信开发者工具运行。

- **当前形态**：纯前端 + Mock 数据，不依赖真实服务端。
- **AppID**：`wxb6da3fa84f9053cb`（project.config.json，已是正式号，无需测试号）。
- **工程名**：`teamo-miniapp-mvp`
- **代码规模**：55 文件 / 1491 行（14 js、15 json、11 wxml、12 wxss、3 md）。

---

## 2. 目录结构

```
小程序MVP_V0.1/
├─ project.config.json          工程配置（AppID、miniprogramRoot）
├─ project.private.config.json   私有配置
├─ README.md                     运行说明 + 视觉方向
├─ 小程序产品与UI整改说明_V0.8.md  整改依据与结论
├─ 接口对接说明.md               小程序/服务端/设备通信方案
├─ _清单_manifest.txt            自动生成的文件清单（本归档补充）
└─ miniprogram/
   ├─ app.js / app.json / app.wxss   全局状态 + 路由 + 样式
   ├─ sitemap.json
   ├─ data/mock.js                  全局模拟数据 + 动作库定义
   ├─ services/api.js               接口层（USE_MOCK 开关 / HTTPS / 设备指令 / AI）
   └─ pages/                       11 个页面（见下）
```

---

## 3. 页面清单（11 个，其中 5 个为 tabBar 主入口）

| 路由 | 名称 | 角色 | 关键能力 |
|---|---|---|---|
| `pages/home/index` | 首页 | tabBar | 设备状态、今日运动、快捷动作、任务、AI 入口、最近记录 |
| `pages/tasks/index` | 任务 | tabBar | 单项/AI 计划任务，周期·时间·目标设备，设备回执、取消、离线拦截 |
| `pages/ai/index` | AI | tabBar | 7 天计划生成（Mock）、常见问题、文本提问（演示） |
| `pages/growth/index` | 成长 | tabBar | 周运动数据、亮点、最近分析、全部记录入口、姿态提醒 |
| `pages/mine/index` | 我的 | tabBar | 家长信息、孩子资料编辑、设备、消息、隐私、帮助 |
| `pages/device/index` | 设备 | 子页 | 模拟在线、当前任务、中文状态映射、开始/暂停/继续/结束、能力开关、动态 |
| `pages/analysis/index` | 运动分析 | 子页 | 单次运动分析（AI 建议首位，非医疗） |
| `pages/library/index` | 动作库 | 子页 | 七类动作 + 状态标签（MVP已支持/算法评审中/后续适配） |
| `pages/records/index` | 运动记录 | 子页 | 按次完成状态、来源、设备；详情含完成率/有效动作/节奏/姿态 |
| `pages/posture/index` | 姿态提醒 | 子页 | 坐姿/低头/距离提醒，明确非医疗边界 |
| `pages/profile/index` | 孩子资料 | 子页 | 编辑儿童资料 |

**tabBar 主线**（按 2026-09-24 会议收紧）：家长创建运动邀请 → 设备执行运动 → 学伴积分养成。

---

## 4. 动作库（data/mock.js → actions）

| 动作 | 状态（stage） | 可否发送 |
|---|---|---|
| 开合跳 jumping_jack | MVP已支持 | ✅ |
| 深蹲起 squat | MVP已支持 | ✅ |
| 高抬腿 high_knee | 算法评审中 | ❌ |
| 双脚跳绳 jump_rope | 后续适配 | ❌ |
| 俯卧撑 push_up | 后续适配 | ❌ |
| 仰卧起坐 sit_up | 后续适配 | ❌ |
| 平板支撑 plank | 后续适配 | ❌ |

**MVP 仅开放开合跳、深蹲起两个动作**，其余明确标注算法评审/后续适配，避免硬件与算法误判为全量 MVP。

---

## 5. 接口层（services/api.js）

- `USE_MOCK = true`：默认走 `delay()` 模拟返回，页面无需重做即可切真实后端。
- 真实切换：将 `USE_MOCK` 改为 `false`，填 `API_BASE_URL`。
- 设备指令 `sendDeviceCommand(deviceId, type, payload)` → `POST /devices/{deviceId}/commands`。
- AI 计划 `generatePlan(input)` → `POST /ai/plans`，内置 7 天模板（开合跳/深蹲起/高抬腿等）。
- HTTP 请求带 `Authorization: Bearer ${token}`。

**通信链路**（接口对接说明）：微信小程序 `-- HTTPS/WebSocket -->` 业务服务端 `-- MQTT -->` 设备。
- HTTPS：登录、绑定、任务、计划、记录、AI。
- WebSocket：实时状态/进度/异常。
- MQTT 主题：`devices/{deviceId}/commands`、`/status`、`/events`、`/results`。
- 设备状态机：`offline / idle / ready / running / paused / completed / error`。

---

## 6. 视觉方向

- 品牌主张：**一起动，更靠近**。
- V0.9 亚克力玻璃升级：环境光背景 → 半透明白内容卡（细描边+顶部高光+柔和投影+轻模糊） → 实色操作按钮三层材质。
- 配色：荧光绿（Teamo 主操作色）、深青（设备状态/分析重点）、橙（隐私滑盖）、粉/紫/青/桃仅作低饱和功能光晕。
- 隐私表达：突出物理遮挡与「无实时画面」边界。

---

## 7. MVP 边界（已明确不做的）

- 不加入学校端任务。
- AI 计划/问答当前为模拟数据，接真实服务后才有个性化结果。
- 暂不加入饮食拍照分析、医疗判断、多人家庭权限、正式支付。

---

## 8. 待研发确认（来自整改说明 + 接口说明）

1. 正式登录、家庭空间、设备绑定与权限体系。
2. 服务端命令确认、状态事件、断线重连、任务去重。
3. 开合跳/深蹲起算法验收标准；高抬腿是否进 MVP。
4. 原始视频/结构化姿态事件/儿童资料 的保存与删除规则（儿童隐私底线）。
5. AI 分析与计划生成的正式服务、审核策略、失败降级。
6. 设备：MQTT vs WebSocket、首联绑定、断网缓存条数、上报频率与去重。

---

## 9. 运行方法

1. 微信开发者工具 → 导入项目 → 选本目录。
2. AppID 已填正式号；如需测试号在 `project.config.json` 替换。
3. 真实接口就绪后，改 `miniprogram/services/api.js` 的 `USE_MOCK=false` 并填域名。

---

## 10. 与项目主线的关系

本小程序是 **AI 运动伙伴（Teamo）** 的家长端 MVP 原型，与 `AGENTS.md` 所述产品定义/PRD V3.0/MVP PRD V1.2 对齐，并依据 2026-09-24 会议收紧为三条主线。它把《UE Demo V7.3》的家长侧交互落成可运行代码，作为硬件立项前的技术对齐与交互演示基线。本归档仅解包存放，源码未改动；后续若要演进，应在新分支/新目录进行，避免污染本 MVP 基线。

## 11. 关联文档

- **母本 / 设计源**：`docs/product/design/儿童AI运动陪伴机器人_完整产品UE_Demo_V7.3.html`（本日新归档，小程序 MVP 即「整理自」此件）。
- **最新设计源**：`docs/product/design/儿童AI运动陪伴机器人_完整产品UE_Demo_V7.4.html`（项目既有，V7.3 的边界措辞精炼版，结构等价）。
- **三者对照**：`UE_Demo与小程序MVP对照说明.md`（同目录）—— 解析 V7.3 完整产品原型，并说明小程序 MVP 相对它的收敛、新增与缺口。
- **交互预览**：`预览_小程序MVP.html`（同目录，浏览器打开，11 页面可跳转）。
