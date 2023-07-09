"""
panes
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from PyQt6.QtGui import QFont, QPainter

from . import gui_scale
from .StyleSheets import get_stylesheet

__author__ = 'mamj'


class RibbonPane(QWidget):
    def __init__(self, parent, name):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(9)
        self.setFont(font)

        self.setStyleSheet(get_stylesheet("ribbonPane"))
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setSpacing(0)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(horizontal_layout)

        vertical_widget = QWidget(self)
        horizontal_layout.addWidget(vertical_widget)
        horizontal_layout.addWidget(RibbonSeparator(self))
        vertical_layout = QVBoxLayout()
        vertical_layout.setSpacing(0)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_widget.setLayout(vertical_layout)

        label = QLabel(name)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color:#666;")
        content_widget = QWidget(self)
        vertical_layout.addWidget(content_widget)
        vertical_layout.addWidget(label)
        content_layout = QHBoxLayout()
        content_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)
        self.contentLayout = content_layout
        content_widget.setLayout(content_layout)

    def add_ribbon_widget(self, widget):
        self.contentLayout.addWidget(widget, 0, Qt.AlignmentFlag.AlignTop)

    def add_grid_widget(self, width):
        widget = QWidget()
        widget.setMaximumWidth(width)
        grid_layout = QGridLayout()
        widget.setLayout(grid_layout)
        grid_layout.setSpacing(4)
        grid_layout.setContentsMargins(4, 4, 4, 4)
        self.contentLayout.addWidget(widget)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        return grid_layout


class RibbonSeparator(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMinimumHeight(int(gui_scale() * 80))
        self.setMaximumHeight(int(gui_scale() * 80))
        self.setMinimumWidth(1)
        self.setMaximumWidth(1)
        self.setLayout(QHBoxLayout())

    def paintEvent(self, event):
        pnt = QPainter()
        pnt.begin(self)
        pnt.fillRect(event.rect(), Qt.GlobalColor.lightGray)
        pnt.end()
