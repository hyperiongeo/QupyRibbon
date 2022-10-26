"""
main
"""
import sys

from pyqtgraph.Qt.QtWidgets  import (QApplication)

from ribbon.MainWindow import MainWindow, MainWindowwithRibbon

__author__ = 'mamj'

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    main_window = MainWindow()
    # main_window = MainWindowwithRibbon()
    main_window.show()
    sys.exit(app.exec())

main()
