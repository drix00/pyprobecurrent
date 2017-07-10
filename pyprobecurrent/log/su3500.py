#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pyprobecurrent.log.su3500

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Analyze log for user SEM use.
"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import os.path
import logging

# Third party modules.

# Local modules.

# Project modules.
from pyprobecurrent.log.su8230.LogFiles import LogFiles

# Globals and constants variables.

def analyze_20170628():
    logs_path = r"D:\Dropbox\hdemers\professional\results\experiments\SU3500\logs\Hitachi_20170628\PC_SEM\Log"

    if os.path.isdir(logs_path):
        logging.info("Path exist: %s", logs_path)
        log_files = LogFiles(logs_path)
        log_files.findLogFiles()

        logging.info("Number of log files: %i", log_files.numberLogFiles)

        log_file = log_files.read_all_log_files()

        log_file.print_unique_item()

if __name__ == '__main__':  # pragma: no cover
    logging.getLogger().setLevel(logging.INFO)
    analyze_20170628()
