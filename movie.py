import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor

class Movie(QWidget):
    def __init__(self,lis):
        super().__init__()
        print(lis)
