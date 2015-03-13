#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.AnalyzeSU3500LogFiles
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Analize Su-3500 log files.
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
from . import LogFiles

# Project modules

# Globals and constants variables.


def analyze20140502():
    logging.info("Analyze log files of %s", "20140502")

    basepath = r"K:\hdemers\results\experiments\SU3500\logs\Hitachi_20140502"
    relativePath = r"PC_SEM\Log"
    path = os.path.join(basepath, relativePath)

    if os.path.isdir(path):
        logging.info("Path exist: %s", path)
        logFiles = LogFiles.LogFiles(path)
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

def analyze20141026():
    logging.info("Analyze log files of %s", "20141026")

    basepath = r"K:\hdemers\results\experiments\SU3500\logs\Hitachi_20141026"
    relativePath = r"PC_SEM\Log"
    path = os.path.join(basepath, relativePath)

    if os.path.isdir(path):
        logging.info("Path exist: %s", path)
        logFiles = LogFiles.LogFiles(path)
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
    #analyze20140502()
    analyze20141026()

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
