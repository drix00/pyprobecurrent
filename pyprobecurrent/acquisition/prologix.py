#!/usr/bin/env python
"""
.. py:currentmodule:: pyprobecurrent.acquisition.prologix
   :synopsis: Prologix GPID-USB controler

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Prologix GPID-USB controler
"""
from pip._vendor.pyparsing import line

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Mar 16, 2016"
__copyright__ = "Copyright (c) 2016 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import logging

# Third party modules.
import visa

# Local modules.

# Project modules

# Globals and constants variables.
GTL = chr(0x01)
SDC = chr(0x04)
GET = chr(0x08)
LLO = chr(0x11)
DCL = chr(0x14)
SPE = chr(0x18)
SPD = chr(0x19)
# Address 12
LAG = ','
# Address 12
TAG = 'L'
UNL = chr(0x3f)
UNT = chr(0x5f)

CMD_ADDRESS = "++addr"
CMD_AUTO = "++auto"
CMD_CLEAR = "++clr"
CMD_EOI = "++eoi"
CMD_EOS = "++eos"
CMD_EOT_ENABLE = "++eot_enable"
CMD_EOT_CHARACTER = "++eot_char"
CMD_IFC = "++ifc"
CMD_LLO = "++llo"
CMD_LOC = "++loc"
CMD_LON = "++lon"
CMD_MODE = "++mode"
CMD_READ = "++read"
CMD_READ_TIMEOUT = "++read_tmo_ms"
CMD_RESET = "++rst"
CMD_SAVE_CONFIGURATION = "++savecfg"
CMD_SPOLL = "++spoll"
CMD_SRQ = "++srq"
CMD_STATUS = "++status"
CMD_TRIGGER = "++trg"
CMD_VERSION = "++ver"
CMD_HELP = "++help"

class PrologixGpibUsbController(object):
    def __init__(self):
        self.gpib_usb = None
        self.init_controller()

    def init_controller(self):
        resource_manager = visa.ResourceManager()
        for resource_name in resource_manager.list_resources():
            instrument = resource_manager.open_resource(resource_name)
            version = instrument.query("++ver")
            if version.startswith("Prologix GPIB-USB Controller"):
                self.gpib_usb = instrument

    def log_controller_configuration(self):
        commands = []
        commands.append(CMD_ADDRESS)
        commands.append(CMD_AUTO)
        commands.append(CMD_EOI)
        commands.append(CMD_EOS)
        commands.append(CMD_EOT_ENABLE)
        commands.append(CMD_EOT_CHARACTER)
        commands.append(CMD_LON)
        commands.append(CMD_MODE)
        commands.append(CMD_SAVE_CONFIGURATION)
        commands.append(CMD_SRQ)
        commands.append(CMD_STATUS)
        commands.append(CMD_VERSION)

        for command in commands:
            status = self.gpib_usb.ask(command)
            status = self._formatAnswer(status)

            message = "%14s: %s" % (command, status)
            logging.info(message)

        self.gpib_usb.write(CMD_HELP)
        for i in range(33):
            data = self.gpib_usb.read().strip()
            print("%02i %s" % (i, data))

    def _formatAnswer(self, status):
        return status.strip()

    def setPort(self, port):
        self._port = port
        self._initController()

    def getName(self):
        if self.gpib_usb == None:
            self._initController()

        if self.gpib_usb != None:
            if self._checkVersion():
                return "Prologix Gpib Usb"

        return

    def getInstrumentName(self, address):
        instrumentName = "Unknown"
        if self.gpib_usb == None:
            self._initController()

        if self.gpib_usb != None:
            command = "++addr %s" % (str(address))
            self.gpib_usb.write(command)

            line = self.gpib_usb.read().strip()
            logging.info("Line:%s", line)
            self._logSrqState()

            line = line.strip()

            if line.startswith("NDCI"):
                instrumentName = "Keithley 220 Programmable current source"
            elif line.startswith("NDCV"):
                instrumentName = "Keithley 230 Programmable current source"
            else:
                instrumentName = line

        return instrumentName

    def _logSrqState(self):
        status = self.gpib_usb.ask("++srq")
        status = self._formatAnswer(status)
        logging.info("sqr: %s", status)

    def _checkVersion(self):
        version = self.gpib_usb.ask("++ver")
        version = self._formatAnswer(version)
        logging.info("Version: %s", version)

        versionString = "Prologix GPIB-USB Controller version 6.4"

        if version.strip() == versionString.strip():
            return True
        else:
            return False

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.INFO)

    controller = PrologixGpibUsbController()
    controller.log_controller_configuration()
