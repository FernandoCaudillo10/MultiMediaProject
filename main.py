#	Course:	CST 205
#	Title:	Final Project
#	Abstract:	This Code creates a program that will allow users to modify an image given
#				various predefined modifications. Another feature is that of creating a 
#				slideshow of given images that can be rearranged at any time.
#	Authors:	FernandoCaudillo, Clement Reau,Jose Andres Gonzalez
#	Date:	14 May 2018

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

		self.movie = QPushButton("Play Slideshow",self)#makes and connects the button to the movie maker
		self.movie.clicked.connect(self.movieMaker)

		self.imageEditor = QPushButton("Edit Picture",self)#makes an connects the button to image editor
		self.imageEditor.clicked.connect(self.imEdit)



		self.openFile = QPushButton("Search From File Explorer",self)#makes and connects to the file explorer
#self.openFile.move(305,365)
		self.openFile.clicked.connect(self.showDialog)

		self.saveFiles = QPushButton("Load Files",self)#loads files from the text box
		self.saveFiles.clicked.connect(self.loadFile)


		self.setWindowTitle('Modi-Fly')
#self.setWindowIcon(QtGui.QIcon('C:\Users\Red\Desktop\sd'))
#gui stuff to set the buttons in boxes
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

		self.setGeometry(100, 100, 1000, 500)#end of gui settings
	@pyqtSlot()

	def showDialog(self):

		fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')#opens the file explorerfor users to choose a file
		#self.img = QPixmap(fname)
		#self.img.show()
		self.textEdit.append(fname[0])#saves the file in an array
		#print(fname)
		
	def loadFile(self):
		lot = self.textEdit.toPlainText()#takes the text in the text box

		tempL = lot.split('\n')
		self.files = self.files+tempL

		self.files = list(filter(None, self.files))
		self.files = list(map(lambda x: x[7:] if x[:4] == "file" else x, self.files))
					
		print(self.files)
		self.textEdit.clear()#clears it after it is loaded

	def movieMaker(self):
		#self.m.updateFiles(self.files)
		self.m = Movie(self.files)#this code updates the array
		self.m.show()#opens the movie maker window 
	def imEdit(self):
		self.f.updateFiles(self.files)#populates the array
		self.f.show()#opens the image editor array

app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())