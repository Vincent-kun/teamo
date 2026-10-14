# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Change Impact |
| Current Version | v1.1.0 |
| Status | Review |
| Owner | 魏子奇 |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# CHANGE：《Teamo Circular Display Design System》v1.0.0 → v1.1.0

> 变更类型：Minor（设计系统评审修订：修复几何错误 + 补齐 Token/状态层/校验/交付/追踪七块内容）。
> 修改前基线备份：`docs/governance/backups/teamo-circular-ds-v110/Teamo_Circular_Display_Design_System_v1.0.0.md`（SHA256 前缀 b4f60eaca3490c10）。
> 注：修改执行时发现工作区文件首部曾被用户粘贴评审提示词覆盖（v1.0 正文已被替换）；因 v1.0 基线已在修改前完成备份，无数据丢失，本次以备份基线为 diff 依据。

## 变更内容（对应评审八部分）

| 评审要求 | 落点 | 结果 |
|---|---|---|
| 一、健康检查（几何/安全区阈值） | §1.1/§1.2/§2.5/§4.3 修正 + §15 CDS-R001/002/004/005/010/011 | 发现并修复 2 处几何错误；补 PPI/DPR；88/70 阈值维持 Current Proposal + Decision Pending |
| 二、Design Token | 新增 §9（Layout/Typography/Icon） | `cds-` 前缀 Token 体系；字重 ≤2、中文子集化（OI-08）、tabular figures |
| 三、Fixed Slots 复审 | 新增 §10 Slot Coverage Matrix + S5 候选槽 | PAGE-00–08 全覆盖校验；S2 单项承载可行，轮播场景 S5 标记 Candidate |
| 四、Display State System | 新增 §11 Display State Layer | DS-00–06 映射 PRD 4.21；亮度推荐值待 OI-07 |
| 五、Layout Validation Rules | 新增 §12 | Rule-001–011，Mandatory/Pending 分级 |
| 六、工程交付规范 | 新增 §13 | Frame/Overlay/Export/Asset 命名（TEA_ 前缀） |
| 七、文档映射 | 新增 §14 Traceability Matrix | 12 条 DS 条目 ↔ PRD/UE IA/Gap |
| 八、版本管理 | §15 Revision Log（R001–R013）+ Version History | Status: Draft → Review（Review Candidate） |

## 关键评审发现（几何修正，需评审会确认）

1. **CDS-R001**：v1.0 §2.5 弦宽按物理边界 r=180 计算（y=140 处 226px），文字两端落在玻璃边缘；修正为安全圆 r=158 的可用弦宽 146px。
2. **CDS-R002**：v1.0 S3「199×48px 按钮盒」几何不成立（48px 高矩形在 r=158 圆内下沿必有角点越界，且宽度越大越界越重）；重定义为弦区文字槽 + 胶囊容器 + 不可见热区。
3. **CDS-R003**：S4 进度环与 S3 在 6 点方向重叠；新增 72° 缺口规则。
4. **CDS-R005/OI-06**：ST77916 与 360×360 配对未经 datasheet 复核，列为待确认。
5. **CDS-R010/OI-09**：48px 必读提示 @2.5m 视角约 8.4′ 临界，>2m 场景建议 56px；88%/70% 阈值维持待决策。

## Affected Documents

| 文档 | 影响 |
|---|---|
| Teamo_Circular_Display_Design_System.md | v1.0.0 → v1.1.0（本变更主体） |
| Teamo_Device_UE_IA_v0.3.1.md / Teamo_Device_PRD_v1.0.md / Functional Spec v2.3.0 / Gap Analysis | 零修改；后续 UI Flow/视觉稿引用 v1.1 |
| DOCUMENT_REGISTER.md | 条目版本与状态同步 |

## Risk

Low–Medium。几何修正使 S1/S3 尺寸更严格，但 v1.0 无下游实现，无返工成本；亮度值、阈值、S5 均为 Pending，未经评审不得冻结。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-13 | WorkBuddy（AI，执行用户指令） | Review | 登记设计系统 v1.0.0 新增 |
| v1.1.0 | 2026-10-13 | WorkBuddy（AI，执行用户指令） | Review | 登记设计系统 v1.1.0 评审修订：2 处几何错误修复（R001/R002）、缺口规则（R003）、新增 §9–§15 七个章节与 OI-06–09；记录基线备份与工作区文件被提示词覆盖事件 |

# Decision Log

本次无产品方向、功能取舍或系统架构决策。几何修正（D-CDS-02 已在设计系统文档登记，Proposed）与阈值维持为设计层提案，待 UE 评审会议确认。
