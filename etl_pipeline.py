from datetime import datetime
from config import CITIES
from database import SessionLocal, ETLLog, create_tables
from extract import get_coordinates, fetch_weather
from transform import transform_current, transform_daily
from load import load_current, load_daily


def run_city_etl(city: str) -> None:
    session = SessionLocal()
    log = ETLLog(
        city=city,
        started_at=datetime.now(),
        status="RUNNING",
        records_loaded=0,
    )
    session.add(log)
    session.commit()

    try:
        location = get_coordinates(city)
        raw_weather = fetch_weather(location)

        current_record = transform_current(location, raw_weather)
        daily_records = transform_daily(location, raw_weather)

        loaded = load_current(session, current_record)
        loaded += load_daily(session, daily_records)

        log.status = "SUCCESS"
        log.records_loaded = loaded
        log.completed_at = datetime.now()
        session.commit()

        print(f"[SUCCESS] {city}: {loaded} new record(s) loaded")

    except Exception as exc:
        session.rollback()
        log = session.merge(log)
        log.status = "FAILED"
        log.error_message = str(exc)
        log.completed_at = datetime.now()
        session.commit()
        print(f"[FAILED] {city}: {exc}")

    finally:
        session.close()


def main() -> None:
    create_tables()
    for city in CITIES:
        run_city_etl(city)


if __name__ == "__main__":
    main()
