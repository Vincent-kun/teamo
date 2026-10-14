"""Bootstrap and validate Markdown document controls; standard library only."""
from pathlib import Path
import re, json, hashlib, zipfile, sys

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-10-12'
GOV = ROOT / 'docs/governance'
EXCLUDED = {'.git', 'node_modules', '.sites-deploy', '.workbuddy', '.docx-review', 'archive', '_publish'}

def inventory():
    return sorted(p for p in ROOT.rglob('*.md') if not EXCLUDED.intersection(p.relative_to(ROOT).parts) and 'governance' not in p.relative_to(ROOT).parts)

def core(p):
    s = p.relative_to(ROOT).as_posix()
    return (s.startswith(('docs/', 'AI运动伙伴/00_现行研究与规范_20260918/', 'AI运动伙伴/会议与纪要/', 'apps/')) or p.parent == ROOT or p.name == 'AGENTS.md')

def version(text, name):
    m = re.search(r'(?i)(?:^|[_\s])v(\d+)\.(\d+)(?:\.(\d+))?', name)
    if not m:
        m = re.search(r'(?i)\bv(\d+)\.(\d+)(?:\.(\d+))?', text[:800])
    return tuple(int(x or 0) for x in m.groups()) if m else None

def fmt(v):
    return 'v' + '.'.join(map(str, v))

