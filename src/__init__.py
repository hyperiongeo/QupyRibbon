"""
"""
from PyQt6.QtWidgets import (QApplication)

__author__ = 'mamj'

#from . import Icons, RibbonButton, RibbonCombobox, RibbonMainWindow, RibbonPane, RibbonTab, RibbonTextbox, RibbonWidget, StyleSheets

def gui_scale():
    screen = QApplication.screens()[0];
    dpi = screen.logicalDotsPerInch()
    return dpi / 96
