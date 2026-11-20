# ALDI produce prices

Updated 2026-11-20 from https://www.aldi.us/store/aldi/pages/fresh-produce (default store; prices change).
Updated daily by `.github/workflows/update-aldi-produce.yml`; run manually with `python3 scripts/fetch_aldi_produce.py --csv aldi-produce.csv --json aldi-produce.json && python3 scripts/build_md.py`.

| Item | Size | Price | Unit price |
|---|---|---|---|
| [Bananas, per lb](https://www.aldi.us/store/aldi/products/25720157-bananas-per-lb) | per lb | $0.16 each (est.) | $0.49 / lb |
| [Honeycrisp Apples](https://www.aldi.us/store/aldi/products/17770879-honeycrisp-apples-bag-2-lb) | 2 lb | $2.65 | $1.32 / lb |
| [Mandarin Oranges](https://www.aldi.us/store/aldi/products/16527122-mandarin-clementine-3-lbs) | 3 lb | $2.99 | $1.00 / lb |
| [Blackberries](https://www.aldi.us/store/aldi/products/17327025-blackberries-6-oz) | 6 oz | $2.55 | $6.80 / lb |
| [Blueberries](https://www.aldi.us/store/aldi/products/26312015-always-fresh-farms-blueberries-11-oz) | 11 oz | $4.75 | $6.91 / lb |
| [Fresh Navel Oranges](https://www.aldi.us/store/aldi/products/16553260-navel-orange-bag-4-lbs) | 4 lb | $2.69 | $0.67 / lb |
| [Raspberries](https://www.aldi.us/store/aldi/products/17327097-raspberries-package-6-oz) | 6 oz | $2.29 | $6.11 / lb |
| [Pomegranate](https://www.aldi.us/store/aldi/products/3254711-pomegranate-each) | 1 each | $1.89 | $1.89 / each |
| [Golden Kiwi](https://www.aldi.us/store/aldi/products/17328078-golden-kiwi-package-1-lb) | 1 lb container | $5.15 | $5.15 / lb |
| [Large Avocados, each](https://www.aldi.us/store/aldi/products/3111634-avocado-each) | 1 each | $0.75 | $0.75 / each |

10 items (only those in the page's initial HTML).
