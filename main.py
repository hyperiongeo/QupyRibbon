"""
main
"""
import sys

from pyqtgraph.Qt.QtWidgets  import (QApplication)

from ribbon.MainWindow import TestMainWindow

__author__ = 'mamj'

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    main_window = TestMainWindow()
    main_window.show()
    sys.exit(app.exec())

main()
