from scripts.extract import extract_weather_data
from scripts.transform import transform_weather_data
from scripts.load import load_weather_data

extract_weather_data()
transform_weather_data()
load_weather_data()