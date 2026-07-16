import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
import mysql.connector

from config.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


def load_data():

    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    df = pd.read_csv("data/processed/weather_processed.csv")

    query = """
    INSERT INTO weather_data
    (
        city,
        temperature,
        feels_like,
        humidity,
        pressure,
        weather,
        description,
        wind_speed,
        latitude,
        longitude
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    for row in df.itertuples(index=False):
        cursor.execute(query, tuple(row))

    connection.commit()

    print(f"{cursor.rowcount} Record Inserted Successfully")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    load_data()