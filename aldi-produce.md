# ALDI produce prices

Updated 2026-11-18 from https://www.aldi.us/store/aldi/pages/fresh-produce (default store; prices change).
Updated daily by `.github/workflows/update-aldi-produce.yml`; run manually with `python3 scripts/fetch_aldi_produce.py --csv aldi-produce.csv --json aldi-produce.json && python3 scripts/build_md.py`.

| Item | Size | Price | Unit price |
|---|---|---|---|
| [Bananas, per lb](https://www.aldi.us/store/aldi/products/25720157-bananas-per-lb) | per lb | $0.16 each (est.) | $0.49 / lb |
| [Golden Kiwi](https://www.aldi.us/store/aldi/products/17328078-golden-kiwi-package-1-lb) | 1 lb container | $4.69 | $4.69 / lb |
| [Plums](https://www.aldi.us/store/aldi/products/16631392-plum-bag-2-lbs) | 2 lb | $3.99 | $2.00 / lb |
| [Red Grapes](https://www.aldi.us/store/aldi/products/305371-red-grapes-each) | 1 ct | $3.80 /pkg (est.) | $1.69 / lb |
| [Limes](https://www.aldi.us/store/aldi/products/17498856-lime-1-lb) | 1 lb | $2.45 | $2.45 / lb |
| [Cranberries 12oz](https://www.aldi.us/store/aldi/products/16631440-cranberries-package-12-oz) | 12 oz | $0.75 | $1.00 / lb |
| [Kiwi](https://www.aldi.us/store/aldi/products/16767867-green-kiwi-package-1-lb) | 1 container | $3.99 | $3.99 / each |
| [Honeycrisp Apples](https://www.aldi.us/store/aldi/products/17770879-honeycrisp-apples-bag-2-lb) | 2 lb | $2.39 | $1.20 / lb |
| [Pomegranate Arils](https://www.aldi.us/store/aldi/products/24314223-pomegranate-4-oz) | 4 oz | $3.69 | $14.76 / lb |
| [Pomegranate](https://www.aldi.us/store/aldi/products/3254711-pomegranate-each) | 1 each | $1.69 | $1.69 / each |

10 items (only those in the page's initial HTML).
