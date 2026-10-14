# Change Order: Teamo 设备端功能规格修订清单（v2.2.1 → v2.3.0 建议）

| 字段 | 内容 |
|---|---|
| Change ID | TEAMO-SPEC-REVISION-LIST-230 |
| Date | 2026-10-13 |
| Type | 新增独立阶段文档（修订建议清单） |
| Trigger | 用户指令：根据缺口分析输出功能大纲修订清单，不新增独立"硬件需求对应功能"模块 |
| Status | Draft（建议未批准） |

## 变更对象

- 新增：[Teamo_Device_Function_Specification_Revision_List_v2.3.0.md](../product/requirements/Teamo_Device_Function_Specification_Revision_List_v2.3.0.md)（控制版本 v0.1.0 / Draft）
- 不修改：[Teamo_Device_Function_Specification_v2.1.0.md](../product/requirements/Teamo_Device_Function_Specification_v2.1.0.md)（控制版本 v2.2.1 / Review）——清单被 Owner/Reviewer 评审接受后，才按清单反向修订规格并升版 v2.3.0。
- 不修改：[Teamo_Hardware_Software_Gap_Analysis.md](../product/requirements/Teamo_Hardware_Software_Gap_Analysis.md)（来源，保持 v1.0.0）。

## Section / Before / After

- Section: 设备端软件职责修订入口。
- Before: 缺口分析 v1.0.0 已确认 13 项文档职责缺口（G-01–G-13），但缺少逐项落到规格既有功能 ID 的修订建议；用户提供的草稿编号（1.1.X、3.3.X 等）与规格 v2.2.1 实际结构不一致。
- After: 新增修订清单，按规格 v2.2.1 一级模块结构逐项映射：12 项为既有功能补充、1 项新增子功能（2.2.9 识别就绪确认）；不新增一级模块，不改变 MVP 范围；待确认项（P-01–P-06）与范围差异（S-01–S-08）明确不纳入。
- Impact Scope: 本清单、规格 v2.2.1（后续评审后）、managed-documents.json；PRD、UE IA、硬件输入、源大纲不改写。
- Risk: Low（本轮仅新增建议文档，不改任何基线正文）；评审通过后修订规格时为 Medium（功能描述变更涉及 82 条功能中的 14 项）。

## 修订原则（用户指令）

1. 一级功能编号不变，不新增一级功能模块；
2. 优先修改已有 Function 描述；
3. 只有无法承接时新增子功能（本轮仅 2.2.9 一项）；
4. 描述保持功能大纲语言，不写 PRD/技术参数语言；
5. 摄像头管理、姿态检测不单独新增一级功能，并入既有功能。

## Next Action

魏子奇组织 Owner/Reviewer 评审本清单；接受后按清单修订规格 v2.2.1 → v2.3.0（Minor 升版，另立规格变更记录）；未决项（P-01–P-06、S-01–S-08）单独评审。
