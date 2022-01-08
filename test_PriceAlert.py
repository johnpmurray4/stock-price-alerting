import unittest
from mock import patch
import PriceAlert
from PriceAlert import checkPrices
from PriceAlert import sendEmail


class TestMain(unittest.TestCase):

    @patch('PriceAlert.sendEmail')
    @patch('PriceAlert.getPrice', return_value=165.0)
    def test_price_is_lower(self, mock_price, mock_email):
        checkPrices(["SNG.L,170,180"])
        self.assertTrue(mock_email.called)

    @patch('PriceAlert.sendEmail')
    @patch('PriceAlert.getPrice', return_value=185.0)
    def test_price_is_higher(self, mock_price, mock_email):
        checkPrices(["SNG.L,170,180"])
        self.assertTrue(mock_email.called)

    @patch('PriceAlert.sendEmail')
    @patch('PriceAlert.getPrice', return_value=175.0)
    def test_no_action(self, mock_price, mock_email):
        checkPrices(["SNG.L,170,180"])
        self.assertFalse(mock_email.called)


if __name__ == '__main__':
    unittest.main()
