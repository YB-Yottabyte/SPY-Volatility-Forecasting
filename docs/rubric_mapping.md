# DAT 402 requirement mapping

The instructor’s project PDF and eight-category rubric are the reference. This map records technical coverage; subjective quality/creativity scores and the final grade remain the instructor’s decision.

| Rubric category | Points | Evidence in the final project |
|---|---:|---|
| Appropriate dataset, ≥500 observations, goal, cleaning | 10 | Notebook §§1–2; 4,631 development examples and 11 inputs; source audit, session calendar, finite/price/range checks; target definition |
| Appropriate EDA and descriptive statistics | 15 | Notebook §4; summary distributions, time history, correlations and predictor–target relationships, with observations |
| Train/test and validation/CV split | 5 | Notebook §3; pre-2026 development, new 2026 holdout, four expanding windows with five-origin purges |
| Missing data, scaling, encoding and feature engineering | 10 | Notebook §§2–3; no missing quotes after validation; backward-looking market features; Ridge scaling only within fit folds |
| Two distinct class-approved model types and meaningful tuning | 10 | Notebook §5; regularized linear regression (Ridge) and Random Forest; 9 Ridge penalties, 18 forest settings; common temporal CV and fixed seed |
| Train/test performance, appropriate metrics/plots, discussion | 20 | Notebook §§6–9; RMSE, MAE, R², QLIKE, two baselines, train/test comparison, forecast plots, interpretation and overfitting discussion |
| Creativity, quality and effort | 25 | Evidence includes justified target change, source repair, new-data evaluation, dependence-aware uncertainty, tests, reusable notebook functions and reproducibility; assessed by instructor |
| Report/talk format and source links | 5 | Executed `.ipynb`, HTML export and data references complete; user records/submits the talk separately |

## Additional project-PDF requirements

- **Dataset not used in class/homework:** user has confirmed eligibility. The final source panel is independently rebuilt market data, not a built-in teaching dataset.
- **Methods extend beyond homework:** temporal purging, fresh-data protocol, financial feature construction and dependent-outcome diagnostics provide substantive additional work. The user should be able to explain these decisions in the talk.
- **Reproducible splits/randomness:** chronological boundaries are deterministic; seed 402 fixes forest randomness and the bootstrap. A randomized split is inappropriate here and is not used.
- **No peeking:** the earlier sample is explicitly development data. The 2026 snapshot was downloaded after choices were frozen; source calendar QA occurred before any new-test metric calculation. Test results did not change the target, model settings, features, baseline selection, or forecasting policy.
- **Original work:** examples informed presentation only; their wording, code, data and results are not reused. The user should follow any additional course rules on assistance and attribution.
- **Group size:** individual work or at most two students, according to the instructions.

## Submission contents

Use the separate files in the repository; the assignment explicitly says not to ZIP files unless there are very many data files.

1. `spy_risk_forecasting.ipynb`: all analysis, modeling, and plotting code, with saved outputs.
2. `spy_risk_forecasting.html`: the required derived report.
3. `market_development.csv`, `market_holdout.csv`, and `market_training_data.csv`: all three input datasets.
4. `01_market_history.png` through `09_feature_influence.png`: the nine generated plots saved beside the notebook. Interpretation tables are included in the notebook.
5. `requirements.txt`, `README.md`, and supporting `docs/`: environment setup, source/protocol documentation, and requirement mapping.
6. The approximately 10-minute recorded talk, supplied separately by the student.

The notebook does not execute project `.py` files or read precomputed JSON reports. The historical modules and experiment scripts are not dependencies of this version. The HTML can be derived using standard Jupyter export or `jupyter nbconvert --to html spy_risk_forecasting.ipynb`.

## Check against the supplied project description

| Required step | Notebook evidence |
|---|---|
| 1. Dataset, prediction goal, cleaning | Sections 1–2; linked sources, calendar audit, valid-price/missingness checks; 4,631 development examples and 11 features |
| 2. Brief EDA | Section 4; distributions, descriptive statistics, correlations and predictor–target scatter plots |
| 3. Reproducible split, no test tuning | Section 3; deterministic dates, purged expanding folds, new 2026 holdout; seed 402 controls stochastic modeling |
| 4. Appropriate feature engineering | Section 2; backward-looking returns, rolling risk, log transformations; no categorical inputs requiring encoding |
| 5. Training-only rescaling | Ridge pipeline fits StandardScaler within each training fold; forest does not need scaling |
| 6. Two allowed models, meaningful tuning, selection | Section 5; regularized linear regression (Ridge), Random Forest; 9 and 18 configurations; selection by development CV RMSE |
| 7. Test metrics and performance plots | Section 6; RMSE, MAE, R², QLIKE, baselines, training/test comparison, prediction and actual-vs-predicted plots |
| 8. Results and implications | Sections 5–9; tuning plots, model comparison, dependence, overfitting, interpretation, limitations and conclusion |

Numerical and categorical inputs are an ideal, not a mandatory mix. Random splitting is suggested only where appropriate; shuffling these overlapping future time-series labels would undermine the evaluation. The instructions permit multiple datasets and do not require Kaggle as the only source. Dataset eligibility was confirmed by the student; talk participation and final quality judgments remain outside code verification.
