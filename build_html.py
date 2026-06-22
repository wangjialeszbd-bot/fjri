# -*- coding: utf-8 -*-
# Saddleback College 周边租房综合文件 (HTML, 可点击链接 + 房屋介绍)

college = "Saddleback College · 28000 Marguerite Pkwy, Mission Viejo, CA 92692"

# 公寓社区: (名称, 地址, 城市邮编, 户型, 整租范围, 单间合租估算, 距离mi, 公交, 电话, 介绍, 链接)
apts = [
 ("Eaves Mission Viejo","24950 Via Florecer","Mission Viejo 92692","1–2 BR","$2,190–$3,110","≈$1,095/人 (2人2BR)",1.23,"85/91 直达","(949)525-4714",
  "距学校最近的社区(2km)。含游泳池、健身房，部分户型带洗衣机烘干机。1卧约600-750呎。",
  "https://www.apartments.com/eaves-mission-viejo-mission-viejo-ca/emfbqwn/"),
 ("Alicia Viejo Apartment Homes","23842 Alicia Pkwy","Mission Viejo 92691","1–2 BR","$2,405–$3,035","≈$1,200/人",1.94,"85/91 直达","(949)472-8552",
  "精品小型社区，全部含室内洗衣烘干、硬木地板、壁炉。带泳池+spa+健身房。",
  "https://www.apartments.com/alicia-viejo-apartment-homes-mission-viejo-ca/s2seyd5/"),
 ("Vista Del Lago","21622 Marguerite Pkwy","Mission Viejo 92692","1–3 BR","$2,525–$4,382","≈$840/人 (3人3BR)",2.45,"85/91 直达","(949)243-7570",
  "在 Marguerite Pkwy 主路上，到校一条路直达。有3卧户型，适合3人合租分摊。宠物友好。",
  "https://www.apartments.com/mission-viejo-ca/"),
 ("Mosaic (原 Park Ridge Villas)","27444 Camden","Mission Viejo 92692","Studio–2 BR","$2,145–$3,120","≈$1,073/人",2.79,"85/91 直达","(949)393-5828",
  "★性价比高。有 Studio 户型(525呎)起租低。社区翻新过，泳池+健身。",
  "https://www.apartments.com/park-ridge-apartment-homes-mission-viejo-ca/gvb3fhw/"),
 ("Los Alisos at Mission Viejo","28601 Los Alisos Blvd","Mission Viejo 92692","Studio–3 BR","$2,221–$3,239","≈$740/人 (3人3BR)",3.02,"85/91 直达","(949)762-8930",
  "★高档社区。9尺挑高、木地板、不锈钢电器、石英台面。两个度假式泳池+24小时健身房。有Studio到3卧全户型。",
  "https://www.apartments.com/los-alisos-at-mission-viejo-mission-viejo-ca/jxgw605/"),
 ("Bella Vista Apartments","27550 Hillcrest","Mission Viejo 92691","1–2 BR","$2,330–$3,000","≈$1,165/人",3.78,"85/91 直达","(949)682-7957",
  "1-2卧，650-1000呎。价格在 Mission Viejo 中等偏低。",
  "https://www.apartments.com/bella-vista-apartments-mission-viejo-ca/0h72de0/"),
 ("Saddleback Ranch Apartments","23151 Los Alisos Blvd","Mission Viejo 92691","1–3 BR","$2,041–$5,166","≈$680/人 (3人3BR)",2.9,"85/91 直达","查官网",
  "★1卧起租 $2,041 是全区最低之一。有1-3卧，含吊扇、阳台/露台、步入式衣橱、中央空调。3卧合租超划算。",
  "https://www.saddlebackranch-apartments.com/"),
 ("Laurel Canyon Apartment Homes","76 Mercantile Way","Ladera Ranch 92694","1–3 BR","$2,700–$4,165","≈$900/人 (3人3BR)",2.06,"91 可达","(949)485-3021",
  "含独立车库、定制橱柜、硬木地板。泳池+健身+BBQ。当前有 Up to $2,000 Off 入住优惠(7/31前)。",
  "https://www.apartments.com/laurel-canyon-apartment-homes-ladera-ranch-ca/5kndhvq/"),
 ("Laurel Vista Apartment Homes","27082 O'Neill Dr","Ladera Ranch 92694","1–2 BR","from $2,590","≈$1,295/人",2.99,"91 可达","(949)682-7961",
  "1-2卧，658-994呎。带阳台/露台。宠物友好，泳池+会所+健身+BBQ。曾有「首月免租」优惠。",
  "https://www.apartments.com/laurel-vista-apartment-homes-ladera-ranch-ca/wg64bml/"),
 ("Forest Glen (Lyon)","25092 Farthing St","Lake Forest 92630","1–2 BR","$2,033–$3,169","≈$1,017/人",3.03,"89→转91","(949)393-5848",
  "★★全区最低起租 $2,033！1卧$2,618 / 2卧$3,169。两人合租2BR人均约$1,017，最省钱选择。",
  "https://www.apartments.com/forest-glen-lake-forest-ca/6hpb89t/"),
 ("Spring Lakes Apartment Homes","21641 Canada Rd","Lake Forest 92630","1–2 BR","$2,140–$2,945","≈$1,070/人",3.37,"89→转91","(949)382-1638",
  "★525-1000呎，Studio到2卧都有，起租 $2,140 很低。性价比高。",
  "https://www.apartments.com/spring-lakes-apartment-homes-lake-forest-ca/2x3qeh8/"),
 ("Ridgecrest","21486 Lake Forest Dr","Lake Forest 92630","1–2 BR","$2,507–$2,945","≈$1,254/人",3.11,"89→转91","(949)393-5814",
  "780-1105呎。1卧$2,507起/2卧$2,945起。Sares-Regis 管理。",
  "https://www.apartments.com/ridgecrest-apartments-lake-forest-ca/ntskngm/"),
 ("River Oaks Apartments","20702 El Toro Road","Lake Forest 92630","1–2 BR","$2,495–$2,995","≈$1,248/人",3.27,"89→转91","(949)273-2712",
  "760-960呎。租金 $2,495-$2,995。靠 El Toro Rd，公交方便(89路)。",
  "https://www.apartments.com/river-oaks-apartments-lake-forest-ca/ykg2cqt/"),
 ("Crestwood Apartment Homes","21011 Osterman Rd","Lake Forest 92630","2–3 BR","$3,075–$3,360","≈$1,025/人 (3人3BR)",3.34,"89→转91","(949)243-0451",
  "2-3卧户型，适合多人合租。3人分摊3卧人均约$1,025。",
  "https://www.apartments.com/crestwood-apartment-homes-lake-forest-ca/4zjrrvh/"),
 ("Eaves Santa Margarita","111 Via Serena","Rancho Santa Margarita 92688","Studio–2 BR","$2,195–$3,465","≈$1,098/人",3.41,"89/91","(949)243-7582",
  "★524-1058呎，Studio起租低($2,195)。AvalonBay 旗下品牌，管理规范。",
  "https://www.apartments.com/eaves-santa-margarita-rancho-santa-margarita-ca/ze6g91z/"),
 ("Villas Aliento Apartment Homes","114 Aliento","Rancho Santa Margarita 92688","Studio–2 BR","$2,305–$3,015","≈$1,153/人",4.02,"89/91","(949)382-1634",
  "510-930呎，Studio到2卧。起租 $2,305。",
  "https://www.apartments.com/villas-aliento-apartment-homes-rancho-santa-margarita-ca/m9xlj7h/"),
 ("Skyview","21022 Los Alisos Blvd","Rancho Santa Margarita 92688","询价","请询价","—",3.17,"89/91","(949)393-5817",
  "Los Alisos 沿线，公交便利。具体租金请电话询。",
  "https://www.apartments.com/"),
 ("Villa Solana","26033 Moulton Pkwy","Laguna Hills 92653","询价","请询价","—",4.24,"91 直达","(949)393-5860",
  "Laguna Hills，91路直达学校。EGR 管理。",
  "https://www.apartments.com/"),
 ("Aliso Creek","24152 Hollyoak","Aliso Viejo 92656","询价","请询价","—",4.57,"91","(949)273-2694",
  "Aliso Viejo，Sares-Regis 管理。",
  "https://www.apartments.com/"),
 ("Apex Laguna","27960 Cabot Rd","Laguna Niguel 92677","询价","请询价","—",4.36,"85/91","(949)356-5440",
  "Laguna Niguel，Lincoln 管理。",
  "https://www.apartments.com/"),
]

