#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pyprobcurrent.__init__

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Project to analyze probe current measurement on Hitachi SEMs.
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
import os.path
import logging
import fnmatch
import configparser

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.
__author__ = """Hendrix Demers"""
__email__ = 'hendrix.demers@mail.mcgill.ca'
__version__ = '0.1.0'


def get_current_module_path(module_path, relative_path=""):
    base_path = os.path.dirname(module_path)

    file_path = os.path.join(base_path, relative_path)
    file_path = os.path.normpath(file_path)

    return file_path


def findAllFiles(root, patterns='*', ignorePathPatterns='', ignoreNamePatterns='', single_level=False, yield_folders=False):
    """
    Find all files in a root folder.

    From Python Cookbook section 2.16 pages 88--90

    Mandatory arguments:


    Optional arguments:


    Extra arguments:


    Return parameters:

    """
    # Expand patterns from semicolon-separated string to list
    patterns = patterns.split(';')
    ignorePathPatterns = ignorePathPatterns.split(';')

    root = os.path.abspath(root)
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)

        addPath = True
        for ignorePathPattern in ignorePathPatterns:
            if fnmatch.fnmatch(path, ignorePathPattern):
                addPath = False

        files.sort()

        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    addName = True
                    for ignorePattern in ignoreNamePatterns:
                        if fnmatch.fnmatch(name, ignoreNamePatterns):
                            addName = False

                    if addPath and addName:
                        yield os.path.join(path, name)
                        break

        if single_level:
            logging.debug("single_level")
            break


def getResultsMcGillPath(configurationFile, relativePath=""):
    """
    Read the configuration file for the results path for McGill.

    The configuration file need to have this entry:
    [Paths]
    resultsMcGillPath=/home/hdemers/resultsUdeS

    """
    sectionName = "Paths"
    keyName = "resultsMcGillPath"

    filepath = _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName)

    return filepath


def getLabbookMcGillPath(configurationFile, relativePath=""):
    """
    Read the configuration file for the mcgill labboook path for McGill.

    The configuration file need to have this entry:
    [Paths]
    labbookMcGillPath=J:\hdemers\work\mcgill2012\documents\labbook

    """
    sectionName = "Paths"
    keyName = "labbookMcGillPath"

    path = _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName)

    return path


def _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName):
    path = readValueFromConfigurationFile(configurationFile, sectionName, keyName)

    if relativePath.startswith('/'):
        relativePath = relativePath[1:]

    filepath = os.path.join(path, relativePath)
    filepath = os.path.normpath(filepath)
    return filepath


def readValueFromConfigurationFile(configurationFile, sectionName, keyName, default=None):
    config = configparser.SafeConfigParser()
    config.readfp(open(configurationFile))
    if config.has_section(sectionName):
        if config.has_option(sectionName, keyName):
            value = config.get(sectionName, keyName)
            return value
        else:
            logging.error("Configuration file (%s) does not have this option in section %s: %s", configurationFile,
                          keyName, sectionName)
            if default == None:
                raise configparser.NoOptionError(keyName, sectionName)
            else:
                return default
    else:
        logging.error("Configuration file (%s) does not have this section: %s", configurationFile, sectionName)
        if default == None:
            raise configparser.NoSectionError(sectionName)
        else:
            return default
