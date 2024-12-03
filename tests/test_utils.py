import csv
from pathlib import Path

# Test data is expected to exist in extern/p2108-test-data
TEST_DATA_DIR = (Path(__file__).parent.parent / "extern") / "p2108-test-data"
ABSTOL__DB = 0.1  # Absolute tolerance, in dB, to ensure outputs match expected value


def read_csv_test_data(filename: str):
    with open(TEST_DATA_DIR / filename) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            # yields (*inputs, rtn, output)
            yield tuple(map(float, row[:-2])), int(row[-2]), float(row[-1])
