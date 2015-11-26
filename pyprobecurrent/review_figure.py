#!/usr/bin/env python
"""
.. py:currentmodule:: pyprobecurrent.log.su8230.review_figure
   :synopsis: Probe current figure for review paper

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Probe current figure for review paper.
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
import csv

# Third party modules.
import matplotlib.pyplot as plt
import numpy as np

# Local modules.

# Project modules
from pyprobecurrent.hdf5_file import HDF5File
from pyprobecurrent.log.su8230.exported_ras import getFlash, ETC_DATE, FlashParameters, ETC_PARAMETERS, read_emission, EMISSION_DATE, EMISSION_CURRENT

# Globals and constants variables.

graphic_path = r"D:\work\documents\articles\ModernSemReviewPaper\figures"

path_su8000 = r"D:\work\results\experiments\BeamCurrent\SU8000\20150122_201501"
hdf5_file_su8000 = HDF5File(os.path.join(path_su8000, "ProbeCurrentSU8000.hdf5"), overwrite=False)

path_su8230 = r"D:\work\results\experiments\BeamCurrent\SU8230"
hdf5_file_su8230 = HDF5File(os.path.join(path_su8230, "ProbeCurrentSu8230.hdf5"), overwrite=False)

def get_data_su8000_set01(timeWindow_s=60.0):
    min_max=(1.733*60.0*60.0, (12.0+1.733)*60.0*60.0)
    set_name = "set01"
    filename = "beamCurrent_SU8000_set01_20150122.txt"
    filepath_data = os.path.join(path_su8000, filename)

    x, y, startDateTime = hdf5_file_su8000.getData(set_name, filepath_data)
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

    x -= xmin
    x = x/60.0/60.0

    x = x[~mask_array.mask]
    y = y[~mask_array.mask]

    return x, y

def get_data_su8000_set02(timeWindow_s=60.0):
    min_max=(0.019*60.0*60.0, 12.019*60.0*60.0)
    set_name = "set02"
    filename = "beamCurrent_SU8000_set02_20150123.txt"
    filepath_data = os.path.join(path_su8000, filename)

    x, y, startDateTime = hdf5_file_su8000.getData(set_name, filepath_data)
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

    x -= xmin
    x = x/60.0/60.0

    x = x[~mask_array.mask]
    y = y[~mask_array.mask]

    return x, y

def get_data_su8230_set02(timeWindow_s=60.0):
    min_max=(0.16665*60.0*60.0, 12.0*60.0*60.0)
    set_name = "set02"
    filename = "BeamCurrent_SU8230_Set02_20150130.txt"

    filepath_data = os.path.join(path_su8230, filename)

    x, y, startDateTime = hdf5_file_su8230.getData(set_name, filepath_data)
    logging.debug(min(x))
    logging.debug(max(x))

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

    x = x/60.0/60.0

    x = x[~mask_array.mask]
    y = y[~mask_array.mask]

    return x, y

def analyze_su8000_set01():
    logging.info("analyze_set01")
    min_max=(1.733*60.0*60.0, (12.0+1.733)*60.0*60.0)
    set_name = "set01"
    filename = "beamCurrent_SU8000_set01_20150122.txt"

    _create_all_figures(min_max, set_name, filename)

def analyze_su8000_set02():
    logging.info("analyze_set02")
    min_max=(0.019*60.0*60.0, 12.019*60.0*60.0)
    set_name = "set02"
    filename = "beamCurrent_SU8000_set02_20150123.txt"

    _create_all_figures(min_max, set_name, filename)

def _create_all_figures(min_max, set_name, filename):
    _create_figure_su8000(set_name, filename, min_max=min_max, timeWindow_s=60.0)

def _create_figure_su8000(set_name, filename, log=False, min_max=None, timeWindow_s=None):
    logging.debug(filename)
    filepath_data = os.path.join(path_su8000, filename)

    x, y, startDateTime = hdf5_file_su8000.getData(set_name, filepath_data)
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

    x -= xmin
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
    ax_f.set_ylim(0.2, 1.0)

    figureFilepath = os.path.join(graphic_path, basename + "_IvsT")
    if timeWindow_s is not None:
        figureFilepath += "_tw%i" % (timeWindow_s)
    if log:
        figureFilepath += "_Log"
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    #plt.clf()
    #plt.close()

def analyze_su8230_set02():
    logging.info("analyze_set02")
    min_max=(0.16665*60.0*60.0, 12.0*60.0*60.0)
    _create_figure_su8230("set02", "BeamCurrent_SU8230_Set02_20150130.txt", min_max=min_max, timeWindow_s=60.0)

def _create_figure_su8230(set_name, filename, log=False, min_max=None, timeWindow_s=None):
    logging.debug(filename)
    filepath_data = os.path.join(path_su8230, filename)

    x, y, startDateTime = hdf5_file_su8230.getData(set_name, filepath_data)
    logging.debug(min(x))
    logging.debug(max(x))

    filename = "Ras_20150302_Etc.txt"
    filepath_etc = os.path.join(path_su8230, filename)
    flashData = getFlash(filepath_etc)

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

    minDateTime = startDateTime + datetime.timedelta(seconds=float(xmin))
    maxDateTime = startDateTime + datetime.timedelta(seconds=float(xmax))

    xEmissions_h = []
    emissionCurrents_uA = []

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
    ax_f.set_ylim(3.6, 4.4)

    figureFilepath = os.path.join(graphic_path, basename + "_IvsT")
    if timeWindow_s is not None:
        figureFilepath += "_tw%i" % (timeWindow_s)
    if log:
        figureFilepath += "_Log"
    for extension in ['.png', '.pdf']:
        plt.savefig(figureFilepath+extension)

    #plt.clf()
    #plt.close()

def figure_version1():
    plt.figure()

    x, y = get_data_su8000_set01()
    label = "SU8000 set 1"
    plt.plot(x, y, '.', label=label)

    x, y = get_data_su8000_set02()
    label = "SU8000 set 2"
    plt.plot(x, y, '.', label=label)

    x, y = get_data_su8230_set02()
    label = "SU8230 set 2"
    plt.plot(x, y, '.', label=label)

    plt.xlabel("Time (h)")
    plt.ylabel("Current (nA)")
    plt.ylim((0.4, 5.0))
    plt.legend(loc="center right")

    figureFilepath = os.path.join(graphic_path, "Figure3_version1.png")
    plt.savefig(figureFilepath)

def figure_version2():
    plt.figure()

    x, y = get_data_su8000_set01()
    y = y/max(y)
    label = "SU8000 set 1"
    plt.plot(x, y, '.', label=label)

    x, y = get_data_su8000_set02()
    y = y/max(y)
    label = "SU8000 set 2"
    plt.plot(x, y, '.', label=label)

    x, y = get_data_su8230_set02()
    y = y/max(y)
    label = "SU8230 set 2"
    plt.plot(x, y, '.', label=label)

    plt.xlabel("Time (h)")
    plt.ylabel(r"I/I$_{0}$")
    plt.ylim((0.4, 1.0))
    plt.legend(loc="center right")

    figureFilepath = os.path.join(graphic_path, "Figure3_version2.png")
    plt.savefig(figureFilepath)

def figure_version3():
    fig, ax1 = plt.subplots()

    lines = []
    labels = []

    x, y = get_data_su8000_set01()
    label = "SU8000 set 1"
    line = ax1.plot(x, y, '.', label=label)
    lines.append(line[0])
    labels.append(label)

    x, y = get_data_su8000_set02()
    label = "SU8000 set 2"
    line = ax1.plot(x, y, '.', label=label)
    lines.append(line[0])
    labels.append(label)

    ax2 = ax1.twinx()
    x, y = get_data_su8230_set02()
    label = "SU8230 set 2"
    line = ax2.plot(x, y, '.', color='r', label=label)
    lines.append(line[0])
    labels.append(label)

    ax1.set_xlabel("Time (h)")
    ax1.set_ylabel("Current (nA)")
    ax1.set_ylim(0.2, 1.0)

    ax2.set_ylabel("Current (nA)")
    ax2.set_ylim(3.6, 4.4)

    plt.figlegend(lines, labels, loc="upper center")

    figureFilepath = os.path.join(graphic_path, "Figure3_version3.png")
    plt.savefig(figureFilepath)


def export_data():
    x, y = get_data_su8000_set01()
    filepath = os.path.join(graphic_path, "SU8000_set1.csv")

    writer = csv.writer(open(filepath, 'w', newline='\n'))
    header_row = ["Time (h)", "Current (nA)"]
    writer.writerow(header_row)
    for row in zip(x, y):
        writer.writerow(row)

    x, y = get_data_su8000_set02()
    filepath = os.path.join(graphic_path, "SU8000_set2.csv")

    writer = csv.writer(open(filepath, 'w', newline='\n'))
    header_row = ["Time (h)", "Current (nA)"]
    writer.writerow(header_row)
    for row in zip(x, y):
        writer.writerow(row)

    x, y = get_data_su8230_set02()
    filepath = os.path.join(graphic_path, "SU8230_set2.csv")

    writer = csv.writer(open(filepath, 'w', newline='\n'))
    header_row = ["Time (h)", "Current (nA)"]
    writer.writerow(header_row)
    for row in zip(x, y):
        writer.writerow(row)

def run():
    analyze_su8000_set01()
    analyze_su8000_set02()
    analyze_su8230_set02()

    figure_version1()
    figure_version2()
    figure_version3()

    export_data()

    plt.show()

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.INFO)
    run()