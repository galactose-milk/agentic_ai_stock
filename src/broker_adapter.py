from abc import ABC, abstractmethod

class BrokerAdapter(ABC):
    @abstractmethod
    def authenticate(self):
        """Authenticate with the broker API."""
        pass

    @abstractmethod
    def get_quote(self, ticker):
        """Get real-time quote for a ticker."""
        pass

    @abstractmethod
    def place_order(self, ticker, quantity, transaction_type, order_type="MARKET", product_type="DELIVERY"):
        """Place a buy/sell order."""
        pass

    @abstractmethod
    def get_positions(self):
        """Get current open positions."""
        pass

    @abstractmethod
    def get_holdings(self):
        """Get current holdings."""
        pass
