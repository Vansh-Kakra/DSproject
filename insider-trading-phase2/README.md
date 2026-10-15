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
about 1.31 GB. Price loading, cleaning, plots, and hypothesis tests remain to be added.
No network requests are made by the current notebook.

Suggested locations:
- `data/raw/sec/`: the supplied SEC tables.
- `data/raw/prices/`: the supplied stock-price data, including SPY.
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
