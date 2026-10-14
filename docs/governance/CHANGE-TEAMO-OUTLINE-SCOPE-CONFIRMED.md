# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Documentation Change Record |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# 功能大纲范围确认修改报告

Version: 大纲v2.1.2→v2.2.0；独立映射v0.1.0→v0.2.0；登记表v1.6.0→v1.7.0。

Change Type: Minor（设备儿童切换、角色P0、宠物功能退出与下一代方向调整）。

# Change Impact

本记录先于正文修改写入；完整原文及SHA256见[manifest](backups/teamo-outline-scope-confirmed-20261013/manifest.json)。

| Section | Before | After |
|---|---|---|
| XMind节点索引、优先级与范围差异 | 混在大纲中且存在已解决问题 | 移除这两个章节及失效索引引用；历史原文在备份可恢复 |
| 1.1.2儿童绑定 | 当前儿童确认 | 保留编号/P0，支持设备端切换已绑定儿童，不增加人脸识别 |
| 3.6角色状态 | 待机/活动与待机回应TBD | 3.6.1、3.6.2改P0；3.3.3原P0保留，时间3.6.3仍TBD |
| 3.1.4宠物 | TBD候选 | Deprecated/已废弃，不再纳入产品候选；保留编号追溯，不新增宠物能力 |
| 骨架与视频回放 | Open Questions | 不显示骨架、不做视频回放且不列后置方向；移除待确认问题 |
| 下一代升级 | 投屏、手表、语音输入为TBD | 明确下一代产品升级方向，当前MVP不纳入；语音播报能力保持 |
| 命名与动作 | 成长星/运动星待统一，深蹲称谓差异 | 当前正文统一成长星、开合跳/深蹲起/高抬腿；历史记录原样保留 |
| 映射、统计与问题 | 宠物候选、角色TBD与旧数量 | 同步独立映射、统计和当前问题，避免结论冲突 |

旧口径—新证据—修改：原稿上述事项待评审；用户本次明确范围，按本次指令更新。源设备PRD v1.1.1正文第36/58行已确认演示三动作；其奖励原称运动星，当前大纲按用户明确要求统一成长星，原PRD不静默改写。

Affected Documents: 两份同源功能大纲、独立映射、全局登记。其他PRD、UE、规格与云端文件本次不直接改写。

Risk: Low；无技术/算法/交互设计。角色与儿童切换为用户明确范围，其他未决项继续保留。79条历史编号保留，其中1条宠物已废弃；不将该行计作在做功能。

Next Action: 后续PRD、UE、规格按此同步范围及成长星命名；下一代方向仅记录方向，不承诺实现、排期或接口。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 新增移除索引与差异章节、儿童切换、角色P0、宠物废弃、下一代方向及术语统一的变更记录 |

# Decision Log

## Decision TEAMO-SCOPE-CONFIRMED-001

Date: 2026-10-13

Problem: 当前大纲保留已解决候选与过量索引。

Context: 用户明确本次功能取舍与资料精简；原PRD确认演示三动作。

Options Considered: 继续Pending Review；按明确指令记录结论并移除相关问题。

Decision: 支持设备儿童切换；角色状态及待机回应P0；不显示骨架、不做视频回放、无宠物功能；投屏/手表/语音输入为下一代升级方向；名称成长星、演示动作深蹲起。删除两章并同步独立映射。

Reason: 用户明确范围指令。

Impact: 仅更新功能范围与文档，成长星奖励规则仍待设计；不批准其他未决功能。

Owner: 文档责任待确认（项目协调：魏子奇）。

Status: 本次用户明确功能指令已执行；整份文档Review，非整份产品冻结。

Evidence: 用户本次消息；源MVP设备PRD演示动作段落。
