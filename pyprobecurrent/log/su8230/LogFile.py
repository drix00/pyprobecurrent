#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.LogFile
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read SU-8000 log file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import logging
import datetime

# Third party modules.

# Local modules.

# Project modules
import pyprobecurrent.log.su8230.LogItem as LogItem

# Globals and constants variables.

class LogFile(object):
    def __init__(self):
        self.date = ""
        self.logItems = []

    def read(self, filepath):
        with open(filepath) as logFile:
            lineHeader = logFile.readline()
            logging.info("Header: %s", lineHeader)

            for line in logFile:
                if line.strip() != "":
                    try:
                        logItem = LogItem.LogItem(line)
                        self.logItems.append(logItem)
                    except IndexError as message:
                        logging.info(message)
                        logging.info(line)

    def uniqueInterv(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.interv)

        return uniques

    def uniqueFI(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.fromInstrument)

        return uniques

    def uniqueTI(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.toInstrument)

        return uniques

    def uniqueFITI(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add((logItem.fromInstrument, logItem.toInstrument))

        return uniques

    def uniqueCodes(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.code)

        return uniques

    def uniqueFITICode(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add((logItem.fromInstrument, logItem.toInstrument, logItem.code))

        return uniques

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        self._date = date

    @property
    def numberLines(self):
        return len(self.logItems)

    @property
    def logItems(self):
        return self._logItems
    @logItems.setter
    def logItems(self, logItems):
        self._logItems = logItems

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
