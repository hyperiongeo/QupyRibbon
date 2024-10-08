"""
buttons
"""

from qtpy.QtCore import QSize, Qt
from qtpy.QtGui import QFont, QAction
from qtpy.QtWidgets import (QToolButton)

from . import gui_scale
from .StyleSheets import get_stylesheet

__author__ = 'magnus'


class RibbonButton(QToolButton):
    def __init__(self, owner, action, is_large, menu=None):
        super().__init__(owner)

        font = QFont()
        font.setPointSize(9)
        self.setFont(font)

        scale = gui_scale()

        if isinstance(action, QAction):
            name = action.text().replace("&", "").replace("\n", "_").replace(" ", "_").lower()
            name = "rbtn_"+action.statusTip().replace("...", "").replace(" ", "_").lower()

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
            self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.setMaximumWidth(int(120 * scale))
            self.setIconSize(QSize(int(16 * scale), int(16 * scale)))
            self.setStyleSheet(get_stylesheet("ribbonSmallButton"))

        if menu is not None:
            self.setMenu(menu)
            self.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)


    def update_button_status_from_action(self):
       if isinstance(self._action_owner, QAction):
            self.setText(self._action_owner.text())
            self.setStatusTip(self._action_owner.statusTip())
            self.setToolTip(self._action_owner.toolTip())
            self.setIcon(self._action_owner.icon())
            self.setEnabled(self._action_owner.isEnabled())
            self.setCheckable(self._action_owner.isCheckable())
            self.setChecked(self._action_owner.isChecked())

class RibbonMenuButton(QToolButton):
    def __init__(self, owner, menu, is_large):
        super().__init__(owner)

        font = QFont()
        font.setPointSize(9)
        self.setFont(font)

        scale = gui_scale()

        # self._action_owner = action
        # self.update_button_status_from_action()
        # self.clicked.connect(self._action_owner.trigger)
        # self._action_owner.changed.connect(self.update_button_status_from_action)

        if is_large:
            self.setMaximumWidth(int(80 * scale))
            self.setMinimumWidth(int(50 * scale))
            self.setMinimumHeight(int(75 * scale))
            self.setMaximumHeight(int(80 * scale))
            self.setStyleSheet(get_stylesheet("ribbonButton"))
            self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
            self.setIconSize(QSize(int(32 * scale), int(32 * scale)))
        else:
            self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.setMaximumWidth(int(120 * scale))
            self.setIconSize(QSize(int(16 * scale), int(16 * scale)))
            self.setStyleSheet(get_stylesheet("ribbonSmallButton"))

        if menu is not None:
            self.setMenu(menu)
            self.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)


    def update_button_status_from_action(self):
        self.setText(self._action_owner.text())
        self.setStatusTip(self._action_owner.statusTip())
        self.setToolTip(self._action_owner.toolTip())
        self.setIcon(self._action_owner.icon())
        self.setEnabled(self._action_owner.isEnabled())
        self.setCheckable(self._action_owner.isCheckable())
        self.setChecked(self._action_owner.isChecked())
