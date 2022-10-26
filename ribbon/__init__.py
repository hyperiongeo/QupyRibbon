"""
"""
from pyqtgraph.Qt.QtWidgets import (QApplication)

__author__ = 'mamj'


def gui_scale():
    screen = QApplication.screens()[0];
    dpi = screen.logicalDotsPerInch()
    return dpi / 96
