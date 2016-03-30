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
    #controller.log_controller_configuration()

    #message = controller.getInstrumentName(14)
    #print(message)

    picoammeter = Keithley6485Picoammeter(controller)
    message = picoammeter.identification()
    print(message)
    message = picoammeter.query_errror_queue()
    print(message)
    message = picoammeter.mesure_current()
    print(message)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.INFO)
    run()
