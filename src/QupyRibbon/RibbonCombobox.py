"""
combo boxes
"""
from qtpy.QtWidgets import QComboBox
from qtpy.QtGui import QFont

class RibbonCombobox(QComboBox):
    def __init__(self, default_value, change_connector, min_width=50, max_width=50, label=None, font_size=9):
        super().__init__()
        font = QFont()
        font.setPointSize(font_size)
        self.setFont(font)

        # if label is not None:
        #     # name = label.replace("&", "").replace("\n", "_").replace(" ", "_").lower()
        #     name = "rcb_"+label.replace("...", "").replace(" ", "_").lower()
        #     self.setObjectName(name)

        self.setStyleSheet("border: 1px solid rgba(0,0,0,30%);")
        self.setCurrentText(default_value)
        self.setMinimumWidth(min_width)
        # self.setMaximumWidth(max_width)
        if change_connector is not None:
            self.currentTextChanged.connect(change_connector)
