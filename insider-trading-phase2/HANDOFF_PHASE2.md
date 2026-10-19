# Phase 2 handoff: remaining Steps 4 to 8

This file tells any assistant (or teammate) exactly how to finish Phase 2 of our INFO 2950 project.
Steps 1 to 3 are done and pushed on branch `phase2-part1-sec-cleaning`. **Read this whole file before changing anything.**

---

## 0. Ground rules (from Vansh, the project owner)

1. **Source of truth:** the Phase 2 rubric (summarized in section 2 below). If anything conflicts with it, follow the rubric.
2. **Give finished work, not plans.** No asking permission for obvious next steps.
3. **Stay within the course.** Use only what INFO 2950 lectures 1 to 13 covered: pandas, numpy, DuckDB/SQL, seaborn/matplotlib, summary statistics, single and multivariable linear regression, log transformations, dummy variables, interaction terms, logistic regression, Pearson and Spearman correlation, collinearity/VIF, train/test split, MSE/RMSE/MAE/MAPE, `sklearn.linear_model.LinearRegression` and `LogisticRegression`. **Do not** introduce t-tests, statsmodels p-values, Fama-French factors, or other methods not in the lectures unless Vansh asks. Prefer the simplest approach that fully meets the rubric.
4. **Python in the existing Jupyter notebook** `insider-trading-phase2/phase2_insider_trading.ipynb`. All cleaning code lives in the notebook. Collection code lives in `collect_prices.py` (already done; **do not re-run it**: Yahoo rate-limits and the data is saved).
5. **Consistency:** keep existing variable names, column names, file paths, and the notebook's structure. Do not rename teammates' files. Leave the notebook kernelspec metadata as `{"display_name": "Python (2950)", "name": "2950", "language": "python"}`.
6. **Every code cell has a comment on its first line and is preceded by a markdown cell explaining its purpose** (this is the 3-point readability standard).
7. **Writing style:** complete sentences, headings for every section, bold/italics for key points, bullet lists where helpful. **Never use em dashes** (the long dash). Use commas, colons, parentheses, or separate sentences instead.
8. **Git:** commit to branch `phase2-part1-sec-cleaning` (never `main`), one commit per step, with a clear message describing what changed and the key numbers. Push after each step.
9. **Preregistration rule:** do **not** run the preregistered analyses (comparing CARs across roles, or testing whether the average purchase CAR is above zero with a model) before the preregistrations are written. EDA may describe distributions but must not compare C-suite vs other roles on returns.
10. **Before finishing, check the notebook against the rubric line by line** and report what is covered and what is still open.

When explaining work back to Vansh (for the oral defense): open with a plain-terms definition, define jargon inline at first use, spell out the causal chain step by step (why each choice, how each step leads to the next), build from small pieces up with concrete examples from our actual data, use a diagram only when structure calls for one, and list likely defense questions with answers. No em dashes.

---

## 1. Project context

- **Course:** INFO 2950 (Intro to Data Science), Cornell, Fall 2026. Group: Vansh Kakra (vk365), Dev Shukla (ds2395), Wilson Wang (ww576). Mentor: Saif Mahmud (sm2446).
- **Phase 2 deadline: Tuesday Oct 20, 2026, 4:30pm** (Gradescope, one PDF of the executed notebook).
- **Research question:** Do publicly disclosed insider open-market purchases (SEC Form 4) predict abnormal stock returns for S&P 500 companies, over what horizon (1, 4, 13, 26 weeks), and does the relationship differ by insider role, trade size, or pre-scheduled 10b5-1 plans?
- **Two sources merged:** (A) SEC Insider Transactions Data Sets (Forms 3/4/5, 24 quarters 2020q1 to 2025q4, in `data/raw/sec/`), (B) daily adjusted prices from Yahoo Finance via yfinance (`data/raw/prices/daily_stock_prices.csv.gz`), plus (C) historical S&P 500 membership from github.com/fja05680/sp500 (`data/raw/historical/`).

### What Steps 1 to 3 already produced (real numbers)

| Stage | Rows |
|---|---|
| Raw non-derivative transactions | 1,841,674 |
| 1a Forms 4 and 4/A only | 1,820,329 |
| 1b Purchase (P) and sale (S) codes | 711,439 |
| 1c Valid dates (lag 0 to 365 days), shares > 0, price > 0 | 700,020 |
| 1d Superseded amendment rows removed | 692,025 (154,660 P, 537,365 S) |
| 2b Company in S&P 500 on filing date | 127,529 |
| 2c Same trade under two CIKs removed | **127,368 (6,358 P, 121,010 S) in 593 companies** |

