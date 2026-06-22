import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side, GradientFill
from openpyxl.utils import get_column_letter

# ── DATA ──────────────────────────────────────────────────────────────────
# fmt: name, address, city_zip, beds, rent_low, rent_high, dist_mi, bus, phone, notes
# rent = 0 means "请询价"
data = [
    # ── Mission Viejo (直达 Route 85 / 91) ──────────────────────────────
    ("Eaves Mission Viejo",            "24950 Via Florecer",       "Mission Viejo 92692", "1–2 BR", 2190, 3110,  1.23, "85/91 直达",  "(949)525-4714",  "★推荐 距离最近"),
    ("Alicia Viejo Apt Homes",         "23842 Alicia Pkwy",        "Mission Viejo 92691", "1–2 BR", 2405, 3035,  1.94, "85/91 直达",  "(949)472-8552",  "含洗衣机/烘干机"),
    ("Vista Del Lago",                 "21622 Marguerite Pkwy",    "Mission Viejo 92692", "1–3 BR", 2525, 4382,  2.45, "85/91 直达",  "(949)243-7570",  "3卧可3人合租"),
    ("Mosaic (Park Ridge Villas)",     "27444 Camden",             "Mission Viejo 92692", "Studio–2BR", 2145, 3120, 2.79, "85/91 直达", "(949)393-5828",  "★推荐 Studio起租低"),
    ("Los Alisos at Mission Viejo",    "28601 Los Alisos Blvd",    "Mission Viejo 92692", "Studio–3BR", 2221, 3239, 3.02, "85/91 直达", "(949)762-8930",  "★推荐 直达+价格适中"),
    ("Bella Vista Apartments",         "27550 Hillcrest",          "Mission Viejo 92691", "1–2 BR", 2330, 3000,  3.78, "85/91 直达",  "(949)682-7957",  ""),
    # ── Ladera Ranch (Route 91) ──────────────────────────────────────────
    ("Laurel Canyon Apt Homes",        "76 Mercantile Way",        "Ladera Ranch 92694",  "1–3 BR", 2700, 4165,  2.06, "91 (可达)",   "(949)485-3021",  "含车库"),
    ("Laurel Vista Apt Homes",         "27082 O'Neill Dr",         "Ladera Ranch 92694",  "1–2 BR", 2590, 3300,  2.99, "91 (可达)",   "(949)682-7961",  ""),
    ("Laurel Glen Apt Homes",          "70 Sklar Street",          "Ladera Ranch 92694",  "询价",      0,    0,  4.15, "91 (可达)",   "(949)347-5576",  ""),
    ("Laurel Terrace Apt Homes",       "2000 Corporate Dr",        "Ladera Ranch 92694",  "询价",      0,    0,  4.21, "91 (可达)",   "(949)347-5576",  ""),
    # ── Lake Forest (Route 89 → 转 91) ──────────────────────────────────
    ("Forest Glen",                    "25092 Farthing St",        "Lake Forest 92630",   "1–2 BR", 2033, 3169,  3.03, "89→转91",     "(949)393-5848",  "★推荐 全区最低起租"),
    ("Ridgecrest",                     "21486 Lake Forest Dr",     "Lake Forest 92630",   "1–2 BR", 2507, 2945,  3.11, "89→转91",     "(949)393-5814",  ""),
    ("Bellecour Way",                  "21041 Osterman Rd",        "Lake Forest 92630",   "询价",      0,    0,  3.26, "89→转91",     "(949)243-0461",  ""),
    ("River Oaks Apartments",          "20702 El Toro Road",       "Lake Forest 92630",   "1–2 BR", 2495, 2995,  3.27, "89→转91",     "(949)273-2712",  ""),
    ("Westridge Apt Homes",            "26571 Normandale Dr",      "Lake Forest 92630",   "询价",      0,    0,  3.28, "89→转91",     "(949)354-0138",  ""),
    ("Lyon The Arbors",                "26356 Vintage Woods Rd",   "Lake Forest 92630",   "询价",      0,    0,  3.34, "89→转91",     "(949)393-5810",  ""),
    ("Crestwood Apt Homes",            "21011 Osterman Rd",        "Lake Forest 92630",   "2–3 BR", 3075, 3360,  3.34, "89→转91",     "(949)243-0451",  "3卧可3人合租"),
    ("Spring Lakes Apt Homes",         "21641 Canada Rd",          "Lake Forest 92630",   "1–2 BR", 2140, 2945,  3.37, "89→转91",     "(949)382-1638",  "★推荐 低起租"),
    ("Siena Terrace",                  "20041 Osterman Rd",        "Lake Forest 92630",   "询价",      0,    0,  3.42, "89→转91",     "(949)393-5858",  ""),
    ("Emerald Court Apt Homes",        "21141 Canada Rd",          "Lake Forest 92630",   "询价",      0,    0,  3.50, "89→转91",     "(949)393-5849",  ""),
    ("The Arroyo at Baler Ranch",      "100 Indigo Pl",            "Lake Forest 92630",   "询价",      0,    0,  3.50, "89→转91",     "(949)888-5548",  ""),
    ("Furnished Studio OC",            "20251 Lake Forest Dr",     "Lake Forest 92630",   "Studio",    0,    0,  3.91, "89→转91",     "(949)393-5804",  "按周租 含家具"),
    ("Eaves Lake Forest",              "22700 Lake Forest Dr",     "Lake Forest 92630",   "询价",      0,    0,  4.12, "89→转91",     "(949)273-2699",  ""),
    # ── Rancho Santa Margarita (Route 89/91) ────────────────────────────
    ("Skyview",                        "21022 Los Alisos Blvd",    "Rancho SM 92688",     "询价",      0,    0,  3.17, "89/91",       "(949)393-5817",  ""),
    ("Villas Antonio Apt Homes",       "22482 Alma Aldea",         "Rancho SM 92688",     "询价",      0,    0,  3.21, "89/91",       "(949)393-5863",  ""),
    ("Eaves Santa Margarita",          "111 Via Serena",           "Rancho SM 92688",     "Studio–2BR", 2195, 3465, 3.41, "89/91",    "(949)243-7582",  "★推荐 低起租+多户型"),
    ("Villas Aliento Apt Homes",       "114 Aliento",              "Rancho SM 92688",     "Studio–2BR", 2305, 3015, 4.02, "89/91",    "(949)382-1634",  ""),
    ("Villa La Paz Apt Homes",         "2 Via Amistosa",           "Rancho SM 92688",     "询价",      0,    0,  4.31, "89/91",       "(949)5833",      ""),
    ("Lyon Trabuco Highlands",         "31872 Joshua Dr",          "Rancho SM 92679",     "询价",      0,    0,  4.68, "89→转91",     "(949)393-5805",  ""),
    # ── Laguna Hills (Route 91 直达) ─────────────────────────────────────
    ("Villa Solana",                   "26033 Moulton Pkwy",       "Laguna Hills 92653",  "询价",      0,    0,  4.24, "91 直达",     "(949)393-5860",  ""),
    # ── Laguna Niguel (Route 85/91) ──────────────────────────────────────
    ("Apex Laguna",                    "27960 Cabot Rd",           "Laguna Niguel 92677", "询价",      0,    0,  4.36, "85/91",       "(949)356-5440",  ""),
    ("Laguna Gardens",                 "24455 Via Panasa",         "Laguna Niguel 92677", "询价",      0,    0,  4.64, "85/91",       "(949)525-4193",  ""),
    # ── Aliso Viejo (Route 91) ───────────────────────────────────────────
    ("Aliso Creek",                    "24152 Hollyoak",           "Aliso Viejo 92656",   "询价",      0,    0,  4.57, "91",          "(949)273-2694",  ""),
]

