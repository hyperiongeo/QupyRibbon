"""
widget
"""
from qtpy.QtCore import (Qt)
from qtpy.QtWidgets import (QWidget, QTabWidget, QToolBar, QFrame, QHBoxLayout, QCheckBox, QLabel)
from qtpy.QtGui import QFont

from .RibbonTab import RibbonTab
from . import gui_scale
from .StyleSheets import get_stylesheet

__author__ = 'magnus'


class RibbonWidget(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(9)
        self.setFont(font)

        self.setStyleSheet(get_stylesheet("ribbon"))
        self.setObjectName("ribbonWidget")
        self.setWindowTitle("Ribbon")
        self._ribbon_widget = QTabWidget(self)
        self._ribbon_widget.setMaximumHeight(int(120*gui_scale()))
        self._ribbon_widget.setMinimumHeight(int(110*gui_scale()))
        self._ribbon_widget.setFont(font)
        self.setMovable(False)

        self.addWidget(self._ribbon_widget)

        # self._ribbon_widget.setCornerWidget(frame, Qt.Corner.TopRightCorner)

    def add_ribbon_tab(self, name):
        ribbon_tab = RibbonTab(self, name)
        ribbon_tab.setObjectName("tab_" + name)
        self._ribbon_widget.addTab(ribbon_tab, name)
        return ribbon_tab

    def set_active(self, name):
        self._ribbon_widget.setCurrentWidget(self._ribbon_widget.findChild(QWidget, "tab_" + name))

class RibbonTabBar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet(get_stylesheet("ribbon"))
        self.setObjectName("rightWidget")
        self.setWindowTitle("Right")
        self.setMovable(False)

        self._frame = QFrame()
        self._frame_layout = QHBoxLayout()
        self._frame_layout.addWidget(QCheckBox())
        # self._ribbon_widget.setMaximumHeight(int(120*gui_scale()))
        # self._ribbon_widget.setMinimumHeight(int(110*gui_scale()))
        # self.addWidget(self._frame)
        self.addWidget(QCheckBox())
