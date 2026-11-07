# ALDI produce prices

Updated 2026-11-07 from https://www.aldi.us/store/aldi/pages/fresh-produce (default store; prices change).
Updated daily by `.github/workflows/update-aldi-produce.yml`; run manually with `python3 scripts/fetch_aldi_produce.py --csv aldi-produce.csv --json aldi-produce.json && python3 scripts/build_md.py`.

| Item | Size | Price | Unit price |
|---|---|---|---|
| [Bananas, per lb](https://www.aldi.us/store/aldi/products/25720157-bananas-per-lb) | per lb | $0.16 each (est.) | $0.50 / lb |
| [Apples 2lb](https://www.aldi.us/store/aldi/products/29080027-sugarbee-apples-2-lb) | 2 lb | $4.09 | $2.04 / lb |
| [Honeycrisp Apples](https://www.aldi.us/store/aldi/products/17770879-honeycrisp-apples-bag-2-lb) | 2 lb | $1.99 | $0.99 / lb |
| [Large Avocados, each](https://www.aldi.us/store/aldi/products/3111634-avocado-each) | 1 each | $0.75 | $0.75 / each |
| [Raspberries](https://www.aldi.us/store/aldi/products/17327097-raspberries-package-6-oz) | 6 oz | $1.49 | $3.97 / lb |
| [Mandarin Oranges](https://www.aldi.us/store/aldi/products/16527122-mandarin-clementine-3-lbs) | 3 lb | $2.99 | $1.00 / lb |
| [Red Grapes](https://www.aldi.us/store/aldi/products/305371-red-grapes-each) | 1 ct | $1.39 /lb | $1.39 /lb |
| [Kiwi](https://www.aldi.us/store/aldi/products/16767867-green-kiwi-package-1-lb) | 1 container | $4.39 | $4.39 / each |
| [Pomegranate](https://www.aldi.us/store/aldi/products/3254711-pomegranate-each) | 1 each | $1.29 | $1.29 / each |
| [Golden Kiwi](https://www.aldi.us/store/aldi/products/17328078-golden-kiwi-package-1-lb) | 1 lb container | $3.49 | $3.49 / lb |

10 items (only those in the page's initial HTML).
