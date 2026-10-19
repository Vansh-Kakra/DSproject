# Phase 2 final check

Reviewed against the supplied `Phase2_rubric__INFO2950_FA26.pdf` on October 19, 2026.

## Execution and submission files

- All 30 code cells ran in order in a fresh Python kernel without errors, using the saved raw data. Price collection and the preregistered research models were not run.
- Notebook kernelspec remains `Python (2950)` / `2950`. The execution environment used the available Python 3.12 kernel with the required packages.
- Final event file: 27,820 rows and 25 columns, including 2,356 purchase and 25,464 sale events. The regenerated CSV is byte-for-byte identical to the committed event file.
- Returns are available for 2,227 purchase and 23,873 sale events at all four horizons.
- `phase2_insider_trading.ipynb` contains all executed outputs and six figures.
- `phase2_insider_trading.pdf` combines Parts 1 and 2 in one 43-page PDF. It was exported from the executed notebook through HTML, with wrapped code, repeated table headers, and wide preview tables transposed for printing. All page thumbnails and detailed table/chart pages were inspected for clipping and legibility.

## Rubric checklist

| Requirement | Evidence | Status |
|---|---|---|
| Research questions | Section 1, PDF p. 2: purchase signals, return horizons, roles, size, and the later plan extension. | Covered |
| Collection described in text | Section 2, pp. 3-7: source coverage, filenames, collection tools, recorded download date, and raw-data link. Collection code stays outside the notebook. | Covered |
| Reproducible cleaning | Section 3, pp. 8-24: membership intervals, transaction filters, amendments, role classification, historical matching, price preparation, and event returns, with executed code and explanatory text. | Covered |
| Intermediate files | Saved Datasets, p. 24: SEC trades, S&P trades, ticker links, membership intervals, and final events. | Covered |
| Multiple meaningful sources | SEC filings, historical index membership, and Yahoo prices are combined using company identifiers and dates. | Covered |
| Data description: rows and attributes | Section 4, pp. 25-27: event unit, counts, dates, missingness, and all 25 column definitions. | Covered |
| Data description: motivation | Section 4, Purpose: course project and disclosure-return research objective. | Covered |
| Data description: creation and preprocessing | Sections 2-4: sources, tools, procedures, transformations, and saved files. | Covered |
| Data description: observation mechanisms | Section 4: reporting obligations, index selection, vendor coverage, titles, and plan availability. | Covered |
| Data description: people and awareness | Section 4: public regulatory reporting, no research consent claim, identifiers and aggregation. | Covered |
| Data description: raw access and source credit | Sections 2 and 4 contain repository and original-source links and explain each source's contribution. | Covered |
| Data limitations | Section 6, pp. 37-38: gaps, selection, timing, dependence, confounding, model assumptions, classification, and implications for people. | Covered |
| EDA: relevant typical values and pairs | Section 5, pp. 28-36: summary tables and six motivated figures, including recent movement by direction and predictor correlations. | Covered |
| EDA informs project scope | Section 5.9, p. 36: log value, role grouping, plan-period restriction, return coverage, and mixed-week check. | Covered |
| Readability | Consistent chronological sections; every code cell begins with a comment and has preceding explanatory Markdown. Key points are highlighted. No em dashes or unfinished placeholders remain. | Covered |
| Language note | Title page states that the group does not include a native English speaker, as confirmed by Vansh. | Covered |
| Preregistration 1 | Section 7, pp. 39-40: cited motivation, hypothesis, sample, fixed purchase-versus-sale model, coefficient interpretation, exclusions, and sensitivity check. | Covered with prior-EDA disclosure |
| Preregistration 2 | Section 8, pp. 41-42: cited motivation, fixed role/size model, variable definitions, VIF, residual check, fixed 70/30 split, and test RMSE. | Covered with prior-EDA disclosure |
| Present analyses regardless of results | Both statements commit to reporting results regardless of direction and documenting later changes. No research models were executed. | Covered |
| Questions for reviewers | Section 9, p. 43: specific Phase 3 decisions; Vansh confirmed discussion with the group. | Covered |
| Combined executed PDF | One PDF contains the required sections for both parts. | Ready for upload |

## Remaining actions and interpretation limits

The remaining submission action is to upload the combined PDF to Gradescope. The review pull request is for the team; it does not submit the assignment or merge the branch.

The rubric score remains the instructor's judgment. In particular, separate purchase and sale outcome summaries were examined in EDA before the analysis plans were written. That exposure is disclosed in Statement 1; no claim of an outcome-blind preregistration is made. Missing prices, holiday/timestamp assumptions, and overlapping events remain documented study limitations, not resolved data gaps.
