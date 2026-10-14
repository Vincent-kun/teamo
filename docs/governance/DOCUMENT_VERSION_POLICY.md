# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Documentation Governance |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 魏子奇（项目 Owner；文档责任分配待确认） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Markdown 文档版本管理规范

适用于 PRD、功能规格、功能大纲、竞品分析、UX Flow、硬件/技术需求、会议纪要及项目治理文档。用户本次授权对现有核心 Markdown 增加治理结构；既有业务正文和路径保留。历史快照、缓存、部署目录不批量改写。HTML、PDF、Office 源文件未纳入本次 Markdown 改造，不得因 Markdown 版本较新推断其取代现行 HTML PRD。

## 唯一入口与版本

采用 `vMajor.Minor.Patch` 三段格式。旧 `v1.0` 等同 `v1.0.0`，只规范表示不构成业务变更。

| 类型 | 条件 | 示例 |
|---|---|---|
| Major | 产品方向、商业模式、架构或 MVP 阶段变化 | v1.2.3 → v2.0.0 |
| Minor | 新增/删除功能、模块结构或流程变化 | v1.2.3 → v1.3.0 |
| Patch | 文案、错字、格式、小范围描述修正 | v1.2.3 → v1.2.4 |

组合修改取最高级别；升 Major 时 Minor/Patch 归零，升 Minor 时 Patch 归零。日期是项目时区 Asia/Shanghai 的修改日期。同日多次修改仍分别递增。审批状态变化也要记录版本及日期，不能悄悄将 Review 改为 Approved。

新文档使用稳定语义名称，如 `PRD.md`，内部维护版本历史。禁止新建 `xxx_final.md`、`xxx_final_final.md`、`xxx最新版.md` 或以版本/日期不断复制正文。既有文件名暂保留用于链接兼容；以后在登记入口对应文件内迭代。迁移稳定名称必须核对所有引用并留下重定向说明，不批量搬移。

核心文档顶部必须有用户指定八字段的 Document Control 表。Owner 是具体文档责任人，Reviewer 是具体审核人；未知写待确认，不将 AI 或项目 Owner 自动当作批准人。Created Date 不随修改改变，未知日期保留待核实；Last Updated 每次修改更新。Current Version 必须等于 Version History 最后一条有效记录的版本，Last Updated 等于该条日期。Status 仅取 Draft / Review / Approved / Frozen / Deprecated；历史行的状态未知可写待核实。

Draft 为编辑稿；Review 为提交评审；Approved 必须有 Reviewer 的明确批准证据；Frozen 必须有冻结范围和批准证据；Deprecated 必须说明替代入口。版本最高只表示最新修订，不代表已批准，更不代表自动覆盖产品边界。AI 产出标记 Author 为实际 Agent，注明审核状态及来源，未经人工批准保持 Draft/Review。

## 每次修改流程

1. 读取 Document Control、Version History、相关 Decision Log、登记入口和原权威资料；核实当前正文及既有本地修改。若控制表缺失，先登记现存基线，标明历史事实缺口。
2. 判断 Major/Minor/Patch，写明触发条件。变更前保存可恢复原文：已提交 Git 基线可引用提交 SHA；未提交/未跟踪文件用完整备份加 SHA256。不得将工作区中他人已有修改纳入自己的提交。
3. **先写 Change Impact，再改正文**。在 `docs/governance/` 创建独立变更单，逐节写 Section、Before、After，列受影响文档与风险。新证据涉及既有 PRD/画布/大纲时增加「旧口径—新证据—建议修改」，按项目权威顺序处理，不能静默覆盖。
4. 修改正文并升级版本；更新 Last Updated 和状态。在 Version History 追加 Version、Date、Author、Status、Change Summary。Summary 用“新增/删除/调整/修复 + 明确对象和前后变化”，避免“优化文档”等空泛描述。
5. 将已写影响分析放入本文 Change Impact，关联独立变更单。检查引用、功能规格、UI Flow、技术/硬件要求是否需同步；只修改已获授权的内容，未决同步项明确登记。
6. 涉及方向、功能取舍或架构时追加 Decision Log。记录证据、考虑选项、选择理由、范围和 Owner；已批准与待评审提案明确区分。非决策修改记录“本次无产品/架构决策”，不编造历史决策。
7. 校验控制版本、最后一行历史版本/日期、具体摘要、链接及必要决策记录；输出下列修改报告。执行 `tools/document_control.py` 可检查已登记文档的结构、版本及日期一致性；脚本不能替代内容评审。

```yaml
Version:
  Old: v1.0.0
  New: v1.0.1
Change Type: Patch
Changes:
  - 修复具体对象及前后变化
Affected Documents:
  - 文档路径
Next Action: 责任人及待评审/同步事项，或无
```

## 模板

```markdown
# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.1.0 | YYYY-MM-DD | 实际作者 | Draft | 新增具体模块及适用范围 |

# Change Impact

### Modified Sections

- Section: 具体章节
- Before: 原口径
- After: 新口径

### Impact Scope

Affected:
- PRD
- Feature Spec
- UI Flow
- Technical Requirement

### Risk

Low / Medium / High（选择其一并写依据）

# Decision Log

## Decision DOC-XXX

Date:
Problem:
Context:
Options Considered:
Decision:
Reason:
Impact:
Owner:
Status: Proposed / Approved / Superseded
Evidence:
```

## 历史补录和本次基线

审计原始结果见 `audit-before-20261012.json`；原文 ZIP 和 SHA256 可恢复本次修改前状态。缺失 Version History 与 Change Summary 已以“现存基线登记”补齐结构，不把登记日期当作历史发布日期。现有正文中的版本记录保留，未核实的作者、日期、审批记录不自动补造；Owner 后续以 Git、原文或会议确认逐条补录，并写新的修订历史。

文档清单见 `DOCUMENT_REGISTER.md`，逐文件变化见 `CHANGELOG-20261012.md`。本次治理版本高于原正文版本；原文件名/标题的版本仅作历史业务标识，未来修改同步标题或去除标题版本，并保留历史记录。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 新增三段版本、审批证据要求、修改前备份与影响分析流程、历史补录与 AI 内容管理规则 |

# Change Impact

### Modified Sections

- Section: 项目文档治理。
- Before: 分散版本标识，缺少统一执行流程。
- After: 建立控制表、历史记录、变更单与决策记录流程。

### Impact Scope

Affected:
- 所有后续 Markdown 编辑和新建；历史冻结快照保持。

### Risk

Low。流程遵循用户要求；不改变业务基线或代替人工审批。

# Decision Log

## Decision DOC-001

Date: 2026-10-12

Problem: 多版本文件和分散记录导致最新稿、批准状态与修改原因难以追溯。

Context: 用户明确要求严格版本管理；项目存在双树、旧链接和未经冻结的评审稿。

Options Considered: 批量重命名搬移；保留路径并建立登记入口及文档内部版本历史。

Decision: 保留路径、原正文和历史记录，新增文档控制与治理入口；未来在同一文档内迭代。

Reason: 完成用户授权的结构治理，同时保持现行权威关系及链接可用。

Impact: 现存 Markdown 增加结构修订；新增稳定命名和变更追溯规则，不批准产品取舍。

Owner: 魏子奇（规则需求来源：用户本次指令；后续责任分配待确认）。

Status: 用户要求已执行；具体文档审批仍为 Draft/Review。
