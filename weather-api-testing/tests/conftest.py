import pytest
from source.weather import WeatherAPI

@pytest.fixture
def weather():
    return WeatherAPI()