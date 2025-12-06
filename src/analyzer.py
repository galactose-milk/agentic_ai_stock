import pandas as pd
import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

def calculate_technical_indicators(df):
    """
    Calculates technical indicators (SMA, RSI) for the given DataFrame.
    
    Args:
        df (pd.DataFrame): Historical stock data with 'Close' column.
        
    Returns:
        pd.DataFrame: DataFrame with added indicator columns.
    """
    if df.empty:
        return df
    
    # Simple Moving Average (SMA)
    sma_50 = SMAIndicator(close=df["Close"], window=50, fillna=True)
    df["SMA_50"] = sma_50.sma_indicator()
    
    sma_200 = SMAIndicator(close=df["Close"], window=200, fillna=True)
    df["SMA_200"] = sma_200.sma_indicator()
    
    # Relative Strength Index (RSI)
    rsi = RSIIndicator(close=df["Close"], window=14, fillna=True)
    df["RSI"] = rsi.rsi()
    
    return df

def analyze_fundamentals(ticker):
    """
    Fetches fundamental data for a given ticker.
    
    Args:
        ticker (str): The stock ticker symbol.
        
    Returns:
        dict: Fundamental data (P/E, Market Cap, etc.)
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        fundamentals = {
            "Market Cap": info.get("marketCap"),
            "Trailing P/E": info.get("trailingPE"),
            "Forward P/E": info.get("forwardPE"),
            "Dividend Yield": info.get("dividendYield"),
            "52 Week High": info.get("fiftyTwoWeekHigh"),
            "52 Week Low": info.get("fiftyTwoWeekLow"),
        }
        return fundamentals
    except Exception as e:
        print(f"Error fetching fundamentals for {ticker}: {e}")
        return {}
