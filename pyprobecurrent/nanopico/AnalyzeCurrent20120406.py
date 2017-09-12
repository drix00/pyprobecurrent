#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.nanopico.AnalyzeCurrent20120406
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

description
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path

# Third party modules.
import matplotlib.pyplot as plt

# Local modules.

# Project modules
import pyMcGill.experimental.NanoPico.LogFile as LogFile
from pyprobecurrent import get_current_module_path, getResultsMcGillPath

# Globals and constants variables.

def runAnalyzeCurrent20120406():
    configurationFilepath = get_current_module_path(__file__, "../../pyMcGill.cfg")
    dataPath = getResultsMcGillPath(configurationFilepath, r"experimental\McGill\su8000\hdemers\20120406\current")
    filenames = ["20120406_4keV_30uA_H.txt", "20120406_4keV_30uA_N.txt"]

    for filename in filenames:
        filepath = os.path.join(dataPath, filename)
        logFile = LogFile.LogFile(filepath)
        logFile._read(filepath)

        plt.figure()
        basename, _extension = os.path.splitext(filename)
        plt.title(basename)

        x = logFile.times_s
        y = logFile.currents_nA
        plt.plot(x, y)

        plt.xlabel("Time (s)")
        plt.ylabel("Current (nA)")

        figureFilepath = os.path.join(dataPath, basename)
        for extension in ['.png', '.pdf']:
            plt.savefig(figureFilepath+extension)

def run():
    runAnalyzeCurrent20120406()

    plt.show()


if __name__ == '__main__':  # pragma: no cover
    run()
