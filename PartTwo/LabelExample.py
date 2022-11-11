import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie


class Window(QWidget):
    def __init__(self):
        super().__init__()
                        # x,y,width,height
        #self.setGeometry(1920,0,400,400)
        self.setWindowTitle("PyQt6 Tutorial")
        self.setWindowIcon(QIcon("../images/pyqt.png"))
        self.setFixedSize(500,450)
        '''
        label = QLabel("Python GUI development", self)
        # label.setText("New Text is Here")
        label.move(100,100)
        label.setFont(QFont("Arial", 20))
        label.setStyleSheet("color:red")
        # label.setText(str(12))
        label.setNum(15)
        '''
        label = QLabel(self)
        movie = QMovie('../images/NyanCat.gif')
        label.setMovie(movie)
        movie.start()

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()