import unittest
import os
from unittest.mock import patch, MagicMock
from shopee_api import generate_sign, generate_auth_link, get_access_token, refresh_access_token, make_api_call

class TestShopeeAPI(unittest.TestCase):

    def setUp(self):
        os.environ["SHOPEE_PARTNER_ID"] = "test_partner_id"
        os.environ["SHOPEE_PARTNER_KEY"] = "test_partner_key"
        from config import PARTNER_ID, PARTNER_KEY, BASE_URL, AUTH_URL
        self.PARTNER_ID = PARTNER_ID
        self.PARTNER_KEY = PARTNER_KEY
        self.BASE_URL = BASE_URL
        self.AUTH_URL = AUTH_URL

    def test_generate_sign_shop_api(self):
        path = "/api/v2/shop/get_shop_info"
        params = {
            "timestamp": 1678886400,
            "access_token": "test_access_token",
            "shop_id": 12345
        }
        expected_sign = "6042436411429997116744073617300974917631720743123617072617316741"
        sign = generate_sign(path, params)
        self.assertEqual(sign, expected_sign)

    def test_generate_sign_public_api(self):
        path = "/api/v2/public/get_token"
        params = {
            "timestamp": 1678886400
        }
        expected_sign = "7999711674407361730097491763172074312361707261731674160424364114"
        sign = generate_sign(path, params)
        self.assertEqual(sign, expected_sign)

    def test_generate_auth_link(self):
        redirect_url = "https://example.com/redirect"
        auth_link = generate_auth_link(redirect_url)
        self.assertIn(self.AUTH_URL, auth_link)
        self.assertIn(f"partner_id={self.PARTNER_ID}", auth_link)
        self.assertIn(f"redirect_url={redirect_url}", auth_link)
        self.assertIn("sign=", auth_link)

    @patch("requests.post")
    def test_get_access_token(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "new_access_token",
            "refresh_token": "new_refresh_token",
            "shop_id": 67890
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        main_account_id = "test_main_account"
        code = "test_code"
        response = get_access_token(main_account_id, code)
        self.assertEqual(response["access_token"], "new_access_token")
        self.assertEqual(response["shop_id"], 67890)

    @patch("requests.post")
    def test_refresh_access_token(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "refreshed_access_token",
            "refresh_token": "refreshed_refresh_token",
            "shop_id": 67890
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        shop_id = 67890
        refresh_token = "old_refresh_token"
        response = refresh_access_token(shop_id, refresh_token)
        self.assertEqual(response["access_token"], "refreshed_access_token")

    @patch("requests.get")
    def test_make_api_call(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": {"shop_name": "Test Shop"}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        path = "/api/v2/shop/get_shop_info"
        access_token = "some_access_token"
        shop_id = 12345
        response = make_api_call(path, access_token, shop_id)
        self.assertEqual(response["data"]["shop_name"], "Test Shop")

if __name__ == "__main__":
    unittest.main()


