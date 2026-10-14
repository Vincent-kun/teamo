from pathlib import Path
import json,re,csv
root=Path(__file__).resolve().parent;hw=root.parent
parts=json.loads((root/'components.json').read_text(encoding='utf-8'));plans=json.loads((root/'layout-plans.json').read_text(encoding='utf-8'))
css=re.search(r'<style>(.*?)</style>',(hw/'display-protocol-filter-20261009/template.html').read_text(encoding='utf-8'),re.S).group(1)
css+=' .tabs{display:flex;flex-wrap:wrap;gap:7px;padding:16px 18px}.tabs button{padding:7px 12px;background:white;color:#5c6a7b;border:1px solid #dce2e9;border-radius:4px}.tabs button.active{background:#eaf2fc;color:#1764c0;border-color:#aac7ea}'
css+=' .plans{display:grid;grid-template-columns:1fr;gap:16px;margin:20px 0}.plan{background:white;border:1px solid #dce2e9;border-radius:6px;padding:18px}.plan svg{width:100%;height:auto;display:block}.plan h2{margin:0 0 10px}.plan .size{font-size:22px;color:#1764c0;font-weight:600}.plan p{font-size:12px;color:#627184}'
css+=' .parts-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(245px,1fr));gap:14px;padding:18px}.parts-grid .card{display:flex;flex-direction:column}.card details{margin-top:8px}.missing{min-height:100px;display:flex;align-items:center}.card .dims{font-weight:600;color:#3e536b}.card img{height:160px}.stack{background:#f1f5fa;padding:9px;border-radius:4px;font-size:11px;color:#627184}.support{padding:16px 18px;font-size:12px;color:#5e6f82}@media(max-width:700px){.page-head{flex-wrap:wrap}.page-head .primary{margin-top:4px}}'
css+=' .src-h{font-size:11px;color:#7c8a98;margin:6px 0 2px}.src{margin:0 0 4px;padding-left:16px;font-size:11px;color:#526173}.src li{margin:2px 0}'
css+=' .plain{padding:16px 18px;font-size:13px;color:#3e536b;line-height:1.75}.plain p{margin:8px 0}.plain blockquote{margin:10px 0;padding:10px 14px;background:#eaf2fc;border-left:3px solid #1764c0;border-radius:4px;color:#165aa6}.plain-tbl{width:100%;min-width:0;table-layout:fixed;border-collapse:collapse;margin:10px 0}.plain-tbl th,.plain-tbl td{word-break:break-word}.plain-tbl th,.plain-tbl td{border:1px solid #dce2e9;padding:8px 10px;text-align:left;font-size:12.5px}.plain-tbl th{background:#f1f5fa;color:#182433}'
css+=' .lib{display:grid;grid-template-columns:212px minmax(0,1fr);border:1px solid var(--line);border-radius:6px;background:white;overflow:hidden}.lib-side{border-right:1px solid var(--line);padding:14px 10px;background:#f8fafc}.lib-side .grp{font-size:10px;color:#7c8a98;letter-spacing:1.2px;margin:12px 6px 6px}.lib-cat{display:flex;justify-content:space-between;padding:7px 10px;border-radius:4px;cursor:pointer;color:#526173;font-size:12.5px}.lib-cat:hover{background:#eef3f9}.lib-cat.on{background:#eaf2fc;color:#165aa6;font-weight:600}.fchip{display:inline-block;padding:3px 9px;margin:2px;border:1px solid #dce2e9;border-radius:999px;font-size:11px;color:#526173;cursor:pointer;background:white;user-select:none}.fchip.on{background:#1764c0;color:white;border-color:#1764c0}.fchip[data-dim]{opacity:.45}.lib-cb{display:block;font-size:12px;color:#526173;padding:3px 6px}.lib-bar{display:flex;gap:10px;align-items:center;padding:10px 14px;border-bottom:1px solid var(--line);flex-wrap:wrap}.lib-main{min-width:0}.lib-tbl{width:100%;min-width:0;table-layout:auto;border-collapse:collapse}.lib-tbl th{position:sticky;top:0;background:#f1f5fa;text-align:left;font-size:11px;color:#526173;padding:8px 10px;border-bottom:1px solid var(--line);cursor:pointer;white-space:nowrap;user-select:none;z-index:1}.lib-tbl td{padding:7px 10px;border-bottom:1px solid #eef1f5;font-size:12px;vertical-align:middle}.lib-tbl tr.row{cursor:pointer}.lib-tbl tr.row:hover{background:#f6f9fd}.lib-tbl tr.detail td{background:#f8fafc;font-size:12px;line-height:1.7}.thumb{height:44px;min-width:60px;object-fit:cover;border-radius:3px;border:1px solid var(--line);cursor:zoom-in;display:block}.nothumb{font-size:10px;color:#a5b1bd;white-space:nowrap}.tagc{display:inline-block;font-size:10px;padding:1px 6px;margin:1px;background:#eef3f9;color:#3e536b;border-radius:3px;white-space:nowrap}.vbtn{padding:6px 11px;border:1px solid #dce2e9;background:white;border-radius:4px;cursor:pointer;color:#526173;font-size:12px}.vbtn.on{background:#1764c0;color:white;border-color:#1764c0}.card .tagc{margin:1px 2px 1px 0}@media(max-width:900px){.lib{grid-template-columns:1fr}.lib-side{border-right:0;border-bottom:1px solid var(--line)}}'
css+=' .dwg text{font-family:"Segoe UI","Microsoft YaHei",sans-serif}.dwg .out{fill:#fbfcfe;stroke:#3e536b;stroke-width:.6}.dwg .comp{fill:#e8eef7;stroke:#6080a5;stroke-width:.35}.dwg .scr{fill:#d8ece7;stroke:#4b8b80;stroke-width:.35}.dwg .spk{fill:#f2e6d2;stroke:#a18452;stroke-width:.35}.dwg .bat{fill:#f4dfd2;stroke:#a1745a;stroke-width:.35}.dwg .rfz{stroke:#8a5fb0;stroke-width:.35}.dwg .dash{fill:none;stroke:#8a5fb0;stroke-width:.35;stroke-dasharray:2 1.4}.dwg .cln{stroke:#c0392b;stroke-width:.28;stroke-dasharray:7 2 1.6 2}.dwg .dim{stroke:#5b6b7d;stroke-width:.3;fill:none}.dwg .ext{stroke:#9aa7b4;stroke-width:.22}.dwg .arr{fill:#5b6b7d;stroke:none}.dwg .dimtxt{font-size:6.4px;fill:#182433}.dwg .lbl{font-size:5.4px;fill:#4c5d70}.dwg .vtxt{font-size:5.6px;fill:#42566b}.dwg .cut{stroke:#c0392b;stroke-width:.8}.dwg .vtitle{font-size:7.2px;fill:#182433;font-weight:600}.dwg .tblock{fill:#f1f5fa;stroke:#3e536b;stroke-width:.4}.dwg .ttxt{font-size:5px;fill:#182433}.dwg .tsep{stroke:#3e536b;stroke-width:.3}'

