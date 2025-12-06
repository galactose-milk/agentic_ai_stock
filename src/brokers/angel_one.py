import os
from SmartApi import SmartConnect
from broker_adapter import BrokerAdapter
import pyotp

class AngelOneBroker(BrokerAdapter):
    def __init__(self):
        self.api_key = os.getenv("ANGEL_API_KEY")
        self.client_id = os.getenv("ANGEL_CLIENT_ID")
        self.password = os.getenv("ANGEL_PASSWORD")
        self.totp_key = os.getenv("ANGEL_TOTP_KEY")
        
        if not all([self.api_key, self.client_id, self.password, self.totp_key]):
            raise ValueError("Missing Angel One credentials in environment variables.")
            
        self.smart_api = SmartConnect(api_key=self.api_key)
        self.session = None

    def authenticate(self):
        try:
            totp = pyotp.TOTP(self.totp_key).now()
            data = self.smart_api.generateSession(self.client_id, self.password, totp)
            if data['status']:
                self.session = data
                print("Angel One Authentication Successful.")
                return True
            else:
                print(f"Authentication Failed: {data['message']}")
                return False
        except Exception as e:
            print(f"Authentication Error: {e}")
            return False

    def get_quote(self, ticker):
        # Note: Angel One uses tokens. We need a mapping or lookup.
        # For simplicity in this demo, we might need to fetch the token map first.
        # This is a complex part of Angel One API (fetching instrument list).
        # For now, we will assume the user provides the token or we use a lookup.
        # Returning a dummy structure for now as we need the instrument dump to map 'RELIANCE' to token.
        print(f"Getting quote for {ticker} (Not fully implemented without token map)")
        return {}

    def place_order(self, ticker, quantity, transaction_type, order_type="MARKET", product_type="DELIVERY"):
        # transaction_type: "BUY" or "SELL"
        try:
            orderparams = {
                "variety": "NORMAL",
                "tradingsymbol": ticker, # Needs to be exact symbol e.g. "RELIANCE-EQ"
                "symboltoken": "3045", # HARDCODED FOR RELIANCE FOR DEMO - TODO: Dynamic Lookup
                "transactiontype": transaction_type,
                "exchange": "NSE",
                "ordertype": order_type,
                "producttype": product_type,
                "duration": "DAY",
                "price": "0",
                "squareoff": "0",
                "stoploss": "0",
                "quantity": str(quantity)
            }
            order_id = self.smart_api.placeOrder(orderparams)
            print(f"Order Placed. ID: {order_id}")
            return order_id
        except Exception as e:
            print(f"Order Placement Failed: {e}")
            return None

    def get_positions(self):
        try:
            return self.smart_api.position()
        except Exception as e:
            print(f"Error fetching positions: {e}")
            return {}

    def get_holdings(self):
        try:
            return self.smart_api.holding()
        except Exception as e:
            print(f"Error fetching holdings: {e}")
            return {}
