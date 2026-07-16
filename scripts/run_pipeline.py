from extract import extract_weather_data
from transform import transform_data
from load import load_data


def run_pipeline():

    print("=" * 50)
    print("Weather ETL Pipeline Started")
    print("=" * 50)

    extract_weather_data()

    transform_data()

    load_data()

    print("=" * 50)
    print("Pipeline Completed Successfully")
    print("=" * 50)


if __name__ == "__main__":
    run_pipeline()