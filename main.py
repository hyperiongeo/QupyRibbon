"""
"""
import sys

from PyQt5.QtWidgets import QApplication

from GUI.MainWindow import TestMainWindow

__author__ = 'mamj'


def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True)
    main_window = TestMainWindow()
    main_window.show()
    sys.exit(a.exec_())

main()
