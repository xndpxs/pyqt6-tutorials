import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
                        # x,y,width,height
        # self.setGeometry(1920,0,400,400)
        self.setWindowTitle("PyQt6 QHBoxLayout")
        self.setWindowIcon(QIcon("../images/pyqt.png"))
        self.setFixedSize(400,400)

        # starting layout (horizontal box I guess?)
        hbox = QHBoxLayout()

        # creating the buttons for the layout
        btn1 = QPushButton("Click one")
        btn2 = QPushButton("Click two")
        btn3 = QPushButton("Click three")
        btn4 = QPushButton("Click four")

        # Adding layout buttons

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        # adding spacing btw buttons
        hbox.addSpacing(100)
        hbox.addStretch(20)

        # To show the layout on the window
        self.setLayout(hbox)




app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()