def _hatch(pid):
    return f'<pattern id="{pid}" width="3" height="3" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="3" stroke="#c9a6e0" stroke-width=".55"/></pattern>'

def _hdim(x1,x2,y,txt,ext_from=None):
    s=f'<line class="dim" x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}"/>'
    s+=f'<path class="arr" d="M{x1:.1f},{y:.1f} l6,-2.2 v4.4 z M{x2:.1f},{y:.1f} l-6,-2.2 v4.4 z"/>'
    if ext_from is not None:
        y2=f'{y+2.5:.1f}' if y>=ext_from else f'{y-2.5:.1f}'
        s+=f'<line class="ext" x1="{x1:.1f}" y1="{ext_from:.1f}" x2="{x1:.1f}" y2="{y2}"/><line class="ext" x1="{x2:.1f}" y1="{ext_from:.1f}" x2="{x2:.1f}" y2="{y2}"/>'
    s+=f'<text class="dimtxt" x="{(x1+x2)/2:.1f}" y="{y-2.8:.1f}" text-anchor="middle">{txt}</text>'
    return s

def _vdim(y1,y2,x,txt,ext_from=None):
    s=f'<line class="dim" x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}"/>'
    s+=f'<path class="arr" d="M{x:.1f},{y1:.1f} l-2.2,6 h4.4 z M{x:.1f},{y2:.1f} l-2.2,-6 h4.4 z"/>'
    if ext_from is not None:
        x2=f'{x+2.5:.1f}' if x>=ext_from else f'{x-2.5:.1f}'
        s+=f'<line class="ext" x1="{ext_from:.1f}" y1="{y1:.1f}" x2="{x2}" y2="{y1:.1f}"/><line class="ext" x1="{ext_from:.1f}" y1="{y2:.1f}" x2="{x2}" y2="{y2:.1f}"/>'
    s+=f'<text class="dimtxt" transform="rotate(-90 {x-2.8:.1f} {(y1+y2)/2:.1f})" x="{x-2.8:.1f}" y="{(y1+y2)/2:.1f}" text-anchor="middle">{txt}</text>'
    return s

