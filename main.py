import sys
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
    def initUI(self):      

        self.textEdit = QTextEdit()
        #self.textEdit.resize(200,200)
        #self.textEdit.move(200,200)
        #self.setCentralWidget(self.textEdit)

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
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.setLayout(self.vbox)
        
        self.setGeometry(400, 400, 400, 400)
    
    @pyqtSlot()
    
    def showDialog(self):
 
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        #self.img = QPixmap(fname)
        #self.img.show()
        self.files.append(fname[0])
        #print(fname)
           
    def loadFile(self):
        lot = self.textEdit.toPlainText()
        lot = lot[8:]
        #imga = QPixmap(lot)
        
        #self.show()
        self.files.append(lot)
        print(self.files)  
        self.textEdit.clear()
        #label = QLabel(self)
        #pixmap = QPixmap(self.files[0])
        #label.setPixmap(pixmap)
        #label.show()
    
app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())

