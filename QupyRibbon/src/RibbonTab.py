"""
tabs
"""

from qtpy.QtCore import Qt
from qtpy.QtWidgets import (QWidget, QHBoxLayout, QSpacerItem, QSizePolicy)
from qtpy.QtGui import QFont

from .RibbonPane import RibbonPane


class RibbonTab(QWidget):
    def __init__(self, parent, name):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(9)
        self.setFont(font)

        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def add_ribbon_pane(self, name):
        ribbon_pane = RibbonPane(self, name)
        self.layout().addWidget(ribbon_pane)
        return ribbon_pane

    def add_spacer(self):
        self.layout().addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.MinimumExpanding))
        self.layout().setStretch(self.layout().count() - 1, 1)
