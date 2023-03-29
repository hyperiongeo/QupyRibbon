"""
combo boxes
"""
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont

class RibbonCombobox(QComboBox):
    def __init__(self, default_value, change_connector, min_width=50, max_width=50, label=None, font_size=9):
        super().__init__()
        font = QFont()
        font.setPointSize(font_size)
        self.setFont(font)

        self.setStyleSheet("border: 1px solid rgba(0,0,0,30%);")
        self.setCurrentText(default_value)
        self.setMinimumWidth(min_width)
        # self.setMaximumWidth(max_width)
        if change_connector is not None:
            self.currentTextChanged.connect(change_connector)
