""""
fix icon profile issues
"""
import sys

from qtpy.QtGui import QImage, QColorSpace
from qtpy.QtWidgets import (QApplication)

#####################



app = QApplication(sys.argv)
# main_wnd = ViewerMainWindow()

# # Show the window
# main_wnd.show()

infile = "QupyRibbon/icons/zoom.png"
outfile = infile.replace(".png", "_fixed.png")

img = QImage(infile)
csp = QColorSpace.NamedColorSpace.SRgb
print(csp)
img.convertToColorSpace(QColorSpace(QColorSpace.NamedColorSpace.SRgb))
img.save(outfile)

# Start the main messageloop
# sys.exit(app.exec())
