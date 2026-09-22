# Data notes

## Question

The notebook estimates SPY's annualized realized volatility over the **next five NYSE trading sessions**. A forecast is made after the current session's market data are available. The target uses the root-mean-square of the following five daily log returns, annualized with 252 sessions per year.

## Files and sources

| File | Role | Source |
| --- | --- | --- |
| `data/market_training_data.csv` | Source-quality audit only | [Kaggle market and macroeconomic panel](https://www.kaggle.com/datasets/ashwinprakashml/us-macroeconomic-and-market-volatility-features) |
| `data/market_development.csv` | Training and cross-validation through 2025 | SPY, VIX, HYG, IEF, and UUP histories downloaded through [yfinance](https://ranaroussi.github.io/yfinance/reference/yfinance.price_history.html) |
| `data/market_holdout.csv` | New 2026 quotes and enough overlap for trailing features | The same yfinance histories |

VIX is downloaded through Yahoo Finance as `^VIX`. [Cboe's VIX page](https://www.cboe.com/tradable-products/vix/vix-historical-data) provides context for the index; it is not the direct source of the CSV quotes.

The three CSVs are saved in the repository so the analysis can run without downloading current prices. The repository reproduces results from these snapshots. It does not provide a script or complete provider metadata to recreate the exact original downloads.

## Coverage and checks

- Development quotes: May 1, 2007 through December 31, 2025, with **4,699 market sessions**. After the rolling-feature warm-up and incomplete future outcomes are removed, **4,631 examples** remain.
- Holdout evaluation: **169 forecast dates** from January 2 through September 3, 2026, with future outcomes ending by September 11.
- The original Kaggle panel has **6,179 rows**. Its **1,268 non-session rows** are excluded from model training. The notebook checks exchange dates rather than deleting all zero returns, since some real sessions also have zero returns.
- Market inputs are checked for duplicate or missing sessions, missing and nonfinite values, nonpositive prices, and invalid high/low ranges. The notebook does not fill missing prices or clip large valid moves.

The development and holdout files overlap to provide recent history. The notebook appends only holdout dates after the development period before building test features.

## Limits

SPY returns use adjusted-close ratios; the VIX input uses the index close. VIX measures a different horizon from the five-session target. Five future closing returns are a noisy measure of volatility, and neighboring targets overlap. Yahoo Finance may revise adjusted historical data. The snapshots are saved for repeatability, but they are not a full point-in-time data archive. Results from one partial-year holdout should not be treated as a trading signal.
