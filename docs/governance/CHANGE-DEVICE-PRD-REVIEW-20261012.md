# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | PRD Review Compilation |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Change Impact

- Section: 新PRD十章、逐功能产品需求卡、来源追踪、登记入口。
- Before: 四份输入各自独立，v0.6.0 Draft保留既有内容。
- After: 新增v1.0.0 Draft/Review评审稿，保留47核心、20候选、2停用及17 OQ/11 UE-OQ；不修改四份源文档。
- Change Type: PRD Review Compilation；文档正式化，不是需求/产品Major升级。
- Risk: Medium；七/三动作、倒计时数值、工程字段与未决实现之间有差异，不能擅自裁决。
- Affected: PRD及四个登记/导航文件；旧PRD不覆盖，原资料不重写。
- Baseline: backups/device-prd-review-20261012/baseline.zip及sha256.json。

## 旧口径—输入证据—本稿处理

| 旧口径 | 唯一输入证据 | 本稿处理 |
|---|---|---|
| 需求基线七动作 | 功能规格4.2列三动作提议；OQ-01 | 保留差异，由OQ-01/UE-OQ-03确认，不删七动作追踪或增补功能号 |
| 基线倒计时3/2/1 | UE IA4.2时长TBD | 不冻结3秒，引用OQ-07/UE-OQ-05 |
| 基线字段和较广维护/体态描述 | 功能规格0.5/9/10与工程参考声明工程细则TBD | 字段作为已有输入线索，不生成API规格；体态/OTA等保持范围TBD |
| 工作流顺序有不同表述 | 功能规格0.5与13.1、工程参考F | 按用户本次要求展示PRD→FR→UI Flow→Test Case；实际同步迭代，不改变能力 |

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 新增PRD编制前影响分析、差异处理及备份入口 |

# Change Impact

- Section: 设备端PRD结构、需求追踪及文档登记。
- Before: 四份输入分别描述需求、功能、UE和工程参考；此前PRD Draft保留在原路径。
- After: 形成指定十章PRD评审稿，逐项引用既有编号；范围、优先级及未决状态不变。
- Affected: 本PRD、目录README/REGISTER、全局登记表与managed-documents.json。
- Risk: Medium；输入存在三/七动作与倒计时时长差异，已显式保留，不能把候选或TBD当成冻结要求。
- [修改前变更单](CHANGE-DEVICE-PRD-REVIEW-20261012.md)。

# Decision Log

本次无产品方向、功能取舍或架构决策。v1.0表示正式PRD评审材料的文档版次，不表示MVP阶段变化、产品批准、实现或实机验收。源文档差异留待原OQ/UE-OQ评审；本稿不裁决。
