# v2：页面正文放 __PLAIN_PANEL__ 占位符，运行时替换
import io,sys,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
s=open('build.py',encoding='utf-8').read()

inject='''
plain=(root/'方案速览_通俗版.md').read_text(encoding='utf-8')
def _md2html(t):
    out=[];table=[]
    def flush():
        if table:
            out.append('<table class="plain-tbl">'+table[0]+'</table>');table.clear()
    def inline(x):
        x=x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        return re.sub(r'\\*\\*(.+?)\\*\\*',r'<b>\\1</b>',x)
    for ln in t.splitlines():
        ln=ln.rstrip()
        if ln.startswith('|'):
            cells=[c.strip() for c in ln.strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?',c) for c in cells): continue
            row=''.join(f'<th>{inline(c)}</th>' if not table else f'<td>{inline(c)}</td>' for c in cells)
            table.append('<tr>'+row+'</tr>');continue
        flush()
        if not ln: continue
        if ln.startswith('> '): out.append('<blockquote>'+inline(ln[2:])+'</blockquote>')
        else: out.append('<p>'+inline(ln)+'</p>')
    flush()
    return ''.join(out)
plainhtml=_md2html(plain)
'''
i=s.index("planhtml=''")
s=s[:i]+inject+'\n'+s[i:]

# body 字符串内插占位符
anchor='<div class="panel-head"><h2>形态与空间预算</h2>'
assert s.count(anchor)==1
s=s.replace(anchor,'__PLAIN_PANEL__'+anchor,1)

# html 组装行追加占位符替换
old=".replace('__CATS__',str(len(set(p['category'] for p in parts))))"
assert old in s
s=s.replace(old,old+".replace('__PLAIN_PANEL__','<section class=\"panel\"><div class=\"panel-head\"><h2>三方案速览</h2><span>给涛哥的可读版 · 尺寸=宽×高×厚</span></div><div class=\"plain\">'+plainhtml+'</div></section>')",1)

# 样式
cssadd="css+=' .plain{padding:16px 18px;font-size:13px;color:#3e536b;line-height:1.75}.plain p{margin:8px 0}.plain blockquote{margin:10px 0;padding:10px 14px;background:#eaf2fc;border-left:3px solid #1764c0;border-radius:4px;color:#165aa6}.plain-tbl{width:100%;border-collapse:collapse;margin:10px 0}.plain-tbl th,.plain-tbl td{border:1px solid #dce2e9;padding:8px 10px;text-align:left;font-size:12.5px}.plain-tbl th{background:#f1f5fa;color:#182433}'"
m=re.search(r"css\+=' \.src-h\{[^']+'",s)
s=s.replace(m.group(0),m.group(0)+'\n'+cssadd)

# 决策MD末尾追加速览
old_tail="(root/'整机排布与尺寸决策.md').write_text('\\n'.join(lines),encoding='utf-8')"
assert old_tail in s
s=s.replace(old_tail,"lines+=['','---','',plain.strip()]\n"+old_tail,1)
open('build.py','w',encoding='utf-8').write(s)
print('patched v2')
