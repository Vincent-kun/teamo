# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Device Requirements Navigation |
| Current Version | v1.0.4 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇；不等同审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Teamo Device Requirements

## Document Hierarchy

Requirement Baseline → Function Specification → UE IA → PRD → FR → TR。

这是细化和追踪路线，不是自动覆盖的权威顺序。产品边界与竞品规范按根AGENTS.md §4；既有整体PRD V3.0仍保留权威。设备端PRD为Draft，三/七动作、候选范围及工程细则仍待确认。

## Authority Rules

| 对象 | 维护依据 |
|---|---|
| Function ID / Priority / OQ | Function Specification；本轮不重新编号或裁决 |
| PAGE ID / User Flow / UE-OQ | UE IA |
| State Reference / Exception Reference | UE Engineering Reference；不是已批准实现枚举 |
| 需求追踪号 | Requirement Baseline；已有FR编号保留，不推断正式FR已冻结 |
| Test Evidence | 后续TR与实际测试记录；当前不得将TC-TBD或自检当作实机通过 |

## Current Entry

[本目录登记表](DOCUMENT_REGISTER.md)列出现行稿、历史文件和兼容路径；[全局登记表](../../governance/DOCUMENT_REGISTER.md)保持全项目治理入口。

## Naming and Maintenance

本次采用用户批准的Teamo_Device_<Document_Type>_vX.Y.Z命名；PRD特例保留_Draft。版本由Document Control管理，状态不代表批准。未来修改在登记入口内进行，不持续复制多份正文；如文件名需随版本迁移，须重新核对引用并保留兼容入口。历史快照不修改。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 新增设备端文档治理迁移记录与导航 |

| v1.0.1 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 登记Teamo设备端PRD v1.0.0 Draft/Review为当前评审入口，保留v0.6.0历史草稿和固定四份输入 |


| v1.0.2 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 同步PRD控制版本v1.1.0与独立RTM入口，保持旧PRD路径；无需求变更 |

| v1.0.3 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 同步MVP演示三动作确认后的控制版本和导航；既有路径保留 |

| v1.0.4 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 登记独立Feature Specification v0.6.0、RTM及治理日志，保留旧入口快照 |
# Change Impact

- Section: 文件名称、引用路径、治理记录及导航。
- Before: 职责名称不一致，版本、日期及状态混入路径。
- After: 使用批准映射，保留历史及旧路径兼容入口；需求和编号不变。
- Risk: Low；完整原文件及SHA256见治理备份。
- Change Type: Document Governance Migration；不构成需求升级。

# Decision Log

本次无产品/架构决策。用户已批准命名迁移；文档仍为Draft/Review，不代表需求批准。

## PRD v1.0 Draft Review Entry

[Teamo_Device_PRD_v1.0.0_Draft.md](Teamo_Device_PRD_v1.0.0_Draft.md)为当前设备端PRD评审入口；Status Review，未批准或冻结。v0.6.0 Draft原路径保留历史草稿，不作为本次需求来源。四份输入版本不变，审批权威顺序不变。

### Change Impact — PRD Review Entry

- Section: 当前PRD导航/登记。
- Before: 指向v0.6.0 Draft。
- After: 指向v1.0.0 Review，旧草稿保留；只更新文档入口，不更改产品范围。
- Risk: Low；[变更单](../../governance/CHANGE-DEVICE-PRD-REVIEW-20261012.md)。

## PRD正文与RTM入口

[PRD正文](Teamo_Device_PRD_v1.0.0_Draft.md)控制版本v1.1.0；[RTM](Teamo_Device_Requirement_Traceability_Matrix.md)控制版本v1.0.0；正文按业务阅读，完整内部编号与逐项来源在RTM。

### Change Impact — Readability

当前入口同步控制版本及RTM；不改变范围、优先级与历史。详见[变更单](../../governance/CHANGE-PRD-READABILITY-20261012.md)。

## MVP演示动作已确认

仅演示开合跳、深蹲起、高抬腿；整体产品追踪与其他未决项保留。各文件控制表为最新版本来源。

### Change Impact / Decision Log

同步用户已确认演示范围与文档版本，无编号/优先级调整；详见[变更单](../../governance/CHANGE-MVP-THREE-ACTIONS-CONFIRMED-20261012.md)。

## 文档类型隔离入口

- [功能规格](Teamo_Device_Feature_Specification_v0.6.0.md)：PM/设计/研发阅读评审。
- [RTM](Teamo_Device_Requirement_Traceability_Matrix.md)：内部追踪，Excel为同源导出。
- [治理日志](../../governance/Teamo_Device_Governance_Log.md)：完整问题、变更、影响与决策。

### Change Impact — 文档类型隔离

入口重组，无需求/编号/优先级变化；旧路径保留。
