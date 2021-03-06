#	Course:	CST 205
#	Title:	Final Project
#	Abstract:	This Code creates a program that will allow users to modify an image given
#				various predefined modifications. Another feature is that of creating a 
#				slideshow of given images that can be rearranged at any time.
#	Date:	14 May 2018

#	Authors:	FernandoCaudillo

import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QImage, QDrag
from PyQt5.QtCore import QSize, pyqtSlot, QTimer, QRect
from PIL import Image

class Movie(QWidget):
	def __init__(self, files):
		super().__init__()
		
		self.previousRow = 0

	#used for testing
#		self.pictures = [
#			"images/movie_test/1.png",
#			"images/movie_test/2.png",
#			"images/movie_test/3.png",
#			"images/movie_test/4.png",
#			"images/movie_test/5.png",
#			"images/movie_test/6.png",
#			"images/movie_test/7.png",
#			"images/movie_test/8.png",
#			"images/movie_test/9.png",
#			]
		self.pictures = files
		self.buttonMessage = ["Create Slideshow", "Update Picture Order"]	
		self.initWindow()
		self.createPicIcons()
		
#set all signals
		self.picList.itemClicked.connect(self.updateLeftView)
		self.rightButton.clicked.connect(self.updateList)		
		self.leftButton.clicked.connect(self.destroyTimer)
	def updateFiles(self, ls):
		self.pictures = ls
	def initWindow(self):
#created layout and pushed necessary skeleton
		self.setGeometry(100,100,2000,1000)

		self.layout = QBoxLayout(QBoxLayout.RightToLeft)
		
		self.rightLayout = QBoxLayout(QBoxLayout.TopToBottom)

		self.picList = QListWidget(self)
		self.picList.setIconSize(QSize(100,100))

		self.picList.setDragDropMode(QListWidget.InternalMove)
		self.picList.setDropIndicatorShown(True)
		self.picList.setDragEnabled(True)
		self.setAcceptDrops(True)
		
		self.rightButton = QPushButton(self.buttonMessage[0],self)
		self.rightLayout.addWidget(self.picList)
		self.rightLayout.addWidget(self.rightButton)
		
		self.layout.addLayout(self.rightLayout)
		self.setLayout(self.layout)

	def createPicIcons(self):
#loop through paths and create icon
		for p in self.pictures:
			pic = QPixmap(p)
			icon = QIcon(pic)
			item = QListWidgetItem(p, self.picList)
			item.setStatusTip(p)
			item.setIcon(icon)
#create list of icons with paths		
		self.leftLayout = QBoxLayout(QBoxLayout.TopToBottom)
		self.leftLabel = QLabel()
		self.leftLayout.addWidget(self.leftLabel)
		self.leftButton = QPushButton(self.buttonMessage[1], self)
		self.leftButton.setHidden(not self.leftButton.isHidden())
		self.leftLayout.addWidget(self.leftButton)
		self.layout.addLayout(self.leftLayout)

	def updateLeftView(self):
#creates preview of current active image on left side
		self.previousRow = self.picList.currentRow()
		current = QPixmap(self.picList.currentItem().text())
		self.leftLabel.setPixmap(current)

	def updateList(self):
		
		# Does not work for Ubuntu
		# Tried to make a video file that could be saved from given images	

#		firstFrame = cv2.imread(self.picList.item(0).text())		
#		fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#		out = cv2.VideoWriter("createdVideo", fourcc, 1.0, (firstFrame.shape[0], firstFrame.shape[1]))
#		
#		for i in range(self.picList.count()):
#			frame = cv2.imread(self.picList.item(i).text())
#			out.write(frame)
#			
#		out.release()
		
		self.itemID = 0

		self.toggleRightWidget()
		self.toggleLeftWidget()
		self.playSlideshow()

		
	def playSlideshow(self):
#updates image for slideshow every 1 second
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update)
		self.timer.start(1000)
	
	def update(self):
		try:
			#updates image on left side else-->
			self.leftLabel.setPixmap( QPixmap(self.picList.item(self.itemID).text()) )
			self.itemID += 1
		except:
			#else stops timer and brings up list again
			self.timer.stop()
			self.toggleRightWidget()

	def toggleRightWidget(self):
		self.picList.setHidden(not self.picList.isHidden())
		self.rightButton.setHidden(not self.rightButton.isHidden())
		
	def toggleLeftWidget(self):
		self.leftButton.setHidden(not self.leftButton.isHidden())
	
	def destroyTimer(self):
		self.timer.stop()
		self.toggleRightWidget()
		self.toggleLeftWidget()

