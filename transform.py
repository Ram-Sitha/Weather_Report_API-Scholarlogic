from datetime import datetime
from typing import Any
from weather_codes import describe_weather


def parse_datetime(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None


def transform_current(
    location: dict[str, Any], api_data: dict[str, Any]
) -> dict[str, Any]:
    current = api_data.get("current", {})
    code = current.get("weather_code")

    required = ["time", "temperature_2m", "relative_humidity_2m"]
    missing = [field for field in required if current.get(field) is None]
    if missing:
        raise ValueError(f"Missing current-weather fields: {', '.join(missing)}")

    return {
        **location,
        "recorded_at": parse_datetime(current["time"]),
        "temperature": current.get("temperature_2m"),
        "apparent_temperature": current.get("apparent_temperature"),
        "humidity": current.get("relative_humidity_2m"),
        "pressure": current.get("surface_pressure"),
        "wind_speed": current.get("wind_speed_10m"),
        "precipitation": current.get("precipitation"),
        "weather_code": code,
        "weather_condition": describe_weather(code),
        "is_day": current.get("is_day"),
    }


def transform_daily(
    location: dict[str, Any], api_data: dict[str, Any]
) -> list[dict[str, Any]]:
    daily = api_data.get("daily", {})
    dates = daily.get("time", [])
    transformed = []

    for index, date_string in enumerate(dates):
        code = daily["weather_code"][index]
        transformed.append(
            {
                **location,
                "forecast_date": parse_datetime(date_string),
                "min_temperature": daily["temperature_2m_min"][index],
                "max_temperature": daily["temperature_2m_max"][index],
                "precipitation_sum": daily["precipitation_sum"][index],
                "max_wind_speed": daily["wind_speed_10m_max"][index],
                "sunrise": parse_datetime(daily["sunrise"][index]),
                "sunset": parse_datetime(daily["sunset"][index]),
                "weather_code": code,
                "weather_condition": describe_weather(code),
            }
        )

    return transformed
