# Recommendation ITU-R P.2108 - U.S. Reference Implementation, Python #

[![GitHub issues][github-issue-count-badge]][github-issues]
[![Code style: black][code-style-badge]][code-style-repo]

[code-style-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[code-style-repo]: https://github.com/psf/black
[github-issue-count-badge]: https://img.shields.io/github/issues/NTIA/p2108-python
[github-issues]: https://github.com/NTIA/p2108-python/issues

Python® wrapper for U.S. Reference Software Implementation of Recommendation ITU-R
P.2108. This Recommendation contains three methods for the prediction of clutter
loss: Height Gain Terminal Correction Model, Terrestrial Statistical Model, and
Aeronautical Statistical Model. The software implements Section 3 of Annex 1 of
the Recommendation.

## Usage ##

For an overview of the available functions of this model, view the
[NTIA/ITS Propagation Library Wiki](https://ntia.github.io/propagation-library-wiki/models/P2108).
Additionally, Python-specific usage information, installation instructions, and
code examples are available [here](https://ntia.github.io/propagation-library-wiki/models/P2108/python).

## Development ##

This repository contains code which wraps [the C++ source](https://github.com/NTIA/p2108)
as an importable Python module. If you wish to contribute to this repository,
testing your changes will require the inclusion of the dynamic library binary
built from the C++ source code. You may retrieve this either from the
[relevant GitHub Releases page](https://github.com/NTIA/p2108/releases), or by
compiling it yourself from the source code. If providing the dynamic library file
(`.dll`, `.dylib`, or `.so`) manually from a release, place it in
`src/ITS/ITU/PSeries/P2108/`, alongside `__init__.py`. Otherwise, follow these
instructions to compile the library yourself.

### Building the Library from Source ###

The following development workflow assumes that you work within a cloned copy of
the [parent repository](https://github.com/NTIA/p2108). Below are the steps to build
and install the Python package from source, including
compiling the library from the C++ source code. Working installations of Git and
Python (3.8 or above) are required.

1. Clone the parent repository, then initialize the Git submodule containing the
Python wrapper.

    ```cmd
    # Clone the parent repository:
    git clone https://github.com/NTIA/p2108
    cd p2108

    # Then run one of the following:
    git submodule init wrap/python  # Only the Python wrapper
    git submodule init  # All available wrappers

    # Finally, to clone the submodule(s):
    git submodule update
    ```

1. Compile the C++ library for your platform using CMake. Here, we use CMake
options to _only_ build the library, without building documentation or running C++
unit tests. If you are using a 32-bit platform, use the `release32` preset
instead of `release64`.

    ```cmd
    # From the cloned repository:

    cmake --preset release64 -DBUILD_DOCS=OFF -DRUN_TESTS=OFF
    cmake --build --preset release64
    ```

    When the CMake build command is run, the compiled library will be automatically
    be copied into place where needed to build the Python package (alongside `__init__.py`).

1. Install the local package, and development dependencies:

    ```cmd
    cd wrap/python
    pip install .[dev]
    ```

    This will install the Python package itself along with development dependencies
    for pre-commit hooks, building distributable packages, and running unit tests.

### Running Tests ###

Python unit tests can be run to confirm successfull installation. Test data is
expected to be located in the parent repository. Therefore, if you haven't cloned
this repository as a submodule (as described above), you will need to first specify
the location of the test data files in `tests/test_p2108.py` (using the `TEST_DATA_DIR`
variable). Then, run the tests with pytest:

```cmd
pytest .
```

Additionally, the [Study Group Clutter Excel Workbook](https://www.itu.int/en/ITU-R/study-groups/rsg3/ionotropospheric/Clutter%20and%20BEL%20workbook_V2.xlsx)
contains an extensive set of example values which are useful as validation cases.

## License ##

See [LICENSE](LICENSE.md).

"Python" and the Python logos are trademarks or registered trademarks of the Python
Software Foundation, used by the National Telecommunications and Information Administration
with permission from the Foundation.

## References ##

* [ITS Propagation Library Wiki](https://ntia.github.io/propagation-library-wiki)
* [`ITS.ITU.PSeries.P2108` C++ API Reference](https://ntia.github.io/P2108)
* [Recommendation ITU-R P.2108](https://www.itu.int/rec/R-REC-P.2108/en)
* [Report ITU-R P.2402](https://www.itu.int/pub/R-REP-P.2402)

## Contact ##

For technical questions, contact <code@ntia.gov>.
