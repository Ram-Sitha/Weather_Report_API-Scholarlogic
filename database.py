from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    Text,
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    city = Column(String(100), nullable=False)
    country = Column(String(100))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    timezone = Column(String(100))

    weather_records = relationship(
        "WeatherRecord", back_populates="location", cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("city", "country", name="uq_location_city_country"),
    )


class WeatherRecord(Base):
    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    recorded_at = Column(DateTime, nullable=False)
    temperature = Column(Float)
    apparent_temperature = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)
    wind_speed = Column(Float)
    precipitation = Column(Float)
    weather_code = Column(Integer)
    weather_condition = Column(String(100))
    is_day = Column(Integer)

    location = relationship("Location", back_populates="weather_records")

    __table_args__ = (
        UniqueConstraint(
            "location_id", "recorded_at", name="uq_location_recorded_at"
        ),
    )


class DailyForecast(Base):
    __tablename__ = "daily_forecasts"

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    forecast_date = Column(DateTime, nullable=False)
    min_temperature = Column(Float)
    max_temperature = Column(Float)
    precipitation_sum = Column(Float)
    max_wind_speed = Column(Float)
    sunrise = Column(DateTime)
    sunset = Column(DateTime)
    weather_code = Column(Integer)
    weather_condition = Column(String(100))

    __table_args__ = (
        UniqueConstraint(
            "location_id", "forecast_date", name="uq_location_forecast_date"
        ),
    )


class ETLLog(Base):
    __tablename__ = "etl_logs"

    id = Column(Integer, primary_key=True)
    started_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime)
    city = Column(String(100), nullable=False)
    status = Column(String(30), nullable=False)
    records_loaded = Column(Integer, default=0)
    error_message = Column(Text)


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)
