#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.test_LogFileOptions
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `LogFileOptions`.
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

# Third party modules.
from nose import SkipTest

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules
import pyprobecurrent.log.su8230.LogFileOptions as LogFileOptions

# Globals and constants variables.

class TestLogFileOptions(unittest.TestCase):
    """
    TestCase class for the module `LogFileOptions`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.filepath = Files.getCurrentModulePath(__file__, "../../../testData/su8230/log/SemLog.xml")

        if not os.path.isfile(self.filepath):
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

        self.assertTrue(os.path.isfile(self.filepath), self.filepath)

        #self.fail("Test if the testcase is working.")

    def test_readFile(self):
        """
        Tests for method `readFile`.
        """
        raise SkipTest

        logFileOptions = LogFileOptions.LogFileOptions()
        logFileOptions.read(self.filepath)

        self.assertEqual(True, logFileOptions.isLogging)
        self.assertEqual('F', logFileOptions.logMode)
        self.assertEqual("sem08.log", logFileOptions.nextFile)
        self.assertEqual(5000, logFileOptions.filesize)
        self.assertEqual(20, logFileOptions.fileCounts)
        self.assertEqual('0103', logFileOptions.version)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
