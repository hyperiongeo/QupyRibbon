"""
text boxes
"""
from pyqtgraph.Qt.QtWidgets import QLineEdit

class RibbonTextbox(QLineEdit):
    def __init__(self, default_value, change_connector, max_width=50):
        super().__init__()
        self.setStyleSheet("border: 1px solid rgba(0,0,0,30%);")
        self.setText(default_value)
        self.setMaximumWidth(max_width)
        self.textChanged.connect(change_connector)
