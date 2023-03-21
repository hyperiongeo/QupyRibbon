"""
main
"""
import sys

from pyqtgraph.Qt.QtWidgets  import (QApplication)

from ribbon.RibbonMainWindow import MainWindow #, RibbonMainWindow

__author__ = 'mamj'

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    main_window = MainWindow()
    # main_window = RibbonMainWindow()
    main_window.show()
    sys.exit(app.exec())

main()