def svg(p):
    w,h,d=p['w'],p['h'],p['d'];cr=p['corner_radius'];wall=p['wall']
    sw,sh,st=p['screen'];spw,sph,spt=p['speaker'];bw,bh,bt=p['battery'];pw,ph,pt=p['pcb']
    rnd_spk=(spw==sph);rnd_scr=abs(sw-sh)<0.5
    top=34;fx=26;bot=top+h
    side_x=fx+w+54;back_x=side_x+d+54
    W0=back_x+w+24;H0=bot+72
    row1=bot+15;row2=bot+24;row3=bot+32;yD=bot+41;tleg=bot+48;tb=bot+54
    g=['<svg class="dwg" viewBox="0 0 %.0f %.0f" role="img" aria-label="%s 制图式排布：正视图、A-A剖切、背视图">'%(W0,H0,p['id']),_hatch(p['id']+'-h')]
    # ===== 正视图 =====
    camx=fx+(w-25)/2;camy=top+4;ccx=camx+12.5;ccy=camy+12.5
    scrx=fx+(w-sw)/2;scry=top+32
    spkx=fx+(w-spw)/2;spky=bot-4-sph
    scx=fx+w/2;scy=spky+sph/2
    g.append(f'<rect class="out" x="{fx}" y="{top}" width="{w}" height="{h}" rx="{cr}"/>')
    # 相机：PCB + 同心镜头 + 4 安装孔
    g.append(f'<rect class="comp" x="{camx:.1f}" y="{camy}" width="25" height="24" rx="1"/>')
    g.append(f'<circle cx="{ccx:.1f}" cy="{ccy:.1f}" r="8" fill="#c9d8ee" stroke="#6080a5" stroke-width=".35"/>')
    g.append(f'<circle cx="{ccx:.1f}" cy="{ccy:.1f}" r="5.4" fill="#93a9c8" stroke="#6080a5" stroke-width=".3"/>')
    g.append(f'<circle cx="{ccx:.1f}" cy="{ccy:.1f}" r="2.9" fill="#1d3348"/>')
    for hx,hy in ((camx+2.6,camy+2.6),(camx+22.4,camy+2.6),(camx+2.6,camy+21.4),(camx+22.4,camy+21.4)):
        g.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="1.1" fill="#fbfcfe" stroke="#6080a5" stroke-width=".3"/>')
    # 屏：圆屏=方模块+虚线显示圆；方屏=模块+虚线有效区
    if rnd_scr:
        g.append(f'<rect class="scr" x="{scrx:.1f}" y="{scry}" width="{sw:.1f}" height="{sh:.1f}" rx="3"/>')
        dr=min(sw,sh)/2-4.5
        g.append(f'<circle class="dash" cx="{scrx+sw/2:.1f}" cy="{scry+sh/2:.1f}" r="{dr:.1f}"/>')
        g.append(f'<text class="lbl" text-anchor="middle" x="{scrx+sw/2:.1f}" y="{scry+sh/2-2:.1f}">显示圆Ø待核</text>')
    else:
        g.append(f'<rect class="scr" x="{scrx:.1f}" y="{scry}" width="{sw:.1f}" height="{sh:.1f}" rx="1.5"/>')
        g.append(f'<rect class="dash" x="{scrx+3:.1f}" y="{scry+3:.1f}" width="{sw-6:.1f}" height="{sh-6:.1f}"/>')
        g.append(f'<text class="lbl" text-anchor="middle" x="{scrx+sw/2:.1f}" y="{scry+sh/2-2:.1f}">有效区待核</text>')
    # 喇叭：圆形=振膜同心圆+两侧安装耳；椭圆=同心椭圆
    if rnd_spk:
        g.append(f'<circle cx="{scx:.1f}" cy="{scy:.1f}" r="{spw/2:.1f}" fill="#f2e6d2" stroke="#a18452" stroke-width=".4"/>')
        g.append(f'<circle cx="{scx:.1f}" cy="{scy:.1f}" r="{spw*0.36:.1f}" fill="#e7d3b3" stroke="#a18452" stroke-width=".3"/>')
        g.append(f'<circle cx="{scx:.1f}" cy="{scy:.1f}" r="{spw*0.15:.1f}" fill="#6b5330"/>')
        g.append(f'<rect class="spk" x="{scx-spw/2-2.5:.1f}" y="{scy-1.5:.1f}" width="2.5" height="3"/>')
        g.append(f'<rect class="spk" x="{scx+spw/2:.1f}" y="{scy-1.5:.1f}" width="2.5" height="3"/>')
    else:
        g.append(f'<ellipse cx="{scx:.1f}" cy="{scy:.1f}" rx="{spw/2:.1f}" ry="{sph/2:.1f}" fill="#f2e6d2" stroke="#a18452" stroke-width=".4"/>')
        g.append(f'<ellipse cx="{scx:.1f}" cy="{scy:.1f}" rx="{spw*0.32:.1f}" ry="{sph*0.32:.1f}" fill="#e7d3b3" stroke="#a18452" stroke-width=".3"/>')
        g.append(f'<ellipse cx="{scx:.1f}" cy="{scy:.1f}" rx="{spw*0.13:.1f}" ry="{sph*0.16:.1f}" fill="#6b5330"/>')
    # 中心线
    g.append(f'<line class="cln" x1="{fx+w/2:.1f}" y1="{top-12}" x2="{fx+w/2:.1f}" y2="{bot+10}"/>')
    g.append(f'<line class="cln" x1="{camx-6:.1f}" y1="{ccy:.1f}" x2="{camx+31:.1f}" y2="{ccy:.1f}"/>')
    g.append(f'<line class="cln" x1="{spkx-8:.1f}" y1="{scy:.1f}" x2="{scx+spw/2+8:.1f}" y2="{scy:.1f}"/>')
    # 标注
    g.append(_hdim(fx,fx+w,bot+15,'%g'%w,ext_from=bot))
    g.append(_vdim(top,bot,fx-14,'%g'%h,ext_from=fx))
    g.append(_hdim(scrx,scrx+sw,scry-2,'%g'%sw,ext_from=scry))
    g.append(_vdim(scry,scry+sh,scrx+sw+9,'%g'%sh,ext_from=scrx+sw))
    g.append(_hdim(spkx,spkx+spw,bot-2,'%g'%spw,ext_from=spky+sph))
    g.append(f'<line class="ext" x1="{camx+25:.1f}" y1="{camy+6}" x2="{camx+32:.1f}" y2="{top-2}"/><text class="lbl" x="{camx+33:.1f}" y="{top-3}">CAM 25×24</text>')
    g.append(f'<line class="ext" x1="{fx+w-10.6:.1f}" y1="{top+10.6}" x2="{fx+w+9:.1f}" y2="{top-6}"/><text class="lbl" x="{fx+w+10:.1f}" y="{top-7}">R{cr}</text>')
    ax=fx+w/2
    g.append(f'<line class="cut" x1="{ax:.1f}" y1="{top-14}" x2="{ax:.1f}" y2="{top-10}"/><line class="cut" x1="{ax:.1f}" y1="{bot+5}" x2="{ax:.1f}" y2="{bot+9}"/>')
    g.append(f'<text class="lbl" x="{ax+3.5:.1f}" y="{top-11}">A</text><text class="lbl" x="{ax+3.5:.1f}" y="{bot+8.5}">A</text>')
    g.append(f'<text class="vtitle" x="{fx}" y="14">正视图 FRONT</text>')
    # ===== 侧视 A-A 剖视 =====
    sx=side_x;cy=top+h/2
    chain=[('壁',wall,False),('屏',st,True),('隙',1,True),('板',pt,True),('隔',2,True),('池',bt,False),('撑',2,True)]
    used=wall+st+1+pt+2+bt+2+wall
    rem=d-used
    chain.append(('余',rem,True));chain.append(('壁',wall,False))
    bounds=[sx];x=sx;rects=[];nn=0
    for name,val,asm in chain:
        if name=='壁': rects.append(('out',x,top,wall,h,None))
        elif name=='屏': rects.append(('scr',x,cy-sh/2,st,sh,'屏'))
        elif name=='板': rects.append(('comp',x,cy-ph/2,pt,ph,'板'))
        elif name=='池': rects.append(('bat',x,cy-bh/2,bt,bh,'池'))
        x+=val;bounds.append(x)
    for cls,rx,ry,rw,rh,vl in rects:
        if cls=='out':
            g.append(f'<rect class="{cls}" x="{rx:.1f}" y="{ry:.1f}" width="{rw:.1f}" height="{rh:.1f}"/>')
        elif cls=='scr':
            g.append(f'<rect class="{cls}" x="{rx:.1f}" y="{ry:.1f}" width="{rw:.1f}" height="{rh:.1f}" rx="1.5"/>')
        elif cls=='comp':
            g.append(f'<rect class="{cls}" x="{rx:.1f}" y="{ry:.1f}" width="{rw:.1f}" height="{rh:.1f}"/>')
            g.append(f'<rect x="{rx+rw/2-5.5:.1f}" y="{ry+rh/2-5.5:.1f}" width="11" height="11" fill="#cfdeef" stroke="#6080a5" stroke-width=".3"/>')
            g.append(f'<rect x="{rx+1.5:.1f}" y="{ry+3:.1f}" width="6" height="3" fill="#b9cbe4" stroke="#6080a5" stroke-width=".25"/>')
            g.append(f'<rect x="{rx+1.5:.1f}" y="{ry+rh-6:.1f}" width="8" height="3" fill="#b9cbe4" stroke="#6080a5" stroke-width=".25"/>')
        elif cls=='bat':
            g.append(f'<rect class="{cls}" x="{rx:.1f}" y="{ry:.1f}" width="{rw:.1f}" height="{rh:.1f}" rx="2"/>')
            g.append(f'<rect x="{rx+rw/2-6:.1f}" y="{ry-1.8:.1f}" width="4.5" height="1.8" fill="#d9c4b4" stroke="#a1745a" stroke-width=".25"/>')
            g.append(f'<rect x="{rx+rw/2+1.5:.1f}" y="{ry-1.8:.1f}" width="4.5" height="1.8" fill="#d9c4b4" stroke="#a1745a" stroke-width=".25"/>')
        if vl: g.append(f'<text class="vtxt" transform="rotate(-90 {rx+rw/2+2:.1f} {ry+rh/2:.1f})" x="{rx+rw/2+2:.1f}" y="{ry+rh/2:.1f}" text-anchor="middle">{vl}</text>')
    g.append(f'<rect class="dash" x="{sx+wall:.1f}" y="{top+4}" width="24" height="24"/>')
    g.append(f'<circle class="dash" cx="{sx+wall+4.5:.1f}" cy="{top+16}" r="4"/>')
    g.append(f'<text class="lbl" x="{sx+wall+26:.1f}" y="{top+10}">CAM深≈24(假设)</text>')
    for b in bounds[1:-1]:
        g.append(f'<line class="ext" x1="{b:.1f}" y1="{bot:.1f}" x2="{b:.1f}" y2="{yD+2.5:.1f}"/>')
    for i,(name,val,asm) in enumerate(chain):
        b0,b1=bounds[i],bounds[i+1]
        t=(('~' if asm else '')+'%g'%val)
        if val<6:
            g.append(f'<line class="dim" x1="{b0-9:.1f}" y1="{row1:.1f}" x2="{b1+9:.1f}" y2="{row1:.1f}"/>')
            g.append(f'<path class="arr" d="M{b0:.1f},{row1:.1f} l-6,-2.2 v4.4 z M{b1:.1f},{row1:.1f} l6,-2.2 v4.4 z"/>')
            yr=row2 if nn%2==0 else row3; nn+=1
            g.append(f'<text class="dimtxt" x="{(b0+b1)/2:.1f}" y="{yr-2.4:.1f}" text-anchor="middle">{t}</text>')
        else:
            g.append(_hdim(b0,b1,row1,t))
    g.append(_hdim(sx,sx+d,yD,'%g'%d,ext_from=bot))
    g.append(f'<text class="lbl" x="6" y="{tleg}">链序 壁-屏-隙-板-隔-池-撑-余-壁 ｜ 壁=打印壁，隙=装配隙，隔=RF隔离，池=电池（上方小耳=极耳），撑=支撑，余=造型余量</text>')
    g.append(f'<text class="vtitle" x="{sx}" y="14">侧视剖切 A–A</text>')
    # ===== 背视图 =====
    bx=back_x
    g.append(f'<rect class="out" x="{bx}" y="{top}" width="{w}" height="{h}" rx="{cr}"/>')
    ltew=20;ltex=bx+w-2-ltew
    g.append(f'<rect class="rfz" x="{ltex:.1f}" y="{top+2}" width="{ltew}" height="{h-4:.1f}" style="fill:url(#{p["id"]}-h)"/>')
    g.append(f'<text class="vtxt" transform="rotate(-90 {ltex+ltew/2:.1f} {top+h/2:.1f})" x="{ltex+ltew/2:.1f}" y="{top+h/2:.1f}" text-anchor="middle">LTE天线区</text>')
    g.append(f'<circle cx="{ltex+ltew/2:.1f}" cy="{top+9}" r="1.4" fill="#e8eef7" stroke="#6080a5" stroke-width=".3"/>')
    g.append(f'<text class="lbl" text-anchor="end" x="{ltex+ltew-1.5:.1f}" y="{top+10.4}">IPEX</text>')
    g.append(_hdim(ltex,ltex+ltew,top-8,'~20',ext_from=top+2))
    g.append(f'<text class="lbl" text-anchor="end" x="{ltex+ltew:.1f}" y="{top-14}">净空待审图</text>')
    g.append(f'<rect class="rfz" x="{bx+4}" y="{top+4}" width="14" height="14" style="fill:url(#{p["id"]}-h)"/>')
    g.append(f'<path d="M{bx+7},{top+8} h5 v2.5 h-3 v3 h5" fill="none" stroke="#6080a5" stroke-width=".45"/>')
    g.append(f'<text class="lbl" x="{bx+20}" y="{top+14}">Wi-Fi FPC</text>')
    # 声腔与喇叭（背视投影）居中，USB-C/SIM 移到左下避开声腔
    cav_cy=bot-18
    if rnd_spk:
        g.append(f'<circle class="dash" cx="{bx+w/2:.1f}" cy="{cav_cy:.1f}" r="17.5"/>')
        g.append(f'<circle class="dash" cx="{bx+w/2:.1f}" cy="{cav_cy:.1f}" r="{spw/2:.1f}"/>')
        g.append(f'<text class="lbl" x="{bx+w/2-18:.1f}" y="{cav_cy-19.5:.1f}">声腔禁占Ø35(试验)</text>')
    else:
        g.append(f'<ellipse class="dash" cx="{bx+w/2:.1f}" cy="{bot-16:.1f}" rx="17.5" ry="15"/>')
        g.append(f'<ellipse class="dash" cx="{bx+w/2:.1f}" cy="{bot-16:.1f}" rx="{spw/2:.1f}" ry="{sph/2:.1f}"/>')
        g.append(f'<text class="lbl" x="{bx+w/2-18:.1f}" y="{bot-34:.1f}">声腔禁占35×30(试验)</text>')
    g.append(f'<rect class="comp" x="{bx+2.5:.1f}" y="{bot-8:.1f}" width="9" height="3.5" rx="1.6"/>')
    g.append(f'<ellipse cx="{bx+7:.1f}" cy="{bot-6.2:.1f}" rx="2.6" ry="0.85" fill="#2b3f55"/>')
    g.append(f'<line class="ext" x1="{bx+7:.1f}" y1="{bot-4:.1f}" x2="{bx+7:.1f}" y2="{bot+3}"/><text class="lbl" x="{bx+1:.1f}" y="{bot+8}">USB-C</text>')
    g.append(f'<rect class="comp" x="{bx+2.5:.1f}" y="{bot-25:.1f}" width="12" height="11" rx="1"/>')
    g.append(f'<circle cx="{bx+4.6:.1f}" cy="{bot-22.9:.1f}" r="0.7" fill="#2b3f55"/>')
    g.append(f'<text class="lbl" x="{bx+2.5:.1f}" y="{bot-11.5:.1f}">SIM</text>')
    g.append(f'<text class="vtitle" x="{bx}" y="14">背视图 BACK</text>')
    # ===== 标尺 =====
    sbx=W0-58;sby=bot+10
    g.append(f'<line class="dim" x1="{sbx}" y1="{sby}" x2="{sbx+20}" y2="{sby}"/>')
    for i in range(5):
        g.append(f'<line class="dim" x1="{sbx+i*5}" y1="{sby-2}" x2="{sbx+i*5}" y2="{sby+2}"/>')
    g.append(f'<text class="dimtxt" x="{sbx}" y="{sby-3.4}" text-anchor="middle">0</text><text class="dimtxt" x="{sbx+10}" y="{sby-3.4}" text-anchor="middle">10</text><text class="dimtxt" x="{sbx+20}" y="{sby-3.4}" text-anchor="middle">20</text>')
    g.append(f'<text class="lbl" text-anchor="end" x="{sbx-3}" y="{sby+1.8}">标尺 mm</text>')
    # ===== 图签 =====
    g.append(f'<rect class="tblock" x="6" y="{tb}" width="{W0-12:.0f}" height="14"/>')
    x1=W0*0.28;x2=W0*0.68
    g.append(f'<line class="tsep" x1="{x1:.0f}" y1="{tb}" x2="{x1:.0f}" y2="{tb+14}"/><line class="tsep" x1="{x2:.0f}" y1="{tb}" x2="{x2:.0f}" y2="{tb+14}"/>')
    g.append(f'<text class="ttxt" x="9" y="{tb+9}">方案 {p["id"]} · {p["title"]}</text>')
    g.append(f'<text class="ttxt" x="{x1+3:.0f}" y="{tb+9}">单位 mm · 第一角 · 下限 脸{p["front_min"]:.2f}/深{p["depth_min"]:.2f}</text>')
    g.append(f'<text class="ttxt" x="{x2+3:.0f}" y="{tb+9}">{p["status"]}；~为假设</text>')
    g.append('</svg>')
    return ''.join(g)


