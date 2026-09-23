# DSproject
Data Science Project
- Most likely going with Idea 1 (Insider Trading) or Idea 3 (Land Acquistion Value Estimator)
- Idea 3 update: reframed from a plain value estimator into "is an underpriced house actually a bargain?" Zillow and Redfin ban scraping, so we'd backtest on Cook County public sales instead (~248k Chicago sales since 2012, ~77k repeat-sale pairs).
- Worry for Idea 3: a house that looks cheap is often cheap for a reason (bad condition). Plan is to use Chicago permits and violations to check, and subtract renovation spending before calling anything a deal.
- Idea 1 vs Idea 3: both join a signal to an outcome (Form 4 filing → stock returns, price gap → resale gain), and both break if we leak future data into the past. Deciding after mentor feedback.
