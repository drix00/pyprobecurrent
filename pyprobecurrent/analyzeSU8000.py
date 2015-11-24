#!/usr/bin/env python
"""
.. py:currentmodule:: pyprobecurrent.analyzeSU8000
   :synopsis: Analyze probe current data from the SU-8000 SEM

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Analyze probe current data from the SU-8000 SEM.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Nov 24, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import logging
import os.path
import datetime

# Third party modules.
import matplotlib.pyplot as plt
import numpy as np

# Local modules.

# Project modules
from pyprobecurrent.hdf5_file import HDF5File
from pyprobecurrent.log.su8230.exported_ras import getFlash, ETC_DATE, FlashParameters, ETC_PARAMETERS, read_emission, EMISSION_DATE, EMISSION_CURRENT

# Globals and constants variables.

path = r"D:\work\results\experiments\BeamCurrent\SU8000\20150122_201501"
graphic_path = r"D:\work\documents\labbooks\e-labbook\graphics\beamCurrent"

hdf5_file = HDF5File(os.path.join(path, "ProbeCurrentSU8000.hdf5"), overwrite=False)

timeWindows_s = [60.0, 120.0, 300.0, 600.0]

def analyze_set01():
    logging.info("analyze_set01")
    min_max=(1.733*60.0*60.0, 22.30*60.0*60.0)
    set_name = "set01"
    filename = "beamCurrent_SU8000_set01_20150122.txt"

    _create_all_figures(min_max, set_name, filename)

def analyze_set02():
    logging.info("analyze_set02")
    min_max=(0.019*60.0*60.0, 67.23*60.0*60.0)
    set_name = "set02"
    filename = "beamCurrent_SU8000_set02_20150123.txt"

    _create_all_figures(min_max, set_name, filename)

def analyze_set03():
    logging.info("analyze_set03")
    min_max=(3.03*60.0*60.0, 18.9713*60.0*60.0)
    set_name = "set03"
    filename = "BeamCurrent_SU8000_Set03_20150126.txt"

    _create_all_figures(min_max, set_name, filename)

def analyze_set04():
    logging.info("analyze_set04")
    min_max=(2.96521*60.0*60.0, 18.906*60.0*60.0)
    #min_max=None
    set_name = "set04"
    filename = "BeamCurrent_SU8000_Set04_20150127.txt"

    _create_all_figures(min_max, set_name, filename)

def analyze_set05():
    logging.info("analyze_set05")
    min_max=(3.215*60.0*60.0, 19.1589*60.0*60.0)
    #min_max=None
    set_name = "set05"
    filename = "BeamCurrent_SU8000_Set05_20150128.txt"

    _create_all_figures(min_max, set_name, filename)

def _create_all_figures(min_max, set_name, filename):
    _create_figure_raw(set_name, filename, min_max=min_max, timeWindow_s=60.0)
#     for timeWindow_s in timeWindows_s:
#         _create_figure_statistic(set_name, filename, min_max=min_max, timeWindow_s=timeWindow_s)


def _create_figure_raw(set_name, filename, log=False, min_max=None, timeWindow_s=None):
    logging.debug(filename)
    filepath_data = os.path.join(path, filename)

    x, y, startDateTime = hdf5_file.getData(set_name, filepath_data)
    logging.info(min(x))
    logging.info(max(x))

    if timeWindow_s is not None:
        numberArrays = len(x)//timeWindow_s + 1
        xMean = []
        yMean = []

        for xArray, yArray in zip(np.array_split(x, numberArrays), np.array_split(y, numberArrays)):
            xMean.append(np.median(xArray))
            yMean.append(np.mean(yArray))

        x = np.array(xMean)
        y = np.array(yMean)

    startDateTime = datetime.datetime.strptime(startDateTime, "%Y-%m-%dT%H:%M:%S")

    if min_max is not None:
        xmin, xmax = min_max

        if xmin > xmax:
            xmin, xmax = xmax, xmin

        mask_array = np.ma.masked_outside(x, xmin, xmax)
    else:
        xmin = x[0]
        xmax = x[-1]

    basepath, _extension = os.path.splitext(filepath_data)
    basename = os.path.basename(basepath)

    x = x/60.0/60.0

    fig, ax_f = plt.subplots()

    plt.title(basename)
    if log:
        if min_max is not None:
            ax_f.semilogy(x[mask_array.mask], y[mask_array.mask], '.')
        else:
            ax_f.semilogy(x, y, '.')
    else:
        if min_max is not None:
            ax_f.plot(x[~mask_array.mask], y[~mask_array.mask], '.')
        else:
            ax_f.plot(x, y, '.')

    ax_f.set_xlabel("Time (h)")
    ax_f.set_ylabel("Current (nA)")

    figureFilepath = os.path.join(graphic_path, basename + "_IvsT")
    if timeWindow_s is not None:
        figureFilepath += "_tw%i" % (timeWindow_s)
    if log:
        figureFilepath += "_Log"
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    plt.clf()
    plt.close()

def _create_figure_statistic(set_name, filename, min_max=None, timeWindow_s=60.0):
    logging.debug(filename)
    filepath = os.path.join(path, filename)

    x, y, startDateTime = hdf5_file.getData(set_name, filepath)
    logging.debug(min(x))
    logging.debug(max(x))

    numberArrays = len(x)//timeWindow_s + 1
    xMean = []
    yMean = []
    yStd = []
    yMin = []
    yMax = []
    yPtp = []
    for xArray, yArray in zip(np.array_split(x, numberArrays), np.array_split(y, numberArrays)):
        xMean.append(np.median(xArray))
        yMean.append(np.mean(yArray))
        yStd.append(np.std(yArray))
        yMin.append(np.min(yArray))
        yMax.append(np.max(yArray))
        yPtp.append(np.ptp(yArray))

    xMean = np.array(xMean)
    yMean = np.array(yMean)
    yStd = np.array(yStd)
    yMin = np.array(yMin)
    yMax = np.array(yMax)
    yPtp = np.array(yPtp)

    startDateTime = datetime.datetime.strptime(startDateTime, "%Y-%m-%dT%H:%M:%S")

    if min_max is not None:
        xmin, xmax = min_max

        if xmin > xmax:
            xmin, xmax = xmax, xmin

        mask_array = np.ma.masked_outside(xMean, xmin, xmax)
    else:
        xmin = xMean[0]
        xmax = xMean[-1]

    minDateTime = startDateTime + datetime.timedelta(seconds=float(xmin))
    maxDateTime = startDateTime + datetime.timedelta(seconds=float(xmax))

    xEmissions_h = []
    emissionCurrents_uA = []

    basepath, _extension = os.path.splitext(filepath)
    basename = os.path.basename(basepath)

    xMean = xMean/60.0/60.0

    # Mean with std errorbar.
    fig, ax_f = plt.subplots()

    plt.title(basename)

    if min_max is not None:
        #ax_f.plot(xMean[~mask_array.mask], yMean[~mask_array.mask], '.', label='mean')
        ax_f.errorbar(xMean[~mask_array.mask], yMean[~mask_array.mask], yerr=yStd[~mask_array.mask])
        #ax_f.plot(xMean[~mask_array.mask], yMin[~mask_array.mask], '-', label='min')
        #ax_f.plot(xMean[~mask_array.mask], yMax[~mask_array.mask], '-', label='max')
    else:
        #ax_f.plot(xMean, yMean, '.')
        ax_f.errorbar(xMean, yMean, yerr=yStd)
        #ax_f.plot(xMean, yMin, '-', label='min')
        #ax_f.plot(xMean, yMax, '-', label='max')

    ax_f.set_xlabel("Time (h)")
    ax_f.set_ylabel("Current (nA)")

    figureFilepath = os.path.join(graphic_path, basename + "_IvsT_tw%i" % (timeWindow_s))
    extension = '.png'
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    plt.clf()
    plt.close()

    # Std percentage.
    fig, ax_f = plt.subplots()
    ax_c = ax_f.twinx()
    plt.title(basename)

    if min_max is not None:
        ax_f.plot(xMean[~mask_array.mask], yStd[~mask_array.mask]/yMean[~mask_array.mask]*100.0, '.', label='mean')
    else:
        ax_f.plot(xMean, yStd/yMean*100.0, '.')

    ax_f.set_xlabel("Time (h)")
    ax_f.set_ylabel("Std (%)")

    figureFilepath = os.path.join(graphic_path, basename + "_IvsT_stdPercentage_tw%i" % (timeWindow_s))
    extension = '.png'
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    plt.clf()
    plt.close()

    # Min Max.
    fig, ax_f = plt.subplots()
    ax_c = ax_f.twinx()
    plt.title(basename)

    if min_max is not None:
        ax_f.plot(xMean[~mask_array.mask], yMin[~mask_array.mask], '-', label='min')
        ax_f.plot(xMean[~mask_array.mask], yMax[~mask_array.mask], '-', label='max')
    else:
        ax_f.plot(xMean, yMin, '-', label='min')
        ax_f.plot(xMean, yMax, '-', label='max')

    ax_f.set_xlabel("Time (h)")
    ax_f.set_ylabel("Current (nA)")

    plt.legend(loc='best')

    figureFilepath = os.path.join(graphic_path, basename + "_IvsT_minmax_tw%i" % (timeWindow_s))
    extension = '.png'
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    plt.clf()
    plt.close()

    # Ptp.
    fig, ax_f = plt.subplots()
    ax_c = ax_f.twinx()
    plt.title(basename)

    if min_max is not None:
        ax_f.plot(xMean[~mask_array.mask], yPtp[~mask_array.mask]/yMean[~mask_array.mask]*100.0, '.')
    else:
        ax_f.plot(xMean, yPtp/yMean*100.0, '.')

    ax_f.set_xlabel("Time (h)")
    ax_f.set_ylabel("Range of values (%)")

    figureFilepath = os.path.join(graphic_path, basename + "_IvsT_ptp_tw%i" % (timeWindow_s))
    extension = '.png'
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    plt.clf()
    plt.close()

def run():
    analyze_set01()
    analyze_set02()
    analyze_set03()
    analyze_set04()
    analyze_set05()

    plt.show()

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.INFO)
    run()