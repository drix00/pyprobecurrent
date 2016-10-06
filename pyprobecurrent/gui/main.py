#!/usr/bin/env python
"""
.. py:currentmodule:: pyprobecurrent.gui.main
   :synopsis: Main GUI Tkinter application for probe current.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Main GUI Tkinter application for probe current.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Sep 23, 2016"
__copyright__ = "Copyright (c) 2016 Hendrix Demers"
__license__ = "Apache License Version 2.0"

# Standard library modules.
import tkinter as tk

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid()

if __name__ == '__main__': #pragma: no cover
    app = Application()
    app.master.title("Probe Current")
    app.mainloop()
