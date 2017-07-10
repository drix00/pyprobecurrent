#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.LogFiles
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read all Hitachi log files.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2014 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path
import logging

# Third party modules.

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules
import pyprobecurrent.log.su8230.LogFile as LogFile

# Globals and constants variables.

class LogFiles(object):
    def __init__(self, path):
        self.path = path

        self._logFilepaths = {}
        self._logFileDates = {}

    def findLogFiles(self):
        patterns = "Sem*.log"
        for filepath in Files.findAllFiles(self.path, patterns):
            filename = os.path.basename(filepath)
            basename, _extension = os.path.splitext(filename)
            logging.debug(basename)
            self._logFilepaths[basename] = filepath
            fileDate = os.path.getmtime(filepath)
            self._logFileDates[fileDate] = basename

    def readLastLogFile(self):
        lastFileDate = sorted(self._logFileDates.keys())[-1]
        lastFilename = self._logFileDates[lastFileDate]
        logging.info("Last log file name: %s", lastFilename)

        filepath = self._logFilepaths[lastFilename]

        logFile = LogFile.LogFile()
        logFile.read(filepath)

        return logFile

    def read_all_log_files(self):
        log_file = LogFile.LogFile()
        for file_Date in sorted(self._logFileDates.keys()):
            filename = self._logFileDates[file_Date]
            logging.info("Log file name: %s", filename)

            file_path = self._logFilepaths[filename]

            log_file = LogFile.LogFile()
            log_file.read(file_path)

            log_file.add_items(log_file.logItems)

        return log_file

    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, path):
        self._path = path

    @property
    def numberLogFiles(self):
        return len(self._logFilepaths)
