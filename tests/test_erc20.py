"""
Test suite for erc20 module.
"""

import unittest
from unittest.mock import Mock, patch
from src.erc20_utils import get_usdt_balance, get_token_info

class TestERC20Utils(unittest.TestCase):
    def setUp(self):
        self.mock_web3 = Mock()
        self.mock_contract = Mock()
        self.mock_web3.eth.contract.return_value = self.mock_contract

    def test_get_usdt_balance(self):
        self.mock_contract.functions.balanceOf().call.return_value = 1000000
        self.mock_contract.functions.decimals().call.return_value = 6
        
        balance = get_usdt_balance(
            self.mock_web3,
            "0xTestAddress",
            "0xContractAddress"
        )
        self.assertEqual(balance, 1.0)

if __name__ == '__main__':
    unittest.main()
