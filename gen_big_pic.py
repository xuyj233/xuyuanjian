"""
Programmatic generation of big_pic.png for the academic website.
Uses PIL with proper Chinese font support.
"""
from PIL import Image, ImageDraw, ImageFont
import math
import numpy as np

# ── Canvas ────────────────────────────────────────────────────────────────────
W, H = 1600, 900
img = Image.new("RGB", (W, H), "#f0f4f8")
draw = ImageDraw.Draw(img)

# ── Fonts ─────────────────────────────────────────────────────────────────────
CN_FONT   = "/System/Library/Fonts/STHeiti Medium.ttc"
EN_FONT   = "/System/Library/Fonts/Helvetica.ttc"
MONO_FONT = "/System/Library/Fonts/Menlo.ttc"

def ef(size):  return ImageFont.truetype(EN_FONT, size)
def cnf(size): return ImageFont.truetype(CN_FONT, size)

def lighten(col_hex, amount=0.82):
    """Return a lighter tint of col_hex by blending with white."""
    r,g,b = int(col_hex[1:3],16), int(col_hex[3:5],16), int(col_hex[5:7],16)
    r = int(r + (255-r)*amount)
    g = int(g + (255-g)*amount)
    b = int(b + (255-b)*amount)
    return f"#{r:02x}{g:02x}{b:02x}"

def darken(col_hex, amount=0.6):
    r,g,b = int(col_hex[1:3],16), int(col_hex[3:5],16), int(col_hex[5:7],16)
    return f"#{int(r*amount):02x}{int(g*amount):02x}{int(b*amount):02x}"

# ── Palette ───────────────────────────────────────────────────────────────────
C = dict(
    bg        = "#f0f4f8",
    q1_bg     = "#e3f2fd",   q1_border = "#90caf9",   q1_title = "#0d47a1",
    q2_bg     = "#e8f5e9",   q2_border = "#81c784",   q2_title = "#1b5e20",
    q3_bg     = "#ede7f6",   q3_border = "#b39ddb",   q3_title = "#4527a0",
    q4_bg     = "#fff3e0",   q4_border = "#ffcc80",   q4_title = "#e65100",
    center_bg = "#1a237e",
    white     = "#ffffff",
    paper     = "#1565c0",
    red_badge = "#c62828",
    org_badge = "#e65100",
    gold      = "#f59f00",
    spotlight = "#ff6f00",
    text_dark = "#212121",
    text_mid  = "#424242",
    text_gray = "#757575",
    ms_red="#f25022", ms_green="#7fba00", ms_blue="#00a4ef", ms_yellow="#ffb900",
    air_blue  = "#003087",
)

# ── Helpers ───────────────────────────────────────────────────────────────────
def rect(xy, fill, radius=14, outline=None, width=2):
    x0,y0,x1,y1 = xy
    draw.rounded_rectangle([x0,y0,x1,y1], radius=radius,
                           fill=fill, outline=outline, width=width)

def text_c(txt, cx, cy, font, color, anchor="mm"):
    draw.text((cx, cy), txt, font=font, fill=color, anchor=anchor)

def text_l(txt, x, y, font, color):
    draw.text((x, y), txt, font=font, fill=color)

