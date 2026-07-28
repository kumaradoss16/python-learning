from unittest.mock import patch
import pytest

@pytest.mark.parametrize(
    "city,temp",
    [
        ("Delhi",40),
        ("Chennai",35),
        ("Mumbai",32),
        ("London",18),
        ("Tokyo",28),
    ]
)

@patch("source.weather.requests.get")
def test_multiple_cities(
        mock_get, weather, city, temp
):
    mock_get.return_value.json.return_value = {
        "temperature": temp
    }

    mock_get.return_value.raise_for_status.return_value = None

    assert weather.get_temperature(city) == temp