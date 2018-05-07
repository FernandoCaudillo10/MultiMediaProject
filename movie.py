import sys
from PyQt5.QtWidgets import QApplication, QWidget, QBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QImage, QDrag
from PyQt5.QtCore import QSize, pyqtSlot
import cv2 
from PIL import Image

class Movie(QWidget):
	def __init__(self):
		super().__init__()
		
		self.previousRow = 0
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
		
	
		self.picList.itemClicked.connect(self.updateLeftView)
		self.button.clicked.connect(self.updateList)		

	def initWindow(self):

		self.setGeometry(100,100,2000,1000)

		self.layout = QBoxLayout(QBoxLayout.RightToLeft)
		
		self.rightLayout = QBoxLayout(QBoxLayout.TopToBottom)

		self.picList = QListWidget(self)
		self.picList.setIconSize(QSize(100,100))

		self.picList.setDragDropMode(QListWidget.InternalMove)
		self.picList.setDropIndicatorShown(True)
		self.picList.setDragEnabled(True)
		self.setAcceptDrops(True)
		
		self.button = QPushButton(self)
		self.rightLayout.addWidget(self.picList)
		self.rightLayout.addWidget(self.button)
		
		self.layout.addLayout(self.rightLayout)
		self.setLayout(self.layout)

	def createPicIcons(self):
		for p in self.pictures:
			pic = QPixmap(p)
			icon = QIcon(pic)
			item = QListWidgetItem(p, self.picList)
			item.setStatusTip(p)
			item.setIcon(icon)

		self.leftLabel = QLabel()
		self.layout.addWidget(self.leftLabel)

	def updateLeftView(self):
		self.previousRow = self.picList.currentRow()
		current = QPixmap(self.picList.currentItem().text())
		self.leftLabel.setPixmap(current)
		
	def updateList(self):
		
		firstFrame = cv2.imread(self.picList.item(0).text())		
		fourcc = cv2.VideoWriter_fourcc(*'MJPG')
		out = cv2.VideoWriter("createdVideo", fourcc, 1.0, (firstFrame.shape[0], firstFrame.shape[1]))
		
		for i in range(self.picList.count()):
			frame = cv2.imread(self.picList.item(i).text())
			out.write(frame)
			
		out.release()
		



