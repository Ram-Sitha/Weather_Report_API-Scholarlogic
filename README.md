# Weather Analytics ETL Pipeline

A complete beginner-friendly data engineering project that collects weather
data from Open-Meteo, transforms it with Python, stores it in a SQL database,
and generates graphs and FAQ answers.

## Architecture

```text
City name
   |
   v
Open-Meteo Geocoding API
   |
   v
Latitude + Longitude
   |
   v
Open-Meteo Forecast API
   |
   v
Extract -> Transform -> Load
   |
   v
SQLite / MySQL database
   |
   v
Pandas analysis -> Matplotlib graphs -> FAQ report
   |
   v
GitHub Actions automation
```

## 1. Requirements

Install:

- Python 3.11 or newer
- Git
- VS Code
- Optional: MySQL Server and MySQL Workbench
- GitHub account

No weather API key is required.

## 2. Download and open the project

```bash
git clone YOUR_REPOSITORY_URL
cd weather-analytics-etl
```

## 3. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install packages

```bash
pip install -r requirements.txt
```

## 5. Create the environment file

Windows:

```bash
copy .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

The default configuration uses SQLite:

```env
DATABASE_URL=sqlite:///weather.db
CITIES=Bengaluru,Chennai,Hyderabad,Mumbai,Delhi
```

## 6. Run the full project

```bash
python main.py
```

This command:

1. Creates database tables.
2. Finds the coordinates of every city.
3. Extracts weather data.
4. Validates and transforms the JSON data.
5. Loads current weather and seven-day forecasts.
6. Prevents duplicate records.
7. Creates CSV files.
8. Creates graphs.
9. Creates `reports/faq_report.md`.
10. Writes ETL success/failure logs.

## 7. View outputs

Open:

```text
reports/
├── current_weather.csv
├── daily_forecast.csv
├── faq_report.md
└── graphs/
    ├── city_temperature_comparison.png
    ├── max_temperature_trend.png
    ├── precipitation_by_city.png
    └── temperature_vs_humidity.png
```

## 8. Use MySQL instead of SQLite

Create the database:

```sql
CREATE DATABASE weather_analytics;
```

Update `.env`:

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/weather_analytics
```

Then run:

```bash
python main.py
```

The SQLAlchemy models create the required tables automatically. `schema.sql`
is also included for manual creation through MySQL Workbench.

## 9. Run files separately

Only ETL:

```bash
python etl_pipeline.py
```

Only analysis and graphs:

```bash
python analysis.py
```

Tests:

```bash
pytest
```

## 10. GitHub team workflow

Create these branches:

```text
feature/api-integration
feature/database
feature/etl
feature/analytics
feature/documentation-actions
```

Each member:

```bash
git checkout -b feature/branch-name
git add .
git commit -m "Describe completed work"
git push origin feature/branch-name
```

Then create a Pull Request, review it, and merge it into `main`.

## 11. GitHub Actions

The workflow is stored at:

```text
.github/workflows/weather-etl.yml
```

It runs:

- whenever code is pushed to `main`;
- whenever a Pull Request targets `main`;
- manually from the Actions page;
- every day at 06:00 IST.

The workflow installs Python, installs packages, runs tests, executes the ETL
pipeline, generates reports, and uploads the report folder as an artifact.

## Important production note

The GitHub workflow uses SQLite for demonstration. Each GitHub-hosted runner is
temporary, so its database does not permanently retain previous executions.
For a real scheduled history database, use a cloud MySQL/PostgreSQL database
and save its connection URL as a GitHub Actions secret.

## Team allocation

| Member | Work |
|---|---|
| 1 | `extract.py`, API research and error handling |
| 2 | `database.py`, `schema.sql`, SQL queries |
| 3 | `transform.py`, `load.py`, `etl_pipeline.py` |
| 4 | `analysis.py`, graphs and case study |
| 5 | Tests, README, GitHub Actions and integration |
