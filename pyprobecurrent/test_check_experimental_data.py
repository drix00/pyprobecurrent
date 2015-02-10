#!/usr/bin/env python
"""
.. py:currentmodule:: test_check_experimental_data
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `check_experimental_data`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Feb 9, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.

# Project modules
import pyprobecurrent.check_experimental_data

# Globals and constants variables.

class Testcheck_experimental_data(unittest.TestCase):
    """
    TestCase class for the module `pyprobecurrent.check_experimental_data`.
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
        self.assert_(True)

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=pyprobecurrent.check_experimental_data")
    nose.runmodule(argv=argv)
