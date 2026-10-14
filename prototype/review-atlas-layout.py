"""Static SVG geometry review; no browser or interaction automation."""
from pathlib import Path
import re,json,xml.etree.ElementTree as E
from PIL import ImageFont
ROOT=Path(__file__).parent/'state-atlas-assets'
NS={'s':'http://www.w3.org/2000/svg'}
font_path=r'C:\Windows\Fonts\msyh.ttc'
results=[]
num=lambda s:list(map(float,re.findall(r'-?\d+(?:\.\d+)?',s)))
def shape_box(g):
    e=g.find('s:path',NS)
    if e is not None:
        a=num(e.get('d',''));xs=a[::2];ys=a[1::2]
    else:
        e=g.find('s:polygon',NS)
        if e is None:return None
        a=num(e.get('points',''));xs=a[::2];ys=a[1::2]
    return min(xs),min(ys),max(xs),max(ys)
def intersects(p,r):return r[0]+1<p[0]<r[2]-1 and r[1]+1<p[1]<r[3]-1
for path in ROOT.glob('*.svg'):
    root=E.fromstring(path.read_text(encoding='utf-8'));nodes={};clips=[];hits=[]
    for g in root.findall('.//s:g',NS):
        if 'node' not in g.get('class','').split():continue
        title=g.find('s:title',NS);box=shape_box(g)
        if title is None or box is None:continue
        nodes[title.text]=box
        for t in g.findall('.//s:text',NS):
            text=''.join(t.itertext());size=int(round(float(t.get('font-size','15'))));font=ImageFont.truetype(font_path,size)
            w=font.getlength(text);x=float(t.get('x','0'));y=float(t.get('y','0'));anchor=t.get('text-anchor','start');left=x-w/2 if anchor=='middle' else x-w if anchor=='end' else x
            bb=font.getbbox(text,anchor='ls');top=y+bb[1];bottom=y+bb[3]
            if left<box[0]-.5 or left+w>box[2]+.5 or top<box[1]-.5 or bottom>box[3]+.5:clips.append(text)
    for g in root.findall('.//s:g',NS):
        if g.get('class')!='edge':continue
        title=g.find('s:title',NS);ep=g.find('s:path',NS)
        if title is None or ep is None:continue
        source,target=title.text.split('->');a=num(ep.get('d',''));pts=list(zip(a[::2],a[1::2]));curve=[]
        if not pts:continue
        prior=pts[0]
        for i in range(1,len(pts)-2,3):
            p1,p2,p3=pts[i:i+3]
            for j in range(31):
                t=j/30;u=1-t;curve.append((u**3*prior[0]+3*u*u*t*p1[0]+3*u*t*t*p2[0]+t**3*p3[0],u**3*prior[1]+3*u*u*t*p1[1]+3*u*t*t*p2[1]+t**3*p3[1]))
            prior=p3
        for name,box in nodes.items():
            if name in [source,target]:continue
            if any(intersects(pt,box) for pt in curve):hits.append(title.text+' through '+name)
    results.append({'graph':path.stem,'visibleNodes':len(nodes),'textOutsideNodes':clips,'edgesThroughOtherNodes':hits})
summary={'method':'Static SVG with Microsoft YaHei font measurements and sampled cubic paths; not a browser or human comprehension test','graphs':len(results),'textClips':sum(len(r['textOutsideNodes']) for r in results),'edgeNodeIntersections':sum(len(r['edgesThroughOtherNodes']) for r in results),'details':results}
(ROOT/'static-review.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='details'},ensure_ascii=False))
for r in results:
    if r['textOutsideNodes'] or r['edgesThroughOtherNodes']:print(r)
