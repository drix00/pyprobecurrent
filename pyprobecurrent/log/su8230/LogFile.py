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
            logging.debug("Header: %s", lineHeader)

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

    def unique_log_message(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.logMessage)

        return uniques

    def unique_log_command(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.command)

        return uniques

    def unique_log_command_number(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.commandNumber)

        return uniques

    def unique_log_message(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.logMessage)

        return uniques

    def unique_log_command_parameter(self):
        uniques = set()
        for logItem in self.logItems:
            uniques.add(logItem.parameter)

        return uniques

    def print_unique_item(self):
        if self.logItems:
            logging.info("Number of lines: %i", self.numberLines)

            uniqueInterv = self.uniqueInterv()
            logging.info("Number of unique Interv: %i", len(uniqueInterv))

            uniqueFI = self.uniqueFI()
            logging.info("Number of unique from instrument: %i", len(uniqueFI))
            logging.info("Unique from instruments: %s", uniqueFI)

            uniqueTI = self.uniqueTI()
            logging.info("Number of unique to instrument: %i", len(uniqueTI))
            logging.info("Unique to instruments: %s", uniqueTI)

            uniqueFITI = self.uniqueFITI()
            logging.info("Number of unique from/to instrument: %i", len(uniqueFITI))
            logging.info("Unique from/to instruments:")
            for fi, ti in uniqueFITI:
                logging.debug("                          : %s, %s", fi, ti)

            uniqueCodes = self.uniqueCodes()
            logging.info("Number of unique code: %i", len(uniqueCodes))
            logging.info("Unique codes: %s", uniqueCodes)

            uniqueFITICode = self.uniqueFITICode()
            logging.info("Number of unique from/to instrument with code: %i", len(uniqueFITICode))
            logging.info("Unique from/to instruments code:")
            for fi, ti, code in uniqueFITICode:
                logging.info("                          : %s, %s, %s", fi, ti, code)

            unique_log_message = self.unique_log_message()
            logging.info("Number of unique log messages: %i", len(unique_log_message))
            logging.info("Unique log messages: %s", unique_log_message)

            # unique_command = self.unique_log_command()
            # logging.info("Number of unique commands: %i", len(unique_command))
            # logging.info("Unique commands: %s", unique_command)
            #
            # unique_command_number = self.unique_log_command_number()
            # logging.info("Number of unique command numberss: %i", len(unique_command_number))
            # logging.info("Unique command numbers: %s", unique_command_number)
            #
            # unique_message = self.unique_log_message()
            # logging.info("Number of unique commands: %i", len(unique_message))
            # logging.info("Unique commands: %s", unique_message)
            #
            # unique_command_parameter = self.unique_log_command_parameter()
            # logging.info("Number of unique command numberss: %i", len(unique_command_parameter))
            # logging.info("Unique command numbers: %s", unique_command_parameter)

    def add_items(self, new_log_items):
        self.logItems.extend(new_log_items)

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


if __name__ == '__main__':  # pragma: no cover
    run()
