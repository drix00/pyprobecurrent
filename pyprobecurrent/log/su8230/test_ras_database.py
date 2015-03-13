#!/usr/bin/env python
"""
.. py:currentmodule:: test_ras_database
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `ras_database`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Jan 23, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import unittest
import logging
import os.path
import sqlite3

# Third party modules.
import pyodbc
#import pypyodbc

# Local modules.

# Project modules
#import pyprobecurrent.ras_database

# Globals and constants variables.

class Testras_database(unittest.TestCase):
    """
    TestCase class for the module `ras_database`.
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

    def test_open_database(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        filepath = os.path.normpath(os.path.join("../../../testdata/su8230", "Ras_20150130b.mdb"))
        filepath = r"D:\work\codings\hendrix_demersBitbucket\pyprobecurrent\testdata\su8230\Ras_20150130b.mdb"
        driver = 'DRIVER={Microsoft Access Driver (*.mdb)}; DBQ=%s' % filepath
        cnxn = pyodbc.connect(driver)
        #cnxn = pypyodbc.win_connect_mdb(filepath)
        cursor = cnxn.cursor()

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=ras_database")
    nose.runmodule(argv=argv)
