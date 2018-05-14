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
<<<<<<< HEAD
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
=======
    def __init__(self):#or is this the constructor
        super().__init__()
        
        self.initUI()
        self.files = []
        self.m = Movie()#creating the other pages
        self.f = modif()#

    def initUI(self):      #the constructor i think

        self.textEdit = QTextEdit()
        #self.textEdit.resize(200,200)
        #self.textEdit.move(200,200)
        #self.setCentralWidget(self.textEdit)

        self.movie = QPushButton("movie",self)
        self.movie.clicked.connect(self.movieMaker)

        self.imageEditor = QPushButton("Edit",self)
        self.imageEditor.clicked.connect(self.imEdit)
        


        self.openFile = QPushButton("search",self)
        #self.openFile.move(305,365)
        self.openFile.clicked.connect(self.showDialog)

        self.saveFiles = QPushButton("load",self)
        self.saveFiles.clicked.connect(self.loadFile)

        
        self.setWindowTitle('Good Stuff')
        #self.setWindowIcon(QtGui.QIcon('C:\Users\Red\Desktop\sd'))

        self.hbox2 = QHBoxLayout()#gui stuff
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
        
        self.setGeometry(400, 400, 400, 400)
    
    @pyqtSlot()
    
    def showDialog(self):#opens and saves the file path
 
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        #self.img = QPixmap(fname)
        #self.img.show()
        self.files.append(fname[0])
        #print(fname)
           
    def loadFile(self):#drag and drop part, can only take one file at a time.
        lot = self.textEdit.toPlainText()
        lot = lot[8:]
        self.files.append(lot)
        print(self.files)  
        self.textEdit.clear()

    def movieMaker(self):#connects to non-working code 
        self.m.updateFiles(self.files)
        self.m.show()
    def imEdit(self):#image editor
        self.f.updateFiles(self.files)
        self.f.show()
>>>>>>> b9dc65a85b2f08d973363d7fd66623374490be4b

app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())

