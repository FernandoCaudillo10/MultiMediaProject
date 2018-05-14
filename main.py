#	Course:	CST 205
#	Title:	Final Project
#	Abstract:	This Code creates a program that will allow users to modify an image given
#				various predefined modifications. Another feature is that of creating a 
#				slideshow of given images that can be rearranged at any time.
#	Date:	14 May 2018

#	Authors: Andres Gonzalez

import sys
from movie import Movie
from modifWindow import modif
#from filtering import Filters
#from movie import Movie
from PIL import Image
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Main(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()
		self.files = []
		self.f = modif()

	def initUI(self):      

		self.textEdit = QTextEdit()
#self.textEdit.resize(200,200)
#self.textEdit.move(200,200)
#self.setCentralWidget(self.textEdit)

		self.movie = QPushButton("Play Slideshow",self)
		self.movie.clicked.connect(self.movieMaker)

		self.imageEditor = QPushButton("Edit Picture",self)
		self.imageEditor.clicked.connect(self.imEdit)



		self.openFile = QPushButton("Search From File Explorer",self)
#self.openFile.move(305,365)
		self.openFile.clicked.connect(self.showDialog)

		self.saveFiles = QPushButton("Load Files",self)
		self.saveFiles.clicked.connect(self.loadFile)


		self.setWindowTitle('Modi-Fly')
#self.setWindowIcon(QtGui.QIcon('C:\Users\Red\Desktop\sd'))

		self.hbox2 = QHBoxLayout()
		self.hbox2.addWidget(self.openFile)
		self.hbox = QHBoxLayout()
		self.hbox.addWidget(self.textEdit)
		self.hbox1 = QHBoxLayout()
		self.hbox1.addWidget(self.saveFiles)
		self.hbox1.addWidget(self.movie)
		self.hbox1.addWidget(self.imageEditor)
		self.vbox = QVBoxLayout()
		self.vbox.addLayout(self.hbox2)
		self.vbox.addLayout(self.hbox)
		self.vbox.addLayout(self.hbox1)
		self.setLayout(self.vbox)

		self.setGeometry(100, 100, 1000, 500)
		
	@pyqtSlot()

	def showDialog(self):

		fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
		#self.img = QPixmap(fname)
		#self.img.show()
		self.textEdit.append(fname[0])
		#print(fname)
		
	def loadFile(self):
		lot = self.textEdit.toPlainText()

		tempL = lot.split('\n')
		self.files = self.files+tempL

		self.files = list(filter(None, self.files))
		self.files = list(map(lambda x: x[7:] if x[:4] == "file" else x, self.files))
					
		print(self.files)
		self.textEdit.clear()

	def movieMaker(self):
		#self.m.updateFiles(self.files)
		self.m = Movie(self.files)
		self.m.show()
	def imEdit(self):
		self.f.updateFiles(self.files)
		self.f.show()

app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())

