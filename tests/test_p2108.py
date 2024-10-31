import csv
from pathlib import Path

import pytest

from ITS.ITU.PSeries import P2108

# Test data is expected to exist in parent repository
# (i.e., that NTIA/P2108-python is cloned as a submodule of NTIA/P2108)
TEST_DATA_DIR = (Path(__file__).parent.parent.parent.parent / "tests") / "data"
ABSTOL__DB = 0.1  # Absolute tolerance, in dB, to ensure outputs match expected value


def read_csv_test_data(filename: str):
    with open(TEST_DATA_DIR / filename) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            # yield (inputs, rtn, output)
            yield tuple(map(float, row[:-2])), int(row[-2]), float(row[-1])


@pytest.mark.parametrize(
    "inputs,rtn,expected",
    read_csv_test_data("AeronauticalStatisticalModelTestData.csv"),
)
def test_AeronauticalStatisticalModel(inputs, rtn, expected):
    if rtn == 0:
        out = P2108.AeronauticalStatisticalModel(*inputs)
        assert out == pytest.approx(expected, abs=ABSTOL__DB)
    else:
        with pytest.raises(RuntimeError):
            P2108.AeronauticalStatisticalModel(*inputs)


@pytest.mark.parametrize(
    "inputs,rtn,expected",
    read_csv_test_data("HeightGainTerminalCorrectionModelTestData.csv"),
)
def test_HeightGainTerminalCorrection(inputs, rtn, expected):
    clutter_type = P2108.ClutterType(int(inputs[-1]))
    if rtn == 0:
        out = P2108.HeightGainTerminalCorrectionModel(*inputs[:-1], clutter_type)
        assert out == pytest.approx(expected, abs=ABSTOL__DB)
    else:
        with pytest.raises(RuntimeError):
            P2108.HeightGainTerminalCorrectionModel(*inputs[:-1], clutter_type)


@pytest.mark.parametrize(
    "inputs,rtn,expected", read_csv_test_data("TerrestrialStatisticalModelTestData.csv")
)
def test_TerrestrialStatisticalModel(inputs, rtn, expected):
    if rtn == 0:
        out = P2108.TerrestrialStatisticalModel(*inputs)
        assert out == pytest.approx(expected, abs=ABSTOL__DB)
    else:
        with pytest.raises(RuntimeError):
            P2108.TerrestrialStatisticalModel(*inputs)
