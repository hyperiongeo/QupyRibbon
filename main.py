"""
main
"""
import sys

from PyQt6.QtWidgets  import (QApplication)

from src.RibbonMainWindow import RibbonMainWindow #, RibbonMainWindow

__author__ = 'mamj'

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    main_window = RibbonMainWindow()
    # main_window = RibbonMainWindow()
    main_window.show()
    sys.exit(app.exec())

main()
