# Recommendation ITU-R P.2108 - U.S. Reference Implementation, Python #

![NTIA/ITS PropLib][proplib-badge]
![GitHub Release][gh-releases-badge]
![GitHub Issues][gh-issues-badge]
<!-- TODO: Add unit test badge after CI workflow is added -->
<!-- [![Unit Tests Status][gh-actions-test-badge]][gh-actions-test-link] -->
<!-- TODO: Include a DOI badge if a DOI exists for a release -->
<!-- [![DOI][doi-badge]][doi-link] -->

[proplib-badge]: https://img.shields.io/badge/NTIA-PropLib-D63E04?label=NTIA%2FITS&labelColor=162E51&link=https%3A%2F%2Fntia.github.io%2Fpropagation-library-wiki
<!--
[gh-actions-test-link]: https://github.com/NTIA/p2108-python/actions/workflows/tox.yml
[gh-actions-test-badge]: https://github.com/NTIA/p2108-python/actions/workflows/tox.yml/badge.svg?branch=main
-->
[gh-releases-badge]: https://img.shields.io/github/v/release/NTIA/p2108-python
[gh-issues-badge]: https://img.shields.io/github/issues/NTIA/p2108-python
<!-- TODO-TEMPLATE: Only create a DOI for versioned public releases -->
<!-- [doi-badge]: https://zenodo.org/badge/DOI/TODO-TEMPLATE/zenodo.TODO-TEMPLATE.svg
[doi-link]: https://doi.org/TODO-TEMPLATE/zenodo.TODO-TEMPLATE -->

Python® wrapper for U.S. Reference Software Implementation of Recommendation ITU-R
P.2108. This Recommendation contains three methods for the prediction of clutter
loss: Height Gain Terminal Correction Model, Terrestrial Statistical Model, and
Aeronautical Statistical Model. The software implements Section 3 of Annex 1 of
the Recommendation. This Python package wraps the
[base C++ implementation](https://github.com/NTIA/p2108).

## Getting Started ##

For an overview of the available functions of this model, view the
[NTIA/ITS Propagation Library Wiki](https://ntia.github.io/propagation-library-wiki/models/P2108).
Additionally, Python-specific usage information, installation instructions, and
code examples are available [here](https://ntia.github.io/propagation-library-wiki/models/P2108/python).

If you're a developer and would like to contribute to or extend this repository,
please review the guide for contributors [here](CONTRIBUTING.md) or open an
[issue](https://github.com/NTIA/p2108-python/issues) to start a discussion.

## Development ##

This repository contains code which wraps [the C++ source](https://github.com/NTIA/p2108)
as an importable Python module. If you wish to contribute to this repository,
testing your changes will require the inclusion of this shared library. You may retrieve
this either from the
[relevant GitHub Releases page](https://github.com/NTIA/p2108/releases), or by
compiling it yourself from the C++ source code (instructions
[here](https://github.com/NTIA/p2108?tab=readme-ov-file#configure-and-build)).
If providing the shared library (`.dll`, `.dylib`, or `.so` file) manually
from a GitHub release, place it in `src/ITS/ITU/PSeries/P2108/`, alongside
`__init__.py`.

Below are the steps to build and install the Python package from source, including
compiling the library from the C++ source code. Working installations of Git and
Python (3.9 or above) are required.

1. Clone the parent repository, then initialize the Git submodule containing the
Python wrapper. This repository structure makes test data available to the Python
wrapper.

    ```cmd
    # Clone the parent repository:
    git clone https://github.com/NTIA/p2108
    cd p2108

    # Then run one of the following:
    git submodule init wrap/python  # Only the Python wrapper
    git submodule init              # All available wrappers

    # Finally, clone the submodule(s):
    git submodule update
    ```

1. Compile the C++ library for your platform, following instructions
[here](https://github.com/NTIA/p2108?tab=readme-ov-file#configure-and-build).
Following these instructions should automatically copy the shared library
into the location required by the Python wrapper.

    **OR**

    Download the shared library (`.dll`, `.so`, or `.dylib`) from a
    [GitHub Release](https://github.com/NTIA/p2108/releases). Then place the
    downloaded file in `src/ITS/ITU/PSeries/P2108/` (alongside `__init__.py`).

1. Install the local package and development dependencies:

    ```cmd
    cd wrap/python
    pip install .[dev]
    ```

1. To build the wheel for your platform:

    ```cmd
    hatchling build
    ```

### Running Tests ###

Python unit tests can be run to confirm successful installation. Test data is
expected to be located in the parent repository. Therefore, if you haven't cloned
this repository as a submodule (as described above), you will need to first specify
the location of the test data files in `tests/test_p2108.py` (using the `TEST_DATA_DIR`
variable). Then, run the tests with pytest:

```cmd
pytest
```

Additionally, the [Study Group Clutter Excel Workbook](https://www.itu.int/en/ITU-R/study-groups/rsg3/ionotropospheric/Clutter%20and%20BEL%20workbook_V2.xlsx)
contains an extensive set of example values which are useful as validation cases.

## References ##

* [ITS Propagation Library Wiki](https://ntia.github.io/propagation-library-wiki)
* [P2108 Wiki Page](https://ntia.github.io/propagation-library-wiki/models/P2108)
* [`ITS.ITU.PSeries.P2108` C++ API Reference](https://ntia.github.io/P2108)
* [Recommendation ITU-R P.2108](https://www.itu.int/rec/R-REC-P.2108/en)
* [Report ITU-R P.2402](https://www.itu.int/pub/R-REP-P.2402)

## Contact ##

For technical questions, contact <code@ntia.gov>.
