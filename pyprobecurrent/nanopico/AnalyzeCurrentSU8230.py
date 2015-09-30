#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.nanopico.AnalyzeCurrentSU8230
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Analyze the current from SU-8230.
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
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
import scipy.signal as signal

# Local modules.
import pyHendrixDemersTools.Files as Files
import pyHendrixDemersTools.Graphics as Graphics

# Project modules
import pyMcGill.experimental.NanoPico.LogFile as LogFile

# Globals and constants variables.

def analyzeAllBeamCurrentMeasurement():
    folders = []
    folders.append(r"K:\hdemers\results\experiments\SU8230\hdemers\BeamCurrent")

    for folder in folders:
        dataPath = folder
        for filepath in Files.findAllFiles(dataPath, "*.txt"):
            logging.info(filepath)
            _createFigures(filepath)

def _createFigures(filepath):
    _createFigureVersusTime(filepath)
    _createFigureVersusTime(filepath, log=True)
    _createFigureResidual(filepath)

def _createFigureVersusTime(filepath, log=False):
    basepath, _extension = os.path.splitext(filepath)
    basename = os.path.basename(basepath)

    logFile = LogFile.LogFile(filepath)
    logFile._read(filepath)
    x = np.array(logFile.times_s)
    y = np.array(logFile.currents_nA)*(-1.0)

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

    figureFilepath = basepath + "_IvsT"
    if log:
        figureFilepath += "_Log"
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    plt.clf()
    plt.close()

def _createFigureResidual(filepath):
    basepath, _extension = os.path.splitext(filepath)
    basename = os.path.basename(basepath)

    logFile = LogFile.LogFile(filepath)
    logFile._read(filepath)
    x = np.array(logFile.times_s)
    y = np.array(logFile.currents_nA)*(-1.0)

    windowSize = 60*10
    if len(x) < windowSize:
        return

    #yFiltered = signal.wiener(y, windowSize)
    yFiltered = signal.medfilt(y, windowSize+1)

    residual = y - yFiltered

    plt.figure()
    plt.title(basename)
    plt.plot(x[windowSize:-windowSize], residual[windowSize:-windowSize])

    plt.xlabel("Time (s)")
    plt.ylabel("Residual")

    figureFilepath = basepath + "_RvsT"
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    plt.clf()
    plt.close()

def _get20140127Data():
    dataPath = r"K:\hdemers\results\experiments\SU8230\hdemers\BeamCurrent"
    filename = "BeamCurrent_20140127.txt"

    filepath = os.path.join(dataPath, filename)
    logFile = LogFile.LogFile(filepath)
    logFile._read(filepath)

    x = np.array(logFile.times_s)
    y = np.array(logFile.currents_nA)

    return x, y

def _get20140128Data():
    dataPath = r"K:\hdemers\results\experiments\SU8230\hdemers\BeamCurrent"
    filename = "BeamCurrent_20140128.txt"

    filepath = os.path.join(dataPath, filename)
    logFile = LogFile.LogFile(filepath)
    logFile._read(filepath)

    x = np.array(logFile.times_s)
    y = np.array(logFile.currents_nA)

    return x, y

def runAnalyzeCurrent():
    xA, yA = _get20140127Data()
    xB, yB = _get20140128Data()

    # inverse current sign
    yA *= -1
    yB *= -1

    # scale
    #yB -= 3.45

    plt.figure()

    xA += 5.47*60.0*60.0
    #plt.plot(xA, yA, label='End of the day')
    plt.plot(xB, yB, label='Right after flashing')

    plt.xlabel("Time (s)")
    plt.ylabel("Current (nA)")
    #plt.legend(loc='best')

    xMax_s = 12.0*60.0*60.0
    xMin_s = min(xA[0], xB[0])
    plt.xlim((xMin_s, xMax_s))
    plt.ylim(ymax=2.5)

    ax2 = plt.gca().twiny()
    ax2.set_xlim((xMin_s/60.0/60.0, xMax_s/60.0/60.0))
    ax2.set_xlabel("Time (h)")

    configurationFilepath = Files.getCurrentModulePath(__file__, "../../pyMcGill.cfg")
    graphicPath = Files.getLabbookMcGillPath(configurationFilepath, "graphics/beamCurrent");
    basename = "GraphicBeamCurrentSU8230"
    figureFilepath = os.path.join(graphicPath, basename)
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