# Sort by distance
data.sort(key=lambda x: x[6])

# ── STYLES ────────────────────────────────────────────────────────────────
thin = Side(style="thin", color="CCCCCC")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

RED_DARK  = "8B0000"
RED_MED   = "C0392B"
RED_LIGHT = "FBEEE9"
GREEN_BG  = "E8F5E9"
YELLOW_BG = "FFFDE7"
ORANGE_BG = "FFF3E0"
GREY_BG   = "F5F5F5"

def cell_style(ws, row, col, value, bold=False, bg=None, color="000000",
               halign="left", valign="center", wrap=True, size=10, italic=False):
    c = ws.cell(row=row, column=col, value=value)
    c.font = Font(bold=bold, size=size, color=color, italic=italic)
    c.alignment = Alignment(horizontal=halign, vertical=valign, wrap_text=wrap)
    c.border = border
    if bg:
        c.fill = PatternFill("solid", fgColor=bg)
    return c

def per_person(rent_low):
    if rent_low == 0:
        return "—"
    return f"≈${rent_low//2:,}"

def price_color(rent_low):
    if rent_low == 0:
        return GREY_BG
    elif rent_low < 2200:
        return GREEN_BG
    elif rent_low < 2600:
        return YELLOW_BG
    else:
        return ORANGE_BG

