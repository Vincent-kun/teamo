# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Document Separation Change |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Change Impact

- Before: 功能大纲包含功能正文、RTM映射、OQ展开、变更表、影响和决策记录。
- After: 功能规格v0.6.0只负责产品功能/业务评审；既有RTM维护映射；独立治理日志维护原问题、变更和决策；Excel为RTM的可筛选导出。
- Change Type: Minor（文档职责/结构重组）；47核心、20候选、2停用、原优先级与编号不变。
- Compatibility: 旧源文件保留完整快照和替代入口；旧HTML保留快照并转向当前预览。
- Risk: Medium；细节迁出后须核对完整保留，不以范围状态替代交付批准。
- Baseline: backups/feature-document-separation-20261012/baseline.zip及sha256.json。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 记录功能正文、RTM与治理日志拆分的影响和恢复基线 |

# Decision Log

无产品/架构决策；按用户Document Separation Rule执行职责隔离，不批准候选范围或修改动作规则。
