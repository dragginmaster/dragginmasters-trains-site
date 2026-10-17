#!/usr/bin/env python3
"""Generate price-list.html — a static, crawler-friendly snapshot of every
comp in the price guide. Real HTML text (no JavaScript) so search engines
index the actual sold prices. Re-run after banking new comps:
    python3 build-price-list.py
Reads ~/workspace/dragginmasters-comps-data/comps.json, writes price-list.html
next to this script.
"""
import json, os, html
from collections import defaultdict

DATA = os.path.expanduser("~/workspace/dragginmasters-comps-data/comps.json")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "price-list.html")
BASE = "https://dragginmasterstrains.com"

d = json.load(open(DATA))
comps = d.get("comps", d)
updated = d.get("updated", "")[:10]

tiers = defaultdict(list)
for c in comps:
    tiers[(c["brand"], c["model"], c["scale"], c["control"])].append(c)

def money(v):
    return "$%.2f" % v

parts = []
parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Model Train Sold Prices — Full Price List | Dragginmasters Trains</title>
<meta name="description" content="Every sold listing in the Dragginmasters Trains model train price guide: real eBay sold prices for N and HO scale locomotives, with dates. %%NCOMPS%% verified comps and counting.">
<link rel="canonical" href="%%BASE%%/price-list.html">
<meta property="og:title" content="Model Train Sold Prices — Full Price List | Dragginmasters Trains">
<meta property="og:description" content="Every sold listing in the Dragginmasters Trains model train price guide: real eBay sold prices for N and HO scale locomotives, with dates. %%NCOMPS%% verified comps and counting.">
<meta property="og:type" content="website">
<meta property="og:url" content="%%BASE%%/price-list.html">
<meta property="og:image" content="%%BASE%%/icon-512.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Model Train Sold Prices — Full Price List | Dragginmasters Trains">
<meta name="twitter:description" content="Every sold listing in the Dragginmasters Trains model train price guide: real eBay sold prices for N and HO scale locomotives, with dates. %%NCOMPS%% verified comps and counting.">
<style>
:root{--navy:#16202e;--green:#2e7d43;--muted:#8a7f68;--line:#e4dcc8;--card:#fffdf6;}
body{font-family:system-ui,-apple-system,sans-serif;background:var(--card);color:var(--navy);margin:0;line-height:1.55;}
.wrap{max-width:860px;margin:0 auto;padding:20px 14px 60px;}
h1{font-size:26px;margin:6px 0;} h2{font-size:18px;margin:26px 0 6px;color:var(--navy);}
.lede{color:#444;max-width:640px;}
.tier{border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:14px 0;background:#fff;}
.tier h2{margin:0 0 4px;} .avg{color:var(--green);font-weight:700;}
table{border-collapse:collapse;width:100%;font-size:14px;margin-top:8px;}
th{background:var(--navy);color:#fff;text-align:left;padding:8px 10px;}
td{padding:8px 10px;border-top:1px solid var(--line);}
.meta{color:var(--muted);font-size:13px;} a{color:#b3541e;}
.topnav{margin:10px 0 20px;} .topnav a{margin-right:14px;}
.ref{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11.5px;color:var(--muted);cursor:pointer;white-space:nowrap;}
.ref:active{color:var(--navy);}
.printbtn{font:inherit;font-size:15px;padding:9px 16px;border:1px solid var(--line);border-radius:8px;background:#fff;cursor:pointer;margin:4px 0 12px;}
.printbtn:active{transform:translateY(1px);}
@media print{
  .topnav,.printbtn{display:none;}
  body{background:#fff;}
  .wrap{max-width:none;padding:0;}
  .tier{break-inside:avoid;border:1px solid #999;}
  th{background:#eee !important;color:#000;}
  h1{font-size:20px;}
  table{font-size:12px;}
}
</style>
</head>
<body><div class="wrap">
<div class="topnav"><a href="./">← Back to the price guide</a></div>
<button class="printbtn" onclick="window.print()">🖨 Print this list</button>
<h1>Model Train Sold Prices — Complete List</h1>
<p class="lede">Every verified sold listing behind the <a href="./">Dragginmasters Trains price guide</a>:
real eBay sold prices for N scale and HO scale model train locomotives, each one checked
against the actual sold listing. %%NCOMPS%% comps below, updated %%UPDATED%%. Prices shown are the final
sold prices; control types (DC, DCC-ready, DCC, DCC with sound) are kept on separate lines
because a decoder changes what a locomotive is worth.</p>
""".replace("%%NCOMPS%%", str(len(comps))).replace("%%UPDATED%%", updated).replace("%%BASE%%", BASE))

for (brand, model, scale, control) in sorted(tiers):
    rows = sorted(tiers[(brand, model, scale, control)], key=lambda r: r["date"])
    prices = [r["price"] for r in rows]
    avg = sum(prices) / len(prices)
    label = "%s %s — %s scale, %s" % (brand, model, scale, control)
    parts.append('<div class="tier">\n<h2>%s</h2>' % html.escape(label))
    parts.append('<div><span class="avg">%d sold — average %s, range %s to %s</span></div>'
                 % (len(rows), money(avg), money(min(prices)), money(max(prices))))
    parts.append('<table><thead><tr><th>Sold date</th><th>Road name</th><th>Price</th><th>Listing ID</th><th>Notes</th></tr></thead><tbody>')
    for r in rows:
        eid = str(r["ebayId"])
        parts.append('<tr><td>%s</td><td>%s</td><td><strong>%s</strong></td>'
                     '<td class="ref" title="Tap to copy" onclick="navigator.clipboard.writeText(\'%s\')">%s</td>'
                     '<td class="note">%s</td></tr>'
                     % (html.escape(r["date"]), html.escape(r.get("road") or "—"), money(r["price"]),
                        html.escape(eid), html.escape(eid), html.escape(r.get("note") or "")))
    parts.append('</tbody></table></div>')

parts.append("""<p class="meta">Dragginmasters Trains — an independent model train price guide.
Sold data is verified per listing; prices reflect what buyers actually paid.</p>
</div></body></html>""")

open(OUT, "w").write("\n".join(parts))
print("wrote %s (%d comps, %d tiers)" % (OUT, len(comps), len(tiers)))
