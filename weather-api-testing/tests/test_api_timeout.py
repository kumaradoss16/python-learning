import requests
from unittest.mock import patch

@patch("source.weather.requests.get")   # Replace the real 'requests.get' with a fake one ('mock_get'); No internet is used
def test_timeout(mock_get, weather):
    # Whenever someone calls me, don't return anything. Immediately (side_effect) -> raise a Timeout exception
    mock_get.side_effect = requests.exceptions.Timeout   # Creates (simulates the exception

    import pytest
    # Checks (expects) the exception
    with pytest.raises(requests.exceptions.Timeout):
        weather.get_temperature("Mumbai")