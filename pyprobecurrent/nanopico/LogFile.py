#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.nanopico.LogFile
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

description
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import datetime

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.


class LogFile(object):
    def __init__(self, filepath):
        self.currents_nA = []
        self.times_s = []

        self._filepath = filepath

    def _read(self, filepath):
        lines = open(filepath, 'r').readlines()

        self._readInit(lines[1])

        for line in lines[4:]:
            items = line.split('\t')

            try:
                currentTime_s = self._extractDateTime(items[0])
                self.times_s.append(currentTime_s)

                current_nA = float(items[1])
                self.currents_nA.append(current_nA)
            except ValueError:
                pass

        #assert float(len(self.times_s)) == self.times_s[-1]

    def _readInit(self, line):
        self._startTime = self._extractStartTime(line)
        self._previousDateTime = self._startTime
        self._currentTime_s = 0.0
        self._currentDay = 0

    def _extractStartTime(self, line):
        """
        3/27/2012 8:16:32 PM
        """
        formatDateTime = "%m/%d/%Y %I:%M:%S %p"
        dateTimeStr = line.replace("Logging started at", '')
        startDateTime = datetime.datetime(2012, 1, 1)
        startDateTime = startDateTime.strptime(dateTimeStr.strip(), formatDateTime)
        self.start_time = startDateTime.isoformat()
        return startDateTime

    def _extractTime(self, timeStr):
        """
        5:40:50 PM
        """
        formatDateTime = "%I:%M:%S %p"
        startDateTime = self._startTime
        curentDateTime = startDateTime.strptime(timeStr, formatDateTime).time()
        return curentDateTime

    def _extractDateTime(self, timeStr):
        curentDateTime = self._extractTime(timeStr)
        date = self._startTime.date()
        date += datetime.timedelta(days=self._currentDay)
        curentDateTime = datetime.datetime.combine(date, curentDateTime)
        if curentDateTime < self._previousDateTime:
            self._currentDay += 1
            curentDateTime += datetime.timedelta(days=1.0)

        deltaTime_s = curentDateTime - self._previousDateTime
        self._currentTime_s += deltaTime_s.total_seconds()
        self._previousDateTime = curentDateTime

        return self._currentTime_s

    @property
    def start_time(self):
        return self._start_time
    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def currents_nA(self):
        return self._currents_nA
    @currents_nA.setter
    def currents_nA(self, currents_nA):
        self._currents_nA = currents_nA

    @property
    def times_s(self):
        return self._times_s
    @times_s.setter
    def times_s(self, times_s):
        self._times_s = times_s

    @property
    def numberPoints(self):
        return len(self.currents_nA)

def run():
    import pyHendrixDemersTools.Files as Files
    import os.path
    import matplotlib.pyplot as plt

    dataPath = Files.getCurrentModulePath(__file__, "../../testData/nanopico")
    #filepath = os.path.join(dataPath, "testCurrent_10s.txt")
    filepath = os.path.join(dataPath, "testCurrent_1s.txt")
    #filepath = os.path.join(dataPath, "testCurrent.txt")
    logFile = LogFile(filepath)
    logFile._read(filepath)

    plt.figure()
    x = logFile.times_s
    y = logFile.currents_nA
    plt.plot(x, y)

    plt.xlabel("Time (s)")
    plt.ylabel("Current (nA)")

    plt.show()

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
