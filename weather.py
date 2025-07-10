# Utility functions here...
import requests
import logging
from config import API_KEY


def get_weather(city):
    """
    Fetches weather data for a given city from a weather API.

    Args:
        city (str): The name of the city to fetch the weather for.

    Returns:
        dict: Weather data for the city.
    """
    try:
        logging.info(f'Fetching weather data for {city}')
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f'Error fetching weather data: {e}')
        raise