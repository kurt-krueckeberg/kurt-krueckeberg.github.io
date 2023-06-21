# Comments

This bibliography originally came from the now defunct `Genealoger.com`. It was extracted from the **October 16, 2021,
WayBackMachine** version of
[www.genealoger.com/german/ger_emigration_records.htm](https://web.archive.org/web/20230000000000*/http://www.genealoger.com/german/ger_emigration_records.htm).

Since the 2013 copyright (that was located in the footer in the October 16, 2021, WayBackMachine version) has expired, the [German Emigration Records](https://web.archive.org/web/20230000000000*/http://www.genealoger.com/german/ger_emigration_records.htm)
was converted to [Sphinx-doc and Restructured Text](https://www.sphinx-doc.org/en/master/).

Each entry is currently being double checked. Many broken links have been corrected, many other sources and their links added; in the case of broken links where no correct current link could be found, the entry was removed.

## Sphinx Subfolder

The `html` files in the root folder compise the actual website files of <https://kurt-krueckeberg.github.io>. They are copied to the root `cp -r Sphinx/_build/html` after they have been built using the `build` bash executabe
A python virtual environment is used to install Sphinx themes and Sphinx extension like `myst-parser` and to build the website files. This is done using the `build` exectuable:

```bash
#!/usr/bin/env bash
source ~/python-venv/bin/activate
cd sphinx
make clean && make html
cp -r _build/html/* ..
cd ..
deactivate
gadd 'updates'
```
