#!/usr/bin/env python3
"""Build Compound Engineering cheatsheet — PIL rendering with correct sizes.

Layout: PIL image y=0=TOP, y=H=BOTTOM.
PDF embed: PIL y=H → PDF y=0 (page bottom), PIL y=0 → PDF y=PH (page top).
So image BOTTOM = PDF TOP and image TOP = PDF BOTTOM.
Content order in image: Section 3 (TOP) → Section 0 (BOTTOM) → PDF reads 0→3 top→bottom ✓
"""
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as cv
from reportlab.lib.utils import ImageReader
from io import BytesIO

PW, PH = A4[1], A4[0]   # 841.89 × 595.28 pts (landscape)
DPI = 300
W   = round(PW * DPI / 72.0)   # 3508 px
H   = round(PH * DPI / 72.0)   # 2480 px

F_ZH   = '/Users/liubinbin/Library/Fonts/LXGWWenKai-Regular.ttf'
F_MONO = '/Users/liubinbin/Library/Fonts/LXGWWenKaiMono-Regular.ttf'

def font_zh(size_px):   return ImageFont.truetype(F_ZH,   size_px)
def font_mono(size_px): return ImageFont.truetype(F_MONO, size_px)
def ts(f, text):
    b = f.getbbox(text)
    return b[2]-b[0], b[3]-b[1]

NAVY=(26,42,74); BLUE=(59,130,246); BLUE_D=(29,78,216)
VIOLET=(79,70,229); GREEN=(16,185,129); WHITE=(255,255,255)
GRAY_BG=(248,250,252); GRAY_LN=(226,232,240)
GRAY_TXT=(71,85,105); DARK_TXT=(30,41,59)
LT_BLUE=(147,197,253); DK_BG=(15,23,42)

# Layout
HEADER_H=180; FOOTER_H=50
SB_W=28; SB_ACCENT=2
TITLE_FSZ=130; SUB_FSZ=36
SEC_FSZ=56; SEC_EN_FSZ=22
BODY_FSZ=36; PILL_FSZ=32
FOOT_FSZ=20; SB_ZH_FSZ=22; SB_EN_FSZ=16
ROW_H=54; S0=18; S1=22; RULE=2
PPX=14; PPY=8

