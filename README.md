# Recommendation ITU-R P.2108-1: U.S. Reference Implementation

[![GitHub release (latest SemVer)][latest-release-semver-badge]][github-releases]
[![GitHub issues][github-issue-count-badge]][github-issues]
[![Code style: black][code-style-badge]][code-style-repo]

[latest-release-semver-badge]: https://img.shields.io/github/v/release/NTIA/p2108-python?display_name=tag&sort=semver
[github-releases]: https://github.com/NTIA/p2108-python/releases
[code-style-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[code-style-repo]: https://github.com/psf/black
[github-issue-count-badge]: https://img.shields.io/github/issues/NTIA/p2108-python
[github-issues]: https://github.com/NTIA/p2108-python/issues

Python® wrapper for U.S. Reference Software Implementation of Recommendation ITU-R
P.2108. This Recommendation contains three methods for the prediction of clutter
loss: Height Gain Terminal Correction Model, Terrestrial Statistical Model, and
Aeronautical Statistical Model. The software implements Section 3 of Annex 1 of
the Recommendation.

## Usage

For an overview of the available functions of this model, view the
[NTIA/ITS Propagation Library Wiki](https://github.com/NTIA/propagation/wiki/P2108).
Additionally, Python-specific usage information and examples are available
[here](https://github.com/NTIA/propagation/wiki/P2108-(Python)).

## Development

This repository contains code which wraps [the C++ source](https://github.com/NTIA/p2108)
as an importable Python module. The development workflow assumes that you work
within a cloned copy of the [parent repository](https://github.com/NTIA/p2108).
Below are the steps to build and install the Python package from source, including
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

1. Compile the C++ library for your platform using CMake:

    ```cmd
    # From the cloned repository
    mkdir build
    cmake -S . -B build
    cmake --build build
    ```

    When the CMake build command is run, the compiled library will be copied
    into place where needed to build the Python package (alongside `__init__.py`).

1. Install the local package, and development dependencies:

    ```cmd
    cd wrap/python
    pip install .[dev]
    ```

    This will install the Python package itself along with development dependencies
    for pre-commit hooks, building distributable packages, and running unit tests.

1. (Optional) Run unit tests to confirm successfull installation. Test data is
used from the parent repository.

    ```cmd
    pytest .
    ```

## License

See [LICENSE](LICENSE.md).

"Python" and the Python logos are trademarks or registered trademarks of the Python
Software Foundation, used by the National Telecommunications and Information Administration
with permission from the Foundation.

## Contact

For technical questions about the NTIA/ITS Propagation Library, contact <code@ntia.gov>.
