# ALDI produce prices

Updated 2026-11-04 from https://www.aldi.us/store/aldi/pages/fresh-produce (default store; prices change).
Updated daily by `.github/workflows/update-aldi-produce.yml`; run manually with `python3 scripts/fetch_aldi_produce.py --csv aldi-produce.csv --json aldi-produce.json && python3 scripts/build_md.py`.

| Item | Size | Price | Unit price |
|---|---|---|---|
| [Bananas, per lb](https://www.aldi.us/store/aldi/products/25720157-bananas-per-lb) | per lb | $0.15 each (est.) | $0.44 / lb |
| [Honeycrisp Apples](https://www.aldi.us/store/aldi/products/17770879-honeycrisp-apples-bag-2-lb) | 2 lb | $1.99 | $0.99 / lb |
| [Large Avocados, each](https://www.aldi.us/store/aldi/products/3111634-avocado-each) | 1 each | $0.75 | $0.75 / each |
| [Kiwi](https://www.aldi.us/store/aldi/products/16767867-green-kiwi-package-1-lb) | 1 container | $4.39 | $4.39 / each |
| [Mandarin Oranges](https://www.aldi.us/store/aldi/products/16527122-mandarin-clementine-3-lbs) | 3 lb | $2.99 | $1.00 / lb |
| [Pomegranate](https://www.aldi.us/store/aldi/products/3254711-pomegranate-each) | 1 each | $1.29 | $1.29 / each |
| [Green Grapes, per lb](https://www.aldi.us/store/aldi/products/19242784-green-grapes-per-lb) | per lb | $4.03 /pkg (est.) | $1.79 / lb |
| [Strawberries](https://www.aldi.us/store/aldi/products/16383764-whole-strawberries-1-lb) | 1 lb | $3.09 | $3.09 / lb |
| [Red Grapes](https://www.aldi.us/store/aldi/products/305371-red-grapes-each) | 1 ct | $1.39 /lb | $1.39 /lb |
| [Raspberries](https://www.aldi.us/store/aldi/products/17327097-raspberries-package-6-oz) | 6 oz | $1.49 | $3.97 / lb |

10 items (only those in the page's initial HTML).
