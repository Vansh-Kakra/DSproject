# Insider Disclosures and Stock Returns

**[Read the Phase 4 report (PDF)](phase4_insider_trading.pdf)**

[View the executed analysis notebook](phase4_insider_trading.ipynb)

We studied public insider purchase and sale disclosures filed from 2020 through 2025 for companies that belonged to the S&P 500 at the time. We asked whether stocks performed better after purchases than after sales, and whether the size of a purchase or the participation of a senior executive helped explain what happened next.

## What we found

We measured performance using **13-week cumulative abnormal return (CAR)**: the sum of a stock's weekly returns above or below what its earlier relationship with the market would predict.

**Purchases and sales showed different average outcomes:** Among 2,227 purchase events, average 13-week CAR was **+2.13 percentage points**. Among 23,873 sale events, it was **-2.47 points**, giving a **4.60-point purchase-minus-sale difference**. Both parts of the first hypothesis matched the observed direction: the purchase mean was positive and exceeded the sale mean. The difference also remained positive after excluding weeks with both buying and selling and after removing overlapping return periods within companies. The pattern therefore was not limited to the original sample definition, although these checks do not establish that purchases caused better performance.

**Executive involvement and purchase size had positive associations:** Within the full purchase sample, events involving a C-suite executive had fitted CARs **2.18 percentage points higher**, holding purchase value and insider count constant. Larger purchases also had a positive association, but its magnitude was small: a 1% increase in purchase dollars corresponded to about **0.0018 percentage points** higher fitted CAR. These estimates describe average relationships within the observed data. They do not show that every executive purchase performed well or that increasing a purchase would improve the stock's return.

**The uncertainty check provided narrower support:** In separate samples containing one eligible event per company, the adjusted confidence intervals were above zero for the purchase mean and purchase-minus-sale difference, but included zero for the executive and purchase-size coefficients. This provides conditional support for the first hypothesis in those smaller samples, while leaving the role and size relationships uncertain. The comparison sample was heavily concentrated in 2020, when companies could have responded to shared shocks. Its intervals therefore cannot establish significance for the full set of events.

**Predicting individual outcomes remained difficult:** We fitted the purchase model to earlier events and evaluated it on 690 later purchase events. Its root mean squared error, a measure of prediction error that gives greater weight to large misses, was **19.454 percentage points**, compared with **19.509 points** for always predicting the earlier purchase mean. The improvement was just **0.055 points**, or about **0.28%** of the baseline error. Executive participation, purchase size, and insider count therefore added little forecasting value on this test, despite their observed historical associations.

Taken together, the findings show why an average pattern and a useful investment forecast are different results. Purchase disclosures were followed by stronger average market-adjusted performance than sales, but the selected purchase characteristics did little to identify how a particular later event would perform. For someone researching a company, disclosures may provide context for further investigation alongside business fundamentals and contemporaneous news. This study does not demonstrate a profitable strategy for following insider trades: an executable strategy, its costs, and its performance on fresh data would still need to be evaluated.

## Data and reproducibility

The [cleaning notebook](data_cleaning.ipynb) explains how we combined SEC filings, historical index membership, and prices. It writes the [cleaned CSV files](data/processed/) used by the analysis. To reproduce the report, install the packages in [requirements.txt](requirements.txt), open [the analysis notebook](phase4_insider_trading.ipynb), select the 2950 kernel, restart it, and run all cells. The saved CSVs are included, so there is no need to download prices again.

The PDF above is exported from the current Phase 4 notebook, including its saved code outputs, tables, and figures. The revisions improve the writing and organization while preserving the analysis and results.

The original [Phase 3 report (PDF)](phase3_insider_trading.pdf) and [Phase 3 notebook](phase3_insider_trading.ipynb) remain available for comparison. The [Phase 3 rubric review](RUBRIC_REVIEW.md) records the earlier coverage check.
