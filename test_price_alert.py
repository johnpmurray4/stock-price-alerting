import unittest
from mock import patch
import price_alert
from price_alert import check_prices
from price_alert import send_email


class TestMain(unittest.TestCase):

    @patch('price_alert.send_email')
    @patch('price_alert.get_price', return_value=165.0)
    def test_price_is_lower(self, mock_price, mock_email):
        check_prices(["SNG.L,170,180"])
        self.assertTrue(mock_email.called)

    @patch('price_alert.send_email')
    @patch('price_alert.get_price', return_value=185.0)
    def test_price_is_higher(self, mock_price, mock_email):
        check_prices(["SNG.L,170,180"])
        self.assertTrue(mock_email.called)

    @patch('price_alert.send_email')
    @patch('price_alert.get_price', return_value=170.0)
    def test_no_action(self, mock_price, mock_email):
        check_prices(["SNG.L,170,180"])
        self.assertFalse(mock_email.called)


if __name__ == '__main__':
    unittest.main()
