from PyQt6.QtGui import * 
from PyQt6.QtWidgets import *
from PyQt6.QtCore import * 
from PyQt6 import uic
import sys

class Window(QWidget): # extended object of QWidget
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Window')
        self.setGeometry(500,300,400,300)
        self.create_widgets()

        # stylesheet = (
        #     'background-color:red'
        # )
        # self.setStyleSheet(stylesheet)

    def create_widgets(self):
        btn = QPushButton('Click Me!', self)
        btn.move(100,100)
        btn.setGeometry(100,100,100,100)
        # btn.setStyleSheet()
        btn.setIcon(QIcon('nih_logo.png'))
        btn.clicked.connect(self.clicked_btn)

        self.label = QLabel('my label', self)
        # self.label.setGeometry(100,100,100,100)

    def clicked_btn(self):
        self.label.setText('Button was clicked')



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())