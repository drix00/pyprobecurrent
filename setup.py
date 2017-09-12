#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: setup.py

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

SEtup project for deplyement on pypi
"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import os
import zipfile
from distutils.cmd import Command

# Third party modules.
from setuptools import setup, find_packages

# Local modules.

# Project modules.
from pyprobecurrent import __version__

# Globals and constants variables.


class TestDataCommand(Command):

    description = "create a zip of all files in the testData folder"
    user_options = [('dist-dir=', 'd',
                     "directory to put final built distributions in "
                     "[default: dist]"), ]

    def initialize_options(self):
        self.dist_dir = None

    def finalize_options(self):
        if self.dist_dir is None:
            self.dist_dir = "dist"

    def run(self):
        if not os.path.isdir(self.dist_dir):
            os.makedirs(self.dist_dir)

        basepath = os.path.dirname(__file__)
        testdatapath = os.path.join(basepath, 'testData')

        zipfilename = self.distribution.get_fullname() + '-testData.zip'
        zipfilepath = os.path.join(self.dist_dir, zipfilename)
        with zipfile.ZipFile(zipfilepath, 'w') as z:
            for root, _dirs, files in os.walk(testdatapath):
                for file in files:
                    filename = os.path.join(root, file)
                    arcname = os.path.relpath(filename, basepath)
                    z.write(filename, arcname)


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyodbc',
    "matplotlib",
    "scipy",
]

test_requirements = [
    'nose', 'coverage'
]

description = "Project to analyze probe current measurement on Hitachi SEMs."
# long_description = readme + '\n\n' + history
long_description = """
Project to analyze probe current measurement on Hitachi SEMs.
"""

packages = find_packages()

setup(
    name="pyProbeCurrent",
    version=__version__,
    url='https://github.com/drix00/pyprobecurrent',
    description=description,
    long_description=long_description,
    author="Hendrix Demers",
    author_email="hendrix.demers@mail.mcgill.ca",
    license="Apache Software License 2.0",
    classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: Apache Software License',
                 'Natural Language :: English',
                   'Programming Language :: Python',
                 "Programming Language :: Python :: 2",
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Operating System :: OS Independent',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Physics'],

    packages=packages,
    package_dir={'pyprobecurrent':
                     'pyprobecurrent'},

    include_package_data=False,  # Do not include test data

    install_requires=requirements,
    setup_requires=['nose', 'coverage'],

    test_suite='nose.collector',
    tests_require=test_requirements,

    cmdclass={'zip_testdata': TestDataCommand},
)

