# ALDI produce prices

Updated 2026-11-12 from https://www.aldi.us/store/aldi/pages/fresh-produce (default store; prices change).
Updated daily by `.github/workflows/update-aldi-produce.yml`; run manually with `python3 scripts/fetch_aldi_produce.py --csv aldi-produce.csv --json aldi-produce.json && python3 scripts/build_md.py`.

| Item | Size | Price | Unit price |
|---|---|---|---|
| [Bananas, per lb](https://www.aldi.us/store/aldi/products/25720157-bananas-per-lb) | per lb | $0.16 each (est.) | $0.50 / lb |
| [Honeycrisp Apples](https://www.aldi.us/store/aldi/products/17770879-honeycrisp-apples-bag-2-lb) | 2 lb | $2.35 | $1.18 / lb |
| [Large Avocados, each](https://www.aldi.us/store/aldi/products/3111634-avocado-each) | 1 each | $0.49 | $0.49 / each |
| [Blackberries](https://www.aldi.us/store/aldi/products/17327025-blackberries-6-oz) | 6 oz | $1.69 | $4.51 / lb |
| [Mandarin Oranges](https://www.aldi.us/store/aldi/products/16527122-mandarin-clementine-3-lbs) | 3 lb | $2.69 | $0.90 / lb |
| [Cranberries 12oz](https://www.aldi.us/store/aldi/products/16631440-cranberries-package-12-oz) | 12 oz | $0.75 | $1.00 / lb |
| [Kiwi](https://www.aldi.us/store/aldi/products/16767867-green-kiwi-package-1-lb) | 1 container | $4.39 | $4.39 / each |
| [Golden Kiwi](https://www.aldi.us/store/aldi/products/17328078-golden-kiwi-package-1-lb) | 1 lb container | $5.19 | $5.19 / lb |
| [Red Grapes](https://www.aldi.us/store/aldi/products/305371-red-grapes-each) | 1 ct | $1.69 /lb | $1.69 /lb |
| [Fresh Navel Oranges](https://www.aldi.us/store/aldi/products/16553260-navel-orange-bag-4-lbs) | 4 lb | $2.99 | $0.75 / lb |

10 items (only those in the page's initial HTML).
