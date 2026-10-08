# docs/ — 规范树（现行优先）交接文档

> 本目录是 **AI 运动伙伴** 项目的**规范化组织版本**，由早期扁平资料于 2026-09 起迁移整理而成。
> **新接手 agent：产品/研究类资料一律先在本目录找，同名文件以本目录为最新。** 旧树 `AI运动伙伴/` 的扁平稿仅供追溯。

---

## 目录结构

| 子目录 | 内容 | 关键文件 |
|---|---|---|
| `product/planning/` | 产品规划与版本演进 | `01_儿童AI运动陪伴机器人_功能大纲_正式版_V1.0.html`、`01_儿童AI运动陪伴机器人_商业画布_V1.0.html`、`儿童AI运动陪伴机器人_MVP与版本演进说明_V1.0.html` |
| `product/requirements/` | 当前产品需求 | `03_儿童AI运动陪伴机器人_PRD_V3.0.html` |
| `product/design/` | 交互设计与演示 | `儿童AI运动陪伴机器人_完整产品UE_Demo_V7.4.html` |
| `hardware/` | MVP 硬件技术需求 | `儿童AI运动陪伴机器人_MVP硬件技术需求说明书_V2.0.html` + `assets/MVP胶囊形态硬件示意图_V2.0.png` |
| `research/competitive/` | 竞品专项分析报告 | `儿童AI运动产品_天天跳绳与满分运动竞品分析报告.html`、`bodypark/`、`星角萌萌/` |
| `research/bodypark-teardown/` | BodyPark ATOM 拆解/复刻/器件资料 | 见下方与 `bodypark-teardown/README.md` |
| `archive/product-requirements/` | 历史版本（仅供追溯） | `儿童AI运动陪伴机器人_MVP_PRD_V1.2_技术对接版.html` |

---

## 竞品研究入口

- **天天跳绳 × 满分运动**：`research/competitive/儿童AI运动产品_天天跳绳与满分运动竞品分析报告.html`
- **BodyPark ATOM**：`research/competitive/bodypark/BodyPark_ATOM_专项竞品分析报告_V1.0.html`（配图在 `bodypark/bodypark图片/`）
- **星角萌萌**：`research/competitive/星角萌萌/星角萌萌_AI陪伴机器人_专项竞品分析报告_V1.1_精简版.html`（产品图在 `星角萌萌/images/`，修改须知 `README_给修改者.txt`）

## BodyPark 拆解与技术研究

`research/bodypark-teardown/` 已从旧树 `AI运动伙伴/参考与拆解/BodyPark拆解/` 迁入（见 `_move_log.txt`）。包含：
- `reports/`：产品技术介绍、BOM 成本与可复刻性评估（pdf + docx + svg 框图）
- `replication/`：复刻工程技术方案、复刻硬件架构、前期准备方案
- `teardown-images/`：~21 张实机拆解照片
- `datasheets/original/` 与 `datasheets/ai-translated/`：主控/存储/无线/电源/电池等器件资料（AI 译文仅供阅读辅助，关键参数以 original 为准）
- `路线.md`：从拆解升级为"可画板"的系统架构与原理图设计规范

---

## 使用约定

1. 当前有效版本放对应业务目录；旧版本移入 `archive/`。
2. 文件名保留产品名 + 文档类型 + 版本号。
3. 含竞品图片/拆解照片/供应商资料的，对外发布前必须复核授权与保密要求（见根 `AGENTS.md` §4、§6）。
4. HTML 文档 GitHub 默认显示源码，本地用浏览器打开；在线演示另配 Pages/站点。
