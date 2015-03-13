#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.LogItem
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Log item for the SU-8000 log file.
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
LOG_ITEM_DATE = "Date"
LOG_ITEM_TIME = "Time"
LOG_ITEM_INTERV = "Interv"
LOG_ITEM_FI = "FI"
LOG_ITEM_TI = "TI"
LOG_ITEM_CODE = "Code"
LOG_ITEM_LOG = "Log"

LOG_ITEM_MESSAGE = "Message"
LOG_ITEM_COMMAND_NUMBER = "Cmd No"
LOG_ITEM_COMMAND = "Command"
LOG_ITEM_PARAMETER = "Parameter"

LOG_ITEM_UNIT_PC_MSG = "PC Msg"

class LogItem(object):
    def __init__(self, line):
        self._value = {}

        self._extractItemsFromLine(line)

    def _extractItemsFromLine(self, line):
        items = line.split(',')

        self.date, self.time = self._extractDatetime(items[0])
        self.interv = self._extractInterv(items[1])
        self.fromInstrument = self._extractFromInstrument(items[2])
        self.toInstrument = self._extractToInstrument(items[3])
        self.code = self._extractCode(items[4])
        self.logMessage = self._extractLog(items[5])

#         if self.unit == LOG_ITEM_UNIT_PC_MSG or len(items) == 5:
#             self.message = self._extractMessage(items[4])
#             self.commandNumber = None
#             self.command = None
#             self.parameter = None
#         elif len(items) == 6:
#             self.unit = None
#             self.message = self._extractMessage(items[5])
#             self.commandNumber = None
#             self.command = self._extractCommand(items[3])
#             self.parameter = None
#         else:
#             self.message = None
#             self.commandNumber = self._extractCommandNumber(items[4])
#             self.command = self._extractCommand(items[5])
#             self.parameter = self._extractParameter(items[6])

    def _extractDatetime(self, datetimeStr):
        items = datetimeStr.split(' ')
        date = self._extractDate(items[0])
        time = self._extractTime(items[1])

        return date, time

    def _extractDate(self, dateStr):
        dateFormat = "%Y/%m/%d"
        dateTime = datetime.datetime.strptime(dateStr, dateFormat)
        date = dateTime.date()
        return date

    def _extractTime(self, dateStr):
        dateFormat = "%H:%M:%S"
        dateTime = datetime.datetime.strptime(dateStr, dateFormat)
        time = dateTime.time()
        return time

    def _extractInterv(self, item):
        interv = item.strip()
        return interv

    def _extractFromInstrument(self, item):
        fromInstrument = item.strip()
        return fromInstrument

    def _extractToInstrument(self, item):
        toInstrument = item.strip()
        return toInstrument

    def _extractCode(self, item):
        code = item.strip()
        return code

    def _extractLog(self, item):
        logMessage = item.strip()
        return logMessage

    def _extractCommandNumber(self, item):
        commandNumber = item.strip()
        return commandNumber

    def _extractCommand(self, item):
        command = item.strip()
        return command

    def _extractParameter(self, item):
        parameter = item.strip()
        return parameter

    @property
    def date(self):
        return self._value[LOG_ITEM_DATE]
    @date.setter
    def date(self, date):
        self._value[LOG_ITEM_DATE] = date

    @property
    def time(self):
        return self._value[LOG_ITEM_TIME]
    @time.setter
    def time(self, time):
        self._value[LOG_ITEM_TIME] = time

    @property
    def interv(self):
        return self._value[LOG_ITEM_INTERV]
    @interv.setter
    def interv(self, interv):
        self._value[LOG_ITEM_INTERV] = interv

    @property
    def fromInstrument(self):
        return self._value[LOG_ITEM_FI]
    @fromInstrument.setter
    def fromInstrument(self, fromInstrument):
        self._value[LOG_ITEM_FI] = fromInstrument

    @property
    def toInstrument(self):
        return self._value[LOG_ITEM_TI]
    @toInstrument.setter
    def toInstrument(self, toInstrument):
        self._value[LOG_ITEM_TI] = toInstrument

    @property
    def code(self):
        return self._value[LOG_ITEM_CODE]
    @code.setter
    def code(self, code):
        self._value[LOG_ITEM_CODE] = code

    @property
    def logMessage(self):
        return self._value[LOG_ITEM_LOG]
    @logMessage.setter
    def logMessage(self, logMessage):
        self._value[LOG_ITEM_LOG] = logMessage

    @property
    def message(self):
        return self._value[LOG_ITEM_MESSAGE]
    @message.setter
    def message(self, message):
        self._value[LOG_ITEM_MESSAGE] = message

    @property
    def commandNumber(self):
        return self._value[LOG_ITEM_COMMAND_NUMBER]
    @commandNumber.setter
    def commandNumber(self, commandNumber):
        self._value[LOG_ITEM_COMMAND_NUMBER] = commandNumber

    @property
    def command(self):
        return self._value[LOG_ITEM_COMMAND]
    @command.setter
    def command(self, command):
        self._value[LOG_ITEM_COMMAND] = command

    @property
    def parameter(self):
        return self._value[LOG_ITEM_PARAMETER]
    @parameter.setter
    def parameter(self, parameter):
        self._value[LOG_ITEM_PARAMETER] = parameter

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
