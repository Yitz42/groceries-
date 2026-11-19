# ALDI produce prices

Updated 2026-11-19 from https://www.aldi.us/store/aldi/pages/fresh-produce (default store; prices change).
Updated daily by `.github/workflows/update-aldi-produce.yml`; run manually with `python3 scripts/fetch_aldi_produce.py --csv aldi-produce.csv --json aldi-produce.json && python3 scripts/build_md.py`.

| Item | Size | Price | Unit price |
|---|---|---|---|
| [Bananas, per lb](https://www.aldi.us/store/aldi/products/25720157-bananas-per-lb) | per lb | $0.14 each (est.) | $0.43 / lb |
| [Apples 2lb](https://www.aldi.us/store/aldi/products/29080027-sugarbee-apples-2-lb) | 2 lb | $4.09 | $2.04 / lb |
| [Honeycrisp Apples](https://www.aldi.us/store/aldi/products/17770879-honeycrisp-apples-bag-2-lb) | 2 lb | $2.65 | $1.32 / lb |
| [Mandarin Oranges](https://www.aldi.us/store/aldi/products/16527122-mandarin-clementine-3-lbs) | 3 lb | $2.99 | $1.00 / lb |
| [Large Avocados, each](https://www.aldi.us/store/aldi/products/3111634-avocado-each) | 1 each | $0.75 | $0.75 / each |
| [Kiwi](https://www.aldi.us/store/aldi/products/16767867-green-kiwi-package-1-lb) | 1 container | $4.39 | $4.39 / each |
| [Blackberries](https://www.aldi.us/store/aldi/products/17327025-blackberries-6-oz) | 6 oz | $2.55 | $6.80 / lb |
| [Fresh Navel Oranges](https://www.aldi.us/store/aldi/products/16553260-navel-orange-bag-4-lbs) | 4 lb | $2.69 | $0.67 / lb |
| [Pomegranate](https://www.aldi.us/store/aldi/products/3254711-pomegranate-each) | 1 each | $1.89 | $1.89 / each |
| [Raspberries](https://www.aldi.us/store/aldi/products/17327097-raspberries-package-6-oz) | 6 oz | $2.29 | $6.11 / lb |

10 items (only those in the page's initial HTML).
