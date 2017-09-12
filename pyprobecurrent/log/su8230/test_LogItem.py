#!/usr/bin/env python
"""
.. py:currentmodule:: experimental.su8000.log.test_LogItem
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `LogItem`.
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
import datetime

# Third party modules.
from nose import SkipTest

# Local modules.

# Project modules
import pyprobecurrent.log.su8230.LogItem as LogItem

# Globals and constants variables.

class TestLogItem(unittest.TestCase):
    """
    TestCase class for the module `LogItem`.
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

    def test__extractVext(self):
        """
        Tests for method `_extractVext`.
        """
        raise SkipTest

        line = r"2012/04/26,19:23:58,001562,SH->PC   ,(0106):1 ,Vext               ,00001054                                     "
        logItem = LogItem.LogItem(line)

        dateRef = datetime.date(2012, 4, 26)
        self.assertEqual(dateRef, logItem.date)

        timeRef = datetime.time(19, 23, 58)
        self.assertEqual(timeRef, logItem.time)

        intervRef = "001562"
        self.assertEqual(intervRef, logItem.interv)

        unitRef = "SH->PC"
        self.assertEqual(unitRef, logItem.unit)

        self.assertEqual(None, logItem.message)

        commandNumberRef = "(0106):1"
        self.assertEqual(commandNumberRef, logItem.commandNumber)
        commandRef = "Vext"
        self.assertEqual(commandRef, logItem.command)
        parameterRef = "00001054"
        self.assertEqual(parameterRef, logItem.parameter)

        #self.fail("Test if the testcase is working.")

    def test__extractEmissionDisp(self):
        """
        Tests for method `_extractEmissionDisp`.
        """
        raise SkipTest

        line = r"2012/04/26,19:23:58,000000,SH->PC   ,(0108):1 ,Emission(Disp)     ,0000012C                                     "
        logItem = LogItem.LogItem(line)

        dateRef = datetime.date(2012, 4, 26)
        self.assertEqual(dateRef, logItem.date)

        timeRef = datetime.time(19, 23, 58)
        self.assertEqual(timeRef, logItem.time)

        intervRef = "000000"
        self.assertEqual(intervRef, logItem.interv)

        unitRef = "SH->PC"
        self.assertEqual(unitRef, logItem.unit)

        self.assertEqual(None, logItem.message)

        commandNumberRef = "(0108):1"
        self.assertEqual(commandNumberRef, logItem.commandNumber)
        commandRef = "Emission(Disp)"
        self.assertEqual(commandRef, logItem.command)
        parameterRef = "0000012C"
        self.assertEqual(parameterRef, logItem.parameter)

        #self.fail("Test if the testcase is working.")


    def test__extractPCMessage(self):
        """
        Tests for method `_extractItemsFromLine` for PC Msg log item.
        """
        raise SkipTest
        line = r"2012/04/27,15:35:30,000031,PC Msg   ,          Wait Err(Event Now) 11"
        logItem = LogItem.LogItem(line)

        dateRef = datetime.date(2012, 4, 27)
        self.assertEqual(dateRef, logItem.date)

        timeRef = datetime.time(15, 35, 30)
        self.assertEqual(timeRef, logItem.time)

        intervRef = "000031"
        self.assertEqual(intervRef, logItem.interv)

        unitRef = "PC Msg"
        self.assertEqual(unitRef, logItem.unit)

        messageRef = "Wait Err(Event Now) 11"
        self.assertEqual(messageRef, logItem.message)

        self.assertEqual(None, logItem.commandNumber)
        self.assertEqual(None, logItem.command)
        self.assertEqual(None, logItem.parameter)

        line = r"2012/04/27,15:36:23,000250,PC->Log  ,          LogEnd"
        logItem = LogItem.LogItem(line)

        dateRef = datetime.date(2012, 4, 27)
        self.assertEqual(dateRef, logItem.date)

        timeRef = datetime.time(15, 36, 23)
        self.assertEqual(timeRef, logItem.time)

        intervRef = "000250"
        self.assertEqual(intervRef, logItem.interv)

        unitRef = "PC->Log"
        self.assertEqual(unitRef, logItem.unit)

        messageRef = "LogEnd"
        self.assertEqual(messageRef, logItem.message)

        self.assertEqual(None, logItem.commandNumber)
        self.assertEqual(None, logItem.command)
        self.assertEqual(None, logItem.parameter)

        #self.fail("Test if the testcase is working.")

    def test__extractCheckCode(self):
        """
        Tests for method `_extractItemsFromLine` for CheckCode log item.
        """
        raise SkipTest

        line = r"2012/04/27,15:35:14,000766,CheckCode,         ,GCheck Code = 1502 -> OK"
        logItem = LogItem.LogItem(line)

        dateRef = datetime.date(2012, 4, 27)
        self.assertEqual(dateRef, logItem.date)

        timeRef = datetime.time(15, 35, 14)
        self.assertEqual(timeRef, logItem.time)

        intervRef = "000766"
        self.assertEqual(intervRef, logItem.interv)

        unitRef = None
        self.assertEqual(unitRef, logItem.unit)

        messageRef = "GCheck Code = 1502 -> OK"
        self.assertEqual(messageRef, logItem.message)

        self.assertEqual(None, logItem.commandNumber)
        commandRef = "CheckCode"
        self.assertEqual(commandRef, logItem.command)
        self.assertEqual(None, logItem.parameter)

        #self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