def badge(txt, cx, cy, bg, fg, pad_x=10, pad_y=4, radius=8, font_size=18):
    f = ef(font_size)
    bbox = draw.textbbox((0,0), txt, font=f)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    bx0, by0 = cx - tw//2 - pad_x, cy - th//2 - pad_y
    bx1, by1 = cx + tw//2 + pad_x, cy + th//2 + pad_y
    rect([bx0,by0,bx1,by1], fill=bg, radius=radius)
    text_c(txt, cx, cy+(by1-by0)//2 - th//2 - pad_y + th//2, ef(font_size), fg)
    return bx1 - bx0

def dashed_rect(xy, color, dash=10, gap=6, width=2, radius=14):
    x0,y0,x1,y1 = xy
    corners = radius
    def dash_line(pts):
        total = 0
        for i in range(len(pts)-1):
            seg_len = math.dist(pts[i], pts[i+1])
            total += seg_len
        pos = 0
        drawing = True
        seg_i = 0
        pts_pairs = list(zip(pts[:-1], pts[1:]))
        for (ax,ay),(bx,by) in pts_pairs:
            seg_len = math.dist((ax,ay),(bx,by))
            seg_pos = 0
            while seg_pos < seg_len:
                if drawing:
                    end = min(seg_pos + dash, seg_len)
                    t0 = seg_pos / seg_len
                    t1 = end / seg_len
                    p0 = (ax + t0*(bx-ax), ay + t0*(by-ay))
                    p1 = (ax + t1*(bx-ax), ay + t1*(by-ay))
                    draw.line([p0, p1], fill=color, width=width)
                    seg_pos = end
                else:
                    seg_pos = min(seg_pos + gap, seg_len)
                drawing = not drawing

    # top edge
    dash_line([(x0+corners, y0), (x1-corners, y0)])
    # right edge
    dash_line([(x1, y0+corners), (x1, y1-corners)])
    # bottom edge
    dash_line([(x1-corners, y1), (x0+corners, y1)])
    # left edge
    dash_line([(x0, y1-corners), (x0, y0+corners)])

def gradient_rect(xy, color1, color2, vertical=True):
    x0,y0,x1,y1 = [int(v) for v in xy]
    w, h = x1-x0, y1-y0
    r1,g1,b1 = int(color1[1:3],16),int(color1[3:5],16),int(color1[5:7],16)
    r2,g2,b2 = int(color2[1:3],16),int(color2[3:5],16),int(color2[5:7],16)
    if vertical:
        for i in range(h):
            t = i/h
            r = int(r1 + t*(r2-r1))
            g = int(g1 + t*(g2-g1))
            b = int(b1 + t*(b2-b1))
            draw.line([(x0,y0+i),(x1,y0+i)], fill=(r,g,b))
    else:
        for i in range(w):
            t = i/w
            r = int(r1 + t*(r2-r1))
            g = int(g1 + t*(g2-g1))
            b = int(b1 + t*(b2-b1))
            draw.line([(x0+i,y0),(x0+i,y1)], fill=(r,g,b))

# ── Soft background ───────────────────────────────────────────────────────────
gradient_rect([0,0,W,H], "#e8eef5", "#f5f0fa")

# ── Quadrant layout ───────────────────────────────────────────────────────────
PAD = 18
CX, CY = W//2, H//2
CIRCLE_R = 108

q = {
    1: (PAD,       PAD,       CX-12,  CY-12),
    2: (CX+12,     PAD,       W-PAD,  CY-12),
    3: (PAD,       CY+12,     CX-12,  H-PAD),
    4: (CX+12,     CY+12,     W-PAD,  H-PAD),
}

configs = {
    1: dict(bg=C["q1_bg"], border=C["q1_border"], title_c=C["q1_title"]),
    2: dict(bg=C["q2_bg"], border=C["q2_border"], title_c=C["q2_title"]),
    3: dict(bg=C["q3_bg"], border=C["q3_border"], title_c=C["q3_title"]),
    4: dict(bg=C["q4_bg"], border=C["q4_border"], title_c=C["q4_title"]),
}

# Draw quadrant backgrounds
for i, (x0,y0,x1,y1) in q.items():
    cfg = configs[i]
    rect([x0,y0,x1,y1], fill=cfg["bg"], radius=16, outline=None)
    dashed_rect([x0,y0,x1,y1], color=cfg["border"], dash=12, gap=6, width=2)

# ── Microsoft logo helper ─────────────────────────────────────────────────────
def ms_logo(cx, cy, size=14):
    g = size + 2
    draw.rectangle([cx-g, cy-g, cx-2, cy-2], fill=C["ms_red"])
    draw.rectangle([cx+2, cy-g, cx+g, cy-2], fill=C["ms_green"])
    draw.rectangle([cx-g, cy+2, cx-2, cy+g], fill=C["ms_blue"])
    draw.rectangle([cx+2, cy+2, cx+g, cy+g], fill=C["ms_yellow"])
    draw.text((cx+g+6, cy), "Microsoft", font=ef(20), fill=C["text_dark"], anchor="lm")

# ── AIR logo helper ───────────────────────────────────────────────────────────
def air_logo(cx, cy):
    # "AIR" in bold blue
    draw.text((cx, cy-9), "AIR", font=ef(26), fill=C["air_blue"], anchor="mm")
    # Chinese line 1
    draw.text((cx, cy+10), "清华大学", font=cnf(14), fill=C["air_blue"], anchor="mm")
    # Chinese line 2
    draw.text((cx, cy+26), "智能产业研究院", font=cnf(12), fill=C["air_blue"], anchor="mm")

def hkust_logo(cx, cy):
    draw.text((cx, cy-8), "HKUST", font=ef(22), fill="#003087", anchor="mm")
    draw.text((cx, cy+10), "香港科技大学", font=cnf(13), fill="#003087", anchor="mm")

# ── Paper citation row ────────────────────────────────────────────────────────
def paper_badge(txt, x, y, bg, fg, fs=17):
    f = ef(fs)
    bbox = draw.textbbox((0,0), txt, font=f)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    px, py = 7, 3
    draw.rounded_rectangle([x,y-py, x+tw+2*px, y+th+py], radius=6, fill=bg)
    draw.text((x+px, y), txt, font=f, fill=fg)
    return x + tw + 2*px + 6

def draw_arrow(x1a, y1a, x2a, y2a, col, w=2):
    draw.line([(x1a,y1a),(x2a,y2a)], fill=col, width=w)
    angle = math.atan2(y2a-y1a, x2a-x1a)
    asize = 8
    for da in [0.5, -0.5]:
        ax = x2a - asize*math.cos(angle-da)
        ay = y2a - asize*math.sin(angle-da)
        draw.line([(x2a,y2a),(ax,ay)], fill=col, width=w)

def paper_row(items, x, y, line_h=28):
    """items: list of (text, type) where type: 'venue'|'title'|'badge'|'spotlight'"""
    cx = x
    cy = y
    for (txt, kind) in items:
        if kind == "venue":
            cx = paper_badge(txt, cx, cy, "#ffebee", C["red_badge"], 16)
        elif kind == "spotlight":
            cx = paper_badge(txt, cx, cy, "#fff3e0", C["spotlight"], 16)
        elif kind == "product":
            cx = paper_badge(txt, cx, cy, "#fff9c4", C["gold"], 16)
        elif kind == "text":
            f = ef(18)
            bbox = draw.textbbox((0,0), txt, font=f)
            draw.text((cx, cy), txt, font=f, fill=C["paper"], anchor="lt")
            cx += bbox[2]-bbox[0] + 4
        elif kind == "bold":
            f = ef(19)
            bbox = draw.textbbox((0,0), txt, font=f)
            draw.text((cx, cy), txt, font=f, fill=C["paper"], anchor="lt")
            cx += bbox[2]-bbox[0] + 4

# ═══════════════════════════════════════════════════════════════════════════════
# RQ1 — top-left
# ═══════════════════════════════════════════════════════════════════════════════
x0,y0,x1,y1 = q[1]
tc = configs[1]["title_c"]

# Title
draw.text((x0+20, y0+16), "RQ1:", font=ef(22), fill=tc, anchor="lt")
draw.text((x0+78, y0+16), " On which data should the model be trained?",
          font=ef(20), fill=C["text_dark"], anchor="lt")

# Data pipeline diagram
DY = y0 + 56
DX = x0 + 18

# Data source boxes
sources = [("Doc  45%","#1565c0"),("Code 30%","#2e7d32"),
           ("Web  15%","#6a1b9a"),("Dial  10%","#bf360c")]
MID_Y = DY + len(sources)*44 // 2 - 10
for i,(lbl,col) in enumerate(sources):
    bx = DX; by = DY + i*44
    rect([bx, by, bx+96, by+34], fill=lighten(col, 0.85), radius=8, outline=col, width=2)
    draw.text((bx+48, by+17), lbl, font=ef(15), fill=darken(col, 0.7), anchor="mm")
    # arrow to funnel
    draw.line([(bx+96, by+17),(bx+120, MID_Y)], fill="#90a4ae", width=1)

# Funnel shape
FX = DX + 122; FY = DY + 20; FW = 72; FH = 90
pts = [(FX,FY),(FX+FW,FY),(int(FX+FW*0.75),FY+FH),(int(FX+FW*0.25),FY+FH)]
draw.polygon(pts, fill="#78909c", outline="#546e7a", width=2)
draw.text((int(FX+FW*0.5), FY+FH//2), "Filter", font=ef(14), fill=C["white"], anchor="mm")
draw.line([(FX+FW*0.5, FY+FH),(FX+FW*0.5, FY+FH+14)], fill="#546e7a", width=2)

# Bar chart (mixing)
BX = int(FX + FW + 14); BY = DY + 18; BW = 68; BH = 88
bars = [(0.45,"#1565c0"),(0.30,"#2e7d32"),(0.15,"#6a1b9a"),(0.10,"#bf360c")]
bw_bar = BW // len(bars) - 3
for i,(pct,col) in enumerate(bars):
    bh = int(BH * pct)
    bx2 = BX + i*(bw_bar+3)
    draw.rectangle([bx2, BY+BH-bh, bx2+bw_bar, BY+BH], fill=col)
draw.text((BX+BW//2, BY+BH+12), "Ratio Mixing", font=ef(13), fill=C["text_gray"], anchor="mm")

# Arrow → LLM
LX = BX + BW + 10
draw_arrow(LX, DY+62, LX+22, DY+62, "#546e7a", w=2)

# LLM box
rect([LX+24, DY+40, LX+88, DY+84], fill="#1a237e", radius=10)
draw.text((LX+56, DY+62), "LLM", font=ef(22), fill=C["white"], anchor="mm")
draw.text((LX+56, DY+96), "Training", font=ef(14), fill=C["text_gray"], anchor="mm")

# Logos row
LOGO_Y = y1 - 88
air_logo(x0 + 80, LOGO_Y)
ms_logo(x0 + 260, LOGO_Y - 2, size=14)

# Papers
PY = y1 - 44
draw.text((x0+20, PY), "HardPT ", font=ef(17), fill=C["paper"])
bbox = draw.textbbox((x0+20, PY), "HardPT ", font=ef(17))
cx = bbox[2]
cx = paper_badge("ACL 2023", cx, PY, "#ffebee", C["red_badge"], 15)
draw.text((cx, PY), "  DoGraph ", font=ef(17), fill=C["paper"])
bbox = draw.textbbox((cx, PY), "  DoGraph ", font=ef(17))
cx = bbox[2]
cx = paper_badge("ACL 2026", cx, PY, "#ffebee", C["red_badge"], 15)
draw.text((cx, PY), "  DirEct ", font=ef(17), fill=C["paper"])
bbox = draw.textbbox((cx, PY), "  DirEct ", font=ef(17))
cx = bbox[2]
cx = paper_badge("ICML 2026", cx, PY, "#ffebee", C["red_badge"], 15)
draw.text((cx, PY), " ", font=ef(17), fill=C["paper"])
bbox = draw.textbbox((cx, PY), " ", font=ef(17))
cx = bbox[2]
paper_badge("⭐ Spotlight", cx, PY, "#fff3e0", C["spotlight"], 15)

# ═══════════════════════════════════════════════════════════════════════════════
# RQ2 — top-right
# ═══════════════════════════════════════════════════════════════════════════════
x0,y0,x1,y1 = q[2]
tc = configs[2]["title_c"]

draw.text((x0+20, y0+16), "RQ2:", font=ef(22), fill=tc, anchor="lt")
draw.text((x0+80, y0+16), " In what order should training data be scheduled?",
          font=ef(19), fill=C["text_dark"], anchor="lt")

schedules = [
    ("1  Curriculum Order",  ["Easy","Medium","Hard"],  "#43a047", True),
    ("2  Reverse Order",     ["Hard","Medium","Easy"],   "#e53935", False),
    ("3  Random Order",      ["BC","123","A ..."],        "#1e88e5", None),
]
SX = x0 + 28; SY = y0 + 54
for i, (title, steps, col, asc) in enumerate(schedules):
    ty = SY + i * 80
    draw.text((SX, ty), title, font=ef(20), fill=col)
    # draw step boxes with arrows
    bx = SX + 10; by = ty + 28
    for j, step in enumerate(steps):
        bw2 = 68; bh2 = 24
        rect([bx, by, bx+bw2, by+bh2], fill=lighten(col, 0.80), radius=6, outline=col, width=1)
        draw.text((bx+bw2//2, by+bh2//2), step, font=ef(14), fill=darken(col, 0.7), anchor="mm")
        if j < len(steps)-1:
            draw_arrow(bx+bw2+2, by+bh2//2, bx+bw2+18, by+bh2//2, col)
        bx += bw2 + 20
    # mini bar chart
    BCX = x1 - 130; BCY = ty - 4
    vals = [0.3,0.55,0.85] if asc is True else [0.85,0.55,0.3] if asc is False else [0.55,0.3,0.75]
    for j, v in enumerate(vals):
        bh = int(42 * v)
        bx2 = BCX + j*28
        draw.rectangle([bx2, BCY+42-bh, bx2+20, BCY+42], fill=col)

# Logos
LOGO_Y = y1 - 88
ms_logo(x0 + 100, LOGO_Y - 2, size=14)

# Papers
PY = y1 - 44
draw.text((x0+20, PY), "D³ ", font=ef(17), fill=C["paper"])
bbox = draw.textbbox((x0+20, PY), "D³ ", font=ef(17))
cx = bbox[2]
paper_badge("ICML 2026", cx, PY, "#ffebee", C["red_badge"], 15)

# ═══════════════════════════════════════════════════════════════════════════════
# RQ3 — bottom-left
# ═══════════════════════════════════════════════════════════════════════════════
x0,y0,x1,y1 = q[3]
tc = configs[3]["title_c"]

draw.text((x0+20, y0+16), "RQ3:", font=ef(22), fill=tc, anchor="lt")
draw.text((x0+80, y0+16), " How should complex data characteristics be addressed?",
          font=ef(18), fill=C["text_dark"], anchor="lt")

draw.text((x0+20, y0+52), "Complex Data Characteristics", font=ef(18), fill=C["text_mid"])

# Multi-modal distribution (bell curves)
MX = x0 + 30; MY = y0 + 78; MW = 220; MH = 100
draw.text((MX + MW//2, MY - 6), "1. Multi-modal Distribution", font=ef(15), fill=C["text_mid"], anchor="mm")
gaussians = [(MX+50, "#ef5350"), (MX+100, "#ff9800"), (MX+140, "#43a047"), (MX+180, "#1e88e5")]
for (px, col) in gaussians:
    for dx in range(-45, 46):
        sx = px + dx
        sy = MY + MH - int(MH * 0.85 * math.exp(-0.5*(dx/18)**2))
        draw.point((sx, sy), fill=col)
    # draw curve as a polyline
    pts2 = [(px+dx, MY+MH-int(MH*0.85*math.exp(-0.5*(dx/18)**2))) for dx in range(-40,41)]
    draw.line(pts2, fill=col, width=2)

# Separator
draw.line([(MX+MW+20, y0+70),(MX+MW+20, y1-80)], fill="#bdbdbd", width=1)

# Irregular high-freq time series
FX2 = MX+MW+35; FY2 = MY; FW2 = x1-x0-FX2+x0-30; FH2 = MH
draw.text((FX2+FW2//2, MY-6), "② Irregular High-freq Data", font=ef(15), fill=C["text_mid"], anchor="mm")
draw.line([(FX2, FY2+FH2),(FX2+FW2, FY2+FH2)], fill="#bdbdbd", width=1)
draw.line([(FX2, FY2),(FX2, FY2+FH2)], fill="#bdbdbd", width=1)
np.random.seed(42)
ts = np.cumsum(np.random.randn(60)*6) + FY2 + FH2//2
ts = np.clip(ts, FY2+5, FY2+FH2-5)
pts3 = [(int(FX2 + i*(FW2/59)), int(ts[i])) for i in range(60)]
draw.line(pts3, fill="#7b1fa2", width=2)
# add some spikes
for si in [10,25,40,50]:
    draw.line([(pts3[si][0], pts3[si][1]),(pts3[si][0], FY2+10)], fill="#e53935", width=2)

# Logos
LOGO_Y = y1 - 88
# JoinQuant
draw.text((x0+80, LOGO_Y-8), "JoinQuant", font=ef(22), fill="#1565c0", anchor="mm")
draw.text((x0+80, LOGO_Y+12), "聚宽量化", font=cnf(14), fill="#1565c0", anchor="mm")
hkust_logo(x0 + 260, LOGO_Y)

# Papers
PY = y1 - 44
parts = [("LENs ","text"),("ICAIF 2025","venue"),("  HGAN-SDEs ","text"),
         ("ICASSP 2026","venue"),("  MM-NSDEs ","text"),("IJCAI 2026","venue")]
cx = x0 + 20
for (txt, kind) in parts:
    if kind == "text":
        draw.text((cx, PY), txt, font=ef(17), fill=C["paper"])
        bbox = draw.textbbox((cx, PY), txt, font=ef(17))
        cx = bbox[2]
    else:
        cx = paper_badge(txt, cx, PY, "#ffebee", C["red_badge"], 15)

PY2 = PY + 26
draw.text((x0+20, PY2), "High-Frequency Pretraining Model ", font=ef(17), fill=C["paper"])
bbox = draw.textbbox((x0+20, PY2), "High-Frequency Pretraining Model ", font=ef(17))
paper_badge("Product", bbox[2], PY2, "#fff9c4", C["gold"], 15)

# ═══════════════════════════════════════════════════════════════════════════════
# RQ4 — bottom-right
# ═══════════════════════════════════════════════════════════════════════════════
x0,y0,x1,y1 = q[4]
tc = configs[4]["title_c"]

draw.text((x0+20, y0+16), "RQ4:", font=ef(22), fill=tc, anchor="lt")
draw.text((x0+80, y0+16), " How can we organize the data in a more elegant way?",
          font=ef(18), fill=C["text_dark"], anchor="lt")

# Knowledge graph
KCX = (x0+x1)//2; KCY = y0 + 128
KRAD = 40
# Center node
draw.ellipse([KCX-KRAD, KCY-KRAD, KCX+KRAD, KCY+KRAD], fill="#1b5e20", outline="#fff", width=3)
draw.text((KCX, KCY-7), "Starbucks", font=ef(13), fill=C["white"], anchor="mm")
draw.text((KCX, KCY+9), "知识图谱", font=cnf(12), fill="#a5d6a7", anchor="mm")

qw = x1 - x0
nodes = [
    ("Beverage\nsector",  -0.40, -0.60,  "#1565c0"),
    ("Non-Alc.\nDrinks",  -0.42,  0.08,  "#6a1b9a"),
    ("Health\nDrinks",    -0.32,  0.70,  "#2e7d32"),
    ("Soft\nDrinks",      -0.08,  0.85,  "#bf360c"),
    ("Catering\nsector",   0.40, -0.60,  "#e65100"),
    ("Raised\nCoffee",     0.42,  0.15,  "#4e342e"),
    ("JONES",              0.25,  0.75,  "#1a237e"),
    ("BRDC",               0.42,  0.70,  "#37474f"),
]

SPREAD_X = min(qw*0.40, 155)
SPREAD_Y = 100
node_r = 28
for (lbl, dx_r, dy_r, col) in nodes:
    nx = int(KCX + dx_r * SPREAD_X)
    ny = int(KCY + dy_r * SPREAD_Y)
    draw.line([(KCX, KCY),(nx,ny)], fill=lighten(col, 0.3), width=2)
    draw.ellipse([nx-node_r,ny-node_r,nx+node_r,ny+node_r], fill=lighten(col, 0.75), outline=col, width=2)
    for j, line in enumerate(lbl.split("\n")):
        draw.text((nx, ny-6+j*13), line, font=ef(11), fill=col, anchor="mm")

# Logos
LOGO_Y = y1 - 88
air_logo(x0 + 80, LOGO_Y)
hkust_logo(x0 + 280, LOGO_Y)

# Papers
PY = y1 - 44
draw.text((x0+20, PY), "FinRipple ", font=ef(17), fill=C["paper"])
bbox = draw.textbbox((x0+20, PY), "FinRipple ", font=ef(17))
cx = bbox[2]
cx = paper_badge("ACL 2025", cx, PY, "#ffebee", C["red_badge"], 15)
draw.text((cx, PY), "  Meituan Nutrition Knowledge Graph ", font=ef(17), fill=C["paper"])
bbox = draw.textbbox((cx, PY), "  Meituan Nutrition Knowledge Graph ", font=ef(17))
paper_badge("Product", bbox[2], PY, "#fff9c4", C["gold"], 15)

# ═══════════════════════════════════════════════════════════════════════════════
# Center circle
# ═══════════════════════════════════════════════════════════════════════════════
# Shadow
for r_off in range(8, 0, -1):
    alpha = int(40 * (1 - r_off/8))
    draw.ellipse([CX-CIRCLE_R-r_off, CY-CIRCLE_R-r_off,
                  CX+CIRCLE_R+r_off, CY+CIRCLE_R+r_off],
                 fill=f"#{'%02x'%alpha}{'%02x'%alpha}{'%02x'%alpha}")

# Gradient circle (simulate with concentric ellipses)
for r in range(CIRCLE_R, 0, -1):
    t = 1 - r/CIRCLE_R
    ri = int(0x1a + t*(0x0d-0x1a))
    gi = int(0x23 + t*(0x47-0x23))
    bi = int(0x7e + t*(0xa0-0x7e))
    draw.ellipse([CX-r, CY-r, CX+r, CY+r], fill=(ri,gi,bi))

draw.ellipse([CX-CIRCLE_R, CY-CIRCLE_R, CX+CIRCLE_R, CY+CIRCLE_R],
             fill=None, outline=C["white"], width=3)

# Center text
draw.text((CX, CY-36), "Data Centric", font=ef(20), fill=C["white"], anchor="mm")
draw.text((CX, CY-14), "Machine Learning", font=ef(20), fill=C["white"], anchor="mm")
draw.line([(CX-60, CY+2),(CX+60, CY+2)], fill="#90caf9", width=1)
draw.text((CX, CY+18), "Chinese Fineweb-EDU", font=ef(13), fill="#90caf9", anchor="mm")
draw.text((CX, CY+36), "BizCompass (ACL 2026)", font=ef(13), fill="#90caf9", anchor="mm")

# ── Save ──────────────────────────────────────────────────────────────────────
OUT = "/Users/xuyuanjian/Documents/DesktopOrganizer/文件夹 1/papers/xuyuanjian/static/big_pic.png"
img.save(OUT, "PNG", optimize=True)
print(f"Saved to {OUT}  ({W}x{H})")
