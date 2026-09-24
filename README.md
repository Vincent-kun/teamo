# Teamo｜儿童 AI 运动陪伴机器人

本仓库用于管理儿童 AI 运动陪伴机器人项目的产品需求、交互设计、硬件需求、项目计划和竞品研究资料。

> 注意：仓库中的竞品图片、拆解照片和器件资料仅用于项目研究与内部评审。对外公开前，应按公司要求检查商业保密范围、第三方图片版权和资料授权情况。

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

## 查看 HTML 文档

GitHub 默认显示 HTML 源码，不会直接运行交互页面。可以下载文件后用浏览器打开；如需在线演示，可另行配置 GitHub Pages。
