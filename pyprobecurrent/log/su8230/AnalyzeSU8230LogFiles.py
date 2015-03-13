#!/usr/bin/env python
"""
.. py:currentmodule:: log.su8230.AnalyzeSU8230LogFiles
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Analyze Hitachi SU-8230 log files.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Feb 27, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import logging
import os.path

# Third party modules.

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules
from pyprobecurrent.log.su8230.LogFiles import LogFiles

# Globals and constants variables.

def runTestFile():
    #filepath = Files.getCurrentModulePath(__file__, "../../../testData/su8230/log/Sem065.log")
    path = Files.getCurrentModulePath(__file__, "../../../testData/su8230/log/")

    if os.path.isdir(path):
        logging.info("Path exist: %s", path)
        logFiles = LogFiles(path)
        logFiles.findLogFiles()

        logging.info("Number of log files: %i", logFiles.numberLogFiles)

        logFile = logFiles.readLastLogFile()

        if logFile is not None:
            logging.info("Number of lines: %i", logFile.numberLines)

            uniqueInterv = logFile.uniqueInterv()
            logging.info("Number of unique Interv: %i", len(uniqueInterv))

            uniqueFI = logFile.uniqueFI()
            logging.info("Number of unique from instrument: %i", len(uniqueFI))
            logging.info("Unique from instruments: %s", uniqueFI)

            uniqueTI = logFile.uniqueTI()
            logging.info("Number of unique to instrument: %i", len(uniqueTI))
            logging.info("Unique to instruments: %s", uniqueTI)

            uniqueFITI = logFile.uniqueFITI()
            logging.info("Number of unique from/to instrument: %i", len(uniqueFITI))
            logging.info("Unique from/to instruments:")
            for fi, ti in uniqueFITI:
                logging.debug("                          : %s, %s", fi, ti)

            uniqueCodes = logFile.uniqueCodes()
            logging.info("Number of unique code: %i", len(uniqueCodes))
            logging.info("Unique codes: %s", uniqueCodes)

            uniqueFITICode = logFile.uniqueFITICode()
            logging.info("Number of unique from/to instrument with code: %i", len(uniqueFITICode))
            logging.info("Unique from/to instruments code:")
            for fi, ti, code in uniqueFITICode:
                logging.info("                          : %s, %s, %s", fi, ti, code)

def run():
    runTestFile()

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.INFO)
    run()