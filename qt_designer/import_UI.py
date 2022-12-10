from PyQt6.QtGui import * 
from PyQt6.QtWidgets import *
from PyQt6.QtCore import * 
from PyQt6 import uic
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('nk_page.ui', self)

app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())