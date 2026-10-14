# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Documentation Reference |
| Current Version | v0.1.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# 功能大纲与架构映射拆分修改报告

Version: 功能大纲v2.1.1 → v2.1.2；独立映射v0.1.0；登记表v1.5.2 → v1.6.0。

Change Type: 大纲Patch（内容归档位置调整，无功能或软件架构变化）；登记表Minor（新增独立入口）。

## 修改前影响分析

- Section: 大纲0.3、X001结构归属、版本与登记。
- Before: 0.3在大纲内；X001指向该节。
- After: 0.3完整提取到独立稳定路径，X001改为源图根节点/功能总览归属；原六类一级、全部二级、79条功能行不变。
- Affected: 稳定大纲、同源交付、独立映射、登记与治理清单。
- 不修改PRD、UE、硬件、云端或其他功能文档；本次不扩展其他附录拆分范围。
- 基线：[manifest](backups/teamo-outline-separate-mapping-20261013/manifest.json)。
- 旧口径—新证据—修改：原大纲容纳架构映射；用户明确它应独立；拆分文档而不重新设计架构。

Next Action: 后续在功能大纲维护功能、在独立映射维护对应关系。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.1.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 拆分既有架构映射与功能大纲，保留功能编号与职责内容 |

# Change Impact

- Section: 大纲原0.3软件功能架构映射。
- Before: 七模块映射混在功能大纲。
- After: 独立存放并引用稳定功能大纲；大纲仅保留功能分类与说明。
- Risk: Low；既有映射提取，未设计新架构或改变功能范围。

# Decision Log

Date: 2026-10-13

Decision: 按用户明确要求将架构映射作为独立文档；不扩展实现、接口或算法。

Reason: 功能大纲与架构映射承担不同文档用途。

Impact: 文档职责分离，79条功能与原优先级保持不变。

Owner: 文档审核责任待确认。

Status: 用户文档拆分要求已执行；既有映射保持Review，非已批准架构。
