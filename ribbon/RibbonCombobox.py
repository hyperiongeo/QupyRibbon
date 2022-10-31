"""
combo boxes
"""
from pyqtgraph.Qt.QtWidgets import QComboBox
from pyqtgraph.Qt.QtGui import QFont

class RibbonCombobox(QComboBox):
    def __init__(self, default_value, change_connector, max_width=50, label=None):
        super().__init__()
        font = QFont()
        font.setPointSize(9)
        self.setFont(font)

        self.setStyleSheet("border: 1px solid rgba(0,0,0,30%);")
        self.setCurrentText(default_value)
        self.setMaximumWidth(max_width)
        if change_connector is not None:
            self.currentTextChanged.connect(change_connector)
