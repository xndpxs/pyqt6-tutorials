import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
                        # x,y,width,height
        # self.setGeometry(1920,0,400,400)
        self.setWindowTitle("PyQt6 QHBoxLayout")
        self.setWindowIcon(QIcon("../images/pyqt.png"))
        self.setFixedSize(400,400)
        # starting layout (vertical box I guess?)
        vbox = QVBoxLayout()

        # creating buttons
        btn1 = QPushButton("Click one")
        btn2 = QPushButton("Click two")
        btn3 = QPushButton("Click three")
        btn4 = QPushButton("Click four")

        #Add push buttons on vbox
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        #show the layout
        self.setLayout(vbox)

        vbox.addStretch(20)
        vbox.addSpacing(100)





app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()