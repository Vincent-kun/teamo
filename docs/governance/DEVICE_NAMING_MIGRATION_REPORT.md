# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Document Migration Report |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇；不等同审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Migration Report

## 1. Rename Summary

迁移5份Markdown及3份HTML。旧路径保留完整兼容快照；另保留不同内容的.md.html历史导出。14个历史文件及整体PRD原字节保持。需求版本不升级；PRD v0.6 Draft仅规范为v0.6.0 / Draft。

## 2. File Hash Before/After

SHA256不同源于链接及治理元数据；不是需求变化。完整原文见[备份](backups/device-naming-migration-20261012/originals.zip)。

| Old | New | SHA256 Before | SHA256 After |
|---|---|---|---|
| 设备端需求基线_评审稿_V0.1_20261010.md | Teamo_Device_Requirement_Baseline_v0.1.1.md | `c4c950fa87053b1e8776018a5b5d002c9f964abd62edee72821962ff162fbb5b` | `3f7fa857e14d8a849e05ec755e40e522f91b4cca007950f93a7fb89dd34e6aa8` |
| Teamo_MVP_设备端软件功能大纲_v0.5_UE功能同步评审_20261012.md | Teamo_Device_Function_Specification_v0.5.2.md | `6203ac091a2cf0c2e696b2d182e7fbec161d7eed76d4210226c5bee27654db7f` | `cf0e09aebc83594cce7b3f92372f99bbff0f5219590f901f82dc3e68bc1db040` |
| Teamo_MVP_设备端UE信息架构_v0.3.1_20261012.md | Teamo_Device_UE_IA_v0.3.1.md | `f210af2f34817e4c6b261c1c5056f4a3942d2382554f21c2ff96f5a70294c18e` | `4d2cf7e0a1f9f7c6dadee2320dcecfa9c82395298ac20b9feb1f471d7b328ee5` |
| Teamo_MVP_UE工程附录.md | Teamo_Device_UE_Engineering_Reference_v0.1.0.md | `cd40ce928a054821cbba0f0118de28d3c88da1b47e5e0785ec562baaf2dcee4c` | `0a850435a8ddc3638c40f9429e40f8b8f80c215b4073389664bc2ab10f9323ab` |
| Teamo_MVP_Device_PRD_v0.6_Draft.md | Teamo_Device_PRD_v0.6.0_Draft.md | `4ac2418fbb66300829885eedac202834caaedb71e43465e92ac305831edf3ef3` | `83eb2fed8d071eaf5a8d3e516ba77cf9c06250b26a3f56683aebcfa367b29520` |
| Teamo_MVP_设备端软件功能大纲_v0.5_UE功能同步评审_20261012.html | Teamo_Device_Function_Specification_v0.5.2.html | `f603b1e7342bdc48ffd5b1a22452112c073f458dd302da1ab4783ed25fae3fb2` | `57ea9f6ad5283907545c21a0927090898b9c2edb184184878ab475fc3a88e297` |
| Teamo_MVP_设备端UE信息架构_v0.3.1_20261012.html | Teamo_Device_UE_IA_v0.3.1.html | `f63e8b8e5bc915713bc52c236d5b7aad4aea28403c78f068dd7d1e881d67daec` | `a052249e1c78a6a8d110e338b5435a37bbef92e12f6bcb25dc134acb857c4785` |
| Teamo_MVP_UE工程附录.html | Teamo_Device_UE_Engineering_Reference_v0.1.0.html | `228d635ee44c20aa844c7c1a718ea39f7f8896990667553448d4534e8e959e20` | `a22f3b6a6d2fa8757cc7650b1c6046ea4086b4ba1c04d379fc8f090c7b99fffe` |

## 3. Link Migration Result

规范文件路径引用已迁移。目录本地引用检查：迁移前267处，迁移后416处；HTML文件及显式锚点检查完成。旧HTML兼容快照保留全部原锚点，旧Markdown保留原正文与标题。外部引用未改写，继续经旧路径兼容入口访问。未验证远程链接或浏览器动态脚本。

## 4. Broken Link Report

迁移前：0处；迁移后：0处。详见[检查证据](device-naming-migration-evidence.json)。Markdown标题锚点未自动验收，采用正文标题原样保留策略。

## 5. Document Register Update

全局登记表v1.0.0→v1.0.1（登记修订）；补充设备端目录README和REGISTER；managed-documents.json迁移路径并补登记现行文档。历史审计、变更单、保护目录不改写。

### Document Control Validation

执行tools/document_control.py：本次迁移文档、新导航、新登记与报告未报告错误。全库检查仍报告31项既有治理结构错误，位于6份历史变更单；未改写这些历史记录。

