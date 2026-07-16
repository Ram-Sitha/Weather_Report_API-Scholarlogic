import os
import sys
import json
import requests

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from config.config import API_KEY, BASE_URL, CITY, UNITS


def extract_weather_data():
    """
    Extract weather data from OpenWeather API
    and save it as a raw JSON file.
    """

    url = f"{BASE_URL}?q={CITY}&appid={API_KEY}&units={UNITS}"

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        # Create raw folder if it doesn't exist
        os.makedirs("data/raw", exist_ok=True)

        # Save JSON
        with open("data/raw/weather_raw.json", "w") as file:
            json.dump(data, file, indent=4)

        print("=" * 50)
        print("Weather Data Successfully Extracted")
        print("=" * 50)

        print(f"City        : {data['name']}")
        print(f"Temperature : {data['main']['temp']} °C")
        print(f"Humidity    : {data['main']['humidity']} %")
        print(f"Pressure    : {data['main']['pressure']} hPa")
        print(f"Weather     : {data['weather'][0]['main']}")
        print(f"Wind Speed  : {data['wind']['speed']} m/s")

        print("\nRaw JSON saved successfully.")
        print("Location: data/raw/weather_raw.json")

        return data

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")

    except requests.exceptions.ConnectionError:
        print("Connection Error")

    except requests.exceptions.Timeout:
        print("Request Timeout")

    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    extract_weather_data()