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
import pyvisa

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
        self.controller.gpib_usb.write("*RST")
        #self.controller.gpib_usb.write("status:preset")
        self.controller.gpib_usb.write("*CLS")
        #print(self.controller.gpib_usb.read().strip())

    def log_options(self):
        data = self.controller.gpib_usb.query("SYST:LRF?")
        logging.info("Line frequency: %s", data)
        data = self.controller.gpib_usb.query("SYST:LRF:AUTO?")
        logging.info("Line frequency auto: %s", data)
        data = self.controller.gpib_usb.query("SYST:AZER?")
        logging.info("Autozero: %s", data)

    def do_zero_correction(self):
        self.controller.gpib_usb.write("*RST")
        self.controller.gpib_usb.write("SYST:ZCH ON")
        self.controller.gpib_usb.write("CURR:RANG 2E-4")
        self.controller.gpib_usb.write("INIT")
        self.controller.gpib_usb.write("SYST:ZCOR:ACQ")
        self.controller.gpib_usb.write("SYST:ZCH OFF")
        self.controller.gpib_usb.write("SYST:ZCOR ON")

    def do_one_reading(self):
        self.controller.gpib_usb.write("*RST")
        self.controller.gpib_usb.write("SYST:ZCH ON")
        self.controller.gpib_usb.write("CURR:RANG 2E-9")
        self.controller.gpib_usb.write("INIT")
        self.controller.gpib_usb.write("SYST:ZCOR:ACQ")
        self.controller.gpib_usb.write("SYST:ZCOR ON")
        self.controller.gpib_usb.write("CURR:RANG:AUTO ON")
        self.controller.gpib_usb.write("SYST:ZCH OFF")
        data = self.controller.gpib_usb.query("READ?")
        data = data.strip()
        logging.debug("Current: %s", data)
        return data

    def identification(self):
        try:
            self.controller.gpib_usb.write("*IDN?")
            data = self.controller.gpib_usb.ask("++read eoi")
            data = data.strip()
            logging.debug("Dataline:%s", data)
        except pyvisa.errors.VisaIOError as message:
            data = message.abbreviation
        return data

    def query_error_queue(self):
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
