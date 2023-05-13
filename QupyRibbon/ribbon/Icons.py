"""
icons
"""
import sys
import os
from PyQt5.QtGui import QIcon, QPixmap

__author__ = 'magnus'
__maintainer__ = "Corey Hooge"

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_icon(name):
    icons_instance = Icons()
    return icons_instance.icon(name)


class Icons:
    def __init__(self):
        self._icons = {}
        self.make_icon("", "icons/under-construction.png")
        self.make_icon("default", "icons/under-construction.png")
        self.make_icon("under_construction", "icons/under-construction.png")
       
        self.make_icon("folder", "icons/open-folder.png")
        self.make_icon("open", "icons/open-folder.png")
        self.make_icon("save", "icons/data-storage.png")
        self.make_icon("exit", "icons/exit.png")
        self.make_icon("paste", "icons/paste.png")
        self.make_icon("zoom", "icons/zoom.png")
        self.make_icon("zoom_in", "icons/zoom_in.png")
        self.make_icon("zoom_out", "icons/zoom_out.png")
        self.make_icon("hand-cursor", "icons/icons8-hand-cursor-50.png")
        self.make_icon("copy", "icons/copy.png")
        self.make_icon("about", "icons/about.png")
        self.make_icon("help", "icons/help.png")
        self.make_icon("license", "icons/license.png")
        self.make_icon("create", "icons/project.png")

        self.make_icon("excel", "icons/excel.png")
        self.make_icon("csv", "icons/csv.png")
        self.make_icon("tif", "icons/icons8-tif-64.png")
        self.make_icon("json", "icons/icons8-json-80.png")

        self.make_icon("database", "icons/database.png")
        self.make_icon("row", "icons/row.png")
        self.make_icon("column", "icons/column.png")

        self.make_icon("map", "icons/map.png")
        self.make_icon("seismic", "icons/seismic.png")
        self.make_icon("wells", "icons/well.png")
        self.make_icon("las", "icons/icons8-well-100.png")
        self.make_icon("raster", "icons/icons8-raster-graphics-60.png")
        self.make_icon("vector", "icons/icons8-pen-64.png")

        self.make_icon("show", "icons/under-construction.png")
        self.make_icon("import", "icons/under-construction.png")
        self.make_icon("add_fault", "icons/layers.png")
        self.make_icon("import wells", "icons/well.png")
        self.make_icon("project", "icons/project.png")
        self.make_icon("delete", "icons/icons8-delete-document-100.png")

        self.make_icon("style", "icons/style.png")
        self.make_icon("style_add", "icons/style_add.png")
        self.make_icon("add", "icons/add.png")
        self.make_icon("save_as", "icons/icons8-save-as-48.png")

        self.make_icon("radio", "icons/radio-waves.png")
        self.make_icon("bezier", "icons/bezier-tool.png")
        self.make_icon("well", "icons/well.png")
        self.make_icon("water-well", "icons/water-well.png")

        self.make_icon("drilling-rig", "icons/icons8-drilling-rig-68.png")
        self.make_icon("scatter", "icons/scatter.png")
        self.make_icon("scatter-plot", "icons/scatter-plot.png")
        self.make_icon("settings", "icons/settings.png")
        self.make_icon("las", "icons/line-graph_vert.png")
        self.make_icon("sgy", "icons/segy.png")

        self.make_icon("create", "icons/icons8-create-100.png")
        self.make_icon("grid", "icons/grid.png")
        self.make_icon("table", "icons/table.png")
        self.make_icon("raster", "icons/raster-graphics.png")
        self.make_icon("vector", "icons/vectors.png")
        self.make_icon("rename", "icons/rename.png")
        
        self.make_icon("preferences", "icons/48px-Preferences-system.svg.png")
        self.make_icon("arrow", "icons/arrow.png")
        self.make_icon("icon", "icons/icon.png")
        self.make_icon("merge", "icons/consolidate.png")
        self.make_icon("compile", "icons/compile.png")
        self.make_icon("zone", "icons/zone.png")
        self.make_icon("coding", "icons/coding.png")
        


    def make_icon(self, name, path):
        path = os.path.join(bundle_dir, path)
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

    def get_icon(self, name):
        return self.icon(name)