# 单间合租平台: (平台, 价格/月, 介绍, 链接)
rooms = [
 ("SpareRoom — Saddleback 专页","$700–$1,500","专门的近 Saddleback College 单间/合租页面，可直接联系房东或现有室友。138+ 个房源。例: Mission Viejo 带家具单间+共用卫浴，含水电WiFi $1,500/月。",
  "https://www.spareroom.com/rooms-for-rent/saddleback_college"),
 ("SpareRoom — Mission Viejo","$1,100–$1,500","Mission Viejo 单间。例: $1,100/月 + 1/4水电，押金$2,000。",
  "https://www.spareroom.com/rooms-for-rent/ca/orange_county/mission_viejo"),
 ("SpareRoom — Lake Forest","$1,000–$1,450","Lake Forest 单间，起价 $1,000/月含水电。",
  "https://www.spareroom.com/rooms-for-rent/ca/orange_county/lake_forest"),
 ("SpareRoom — Laguna Hills","$1,300起","Laguna Hills 单间，$1,300/月含水电。",
  "https://www.spareroom.com/rooms-for-rent/ca/orange_county/laguna_hills"),
 ("Roomies.com — 近 Saddleback","$800–$1,500","学生友好，可按学校筛选找室友。例: Mission Viejo 2022新建3层联排，主卧带独立卫浴+步入衣橱+泳池+车库，全水电含 $1,500/月。",
  "https://www.roomies.com/near/saddleback-college"),
 ("Roomsurf — Saddleback 室友","免费匹配","Saddleback College 学生专用室友匹配工具，先找室友再一起租房。",
  "https://www.roomsurf.com/saddleback-college-roommates"),
 ("Uloop — Saddleback 学生房","$700–$1,400","学生off-campus房源+室友匹配，专门服务 Saddleback。",
  "https://saddleback.uloop.com/housing"),
 ("Zumper Rooms","$900–$1,600","单间出租聚合，更新快。",
  "https://www.zumper.com/rooms-for-rent/near-saddleback-college-ca"),
 ("Craigslist OC — rooms & shares","$600–$1,200","本地房东直租，价格最低，但需自己甄别真假。",
  "https://orangecounty.craigslist.org/search/roo"),
 ("Facebook 群组 — Saddleback Housing","$700–$1,300","「Mission Viejo, Saddleback College Housing, Room」专门租房群，房东直发，可砍价。",
  "https://www.facebook.com/groups/1187106126212600/"),
]

