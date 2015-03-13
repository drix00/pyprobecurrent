#!/usr/bin/env python
"""
.. py:currentmodule:: log.su8230.exported_ras
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read exported RAS data file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Mar 2, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import csv
import logging

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.
ETC_ID = "EtcID"
ETC_DATE = "EtcDate"
ETC_COMMAND = "Command"
ETC_PARAMETERS = "EtcParameters"

ETC_COMMAND_SEMON = "SEMON"
ETC_COMMAND_SEMOFF = "SEMOFF"
ETC_COMMAND_HVN = "HVN"
ETC_COMMAND_SEMOFF = "SEMOFF"
ETC_COMMAND_FLSH = "FLSH"

EMISSION_ID = "EmissionID"
EMISSION_DATE = "EmissionDate"
EMISSION_CURRENT = "EmissionCurrent"
EMISSION_VEXT = "Vext"
EMISSION_IF = "If"
EMISSION_VS = "Vs"
EMISSION_VACC = "Vacc"
EMISSION_VD = "Vd"

class FlashParameters(object):
    def __init__(self, paramtersStr):
        items = paramtersStr.split(',')

        self.flashIntensity = int(items[0])
        self.flashCode = int(items[1])
        self.acceleratingVoltage_V = float(items[2])
        self.emissionCurrent_uA = float(items[3])

    @property
    def flashIntensity(self):
        return self._flashIntensity
    @flashIntensity.setter
    def flashIntensity(self, flashIntensity):
        self._flashIntensity = flashIntensity

    @property
    def flashCode(self):
        return self._flashCode
    @flashCode.setter
    def flashCode(self, flashCode):
        self._flashCode = flashCode

    @property
    def acceleratingVoltage_V(self):
        return self._acceleratingVoltage_V
    @acceleratingVoltage_V.setter
    def acceleratingVoltage_V(self, acceleratingVoltage_V):
        self._acceleratingVoltage_V = acceleratingVoltage_V

    @property
    def emissionCurrent_uA(self):
        return self._emissionCurrent_uA
    @emissionCurrent_uA.setter
    def emissionCurrent_uA(self, emissionCurrent_uA):
        self._emissionCurrent_uA = emissionCurrent_uA

def read_etc(filepath):
    etcData = []

    fieldnames = [ETC_ID, ETC_DATE, ETC_COMMAND, ETC_PARAMETERS]
    reader = csv.DictReader(open(filepath), fieldnames=fieldnames)

    # Skip header.
    next(reader)

    for row in reader:
        etcData.append(row)

    return etcData


def getFlash(filepath):
    etcData = read_etc(filepath)

    flashData = []
    for data in etcData:
        if data[ETC_COMMAND] == ETC_COMMAND_FLSH:
            flashData.append(data)

    return flashData

def read_emission(filepath):
    emissionData = []

    fieldnames = [EMISSION_ID, EMISSION_DATE, EMISSION_CURRENT, EMISSION_VEXT, EMISSION_IF, EMISSION_VS, EMISSION_VACC, EMISSION_VD]
    reader = csv.DictReader(open(filepath), fieldnames=fieldnames)

    # Skip header.
    next(reader)

    for row in reader:
        emissionData.append(row)

    return emissionData

def uniqueParameter(parameterData, parameter_name):
    parameterSet = set()
    for data in parameterData:
        parameter = data[parameter_name]
        parameterSet.add(parameter)

    logging.info(parameterSet)
    return parameterSet

def runFlash():
    from pyHendrixDemersTools.Files import getCurrentModulePath
    import os.path
    import matplotlib.pyplot as plt

    path = getCurrentModulePath(__file__, "../../../testdata/su8230")
    filename = "Ras_20150302_Etc.txt"
    filepath = os.path.join(path, filename)

    flashData = getFlash(filepath)

    indices = []
    flashIntensities = []
    emissionCurrents_uA = []
    acceleratingVoltages_V = []

    index = 0
    for data in flashData:
        flash_parameters = FlashParameters(data[ETC_PARAMETERS])
        flashIntensity = flash_parameters.flashIntensity
        emissionCurrent_uA = flash_parameters.emissionCurrent_uA
        acceleratingVoltage_V = flash_parameters.acceleratingVoltage_V

        if emissionCurrent_uA > 0.0:
            indices.append(index)
            emissionCurrents_uA.append(emissionCurrent_uA)
            flashIntensities.append(flashIntensity)
            acceleratingVoltages_V.append(acceleratingVoltage_V)

            index += 1

    fig, ax_f = plt.subplots()
    ax_c = ax_f.twinx()

    ax_f.plot(indices, emissionCurrents_uA, 'o')

    ax_c.plot(indices, flashIntensities, 'or')

    plt.figure()
    plt.plot(indices, flashIntensities, '.')

    plt.figure()
    plt.plot(indices, emissionCurrents_uA, '.')

    plt.figure()
    plt.plot(indices, acceleratingVoltages_V, '.')

    plt.show()

def run():
    from pyHendrixDemersTools.Files import getCurrentModulePath
    import os.path
    import matplotlib.pyplot as plt

    path = getCurrentModulePath(__file__, "../../../testdata/su8230")
    filename = "Ras_20150302_Emission.txt"
    filepath = os.path.join(path, filename)

    emissionData = read_emission(filepath)

    indices = []
    emissionCurrents_uA = []
    extractionVoltages_V = []
    acceleratingVoltages_V = []

    index = 0
    for data in emissionData:
        emissionCurrent_uA = float(data[EMISSION_CURRENT])*1.0e-1
        extractionVoltage_V = float(data[EMISSION_VEXT])
        acceleratingVoltage_V = float(data[EMISSION_VACC])
        if emissionCurrent_uA > 0.0 and extractionVoltage_V > 0.0:
            indices.append(index)
            emissionCurrents_uA.append(emissionCurrent_uA)
            extractionVoltages_V.append(extractionVoltage_V)
            acceleratingVoltages_V.append(acceleratingVoltage_V)

            index += 1

    fig, ax_f = plt.subplots()
    ax_c = ax_f.twinx()

    ax_f.plot(indices, emissionCurrents_uA, 'o')

    ax_c.plot(indices, extractionVoltages_V, 'or')
    ax_c.set_ylim(top=4000.0)

    plt.figure()
    plt.plot(acceleratingVoltages_V, extractionVoltages_V, '.')
    plt.ylim(ymax=4000.0)

    plt.figure()
    plt.plot(acceleratingVoltages_V, emissionCurrents_uA, '.')

    plt.show()

if __name__ == '__main__':  #pragma: no cover
    runFlash()