- S&P 500 purchases by role: C-suite 1,205; Director 3,633; Other officer 758; 10% owner 742; Other 20.
- Prices: 553 tickers with data plus SPY; 75 symbols missing (mostly acquired/delisted: TWTR, ATVI, SIVB, etc.). 540 of 593 companies have a usable price series. Trades in companies with no prices: 4,511 (271 purchases) in 53 companies.
- Weekly stock returns (Friday to Friday): median 0.32%, std 5.21%.
- The 10b5-1 checkbox (`plan_10b5_1`) exists only for filings from 2023 on; about 44% of 2023 to 2025 P/S trades are flagged.
- Filing lag after cleaning: median 2 days, 90th percentile 4 days, 99th percentile 78 days.

### Variables already defined in the notebook that later steps use

`df_trades_clean`, `df_roles`, `role_names`, `df_sp_trades` (S&P trades with `role`, `role_rank`, `sp_ticker`, `issuer_cik`, `owner_cik`, `filing_date`, `trade_value`, `plan_10b5_1`, `filing_lag_days`, `trans_code`), `df_ticker_cik`, `df_historical_clean`, `df_weekly` (columns `ticker`, `week`, `close`, `ret`, `mkt_ret`), `market`, `price_choice` (`issuer_cik`, `price_ticker`), `cleaning_log` (list of dicts), `raw_dir`, `interim_dir`, `processed_dir` (defined in the membership "Group by ticker" cell), `np`, `pd`, `sns`, `plt`, `display`.

### Notebook section order (current)

Title, Research questions, Importing, Data overview, Loading SEC data, Initial inspection, Preview, Loading membership, DATA COLLECTION AND CLEANING APPENDIX (Collection process, membership cleaning, Collecting stock prices, Step 1, Step 2, Step 3), **Saving intermediate and cleaned data**, EXPLORATORY DATA ANALYSIS (Summary statistics, Plots, What we learned), DATA DESCRIPTION, DATA LIMITATIONS, PREREGISTRATION STATEMENT 1, PREREGISTRATION STATEMENT 2, QUESTIONS FOR REVIEWERS.

---

## 2. Phase 2 rubric (summary; 3 points = "more developed")

**Submission:** one PDF of an executed Jupyter notebook containing: Research question(s); Data collection and cleaning (text describing collection, code + text for every cleaning step, intermediate files saved); Data description (Gebru et al. 2018 "Datasheets for Datasets" sections 3.1 to 3.5); Data limitations; Exploratory data analysis; Preregistration Statement 1; Preregistration Statement 2; Questions for reviewers.

| Category | What earns 3 points |
|---|---|
| Research questions | Clearly states complex research questions with significant potential for interesting analysis |
| Data cleaning | All necessary cleaning done; every step described in full detail so a reader could replicate it from raw data; multiple meaningfully different sources merged |
| Data description | Answers all relevant Datasheets questions thoroughly and credits/values the data sources |
| Data limitations | Creatively identifies potential harms and data gaps, how they affect the meaning of results, and the impact of results on people |
| EDA | Plots and summary stats identify typical values of relevant single variables and connections between pairs of relevant variables; methods carefully chosen (no "chart barf"); EDA used to confirm/update research questions and data description |
| Readability | Every point clear and simple; each code cell has a comment AND a markdown cell explaining it; each section has a heading; bold/italics highlight key points |
| Preregistration (x2) | Hypothesis + proposed analysis; concepts clearly defined; claims supported by prior research or domain knowledge; hypothesis clearly answerable by the proposed analysis; feasible with course tools |
| Questions for reviewers | Specific to our datasets, based on group discussion, and look toward the next stage of the project |

Required Datasheets questions: What are the observations and attributes? Why was this dataset created? How was it created (tools, procedures, sources)? What processes influenced what was observed and recorded? What preprocessing was done? If people are involved, were they aware and what purpose did they expect? Where can the raw source data be found (link hosted on GitHub, Cornell Google Drive, or Cornell Box)?

---

## 3. STEP 4: Build the event table and abnormal returns (code is written and tested)

