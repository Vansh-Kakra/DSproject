# Insider trading project - Phase 2 starter

This is a simple notebook outline modeled on the supplied past-year InvestmentFunds
example, with the sections required by the current Phase 2 rubric. It includes
SciPy, NumPy, DuckDB, Seaborn, Pandas, and Matplotlib imports.

Open `phase2_insider_trading.ipynb` in VS Code or Jupyter. Install `requirements.txt`
in the selected Python environment. All project code will live in the notebook;
there are no separate extraction or cleaning scripts.

The notebook now loads the four required SEC table types from all 24 quarters
in 2020-2025, labels each row with its source quarter, and displays input row counts.
Run the imports and loading cells from this folder (or from the repository root).
The first loading check read all 96 TSVs in about 40 seconds on this computer;
performance and memory use vary across machines. The uncompressed inputs total
about 1.31 GB. Historical membership also has a loading cell. Weekly stock-price collection via yfinance is prepared after the ticker grouping.
SEC and price cleaning, plots, and hypothesis tests remain to be added.
The weekly-price cell keeps saved Yahoo Finance downloads and retries missing
tickers. Verified ticker changes are mapped, and AVB daily prices are aggregated
to weekly bars. Prices are saved to `data/raw/prices/weekly_stock_prices.csv`;
unresolved symbols and error messages are saved to `weekly_stock_prices_missing.csv`
in the same folder. Other loading cells read local files.

Historical membership cleaning is now implemented in the cleaning appendix. It
retains the starting snapshot and changes covering the actual SEC filing dates,
then creates `df_historical_clean` with ticker/date coverage intervals. The saved
output is `data/processed/historical_membership_clean.csv`. Its end dates are
exclusive; parse all three date columns when reloading the CSV. Raw inputs are
preserved. SEC transaction and company-price cleaning remain to be completed.


Suggested locations:
- `data/raw/sec/`: the supplied SEC tables.
- `data/raw/historical/`: the supplied historical S&P 500 membership CSV.
- `data/raw/prices/`: the weekly company-price CSV saved by the yfinance cell.
  A separate market-benchmark series remains to be collected.
- `data/interim/`: intermediate cleaning files, if useful.
- `data/processed/`: final cleaned files.

The draft preregistrations must be completed before their tests are run. Replace
bracketed prompts with actual information before submission. The finished notebook
must be executed on real data and exported to PDF; this starter is not a completed
Phase 2 submission.

For GitHub, `.gitignore` excludes local credentials, environments, and temporary
notebook files. Dataset folders are not ignored. An optional `.env.example` is
provided for future API access; each teammate can make their own local `.env`.
The starter does not use an API key. Do not commit an actual key or print it in
saved notebook outputs. Nothing has been uploaded to GitHub.
