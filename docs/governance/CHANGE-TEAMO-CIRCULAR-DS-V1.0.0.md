# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Change Impact |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 魏子奇 |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# CHANGE：新增《Teamo Circular Display Design System》v1.0.0

> 变更类型：Minor（新增独立 UE 设计输入文档，不修改任何既有文档正文）。
> 执行流程依据：[Markdown 文档版本管理规范](DOCUMENT_VERSION_POLICY.md)。

## 变更内容

- Section: `docs/product/design/` 新增 `Teamo_Circular_Display_Design_System.md`（v1.0.0，Draft）。
- Before: 设备端圆形屏幕缺少统一的屏幕几何、安全区与圆形网格规范；UE IA v0.3.1 明确「本文不负责 UI 视觉、硬件尺寸」，该层为空。
- After: 新增圆形屏设计系统，定义屏幕几何变量（含 1.8″ / 360×360 参考基线，待硬件确认）、三层安全显示区（Outer Unsafe / Content Safe / Core Interaction）、双网格（同心 + 12px 正交基线）、固定槽位（S1–S4）、两档视距字号基线；仅提供布局约束与模板槽位，不设计具体页面、不新增功能需求。

## 旧口径 — 新证据 — 建议修改

- 旧口径：无（此前无圆形屏设计规范文档；`docs/hardware/display-protocol-filter-20261009/UI设计说明.md` 为屏驱侧说明，不含安全区/网格）。
- 新证据：用户 2026-10-13 指令要求建立 Circular Display Design System；输入依据为 Device PRD v1.1（Teamo_Device_PRD_v1.0.md）、Device Software Functional Specification v2.3.0、Hardware-Software Gap Analysis；屏幕参考基线沿用 2026-09-24 掌心路线屏幕选型研究（1.8″ 圆形 IPS 360×360，待硬件确认）。
- 建议修改：仅新增文档，不改既有文档；后续 PAGE 级 UI Flow / 视觉稿应引用本文件作为几何约束。

## Affected Documents

| 文档 | 影响 |
|---|---|
| Teamo_Circular_Display_Design_System.md（新增） | 本变更主体 |
| Teamo_Device_UE_IA_v0.3.1.md | 无正文修改；其 PAGE-00–09 后续 UI 化时应引用本设计系统 |
| Teamo_Device_PRD_v1.0.md | 无正文修改；4.10 实时反馈、4.24 摄像头状态的「用户可感知」呈现需符合本系统槽位规则 |
| managed-documents.json / DOCUMENT_REGISTER.md | 登记新增条目 |

## Risk

Low。新增设计输入文档，Status=Draft，不改变功能范围、不冻结任何需求、不修改权威顺序。分区比例与字号基线为本稿提案（Pending Review），未经人工评审不得作为工程冻结依据。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-13 | WorkBuddy（AI，执行用户指令） | Review | 新增变更单：登记圆形屏设计系统 v1.0.0 新增条目、输入依据、影响范围与风险；未修改任何既有文档正文 |

# Decision Log

本次无产品方向、功能取舍或系统架构决策。屏幕几何参数（分区比例、网格、字号基线）为设计提案，决策记录置于设计系统文档自身 Decision Log（D-CDS-01，Status: Proposed），待评审。
