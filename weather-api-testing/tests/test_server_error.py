import requests
from unittest.mock import patch

@patch("source.weather.requests.get")
def test_server_error(mock_get, weather):
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()

    import pytest
    with pytest.raises(requests.exceptions.HTTPError):
        weather.get_temperature("London")