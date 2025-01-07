"""
Test suite for alchemy module.
"""

import unittest
from unittest.mock import patch
from src.alchemy_integration import web3

class TestAlchemyIntegration(unittest.TestCase):
    def test_web3_connection(self):
        self.assertTrue(web3.isConnected())

if __name__ == '__main__':
    unittest.main()
