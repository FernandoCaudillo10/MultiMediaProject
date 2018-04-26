import sys
from PyQt5.QtWidgets import QApplication, QWidget, QBoxLayout, QLabel, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtCore import QSize, pyqtSlot
 
from PIL import Image

class Movie(QWidget):
    def __init__(self):
        super().__init__()
        
        self.pictures = [
                "images/movie_test/1.png",
                "images/movie_test/2.png",
                "images/movie_test/3.png",
                "images/movie_test/4.png",
                "images/movie_test/5.png",
                "images/movie_test/6.png",
                "images/movie_test/7.png",
                "images/movie_test/8.png",
                "images/movie_test/9.png",
                ]
        self.initWindow()
        self.createPicIcons()

        self.leftLabel = QLabel()
        self.layout.addWidget(self.leftLabel)

        self.picList.currentItemChanged.connect(self.updateLeftView)

    def initWindow(self):

        self.setGeometry(100,100,2000,1000)

        self.layout = QBoxLayout(QBoxLayout.RightToLeft)

        self.picList = QListWidget(self)
        self.picList.setIconSize(QSize(100,100))

        self.layout.addWidget(self.picList)

        self.setLayout(self.layout)

    def createPicIcons(self):
        for p in self.pictures:
            pic = QPixmap(p)
            
            icon = QIcon(pic)
            item = QListWidgetItem(p, self.picList)
            item.setStatusTip(p)
            item.setIcon(icon)
    
    def updateLeftView(self):
        current = QPixmap(self.picList.currentItem().text())
        self.leftLabel.setPixmap(current)