Insert the cells below **immediately after the Step 3 cells (after the cell starting `# 3b. For each company`) and before the markdown cell `### Saving intermediate and cleaned data`**. They were tested on the full data and produce: **27,820 events (2,356 purchase events in 459 companies, 25,464 sale events in 582 companies)**; 26,100 events with an estimated beta (median beta 1.00, 5th to 95th percentile 0.25 to 1.89); CARs available for 2,227 purchase events and 23,873 sale events at every horizon. They save `data/processed/insider_events.csv`.

Then update the existing **"Saving intermediate and cleaned data"** markdown cell to list all saved files: `data/interim/sec_ps_trades.csv.gz` (Step 1), `data/interim/sp500_trades.csv.gz` and `data/interim/sp500_ticker_cik_links.csv` (Step 2), `data/processed/historical_membership_clean.csv` (membership), `data/processed/insider_events.csv` (Step 4, analysis-ready). Remove the bracketed placeholder text.

Also update the status line in the first notebook cell to say Steps 1 to 4 are complete.

Commit message: `Phase 2 Step 4: event table, market-model beta, and abnormal returns`.

**Cell 4.1 (markdown)**

````markdown
### Step 4: Building the event table and measuring abnormal returns

This step turns individual trades into the **analysis-ready dataset**. Each row is one *event*: a week in which insiders at one company bought (or sold), together with what the stock did afterward compared with what the market alone would predict.
````

**Cell 4.2 (markdown)**

````markdown
#### 4a. Roll trades up into company-week events

**Why not one row per trade?** An investor reading EDGAR asks one question per company per week: *did insiders buy here?* If a CEO and two directors all buy Boeing in the same week, that is one signal, not three, and counting it three times would let one busy company dominate the averages.

**Event week.** The SEC posts a filing to its public index the business day after it is received, so information becomes tradeable on *filing date + 1 business day*. The event week is the week ending on the first **Friday on or after** that date, and we assume an investor buys at that Friday's close. This rule never uses a price from before the public could know.

For each company, event week, and direction (P or S), we record:

- `n_trades` and `n_insiders`: how many trades and distinct insiders.
- `total_value`: the total dollar value traded, and `log_value`, its natural log. Trade sizes range from hundreds of dollars to hundreds of millions, so the log compresses that range for regression (as in Lectures 8 to 10).
- `role`: the **most senior** role among the traders that week, plus `any_c_suite` (1 if any C-suite officer traded).
- `any_plan_10b5_1`: 1 if any trade was marked as made under a pre-scheduled plan (available from April 2023).
- `mixed_week`: 1 if the same company had both insider buying and selling that week.
````

**Cell 4.3 (code)**

```python
# 4a. Assign each trade to its event week and aggregate to one row per company, week, and direction.
df_sp_trades["public_date"] = df_sp_trades["filing_date"] + pd.offsets.BDay(1)
# First Friday on or after the public date (rollforward leaves a date that is already a Friday unchanged).
df_sp_trades["event_week"] = df_sp_trades["public_date"].map(pd.offsets.Week(weekday=4).rollforward)

df_events = (df_sp_trades.groupby(["issuer_cik", "event_week", "trans_code"])
             .agg(issuer_name=("issuer_name", "first"), sp_ticker=("sp_ticker", "first"),
                  n_trades=("accession", "size"), n_insiders=("owner_cik", "nunique"),
                  total_value=("trade_value", "sum"), role_rank=("role_rank", "min"),
                  any_c_suite=("role_rank", lambda r: int((r == 1).any())),
                  any_plan_10b5_1=("plan_10b5_1", "max"), mean_filing_lag=("filing_lag_days", "mean"),
                  first_filing=("filing_date", "min"))
             .reset_index())
df_events["role"] = df_events["role_rank"].map(role_names)
df_events["log_value"] = np.log(df_events["total_value"])
both = df_events.groupby(["issuer_cik", "event_week"])["trans_code"].transform("nunique")
df_events["mixed_week"] = both.gt(1).astype(int)
df_events = df_events.merge(price_choice, on="issuer_cik", how="left")
print(df_events.groupby("trans_code").agg(events=("issuer_cik", "size"), companies=("issuer_cik", "nunique"),
                                          trades=("n_trades", "sum")).rename(index={"P": "purchases", "S": "sales"}).to_string())
```

**Cell 4.4 (markdown)**

````markdown
#### 4b. Expected returns from the market model

