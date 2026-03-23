import pytest
from tdd_practice import StockBroker, should_execute_buy

@pytest.fixture
def mock_json_data():
    """
    Fixture representing a standardized JSON response 
    typically received from the Broker API.
    """
    return {
        "ticker": "AAPL",
        "last_price": 150.0,
        "volume": 1000000
    }

@pytest.fixture
def mocked_broker(monkeypatch, mock_json_data):
    """
    Fixture that patches the real StockBroker methods to return 
    mock data, preventing actual network requests during testing.
    """
    broker = StockBroker()

    # Define a fake method that mimics the real API behavior
    def fake_fetch(self, ticker):
        return mock_json_data

    # Use monkeypatch to replace the real method with our fake one
    monkeypatch.setattr(StockBroker, "fetch_market_data", fake_fetch)
    return broker

def test_should_buy_when_price_is_under_limit(mocked_broker):
    """Verify buy logic when market price (150.0) is under limit (160.0)."""
    assert should_execute_buy(mocked_broker, "AAPL", 160.0) is True

def test_should_not_buy_when_price_is_over_limit(mocked_broker, monkeypatch):
    """Verify logic when market price exceeds the limit."""
    # Override the fixture data locally for a specific edge case
    monkeypatch.setattr(mocked_broker, "fetch_market_data", lambda t: {"last_price": 200.0})
    
    assert should_execute_buy(mocked_broker, "AAPL", 160.0) is False
