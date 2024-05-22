import platform
from ctypes import *
from enum import IntEnum
from pathlib import Path

ERROR_CODES = {
    0: "Successful execution",
    3100: "Frequency must be between 0.3 and 3 GHz, inclusive",
    3101: "Antenna heigh must be >= 0 meters",
    3102: "Street width must be > 0 meters",
    3103: "Representative clutter height must be > 0 meters",
    3104: "Invalid value for clutter type",
    3200: "Frequency must be between 2 and 67 GHz, inclusive",
    3201: "Path distance must be >= 0.25 km",
    3202: "Percentage must be between 0 and 100",
    3300: "Frequency must be between 10 and 100 GHz, inclusive",
    3301: "Elevation angle must be between 0 and 100 GHz, inclusive",
    3302: "Percentage must be between 0 and 100, inclusive",
}


class ClutterType(IntEnum):
    WaterSea = 1
    OpenRural = 2
    Suburban = 3
    Urban = 4
    TreesForest = 5
    DenseUrban = 6


# Load the compiled library
if platform.uname()[0] == "Windows":
    lib_name = "P2108.dll"
elif platform.uname()[0] == "Linux":
    lib_name = "libP2108.so.1.0"
# elif platform.uname()[0] == "Darwin":
# lib_name = "P2108.dylib" # TODO test and confirm
else:
    raise NotImplementedError("Your OS is not yet supported")

# Library should be in the same directory as this file
lib_path = Path(__file__).parent / lib_name
lib = CDLL(str(lib_path.resolve()))
# note: 32-bit python is needed to load 32-bit lib.

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


def err_check(error_code: int) -> None:
    """ """
    ec = error_code
    if ec == 0:
        return
    if ec in ERROR_CODES:
        # All errors as of v1.0 pertain to inputs out-of-range
        raise ValueError(ec)
    else:
        raise Exception(f"ITS.ITU.PSeries.P2108 returned unknown error {ec}")


def HeightGainTerminalCorrectionModel(
    f__ghz: float,
    h__meter: float,
    w_s__meter: float,
    R__meter: float,
    clutter_type: ClutterType,
) -> float:
    """
    Description
    -----------
    Height gain terminal correction model as described in Section 3.1.
    This method gives the median loss due to different terminal surroundings.
    This model can be applied to both transmitting and receiving ends of the path.

    Parameters
    ----------
    f__ghz : FLOAT
        Frequency, in GHz.
    h__meter : FLOAT
        Antenna height, in meters.
    w_s__meter : FLOAT
        Street width, in meters.
    R__meter : FLOAT
        Representative clutter height, in meters.
    clutter_type : INT # TODO enum
        Clutter type.

    Returns
    -------
    FLOAT
        Additional loss (clutter loss), in dB.

    """
    A_h__db = c_double()
    err_check(
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
    """
    Description
    -----------
    Statistical clutter loss model for terrestrial paths as described
    in Section 3.2. This model can be applied for urban and suburban
    clutter loss modelling.

    Parameters
    ----------
    f__ghz : FLOAT
        Frequency, in GHz.
    d__km : FLOAT
        Path distance, in km.
    p : FLOAT
        Percentange of locations, in %.

    Returns
    -------
    FLOAT
        Additional loss (clutter loss), in dB.

    """
    L_ctt__db = c_double()
    err_check(
        lib.TerrestrialStatisticalModel(
            c_double(f__ghz),
            c_double(d__km),
            c_double(p),
            byref(L_ctt__db),
        )
    )

    return L_ctt__db.value


def AeronauticalStatisticalModel(f__ghz: float, theta__deg: float, p: float) -> float:
    """
    Description
    -----------
    The Earth-space and aeronautical statistical clutter loss
    model as described in Section 3.3. This model is applicable
    when one end of the path is within man-made clutter and the
    other end is a satellite, aeroplane, or other platform
    above the Earth.

    Parameters
    ----------
    f__ghz : FLOAT
        Frequency, in GHz.
    theta__deg : FLOAT
        Elevation angle, in degrees.
    p : FLOAT
        Percentange of locations, in %.

    Returns
    -------
    INT
        Return code.
    FLOAT
        Additional loss (clutter loss), in dB.

    """
    L_ces__db = c_double()
    err_check(
        lib.AeronauticalStatisticalModel(
            c_double(f__ghz), c_double(theta__deg), c_double(p), byref(L_ces__db)
        )
    )

    return L_ces__db.value
