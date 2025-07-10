# Configuration code here...
import os

# Load environment variables
CITY = os.getenv('CITY', 'New York')
API_KEY = os.getenv('WEATHER_API_KEY')

if not API_KEY:
    raise ValueError('API_KEY environment variable is not set')
