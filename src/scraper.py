import yfinance as yf
from nsepython import nse_quote
import pandas as pd

def fetch_historical_data(ticker, period="1y"):
    """
    Fetches historical data for a given ticker using yfinance.
    
    Args:
        ticker (str): The stock ticker symbol (e.g., "RELIANCE.NS").
        period (str): The period for which to fetch data (e.g., "1y", "1mo").
        
    Returns:
        pd.DataFrame: Historical stock data.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        return hist
    except Exception as e:
        print(f"Error fetching historical data for {ticker}: {e}")
        return pd.DataFrame()

def fetch_live_data(ticker):
    """
    Fetches live data for a given ticker using nsepython.
    
    Args:
        ticker (str): The stock ticker symbol (e.g., "RELIANCE").
        
    Returns:
        dict: Live stock data.
    """
    try:
        # nsepython typically expects the symbol without .NS extension for NSE
        clean_ticker = ticker.replace(".NS", "").replace(".BO", "")
        quote = nse_quote(clean_ticker)
        return quote
    except Exception as e:
        print(f"Error fetching live data for {ticker}: {e}")
        return {}
