"""
icons
"""
import os
from pyqtgraph.Qt.QtGui import QIcon, QPixmap

__author__ = 'magnus'

# icons_instance = None

def get_icon(name):
    # global icons_instance
    # if not icons_instance:
    icons_instance = Icons()
    return icons_instance.icon(name)


class Icons(object):
    def __init__(self):
        self._icons = {}
        self.make_icon("", "icons/under-construction.png")
        self.make_icon("folder", "icons/open-folder.png")
        self.make_icon("open", "icons/open-folder.png")
        self.make_icon("save", "icons/data-storage.png")
        self.make_icon("icon", "icons/icon.png")
        self.make_icon("exit", "icons/exit.png")
        self.make_icon("paste", "icons/paste.png")
        self.make_icon("zoom", "icons/zoom.png")
        self.make_icon("zoom_in", "icons/zoom_in.png")
        self.make_icon("zoom_out", "icons/zoom_out.png")
        self.make_icon("copy", "icons/copy.png")
        self.make_icon("about", "icons/about.png")
        self.make_icon("license", "icons/license.png")
        self.make_icon("default", "icons/under-construction.png")
        self.make_icon("create", "icons/project.png")
        self.make_icon("under_construction", "icons/under-construction.png")
        self.make_icon("database", "icons/database.png")
        self.make_icon("map", "icons/map.png")
        self.make_icon("seismic", "icons/seismic.png")
        self.make_icon("wells", "icons/under-construction.png")

        self.make_icon("show", "icons/under-construction.png")
        self.make_icon("import", "icons/under-construction.png")
        self.make_icon("add_fault", "icons/under-construction.png")
        self.make_icon("import wells", "icons/under-construction.png")


    def make_icon(self, name, path):
        path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), path)
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Mode.Normal, QIcon.State.Off)
        self._icons[name] = icon

    def icon(self, name):
        icon = self._icons["default"]
        try:
            icon = self._icons[name]
        except KeyError:
            print("icon " + name + " not found")
        return icon
