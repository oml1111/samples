from PyQt5.QtWidgets import QApplication, QMainWindow

application = QApplication([])
application.setApplicationName("PyQt Empty Window")
window = QMainWindow()
window.resize(800, 600)
window.show()
application.exec()