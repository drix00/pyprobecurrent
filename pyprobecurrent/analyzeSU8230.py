#!/usr/bin/env python
"""
.. py:currentmodule:: analyzeSU8230
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Analyze probe current data from the SU-8230 SEM.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Mar 2, 2015"
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
path = r"D:\work\results\experiments\BeamCurrent\SU8230"
graphic_path = r"D:\work\documents\labbooks\e-labbook\graphics\beamCurrent"

hdf5_file = HDF5File(os.path.join(path, "ProbeCurrentSu8230.hdf5"), overwrite=False)

timeWindows_s = [60.0, 120.0, 300.0, 600.0]

def analyze_set01():
    logging.info("analyze_set01")
    min_max=(2.865*60.0*60.0, 11.8022*60.0*60.0)
    _create_figure_raw("set01", "BeamCurrent_SU8230_Set01_20150129.txt", min_max=min_max)
    for timeWindow_s in timeWindows_s:
        _create_figure_statistic("set01", "BeamCurrent_SU8230_Set01_20150129.txt", min_max=min_max, timeWindow_s=timeWindow_s)

def analyze_set02():
    logging.info("analyze_set02")
    min_max=(0.16665*60.0*60.0, 12.0*60.0*60.0)
    _create_figure_raw("set02", "BeamCurrent_SU8230_Set02_20150130.txt", min_max=min_max)
    for timeWindow_s in timeWindows_s:
        _create_figure_statistic("set02", "BeamCurrent_SU8230_Set02_20150130.txt", min_max=min_max, timeWindow_s=timeWindow_s)

def analyze_set03():
    logging.info("analyze_set03")
    min_max=(0.106678*60.0*60.0, 11.9362*60.0*60.0)
    _create_figure_raw("set03", "BeamCurrent_SU8230_Set03_20150202.txt", min_max=min_max)
    for timeWindow_s in timeWindows_s:
        _create_figure_statistic("set03", "BeamCurrent_SU8230_Set03_20150202.txt", min_max=min_max, timeWindow_s=timeWindow_s)

def analyze_set04():
    logging.info("analyze_set04")
    min_max=(0.113597*60.0*60.0, 12.0058*60.0*60.0)
    _create_figure_raw("set04", "BeamCurrent_SU8230_Set04_20150203.txt", min_max=min_max)
    for timeWindow_s in timeWindows_s:
        _create_figure_statistic("set04", "BeamCurrent_SU8230_Set04_20150203.txt", min_max=min_max, timeWindow_s=timeWindow_s)

def analyze_set05():
    logging.info("analyze_set05")
    min_max=(0.0805522*60.0*60.0, 12.0112*60.0*60.0)
    _create_figure_raw("set05", "BeamCurrent_SU8230_Set05_20150204.txt", min_max=min_max)
    for timeWindow_s in timeWindows_s:
        _create_figure_statistic("set05", "BeamCurrent_SU8230_Set05_20150204.txt", min_max=min_max, timeWindow_s=timeWindow_s)

def analyze_set06():
    logging.info("analyze_set06")
    min_max=(0.109995*60.0*60.0, 12.0092*60.0*60.0)
    _create_figure_raw("set06", "BeamCurrent_SU8230_Set06_20150206.txt", min_max=min_max)
    for timeWindow_s in timeWindows_s:
        _create_figure_statistic("set06", "BeamCurrent_SU8230_Set06_20150206.txt", min_max=min_max, timeWindow_s=timeWindow_s)

def analyze_set07():
    logging.info("analyze_set07")
    min_max=(0.19*60.0*60.0, 48.0*60.0*60.0)
    _create_figure_raw("set07", "BeamCurrent_SU8230_Set07_20150227.txt", min_max=min_max)
    for timeWindow_s in timeWindows_s:
        _create_figure_statistic("set07", "BeamCurrent_SU8230_Set07_20150227.txt", min_max=min_max, timeWindow_s=timeWindow_s)

def _create_figure_raw(set_name, filename, log=False, min_max=None):
    logging.debug(filename)
    filepath_data = os.path.join(path, filename)

    x, y, startDateTime = hdf5_file.getData(set_name, filepath_data)
    logging.debug(min(x))
    logging.debug(max(x))

    filename = "Ras_20150302_Emission.txt"
    filepath_emission = os.path.join(path, filename)
    emissionData = read_emission(filepath_emission)

    filename = "Ras_20150302_Etc.txt"
    filepath_etc = os.path.join(path, filename)
    flashData = getFlash(filepath_etc)
    startDateTime = datetime.datetime.strptime(startDateTime, "%Y-%m-%dT%H:%M:%S")

    if min_max is not None:
        xmin, xmax = min_max

        if xmin > xmax:
            xmin, xmax = xmax, xmin

        mask_array = np.ma.masked_outside(x, xmin, xmax)
    else:
        xmin = x[0]
        xmax = x[-1]

    minDateTime = startDateTime + datetime.timedelta(seconds=float(xmin))
    maxDateTime = startDateTime + datetime.timedelta(seconds=float(xmax))

    xEmissions_h = []
    emissionCurrents_uA = []
    for data in emissionData:
        dateStr = data[EMISSION_DATE]
        # 2015-2-18 12:49:07
        date = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")
        if date >= minDateTime and date <= maxDateTime:
            emissionCurrent_uA = float(data[EMISSION_CURRENT])*1.0e-1
            seconds = (date - startDateTime).total_seconds()
            hours = seconds/60.0/60.0
            xEmissions_h.append(hours)
            emissionCurrents_uA.append(emissionCurrent_uA)

    emissionCurrentEightyPercent_uA = emissionCurrents_uA[0] * 0.80

    basepath, _extension = os.path.splitext(filepath_data)
    basename = os.path.basename(basepath)

    x = x/60.0/60.0

    fig, ax_f = plt.subplots()
    ax_c = ax_f.twinx()
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

    ax_c.plot(xEmissions_h, emissionCurrents_uA, 'o-g')
    ax_c.set_ylabel(r"$I_{e}$ ($\mu$A)")
    ax_c.axhline(emissionCurrentEightyPercent_uA, color='red')

    for data in flashData:
        dateStr = data[ETC_DATE]
        # 2015-2-18 12:49:07
        date = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")

        if date >= minDateTime and date <= maxDateTime:
            logging.debug(date)
            seconds = (date - startDateTime).total_seconds()
            hours = seconds/60.0/60.0
            logging.debug(hours)

            flash_parameters = FlashParameters(data[ETC_PARAMETERS])
            flashIntensity = flash_parameters.flashIntensity
            if flashIntensity > 1:
                color = "red"
            else:
                color = "gray"

            plt.axvline(hours, color=color)

    ax_f.set_xlabel("Time (h)")
    ax_f.set_ylabel("Current (nA)")

    figureFilepath = os.path.join(graphic_path, basename + "_IvsT")
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

    filename = "Ras_20150302_Emission.txt"
    filepathEmission = os.path.join(path, filename)
    emissionData = read_emission(filepathEmission)

    filename = "Ras_20150302_Etc.txt"
    filepathFlash = os.path.join(path, filename)
    flashData = getFlash(filepathFlash)
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
    for data in emissionData:
        dateStr = data[EMISSION_DATE]
        # 2015-2-18 12:49:07
        date = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")
        if date >= minDateTime and date <= maxDateTime:
            emissionCurrent_uA = float(data[EMISSION_CURRENT])*1.0e-1
            seconds = (date - startDateTime).total_seconds()
            hours = seconds/60.0/60.0
            xEmissions_h.append(hours)
            emissionCurrents_uA.append(emissionCurrent_uA)

    emissionCurrentEightyPercent_uA = emissionCurrents_uA[0] * 0.80

    basepath, _extension = os.path.splitext(filepath)
    basename = os.path.basename(basepath)

    xMean = xMean/60.0/60.0

    # Mean with std errorbar.
    fig, ax_f = plt.subplots()
    ax_c = ax_f.twinx()
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

    ax_c.plot(xEmissions_h, emissionCurrents_uA, 'o-g')
    ax_c.set_ylabel(r"$I_{e}$ ($\mu$A)")
    ax_c.axhline(emissionCurrentEightyPercent_uA, color='red')

    for data in flashData:
        dateStr = data[ETC_DATE]
        # 2015-2-18 12:49:07
        date = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")

        if date >= minDateTime and date <= maxDateTime:
            logging.debug(date)
            seconds = (date - startDateTime).total_seconds()
            hours = seconds/60.0/60.0
            logging.debug(hours)

            flash_parameters = FlashParameters(data[ETC_PARAMETERS])
            flashIntensity = flash_parameters.flashIntensity
            if flashIntensity > 1:
                color = "red"
            else:
                color = "gray"

            plt.axvline(hours, color=color)

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

    ax_c.plot(xEmissions_h, emissionCurrents_uA, 'o-g')
    ax_c.set_ylabel(r"$I_{e}$ ($\mu$A)")
    ax_c.axhline(emissionCurrentEightyPercent_uA, color='red')

    for data in flashData:
        dateStr = data[ETC_DATE]
        # 2015-2-18 12:49:07
        date = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")

        if date >= minDateTime and date <= maxDateTime:
            logging.debug(date)
            seconds = (date - startDateTime).total_seconds()
            hours = seconds/60.0/60.0
            logging.debug(hours)

            flash_parameters = FlashParameters(data[ETC_PARAMETERS])
            flashIntensity = flash_parameters.flashIntensity
            if flashIntensity > 1:
                color = "red"
            else:
                color = "gray"

            plt.axvline(hours, color=color)

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

    ax_c.plot(xEmissions_h, emissionCurrents_uA, 'o-g')
    ax_c.set_ylabel(r"$I_{e}$ ($\mu$A)")
    ax_c.axhline(emissionCurrentEightyPercent_uA, color='red')

    for data in flashData:
        dateStr = data[ETC_DATE]
        # 2015-2-18 12:49:07
        date = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")

        if date >= minDateTime and date <= maxDateTime:
            logging.debug(date)
            seconds = (date - startDateTime).total_seconds()
            hours = seconds/60.0/60.0
            logging.debug(hours)

            flash_parameters = FlashParameters(data[ETC_PARAMETERS])
            flashIntensity = flash_parameters.flashIntensity
            if flashIntensity > 1:
                color = "red"
            else:
                color = "gray"

            plt.axvline(hours, color=color)

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

    ax_c.plot(xEmissions_h, emissionCurrents_uA, 'o-g')
    ax_c.set_ylabel(r"$I_{e}$ ($\mu$A)")
    ax_c.axhline(emissionCurrentEightyPercent_uA, color='red')

    for data in flashData:
        dateStr = data[ETC_DATE]
        # 2015-2-18 12:49:07
        date = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")

        if date >= minDateTime and date <= maxDateTime:
            logging.debug(date)
            seconds = (date - startDateTime).total_seconds()
            hours = seconds/60.0/60.0
            logging.debug(hours)

            flash_parameters = FlashParameters(data[ETC_PARAMETERS])
            flashIntensity = flash_parameters.flashIntensity
            if flashIntensity > 1:
                color = "red"
            else:
                color = "gray"

            plt.axvline(hours, color=color)

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
    analyze_set06()
    analyze_set07()

    plt.show()

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.INFO)
    run()