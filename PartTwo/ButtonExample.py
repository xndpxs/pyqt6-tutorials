import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize

def createButton():
    btn = QPushButton("Click", self)




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,500)
        self.setWindowTitle("PyQt6 QPushButton")
        self.setWindowIcon(QIcon("../images/pyqt.png"))
        self.create_button()



    def create_button(self):
        btn = QPushButton("Click", self)
                    #    x,y,width,height
        btn.setGeometry(100,100,130,130)
        btn.setFont(QFont("Comic Sans",16, QFont.Weight.Bold))
        btn.setIcon(QIcon('../images/pyqt.png'))
        btn.setIconSize(QSize(36,36))


    # Create popup menu
        menu = QMenu()
        menu.setFont(QFont("Comic Sans", 16, QFont.Weight.Bold))
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)




app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()