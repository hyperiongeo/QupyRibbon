"""
main windows
"""
import sys
from qtpy.QtCore import Qt
from qtpy.QtGui import QKeySequence as QKSec, QAction
from qtpy.QtWidgets import (QApplication, QMainWindow, QDockWidget, QMessageBox, QLabel)

from RibbonButton import RibbonButton
from Icons import get_icon
from RibbonTextbox import RibbonTextbox
from RibbonCombobox import RibbonCombobox
from RibbonWidget import RibbonWidget, RibbonTabBar

__author__ = 'cdh'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.resize(1280, 800)
        self.setWindowTitle("Main Window")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))
        self._main_dock_widget = QDockWidget(self)
        self._main_dock_widget.setObjectName("MainDock")
        self._main_dock_widget.setWindowTitle("Main dock")
        self.addDockWidget(Qt.LeftDockWidgetArea, self._main_dock_widget)
        self.centralWidget()

        # -------------      actions       -----------------

        self._open_action = self.add_action("Open", "open", "Open file", True, self.on_open_file, QKSec.Open)
        self._save_action = self.add_action("Save", "save", "Save file", True, self.on_save, QKSec.Save)
        self._copy_action = self.add_action("Copy", "copy", "Copy selection", True, self.on_copy, QKSec.Copy)
        self._paste_action = self.add_action("Paste", "paste", "Paste from clipboard", True, self.on_paste, QKSec.Paste)
        self._zoom_action = self.add_action("Zoom", "zoom", "Zoom in on document", True, self.on_zoom)
        self._about_action = self.add_action("About", "about", "About QupyRibbon", True, self.on_about)
        self._license_action = self.add_action("License", "license", "Licence for this software", True, self.on_license)

        # -------------      textboxes       -----------------

        self._text_box1 = RibbonTextbox("Text 1", self.on_text_box1_changed, 80)
        self._text_box2 = RibbonTextbox("Text 2", self.on_text_box1_changed, 80)
        self._text_box3 = RibbonTextbox("Text 3", self.on_text_box1_changed, 80)
        self._combo_box4 = RibbonCombobox("", self.on_text_box1_changed, 80)
        self._combo_box4.addItem("DJvnjnvfsjnv")
        self._combo_box4.addItem("jouyufvhkjft")

        # Ribbon

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()

        self.show()

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def init_ribbon(self):
        home_tab = self._ribbon.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._open_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._save_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        edit_panel.add_ribbon_widget(RibbonButton(self, self._copy_action, True))
        edit_panel.add_ribbon_widget(RibbonButton(self, self._paste_action, True))
        grid = edit_panel.add_grid_widget(200)
        grid.addWidget(QLabel("Text box 1"), 1, 1)
        grid.addWidget(QLabel("Text box 2"), 2, 1)
        grid.addWidget(QLabel("Text box 3"), 3,1)
        grid.addWidget(QLabel("Combo box 4"), 4, 1)
        grid.addWidget(self._text_box1, 1, 2)
        grid.addWidget(self._text_box2, 2, 2)
        grid.addWidget(self._text_box3, 3, 2)
        grid.addWidget(self._combo_box4, 4, 2)

        view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        home_tab.add_spacer()

        about_tab = self._ribbon.add_ribbon_tab("About")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

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


if __name__ == '__main__':
    # version = utils.Version()
    # version.load(Config().bundle_dir)
    # # info, version, date1 = utils.version_handling(Config().bundle_dir, json=True)

    # # QgsApplication.setPrefixPath(os.environ.get("QGIS_PREFIX_PATH", r"C:\Program Files\QGIS 3.14\apps\qgis"), True)
    # # QgsApplication.setPrefixPath(os.environ.get("QGIS_PREFIX_PATH", r"C:\Users\hooge\miniconda3\envs\qgis"), True)

    # curr_date = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
    # log_file = os.path.join(os.environ['TEMP'], 'Prospector log file ' + curr_date + '.txt')
    # logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.INFO)
    # logging.info("Welcome to Hyperion Software's Prospector Seismic Interpretation Package")

    app = QApplication([])

    main_window = MainWindow()
    # main_window.show()

    # Start the main messageloop
    sys.exit(app.exec())


