from transform import transform_current, transform_daily


LOCATION = {
    "city": "Bengaluru",
    "country": "India",
    "latitude": 12.97,
    "longitude": 77.59,
    "timezone": "Asia/Kolkata",
}


def test_transform_current():
    api_data = {
        "current": {
            "time": "2026-07-19T12:00",
            "temperature_2m": 26.5,
            "relative_humidity_2m": 70,
            "apparent_temperature": 28.0,
            "precipitation": 0.0,
            "weather_code": 2,
            "surface_pressure": 920.0,
            "wind_speed_10m": 12.0,
            "is_day": 1,
        }
    }
    result = transform_current(LOCATION, api_data)
    assert result["temperature"] == 26.5
    assert result["weather_condition"] == "Partly cloudy"


def test_transform_daily():
    api_data = {
        "daily": {
            "time": ["2026-07-19"],
            "weather_code": [61],
            "temperature_2m_max": [28.0],
            "temperature_2m_min": [20.0],
            "sunrise": ["2026-07-19T06:00"],
            "sunset": ["2026-07-19T18:45"],
            "precipitation_sum": [5.2],
            "wind_speed_10m_max": [18.0],
        }
    }
    result = transform_daily(LOCATION, api_data)
    assert len(result) == 1
    assert result[0]["weather_condition"] == "Slight rain"
