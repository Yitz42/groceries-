#!/usr/bin/env python3
"""Rebuild aldi-produce.md from aldi-produce.json."""
import datetime, json

r = json.load(open("aldi-produce.json"))
L = [f"# ALDI produce prices\n\nUpdated {datetime.date.today().isoformat()} from https://www.aldi.us/store/aldi/pages/fresh-produce (default store; prices change).\nUpdated daily by `.github/workflows/update-aldi-produce.yml`; run manually with `python3 scripts/fetch_aldi_produce.py --csv aldi-produce.csv --json aldi-produce.json && python3 scripts/build_md.py`.\n",
     "| Item | Size | Price | Unit price |", "|---|---|---|---|"]
for x in r:
    L.append(f"| [{x['name']}]({x['url']}) | {x['size'] or ''} | {x['price_text'] or ''} | {x['unit_price'] or ''} |")
L.append(f"\n{len(r)} items (only those in the page's initial HTML).")
open("aldi-produce.md", "w").write("\n".join(L) + "\n")
