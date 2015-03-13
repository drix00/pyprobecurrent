#!/usr/bin/env python
"""
.. py:currentmodule:: check_experimental_data
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Check experimental data.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Feb 9, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import os.path
import logging

# Third party modules.
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

# Local modules.
import pyMcGill.experimental.NanoPico.LogFile as LogFile

# Project modules

# Globals and constants variables.
log = False

def runSU8000():
    filenames = []
    filenames.append("beamCurrent_SU8000_set01_20150122.txt")
    filenames.append("beamCurrent_SU8000_set02_20150123.txt")
    #filenames.append("BeamCurrent_SU8000_Set03_20150126.txt")
    #filenames.append("BeamCurrent_SU8000_Set04_20150127.txt")
    #filenames.append("BeamCurrent_SU8000_Set05_20150128.txt")

    path = r"D:\work\results\experiments\BeamCurrent\SU8000\20150122_201501"

    createFigures(filenames, path)

def runSU8230():
    filenames = []
    filenames.append("BeamCurrent_SU8230_Set01_20150129.txt")
    filenames.append("BeamCurrent_SU8230_Set02_20150130.txt")
    filenames.append("BeamCurrent_SU8230_Set03_20150202.txt")
    filenames.append("BeamCurrent_SU8230_Set04_20150203.txt")
    filenames.append("BeamCurrent_SU8230_Set05_20150204.txt")
    filenames.append("BeamCurrent_SU8230_Set06_20150206.txt")
    filenames.append("BeamCurrent_SU8230_Set07_20150227.txt")

    path = r"D:\work\results\experiments\BeamCurrent\SU8230"

    createFigures(filenames, path)

def createFigures(filenames, path):
    for filename in filenames:
        logging.info(filename)
        filepath = os.path.join(path, filename)
        basepath, _extension = os.path.splitext(filepath)
        basename = os.path.basename(basepath)

        logFile = LogFile.LogFile(filepath)
        logFile._read(filepath)
        x = np.array(logFile.times_s)
        y = np.array(logFile.currents_nA)*(-1.0)

        x = x/60.0/60.0

        plt.figure()
        plt.title(basename)
        windowSize = 60*10
        #yFiltered = signal.wiener(y, windowSize)
        yFiltered = signal.medfilt(y, windowSize+1)
        if log:
            plt.semilogy(x, y)
            plt.semilogy(x[windowSize:-windowSize], yFiltered[windowSize:-windowSize])
        else:
            plt.plot(x, y)
            plt.plot(x[windowSize:-windowSize], yFiltered[windowSize:-windowSize])

        plt.xlabel("Time (h)")
        plt.ylabel("Current (nA)")

        figureFilepath = basepath + "_IvsT_raw"
        if log:
            figureFilepath += "_Log"
        extension = '.png'
        plt.savefig(figureFilepath+extension)

        plt.clf()
        plt.close()

def run():
    #runSU8000()
    runSU8230()

if __name__ == '__main__':  #pragma: no cover
    run()