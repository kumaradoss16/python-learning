from unittest.mock import patch

@patch("source.weather.requests.get")
def test_get_api_called(mock_get, weather):
    mock_get.return_value.json.return_value = {
        "temperature": 25
    }

    mock_get.return_value.raise_for_status.return_value = None

    weather.get_temperature("Delhi")

    mock_get.assert_called_once_with(
        "https://api.weather-api.com/Delhi"
    )