plain=(root/'方案速览_通俗版.md').read_text(encoding='utf-8')
def _md2html(t):
    out=[];table=[]
    def flush():
        if table:
            out.append('<table class="plain-tbl">'+table[0]+'</table>');table.clear()
    def inline(x):
        x=x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',x)
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

planhtml=''
for p in plans:
 planhtml+=f'''<article class="plan"><h2>{p['id']} · {p['title']}</h2><div class="size">{p['w']} × {p['h']} × {p['d']} mm</div><p>W左右 × H上下 × D前后（外形包络）</p>{svg(p)}<div class="stack">前脸下限 {p['front_min']:.2f}mm / 深度栈下限 {p['depth_min']:.2f}mm<br>外接盒体积 {p['box_volume_cm3']:.1f}cm³ / R15圆角估计 {p['rounded_estimate_cm3']:.1f}cm³</div><p>{p['notes']}</p><details class="row-detail"><summary>尺寸为什么这样定</summary>H≈1.618W，D≈W/1.618，向0.1mm工程讨论尺度取整；先满足硬件下限再套比例。前脸=24相机+{p['screen'][1]}屏+{p['speaker'][1]}喇叭+16间隙/上下安装。深度=屏厚+1间隙+10自研板占位+2隔离+电池厚+2支撑+2×2打印壁（余量为造型量）。屏完整T未知时为预算，不是厂家厚度。中心线/剖切符号按制图惯例绘制，未做3D干涉验证。</details></article>'''
