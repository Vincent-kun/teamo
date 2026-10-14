# 候选库后台化改造：替换 body 中目录区块 + 整段 script + 新增样式
import io,sys,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
s=open('build.py',encoding='utf-8').read()
js=open('lib_ui.js',encoding='utf-8').read().rstrip('\n')

# 1 替换目录区块（toolbar/tabs/catalog → lib 布局）
old_block='<div class="toolbar"><input id="search" class="search" placeholder="搜索型号、接口或缺项" aria-label="搜索候选"><span id="summary" class="small"></span></div><div class="tabs" id="categories"></div><div class="parts-grid" id="catalog"></div>'
assert old_block in s
new_block='<div class="lib"><aside class="lib-side" id="libSide"></aside><div class="lib-main"><div class="lib-bar"><input id="libSearch" class="search" placeholder="搜索型号、厂商、接口或缺项" aria-label="搜索候选"><span id="libCount" class="small"></span><span style="flex:1"></span><button class="vbtn on" data-view="table">表格视图</button><button class="vbtn" data-view="cards">卡片视图</button></div><div id="libContent"></div></div></div>'
s=s.replace(old_block,new_block,1)

# 2 面板副标题
s=s.replace('<h2>全品类候选库</h2><span>裸芯/模组/开发板不是同层级产品</span>',
            '<h2>全品类候选库</h2><span>后台式筛选：类别 / 接口特性 / 有图无图 · 默认表格视图，点行看详情</span>',1)

# 3 替换整段 script
i=s.index("script=r'''");j=s.index("'''",i+10)
s=s[:i]+"script=r'''"+js+"'''"+s[j+3:]

# 4 样式
cssadd="css+=' .lib{display:grid;grid-template-columns:212px minmax(0,1fr);border:1px solid var(--line);border-radius:6px;background:white;overflow:hidden}.lib-side{border-right:1px solid var(--line);padding:14px 10px;background:#f8fafc}.lib-side .grp{font-size:10px;color:#7c8a98;letter-spacing:1.2px;margin:12px 6px 6px}.lib-cat{display:flex;justify-content:space-between;padding:7px 10px;border-radius:4px;cursor:pointer;color:#526173;font-size:12.5px}.lib-cat:hover{background:#eef3f9}.lib-cat.on{background:#eaf2fc;color:#165aa6;font-weight:600}.fchip{display:inline-block;padding:3px 9px;margin:2px;border:1px solid #dce2e9;border-radius:999px;font-size:11px;color:#526173;cursor:pointer;background:white;user-select:none}.fchip.on{background:#1764c0;color:white;border-color:#1764c0}.fchip[data-dim]{opacity:.45}.lib-cb{display:block;font-size:12px;color:#526173;padding:3px 6px}.lib-bar{display:flex;gap:10px;align-items:center;padding:10px 14px;border-bottom:1px solid var(--line);flex-wrap:wrap}.lib-main{min-width:0}.lib-tbl{width:100%;min-width:0;table-layout:auto;border-collapse:collapse}.lib-tbl th{position:sticky;top:0;background:#f1f5fa;text-align:left;font-size:11px;color:#526173;padding:8px 10px;border-bottom:1px solid var(--line);cursor:pointer;white-space:nowrap;user-select:none;z-index:1}.lib-tbl td{padding:7px 10px;border-bottom:1px solid #eef1f5;font-size:12px;vertical-align:middle}.lib-tbl tr.row{cursor:pointer}.lib-tbl tr.row:hover{background:#f6f9fd}.lib-tbl tr.detail td{background:#f8fafc;font-size:12px;line-height:1.7}.thumb{height:44px;min-width:60px;object-fit:cover;border-radius:3px;border:1px solid var(--line);cursor:zoom-in;display:block}.nothumb{font-size:10px;color:#a5b1bd;white-space:nowrap}.tagc{display:inline-block;font-size:10px;padding:1px 6px;margin:1px;background:#eef3f9;color:#3e536b;border-radius:3px;white-space:nowrap}.vbtn{padding:6px 11px;border:1px solid #dce2e9;background:white;border-radius:4px;cursor:pointer;color:#526173;font-size:12px}.vbtn.on{background:#1764c0;color:white;border-color:#1764c0}.card .tagc{margin:1px 2px 1px 0}@media(max-width:900px){.lib{grid-template-columns:1fr}.lib-side{border-right:0;border-bottom:1px solid var(--line)}}'"
m=re.search(r"css\+=' \.plain\{[^']+'",s)
assert m
s=s.replace(m.group(0),m.group(0)+'\n'+cssadd)
open('build.py','w',encoding='utf-8').write(s)
print('lib patched')
