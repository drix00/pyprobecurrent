#!/usr/bin/env python
"""
.. py:currentmodule:: log.su8230.test_exported_ras
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `exported_ras`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Mar 2, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import unittest
import logging
import os.path

# Third party modules.
from nose import SkipTest

# Local modules.
from pyHendrixDemersTools.Files import getCurrentModulePath

# Project modules
from pyprobecurrent.log.su8230.exported_ras import read_etc, getFlash, FlashParameters, read_emission, uniqueParameter
from pyprobecurrent.log.su8230.exported_ras import ETC_COMMAND, ETC_COMMAND_SEMON, ETC_COMMAND_SEMOFF, ETC_COMMAND_HVN, ETC_COMMAND_SEMOFF, ETC_COMMAND_FLSH
from pyprobecurrent.log.su8230.exported_ras import EMISSION_CURRENT, EMISSION_VEXT, EMISSION_IF, EMISSION_VS, EMISSION_VACC, EMISSION_VD

# Globals and constants variables.

class Testexported_ras(unittest.TestCase):
    """
    TestCase class for the module `exported_ras`.
    """

    def setUp(self):
        """
        Setup method.
        """

        path = getCurrentModulePath(__file__, "../../../testdata/su8230")
        filename = "Ras_20150302_Etc.txt"
        self._filepath = os.path.join(path, filename)
        if not os.path.isfile(self._filepath):
            raise SkipTest

        self._etcData = read_etc(self._filepath)

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

    def test_read_etc(self):
        """
        Tests for method `read_etc`.
        """
        path = getCurrentModulePath(__file__, "../../../testdata/su8230")
        filename = "Ras_20150302_Etc.txt"
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            raise SkipTest

        etcData = read_etc(filepath)

        self.assertEqual(1207, len(etcData))

        #self.fail("Test if the testcase is working.")

    def test_uniqueEtc(self):
        """
        Tests for method `uniqueEtc`.
        """

        commands = uniqueParameter(self._etcData, ETC_COMMAND)
        self.assertEqual(5, len(commands))
        self.assertIn(ETC_COMMAND_SEMON, commands)
        self.assertIn(ETC_COMMAND_SEMOFF, commands)
        self.assertIn(ETC_COMMAND_HVN, commands)
        self.assertIn(ETC_COMMAND_SEMOFF, commands)
        self.assertIn(ETC_COMMAND_FLSH, commands)

        #self.fail("Test if the testcase is working.")

    def test_getFlash(self):
        """
        Tests for method `getFlash`.
        """

        flashData = getFlash(self._filepath)
        self.assertEqual(821, len(flashData))

        #self.fail("Test if the testcase is working.")

    def test_FlashParameters(self):
        """
        Tests for method `FlashParameters`.
        """

        parametersStr = "1,204,0,0"
        flash_parameters = FlashParameters(parametersStr)
        self.assertEqual(1, flash_parameters.flashIntensity)
        self.assertAlmostEqual(204, flash_parameters.flashCode)
        self.assertAlmostEqual(0.0, flash_parameters.acceleratingVoltage_V)
        self.assertAlmostEqual(0.0, flash_parameters.emissionCurrent_uA)

        parametersStr = "1,3722,30000,11.7"
        flash_parameters = FlashParameters(parametersStr)
        self.assertEqual(1, flash_parameters.flashIntensity)
        self.assertAlmostEqual(3722, flash_parameters.flashCode)
        self.assertAlmostEqual(30000.0, flash_parameters.acceleratingVoltage_V)
        self.assertAlmostEqual(11.7, flash_parameters.emissionCurrent_uA)


        parametersStr = "2,200,0,20.7"
        flash_parameters = FlashParameters(parametersStr)
        self.assertEqual(2, flash_parameters.flashIntensity)
        self.assertAlmostEqual(200, flash_parameters.flashCode)
        self.assertAlmostEqual(0.0, flash_parameters.acceleratingVoltage_V)
        self.assertAlmostEqual(20.7, flash_parameters.emissionCurrent_uA)

        #self.fail("Test if the testcase is working.")

    def test_read_emission(self):
        """
        Tests for method `read_emission`.
        """

        path = getCurrentModulePath(__file__, "../../../testdata/su8230")
        filename = "Ras_20150302_Emission.txt"
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            raise SkipTest

        emissionData = read_emission(filepath)

        self.assertEqual(1537, len(emissionData))

        #self.fail("Test if the testcase is working.")

    def test_uniqueParameter(self):
        """
        Tests for method `uniqueEtcCommand`.
        """

        path = getCurrentModulePath(__file__, "../../../testdata/su8230")
        filename = "Ras_20150302_Emission.txt"
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            raise SkipTest
        emissionData = read_emission(filepath)

        parameters = uniqueParameter(emissionData, EMISSION_CURRENT)
        self.assertEqual(70, len(parameters))

        parameters = uniqueParameter(emissionData, EMISSION_VEXT)
        self.assertEqual(20, len(parameters))

        parameters = uniqueParameter(emissionData, EMISSION_IF)
        self.assertEqual(1, len(parameters))

        parameters = uniqueParameter(emissionData, EMISSION_VS)
        self.assertEqual(1, len(parameters))

        parameters = uniqueParameter(emissionData, EMISSION_VACC)
        self.assertEqual(28, len(parameters))

        parameters = uniqueParameter(emissionData, EMISSION_VD)
        self.assertEqual(13, len(parameters))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=pyprobecurrent.log.su8230.exported_ras")
    nose.runmodule(argv=argv)
