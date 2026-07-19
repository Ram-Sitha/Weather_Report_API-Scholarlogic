import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///weather.db")
CITIES = [
    city.strip()
    for city in os.getenv(
        "CITIES", "Bengaluru,Chennai,Hyderabad,Mumbai,Delhi"
    ).split(",")
    if city.strip()
]

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
