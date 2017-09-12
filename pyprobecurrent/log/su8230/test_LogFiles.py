#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.test_LogFiles
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests module LogFiles.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2014 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.

# Project modules
import pyprobecurrent.log.su8230.LogFiles as LogFiles

# Globals and constants variables.

class TestLogFiles(unittest.TestCase):
    """
    TestCase class for the module `LogFiles`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

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


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
