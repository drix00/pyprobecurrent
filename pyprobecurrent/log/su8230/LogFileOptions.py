#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.LogFileOptions
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read SU-8000 log file option.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""
# Standard library modules.
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.
SECTION_NAME_LOGFILE = "logFile"
OPTION_NAME_LOG = "Log"
OPTION_NAME_LOGMODE = "LogMode"
OPTION_NAME_NEXTFILE = "NextFile"
OPTION_NAME_FILESIZE = "FileSize"
OPTION_NAME_FILECOUNTS = "FileCnt"
OPTION_NAME_VERSION = "Version"

class LogFileOptions(object):
    def __init__(self):
        self._values = {}

    def read(self, filepath):
        configParser = configparser.SafeConfigParser()
        configParser.read(filepath)

        sectionName = SECTION_NAME_LOGFILE
        for optionName in self._getOptionNames():
            if optionName == OPTION_NAME_LOG:
                self._values[optionName] = configParser.getboolean(sectionName, optionName)
            elif optionName == OPTION_NAME_FILESIZE or optionName == OPTION_NAME_FILECOUNTS:
                self._values[optionName] = configParser.getint(sectionName, optionName)
            else:
                self._values[optionName] = configParser.get(sectionName, optionName)

    def _getOptionNames(self):
        optionNames = []

        optionNames.append(OPTION_NAME_LOG)
        optionNames.append(OPTION_NAME_LOGMODE)
        optionNames.append(OPTION_NAME_NEXTFILE)
        optionNames.append(OPTION_NAME_FILESIZE)
        optionNames.append(OPTION_NAME_FILECOUNTS)
        optionNames.append(OPTION_NAME_VERSION)

        return optionNames

    @property
    def isLogging(self):
        return self._values[OPTION_NAME_LOG]
    @isLogging.setter
    def isLogging(self, isLogging):
        self._values[OPTION_NAME_LOG] = isLogging

    @property
    def logMode(self):
        return self._values[OPTION_NAME_LOGMODE]
    @logMode.setter
    def logMode(self, logMode):
        self._values[OPTION_NAME_LOGMODE] = logMode

    @property
    def nextFile(self):
        return self._values[OPTION_NAME_NEXTFILE]
    @nextFile.setter
    def nextFile(self, nextFile):
        self._values[OPTION_NAME_NEXTFILE] = nextFile

    @property
    def filesize(self):
        return self._values[OPTION_NAME_FILESIZE]
    @filesize.setter
    def filesize(self, filesize):
        self._values[OPTION_NAME_FILESIZE] = filesize

    @property
    def fileCounts(self):
        return self._values[OPTION_NAME_FILECOUNTS]
    @fileCounts.setter
    def fileCounts(self, fileCounts):
        self._values[OPTION_NAME_FILECOUNTS] = fileCounts

    @property
    def version(self):
        return self._values[OPTION_NAME_VERSION]
    @version.setter
    def version(self, version):
        self._values[OPTION_NAME_VERSION] = version


if __name__ == '__main__':  # pragma: no cover
    run()
