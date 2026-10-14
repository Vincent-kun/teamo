# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Change Record |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Change Impact

### Modified Sections

- Section: 新增设备端功能大纲、XMind逐节点索引、文档登记入口。
- Before: 用户提供88节点XMind和另一产品的表格式功能大纲参考；仓库已有独立功能规格评审稿，前文对话的通用大纲未准确对应XMind。
- After: 新建稳定语义命名的源图整理文档，按开箱、运动、反馈、设置、信息同步、开关展开；保留全部88节点映射及未决事项，登记为源图整理评审稿。
- Change Type: 新建文档初始v1.0.0；登记表新增独立来源整理入口，Minor v1.0.6 → v1.1.0。

### Impact Scope

Affected:
- docs/product/requirements/Teamo_Device_Function_Outline.md（新建）
- docs/governance/DOCUMENT_REGISTER.md（追加入口）
- docs/governance/managed-documents.json（追加管理范围）

既有Feature Specification、PRD、UE IA、硬件需求不直接修改；同步与合并须经评审。源文件及登记表原文备份和SHA256见backups/teamo-function-outline/manifest.json。

### Risk

Medium。源图混合菜单、流程、状态和占位节点；优先级大多未标注，不能将整理建议视为MVP批准。

### 旧口径—新证据—建议修改

- 旧口径：现行规格二维码/学校任务等细化范围待评审；前文通用大纲加入开放对话、社交分享等内容。
- 新证据：用户提供的XMind明确列二维码、学校任务、成长星等，未列开放对话或社交分享；仅“动作判断p0”显式标P0。
- 建议修改：本稿保留源图范围并将新增描述和优先级标为建议；排行榜须服从禁止全站公开排名的既有边界；不自动覆盖现行规格或PRD。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 新增六类源图模块的表格式大纲、88节点追踪、待确认问题及需求映射；未批准MVP范围 |

# Decision Log

## Decision OUTLINE-001

Date: 2026-10-12

Problem: 源图范围、前文通用大纲与现行规格不能直接视为同一批准基线。

Context: 用户要求参考所提供文件写成文档；XMind为内容输入，Titan Gateway文档为格式参考。

Options Considered: 改写现行规格；独立整理源图并登记用途。

Decision: 独立源图整理稿供评审，后续是否合并到现行规格待决定。

Reason: 保留源节点与来源差异，避免静默修改已有需求。

Impact: 六模块结构和建议优先级仅用于本稿讨论，不承诺工程架构或菜单页面实现。

Owner: 待确认。

Status: Proposed

Evidence: 用户本次请求、teamo设备端.xmind、项目产品边界规范及现行功能规格。
