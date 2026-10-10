# 生成静态部署副本：.sites-deploy/hardware-workbench/ ← docs/hardware（剔除脚本/抓取源/评审截图/重复PDF）
import io,sys,os,shutil,re,glob
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
SRC=r'D:/work/sportmate/docs/hardware'
DST=r'D:/work/sportmate/.sites-deploy/hardware-workbench'
if os.path.exists(DST): shutil.rmtree(DST)
os.makedirs(DST)
EXCL_EXT={'.py','.cjs','.js'}
def skip(rel):
    parts=rel.replace('/',os.sep).split(os.sep)
    name=os.path.basename(rel)
    if any(p in ('review','__pycache__') for p in parts): return True
    if name.endswith(('.html.source','-source.html')): return True
    if name.startswith('review-') and name.endswith('.png'): return True
    if os.path.splitext(name)[1].lower() in EXCL_EXT: return True
    if rel.replace('/',os.sep).startswith('system-layout-20261009'+os.sep+'assets') and name.startswith('PWR') and name.lower().endswith('.pdf'): return True
    if name=='components.pre_wp_backup_20261009.json': return True
    if name in ('verify.cjs','page-script-check.js'): return True
    return False
n=0;total=0
for r,ds,fs in os.walk(SRC):
    for f in fs:
        sp=os.path.join(r,f); rel=os.path.relpath(sp,SRC)
        if skip(rel): continue
        dp=os.path.join(DST,rel)
        os.makedirs(os.path.dirname(dp),exist_ok=True)
        shutil.copy2(sp,dp); n+=1; total+=os.path.getsize(sp)
print('copied',n,'files,',round(total/1048576,2),'MB')
# 校验：各 index.html 与 MD 里的相对链接目标是否存在
missing=[]
def check(dirbase,text,patterns):
    for m in re.findall(patterns,text):
        t=m.strip()
        if t.startswith(('http','mailto','#','data:')): continue
        t=t.split('#')[0].split('?')[0]
        if not t: continue
        tp=os.path.normpath(os.path.join(dirbase,t))
        if not os.path.exists(tp): missing.append((os.path.relpath(dirbase,DST),t))
for root,ds,fs2 in os.walk(DST):
    for f in fs2:
        p=os.path.join(root,f)
        if f.endswith(('.html','.md')):
            txt=open(p,encoding='utf-8',errors='ignore').read()
            check(root,txt,r'(?:href|src)="([^"]+)"')
            check(root,txt,r'\]\(([^)]+)\)')
print('missing refs:',len(missing))
for x in missing[:15]:print('  ',x)
