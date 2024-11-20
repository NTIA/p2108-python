# NTIA/ITS Propagation Library Template Python Wrapper #
<!-- TODO-TEMPLATE Update software name above -->
<!-- TODO-TEMPLATE: README BADGES

- The first badge links to the PropLib Wiki and does not need to be edited
- The second badge automatically displays and links to the most recent GitHub Release.
    - Make sure to update the [gh-releases-badge] and [gh-releases-link] URLs with your repo name
- The third badge links to the zenodo DOI page. Only include this badge if a DOI exists for a release.
    - Update the [doi-link] using the "id" from https://api.github.com/repos/ntia/{repo_name}. For example, the
      [doi-link] for ITM would be https://zenodo.org/badge/latestdoi/218981682. Using the repository ID in this link
      will automatically make the link always point to the most recent DOI for the repository, so this won't need to be
      edited every time a new release is made.
    - Update the [doi-badge] to include the "all versions" DOI which always points to the latest version.
      This can be found when creating the DOI in zenodo. The slash in the DOI must be replaced with "%2F" to
      render in the badge. For example, the P2108 DOI is 10.5281/zenodo.7114033 which must be input as
      "10.5281%2Fzenodo.7114033"
- The fourth badge is the Tox GitHub actions status.
    - Update the repository name in [gh-actions-test-badge] and [gh-actions-test-link]
- The fifth badge displays open GitHub Issues
    - Update the repository name in [gh-issues-badge]
    - Update the repository name in [gh-issues-link]
-->
[![NTIA/ITS PropLib][proplib-badge]][proplib-link]
<!--
[![GitHub Release][gh-releases-badge]][gh-releases-link]
[![DOI][doi-badge]][doi-link]
[![GitHub Actions Unit Test Status][gh-actions-test-badge]][gh-actions-test-link]
[![GitHub Issues][gh-issues-badge]][gh-issues-link]
-->
[proplib-badge]: https://img.shields.io/badge/PropLib-badge?label=%F0%9F%87%BA%F0%9F%87%B8%20NTIA%2FITS&labelColor=162E51&color=D63E04
[proplib-link]: https://ntia.github.io/propagation-library-wiki
[gh-actions-test-badge]: https://img.shields.io/github/actions/workflow/status/NTIA/TODO-TEMPLATE/tox.yml?branch=main&logo=pytest&logoColor=ffffff&label=Build%2FTests&labelColor=162E51
[gh-actions-test-link]: https://github.com/NTIA/TODO-TEMPLATE/actions/workflows/tox.yml
[gh-releases-badge]: https://img.shields.io/github/v/release/NTIA/TODO-TEMPLATE?logo=github&label=Release&labelColor=162E51&color=D63E04
[gh-releases-link]: https://github.com/NTIA/TODO-TEMPLATE/releases
[gh-issues-badge]: https://img.shields.io/github/issues/NTIA/TODO-TEMPLATE?logo=github&label=Issues&labelColor=162E51
[gh-issues-link]: https://github.com/NTIA/TODO-TEMPLATE/issues
[doi-badge]: https://img.shields.io/badge/{TODO-TEMPLATE-ALL-VERSIONS-DOI}-x?logo=doi&logoColor=ffffff&labelColor=162E51&color=D63E04
[doi-link]: https://zenodo.org/badge/latestdoi/{TODO-TEMPLATE-REPOSITORY-ID}

<!-- TODO-TEMPLATE: Replace the below description with one for your software -->
This code repository is a template repository for Python wrappers in the NTIA/ITS
Propagation Library (PropLib). This template is intended for developers wishing
to develop a cross-platform Python interface to a compiled C++ library as part of
PropLib. Instructions on how to use this repository are found in the
[PropLib Template Wiki](https://github.com/NTIA/proplib-template/wiki).

Additional template repositories exist for building the C++ base repository and the
C#/.NET and MATLAB wrappers. See:

- [NTIA/proplib-template](https://github.com/NTIA/proplib-template)
- [NTIA/proplib-template-dotnet](https://github.com/NTIA/proplib-template-dotnet)
- [NTIA/proplib-template-matlab](https://github.com/NTIA/proplib-template-matlab)

## Contact ##

For questions about using this template repository, contact <aromaniello@ntia.gov>

<!-- TODO-TEMPLATE: Create the README contents. Boilerplate provided below.

## Getting Started ##

TODO-TEMPLATE: Update links in this section

This software is distributed on [PyPi](https://pypi.org/project/TODO-TEMPLATE) and is easily installable
using the following command.

```cmd
pip install TODO-TEMPLATE
```

General information about using this model is available on
[its page on the **NTIA/ITS Propagation Library Wiki**](https://ntia.github.io/propagation-library-wiki/models/TODO-TEMPLATE/).
Additionally, Python-specific instructions and code examples are available
[here](https://ntia.github.io/propagation-library-wiki/models/TODO-TEMPLATE/python).

If you're a developer and would like to contribute to or extend this repository,
please review the guide for contributors [here](CONTRIBUTING.md) or open an
[issue](https://github.com/NTIA/TODO-TEMPLATE/issues) to start a discussion.

## Development ##

This repository contains code which wraps [the C++ shared library](https://github.com/NTIA/TODO-TEMPLATE)
as an importable Python module. If you wish to contribute to this repository,
testing your changes will require the inclusion of this shared library. You may retrieve
this either from the
[relevant GitHub Releases page](https://github.com/NTIA/TODO-TEMPLATE/releases), or by
compiling it yourself from the C++ source code. Either way, ensure that the shared library
(`.dll`, `.dylib`, or `.so` file) is placed in `src/TODO-TEMPLATE/MODEL-NAMESPACE/`, alongside `__init__.py`.

Below are the steps to build and install the Python package from source, including
compiling the library from the C++ source code. Working installations of Git and
Python (3.9 or above) are required. If compiling the shared library, CMake and a C++ compiler
are also required.

1. Clone the parent repository, then initialize the Git submodule containing the
Python wrapper. This repository structure makes test data available to the Python
wrapper.

    ```cmd
    # Clone the parent repository
    git clone https://github.com/NTIA/TODO-TEMPLATE
    cd TODO-TEMPLATE

    # Initialize Git submodules (wrappers and external dependencies)
    git submodule init

    # Clone the submodules
    git submodule update
    ```

1. Compile the C++ library for your platform, following instructions
[here](https://github.com/NTIA/TODO-TEMPLATE?tab=readme-ov-file#configure-and-build).
Following these instructions should automatically copy the shared library
into the location required by the Python wrapper.

    **OR**

    Download the shared library (`.dll`, `.so`, or `.dylib`) from a
    [GitHub Release](https://github.com/NTIA/TODO-TEMPLATE/releases). Then place the
    downloaded file in `src/TODO-TEMPLATE/MODEL-NAMESPACE/` (alongside `__init__.py`).

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
the location of the test data files in `tests/test_<TODO-TEMPLATE>.py` (using the `TEST_DATA_DIR`
variable). Then, run the tests with pytest:

```cmd
pytest
```

## References ##

TODO-TEMPLATE: Update references

* [ITS Propagation Library Wiki](https://ntia.github.io/propagation-library-wiki)
* [TODO-TEMPLATE Wiki Page](https://ntia.github.io/propagation-library-wiki/models/TODO-TEMPLATE)
* [`TODO-TEMPLATE` C++ API Reference](https://ntia.github.io/TODO-TEMPLATE)
* TODO-TEMPLATE: Link supporting documentation such as ITU-R Recommendations, NTIA reports, etc.

## Contact ##

For technical questions, contact <code@ntia.gov>.

-->