def price_label(rent_low, rent_high):
    if rent_low == 0:
        return "请询价"
    return f"${rent_low:,} – ${rent_high:,}"

# ── WORKBOOK ──────────────────────────────────────────────────────────────
wb = openpyxl.Workbook()

# ══ Sheet 1: Main table ═══════════════════════════════════════════════════
ws = wb.active
ws.title = "租房社区列表"

# ── Title ─────────────────────────────────────────────────────────────────
ws.merge_cells("A1:L1")
t = ws["A1"]
t.value = "🏫 Saddleback College 10公里内租房社区总表  |  28000 Marguerite Pkwy, Mission Viejo, CA 92692  |  截至 2026-06"
t.font = Font(bold=True, size=13, color="FFFFFF")
t.fill = PatternFill("solid", fgColor=RED_DARK)
t.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
ws.row_dimensions[1].height = 30

# ── Sub-title ─────────────────────────────────────────────────────────────
ws.merge_cells("A2:L2")
s = ws["A2"]
s.value = ("⭐ 学生免费公交卡：Saddleback College 在读学生可申请 OCTA 免费 Bus Pass！免费搭乘 Route 85/89/91 等线路  |  "
           "合租人均 = 最低租金 ÷ 2（两人共租2BR估算）  |  "
           "绿底 = 起租 < $2,200  黄底 = $2,200–$2,600  橙底 = > $2,600  灰底 = 请询价")
s.font = Font(italic=True, size=9, color="555555")
s.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
s.fill = PatternFill("solid", fgColor="FFF9F9")
ws.row_dimensions[2].height = 30

# ── Headers ───────────────────────────────────────────────────────────────
headers = ["#", "社区名称", "地址", "城市/邮编", "户型", "月租范围 (USD)",
           "合租人均\n(2人)", "距离\n(英里)", "距离\n(公里)",
           "公交线路\n(到学校)", "电话", "备注"]
col_widths = [4, 28, 22, 20, 11, 16, 10, 8, 8, 14, 16, 22]

