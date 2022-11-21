import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
                        # x,y,width,height
        # self.setGeometry(1920,0,400,400)
        self.setWindowTitle("PyQt6 QLineEdit")
        self.setWindowIcon(QIcon("../images/pyqt.png"))
        self.setFixedSize(400,400)

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Arial", 16))
        # Default normal text
        # line_edit.setText("Default Text")
        # gray words asking for completion
        # line_edit.setPlaceholderText("Please enter username")
        # no edit possible
        # line_edit.setEnabled(False)
        # To put as password
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