```text
docs/governance/CHANGE-AGENTS-V021-20261012.md: missing Document Control
docs/governance/CHANGE-AGENTS-V021-20261012.md: missing Version History
docs/governance/CHANGE-AGENTS-V021-20261012.md: missing Change Impact
docs/governance/CHANGE-AGENTS-V021-20261012.md: missing Decision Log
docs/governance/CHANGE-AGENTS-V021-20261012.md: current/history mismatch
docs/governance/CHANGE-AGENTS-V021-20261012.md: updated/history date mismatch
docs/governance/CHANGE-FEATURE-OUTLINE-UE-SYNC-20261012.md: missing Document Control
docs/governance/CHANGE-FEATURE-OUTLINE-UE-SYNC-20261012.md: missing Version History
docs/governance/CHANGE-FEATURE-OUTLINE-UE-SYNC-20261012.md: missing Decision Log
docs/governance/CHANGE-FEATURE-OUTLINE-UE-SYNC-20261012.md: current/history mismatch
docs/governance/CHANGE-FEATURE-OUTLINE-UE-SYNC-20261012.md: updated/history date mismatch
docs/governance/CHANGE-UE-IA-V03-20261012.md: missing Document Control
docs/governance/CHANGE-UE-IA-V03-20261012.md: missing Version History
docs/governance/CHANGE-UE-IA-V03-20261012.md: missing Decision Log
docs/governance/CHANGE-UE-IA-V03-20261012.md: current/history mismatch
docs/governance/CHANGE-UE-IA-V03-20261012.md: updated/history date mismatch
docs/governance/CHANGE-UE-IA-V031-20261012.md: missing Document Control
docs/governance/CHANGE-UE-IA-V031-20261012.md: missing Version History
docs/governance/CHANGE-UE-IA-V031-20261012.md: missing Decision Log
docs/governance/CHANGE-UE-IA-V031-20261012.md: current/history mismatch
docs/governance/CHANGE-UE-IA-V031-20261012.md: updated/history date mismatch
docs/governance/CHANGE-UE-OPEN-QUESTIONS-20261012.md: missing Document Control
docs/governance/CHANGE-UE-OPEN-QUESTIONS-20261012.md: missing Version History
docs/governance/CHANGE-UE-OPEN-QUESTIONS-20261012.md: missing Decision Log
docs/governance/CHANGE-UE-OPEN-QUESTIONS-20261012.md: current/history mismatch
docs/governance/CHANGE-UE-OPEN-QUESTIONS-20261012.md: updated/history date mismatch
docs/governance/CHANGE-UE-STATE-WIREFRAMES-20261012.md: missing Document Control
docs/governance/CHANGE-UE-STATE-WIREFRAMES-20261012.md: missing Version History
docs/governance/CHANGE-UE-STATE-WIREFRAMES-20261012.md: missing Decision Log
docs/governance/CHANGE-UE-STATE-WIREFRAMES-20261012.md: current/history mismatch
docs/governance/CHANGE-UE-STATE-WIREFRAMES-20261012.md: updated/history date mismatch
```

## 6. Final Requirement Tree

```text
docs/product/requirements/
  03_儿童AI运动陪伴机器人_PRD_V3.0.html
  DOCUMENT_REGISTER.md
  README.md
  Teamo_Device_Function_Specification_v0.5.2.html
  Teamo_Device_Function_Specification_v0.5.2.md
  Teamo_Device_PRD_v0.6.0_Draft.md
  Teamo_Device_Requirement_Baseline_v0.1.1.md
  Teamo_Device_UE_Engineering_Reference_v0.1.0.html
  Teamo_Device_UE_Engineering_Reference_v0.1.0.md
  Teamo_Device_UE_IA_v0.3.1.html
  Teamo_Device_UE_IA_v0.3.1.md
  Teamo_MVP_Device_PRD_v0.6_Draft.md
  Teamo_MVP_UE工程附录.html
  Teamo_MVP_UE工程附录.md
  Teamo_MVP_设备端UE信息架构_v0.1_20261012.html
  Teamo_MVP_设备端UE信息架构_v0.1_20261012.md
  Teamo_MVP_设备端UE信息架构_v0.2_20261012.html
  Teamo_MVP_设备端UE信息架构_v0.2_20261012.md
  Teamo_MVP_设备端UE信息架构_v0.3.1_20261012.html
  Teamo_MVP_设备端UE信息架构_v0.3.1_20261012.md
  Teamo_MVP_设备端UE信息架构_v0.3_20261012.html
  Teamo_MVP_设备端UE信息架构_v0.3_20261012.md
  Teamo_MVP_设备端软件功能大纲_PRD前置文档_v0.1_20261012.html
  Teamo_MVP_设备端软件功能大纲_PRD前置文档_v0.1_20261012.md
  Teamo_MVP_设备端软件功能大纲_v0.2_20261012.html
  Teamo_MVP_设备端软件功能大纲_v0.2_20261012.md
  Teamo_MVP_设备端软件功能大纲_v0.3_20261012.html
  Teamo_MVP_设备端软件功能大纲_v0.3_20261012.md
  Teamo_MVP_设备端软件功能大纲_v0.4_冻结候选_20261012.html
  Teamo_MVP_设备端软件功能大纲_v0.4_冻结候选_20261012.md
  Teamo_MVP_设备端软件功能大纲_v0.5_UE功能同步评审_20261012.html
  Teamo_MVP_设备端软件功能大纲_v0.5_UE功能同步评审_20261012.md
  Teamo_MVP_设备端软件功能大纲_v0.5_UE功能同步评审_20261012.md.html
  设备端需求基线_评审稿_V0.1_20261010.md
```

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 新增设备端文档治理迁移记录与导航 |

# Change Impact

- Section: 文件名称、引用路径、治理记录及导航。
- Before: 职责名称不一致，版本、日期及状态混入路径。
- After: 使用批准映射，保留历史及旧路径兼容入口；需求和编号不变。
- Risk: Low；完整原文件及SHA256见治理备份。
- Change Type: Document Governance Migration；不构成需求升级。

# Decision Log

本次无产品/架构决策。用户已批准命名迁移；文档仍为Draft/Review，不代表需求批准。
