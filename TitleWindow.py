import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
                        # x,y,width,height
        self.setGeometry(1920,0,400,400)
        self.setWindowTitle("PyQt6 Tutorial")
        self.setWindowIcon(QIcon("images/pyqt.png"))
        #self.setFixedWidth(700)
        #self.setFixedWidth(300)
        self.setStyleSheet("background-color: gray")
        self.setWindowOpacity(0.5)





app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()


