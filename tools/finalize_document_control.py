from pathlib import Path
import json, re, hashlib, zipfile
from document_control import ROOT, GOV, DATE

rows = json.loads((GOV/'audit-before-20261012.json').read_text(encoding='utf-8'))
managed = json.loads((GOV/'managed-documents.json').read_text(encoding='utf-8'))

def wrapper(body, summary, version='v1.0.0'):
    return f'''# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Documentation Governance |
| Current Version | {version} |
| Status | Review |
| Owner | 魏子奇（项目协调；文档审核责任待确认） |
| Reviewer | 待指派 |
| Created Date | {DATE} |
| Last Updated | {DATE} |

'''+body+f'''

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| {version} | {DATE} | Codex（AI，执行用户指令） | Review | {summary} |

# Decision Log

本次文档治理决策见 DOCUMENT_VERSION_POLICY.md 的 DOC-001；无新增产品或架构决定。
'''

# Update agent instruction and make the substantive process addition a Minor.
p = ROOT/'AGENTS.md'
text = p.read_text(encoding='utf-8')
r = next(r for r in rows if r['path']=='AGENTS.md')
new = 'v0.2.0'
text = text.replace(r['new_version'], new)
text = text.replace('新增 Document Control、标准 Version History、Change Impact 与 Decision Log；保留既有业务正文及历史记录',
                    '新增文档版本管理强制入口与修改流程；补齐控制表、历史、影响及决策入口；保留原导航与业务规则')
insert = '''

## 10. Markdown 文档版本管理（2026-10-12 用户指定）

修改或新建任何 Markdown 前，必须读取 [文档版本管理规范](docs/governance/DOCUMENT_VERSION_POLICY.md) 和 [文档登记表](docs/governance/DOCUMENT_REGISTER.md)，执行其中七步流程。修改前留存可恢复基线并先写 Change Impact；修改后同步控制版本、日期、具体变更历史，涉及产品/功能/架构取舍时记录 Decision Log，最后输出修改报告。现行权威顺序继续按 §4；文档版本较高不等于业务批准。

本次用户授权只对核心 Markdown 补齐治理结构，保留原正文和路径。未来新文档用稳定语义名称，在同一文件内维护版本历史；历史冻结快照及禁止触碰目录遵循原保护规则。检查命令：受管 Python 执行 `tools/document_control.py`；新增核心文档须加入 `docs/governance/managed-documents.json`。
'''
text = text.replace('\n\n---\n\n# Version History', insert+'\n\n---\n\n# Version History', 1)
p.write_text(text, encoding='utf-8')

change = (GOV/'CHANGELOG-20261012.md').read_text(encoding='utf-8')
change = change.replace(f"| [AGENTS.md](../../AGENTS.md) | {r['old_version']} | {r['new_version']} | Patch | 新增控制表、基线登记、影响记录及决策入口；保留原业务正文 |",
                        f"| [AGENTS.md](../../AGENTS.md) | {r['old_version']} | {new} | Minor | 新增强制文档治理流程入口；补齐控制与历史结构 |")
(GOV/'CHANGELOG-20261012.md').write_text(wrapper(change, '登记105份核心Markdown的原版本、新版本及具体结构变更；记录备份与影响范围'), encoding='utf-8')

body = '''# 文档登记表与现行入口

本表登记本次治理范围，路径保持不变。规范树/现行规范的原权威顺序仍生效。下表“最新修订入口”按同族版本号推导，仅用于定位最新稿，不表示获批或取代现行 PRD；各文件 Document Control 是其治理版本来源。

## 已识别的多版本文档族

| 文档族 | 最新修订入口 | 历史文件 | 审批说明 |
|---|---|---|---|
'''
families = {
    'Teamo MVP设备端功能大纲': [r for r in rows if r['path'].startswith('docs/product/requirements/Teamo_MVP_设备端软件功能大纲')],
    'Teamo MVP设备端UE信息架构': [r for r in rows if r['path'].startswith('docs/product/requirements/Teamo_MVP_设备端UE信息架构')],
    'Teamo整体UI逻辑框架': [r for r in rows if '/Teamo_' in r['path'] and 'UI整体逻辑框架' in r['path']],
}
for family, group in families.items():
    group.sort(key=lambda r:tuple(map(int, r['old_version'][1:].split('.'))))
    latest = group[-1]
    link=lambda r:f"[{Path(r['path']).name}](../../{r['path']})"
    body += f"| {family} | {link(latest)} | {'；'.join(link(r) for r in group[:-1])} | 最新稿为候选/研究入口，批准状态以审查证据为准；旧文件保留用于追溯，后续在最新入口内迭代 |\n"
body += '''
planning 下 Teamo_DeviceSoftware 功能大纲为另一份功能梳理稿，不自动与 requirements 文档合并。docs/product/requirements 下现行 HTML PRD 继续保持原权威。既有旧文件名包含“最新”等字样属于历史兼容保留，后续不新建这种名称。

## 核心 Markdown 清单

| 文档 | 治理版本 | 提交状态 | 历史缺口 |
|---|---|---|---|
'''
for row in rows:
    if row['path'] not in managed: continue
    gap = '已有正文历史，作者/日期/审批待逐条核实' if row['legacy_history'] else '缺少历史变更序列；已登记现存基线，待Owner补录'
    v = new if row['path']=='AGENTS.md' else row['new_version']
    body += f"| [{row['path']}](../../{row['path']}) | {v} | {row['status']} | {gap} |\n"
body += '''
## 未改写范围

archive、部署/工具缓存、prototype 的非 AGENTS 文档、PPOS 模板及旧树非现行规范/会议纪要等保持原样；原始审计结果也包含未改写文档。未来修改这些可编辑 Markdown 时仍执行版本规则；模板内容应使用占位字段，历史快照不回写。旧树会议纪要已纳入治理结构，原会议内容保留。

# Change Impact

### Modified Sections

- Section: 文档入口登记。
- Before: 同族多个版本缺少统一登记。
- After: 登记核心文档及已识别版本族的最新修订入口，保留历史路径。

### Impact Scope

Affected:
- 文档查找与后续版本修改。

### Risk

Low。入口选择基于文件版本，不推断审批或范围冻结；同名不同用途不合并。
'''
(GOV/'DOCUMENT_REGISTER.md').write_text(wrapper(body, '新增105份核心文档登记、三组多版本修订入口及历史补录缺口'), encoding='utf-8')

# Verify byte-level preservation of every original body, including untracked local edits.
with zipfile.ZipFile(GOV/'baseline-before-document-control-20261012.zip') as z:
    for name in managed:
        original = z.read(name)
        record = next(r for r in rows if r['path']==name)
        assert hashlib.sha256(original).hexdigest()==record['sha256'], name
        original_text = original.decode('utf-8-sig')
        current = (ROOT/name).read_text(encoding='utf-8')
        assert original_text.replace('\r\n','\n') in current, name
print('PASS: 105 original document bodies preserved; baseline SHA256 verified')
