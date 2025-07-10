# Main bot code here...
import logging
from weather import get_weather
from config import CITY

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    """
    Main function to run the weather bot.
    """
    try:
        logging.info('Weather bot started')
        weather_data = get_weather(CITY)
        logging.info(f'Weather data for {CITY}: {weather_data}')
    except Exception as e:
        logging.error(f'Error occurred: {e}')


if __name__ == '__main__':
    main()
