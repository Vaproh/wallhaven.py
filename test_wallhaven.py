import unittest
import requests
from unittest.mock import patch, Mock
from wallhaven import WallhavenPY
from errors import WallhavenAPIError


class TestWallhavenPY(unittest.TestCase):
    def setUp(self):
        self.client = WallhavenPY(api_key="test_api_key", ssl_verify=True)

    @patch("wallhaven.requests.get")
    def test_get_success(self, mock_get):
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        result = self.client.get("test-endpoint")

        # Assert
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with(
            url="https://wallhaven.cc/api/v1/test-endpoint",
            verify=True,
            headers={"X-API-KEY": "test_api_key"},
        )

    @patch("wallhaven.requests.get")
    def test_get_http_error(self, mock_get):
        # Arrange
        mock_get.side_effect = requests.exceptions.HTTPError("HTTP error")

        # Act & Assert
        with self.assertRaises(WallhavenAPIError):
            self.client.get("test-endpoint")

    @patch("wallhaven.requests.get")
    def test_get_request_exception(self, mock_get):
        # Arrange
        mock_get.side_effect = requests.exceptions.RequestException("Request error")

        # Act & Assert
        with self.assertRaises(WallhavenAPIError):
            self.client.get("test-endpoint")

    @patch("wallhaven.requests.get")
    def test_get_json_error(self, mock_get):
        # Arrange
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("JSON error")
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act & Assert
        with self.assertRaises(WallhavenAPIError):
            self.client.get("test-endpoint")

    @patch("wallhaven.requests.get")
    def test_search_success(self, mock_get):
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        result = self.client.search(categories="general", purity="sfw")

        # Assert
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with(
            url="https://wallhaven.cc/api/v1/search",
            params={"categories": "general", "purity": "sfw"},
            verify=True,
            headers={"X-API-KEY": "test_api_key"},
        )

    def tearDown(self):
        import os

        if os.path.exists("test_file.json"):
            os.remove("test_file.json")


if __name__ == "__main__":
    unittest.main()
