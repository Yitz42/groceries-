# ALDI produce prices

Updated 2026-11-09 from https://www.aldi.us/store/aldi/pages/fresh-produce (default store; prices change).
Updated daily by `.github/workflows/update-aldi-produce.yml`; run manually with `python3 scripts/fetch_aldi_produce.py --csv aldi-produce.csv --json aldi-produce.json && python3 scripts/build_md.py`.

| Item | Size | Price | Unit price |
|---|---|---|---|
| [Bananas, per lb](https://www.aldi.us/store/aldi/products/25720157-bananas-per-lb) | per lb | $0.15 each (est.) | $0.46 / lb |
| [Honeycrisp Apples](https://www.aldi.us/store/aldi/products/17770879-honeycrisp-apples-bag-2-lb) | 2 lb | $1.99 | $0.99 / lb |
| [Large Avocados, each](https://www.aldi.us/store/aldi/products/3111634-avocado-each) | 1 each | $0.55 | $0.55 / each |
| [Mandarin Oranges](https://www.aldi.us/store/aldi/products/16527122-mandarin-clementine-3-lbs) | 3 lb | $2.99 | $1.00 / lb |
| [Strawberries](https://www.aldi.us/store/aldi/products/16383764-whole-strawberries-1-lb) | 1 lb | $3.85 | $3.85 / lb |
| [Limes, each](https://www.aldi.us/store/aldi/products/25725888-limes-each) | 1 each | $0.25 | $0.25 / each |
| [Blackberries](https://www.aldi.us/store/aldi/products/17327025-blackberries-6-oz) | 6 oz | $2.75 | $7.33 / lb |
| [Red Grapes](https://www.aldi.us/store/aldi/products/305371-red-grapes-each) | 1 ct | $1.69 /lb | $1.69 /lb |
| [Blueberries](https://www.aldi.us/store/aldi/products/26312015-always-fresh-farms-blueberries-11-oz) | 11 oz | $4.75 | $6.91 / lb |
| [Raspberries](https://www.aldi.us/store/aldi/products/17327097-raspberries-package-6-oz) | 6 oz | $1.99 | $5.31 / lb |

10 items (only those in the page's initial HTML).
