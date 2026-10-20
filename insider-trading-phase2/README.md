# Phase 2: Insider Disclosures and Stock Returns

1. **[Read the report (PDF)](phase2_insider_trading.pdf)**
2. **[View the analysis and code (Jupyter notebook)](phase2_insider_trading.ipynb)**

The notebook contains executed data preparation and exploratory analysis, followed by limitations, two planned Phase 3 analyses, and reviewer questions. Its saved tables and charts can be read on GitHub. The planned research models remain unrun.

## Files in This Folder

| File or folder | Purpose |
| --- | --- |
| `phase2_insider_trading.pdf` | Readable report exported from the notebook. |
| `phase2_insider_trading.ipynb` | Analysis code, explanations, tables, and charts. |
| `data/raw/` | SEC tables, historical membership, and saved price inputs. |
| `data/interim/` | Intermediate cleaned trade and matching files. |
| `data/processed/` | Membership intervals and the final event table. |
| `collect_prices.py` | Price-collection script retained for reproducibility. |
| `requirements.txt` | Python dependencies. |
| `.env.example` | Optional example environment settings. |
| `.gitignore` | Excludes local credentials and temporary files from Git. |

### Requirements and expected resources

A full notebook run requires the raw SEC source files, which total approximately **1.3 GB** across 24 quarterly releases. The project also uses historical S&P 500 membership data and saved daily price data. A full run needs several gigabytes of available memory because multiple SEC tables are loaded and merged in memory. Runtime depends on the computer used; loading the SEC source tables took about 17 seconds in the recorded run, while the complete notebook may take longer because it performs cleaning, matching, return calculations, table creation, and figure generation.

### What can be run without raw SEC files

The raw SEC files are required to reproduce the complete collection and cleaning pipeline from the beginning. However, the saved processed event dataset can be used to inspect the final analysis-ready sample and reproduce downstream descriptive analysis or Phase 3 modeling without reloading all raw source files.
The final analysis-ready dataset is available here: [`data/processed/insider_events.csv`](data/processed/insider_events.csv).
The saved intermediate files in `data/interim/` also allow reviewers to inspect cleaned transactions, S&P 500-matched trades, and ticker-to-CIK links without repeating every earlier processing step.

### Expected notebook outputs

After a successful full run, the notebook produces:
- combined SEC source tables and quarterly coverage checks;
- cleaned historical S&P 500 membership intervals;
- cleaned SEC purchase and sale transaction data;
- matched S&P 500 transaction records and ticker-to-CIK links;
- weekly stock and SPY returns;
- the final event-level dataset at [`data/processed/insider_events.csv`](data/processed/insider_events.csv);
- cleaning-funnel tables, coverage summaries, descriptive statistics, and EDA charts;
- documented limitations, planned Phase 3 analyses, and reviewer questions.

### Keeping the report current

The PDF report is an exported version of the notebook. If the notebook code, outputs, figures, or written explanations change, export a new `phase2_insider_trading.pdf` before submission so that the report matches the notebook and saved datasets.

## Run the Notebook

1. Download or clone the repository, including the data folders.
2. Open this folder in Jupyter or VS Code and install dependencies with `python -m pip install -r requirements.txt` in your Python environment.
3. Open `phase2_insider_trading.ipynb` and select the course Python environment. The saved kernel name is `2950`.
4. Restart the kernel and run all cells from top to bottom. Loading the raw SEC inputs requires approximately 1.3 GB of input files and additional memory for processing.

SEC inputs belong in `data/raw/sec/`, with four TSV tables per quarter across 2020-2025. Historical membership inputs belong in `data/raw/historical/`, and saved prices in `data/raw/prices/`. Keep these paths unchanged.

Use the saved prices. Do not rerun `collect_prices.py` for a normal notebook run. If you edit the notebook, export a new PDF so the report matches it.

[Back to the project overview](../README.md)
