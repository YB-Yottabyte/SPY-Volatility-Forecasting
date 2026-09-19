# Data card

## Final question and sources

Forecast the annualized root-mean-square of SPY log returns over the **next five NYSE sessions**. Forecasts are defined after market data for the current session are available, at 17:00 America/New_York. This is a conditional risk estimate, not an executable closing-price trade.

| Instrument | Input interpretation | Source definition |
|---|---|---|
| SPY | US large-cap equity ETF: returns, trailing risk, downside moves, intraday range | [SPY historical data](https://finance.yahoo.com/quote/SPY/history/) |
| VIX | Option-implied S&P 500 volatility, approximately 30-day horizon | [Cboe VIX history and methodology context](https://www.cboe.com/tradable-products/vix/vix-historical-data) |
| HYG | High-yield corporate bond ETF return; a credit-market proxy | [iShares HYG](https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf) |
| IEF | 7–10 year Treasury bond ETF return; an interest-rate-market proxy | [iShares IEF](https://www.ishares.com/us/products/239456/ishares-710-year-treasury-bond-etf) |
| UUP | US dollar bullish ETF return; a currency-market proxy | [Invesco UUP](https://www.invesco.com/us-rest/contentdetail?contentId=a65d31ae-7cc2-47c9-96f1-78b47809af40&dnsName=us) |

Quotes are downloaded from Yahoo Finance through yfinance 0.2.64. VIX is downloaded through Yahoo as `^VIX`; Cboe is cited for its definition, not claimed as the direct download provider. The [yfinance history documentation](https://ranaroussi.github.io/yfinance/reference/yfinance.price_history.html) describes inclusive start and exclusive end dates and adjustment controls.

`repair=False` and `auto_adjust=False` preserve source OHLC fields. ETF log returns are computed from **adjusted-close ratios**; future multiplicative adjustment factors common to an interval cancel in ratios. Adjusted price levels themselves are not model features. SPY’s high/low ratio is scale invariant. Provider corrections can still revise history; this is not a full point-in-time vintage archive.

## Snapshots and audit trail

- Development: May 1, 2007–December 31, 2025, 4,699 session rows. The 63-session warm-up and five incomplete future-label rows leave 4,631 training examples.
- New-source snapshot: September 2, 2025–September 11, 2026. The overlap supports source consistency checks and trailing windows.
- New test: 169 origins from January 2–September 3, 2026, with outcomes ending by September 11.
- The provider returns two additional 2026 dates outside the NYSE calendar (May 25 and September 7). The calendar rule excludes them **before return calculation**. The initial validation stopped on these dates; no model metrics had been evaluated, and no model or target choices changed.
- Snapshot `.metadata.json` files store provider, symbols, retrieval timestamp, requested range, and SHA-256 checksum. `docs/evaluation_protocol.json` was written before the new download; `reports/final_results.json` records the first successful evaluation and protocol checksum.

The calendar includes exceptional closures, not just weekends or federal holidays. Validation rejects duplicate sessions, missing sessions, missing/nonfinite values, nonpositive prices, invalid ranges, and negative volume. It does not clip large but valid market movements or impute missing prices.

## Why the original prepared dataset was replaced

The [Kaggle panel](https://www.kaggle.com/datasets/ashwinprakashml/us-macroeconomic-and-market-volatility-features) has 6,179 observations, including 1,268 non-session rows whose SPY returns are all zero. Thirteen zero returns occur on real sessions and should not be dropped. Its documentation describes exponential-decay macro fills and precomputed transformations, whose availability histories are not established by the CSV.

The independent source check found matching SPY log returns on the overlapping real sessions (within 1e-5), supporting calendar/data-preparation repair rather than an allegation that all observations are incorrect. The final models exclude the prepared macro fields and rebuild all inputs directly. `reports/original_data_audit.json` records source provenance and counts; `scripts/audit_original.py` reproduces this optional audit if the original CSV is present.

## Features and target units

The feature list is fixed in the protocol: logged trailing 5/21/63-session RMS volatility; log VIX; five-session log VIX change; five-session SPY return; trailing downside RMS volatility; mean five-session high/low log range; and five-session HYG/IEF/UUP log returns.

Risk measures are annualized with 252 sessions per year. The target is `100 * sqrt(252 * mean(next_five_log_returns ** 2))`. It is not the sample standard deviation after subtracting a five-observation mean. Close-to-close sampling misses intraday variation and has measurement noise. A forecast of 20% annualized volatility does **not** mean a 20% price decline over the next week.

## Access and distribution

Raw market CSVs are kept locally for the class submission and ignored by Git by default; data remain subject to the original providers’ terms. The code, metadata, derived figures, and report identify how the study was made. Source histories can change, so preserving the exact snapshots is necessary to reproduce the published numerical results. Do not silently replace snapshot hashes or overwrite the frozen protocol after seeing test results.
