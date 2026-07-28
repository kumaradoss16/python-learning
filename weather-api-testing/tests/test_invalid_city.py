import pytest
from unittest.mock import patch
 # Testing what happens when the API returns an error (such as 404 Not Found)
@patch("source.weather.requests.get")
def test_invalid_city(mock_get, weather):
    mock_get.return_value.raise_for_status.side_effect = Exception(
        "404 Not Found"
    )

    with pytest.raises(Exception):
        weather.get_temperature("ABC")


"""
requests.get()
  ↓
Mock
  ↓
raise_for_status()
  ↓
Exception
  ↓
pytest.raises()
  ↓
Passed
"""