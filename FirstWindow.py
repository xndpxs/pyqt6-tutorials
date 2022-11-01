from PyQt6.QtWidgets import QApplication, QWidget
#needed for access to command line arguments
import sys

#if you need command line
app = QApplication(sys.argv)

window = QWidget()

window.show()

app.exec()