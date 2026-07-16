"""
Test File : test_extract.py
Purpose   : Test Weather API Extraction
"""

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from scripts.extract import extract_weather_data


def test_extract_weather_data():

    data = extract_weather_data()

    assert data is not None

    assert data["cod"] == 200

    assert "main" in data

    print("Extract Test Passed")


if __name__ == "__main__":

    test_extract_weather_data()