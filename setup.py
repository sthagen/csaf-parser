#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Interface to setup tools for PyPI publication

Note: To use the 'upload' functionality of this file, you must:
$ pip install twine
"""
import pathlib
import shutil
import subprocess
import sys

from setuptools import find_packages, setup, Command

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Package meta-data.
NAME = 'csaf-parser'
VERSION = '0.0.1'
DESCRIPTION = 'CSAF Common Vulnerability Reporting Framework (CVRF) Viewer and Parser'
REQUIRES = [
    "jsonschema",
    "lxml",
    "xmlschema",
]
KEYWRODS = "csaf cvrf parser development"
AUTHOR = 'Omar Santos'
EMAIL = 'osantos@cisco.com'
URL = 'https://github.com/oasis-open/csaf-parser'


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def _call(vector, shell=False):
        """Execute the vector in a subprocess (default without shell, eg. for globbing)."""
        try:
            sts = subprocess.call(vector, shell=shell)
            if sts < 0:
                print("Child was terminated by signal", -sts, file=sys.stderr)
            else:
                print("Child returned", sts, file=sys.stderr)
        except OSError as err:
            print("Execution failed:", err, file=sys.stderr)

    def run(self):
        try:
            self.status('Removing previous builds…')
            shutil.rmtree(pathlib.Path(HERE, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        self._call([sys.executable, "setup.py", "sdist", "bdist_wheel", "--universal"])

        self.status('Uploading the package to PyPi via Twine…')
        self._call(["twine", "upload", "dist/*"], shell=True)

        sys.exit()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    keywords=KEYWRODS,
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=REQUIRES,
    entry_points={
        "console_scripts": [
            "csaf-parser=csaf_parser.cli:main",
        ]
    },
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)

