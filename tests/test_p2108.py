import pytest

from ITS.ITU.PSeries import P2108

from .test_utils import ABSTOL__DB, read_csv_test_data


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
