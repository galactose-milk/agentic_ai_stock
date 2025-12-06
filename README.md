# Agentic AI Stock Trader

This project implements an autonomous stock trading agent using AI/ML techniques.

## Features

- **Data Fetching**: Fetches historical and live data using `yfinance` and `nsepython`.
- **Technical Analysis**: Calculates SMA, RSI, and other indicators.
- **Sentiment Analysis**: Uses BERT-based models (via `transformers`) to analyze news headlines.
- **Price Prediction**: Uses Random Forest (via `scikit-learn`) to predict future prices.
- **Paper Trading**: Simulates trading with a virtual portfolio.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Analyze a Stock
```bash
python src/main.py --ticker RELIANCE.NS --mode analyze
```

### Run Trading Agent
```bash
python src/main.py --ticker RELIANCE.NS --mode trade
```

## Project Structure

- `src/main.py`: Entry point.
- `src/trading_agent.py`: The core agent logic.
- `src/ml_models.py`: Machine Learning models (Sentiment & Price Prediction).
- `src/paper_trading.py`: Virtual portfolio management.
- `src/scraper.py`: Data fetching utilities.
- `src/analyzer.py`: Technical analysis utilities.