hr = 3
for c, (h, w) in enumerate(zip(headers, col_widths), start=1):
    cell = ws.cell(row=hr, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF", size=10)
    cell.fill = PatternFill("solid", fgColor=RED_MED)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = border
    ws.column_dimensions[get_column_letter(c)].width = w
ws.row_dimensions[hr].height = 36

# ── Data rows ─────────────────────────────────────────────────────────────
for i, row in enumerate(data):
    name, addr, city, beds, lo, hi, dist_mi, bus, phone, notes = row
    rr = hr + 1 + i
    dist_km = round(dist_mi * 1.60934, 2)
    bg = price_color(lo)
    stripe = "F9F9F9" if i % 2 == 0 else "FFFFFF"

    def c(col, val, halign="left", bold=False):
        b = bg if col in (6, 7) else stripe
        cell_style(ws, rr, col, val, bold=bold, bg=b,
                   halign=halign, size=10)

    is_rec = "★推荐" in notes

    cell_style(ws, rr, 1, i+1, halign="center", bg=stripe, bold=False)
    cell_style(ws, rr, 2, name, bg=stripe, bold=is_rec,
               color="8B0000" if is_rec else "000000")
    cell_style(ws, rr, 3, addr, bg=stripe)
    cell_style(ws, rr, 4, city, bg=stripe)
    cell_style(ws, rr, 5, beds, bg=stripe, halign="center")
    cell_style(ws, rr, 6, price_label(lo, hi), bg=bg, halign="center", bold=(lo < 2200 and lo > 0))
    cell_style(ws, rr, 7, per_person(lo), bg=bg, halign="center", bold=(lo < 2200 and lo > 0))
    cell_style(ws, rr, 8, dist_mi, bg=stripe, halign="center")
    cell_style(ws, rr, 9, dist_km, bg=stripe, halign="center")
    cell_style(ws, rr, 10, bus, bg=stripe, halign="center",
               bold=("直达" in bus), color=("006400" if "直达" in bus else ("8B6914" if "转" in bus else "000000")))
    cell_style(ws, rr, 11, phone, bg=stripe)
    cell_style(ws, rr, 12, notes.replace("★推荐 ", ""), bg=stripe, italic=is_rec)
    ws.row_dimensions[rr].height = 18

# Freeze
ws.freeze_panes = "A4"

# ══ Sheet 2: Shared housing platforms ════════════════════════════════════
ws2 = wb.create_sheet("合租平台 & 省钱攻略")

ws2.merge_cells("A1:E1")
h = ws2["A1"]
h.value = "合租 / 找室友平台推荐（比整租便宜 40-60%）"
h.font = Font(bold=True, size=13, color="FFFFFF")
h.fill = PatternFill("solid", fgColor=RED_DARK)
h.alignment = Alignment(horizontal="center", vertical="center")
ws2.row_dimensions[1].height = 28

platforms = [
    ("平台", "网址", "价格范围/月", "特点", "适合人群"),
    ("SpareRoom", "spareroom.com/rooms-for-rent/saddleback_college", "$700–$1,500", "专注合租/单间，近Saddleback页面", "学生首选"),
    ("Roomies.com", "roomies.com/near/saddleback-college", "$800–$1,400", "学生友好，可按学校筛选", "找室友"),
    ("Zumper Rooms", "zumper.com/rooms-for-rent/near-saddleback-college-ca", "$900–$1,600", "单间出租聚合", "速找"),
    ("Facebook Marketplace", "facebook.com/marketplace", "$700–$1,300", "本地房东直租，可砍价", "灵活"),
    ("Craigslist OC", "orangecounty.craigslist.org → rooms & shares", "$600–$1,200", "价格最低但需甄别", "预算最紧"),
]

col_w2 = [18, 45, 16, 32, 14]
for i, row in enumerate(platforms):
    for j, (val, w) in enumerate(zip(row, col_w2), start=1):
        c = ws2.cell(row=i+2, column=j, value=val)
        c.border = border
        c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        if i == 0:
            c.font = Font(bold=True, color="FFFFFF", size=10)
            c.fill = PatternFill("solid", fgColor=RED_MED)
        else:
            c.font = Font(size=10)
            c.fill = PatternFill("solid", fgColor=(GREEN_BG if i % 2 == 0 else "FFFFFF"))
        ws2.column_dimensions[get_column_letter(j)].width = w
    ws2.row_dimensions[i+2].height = 22

# Tips section
ws2.row_dimensions[9].height = 10
tips = [
    (10, "💡 省钱攻略", True, RED_MED, "FFFFFF"),
    (11, "① 学生免费公交卡：在 Saddleback College 学生服务中心申请 OCTA Free Bus Pass，在读期间免费乘坐 Route 85/89/91 等所有 OCTA 线路！", False, "FFFFFF", "000000"),
    (12, "② 2人合租2BR：最低月租约 $2,033（Forest Glen），两人各出约 $1,017/月，远低于整租1BR。", False, GREEN_BG, "000000"),
    (13, "③ 3人合租3BR：Los Alisos/Laurel Canyon 等有3BR，三人分摊仅需约 $740–$900/人/月。", False, GREEN_BG, "000000"),
    (14, "④ SpareRoom 单间：单间含水电约 $700–$1,200/月，无需签长期租约，最灵活。", False, YELLOW_BG, "000000"),
    (15, "⑤ 公交最优选：Route 85/91 直达 Saddleback College；Lake Forest 社区搭 Route 89 至 Laguna Hills TC 后转 91 即到校。", False, YELLOW_BG, "000000"),
    (16, "⑥ 签约前必做：核实是否允许多人合租（lease addendum），部分社区需每人单独列入租约。", False, ORANGE_BG, "000000"),
]
ws2.merge_cells("A9:E9")
for r, (row_n, text, bold, bg, fg) in enumerate(tips):
    ws2.merge_cells(f"A{row_n}:E{row_n}")
    c = ws2.cell(row=row_n, column=1, value=text)
    c.font = Font(bold=bold, size=10 if not bold else 12, color=fg)
    c.fill = PatternFill("solid", fgColor=bg)
    c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws2.row_dimensions[row_n].height = 28

# ── Save ──────────────────────────────────────────────────────────────────
out = "/home/user/fjri/output/Saddleback_College_10km_Rentals_v2.xlsx"
wb.save(out)
print("saved:", out)
