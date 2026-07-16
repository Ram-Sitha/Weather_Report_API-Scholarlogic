"""
===========================================================
Project Name : Weather API Data Analytics
File Name    : transform.py
Author       : Ramanjaneyulu
Description  : Transform raw weather JSON data into a
               cleaned CSV file for MySQL loading.
===========================================================
"""

# ==========================================================
# Import Required Libraries
# ==========================================================

import os
import sys
import json
import pandas as pd

# ==========================================================
# Add Project Root to Python Path
# ==========================================================

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# Function : transform_data()
# Purpose  : Read JSON, Clean Data, Convert to CSV
# ==========================================================

def transform_data():

    try:

        # --------------------------------------------------
        # Read Raw JSON File
        # --------------------------------------------------

        with open("data/raw/weather_raw.json", "r") as file:
            data = json.load(file)

        print("Raw JSON File Loaded Successfully.")

        # --------------------------------------------------
        # Extract Required Weather Information
        # --------------------------------------------------

        weather = {

            "city": data["name"],

            "temperature": data["main"]["temp"],

            "feels_like": data["main"]["feels_like"],

            "humidity": data["main"]["humidity"],

            "pressure": data["main"]["pressure"],

            "weather": data["weather"][0]["main"],

            "description": data["weather"][0]["description"],

            "wind_speed": data["wind"]["speed"],

            "latitude": data["coord"]["lat"],

            "longitude": data["coord"]["lon"]

        }

        # --------------------------------------------------
        # Convert Dictionary into Pandas DataFrame
        # --------------------------------------------------

        df = pd.DataFrame([weather])

        print("\nDataFrame Created Successfully.\n")

        print(df)

        # --------------------------------------------------
        # Data Cleaning
        # --------------------------------------------------

        # Remove Null Values
        df.dropna(inplace=True)

        # Remove Duplicate Records
        df.drop_duplicates(inplace=True)

        # --------------------------------------------------
        # Create Processed Folder (If Not Exists)
        # --------------------------------------------------

        os.makedirs("data/processed", exist_ok=True)

        # --------------------------------------------------
        # Save DataFrame as CSV
        # --------------------------------------------------

        output_path = "data/processed/weather_processed.csv"

        df.to_csv(output_path, index=False)

        print("\nProcessed CSV Saved Successfully.")

        print(f"Location : {output_path}")

        print("\nTransformation Completed Successfully.")

        return df

    except FileNotFoundError:

        print("Error : weather_raw.json file not found.")

    except json.JSONDecodeError:

        print("Error : Invalid JSON format.")

    except KeyError as e:

        print(f"Missing JSON Key : {e}")

    except Exception as e:

        print(f"Unexpected Error : {e}")


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":

    transform_data()