class RiskManager:
    def __init__(self, max_daily_loss=5000, max_order_value=10000):
        self.max_daily_loss = max_daily_loss
        self.max_order_value = max_order_value
        self.daily_loss = 0
        self.restricted_tickers = ["PENNY_STOCK"]

    def validate_order(self, ticker, price, quantity, transaction_type):
        """
        Validates if an order can be placed based on risk rules.
        """
        order_value = price * quantity
        
        # 1. Check Max Order Value
        if order_value > self.max_order_value:
            print(f"Risk Reject: Order value {order_value} exceeds limit {self.max_order_value}")
            return False

        # 2. Check Restricted Tickers
        if ticker in self.restricted_tickers:
            print(f"Risk Reject: {ticker} is restricted.")
            return False

        # 3. Check Daily Loss (Simplified)
        # In a real system, we'd need to track realized + unrealized P&L live.
        if self.daily_loss > self.max_daily_loss:
            print(f"Risk Reject: Max daily loss {self.max_daily_loss} reached.")
            return False

        return True

    def update_loss(self, loss_amount):
        self.daily_loss += loss_amount
