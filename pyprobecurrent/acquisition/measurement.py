#!/usr/bin/env python
"""
.. py:currentmodule:: pyprobecurrent.acquisition.measurement
   :synopsis: Script to measure the current from Keithley 6485 Picoammeter

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Script to measure the current from Keithley 6485 Picoammeter
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
from pyprobecurrent.acquisition.prologix import PrologixGpibUsbController
from pyprobecurrent.acquisition.keithley6485 import Keithley6485Picoammeter

# Globals and constants variables.

def run():
    controller = PrologixGpibUsbController()
    if controller.gpib_usb is None:
        print("Controller not found.")
        return

    controller.log_controller_configuration()
    controller._logSrqState()

    picoammeter = Keithley6485Picoammeter(controller)

    message = picoammeter.identification()
    if message.startswith("VI_ERROR_TMO"):
        print("Picoammeter not found.")
        return
    print(message)

    #picoammeter.log_options()
    #picoammeter.do_zero_correction()

    #print(picoammeter.query_error_queue())
    #print(picoammeter.do_one_reading())

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.INFO)
    run()
    print("Done")
