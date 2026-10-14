import io,sys,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
s=open('build.py',encoding='utf-8').read()
blk=open('dwg_block.py',encoding='utf-8').read()
old_css=re.search(r"css\+=' \.dwg text\{.*?'\n",s,re.S).group(0)
new_css="""css+=' .dwg text{font-family:"Segoe UI","Microsoft YaHei",sans-serif}.dwg .out{fill:#fbfcfe;stroke:#3e536b;stroke-width:.6}.dwg .comp{fill:#e8eef7;stroke:#6080a5;stroke-width:.35}.dwg .scr{fill:#d8ece7;stroke:#4b8b80;stroke-width:.35}.dwg .spk{fill:#f2e6d2;stroke:#a18452;stroke-width:.35}.dwg .bat{fill:#f4dfd2;stroke:#a1745a;stroke-width:.35}.dwg .rfz{stroke:#8a5fb0;stroke-width:.35}.dwg .dash{fill:none;stroke:#8a5fb0;stroke-width:.35;stroke-dasharray:2 1.4}.dwg .cln{stroke:#c0392b;stroke-width:.28;stroke-dasharray:7 2 1.6 2}.dwg .dim{stroke:#5b6b7d;stroke-width:.3;fill:none}.dwg .ext{stroke:#9aa7b4;stroke-width:.22}.dwg .arr{fill:#5b6b7d;stroke:none}.dwg .dimtxt{font-size:6.4px;fill:#182433}.dwg .lbl{font-size:5.4px;fill:#4c5d70}.dwg .vtxt{font-size:5.6px;fill:#42566b}.dwg .cut{stroke:#c0392b;stroke-width:.8}.dwg .vtitle{font-size:7.2px;fill:#182433;font-weight:600}.dwg .tblock{fill:#f1f5fa;stroke:#3e536b;stroke-width:.4}.dwg .ttxt{font-size:5px;fill:#182433}.dwg .tsep{stroke:#3e536b;stroke-width:.3}'
"""
i=s.index('def _hdim');j=s.index("planhtml=''")
s=s[:i]+blk+'\n'+s[j:]
s=s.replace(old_css,new_css)
open('build.py','w',encoding='utf-8').write(s)
print('spliced ok')