def pill(d, x, y, text, f, bg, fg):
    tw,th=ts(f,text); r=8
    bx2=x+tw+PPX*2; by2=y+th+PPY*2
    d.rounded_rectangle([x,y,bx2,by2],radius=r,fill=bg)
    d.text((x+PPX,y+PPY//2+1),text,font=f,fill=fg)
    return bx2

def stepc(d, cx, cy, n, color):
    r=18; d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=color)
    f=font_zh(20); s=str(n); sw,sh=ts(f,s)
    d.text((cx-sw//2,cy-sh//2),s,font=f,fill=WHITE)

def hline(d, y, color, w=RULE):
    d.line([(SB_W+28,y),(W-28,y)],fill=color,width=max(1,w))

def rect(d, x, y, w, h, fill):
    d.rectangle([x, y, x+w, y+h], fill=fill)

# ── Rows shared helpers ──────────────────────────────────────────────────
def draw_cycle_row(d, cx0, cw, y, n, cmd, desc, accent, rh=ROW_H):
    """Draw one cycle row BELOW current y, return new y."""
    bg=GRAY_BG if n%2==0 else WHITE
    rect(d, cx0, y, cw, rh, bg)
    scr=18; scc=cx0+28; scy=y+rh//2
    d.ellipse([scc-scr,scy-scr,scc+scr,scy+scr],fill=accent)
    sn_f=font_zh(20); sn=str(n); snw,snh=ts(sn_f,sn)
    d.text((scc-snw//2,scy-snh//2),sn,font=sn_f,fill=WHITE)
    pf=font_mono(PILL_FSZ); pw2,ph2=ts(pf,cmd)
    pill(d,cx0+60,y+(rh-ph2)//2,cmd,pf,BLUE_D,WHITE)
    df=font_zh(BODY_FSZ); dw,dh=ts(df,desc)
    d.text((cx0+60+pw2+40,y+(rh-dh)//2),desc,font=df,fill=DARK_TXT)
    return rh

def draw_ref_row(d, cx0, cw, y, cmd, desc, rh=50):
    """Draw one ref row BELOW current y, return new y."""
    rect(d, cx0, y, cw, rh, WHITE)
    pf=font_mono(PILL_FSZ); pw2,ph2=ts(pf,cmd)
    pill(d,cx0+14,y+(rh-ph2)//2,cmd,pf,DK_BG,WHITE)
    df=font_zh(BODY_FSZ); dw,dh=ts(df,desc)
    d.text((cx0+14+pw2+40,y+(rh-dh)//2),desc,font=df,fill=DARK_TXT)
    return rh

def section_title(d, cx0, y, num_zh, en_text, accent_color, sf, ef, sh2):
    # Rule ABOVE section content (lower y = higher in image/PDF)
    hline(d, y, accent_color)
    d.text((cx0, y), num_zh, font=sf, fill=DARK_TXT); y += sh2+5
    d.text((cx0, y), en_text, font=ef, fill=GRAY_TXT); y += SEC_EN_FSZ+S0
    return y

def install_row(d, cx0, cw, y, cmd, desc):
    rect(d, cx0, y, cw, ROW_H, GRAY_BG)
    pf=font_mono(PILL_FSZ); pw2,ph2=ts(pf,cmd)
    pill(d,cx0+14,y+(ROW_H-ph2)//2,cmd,pf,VIOLET,WHITE)
    df=font_zh(BODY_FSZ); dw,dh=ts(df,desc)
    d.text((cx0+14+pw2+40,y+(ROW_H-dh)//2),desc,font=df,fill=DARK_TXT)
    return ROW_H

def render():
    img=Image.new('RGB',(W,H),WHITE)
    d=ImageDraw.Draw(img)

    # ── Sidebar ──
    rect(d, 0, 0, SB_W, H, NAVY)
    rect(d, SB_W-SB_ACCENT, 0, SB_ACCENT, H, BLUE)
    items=[(H-80,'安装上手','Install'),(H-195,'典型开发周期','Typical Cycle'),
           (H-310,'专注 Bug 调查','Bug Investigation'),(H-425,'命令说明','Command Reference')]
    for sy,zhl,enl in items:
        r=16; cx0=16
        d.ellipse([cx0-r,sy-r,cx0+r,sy+r],fill=BLUE)
        fz=font_zh(SB_ZH_FSZ); d.text((36,sy-SB_ZH_FSZ//2-3),zhl,font=fz,fill=WHITE)
        fe=font_zh(SB_EN_FSZ); d.text((36,sy+SB_EN_FSZ//2+2),enl,font=fe,fill=LT_BLUE)

    # ── Header bar (BOTTOM of image = TOP of PDF) ──
    rect(d, SB_W, H-HEADER_H, W-SB_W, HEADER_H, NAVY)
    tf=font_zh(TITLE_FSZ); ttw,tth=ts(tf,'Compound Engineering')
    d.text((SB_W+36, H-HEADER_H+(HEADER_H-tth)//2), 'Compound Engineering', font=tf, fill=WHITE)
    sf2=font_zh(SUB_FSZ); st='工作流速查卡  |  Workflow Cheatsheet'
    d.text((SB_W+36, H-HEADER_H+(HEADER_H-tth)//2+tth+6), st, font=sf2, fill=LT_BLUE)

    # ── Footer (TOP of image = BOTTOM of PDF) ──
    rect(d, 0, 0, W, FOOTER_H, GRAY_BG)
    d.line([(SB_W,FOOTER_H),(W,FOOTER_H)],fill=GRAY_LN,width=1)
    ft_f=font_zh(FOOT_FSZ); ft='Compound Engineering  ·  Print this and keep it at your desk'
    ftw,fth=ts(ft_f,ft)
    d.text(((W-ftw)//2,(FOOTER_H-fth)//2),ft,font=ft_f,fill=GRAY_TXT)

    # ── Content area ──
    cx0=SB_W+36; cw=W-cx0-28
    y = FOOTER_H + 650  # content starts further down, closer to header

    # Draw in PDF-reading order: Section 3 first (TOP of image), Section 0 last (BOTTOM)
    # PDF order: Section 3 → Section 2 → Section 1 → Section 0 (top→bottom)

    sf=font_zh(SEC_FSZ); ef=font_zh(SEC_EN_FSZ); _,sh2=ts(sf,'0  安装上手')

    # ══ SECTION 3: Command Reference ══
    y = section_title(d, cx0, y, '3  命令说明', 'All /ce-* commands at a glance.', (100,116,139), sf, ef, sh2)
    ref_cmds=[
        ('/ce-brainstorm <idea>', '从自然语言想法启动头脑风暴，产生需求文档。'),
        ('/ce-plan <requirements-doc-path>', '基于需求文档制定执行计划。'),
        ('/ce-work', '执行计划中的任务（自动读取 /ce-plan 输出）。'),
        ('/ce-code-review', '审查所有变更，支持代码质量与安全检查。'),
        ('/ce-compound', '将实验分支合并回主分支，完成工作流。'),
        ('/ce-debug <problem>', '专注调查并修复特定问题，适合 Bug 修复场景。'),
    ]
    for cmd,desc in ref_cmds:
        y += draw_ref_row(d, cx0, cw, y, cmd, desc)
    y += 12; hline(d, y, (100,116,139))

    # ══ SECTION 2: Bug Investigation ══
    y += S1; y = section_title(d, cx0, y, '2  专注 Bug 调查', '专注调查特定问题，然后完成修复。', GREEN, sf, ef, sh2)
    for n,cmd,desc in [
        (1,'/ce-debug "the checkout webhook sometimes creates duplicate invoices"','专注调查 + 修复问题'),
        (2,'/ce-code-review','代码审查'),
        (3,'/ce-compound','合并结果到主分支'),
    ]:
        y += draw_cycle_row(d, cx0, cw, y, n, cmd, desc, GREEN)
    y += 12; hline(d, y, GREEN); y += 14
    ff=font_zh(SEC_EN_FSZ)
    flow2='问题  →  /ce-debug  →  /ce-code-review  →  /ce-compound  →  完成'
    fww,fwh=ts(ff,flow2); d.text((cx0+(cw-fww)//2,y),flow2,font=ff,fill=GRAY_TXT); y += fwh+16
    hline(d, y, GRAY_LN)

    # ══ SECTION 1: Typical Cycle ══
    y += S1; y = section_title(d, cx0, y, '1  典型开发周期', '将粗糙想法转化为需求文档，然后从该文档规划内容再执行。', BLUE, sf, ef, sh2)
    for n,cmd,desc in [
        (1,'/ce-brainstorm "make background job retries safer"','头脑风暴，从粗糙想法开始'),
        (2,'/ce-plan docs/brainstorms/...requirements.md','根据文档制定计划'),
        (3,'/ce-work','执行计划（自动读取 /ce-plan 输出）'),
        (4,'/ce-code-review','代码审查'),
        (5,'/ce-compound','合并结果到主分支'),
    ]:
        y += draw_cycle_row(d, cx0, cw, y, n, cmd, desc, BLUE)
    y += 12; hline(d, y, BLUE); y += 14
    flow='想法  →  /ce-brainstorm  →  /ce-plan  →  /ce-work  →  /ce-code-review  →  /ce-compound  →  完成'
    fww,fwh=ts(ff,flow); d.text((cx0+(cw-fww)//2,y),flow,font=ff,fill=GRAY_TXT); y += fwh+18

    # Stats bar
    bh=52; rect(d, cx0, y, 920, bh, (30,58,95))
    bf=font_zh(50); lf=font_zh(22)
    n36,n51='36','51'
    w36,_=ts(bf,n36); w51,_=ts(bf,n51)
    wsk,_=ts(lf,'Skills'); wsa,_=ts(lf,'Agents')
    mid=90; total=w36+16+wsk+mid+w51+16+wsa
    x0=cx0+(920-total)//2
    bh2,_=ts(bf,n36); d.text((x0,y+(bh-bh2)//2),n36,font=bf,fill=WHITE)
    x0+=w36+16; lh,_=ts(lf,'Skills'); d.text((x0,y+(bh-lh)//2),'Skills',font=lf,fill=LT_BLUE)
    x0+=wsk+mid; bh3,_=ts(bf,n51); d.text((x0,y+(bh-bh3)//2),n51,font=bf,fill=WHITE)
    x0+=w51+16; lh2,_=ts(lf,'Agents'); d.text((x0,y+(bh-lh2)//2),'Agents',font=lf,fill=LT_BLUE)
    y += bh+18
    hline(d, y, GRAY_LN)

    # ══ SECTION 0: Install ══
    y += S1; y = section_title(d, cx0, y, '0  安装上手', 'Install the plugin, then set it up in your project.', VIOLET, sf, ef, sh2)
    for cmd,desc in [
        ('/plugin marketplace add EveryInc/compound-engineering-plugin','在 Plugin Marketplace 添加插件'),
        ('/plugin install compound-engineering','安装插件包'),
        ('/ce-setup','检查环境、安装缺失工具、初始化配置'),
    ]:
        y += install_row(d, cx0, cw, y, cmd, desc)

    print(f"Content top y={y}, header bottom={H-HEADER_H}")
    return img

if __name__ == '__main__':
    print(f"Canvas: {W}x{H} px at {DPI} DPI")
    img=render()
    img.save('/tmp/cheatsheet_preview.png','PNG',dpi=(DPI,DPI))
    print(f"PNG: {img.size}")

    output='/Volumes/StorageMacMini2/liubinbin/Github/lotosbin/agent-harness/docs/compound-engineering-cheatsheet.pdf'
    c=cv.Canvas(output,pagesize=(PW,PH))
    buf=BytesIO()
    img.save(buf,'PNG',dpi=(DPI,DPI))
    buf.seek(0)
    c.drawImage(ImageReader(buf), 0, PH, width=PW, height=-PH,
                preserveAspectRatio=False, mask='auto')
    c.save()
    print(f"PDF: {output}")
