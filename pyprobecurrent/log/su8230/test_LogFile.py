#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.test_LogFile
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `LogFile`.
"""
from nose import SkipTest

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
from nose import SkipTest

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules
import pyprobecurrent.log.su8230.LogFile as LogFile

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

        self.filepathNotFull = Files.getCurrentModulePath(__file__, "../../../testData/su8230/log/Sem065.log")

        if not os.path.isfile(self.filepathNotFull):
            raise SkipTest

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

    def test_testFile(self):
        """
        Tests for method `readFile`.
        """

        self.assertTrue(os.path.isfile(self.filepathNotFull), self.filepathNotFull)

        filepathFull = Files.getCurrentModulePath(__file__, "../../../testData/su8230/log/Sem065.log")
        self.assertTrue(os.path.isfile(filepathFull), filepathFull)

        #self.fail("Test if the testcase is working.")

    def test_readFile(self):
        """
        Tests for method `readFile`.
        """
        raise SkipTest

        logFile = LogFile.LogFile()

        self.assertEqual("", logFile.date)
        self.assertEqual(0, logFile.numberLines)

        logFile.read(self.filepathNotFull)

        dateRef = datetime.date(2012, 4, 27)
        self.assertEqual(dateRef, logFile.date)
        self.assertEqual(1086, logFile.numberLines)

        #self.fail("Test if the testcase is working.")

    def test__extractDateFromLine(self):
        """
        Tests for method `_extractDateFromLine`.
        """
        raise SkipTest

        dateRef = datetime.date(2012, 4, 27)

        logFile = LogFile.LogFile()
        line = "Date 2012/04/27"
        date = logFile._extractDateFromLine(line)

        self.assertEqual(dateRef, date)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