Stocks rise and fall with the market, so a stock going up after an insider buy proves nothing on its own. We need each stock's **expected** return: what it would normally do, given what the market did.

The **market model** describes a stock's weekly return as

$$r_{stock} = \alpha + \beta \cdot r_{market} + \varepsilon$$

- **β (beta)** measures how strongly the stock moves with the market. A β of 1.5 means that when SPY rises 1%, the stock typically rises 1.5%.
- **α (alpha)** is the stock's typical weekly return when the market is flat.
- **ε** is the part the market does not explain.

This is the single-variable linear regression from Lecture 7. For each event we fit it on the stock's **52 weekly returns before the event week** (the *estimation window*), requiring at least 40 weeks of data. Using only pre-event weeks matters: if post-event weeks were included, an insider's good news would leak into "normal" behavior and shrink the abnormal return we are trying to measure.

For a single input, the least-squares slope equals cov(stock, market) / var(market), and the intercept equals mean(stock) − β × mean(market). We use those closed-form formulas because they are exactly what `LinearRegression().fit()` returns, and are much faster across 30,000+ regressions.
````

**Cell 4.5 (code)**

```python
# 4b. Estimate alpha and beta for each event from the 52 weeks before its event week.
weekly_by_ticker = {t: g.set_index("week")[["ret", "mkt_ret"]].sort_index() for t, g in df_weekly.groupby("ticker")}
ESTIMATION_WEEKS, MIN_WEEKS = 52, 40

def market_model(ticker, event_week):
    """Return (alpha, beta, weeks used) from the 52 weeks strictly before event_week."""
    series = weekly_by_ticker.get(ticker)
    if series is None:
        return np.nan, np.nan, 0
    window = series.loc[:event_week - pd.Timedelta(days=1)].tail(ESTIMATION_WEEKS)
    if len(window) < MIN_WEEKS:
        return np.nan, np.nan, len(window)
    beta = np.cov(window["ret"], window["mkt_ret"])[0, 1] / window["mkt_ret"].var()
    alpha = window["ret"].mean() - beta * window["mkt_ret"].mean()
    return alpha, beta, len(window)

fits = [market_model(t, w) for t, w in zip(df_events["price_ticker"], df_events["event_week"])]
df_events[["alpha", "beta", "estimation_weeks"]] = pd.DataFrame(fits, index=df_events.index)
print(f"Events with an estimated beta: {df_events['beta'].notna().sum():,} of {len(df_events):,}")
print(df_events["beta"].describe(percentiles=[.05, .5, .95]).round(2).to_string())
```

**Cell 4.6 (markdown)**

````markdown
#### 4c. Abnormal and cumulative abnormal returns

For every week *after* the event week:

- **Abnormal return (AR)** = actual return − expected return = $r_{stock} - (\hat\alpha + \hat\beta \cdot r_{market})$
- **Cumulative abnormal return (CAR)** over *h* weeks = the sum of the weekly ARs from week 1 to week *h*.

A CAR of **+5%** at 13 weeks means the stock did 5 percentage points better over the following quarter than the market model predicted. We compute CAR at **1, 4, 13, and 26 weeks**, our short-to-medium horizons. A CAR is left missing when the stock lacks a full window of prices (for example, events in late 2025 whose 26-week window runs past our data).

We also compute **`car_pre4`**, the CAR over the 4 weeks *ending with* the event week. It is a diagnostic, not a result: it tells us whether prices were already moving before the public could know (for example, if insiders tend to buy after a price drop).
````

**Cell 4.7 (code)**

```python
# 4c. Abnormal returns: sum (actual - expected) over 1, 4, 13, 26 weeks after the event week, plus the 4 weeks ending with it.
HORIZONS = [1, 4, 13, 26]

def cumulative_abnormal_returns(ticker, event_week, alpha, beta):
    series = weekly_by_ticker.get(ticker)
    out = {f"car_{h}w": np.nan for h in HORIZONS} | {"car_pre4": np.nan}
    if series is None or np.isnan(beta):
        return out
    abnormal = series["ret"] - (alpha + beta * series["mkt_ret"])
    after = abnormal.loc[event_week + pd.Timedelta(days=1):]
    for h in HORIZONS:
        window = after.iloc[:h]
        # Require h consecutive weekly returns that end within h weeks plus a holiday buffer of the event week.
        if len(window) == h and (window.index[-1] - event_week).days <= 7 * h + 7:
            out[f"car_{h}w"] = window.sum()
    before = abnormal.loc[:event_week].tail(4)
    if len(before) == 4:
        out["car_pre4"] = before.sum()
    return out

cars = [cumulative_abnormal_returns(t, w, a, b) for t, w, a, b in
        zip(df_events["price_ticker"], df_events["event_week"], df_events["alpha"], df_events["beta"])]
df_events = pd.concat([df_events, pd.DataFrame(cars, index=df_events.index)], axis=1)
car_cols = [f"car_{h}w" for h in HORIZONS]
print("Events with each CAR available:")
print(df_events.groupby("trans_code")[car_cols + ["car_pre4"]].count().rename(index={"P": "purchases", "S": "sales"}).to_string())
```

