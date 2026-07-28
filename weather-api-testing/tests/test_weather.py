import pytest
from unittest.mock import patch

@patch("source.weather.requests.get")
def test_get_temperature(mock_get, weather):
    mock_get.return_value.json.return_value = {
        "temperature": 30
    }

    mock_get.return_value.raise_for_status.return_value = None

    result = weather.get_temperature("Chennai")

    assert result == 30