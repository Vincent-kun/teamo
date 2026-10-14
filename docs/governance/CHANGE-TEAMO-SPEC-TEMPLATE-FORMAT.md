# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Change Request |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 魏子奇 |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# Change Impact

本单先于修改正文建立。规格控制版本v2.1.0→v2.1.1（Patch：表达与格式调整），沿用现有文件路径；登记表v1.3.0→v1.3.1。

| Section | Before | After |
|---|---|---|
| 文首 | 用途长段落，无优先级速查 | 参照模板增加用途/版本/日期/状态/核心变更摘要及优先级速查 |
| 功能表 | 每项重复“设备负责”，优先级无强调 | 保持五列和80条功能；删除重复前缀，优先级加粗；一级模块加定位短注 |
| 优先级统计 | 无独立核对表 | 附录增加精确统计，仅供核对，不替代MVP职责判断 |
| 模板来源 | REF-06未提供、未定位 | 已读取用户指定《功能大纲v4.0》，登记实际路径、只借鉴表达格式 |
| 治理 | 规格v2.1.0，来源与历史齐备 | 规格v2.1.1，追加历史和影响；源大纲、范围及状态不变 |

Affected Documents：规格稿、登记表、managed-documents.json、本变更单。既有功能ID/名称/优先级/状态/分组、MVP、AI、异常、成长、追踪和未决事项不变。

Risk: Low。模板仅用于结构和表达，不复制网关、计费、分润等业务，不迁移模板月份、功能优先级、UI或实现要求。备份与SHA256见[manifest](backups/teamo-spec-template-format/manifest.json)；模板证据备份仅为输入存证，不作为新产品规范。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 新增模板参考格式修订影响，明确字段、范围不变及完整基线 |

# Decision Log

本次无产品方向、功能取舍或实现架构决策。用户授权参考提供的模板；保留原功能模块及五列规格结构，吸收摘要、优先级速查、定位短注和统计格式。不将模板“一级菜单”变为Teamo页面结构，也不将其排期与业务规则迁入。