**Cell 4.8 (markdown)**

````markdown
#### 4d. Save the analysis-ready dataset

The final file, `data/processed/insider_events.csv`, has one row per *(company, event week, direction)* and is the dataset described in the **Data description** section. Events without a usable price series or beta are kept in the file, so the sample-loss counts stay reproducible, but they are excluded from return analyses.

The cleaning log below summarizes the whole pipeline, from raw transactions to events.
````

**Cell 4.9 (code)**

```python
# 4d. Order columns, save the analysis-ready event table, and print the full cleaning funnel.
event_cols = ["issuer_cik", "issuer_name", "sp_ticker", "price_ticker", "trans_code", "event_week", "first_filing",
              "n_trades", "n_insiders", "total_value", "log_value", "role", "role_rank", "any_c_suite",
              "any_plan_10b5_1", "mixed_week", "mean_filing_lag", "alpha", "beta", "estimation_weeks",
              "car_pre4"] + car_cols
df_events = df_events[event_cols].sort_values(["event_week", "issuer_cik", "trans_code"]).reset_index(drop=True)
df_events.to_csv(processed_dir / "insider_events.csv", index=False)

has_returns = df_events["beta"].notna()
cleaning_log.append({"step": "4a. Trades rolled up into company-week events (rows = events)", "rows": len(df_events)})
cleaning_log.append({"step": "4b. Events with a price series and >= 40 weeks for beta", "rows": int(has_returns.sum())})
df_cleaning_log = pd.DataFrame(cleaning_log)
display(df_cleaning_log)
print(f"Saved {len(df_events):,} events ({df_events['trans_code'].eq('P').sum():,} purchase events, "
      f"{df_events['trans_code'].eq('S').sum():,} sale events) to data/processed/insider_events.csv")
display(df_events[df_events["trans_code"].eq("P")].head())
```


---

## 4. STEP 5: Exploratory data analysis

Fill the existing EDA section (replace placeholder cells `# Add summary statistics...` and `# Add focused Seaborn plots...` and the bracketed text). Use `df_events` (and `df_sp_trades` where trade-level detail is needed). Every plot: a markdown cell **before** saying why this plot matters for the research question, and a markdown cell **after** interpreting it with real numbers. No chart barf: about 5 to 6 plots total.

**Summary statistics cell(s):**
- Sample size table: trades, events, companies, date range, by trans_code; share of events with returns available.
- Typical values for purchase events: `total_value` (median, IQR; dollars), `n_insiders`, `beta`, `mean_filing_lag`, role counts, `any_plan_10b5_1` share (2023 on), `mixed_week` share.
- Distribution of CARs (mean, median, std, 5th/95th percentile) at each horizon for purchases and for sales **described separately**. This is a description of the outcome variable, not a hypothesis test; say so explicitly in the markdown.

**Plots (seaborn, each with title, axis labels with units):**
1. **Insider purchases and sales over time:** monthly count of purchase events and sale events (two lines or two panels). Purpose: show the sample's time coverage and whether buying clusters (expect a spike in March 2020 COVID crash when insiders bought dips).
2. **Distribution of purchase size:** histogram of `log_value` for purchase events, x-axis labeled with dollar ticks ($1k, $10k, $100k, $1M, $10M). Purpose: justify the log transform used in Preregistration 2.
3. **Who buys:** bar chart of purchase events by `role` (and maybe purchase vs sale share by role). Purpose: confirm each role group has enough events for the role comparison.
4. **Filing lag:** histogram of trade-level `filing_lag_days` for S&P trades, clipped at 30 days, with a vertical line at 2 business days. Purpose: check data timing quality and the event-date rule.
5. **Pre-event price movement (diagnostic):** distribution or boxplot of `car_pre4` for purchases vs sales. Purpose: are insiders buying after declines (contrarian buying)? This is allowed because `car_pre4` is a pre-period diagnostic, not a preregistered outcome.
6. **Relationship between two predictors:** scatter of `log_value` vs `beta` or a correlation matrix (Pearson and Spearman) of `log_value`, `n_insiders`, `beta`, `mean_filing_lag`, `any_c_suite` for purchase events. Purpose: check collinearity among planned regression inputs (Lecture 11).

