#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.nanopico.test_LogFile
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
import unittest
import logging
import os.path
import datetime

# Third party modules.

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules
import pyMcGill.experimental.NanoPico.LogFile as LogFile

# Globals and constants variables.

class TestLogFile(unittest.TestCase):
    """
    TestCase class for the module `LogFile`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self._dataPath = Files.getCurrentModulePath(__file__, "../../testData/nanopico")

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        #self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        filepath = os.path.join(self._dataPath, "testCurrent.txt")
        logFile = LogFile.LogFile(filepath)
        logFile._read(filepath)

        self.assertEqual(76, logFile.numberPoints)

        #self.fail("Test if the testcase is working.")

    def test__extractStartTime(self):
        """
        Tests for method `_extractStartTime`.
        """

        line = "Logging started at 3/27/2012 8:16:32 PM"
        dateTimeRef = datetime.datetime(2012, 3, 27, 20, 16, 32)

        logFile = LogFile.LogFile(None)
        startDateTime = logFile._extractStartTime(line)

        self.assertEqual(dateTimeRef, startDateTime)

        #self.fail("Test if the testcase is working.")

    def test_multipledays(self):
        """
        Tests for method `_extractStartTime`.
        """

        line = "Logging started at 3/27/2012 8:16:32 PM"

        logFile = LogFile.LogFile(None)
        logFile._readInit(line)

        # 3/27/2012
        line = "8:16:33 PM"
        currentDateTimeRef = 1.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/27/2012
        line = "11:59:59 PM"
        currentDateTimeRef = 27.0 + 43.0*60.0 + 3.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/28/2012
        line = "8:16:32 AM"
        currentDateTimeRef = 0.0 + 0.0*60.0 + 12.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/28/2012
        line = "8:16:33 AM"
        currentDateTimeRef = 1.0 + 0.0*60.0 + 12.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/28/2012
        line = "8:16:31 PM"
        currentDateTimeRef = 59.0 + 59.0*60.0 + 23.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/28/2012
        line = "8:16:32 PM"
        currentDateTimeRef = 0.0 + 0.0*60.0 + 24.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/28/2012
        line = "8:16:33 PM"
        currentDateTimeRef = 1.0 + 0.0*60.0 + 24.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/28/2012
        line = "8:16:31 PM"
        currentDateTimeRef = 59.0 + 59.0*60.0 + 47.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/28/2012
        line = "8:16:32 PM"
        currentDateTimeRef = 0.0 + 0.0*60.0 + 48.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        # 3/28/2012
        line = "8:16:33 PM"
        currentDateTimeRef = 1.0 + 0.0*60.0 + 48.0*60.0*60.0
        currentDateTime = logFile._extractDateTime(line)
        self.assertEqual(currentDateTimeRef, currentDateTime)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=pyMcGill.experimental.nanopico.LogFile")
    nose.runmodule(argv=argv)
