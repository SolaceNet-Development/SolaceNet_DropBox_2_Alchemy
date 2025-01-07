"""
Test suite for crypto_host module.
"""

import unittest
from unittest.mock import patch, mock_open
from src.crypto_host import send_to_crypto_host

class TestCryptoHost(unittest.TestCase):
    @patch('requests.post')
    def test_send_to_crypto_host(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = "Success"
        
        with patch("builtins.open", mock_open(read_data="test data")):
            status, response = send_to_crypto_host("test.txt")
            self.assertEqual(status, 200)
            self.assertEqual(response, "Success")

if __name__ == '__main__':
    unittest.main()
