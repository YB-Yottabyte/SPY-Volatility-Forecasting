# SPY Volatility Forecasting

This project forecasts SPY's annualized realized volatility over the next five trading sessions using recent market-risk signals. It compares Ridge Regression and Random Forest with recent-volatility baselines under chronological cross-validation and evaluates the selected model on a separate 2026 holdout period.

## Project highlights

- Builds 11 backward-looking features from SPY, VIX, HYG, IEF, and UUP market histories.
- Uses an NYSE session calendar and a five-session gap to preserve time order and prevent overlapping outcomes across training and validation boundaries.
- Tunes Ridge and Random Forest with time-series cross-validation.
- Evaluates frozen models on an untouched 2026 holdout using RMSE, MAE, R², QLIKE, and baseline skill.
- Examines performance during stressed conditions and interprets the selected model's feature influence.

## Repository contents

- `spy_risk_forecasting.ipynb`: complete executable analysis and report
- `spy_risk_forecasting.html`: rendered notebook for browser viewing
- `market_training_data.csv`: original Kaggle data used for the source-quality audit
- `market_development.csv`: Yahoo Finance development snapshot used for training and validation
- `market_holdout.csv`: separate Yahoo Finance snapshot used for final evaluation
- `01_market_history.png` through `09_feature_influence.png`: exported project figures
- `docs/data_card.md`: data provenance and intended use
- `docs/rubric_mapping.md`: mapping from project requirements to notebook sections
- `requirements.txt`: Python dependencies

## Run locally

1. Clone this repository.
2. Create a Python environment and install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Open `spy_risk_forecasting.ipynb` in Jupyter.
4. Select **Restart Kernel and Run All Cells**.

The three CSV files are versioned with the project, so the notebook runs without downloading fresh market data. All project code is contained in notebook cells, and the notebook recreates the nine figures beside itself.

## Data sources

- [Kaggle: U.S. Macroeconomic and Market Volatility Features](https://www.kaggle.com/datasets/ashwinprakashml/us-macroeconomic-and-market-volatility-features)
- [Yahoo Finance histories accessed through yfinance](https://ranaroussi.github.io/yfinance/)
- [NYSE trading calendar through pandas-market-calendars](https://github.com/rsheftel/pandas_market_calendars)

The Kaggle dataset is used only for a source-quality audit. The forecasting models use market-price histories recorded from Yahoo Finance; the two sources are not merged as model inputs.

## Authors

Sai Rithwik Kukunuri and Pranith Molakalapalli
