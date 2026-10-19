"""Collect daily adjusted stock prices for the insider-trading project.

This is the data COLLECTION step, kept outside the notebook as the Phase 2 rubric asks
(the notebook shows cleaning code, and describes collection in text).

What it does
------------
1. Reads every ticker that was in the S&P 500 at any point in the study window, from
   data/processed/historical_membership_clean.csv (built in the notebook's membership
   cleaning cells).
2. Adds SPY, the S&P 500 index fund we use as the market benchmark.
3. Downloads DAILY prices from Yahoo Finance via yfinance, from 2019-01-01 onward.
   The extra year before 2020 is needed to estimate each stock's beta (its usual
   sensitivity to the market) from the 52 weeks before an event.
   `auto_adjust=True` returns prices adjusted for splits and dividends, so returns
   computed from them reflect what a shareholder actually earned.
4. Saves data/raw/prices/daily_stock_prices.csv.gz (long format: one row per
   ticker-day) and data/raw/prices/daily_stock_prices_missing.csv listing symbols
   Yahoo could not return (mostly companies delisted after mergers).

Run from the insider-trading-phase2 folder:  python collect_prices.py
Downloaded once on 2026-10-19; the notebook only reads the saved file.
"""
from pathlib import Path

import pandas as pd
import yfinance as yf

START = "2019-01-01"
BENCHMARK = "SPY"
BATCH_SIZE = 50

here = Path(__file__).resolve().parent
membership = pd.read_csv(here / "data/processed/historical_membership_clean.csv")
tickers = sorted(set(membership["ticker"].dropna())) + [BENCHMARK]

# Yahoo writes share classes with a hyphen (BRK-B) where the index list uses a period (BRK.B).
yahoo_symbol = {t: t.replace(".", "-") for t in tickers}

frames, missing = [], []
for i in range(0, len(tickers), BATCH_SIZE):
    batch = tickers[i:i + BATCH_SIZE]
    data = yf.download([yahoo_symbol[t] for t in batch], start=START, interval="1d",
                       auto_adjust=True, group_by="ticker", progress=False, threads=True)
    for t in batch:
        sym = yahoo_symbol[t]
        if sym not in data.columns.get_level_values(0):
            missing.append(t)
            continue
        one = data[sym].dropna(subset=["Close"])
        if one.empty:
            missing.append(t)
            continue
        one = one[["Close", "Volume"]].reset_index().rename(columns=str.lower)
        one["ticker"] = t
        frames.append(one)
    print(f"Downloaded {min(i + BATCH_SIZE, len(tickers))}/{len(tickers)} tickers", flush=True)

# Batch downloads occasionally drop a symbol; retry each miss on its own before calling it missing.
still_missing = []
for t in missing:
    try:
        one = yf.download(yahoo_symbol[t], start=START, interval="1d", auto_adjust=True,
                          progress=False, multi_level_index=False)
    except Exception:
        one = pd.DataFrame()
    if one.empty or "Close" not in one or one["Close"].dropna().empty:
        still_missing.append(t)
        continue
    one = one.dropna(subset=["Close"])[["Close", "Volume"]].reset_index().rename(columns=str.lower)
    one["ticker"] = t
    frames.append(one)
print(f"Retry recovered {len(missing) - len(still_missing)} of {len(missing)} missed symbols", flush=True)
missing = still_missing

prices = pd.concat(frames, ignore_index=True)
prices["date"] = pd.to_datetime(prices["date"]).dt.tz_localize(None).dt.normalize()
prices = prices[["ticker", "date", "close", "volume"]].sort_values(["ticker", "date"])

# A few symbols come back with only a handful of rows (on 2026-10-19, AVB returned a single day).
# Too little history to compute returns, so treat them as missing rather than as real data.
MIN_DAYS = 20
days_per_ticker = prices.groupby("ticker")["date"].count()
too_short = sorted(days_per_ticker[days_per_ticker < MIN_DAYS].index)
prices = prices[~prices["ticker"].isin(too_short)]
missing = sorted(set(missing) | set(too_short))

out_dir = here / "data/raw/prices"
out_dir.mkdir(parents=True, exist_ok=True)
prices.to_csv(out_dir / "daily_stock_prices.csv.gz", index=False)
pd.DataFrame({"ticker": missing}).to_csv(out_dir / "daily_stock_prices_missing.csv", index=False)
print(f"Saved {len(prices):,} rows for {prices['ticker'].nunique()} tickers; {len(missing)} missing.")
