from pathlib import Path
import pandas as pd
from sqlalchemy import text
from database import engine

REPORT_DIR = Path("reports")
GRAPH_DIR = REPORT_DIR / "graphs"
REPORT_DIR.mkdir(exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)


CURRENT_QUERY = """
SELECT
    l.city,
    l.country,
    w.recorded_at,
    w.temperature,
    w.apparent_temperature,
    w.humidity,
    w.pressure,
    w.wind_speed,
    w.precipitation,
    w.weather_condition
FROM weather_records w
JOIN locations l ON l.id = w.location_id
ORDER BY w.recorded_at
"""

DAILY_QUERY = """
SELECT
    l.city,
    d.forecast_date,
    d.min_temperature,
    d.max_temperature,
    d.precipitation_sum,
    d.max_wind_speed,
    d.weather_condition
FROM daily_forecasts d
JOIN locations l ON l.id = d.location_id
ORDER BY d.forecast_date, l.city
"""


def read_data():
    current_df = pd.read_sql(text(CURRENT_QUERY), engine)
    daily_df = pd.read_sql(text(DAILY_QUERY), engine)

    if not current_df.empty:
        current_df["recorded_at"] = pd.to_datetime(current_df["recorded_at"])
    if not daily_df.empty:
        daily_df["forecast_date"] = pd.to_datetime(daily_df["forecast_date"])

    return current_df, daily_df


def create_graphs(current_df, daily_df):
    import matplotlib.pyplot as plt

    if not daily_df.empty:
        pivot = daily_df.pivot(
            index="forecast_date",
            columns="city",
            values="max_temperature",
        )
        ax = pivot.plot(marker="o", figsize=(10, 6))
        ax.set_title("Seven-Day Maximum Temperature Forecast")
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature (°C)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(GRAPH_DIR / "max_temperature_trend.png", dpi=150)
        plt.close()

        city_summary = (
            daily_df.groupby("city")[["min_temperature", "max_temperature"]]
            .mean()
            .sort_values("max_temperature", ascending=False)
        )
        ax = city_summary.plot(kind="bar", figsize=(10, 6))
        ax.set_title("Average Minimum and Maximum Temperature by City")
        ax.set_xlabel("City")
        ax.set_ylabel("Temperature (°C)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(GRAPH_DIR / "city_temperature_comparison.png", dpi=150)
        plt.close()

        precipitation = (
            daily_df.groupby("city")["precipitation_sum"]
            .sum()
            .sort_values(ascending=False)
        )
        ax = precipitation.plot(kind="bar", figsize=(10, 6))
        ax.set_title("Forecast Total Precipitation by City")
        ax.set_xlabel("City")
        ax.set_ylabel("Precipitation (mm)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(GRAPH_DIR / "precipitation_by_city.png", dpi=150)
        plt.close()

    if not current_df.empty:
        ax = current_df.plot.scatter(
            x="temperature",
            y="humidity",
            figsize=(8, 6),
        )
        ax.set_title("Current Temperature vs Humidity")
        ax.set_xlabel("Temperature (°C)")
        ax.set_ylabel("Humidity (%)")
        plt.tight_layout()
        plt.savefig(GRAPH_DIR / "temperature_vs_humidity.png", dpi=150)
        plt.close()


def generate_faq(current_df, daily_df):
    lines = ["# Weather FAQ Report", ""]

    if current_df.empty or daily_df.empty:
        lines.append("No weather data is available. Run the ETL pipeline first.")
    else:
        latest = (
            current_df.sort_values("recorded_at")
            .groupby("city", as_index=False)
            .tail(1)
        )

        lines += ["## 1. What is the current weather in each city?", ""]
        for _, row in latest.iterrows():
            lines.append(
                f"- **{row['city']}**: {row['temperature']:.1f}°C, "
                f"{row['weather_condition']}, humidity {row['humidity']:.0f}%, "
                f"wind {row['wind_speed']:.1f} km/h."
            )

        hottest = daily_df.loc[daily_df["max_temperature"].idxmax()]
        coldest = daily_df.loc[daily_df["min_temperature"].idxmin()]
        wettest = (
            daily_df.groupby("city", as_index=False)["precipitation_sum"]
            .sum()
            .sort_values("precipitation_sum", ascending=False)
            .iloc[0]
        )
        windiest = daily_df.loc[daily_df["max_wind_speed"].idxmax()]
        common = daily_df["weather_condition"].mode().iloc[0]

        lines += [
            "",
            "## 2. Which city/date has the highest forecast temperature?",
            "",
            f"**{hottest['city']}** on {hottest['forecast_date'].date()} "
            f"with **{hottest['max_temperature']:.1f}°C**.",
            "",
            "![Maximum temperature trend](graphs/max_temperature_trend.png)",
            "",
            "## 3. Which city/date has the lowest forecast temperature?",
            "",
            f"**{coldest['city']}** on {coldest['forecast_date'].date()} "
            f"with **{coldest['min_temperature']:.1f}°C**.",
            "",
            "![City temperature comparison](graphs/city_temperature_comparison.png)",
            "",
            "## 4. Which city has the most forecast precipitation?",
            "",
            f"**{wettest['city']}**, with a seven-day total of "
            f"**{wettest['precipitation_sum']:.1f} mm**.",
            "",
            "![Precipitation by city](graphs/precipitation_by_city.png)",
            "",
            "## 5. Where is the strongest forecast wind?",
            "",
            f"**{windiest['city']}** on {windiest['forecast_date'].date()}, "
            f"reaching **{windiest['max_wind_speed']:.1f} km/h**.",
            "",
            "## 6. What is the most common forecast condition?",
            "",
            f"**{common}**.",
            "",
            "## 7. Is temperature related to humidity?",
            "",
            "Use the scatter plot below. A downward pattern suggests that "
            "humidity decreases as temperature rises; an upward pattern suggests "
            "the opposite. More historical records are needed for a reliable conclusion.",
            "",
            "![Temperature versus humidity](graphs/temperature_vs_humidity.png)",
        ]

    (REPORT_DIR / "faq_report.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def main():
    current_df, daily_df = read_data()
    current_df.to_csv(REPORT_DIR / "current_weather.csv", index=False)
    daily_df.to_csv(REPORT_DIR / "daily_forecast.csv", index=False)
    create_graphs(current_df, daily_df)
    generate_faq(current_df, daily_df)
    print("Reports generated inside the reports/ folder.")


if __name__ == "__main__":
    main()
