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

## Run the Notebook

1. Download or clone the repository, including the data folders.
2. Open this folder in Jupyter or VS Code and install dependencies with `python -m pip install -r requirements.txt` in your Python environment.
3. Open `phase2_insider_trading.ipynb` and select the course Python environment. The saved kernel name is `2950`.
4. Restart the kernel and run all cells from top to bottom. Loading the raw SEC inputs requires approximately 1.3 GB of input files and additional memory for processing.

SEC inputs belong in `data/raw/sec/`, with four TSV tables per quarter across 2020-2025. Historical membership inputs belong in `data/raw/historical/`, and saved prices in `data/raw/prices/`. Keep these paths unchanged.

Use the saved prices. Do not rerun `collect_prices.py` for a normal notebook run. If you edit the notebook, export a new PDF so the report matches it.

[Back to the project overview](../README.md)