# Sort apartments by distance
apts.sort(key=lambda x: x[6])

def km(mi): return round(mi*1.60934,1)
def badge(rent):
    if "询价" in rent: return ("询价","#9e9e9e")
    import re
    nums = re.findall(r'[\d,]+', rent)
    if not nums: return ("","#9e9e9e")
    low = int(nums[0].replace(",",""))
    if low < 2200: return ("最便宜","#2e7d32")
    if low < 2600: return ("实惠","#f9a825")
    return ("较高","#e65100")

rows_html = ""
for i,a in enumerate(apts,1):
    name,addr,city,beds,rent,share,mi,bus,phone,desc,link = a
    lab,col = badge(rent)
    busclass = "direct" if "直达" in bus else ("transfer" if "转" in bus else "")
    rows_html += f"""
    <tr>
      <td class="num">{i}</td>
      <td class="name"><a href="{link}" target="_blank">{name} ↗</a><br><span class="badge" style="background:{col}">{lab}</span></td>
      <td>{addr}<br><span class="muted">{city}</span></td>
      <td class="center">{beds}</td>
      <td class="center rent">{rent}</td>
      <td class="center share">{share}</td>
      <td class="center">{mi} mi<br><span class="muted">{km(mi)} km</span></td>
      <td class="center {busclass}">{bus}</td>
      <td class="phone">{phone}</td>
      <td class="desc">{desc}</td>
    </tr>"""

rooms_html = ""
for r in rooms:
    plat,price,desc,link = r
    rooms_html += f"""
    <tr>
      <td class="name"><a href="{link}" target="_blank">{plat} ↗</a></td>
      <td class="center rent">{price}</td>
      <td class="desc">{desc}</td>
    </tr>"""

