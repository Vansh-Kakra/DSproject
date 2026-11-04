# Phase 3 rubric review

Reviewed against the INFO 2950 Phase III and IV rubric, Fall 2026, on November 4, 2026. This is a coverage review, not a prediction of the grade or certification of statistical assumptions.

| Requirement | Location and status |
|---|---|
| Introduction, context, clear questions, findings at end | Section 1 defines events and abnormal returns, states two questions, and summarizes results with qualifications. |
| Data purpose, rows and columns | Section 3 gives the observation unit, 27,820 rows, 25-column dictionary, and intended use. |
| Sources, collection, selection and reliability | Section 3 explains SEC disclosures, historical membership, prices, missingness, coverage, and source limitations. |
| Preprocessing and separate cleaning notebook | Sections 2-3 link `data_cleaning.ipynb`; analysis imports its saved CSV exports. Cleaning remains separate. |
| People, awareness and consent | Section 3 distinguishes mandatory public disclosure from consent to this research use. Section 12 discusses potential harms. |
| Accessible raw data and cleaned exports | Section 3 links the preserved Phase 2 snapshot and original sources; cleaned exports are included in this folder. |
| At least two preregistrations with hypotheses, methods and literature | Section 4 reproduces the submitted statements verbatim. Their original internal numbering is intentionally retained. |
| Execute planned analyses and disclose changes | Sections 5-9 contain both regressions, descriptive horizons, sensitivities, diagnostics, and a chronological prediction split. Section 5 records changes before model fitting. Section 10 discloses that inference design followed inspection of earlier results. |
| Summarizing, predicting, outliers/oddities | Sections 7-9 interpret coefficients, compare test RMSE with a training-mean baseline, and inspect training residuals. |
| Significance, decisions and interpretation | Section 10 includes explicit zero-null claims, bootstrap intervals, four-claim Bonferroni adjustment, and conditional reject/fail-to-reject decisions. **Substantive limitation:** intervals apply only to reduced one-event-per-company samples and assume sufficiently independent companies. Shared calendar shocks remain unresolved. These are not robust significance tests for the original full-event population. |
| Clear values, labels, plots and explanations | Tables label sample sizes and units. Residual and interval figures have explanations and interpretations. |
| Conclusions answer opening questions | Section 11 separates full-event associations, weak later-period prediction, and conditional reduced-sample inference. |
| Limitations, data gaps, harms and effects on conclusions | Section 12 addresses dependence, selection, measurement, omitted variables, prediction scope, privacy, reputational harm, and investment misuse. |
| Acknowledgements and formatted bibliography | Sections 13-14 credit data, literature, course materials, software, and AI assistance. |
| Writing and organization | Explanations precede code; each code cell starts with a comment. Main sections progress from questions and data to plans, results, inference, and conclusions. Language note omitted because the group confirmed it does not apply. |
| Fully executed notebook and PDF | All 16 analysis code cells rerun in order from a fresh Python process with saved outputs. PDF exported from that executed notebook. |
| Phase 4 incorporates feedback | Pending future Phase 3 feedback. Record each response and justify any decision not to follow a suggestion. |

## Verification and scope

- The analysis rerun reproduces the saved 26,100 eligible outcomes, 2,227 purchase events, fixed chronological split, regression estimates, and 10,000-draw bootstrap calculations.
- Original preregistration text and the `2950` kernel metadata are preserved.
- Submitted Phase 2 files and the separate cleaning notebook were not modified in this reporting step. This step reran the analysis, not raw-data collection or the full cleaning pipeline.
- The report uses the course's regression, train/test evaluation, row bootstrap, percentile intervals, and Bonferroni concepts. The event-selection rules are project design choices, not methods specifically prescribed by the lectures.
- No new model search, test-set tuning, or full-event dependence correction was introduced for report preparation.

## Remaining actions

1. Each group member should read the PDF and be able to explain the two questions, CAR, time split, and conditional inference. Confirm the acknowledgement accurately describes assistance used by the group.
2. Submit the executed PDF on Gradescope for Phase 3 by November 10, 2026. Pushing files to GitHub does not submit the assignment.
3. Attend the November 13 peer-review session, retain feedback, and prepare documented Phase 4 revisions for November 19, 2026.

The main unresolved scientific issue is cross-company dependence, especially the concentration of earliest events in 2020. It must remain visible in any submitted version; a positive conditional interval must not be described as conclusive evidence for all events.