def bootstrap():
    GOV.mkdir(parents=True, exist_ok=True)
    paths = inventory()
    rows = []
    for p in paths:
        text = p.read_text(encoding='utf-8-sig')
        v = version(text, p.name)
        dates = re.findall(r'20\d{2}[-/]\d{2}[-/]\d{2}|20\d{6}', p.name + '\n' + text[:1200])
        date = dates[0] if dates else '待核实（无可靠创建日期）'
        if re.fullmatch(r'20\d{6}', date):
            date = date[:4] + '-' + date[4:6] + '-' + date[6:]
        review = bool(re.search(r'评审稿|待评审|Review|REVIEW|评审记录', p.name + text[:600]))
        rows.append(dict(path=p.relative_to(ROOT).as_posix(), core=core(p), existing_version=fmt(v) if v else None,
                         document_control=bool(re.search(r'^# Document Control\s*$', text, re.M)),
                         version_history=bool(re.search(r'^# Version History\s*$', text, re.M)),
                         legacy_history=bool(re.search(r'^#{1,3} .*?(版本记录|版本历史|变更记录)', text, re.M)),
                         change_summary='Change Summary' in text, created_date=date,
                         old_version=fmt(v or (0, 1, 0)), new_version=fmt((v[0], v[1], v[2]+1) if v else (0, 1, 1)),
                         status='Review' if review else 'Draft', sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    targets = [r for r in rows if r['core'] and not r['document_control']]
    backup = GOV / 'baseline-before-document-control-20261012.zip'
    if backup.exists():
        raise RuntimeError('Baseline already exists; refusing to overwrite')
    with zipfile.ZipFile(backup, 'w', zipfile.ZIP_DEFLATED) as z:
        for r in targets:
            z.write(ROOT / r['path'], r['path'])
    (GOV / 'audit-before-20261012.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
    # Persist the impact analysis before modifying any source document.
    impact = '# Change Impact\n\nDate: ' + DATE + '\n\n### Modified Sections\n\n- Section: 所有登记核心文档的文档控制与治理附录。\n- Before: 版本多在文件名或正文；标准控制表、统一历史和影响记录不完整。\n- After: 顶部控制表；基线登记与本次 Patch 记录；影响分析；Decision Log 入口。原正文及既有历史原样保留。\n\n### Impact Scope\n\nAffected:\n- PRD / Feature Spec / Functional Outline\n- UX Flow / Hardware Requirement / Technical Requirement\n- Competitor Analysis / Meeting Summary\n- 项目导航与 Agent 规则\n\n### Risk\n\nLow（正文保持；审批及历史事实不补造）。原文件备份见 baseline-before-document-control-20261012.zip；SHA256见 audit-before-20261012.json。\n\n| Document | Old | New | Change Type | Changes |\n|---|---|---|---|---|\n'
    for r in targets:
        impact += f"| [{r['path']}](../../{r['path']}) | {r['old_version']} | {r['new_version']} | Patch | 新增控制表、基线登记、影响记录及决策入口；保留原业务正文 |\n"
    (GOV / 'CHANGELOG-20261012.md').write_text(impact, encoding='utf-8')
    for r in targets:
        p = ROOT / r['path']
        old = p.read_text(encoding='utf-8-sig')
        dtype = 'Project Documentation'
        for key, label in [('hardware', 'Hardware Requirement / Research'), ('requirements', 'Feature Specification / UX Flow'), ('planning', 'Product Planning'), ('design', 'UX Design / Research'), ('会议', 'Meeting Summary'), ('竞品', 'Competitor Analysis')]:
            if key in r['path']: dtype = label
        header = f"""# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | {dtype} |
| Current Version | {r['new_version']} |
| Status | {r['status']} |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | {r['created_date']} |
| Last Updated | {DATE} |

> 文档控制版本以本表为准；原文件名和正文版本标识保留为历史业务版本。Draft/Review 为本次治理提交状态，非产品审批结论。创建日期取自原标识，待 Owner 核实。

"""
        appendix = f"""

---

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| {r['old_version']} | 待核实 | 原作者待核实 | 待核实 | 登记导入前现存正文基线；{'已有版本标识，既有版本记录仍保留在正文' if r['existing_version'] else '无版本标识，治理初始化编号，不代表历史首次发布'}；不推断历史修改或批准 |
| {r['new_version']} | {DATE} | Codex（AI，执行用户指令） | {r['status']} | 新增 Document Control、标准 Version History、Change Impact 与 Decision Log；保留既有业务正文及历史记录 |

> 本表仅登记已验证的现存基线与本次修改。历史日期、作者和状态待核实；原有版本记录是补录证据入口，不能据文件名编造缺失版本。

# Change Impact

### Modified Sections

- Section: 文档顶部与治理附录。
- Before: 缺少统一的文档控制表和标准版本记录。
- After: 增加控制表、基线与 Patch 历史、影响分析和决策记录入口；原业务正文保留。

### Impact Scope

Affected:
- 本文及引用本文的项目文档；本次无业务要求变更。
- 逐文件版本、备份和修改报告见 docs/governance/CHANGELOG-20261012.md。

### Risk

Low。Owner、Reviewer、历史审批状态仍待确认；本次结构治理不冻结产品需求。

# Decision Log

本次未修改产品方向、功能取舍或系统架构。既有决策及待决事项保留在正文，尚未逐条验证迁入；后续涉及这些事项时按 docs/governance/DOCUMENT_VERSION_POLICY.md 记录，建议与已批准决策必须区分。
"""
        p.write_text(header + old + appendix, encoding='utf-8')
    (GOV / 'managed-documents.json').write_text(json.dumps([r['path'] for r in targets], ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'scanned': len(rows), 'modified': len(targets), 'with_version': sum(bool(r['existing_version']) for r in rows if r['core']), 'with_legacy_history': sum(r['legacy_history'] for r in rows if r['core'])}, ensure_ascii=False))

def check():
    paths = json.loads((GOV / 'managed-documents.json').read_text(encoding='utf-8'))
    paths += [p.relative_to(ROOT).as_posix() for p in GOV.glob('*.md')]
    errors = []
    for name in paths:
        text = (ROOT / name).read_text(encoding='utf-8-sig')
        text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)
        for heading in ['Document Control', 'Version History', 'Change Impact', 'Decision Log']:
            if not re.search(r'^# '+heading+r'\s*$', text, re.M): errors.append(f'{name}: missing {heading}')
        m = re.search(r'\| Current Version \| (v\d+\.\d+\.\d+) \|', text)
        date = re.search(r'\| Last Updated \| (\d{4}-\d{2}-\d{2}) \|', text)
        hist = text.split('# Version History', 1)[-1].split('\n# ', 1)[0]
        versions = re.findall(r'^\| (v\d+\.\d+\.\d+) \| ([^|]+) \|', hist, re.M)
        if not m or not versions or versions[-1][0] != m.group(1): errors.append(f'{name}: current/history mismatch')
        if not date or not versions or versions[-1][1].strip() != date.group(1): errors.append(f'{name}: updated/history date mismatch')
    print('\n'.join(errors) if errors else f'PASS: {len(paths)} documents; required sections, version and date consistency')
    return bool(errors)

if __name__ == '__main__':
    if '--bootstrap' in sys.argv: bootstrap()
    else: sys.exit(check())
