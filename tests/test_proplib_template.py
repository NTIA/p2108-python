# TODO-TEMPLATE: Rename this file
import csv
from pathlib import Path

import pytest

# TODO-TEMPLATE: Import the python wrapper package
from ITS import PropLibTemplate

# Test data is expected to exist in extern/<TODO-TEMPLATE>-test-data
TEST_DATA_DIR = (Path(__file__).parent.parent / "extern") / "TODO-TEMPLATE"
ABSTOL__DB = 0.1  # Absolute tolerance, in dB, to ensure outputs match expected value


# TODO-TEMPLATE: Update CSV reader based on test data CSV structure
def read_csv_test_data(filename: str):
    with open(TEST_DATA_DIR / filename) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            # yield (inputs, rtn, output)
            yield tuple(map(float, row[:-2])), int(row[-2]), float(row[-1])


# TODO-TEMPLATE: Implement unit tests for this Python wrapper
def test_always_pass():
    return
