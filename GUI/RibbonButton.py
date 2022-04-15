"""
buttons
"""
# from PyQt5 import Qt
from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import (QToolButton)

from GUI import gui_scale
from GUI.StyleSheets import get_stylesheet

__author__ = 'magnus'


class RibbonButton(QToolButton):
    def __init__(self, owner, action, is_large):
        super().__init__(owner)

        scale = gui_scale()
        self._action_owner = action
        self.update_button_status_from_action()
        self.clicked.connect(self._action_owner.trigger)
        self._action_owner.changed.connect(self.update_button_status_from_action)

        if is_large:
            self.setMaximumWidth(int(80 * scale))
            self.setMinimumWidth(int(50 * scale))
            self.setMinimumHeight(int(75 * scale))
            self.setMaximumHeight(int(80 * scale))
            self.setStyleSheet(get_stylesheet("ribbonButton"))
            self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
            self.setIconSize(QSize(int(32 * scale), int(32 * scale)))
        else:
            self.setToolButtonStyle(2)
            self.setMaximumWidth(120 * scale)
            self.setIconSize(QSize(16 * scale, 16 * scale))
            self.setStyleSheet(get_stylesheet("ribbonSmallButton"))

    def update_button_status_from_action(self):
        self.setText(self._action_owner.text())
        self.setStatusTip(self._action_owner.statusTip())
        self.setToolTip(self._action_owner.toolTip())
        self.setIcon(self._action_owner.icon())
        self.setEnabled(self._action_owner.isEnabled())
        self.setCheckable(self._action_owner.isCheckable())
        self.setChecked(self._action_owner.isChecked())
