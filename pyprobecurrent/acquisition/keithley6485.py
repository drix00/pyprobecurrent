#!/usr/bin/env python
"""
.. py:currentmodule:: pyprobecurrent.acquisition.keithley6485
   :synopsis: Keithley 6485 Picoammeter

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Keithley 6485 Picoammeter
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Mar 18, 2016"
__copyright__ = "Copyright (c) 2016 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import logging

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.
CURRENT_A = "I"
VOLTAGE_V = "V"
DWELL_TIME_s = "W"
BUFFER_ADDRESS = "B"
DISPLAY_LOCATION = "L"

class Keithley6485Picoammeter():
    def __init__(self, controller):
        self.controller = controller
        self.controller.gpib_usb.write("++addr 14")

    def identification(self):
        self.controller.gpib_usb.write("*IDN?")
        data = self.controller.gpib_usb.ask("++read eoi")
        data = data.strip()
        logging.debug("Dataline:%s", data)

        return data

    def query_errror_queue(self):
        data = self.controller.gpib_usb.query("STAT:QUE?")
        data = data.strip()
        logging.debug("Error queue: %s", data)
        return data

    def mesure_current(self):
        self.controller.gpib_usb.write("CONF:CURR")
        data = self.controller.gpib_usb.query("READ?")
        data = data.strip()
        logging.debug("Current: %s", data)
        return data
