from ctypes import *
from enum import IntEnum

from .proplib_loader import PropLibCDLL

# Load the shared library
lib = PropLibCDLL("P2108-1.0")

# Define function prototypes
lib.AeronauticalStatisticalModel.restype = c_int
lib.AeronauticalStatisticalModel.argtypes = (
    c_double,
    c_double,
    c_double,
    POINTER(c_double),
)
lib.TerrestrialStatisticalModel.restype = c_int
lib.TerrestrialStatisticalModel.argtypes = (
    c_double,
    c_double,
    c_double,
    POINTER(c_double),
)
lib.HeightGainTerminalCorrectionModel.restype = c_int
lib.HeightGainTerminalCorrectionModel.argtypes = (
    c_double,
    c_double,
    c_double,
    c_double,
    c_int,
    POINTER(c_double),
)


class ClutterType(IntEnum):
    WaterSea = 1
    OpenRural = 2
    Suburban = 3
    Urban = 4
    TreesForest = 5
    DenseUrban = 6


def HeightGainTerminalCorrectionModel(
    f__ghz: float,
    h__meter: float,
    w_s__meter: float,
    R__meter: float,
    clutter_type: ClutterType,
) -> float:
    """Height gain terminal correction model as described in Section 3.1.

    This method gives the median loss due to different terminal surroundings.
    This model can be applied to both transmitting and receiving ends of the path.

    :param f__ghz: Frequency, in GHz.
    :param h__meter: Antenna height, in meters.
    :param w_s__meter: Street width, in meters.
    :param R__meter: Representative clutter height, in meters.
    :param clutter_type: Clutter type, a ClutterType enum value.
    :raises ValueError: If any input parameter is not in its valid range.
    :raises Exception: If an unknown error is encountered.
    :return: Additional loss (clutter loss), in dB.
    """
    A_h__db = c_double()
    lib.err_check(
        lib.HeightGainTerminalCorrectionModel(
            c_double(f__ghz),
            c_double(h__meter),
            c_double(w_s__meter),
            c_double(R__meter),
            c_int(clutter_type),
            byref(A_h__db),
        )
    )

    return A_h__db.value


def TerrestrialStatisticalModel(f__ghz: float, d__km: float, p: float) -> float:
    """Statistical clutter loss model for terrestrial paths as described in
    Section 3.2. This model can be applied for urban and suburban clutter loss
    modeling.

    :param f__ghz: Frequency, in GHz.
    :param d__km: Path distance, in km.
    :param p: Percentage of locations, in %.
    :raises ValueError: If any input parameter is not in its valid range.
    :raises Exception: If an unknown error is encountered.
    :return: Additional loss (clutter loss), in dB.
    """
    L_ctt__db = c_double()
    lib.err_check(
        lib.TerrestrialStatisticalModel(
            c_double(f__ghz),
            c_double(d__km),
            c_double(p),
            byref(L_ctt__db),
        )
    )

    return L_ctt__db.value


def AeronauticalStatisticalModel(f__ghz: float, theta__deg: float, p: float) -> float:
    """The Earth-space and aeronautical statistical clutter loss model as
    described in Section 3.3. This model is applicable when one end of the path
    is within man-made clutter and the other end is a satellite, aeroplane, or
    other platform above the Earth.

    Frequency range: 10 < f < 100 (GHz)
    Elevation angle range: 0 < theta < 90 (degrees)
    Percentage locations range: 0 < p < 100 (%)

    :param f__ghz: Frequency, in GHz.
    :param theta__deg: Elevation angle, in degrees.
    :param p: Percentage of locations, in %.
    :raises ValueError: If any input parameter is not in its valid range.
    :raises Exception: If an unknown error is encountered.
    :return: Additional loss (clutter loss), in dB.
    """
    L_ces__db = c_double()
    lib.err_check(
        lib.AeronauticalStatisticalModel(
            c_double(f__ghz), c_double(theta__deg), c_double(p), byref(L_ces__db)
        )
    )

    return L_ces__db.value