#    headers = ["Time (s)", 'Right after flash', '2h after flash', 'FE bombardment + 4:30h after flash',
#               '5:30h after flash']
    #Graphics.saveDataXY(figureFilepath, xA, yA, yB, yC, yD)
    #logging.info(figureFilepath)

def runAnalyzeFlashing():
    xA, yA = _get20120427Data()

    # inverse current sign
    yA *= -1

    # scale
    #yB -= 3.45

    plt.figure()

    plt.plot(xA, yA, label='Flash during use')

    plt.xlabel("Time (s)")
    plt.ylabel("Current (nA)")
    plt.legend(loc='best')

    xMax_s = 16*60.0*60.0
    xMin_s = xA[0]
    plt.xlim((xMin_s, xMax_s))

    ax2 = plt.gca().twiny()
    ax2.set_xlim((xMin_s/60.0/60.0, xMax_s/60.0/60.0))
    ax2.set_xlabel("Time (h)")

#    configurationFilepath = Files.getCurrentModulePath(__file__, "../../pyMcGill.cfg")
#    graphicPath = Files.getLabbookMcGillPath(configurationFilepath, "graphics/beamCurrent");
#    basename = "GraphicBeamCurrent"
#    figureFilepath = os.path.join(graphicPath, basename)
#    for extension in ['.pdf']:
#        plt.savefig(figureFilepath+extension)


def runAnalyzeFlashingTime():
    xA, yA = _get20121110Data()

    # inverse current sign
    yA *= -1

    # scale
    #yB -= 3.45

    plt.figure()

    plt.plot(xA, yA, label='Flash time of 12h')

    plt.xlabel("Time (s)")
    plt.ylabel("Current (nA)")
    plt.legend(loc='best')

    xMax_s = 20*60.0*60.0
    xMin_s = xA[0]
    plt.xlim((xMin_s, xMax_s))

    ax2 = plt.gca().twiny()
    ax2.set_xlim((xMin_s/60.0/60.0, xMax_s/60.0/60.0))
    ax2.set_xlabel("Time (h)")

    configurationFilepath = Files.getCurrentModulePath(__file__, "../../pyMcGillOld.cfg")
    graphicPath = Files.getLabbookMcGillPath(configurationFilepath, "graphics/beamCurrent");
    basename = "GraphicBeamCurrent_FlashTime12h"
    figureFilepath = os.path.join(graphicPath, basename)
    for extension in ['.pdf']:
        plt.savefig(figureFilepath+extension)

    xA, yA = _get20121111Data()

    # inverse current sign
    yA *= -1

    # scale
    #yB -= 3.45

    plt.figure()

    plt.plot(xA, yA, label='Flash time of 16h')

    plt.xlabel("Time (s)")
    plt.ylabel("Current (nA)")
    plt.legend(loc='best')

    xMax_s = 20*60.0*60.0
    xMin_s = xA[0]
    plt.xlim((xMin_s, xMax_s))

    ax2 = plt.gca().twiny()
    ax2.set_xlim((xMin_s/60.0/60.0, xMax_s/60.0/60.0))
    ax2.set_xlabel("Time (h)")

    configurationFilepath = Files.getCurrentModulePath(__file__, "../../pyMcGillOld.cfg")
    graphicPath = Files.getLabbookMcGillPath(configurationFilepath, "graphics/beamCurrent");
    basename = "GraphicBeamCurrent_FlashTime16h"
    figureFilepath = os.path.join(graphicPath, basename)
    for extension in ['.pdf']:
        plt.savefig(figureFilepath+extension)

def run():
    Graphics.setDefaultDisplay()

    #analyzeAllBeamCurrentMeasurement()

    runAnalyzeCurrent()
    #runAnalyzeFlashing()

    #runAnalyzeFlashingTime()

    plt.show()

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
