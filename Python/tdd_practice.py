import requests

class StockBroker:
    """
    Interface for interacting with a Stock Exchange API.
    In production, this would perform actual network calls.
    """
    def fetch_market_data(self, ticker):
        # Simulated network call to a financial API
        response = requests.get(f"https://api.generic-broker.com/v1/quote/{ticker}")
        return response.json()

def should_execute_buy(broker, ticker, limit_price):
    """
    Decision logic: Returns True if the current market price 
    is less than or equal to the user's limit price.
    """
    data = broker.fetch_market_data(ticker)
    current_price = data.get('last_price', 0)
    
    if current_price <= limit_price:
        return True
    return False