html = f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Saddleback College 周边租房总表</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; margin:0; background:#f4f4f6; color:#222; }}
  header {{ background:linear-gradient(135deg,#8B0000,#c0392b); color:#fff; padding:28px 24px; }}
  header h1 {{ margin:0 0 6px; font-size:24px; }}
  header p {{ margin:2px 0; font-size:13px; opacity:.95; }}
  .tip {{ background:#fff8e1; border-left:5px solid #f9a825; padding:14px 18px; margin:18px 24px; border-radius:6px; font-size:14px; line-height:1.7; }}
  .tip b {{ color:#8B0000; }}
  h2 {{ margin:26px 24px 10px; font-size:19px; color:#8B0000; border-bottom:2px solid #f0d0d0; padding-bottom:6px; }}
  .wrap {{ overflow-x:auto; padding:0 24px 10px; }}
  table {{ border-collapse:collapse; width:100%; background:#fff; font-size:13px; box-shadow:0 1px 4px rgba(0,0,0,.08); border-radius:8px; overflow:hidden; }}
  th {{ background:#c0392b; color:#fff; padding:10px 8px; text-align:left; font-size:12px; position:sticky; top:0; }}
  td {{ padding:9px 8px; border-bottom:1px solid #eee; vertical-align:top; line-height:1.5; }}
  tr:nth-child(even) td {{ background:#fafafa; }}
  tr:hover td {{ background:#fff3f0; }}
  .num {{ color:#999; font-weight:bold; text-align:center; }}
  .name a {{ color:#1565c0; text-decoration:none; font-weight:bold; }}
  .name a:hover {{ text-decoration:underline; }}
  .center {{ text-align:center; }}
  .rent {{ font-weight:bold; color:#2e7d32; white-space:nowrap; }}
  .share {{ color:#8B0000; font-weight:bold; white-space:nowrap; }}
  .muted {{ color:#999; font-size:11px; }}
  .desc {{ font-size:12px; color:#444; min-width:220px; max-width:320px; }}
  .phone {{ white-space:nowrap; font-size:12px; }}
  .badge {{ display:inline-block; color:#fff; font-size:10px; padding:1px 7px; border-radius:8px; margin-top:3px; }}
  .direct {{ color:#2e7d32; font-weight:bold; }}
  .transfer {{ color:#8B6914; }}
  footer {{ padding:20px 24px 40px; font-size:12px; color:#888; line-height:1.7; }}
</style>
</head>
<body>
<header>
  <h1>🏫 Saddleback College 周边租房总表</h1>
  <p>{college}</p>
  <p>范围 ~15 km · 截至 2026-06 · 点击社区名/平台名 ↗ 直达租房页面</p>
</header>

<div class="tip">
  <b>💡 「单间找室友」是什么？</b> 不租整套房，只租公寓/房子里的<b>一间卧室</b>，客厅厨房卫生间和室友共用 → 每月只要 $700–$1,500，比整租省一半。见下方<b>「单间/合租平台」</b>表。<br>
  <b>🚌 学生免费公交：</b> 在 Saddleback 学生服务中心申请 <b>OCTA Free Bus Pass</b>，免费坐 Route 85 / 89 / 91 等全部线路到校！<br>
  <b>🟢 绿色=最便宜(起租&lt;$2,200)　🟡 黄色=实惠($2,200–$2,600)　🟠 橙色=较高　⚫ 灰色=请询价</b>
</div>

<h2>① 公寓社区（整租 / 可多人合租分摊）</h2>
<div class="wrap">
<table>
  <thead><tr>
    <th>#</th><th>社区名称 (点击查看)</th><th>地址</th><th>户型</th>
    <th>整租月租</th><th>合租人均估算</th><th>距学校</th><th>公交到校</th><th>电话</th><th>房屋介绍</th>
  </tr></thead>
  <tbody>{rows_html}</tbody>
</table>
</div>

<h2>② 单间 / 合租平台（预算最低 $600–$1,500/月）</h2>
<div class="wrap">
<table>
  <thead><tr><th>平台 (点击进入)</th><th>价格/月</th><th>介绍</th></tr></thead>
  <tbody>{rooms_html}</tbody>
</table>
</div>

<footer>
  <b>省钱建议：</b><br>
  ① 预算最紧 → 直接找<b>单间合租</b>（SpareRoom / Craigslist / Facebook群），$600–$1,200/月最便宜。<br>
  ② 想要整套但省钱 → <b>Forest Glen $2,033起</b> 两人合租人均约 $1,017，或 <b>Saddleback Ranch 3卧</b> 三人合租人均约 $680。<br>
  ③ 一定申请<b>学生免费公交卡</b>，交通成本归零。<br><br>
  数据来源：Saddleback College 官方公寓列表、Apartments.com、SpareRoom、Roomies.com、Craigslist、OCTA。租金为大致区间，会随空置变动，<b>签约前请电话核实并确认是否允许合租</b>。
</footer>
</body>
</html>"""

import io
out = "/home/user/fjri/output/Saddleback_College_租房总表.html"
with io.open(out,"w",encoding="utf-8") as f:
    f.write(html)
print("saved:", out)
print("公寓社区:", len(apts), "| 合租平台:", len(rooms))
