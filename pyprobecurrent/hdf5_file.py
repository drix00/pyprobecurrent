#!/usr/bin/env python
"""
.. py:currentmodule:: hdf5_file
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

HDF5 file for the probe current measurement.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Mar 2, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import logging

# Third party modules.
import numpy as np
import h5py

# Local modules.
import pyprobecurrent.nanopico.LogFile as LogFile

# Project modules

# Globals and constants variables.
GROUP_EXPERIMENT = "experiment"
GROUP_ANALYSIS = "analysis"

ATTRIBUTE_START_DATETIME = "Start time"

class HDF5File(object):
    def __init__(self, filepath, overwrite=False):
        self.filepath = filepath
        self._overwrite = overwrite

        with h5py.File(self.filepath, 'a') as hdf5File:
            exp_group = hdf5File.require_group(GROUP_EXPERIMENT)
            ana_group = hdf5File.require_group(GROUP_ANALYSIS)
            logging.info(exp_group.name)
            logging.info(ana_group.name)

    def getData(self, set_name, filepath):
        with h5py.File(self.filepath, 'a') as hdf5File:
            exp_group = hdf5File.require_group(GROUP_EXPERIMENT)

            if self._overwrite and set_name in exp_group:
                logging.warning("Removing dataset: %s", set_name)
                del exp_group[set_name]

            if set_name not in exp_group:
                logFile = LogFile.LogFile(filepath)
                logFile._read(filepath)
                start_time = logFile.start_time
                x = np.array(logFile.times_s)
                y = np.array(logFile.currents_nA)*(-1.0)

                assert len(x) == len(y)
                data = np.zeros((2, len(x)))
                data[0,] = x
                data[1,] = y

                dset = exp_group.require_dataset(set_name, data.shape, dtype='float32')
                dset[...] = data
                dset.attrs[ATTRIBUTE_START_DATETIME] = start_time
            else:
                data = exp_group[set_name]
                start_time = exp_group[set_name].attrs[ATTRIBUTE_START_DATETIME]
                logging.debug(data.shape)
                x = data[0,:]
                y = data[1,:]
        return x, y, start_time

def run():
    pass

if __name__ == '__main__':  #pragma: no cover
    run()