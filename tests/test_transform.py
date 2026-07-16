"""
Test File : test_transform.py
Purpose   : Test Data Transformation
"""

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from scripts.transform import transform_data


def test_transform():

    df = transform_data()

    assert df is not None

    assert not df.empty

    print("Transform Test Passed")


if __name__ == "__main__":

    test_transform()