import yfinance as yf
import pandas as pd
from scraper import fetch_historical_data, fetch_live_data
from analyzer import calculate_technical_indicators
from paper_trading import PaperTradingEngine
from ml_models import SentimentAnalyzer, PricePredictor

class TradingAgent:
    def __init__(self, initial_balance=100000.0):
        self.engine = PaperTradingEngine(initial_balance)
        self.sentiment_analyzer = SentimentAnalyzer()
        self.price_predictor = PricePredictor()
        
    def get_news_sentiment(self, ticker):
        try:
            stock = yf.Ticker(ticker)
            news = stock.news
            if not news:
                return 0.0
            
            headlines = [item.get('title', '') for item in news]
            print(f"Analyzing {len(headlines)} news headlines...")
            sentiment_score = self.sentiment_analyzer.analyze(headlines)
            return sentiment_score
        except Exception as e:
            print(f"Error fetching news for {ticker}: {e}")
            return 0.0

    def run_strategy(self, ticker):
        print(f"\n--- Running Agent Strategy for {ticker} ---")
        
        # 1. Get Data
        hist_data = fetch_historical_data(ticker, period="2y") # Need enough data for training
        if hist_data.empty:
            print("No historical data. Aborting.")
            return

        hist_data = calculate_technical_indicators(hist_data)
        
        # 2. Train Model
        print("Training Price Predictor...")
        self.price_predictor.train(hist_data)
        
        # 3. Get Current State
        current_price = hist_data['Close'].iloc[-1]
        latest_data = hist_data.iloc[-1]
        
        # 4. Predict Next Price
        predicted_price = self.price_predictor.predict(latest_data)
        if predicted_price is None:
            return

        print(f"Current Price: {current_price:.2f}")
        print(f"Predicted Next Close: {predicted_price:.2f}")
        
        # 5. Get Sentiment
        sentiment_score = self.get_news_sentiment(ticker)
        print(f"News Sentiment Score: {sentiment_score:.2f}")
        
        # 6. Decision Logic
        # Strategy:
        # BUY if Predicted > Current * 1.01 (1% gain predicted) AND Sentiment > -0.2
        # SELL if Predicted < Current * 0.99 (1% loss predicted) OR Sentiment < -0.5
        
        decision = "HOLD"
        quantity = 10 # Fixed quantity for demo
        
        if predicted_price > current_price * 1.005 and sentiment_score > -0.2:
            decision = "BUY"
        elif predicted_price < current_price * 0.995 or sentiment_score < -0.5:
            decision = "SELL"
            
        print(f"Decision: {decision}")
        
        if decision == "BUY":
            self.engine.buy(ticker, current_price, quantity)
        elif decision == "SELL":
            self.engine.sell(ticker, current_price, quantity)
            
        # Summary
        print("\n--- Portfolio Summary ---")
        summary = self.engine.get_summary()
        print(f"Balance: {summary['balance']:.2f}")
        print(f"Holdings: {summary['portfolio']}")