Do **not** plot or compute average post-event CAR by role or by C-suite flag; that is Preregistration 2.

**"What we learned from the EDA"** markdown: 4 to 6 bullet findings with numbers, and explicitly state whether the research questions or data description change (for example: purchases are rare, about 2,356 events, so we focus on purchases with sales as a comparison; 10b5-1 flag only exists from 2023, so the plan-based question is limited to 2023 to 2025; the 26-week horizon loses late-2025 events, etc.).

Update the "Research questions" section at the top with a refined version if the EDA changes it (keep it a clear numbered list: main question plus 2 to 3 sub-questions, with "abnormal return" defined in plain terms).

Commit message: `Phase 2 Step 5: exploratory data analysis`.

---

## 5. STEPS 6 and 7: Written sections

Replace every bracketed placeholder in these sections with finished prose using real numbers from the notebook.

**Data overview cell (near top):** fill "Final company sample and retained observation counts" and "Shared raw-dataset link for reviewers" (use the GitHub repo link: https://github.com/Vansh-Kakra/DSproject, folder `insider-trading-phase2/data/raw/`).

**Collection process cell (top of appendix):** describe which SEC quarters were downloaded (2020q1 to 2025q4, quarterly zip files from https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets), the membership file source, the price download (`collect_prices.py`, Oct 19, 2026), and the raw filenames. Text only, no collection code.

**DATA DESCRIPTION** (Gebru datasheet style, headed subsections):
- *Motivation:* why created (test whether public insider disclosures carry information the market has not priced; relevant to market efficiency).
- *Composition:* rows = one (company, event week, direction) event; data dictionary table for every column of `insider_events.csv` (name, type, meaning, units). Counts and date range. Distinguish trade-level interim files from the event-level analysis file.
- *Collection and preprocessing:* sources, tools (pandas, DuckDB, yfinance), selection criteria, cleaning steps (refer to appendix Steps 1 to 4), transformations (log value, weekly returns, market model).
- *What influenced what was observed:* Section 16(a) reporting rules (only officers, directors, 10% owners file); 2-business-day deadline; S&P 500 scope from free price data; Yahoo missing delisted firms; 10b5-1 checkbox only from April 2023; self-reported titles.
- *People:* insiders are named individuals who file under legal obligation; they know filings are public but did not consent to research analysis; we analyze companies/events, not individuals, and do not infer illegal trading.
- *Where raw data is:* SEC link, fja05680/sp500 link, Yahoo Finance via yfinance, plus our GitHub raw folder link. Credit each source and its value (SEC = legally mandated primary source; community membership list; commercial price vendor).

**DATA LIMITATIONS** (numbered, each with "how this affects what we can conclude"):
survivorship/missing prices (75 symbols, 271 purchases lost, likely failures); S&P 500 only (large caps, where insider signals are weakest per literature); weekly granularity and the entry rule; overlapping events for the same company (CAR windows overlap, observations not independent); confounding news (earnings, buybacks around filings); market model estimated in volatile 2020; sales motivated by liquidity/taxes; 10b5-1 flag only from 2023; role titles self-reported and our C-suite regex may misclassify; amendments/joint filings; Yahoo adjusted prices are a vendor product (not CRSP). Then **harms and impact on people:** results must not be read as evidence that any named insider traded illegally; not investment advice; a positive finding could encourage copy-trading by retail investors who bear the risk; insiders' names are public but aggregating them could expose individuals.

**PREREGISTRATION STATEMENT 1** (replace draft):
- *Hypothesis:* The average 13-week cumulative abnormal return after S&P 500 insider **purchase** events is positive and larger than after **sale** events. Cite prior research: Lakonishok and Lee (2001) and Jeng, Metrick, and Zeckhauser (2003) found insider purchases are followed by abnormal returns while sales are much weaker.
- *Analysis:* Using purchase and sale events with available CARs, run a linear regression `car_13w ~ is_purchase` (dummy, sales = reference). The intercept estimates the average sale CAR and the coefficient the purchase minus sale difference; we test whether β_purchase > 0, and also report the purchase-only mean CAR at 1, 4, 13, 26 weeks. Report results regardless of significance. State the event unit, sample, entry rule (first Friday close on or after filing date + 1 business day), market model (52-week pre-event estimation window, at least 40 weeks), horizon, and exclusions (no price series, insufficient estimation data, `mixed_week` events kept but flagged; robustness: excluding them).

**PREREGISTRATION STATEMENT 2** (replace draft):
- *Hypothesis:* Among purchase events, those involving a **C-suite** officer and those with larger dollar value are followed by larger 13-week CARs. Motivation: executives have the broadest information (Cohen, Malloy, Pomorski 2012 on informative insiders; Seyhun 1986 on top executives), and larger purchases signal stronger conviction.
- *Analysis:* Multivariable linear regression on purchase events: `car_13w ~ any_c_suite + log_value + n_insiders`. (The 10b5-1 flag is left out of the main model because it only exists from 2023; mention it as a Phase 3 extension on the 2023 to 2025 subsample.) Test β_c_suite > 0 and β_log_value > 0. Interpret log_value as linear-log (Lecture 9: a 1% larger purchase is associated with a 0.01·β change in CAR). Check collinearity with a correlation matrix/VIF, check residual plot, and use a 70/30 train/test split (`random_state` fixed) to report RMSE on the test set, being careful that the split is random across events and noting the time-series caveat from Lecture 13. Optional secondary: logistic regression of `car_13w > 0` on the same inputs, interpreting odds ratios.

**QUESTIONS FOR REVIEWERS** (specific, from our group discussion, looking ahead to Phase 3), for example:
1. Is weekly data with the "first Friday close on or after filing date + 1 business day" entry rule acceptable, or should we move to daily returns for the 1-week horizon?
2. Overlapping events for the same company: should we keep only the first event per company within 26 weeks to make observations independent?
3. Is a market model with SPY enough, or do you expect a size/industry adjustment given that most of our sample is large-cap?
4. With 75 symbols missing from Yahoo (mostly acquired firms), is documenting the survivorship bias sufficient, or should we seek another price source?
5. For Preregistration 2, is our C-suite definition (CEO, CFO, COO, President) reasonable, and should directors be a separate dummy rather than the reference group?

Commit message: `Phase 2 Steps 6-7: data description, limitations, preregistrations, reviewer questions`.

---

## 6. STEP 8: Readability pass, final run, PDF

1. Title cell: group member names (Vansh Kakra vk365, Dev Shukla ds2395, Wilson Wang ww576), mentor, remove the "status" sentence, add a 2 to 3 sentence project summary. Note whether the group includes a native English speaker if relevant (rubric readability note).
2. Remove every remaining bracketed placeholder `[...]` and every "draft"/"to be completed" sentence. Search the notebook for `[` and `TODO`.
3. Confirm every code cell's first line is a comment and every code cell is preceded by a markdown cell.
4. Confirm **no em dashes** anywhere in the notebook (search for the long dash character).
5. Restart the kernel and run all cells top to bottom (about 3 minutes; needs about 8 GB RAM). Fix any error. Do **not** run `collect_prices.py`.
6. Export to PDF (`jupyter nbconvert --to pdf` or File > Save and Export As > PDF / print to PDF from HTML). Check that wide tables and plots are readable in the PDF.
7. Check the notebook against the rubric table in section 2, line by line; list what is covered and anything open.
8. Commit the executed notebook (and the PDF if the group wants it in the repo), push, and open a pull request from `phase2-part1-sec-cleaning` into `main` titled "Phase 2: complete notebook" for the team to review.

Commit message: `Phase 2 Step 8: readability pass and final executed notebook`.

---

## 7. Known pitfalls

- Raw SEC tables are 1.3 GB; loading takes about 1 minute. Peak memory about 5 GB.
- Some quarters store CIKs without leading zeros; Step 1 already pads them. Always treat CIKs as strings.
- `event_week` is a Friday date; weekly returns are indexed by Friday (`W-FRI`).
- `any_plan_10b5_1` is missing (NaN) before 2023, not 0. Do not fill it with 0.
- `mixed_week = 1` means the company had both buys and sells that week.
- Yahoo is rate-limiting; never re-download prices.
