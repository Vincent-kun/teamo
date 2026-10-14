# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Project Documentation |
| Current Version | v0.1.1 |
| Status | Draft |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 待核实（无可靠创建日期） |
| Last Updated | 2026-10-12 |

> 文档控制版本以本表为准；原文件名和正文版本标识保留为历史业务版本。Draft/Review 为本次治理提交状态，非产品审批结论。创建日期取自原标识，待 Owner 核实。

# Teamo｜儿童 AI 运动陪伴机器人

本仓库用于管理儿童 AI 运动陪伴机器人项目的微信小程序源码、产品需求、交互设计、硬件需求、项目计划和竞品研究资料。

> 注意：仓库中的竞品图片、拆解照片和器件资料仅用于项目研究与内部评审。对外公开前，应按公司要求检查商业保密范围、第三方图片版权和资料授权情况。

## 软件代码

| 项目 | 说明 |
|---|---|
| [微信小程序 MVP V0.1](apps/wechat-mini-program/) | 家长端微信小程序源码，当前使用 Mock 数据验证任务、设备、记录、姿态和 AI 分析页面 |

使用微信开发者工具打开 `apps/wechat-mini-program/` 目录即可运行。接口切换及设备通信约定见该目录下的说明文档。

## 核心文档

### 产品规划

| 文档 | 说明 |
|---|---|
| [功能大纲 V1.0](docs/product/planning/01_儿童AI运动陪伴机器人_功能大纲_正式版_V1.0.html) | 完整产品的功能结构与模块边界 |
| [商业模式画布 V1.0](docs/product/planning/01_儿童AI运动陪伴机器人_商业画布_V1.0.html) | 产品价值、用户、渠道和商业关系 |
| [MVP 与版本演进说明 V1.0](docs/product/planning/儿童AI运动陪伴机器人_MVP与版本演进说明_V1.0.html) | MVP 范围及后续版本演进方向 |

### 产品需求与交互

| 文档 | 说明 |
|---|---|
| [完整产品 PRD V3.0](docs/product/requirements/03_儿童AI运动陪伴机器人_PRD_V3.0.html) | 完整产品需求文档 |
| [完整产品 UE Demo V7.4](docs/product/design/儿童AI运动陪伴机器人_完整产品UE_Demo_V7.4.html) | 当前完整产品交互演示版本 |
| [MVP PRD V1.2（历史技术对接版）](docs/archive/product-requirements/儿童AI运动陪伴机器人_MVP_PRD_V1.2_技术对接版.html) | 历史版本，仅供追溯，不作为当前需求基线 |

### 硬件需求

| 文档 | 说明 |
|---|---|
| [MVP 硬件技术需求说明书 V2.0](docs/hardware/儿童AI运动陪伴机器人_MVP硬件技术需求说明书_V2.0.html) | MVP 硬件选型、结构、接口、性能和样机验收要求 |

## 竞品与拆解研究

| 资料 | 说明 |
|---|---|
| [天天跳绳 × 满分运动竞品分析](docs/research/competitive/儿童AI运动产品_天天跳绳与满分运动竞品分析报告.html) | 儿童运动类 App 与产品能力对比 |
| [星角萌萌专项竞品分析 V1.1](docs/research/competitive/星角萌萌/星角萌萌_AI陪伴机器人_专项竞品分析报告_V1.1_精简版.html) | AI 陪伴机器人形态、功能和硬件观察 |
| [BodyPark ATOM 专项竞品分析 V1.0](docs/research/competitive/bodypark/BodyPark_ATOM_专项竞品分析报告_V1.0.html) | BodyPark ATOM 产品与功能分析，报告图片按独立素材文件管理 |
| [BodyPark ATOM 拆解资料索引](docs/research/bodypark-teardown/README.md) | 拆解过程、器件资料、BOM 评估和复刻方案 |

## 仓库目录

```text
apps/
└── wechat-mini-program/       微信小程序 MVP 源码
docs/
├── product/
│   ├── planning/              产品规划与版本演进
│   ├── requirements/          当前产品需求
│   └── design/                交互设计与演示
├── hardware/                  MVP 硬件需求及配套图片
├── research/
│   ├── competitive/           竞品分析报告
│   └── bodypark-teardown/     BodyPark 拆解与技术研究
└── archive/                   历史版本，仅供追溯
```

## 版本管理约定

1. 当前有效版本放在对应业务目录中，旧版本移动到 `docs/archive/`。
2. 文件名保留产品名称、文档类型和版本号，例如：`儿童AI运动陪伴机器人_MVP硬件技术需求说明书_V2.0.html`。
3. 需求变更时升级版本号，并在提交说明中写明修改范围。
4. 不提交 `.DS_Store`、临时截图、浏览器缓存和个人周报。
5. 甘特图等使用浏览器本地存储的工具，在跨设备分享前应先导出数据文件。
6. 含竞品图片、拆解照片或供应商资料的内容，对外发布前必须再次检查授权和保密要求。
7. 微信开发者工具的 `project.private.config.json`、真实密钥和本地环境文件不得提交。

## 查看 HTML 文档

GitHub 默认显示 HTML 源码，不会直接运行交互页面。可以下载文件后用浏览器打开；如需在线演示，可另行配置 GitHub Pages。

## 项目分类导航（2026-10-10）

完整分类清单见 [项目文件分类](项目文件分类.md)，双树权威顺序见 [交接说明](AGENTS.md)。原型与评审工具见 [prototype 导航](prototype/README.md)，新增 [Teamo 正面比例方案评审](prototype/industrial-design/Teamo_正面比例方案评审.html) 可直接用浏览器打开。


---

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.1.0 | 待核实 | 原作者待核实 | 待核实 | 登记导入前现存正文基线；已有版本标识，既有版本记录仍保留在正文；不推断历史修改或批准 |
| v0.1.1 | 2026-10-12 | Codex（AI，执行用户指令） | Draft | 新增 Document Control、标准 Version History、Change Impact 与 Decision Log；保留既有业务正文及历史记录 |

> 本表仅登记已验证的现存基线与本次修改。历史日期、作者和状态待核实；原有版本记录是补录证据入口，不能据文件名编造缺失版本。

# Change Impact

### Modified Sections

- Section: 文档顶部与治理附录。
- Before: 缺少统一的文档控制表和标准版本记录。
- After: 增加控制表、基线与 Patch 历史、影响分析和决策记录入口；原业务正文保留。

### Impact Scope

Affected:
- 本文及引用本文的项目文档；本次无业务要求变更。
- 逐文件版本、备份和修改报告见 docs/governance/CHANGELOG-20261012.md。

### Risk

Low。Owner、Reviewer、历史审批状态仍待确认；本次结构治理不冻结产品需求。

# Decision Log

本次未修改产品方向、功能取舍或系统架构。既有决策及待决事项保留在正文，尚未逐条验证迁入；后续涉及这些事项时按 docs/governance/DOCUMENT_VERSION_POLICY.md 记录，建议与已批准决策必须区分。
