from sqlalchemy import select
from sqlalchemy.dialects.mysql import insert as mysql_insert
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from database import Location, WeatherRecord, DailyForecast


def get_or_create_location(session, item):
    statement = select(Location).where(
        Location.city == item["city"],
        Location.country == item["country"],
    )
    location = session.execute(statement).scalar_one_or_none()

    if location:
        return location

    location = Location(
        city=item["city"],
        country=item["country"],
        latitude=item["latitude"],
        longitude=item["longitude"],
        timezone=item["timezone"],
    )
    session.add(location)
    session.flush()
    return location


def _insert_ignore(session, model, values, unique_fields):
    dialect = session.bind.dialect.name

    if dialect == "sqlite":
        statement = sqlite_insert(model).values(**values).on_conflict_do_nothing(
            index_elements=unique_fields
        )
        result = session.execute(statement)
        return result.rowcount or 0

    if dialect == "mysql":
        statement = mysql_insert(model).values(**values).prefix_with("IGNORE")
        result = session.execute(statement)
        return result.rowcount or 0

    # Generic fallback
    filters = [getattr(model, field) == values[field] for field in unique_fields]
    exists = session.execute(select(model).where(*filters)).scalar_one_or_none()
    if exists:
        return 0
    session.add(model(**values))
    session.flush()
    return 1


def load_current(session, current_data):
    location = get_or_create_location(session, current_data)

    values = {
        "location_id": location.id,
        "recorded_at": current_data["recorded_at"],
        "temperature": current_data["temperature"],
        "apparent_temperature": current_data["apparent_temperature"],
        "humidity": current_data["humidity"],
        "pressure": current_data["pressure"],
        "wind_speed": current_data["wind_speed"],
        "precipitation": current_data["precipitation"],
        "weather_code": current_data["weather_code"],
        "weather_condition": current_data["weather_condition"],
        "is_day": current_data["is_day"],
    }
    return _insert_ignore(
        session,
        WeatherRecord,
        values,
        ["location_id", "recorded_at"],
    )


def load_daily(session, daily_records):
    loaded = 0

    for item in daily_records:
        location = get_or_create_location(session, item)
        values = {
            "location_id": location.id,
            "forecast_date": item["forecast_date"],
            "min_temperature": item["min_temperature"],
            "max_temperature": item["max_temperature"],
            "precipitation_sum": item["precipitation_sum"],
            "max_wind_speed": item["max_wind_speed"],
            "sunrise": item["sunrise"],
            "sunset": item["sunset"],
            "weather_code": item["weather_code"],
            "weather_condition": item["weather_condition"],
        }
        loaded += _insert_ignore(
            session,
            DailyForecast,
            values,
            ["location_id", "forecast_date"],
        )

    return loaded
