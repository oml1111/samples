from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

application = QApplication([])
window = uic.loadUi("qt_designer.ui")
window.show()
application.exec()