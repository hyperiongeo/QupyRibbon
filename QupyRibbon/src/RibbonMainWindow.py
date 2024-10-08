"""
main windows
"""
from qtpy.QtCore import Qt
from qtpy.QtGui import QKeySequence as QKSec
from qtpy.QtWidgets import (QMainWindow, QDockWidget, QMessageBox, QLabel, QAction)

from .RibbonButton import RibbonButton, RibbonMenuButton
from .Icons import get_icon
# from .RibbonTextbox import RibbonTextbox
from .RibbonCombobox import RibbonCombobox
from .RibbonWidget import RibbonWidget, RibbonTabBar

__author__ = 'cdh'


class RibbonWindow(QMainWindow):
    def __init__(self, parent, title=""):
        super().__init__(parent)
        # self.resize(1280, 800)
        self.default_window_title = title
        self.setWindowTitle(self.default_window_title)

        self.centralWidget()

        # Ribbon

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)

        # self.init_ribbon()

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def add_ribbon_button(self, action, is_large=True):
        name = "rbtn_"+action.statusTip().replace("...", "").replace(" ", "_").lower()
        setattr(self, name, RibbonButton(self, action, is_large))

        return getattr(self, name)

    def add_ribbon_combobox(self, default, change_connector, min_width=200, label="X"):
        name = "rcb_"+label.replace("...", "").replace(" ", "_").lower()
        btn = RibbonCombobox(default, change_connector=change_connector, min_width=min_width, label=label)
        setattr(self, name, btn)
        # print("__creatint combo:", name)
        return getattr(self, name)

class RibbonMainWindow(QMainWindow):
    def __init__(self, parent=None, dock=False, title="Prospector"):
        super().__init__(parent)
        self.resize(1280, 800)
        self.default_window_title = title
        self.setWindowTitle(self.default_window_title)
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))
        if dock:
            self._main_dock_widget = QDockWidget(self)
            self._main_dock_widget.setObjectName("MainDock")
            self._main_dock_widget.setWindowTitle("Main dock")
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self._main_dock_widget)
        else:
            pass
        self.centralWidget()

        # Ribbon

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)

        # self.init_ribbon()

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    # def add_ribbon_button(self, action, is_large=True):
    #     return RibbonButton(self, action, is_large)
    def add_ribbon_button(self, action, is_large=True):
        name = "rbtn_"+action.statusTip().replace("...", "").replace(" ", "_").lower()
        setattr(self, name, RibbonButton(self, action, is_large))
        # print("__creatint button:", name)
        return getattr(self, name)

    def add_ribbon_combobox(self, default, change_connector, min_width=200, label="X"):
        name = "rcb_"+label.replace("...", "").replace(" ", "_").lower()
        btn = RibbonCombobox(default, change_connector=change_connector, min_width=min_width, label=label)
        setattr(self, name, btn)
        # print("__creatint combo:", name)
        return getattr(self, name)

    def init_ribbon(self):
        self.create_actions()
        home_tab = self._ribbon.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._open_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._save_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._create_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        edit_panel.add_ribbon_widget(RibbonButton(self, self._paste_action, True))
        grid = edit_panel.add_grid_widget(200)
        grid.addWidget(QLabel("Text box 1"), 1, 1)
        grid.addWidget(QLabel("Text box 2"), 2, 1)
        grid.addWidget(QLabel("Text box 3"), 3, 1)
        grid.addWidget(self._text_box1, 1, 2)
        grid.addWidget(self._text_box2, 2, 2)
        grid.addWidget(self._text_box3, 3, 2)

        view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        home_tab.add_spacer()

        about_tab = self._ribbon.add_ribbon_tab("About")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, False))

    def create_actions(self):
        pass

    def closeEvent(self, close_event):
        pass

    def on_open_file(self):
        pass

    def on_save_to_excel(self):
        pass

    def on_save(self):
        pass

    def on_text_box1_changed(self):
        pass

    def on_text_box2_changed(self):
        pass

    def on_text_box3_changed(self):
        pass

    def on_copy(self):
        pass

    def on_paste(self):
        pass

    def on_zoom(self):
        pass

    def on_about(self):
        text = "QupyRibbon\n"
        text += "This program was made by Magnus Jørgensen.\n"
        text += "Copyright © 2016 Magnus Jørgensen"
        QMessageBox().about(self, "About QupyRibbon", text)

    def on_license(self):
        with open('LICENSE', 'r', encoding='utf-8') as open_file:
            lic = open_file.read()
        QMessageBox().information(self, "License", lic)
