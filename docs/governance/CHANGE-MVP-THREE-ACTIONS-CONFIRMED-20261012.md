# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Product Scope Confirmation Change |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Change Impact

- Before: 三动作是否为演示切片尚待确认。
- Evidence: 用户2026-10-12明确“mvp就演示三个动作这是确定了的”。
- After: MVP演示仅开合跳、深蹲起、高抬腿；演示范围已确认。七动作整体产品追踪保留，未删除其余动作。动作有效规则/目标范围/计数单位仍TBD。
- Change Type: Patch（记录既有演示范围确认，不增删Function/PAGE，不改P0/P1）。
- Affected: 四份设备端输入、PRD、RTM、对应HTML及登记导航；稳定路径不改。
- Risk: Low；演示确认与整体产品范围批准分开，OQ-01/UE-OQ-03仅部分解决。
- Baseline: backups/mvp-three-actions-confirmed-20261012/baseline.zip及sha256.json。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 记录用户确认MVP演示只含三动作及跨文档同步影响 |

# Decision Log

## Decision MVP-DEMO-THREE-ACTIONS

Date: 2026-10-12
Evidence: 用户本轮明确确认。
Decision: MVP演示只含开合跳、深蹲起、高抬腿。
Status: 用户已确认演示范围；全文需求审批仍Review。
Owner: 确认来源为本工作区用户；具体交付责任人待指定。
Impact: 演示动作清单不再TBD；七动作产品追踪、有效规则、目标范围、计数单位不由此变更。
