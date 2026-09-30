#!/usr/bin/env python3
"""Fetch ALDI's Fresh Produce page and extract item prices.

The page (https://www.aldi.us/store/aldi/pages/fresh-produce, allowed by
aldi.us/robots.txt) server-renders its product data as URL-encoded JSON, so a
plain HTTP GET is enough; no browser needed.

Prices are for ALDI's default store/location and change often. Only the items
rendered in the initial HTML are returned (the rest lazy-load in the browser).

Usage:
  python3 scripts/fetch_aldi_produce.py            # print a table
  python3 scripts/fetch_aldi_produce.py --json out.json
  python3 scripts/fetch_aldi_produce.py --csv out.csv
"""
import argparse, csv, json, re, sys, urllib.parse, urllib.request

URL = "https://www.aldi.us/store/aldi/pages/fresh-produce"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def fetch(url=URL):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def unit_price(price, size, price_text, card_unit):
    """Best-effort "$x / lb" (or "/ each"); ALDI's own field is sometimes just the size."""
    if card_unit and "/" in card_unit:
        return card_unit
    if price_text and re.search(r"/\s*lb", price_text):
        return price_text
    m = re.match(r"([\d.]+)\s*(lb|oz|ct|each|container)", size or "")
    if price is None or not m or float(m.group(1)) == 0:
        return None
    qty, unit = float(m.group(1)), m.group(2)
    if unit == "lb":
        return f"${price / qty:.2f} / lb"
    if unit == "oz":
        return f"${price / qty * 16:.2f} / lb"
    return f"${price / qty:.2f} / each"


def parse(html):
    text = urllib.parse.unquote(html)
    dec = json.JSONDecoder()
    items = {}
    for m in re.finditer(r'\{"id":"(items_\d+-\d+)","itemLoadId"', text):
        try:
            o, _ = dec.raw_decode(text, m.start())
        except ValueError:
            continue
        p = (o.get("price") or {}).get("viewSection") or {}
        card = p.get("itemCard") or {}
        price = float(p["priceValueString"]) if p.get("priceValueString") else None
        price_text = card.get("priceString") or p.get("priceString")
        items[o["id"]] = {
            "id": o["productId"],
            "name": o["name"],
            "size": o.get("size"),
            "price": price,
            "price_text": price_text,
            "unit_price": unit_price(price, o.get("size"), price_text, card.get("pricingUnitString")),
            "url": f"https://www.aldi.us/store/aldi/products/{o['evergreenUrl']}" if o.get("evergreenUrl") else None,
        }
    return list(items.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--csv")
    a = ap.parse_args()
    rows = parse(fetch())
    if not rows:
        sys.exit("No items found; the page structure may have changed.")
    if a.json:
        json.dump(rows, open(a.json, "w"), indent=2)
    if a.csv:
        with open(a.csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows(rows)
    for r in rows:
        print(f"{r['name'][:48]:48} {r['size'] or '':10} {r['price_text'] or '':20} {r['unit_price'] or ''}")
    print(f"\n{len(rows)} items")


if __name__ == "__main__":
    main()
