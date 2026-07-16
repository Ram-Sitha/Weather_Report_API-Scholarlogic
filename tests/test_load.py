"""
Test File : test_load.py
Purpose   : Test MySQL Load
"""

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from scripts.load import load_data


def test_load():

    load_data()

    print("Load Test Passed")


if __name__ == "__main__":

    test_load()