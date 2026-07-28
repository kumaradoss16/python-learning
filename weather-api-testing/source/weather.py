import requests

class WeatherAPI:
    BASE_URL = "https://api.weather-api.com"

    def get_temperature(self, city):
        response = requests.get(f"{self.BASE_URL}/{city}")
        # checks the HTTP status code of the response.
        response.raise_for_status()
        data = response.json()
        return data["temperature"]

"""
Without Mocking:

WeatherAPI
    ↓
requests.get()
    ↓
Internet
    ↓
Weather Server
    ↓
JSON Response
"""