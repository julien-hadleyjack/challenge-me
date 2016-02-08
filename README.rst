========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |versions| |implementations|

.. |docs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
    :target: https://challenge-me.readthedocs.org/en/latest/
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/julien-hadleyjack/challenge-me.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/julien-hadleyjack/challenge-me

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/julien-hadleyjack/challenge-me?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/julien-hadleyjack/challenge-me

.. |requires| image:: https://requires.io/github/julien-hadleyjack/challenge-me/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/julien-hadleyjack/challenge-me/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/julien-hadleyjack/challenge-me/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/julien-hadleyjack/challenge-me

.. |codacy| image:: https://img.shields.io/codacy/cfacce47c4b84eb385822e262efab73a.svg?style=flat
    :target: https://www.codacy.com/app/julien-hadleyjack/challenge-me/dashboard
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/julien-hadleyjack/challenge-me/badges/gpa.svg
   :target: https://codeclimate.com/github/julien-hadleyjack/challenge-me
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/challenge-me.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/challenge-me

.. |downloads| image:: https://img.shields.io/pypi/dm/challenge-me.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/challenge-me

.. |wheel| image:: https://img.shields.io/pypi/wheel/challenge-me.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/challenge-me

.. |versions| image:: https://img.shields.io/pypi/pyversions/challenge-me.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/challenge-me

.. |implementations| image:: https://img.shields.io/pypi/implementation/challenge-me.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/challenge-me

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/julien-hadleyjack/challenge-me/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/julien-hadleyjack/challenge-me/

.. end-badges

**Note**: This is still an early version which can have unwanted side effects like accidentally deleting a wrong file. Use with care.

A command line tool for improving or at least testing your programming knowledge. *challenge-me* gives you
programming exercises on various topics that you have to solve. It can check to see if your solution is correct and
then provide you with the next exercise if true. A run could look like this:

.. code:: shell

    $ challenge-me start
    Starting first challenge for category array.

    $ challenge-me verify
    Verifying challenge 1 for category array.
    Failure.
    Input: 1 2 3 4
    Result:
    Expected: 1 2 0 0

    $ # edit file to solve challenge

    $ challenge-me verify
    Verifying challenge 1 for category array.
    Success.
    Creating file for next challenge.

The challenges come from different books and websites. You are invited to provide more challenges.

At the moment the solutions have to be in Python. In a future version, support for other languages will be added.

Installation
============

::

    pip install challenge-me

Documentation
=============

The full documentation can be read at `ReadTheDocs <https://challenge-me.readthedocs.org/en/latest/>`_. While using the
tool you you can also consult the command line help:

.. code:: shell

    $ challenge-me --help
    Usage: main.py [OPTIONS] COMMAND [ARGS]...

    Command line tool for running programming challenges.

    Note: This is still an early version which can have unwanted side effects
    like accidentally deleting a wrong file. Use with care.

    Options:
    --version  Show the version and exit.
    --help     Show this message and exit.

    Commands:
    skip    Skip a challenge.
    start   Start a challenge.
    verify  Verify a challenge and on success start the next.

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

