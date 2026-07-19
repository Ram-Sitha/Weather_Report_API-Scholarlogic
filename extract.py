from typing import Any
import requests
from config import GEOCODING_URL, FORECAST_URL


def get_coordinates(city: str) -> dict[str, Any]:
    response = requests.get(
        GEOCODING_URL,
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json",
        },
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()

    results = data.get("results", [])
    if not results:
        raise ValueError(f"No location found for city: {city}")

    location = results[0]
    return {
        "city": location["name"],
        "country": location.get("country", ""),
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "timezone": location.get("timezone", "auto"),
    }


def fetch_weather(location: dict[str, Any]) -> dict[str, Any]:
    current_fields = [
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "precipitation",
        "weather_code",
        "surface_pressure",
        "wind_speed_10m",
        "is_day",
    ]
    daily_fields = [
        "weather_code",
        "temperature_2m_max",
        "temperature_2m_min",
        "sunrise",
        "sunset",
        "precipitation_sum",
        "wind_speed_10m_max",
    ]

    response = requests.get(
        FORECAST_URL,
        params={
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": ",".join(current_fields),
            "daily": ",".join(daily_fields),
            "timezone": location["timezone"],
            "forecast_days": 7,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()
