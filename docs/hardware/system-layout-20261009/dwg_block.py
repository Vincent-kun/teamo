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
    g.append(f'<text class="lbl" x="{ltex+ltew/2+2.5:.1f}" y="{top+10.4}">IPEX</text>')
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
    sbx=W0-58;sby=20
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
