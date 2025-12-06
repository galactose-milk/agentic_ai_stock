import pandas as pd
from datetime import datetime

class PaperTradingEngine:
    def __init__(self, initial_balance=100000.0):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.portfolio = {}  # {ticker: quantity}
        self.transaction_history = []
        self.portfolio_history = []

    def buy(self, ticker, price, quantity, timestamp=None):
        cost = price * quantity
        if cost > self.balance:
            print(f"Insufficient funds to buy {quantity} of {ticker} at {price}. Balance: {self.balance}")
            return False
        
        self.balance -= cost
        self.portfolio[ticker] = self.portfolio.get(ticker, 0) + quantity
        self._log_transaction("BUY", ticker, price, quantity, timestamp)
        print(f"BOUGHT {quantity} {ticker} @ {price}. New Balance: {self.balance:.2f}")
        return True

    def sell(self, ticker, price, quantity, timestamp=None):
        if self.portfolio.get(ticker, 0) < quantity:
            print(f"Insufficient holdings to sell {quantity} of {ticker}. Holdings: {self.portfolio.get(ticker, 0)}")
            return False
        
        revenue = price * quantity
        self.balance += revenue
        self.portfolio[ticker] -= quantity
        if self.portfolio[ticker] == 0:
            del self.portfolio[ticker]
            
        self._log_transaction("SELL", ticker, price, quantity, timestamp)
        print(f"SOLD {quantity} {ticker} @ {price}. New Balance: {self.balance:.2f}")
        return True

    def _log_transaction(self, type, ticker, price, quantity, timestamp):
        if timestamp is None:
            timestamp = datetime.now()
        self.transaction_history.append({
            "timestamp": timestamp,
            "type": type,
            "ticker": ticker,
            "price": price,
            "quantity": quantity,
            "balance": self.balance
        })

    def get_portfolio_value(self, current_prices):
        value = self.balance
        for ticker, quantity in self.portfolio.items():
            if ticker in current_prices:
                value += quantity * current_prices[ticker]
        return value

    def get_summary(self):
        return {
            "balance": self.balance,
            "portfolio": self.portfolio,
            "history_count": len(self.transaction_history)
        }
