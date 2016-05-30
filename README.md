# medicines-crawler
Get **trade names** and **pharmaceutical group names** from supported Pharmaceutical Companies by parsing their site.

**The output data will be available as JSON.**

---
## Supported Companies
* ACME Laboratories Ltd.
* BIOPHARMA Ltd. \* _(This one is a bit fragile)_
* Incepta Pharmaceuticals Ltd.
* Square Pharmaceuticals Ltd.

_Please contribute so that we can add more companies to this list. Make a PR or an Issue to help out._

## Usage
Just download and run `crawler.py`
```bash
python3 crawler.py
```

Alternatively you can make the file executable and run it
```bash
chmod +x crawler.py
./crawler.py
```

## _Note_
If you don't want to download and run the app yourself you can just use my files in the `output_data` directory live from GitHub.
I will try to keep them up to date as much as I can.
