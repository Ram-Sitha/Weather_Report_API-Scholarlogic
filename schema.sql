CREATE DATABASE IF NOT EXISTS weather_analytics;
USE weather_analytics;

CREATE TABLE IF NOT EXISTS locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100),
    latitude DOUBLE NOT NULL,
    longitude DOUBLE NOT NULL,
    timezone VARCHAR(100),
    CONSTRAINT uq_location_city_country UNIQUE (city, country)
);

CREATE TABLE IF NOT EXISTS weather_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    recorded_at DATETIME NOT NULL,
    temperature DOUBLE,
    apparent_temperature DOUBLE,
    humidity DOUBLE,
    pressure DOUBLE,
    wind_speed DOUBLE,
    precipitation DOUBLE,
    weather_code INT,
    weather_condition VARCHAR(100),
    is_day INT,
    CONSTRAINT fk_weather_location
        FOREIGN KEY (location_id) REFERENCES locations(id),
    CONSTRAINT uq_location_recorded_at
        UNIQUE (location_id, recorded_at)
);

CREATE TABLE IF NOT EXISTS daily_forecasts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    forecast_date DATETIME NOT NULL,
    min_temperature DOUBLE,
    max_temperature DOUBLE,
    precipitation_sum DOUBLE,
    max_wind_speed DOUBLE,
    sunrise DATETIME,
    sunset DATETIME,
    weather_code INT,
    weather_condition VARCHAR(100),
    CONSTRAINT fk_daily_location
        FOREIGN KEY (location_id) REFERENCES locations(id),
    CONSTRAINT uq_location_forecast_date
        UNIQUE (location_id, forecast_date)
);

CREATE TABLE IF NOT EXISTS etl_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    started_at DATETIME NOT NULL,
    completed_at DATETIME,
    city VARCHAR(100) NOT NULL,
    status VARCHAR(30) NOT NULL,
    records_loaded INT DEFAULT 0,
    error_message TEXT
);
