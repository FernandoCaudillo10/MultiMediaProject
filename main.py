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
        self.m = Movie()
        self.f = modif()

    def initUI(self):      

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

app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())

