"""
Unittest-based test suite for the trading system

2026.03.23 / Powered by Gemini 3 Flash

This module contains test cases using the unittest framework and MagicMock
for mocking the StockBroker API interactions.

Run tests with:
    python3 ./tdd_unittest.py
"""

import unittest
from unittest.mock import MagicMock
from tdd_practice import StockBroker, should_execute_buy

class TestTradingSystem(unittest.TestCase):
    def setUp(self):
        """Initialize the broker instance before each test."""
        self.broker = StockBroker()
        self.ticker = "AAPL"

    def test_buy_decision_on_low_price(self):
        """Test that the system triggers a buy when the price is below the limit."""
        # Mocking the return value of the network-dependent method
        self.broker.fetch_market_data = MagicMock(return_value={'last_price': 150.0})
        
        # Scenario: Limit is 160.0, Market is 150.0 -> Should buy
        result = should_execute_buy(self.broker, self.ticker, 160.0)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
