"""
main
"""
import sys

from PyQt6.QtWidgets import QApplication

from GUI.MainWindow import TestMainWindow

__author__ = 'mamj'


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    main_window = TestMainWindow()
    main_window.show()
    sys.exit(app.exec())

main()
