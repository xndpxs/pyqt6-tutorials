import sys
from PyQt6.QtWidgets import QApplication, QMainWindow



app = QApplication(sys.argv)

window = QMainWindow()

window.statusBar().showMessage("Welcome to PyQt6 Course")

window.menuBar().addMenu("File")







window.show()
app.exec()