css+=' @media(max-width:700px){.page-head{flex-wrap:wrap}.page-head .primary{margin-top:4px}}'
body='''<header class="shell"><div class="brand">TEAMO <span style="font-size:12px;font-weight:400;margin-left:20px">硬件选型工作台</span></div><div class="shell-note">整机方案讨论 / 2026.10.09</div></header><div class="workspace"><aside><div class="nav-title">HARDWARE WORKSPACE</div><a class="nav-link current" href="index.html">整机候选与排布</a><a class="nav-link" href="../display-protocol-filter-20261009/index.html">显示屏物料库</a><a class="nav-link" href="../battery-selection-20261009/index.html">电池物料库</a><a class="nav-link" href="../rv1106-board-identification-20261009/index.html">主控开发平台</a></aside><main><div class="breadcrumb">硬件研发 / 整机选型 / 空间预算</div><div class="page-head"><div><h1>整机候选与排布</h1><p class="subtitle">真实器件、不同技术路线和未闭环项分开比较。</p></div><a class="primary" href="components.csv" download>导出候选清单 ↓</a></div><div class="notice">不是已冻结BOM：自研PCB42×55×10、部分屏厚、相机24mm安装深度、声腔与射频隔离均为讨论占位。开发板仅验证。尺寸未做3D干涉/热/RF/声学验证；未知包络不强填。</div><section class="metrics"><div class="metric"><div class="metric-label">有来源记录</div><div class="metric-value">__COUNT__</div></div><div class="metric"><div class="metric-label">独立物料类别</div><div class="metric-value">__CATS__</div></div><div class="metric"><div class="metric-label">排布讨论路线</div><div class="metric-value">3</div></div><div class="metric"><div class="metric-label">采购/实测冻结</div><div class="metric-value">待确认</div></div></section>__PLAIN_PANEL__<div class="panel-head"><h2>形态与空间预算</h2><span>正视图 / A–A剖切 / 背视图 · 尺寸按制图惯例标注，带~为假设</span></div><div class="plans">__PLANS__</div><section class="panel"><details class="evidence" open><summary>关键空间决定与不能省略的部件</summary><p>相机在上部前侧，屏幕中部，出音口下部前侧；自研PCB位于屏后、电池在主板后，喇叭后腔单独封闭。相机深度单独避开中部叠层，麦克风远离出音口，避免电池贴热源。</p><p>S1主打Wi-Fi，不能凭63.2mm宽保证内置LTE。S2为LTE留侧壁区域：42mm主板＋20mm FXP14天线区域＋10mm试验隔离＋4mm双侧壁=76mm，故取76.4mm外宽。10mm是审图前假设，不是FXP14厂家保证。S3若也采用这个射频区，则73.2mm宽不足，须放大到S2宽度或改变板/天线布局。</p><p>FXP14实体70×20×0.2mm，不等于天线安装只需0.2mm。Wi-Fi/LTE隔离、线材走向、接地、匹配网络与塑料介电要审图和实测。圆屏背板是方形板框，不把显示圆直径当外形。</p><p>声腔试验预留35×30×10mm净空=10.5cm³，另计喇叭、腔壁、密封及振膜距离。上下2W圆喇叭方案比20mm高椭圆喇叭占更多前脸高度，不能把电池或线束塞进声腔。</p><p>还要留：USB-C插拔区、SIM卡座、电池/喇叭插头、CSI/FPC弯折、麦克风声孔、按键/指示灯、螺柱/热熔螺母、绝缘、散热与屏窗口固定。接头/开关/螺母已建候选池（连接器与结构 CN01–CN30），尺寸以各候选规格书为准。</p><p><a href="整机排布与尺寸决策.md">逐项依据、误差与验证顺序</a> · <a href="../喇叭选型与音腔空间决策_20261009.md">喇叭与声腔研究</a> · <a href="../天线选型与布置依据_20261009.md">天线与频段研究</a> · <a href="../全品类补全_20261009/全品类补全总览.md">全品类补全研究（A–F 工作包）</a></p></details></section><section class="panel"><div class="panel-head"><h2>全品类候选库</h2><span>后台式筛选：类别 / 接口特性 / 有图无图 · 默认表格视图，点行看详情</span></div><div class="lib"><aside class="lib-side" id="libSide"></aside><div class="lib-main"><div class="lib-bar"><input id="libSearch" class="search" placeholder="搜索型号、厂商、接口或缺项" aria-label="搜索候选"><span id="libCount" class="small"></span><span style="flex:1"></span><button class="vbtn on" data-view="table">表格视图</button><button class="vbtn" data-view="cards">卡片视图</button></div><div id="libContent"></div></div></div></section><footer class="footnote">样件价格不代表国内量产BOM；合作供应商、SDK经验、交期与正式报价均待技术负责人确认。</footer></main></div>'''
script=r'''const parts=JSON.parse(document.getElementById('data').textContent),$=id=>document.getElementById(id),esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const TAGDEF=[['SPI',/\bSPI\b/i],['QSPI',/QSPI/i],['RGB',/\bRGB\b/i],['MIPI',/MIPI/i],['CSI',/\bCSI\b/i],['USB',/USB/i],['I2S',/I2S|I²S/i],['I2C',/I2C|I²C/i],['PDM',/\bPDM\b/i],['UART',/UART/i],['SDIO',/SDIO/i],['LTE',/LTE|Cat\.?1|\b4G\b/i],['Wi-Fi',/Wi-?Fi|WIFI/i],['蓝牙',/蓝牙|BLE|\bBT\b/i],['模拟',/模拟/i],['NTC',/NTC/i],['PCM',/PCM/i],['FPC/FFC',/FPC|FFC/i],['Type-C',/Type-C|USB-C/i],['NVDC',/NVDC/i],['升压',/升压/i],['降压/LDO',/降压|LDO/i],['电量计',/电量计/i],['充电',/充电/i],['保护',/保护/i],['净空',/净空/i],['声腔',/后腔|声腔/i],['FOV/广角',/广角|FOV/i],['热熔螺母',/热熔螺母/i],['密封',/密封|泡棉/]];
function tagsOf(p){const t=(p.model||'')+' '+(p.notes||'');const r=[];for(const[n,re]of TAGDEF){if(re.test(t))r.push(n)}return r}
const state={cat:'全部',q:'',tags:new Set(),img:0,view:'table',open:null,sort:{k:'id',d:1}};
function filtered(){let a=parts.filter(p=>state.cat==='全部'||p.category===state.cat);
 if(state.q){const q=state.q.toLowerCase();a=a.filter(p=>((p.model||'')+' '+(p.notes||'')+' '+(p.manufacturer||'')+' '+(p.id||'')).toLowerCase().includes(q))}
 if(state.img===1)a=a.filter(p=>p.photo);if(state.img===2)a=a.filter(p=>!p.photo);
 if(state.tags.size)a=a.filter(p=>{const tg=tagsOf(p);return[...state.tags].every(t=>tg.includes(t))});
 const{k,d}=state.sort;
 return[...a].sort((x,y)=>{let vx,vy;if(k==='dims'){vx=x.w==null?1e9:x.w;vy=y.w==null?1e9:y.w;return(vx-vy)*d}vx=x[k];vy=y[k];if(vx==null)vx=k==='id'?'':'\uffff';if(vy==null)vy=k==='id'?'':'\uffff';return typeof vx==='string'?vx.localeCompare(vy)*d:(vx-vy)*d})}
function dims(p){return(p.w!=null&&p.h!=null)?`${p.w}×${p.h}×${p.t==null?'?':p.t}`:'待核'}
function thumb(p){return p.photo?`<img class="thumb" src="${esc(p.photo)}" alt="${esc(p.model)}" loading="lazy" data-photo="${esc(p.photo)}">`:`<span class="nothumb">缺图</span>`}
function tagc(p){const t=tagsOf(p);return t.length?t.map(n=>`<span class="tagc">${n}</span>`).join(''):'<span class="nothumb">—</span>'}
function detail(p){return`<tr class="detail"><td colspan="6"><b>适配条件与缺项：</b>${esc(p.notes)}<br><b>价格/供应：</b>${esc(p.price)}${p.photo_note?`<br><b>图注：</b>${esc(p.photo_note)}`:''}${p.sources&&p.sources.length?`<br><b>来源：</b>${p.sources.map(s=>`<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.fact||'来源页')}</a>（${esc(s.date||'')}）`).join(' · ')}`:''}${p.missing&&p.missing.length?`<br><b>缺项：</b>${p.missing.map(m=>esc(m)).join('；')}`:''}</td></tr>`}
function renderTable(a){return`<div style="overflow-x:auto"><table class="lib-tbl"><thead><tr><th data-k="id">ID ${state.sort.k==='id'?(state.sort.d>0?'↑':'↓'):''}</th><th>型号 / 厂商</th><th data-k="dims">尺寸mm ${state.sort.k==='dims'?(state.sort.d>0?'↑':'↓'):''}</th><th>接口 / 特性</th><th>图</th><th>来源</th></tr></thead><tbody>`+a.map(p=>`<tr class="row" data-id="${esc(p.id)}"><td>${esc(p.id)}</td><td><b>${esc(p.model)}</b>${p.manufacturer?` <span class="nothumb">${esc(p.manufacturer)}</span>`:''}</td><td>${dims(p)}</td><td>${tagc(p)}</td><td>${thumb(p)}</td><td><a href="${esc(p.url)}" target="_blank" rel="noopener">↗</a></td></tr>`+(state.open===p.id?detail(p):'')).join('')+`</tbody></table></div>`}
function renderCards(a){return`<div class="parts-grid">`+a.map(p=>`<article class="card"><span class="badge">${esc(p.id)} · ${esc(p.category)}</span><b>${esc(p.model)}</b>${p.photo?`<a href="${esc(p.photo)}" target="_blank"><img src="${esc(p.photo)}" alt="${esc(p.model)}" loading="lazy"></a>`:`<div class="missing">对应型号原图待补；不以近似产品代替</div>`}<p class="dims">${dims(p)} mm</p><div>${tagc(p)}</div><details class="row-detail"><summary>适配条件与缺项</summary>${esc(p.notes)}<p>${esc(p.price)}</p>${p.sources&&p.sources.length?`<p class="src-h">来源（核查日期）：</p><ul class="src">${p.sources.map(s=>`<li><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.fact||'来源页')}</a>（${esc(s.date||'')}）</li>`).join('')}</ul>`:''}${p.missing&&p.missing.length?`<p class="src-h">缺项：</p><ul class="src">${p.missing.map(m=>`<li>${esc(m)}</li>`).join('')}</ul>`:''}</details></article>`).join('')+`</div>`}
function renderSide(){const cats=['全部',...new Set(parts.map(p=>p.category))];const cnt=c=>c==='全部'?parts.length:parts.filter(p=>p.category===c).length;
 const live=new Set();filtered().forEach(p=>tagsOf(p).forEach(t=>live.add(t)));
 $('libSide').innerHTML=`<div class="grp">类别</div>`+cats.map(c=>`<div class="lib-cat${state.cat===c?' on':''}" data-cat="${esc(c)}" role="button" tabindex="0"><span>${esc(c)}</span><span>${cnt(c)}</span></div>`).join('')+`<div class="grp">接口 / 特性</div><div>`+TAGDEF.map(([n])=>`<span class="fchip${state.tags.has(n)?' on':''}" data-tag="${n}"${live.has(n)?'':' data-dim="1"'}>${n}</span>`).join('')+`</div><div class="grp">图片</div><label class="lib-cb"><input type="radio" name="imgf" value="0"${state.img===0?' checked':''}>全部</label><label class="lib-cb"><input type="radio" name="imgf" value="1"${state.img===1?' checked':''}>有图</label><label class="lib-cb"><input type="radio" name="imgf" value="2"${state.img===2?' checked':''}>无图</label><div style="margin-top:12px"><button class="vbtn" id="libReset">重置筛选</button></div>`}
function render(){const a=filtered();$('libCount').textContent=`${a.length} / ${parts.length} 条`;$('libContent').innerHTML=state.view==='table'?renderTable(a):renderCards(a);renderSide();window.systemReview={category:state.cat,count:a.length,view:state.view}}
document.addEventListener('click',e=>{
 const cat=e.target.closest('.lib-cat[data-cat]');if(cat){state.cat=cat.dataset.cat;state.open=null;render();return}
 const chip=e.target.closest('.fchip[data-tag]');if(chip){const t=chip.dataset.tag;state.tags.has(t)?state.tags.delete(t):state.tags.add(t);render();return}
 if(e.target.id==='libReset'){state.cat='全部';state.q='';state.tags.clear();state.img=0;state.open=null;$('libSearch').value='';render();return}
 const th=e.target.closest('th[data-k]');if(th){const k=th.dataset.k;if(state.sort.k===k)state.sort.d*=-1;else state.sort={k,d:1};render();return}
 const row=e.target.closest('tr.row');if(row&&state.view==='table'){state.open=state.open===row.dataset.id?null:row.dataset.id;render();return}
 if(e.target.classList&&e.target.classList.contains('thumb')){window.open(e.target.dataset.photo,'_blank');return}});
document.addEventListener('change',e=>{if(e.target.name==='imgf'){state.img=+e.target.value;render()}});
$('libSearch').oninput=e=>{state.q=e.target.value;render()};
document.querySelectorAll('.vbtn[data-view]').forEach(b=>b.onclick=()=>{state.view=b.dataset.view;document.querySelectorAll('.vbtn[data-view]').forEach(x=>x.classList.toggle('on',x===b));render()});
render();'''
html='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>整机候选与排布 · TEAMO</title><style>'+css+'</style>'+body.replace('__COUNT__',str(len(parts))).replace('__CATS__',str(len(set(p['category'] for p in parts)))).replace('__PLAIN_PANEL__','<section class="panel"><div class="panel-head"><h2>三方案速览</h2><span>给涛哥的可读版 · 尺寸=宽×高×厚</span></div><div class="plain">'+plainhtml+'</div></section>').replace('__PLANS__',planhtml)+'<script type="application/json" id="data">'+json.dumps(parts,ensure_ascii=False).replace('<','\\u003c')+'</script><script>'+script+'</script></html>'
(root/'index.html').write_text(html,encoding='utf-8')
with (root/'components.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['ID','类别','型号','W','H','T','来源','条件/缺项'])
 for p in parts:w.writerow([p['id'],p['category'],p['model'],p['w'],p['h'],p['t'],p['url'],p['notes']])
lines=['# 整机排布与尺寸决策｜2026-10-09','','工程讨论版，非CAD或BOM冻结。尺寸为圆角长方壳W×H×D，不是球体或直径×高。','', '| 方案 | 外包络mm | 前脸下限mm | 深度栈mm | 外接盒体积cm³ |','|---|---|---|---|---|']
for p in plans:lines.append(f"| {p['title']} | {p['w']}×{p['h']}×{p['d']} | {p['front_min']:.2f} | {p['depth_min']:.2f} | {p['box_volume_cm3']:.1f} |")
lines+=['','黄金比例是造型目标：H≈φW、D≈W/φ，0.1mm为讨论精度，不是制造能力。体积是外接盒或R15圆角平面等截面估计，不是内部可用体积；真实胶囊/曲面CAD会变化。','', 'S1：1.69触控屏＋CMS-30204-18L250，主板与2000mAh软包前后层叠；Wi-Fi优先。S2：55×55圆屏＋CMS-28528N-L152，侧壁FXP14；推荐作为LTE空间起点，QSPI/协处理仍是条件。S3：裸圆屏＋1S2P4400mAh包，容量与厚度对照，射频区域不足时增大至S2宽度。','', '相机参考MIS5001B25×24，24mm安装深度暂定；它不是120–130°FOV已确认件。自研PCB42×55×10为工程占位，主控/RAM/eMMC、4G、电源、音频、SIM及连接器全部需布局后验证，不能用模组面积相加证明可布完。','', '打印初值壁厚2mm、螺柱位置待CAD；工艺、材料、方向、翘曲及收缩未知，先打槽/螺柱/卡扣试片再用卡尺测误差。0.3mm装配补偿可作为试片A/B参数，不能当所有工艺通用公差。电池公差采用厂商最大包络，膨胀预留供应商指定。屏框、相机镜头、连接器线缆须各自计误差链。','', '后腔35×30×10mm净空另计腔壁、垫片、5.2mm喇叭厚度与1.5mm前侧试验间隙；前后声路隔离。主板与电池不侵占净空。','', 'LTE布置试验：42PCB＋20天线区＋10隔离＋4壁=76mm；10隔离未得到FXP14厂家保证，RF供应商审图后修改。Wi-Fi需按具体安装配置应用规范的5/10mm等距离审图，不统一写万能5mm。塑料/屏蔽罩/电池/磁铁/螺丝影响调谐。','', '完整系统尚待选：USB-C座（CN01–03）、SIM座（CN05–07）、电池/喇叭接头（CN15–19）、FPC座/线长（CN04/CN29–30）、按键（CN17–18）、麦克风/声孔、NTC/PCM、电量计（PWR14–16）、热路径、屏窗口与密封材料。连接器候选已带真实型号，见全品类补全总览。','', '成本：公开美元价是样件参考，供应商合作、MOQ、芯片/PCB/SMT/NRE、结构打印、声腔、RF调试、物流税费皆未闭环，不能承诺≤2000元。确认是否有现成硬件方案比只选便宜芯片更关键。','', '验证顺序：板型/SDK和网络方式 → 电源平均/峰值 → 屏点亮/触控 → 摄像头/FOV和算法 → 声腔/AEC → RF审图/样机 → CAD干涉 → 打印试片/整机 → 续航与热测试。','', '涛哥讨论：板型/可复用自研板？USB联网使用EC800G具体固件还是Air780ER？合作供应商成熟成品电池/喇叭/天线？是否必须内置4G与断电续航？屏SPI/QSPI实现与SDK经验？功耗/充电热/峰值？哪些型号可以本周拿样？','', '[电池依据](../battery-selection-20261009/电池选型与功耗结构输入.md) · [喇叭依据](../喇叭选型与音腔空间决策_20261009.md) · [天线依据](../天线选型与布置依据_20261009.md) · [全品类补全总览](../全品类补全_20261009/全品类补全总览.md) · 全部来源按组件JSON逐项追溯。']
lines+=['','---','',plain.strip()]
(root/'整机排布与尺寸决策.md').write_text('\n'.join(lines),encoding='utf-8')
print('Built',len(parts),'records /',len(plans),'layout plans')
