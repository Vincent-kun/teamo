# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Function Scope Alignment |
| Current Version | v0.1.0 |
| Status | Draft |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# 阶段定位与四份产物变更单

## 修改前影响分析

- Section: 本阶段文档入口。
- Before: 现有大纲、云端对齐稿与派生规格并存，容易提前进入设计。
- After: 新建多端范围定义、云端设备映射、设备修订清单、运动标准调研四个稳定入口。
- 登记表 v1.4.1 → v1.5.0（Minor：新增四个文档入口）；新增正文 v0.1.0。
- 可恢复基线：backups/function-scope-alignment-20261013/；SHA256见同目录sha256.json。
- 既有本地修改已核对；不提交、不覆盖他人修改，不修改原功能大纲/PRD/规格。

## 旧口径—新证据—建议修改

| 旧口径 | 新证据 | 建议修改 |
|---|---|---|
| 范围整理后提前展开技术/规则设计 | 用户明确当前是Function Scope Alignment | 本阶段产物只写功能归属与缺漏 |
| 任务同步、隐私保护可作为新增示例 | 原大纲与云端对齐稿已有对应功能 | 清单记保留/归并，避免重复新增 |
| 成长建议包含接收家长端建议 | 用户要求设备仅接收外部计划 | 清单提出收窄建议，原文不静默改写 |

## 后续同步

由负责人审阅修订清单后，在原设备大纲稳定路径内修订。PRD、UE、硬件要求同步仍待后续阶段。运动标准只作为业务证据资料。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.1.0 | 2026-10-13 | Codex（AI，执行用户指令） | Draft | 新增四份功能范围阶段产物的影响分析、基线与登记计划 |

# Change Impact

- Section: 本文全部正文。
- Before: 无本阶段独立入口。
- After: 新增四份功能范围阶段产物的影响分析、基线与登记计划。
- Impact Scope: 功能范围评审；既有PRD、UE、规格和大纲保留。
- Risk: Low；未决功能不据本文自动批准。
- 独立变更单：[阶段对齐变更单](CHANGE-TEAMO-FUNCTION-SCOPE-ALIGNMENT.md)。

# Decision Log

Date: 2026-10-13

Decision: 按用户指令限定为功能范围对齐；运动标准独立收集。功能取舍以正文标注为准，未决项保持待评审。

Reason: 当前仅回答有哪些功能、属于哪个端、是否重复或遗漏。

Owner: 功能评审责任待确认；阶段定位来源为用户本次指令。

Status: 阶段定位为用户明确要求；新文档内容为Draft，未批准架构或评分规则。
