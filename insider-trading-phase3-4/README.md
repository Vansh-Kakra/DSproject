# Insider Disclosures and Stock Returns: Phase 3

**[Read the Phase 3 report (PDF)](phase3_insider_trading.pdf)** · [View the executed Jupyter notebook](phase3_insider_trading.ipynb)

We studied public insider purchase and sale disclosures filed from 2020 through 2025 for companies that belonged to the S&P 500 at the time. We asked whether stocks performed better after purchases than after sales, and whether the size of a purchase or the participation of a senior executive helped explain what happened next.

## What we found

**Returns after purchases and sales.** We grouped disclosures by company, week, and trade direction. For each event, we measured how far the stock's weekly return was above or below what its past relationship with the market would predict. We added those differences over 13 weeks, the horizon chosen in Phase 2. Across 2,227 purchase events, the average cumulative abnormal return was **+2.13 percentage points**. Across 23,873 sale events, it was **−2.47 points**. The **4.60-point gap** remained positive when we excluded mixed buying and selling weeks and removed overlapping return periods within each company.

**Who bought and how much they spent.** Among purchases, events involving a C-suite executive averaged **2.18 percentage points higher** in the fitted model when purchase value and insider count were held constant. Larger purchases also had a positive estimated association. Yet on 690 later purchase events, the model's prediction error (root mean squared error) was **19.45 percentage points**, compared with **19.51** for simply predicting the earlier average every time. Knowing these details added little predictive value.

**How much confidence to place in the results.** For the uncertainty check, we kept one eligible event per company in each comparison so that frequent filers did not count repeatedly. After adjusting the intervals for four tests, the purchase average and the purchase-minus-sale gap were both above zero; the intervals for executive participation and purchase size included zero. These checks describe the smaller samples. Of the 537 events in the purchase-versus-sale check, 445 occurred in 2020. Different companies could have responded to the same news, so the check does not establish statistical significance for all 26,100 events.

## Data and reproducibility

The [cleaning notebook](data_cleaning.ipynb) explains how we combined SEC filings, historical index membership, and prices. It writes the [cleaned CSV files](data/processed/) used by the analysis. To reproduce the report, install the packages in [requirements.txt](requirements.txt), open [the analysis notebook](phase3_insider_trading.ipynb), select the 2950 kernel, restart it, and run all cells. The saved CSVs are included, so there is no need to download prices again.

The [rubric review](RUBRIC_REVIEW.md) maps the assignment requirements to report sections. The PDF linked above is the Phase 3 Gradescope deliverable. Both notebooks are available here for readers who want to inspect or reproduce the work.
