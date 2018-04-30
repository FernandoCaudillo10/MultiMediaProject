import sys
#from filtering import Filters
#from movie import Movie
from PIL import Image
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Main(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):      

        self.textEdit = QTextEdit()
        #self.textEdit.resize(200,200)
        #self.textEdit.move(200,200)
        self.setCentralWidget(self.textEdit)

        #self.statusBar()
        self.openFile = QPushButton("search",self)
        self.openFile.move(305,365)
        #openFile = QAction(QIcon('open.png'), 'Open', self)
        #openFile.setShortcut('Ctrl+O')
        #openFile.setStatusTip('Open new File')
        #openFile.triggered.connect(self.showDialog)
        self.openFile.clicked.connect(self.showDialog)


        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(openFile)       
        
        
        self.setWindowTitle('File dialog')
        """
        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.textEdit)
        self.hbox1 = QHBoxLayout(self)
        self.hbox1.addWidget(self.openFile)
        self.vbox = QVBoxLayout(self)
        self.vbox.addChildLayout(self.hbox)
        self.vbox.addChildLayout(self.hbox1)
        self.setLayout(self.vbox)
        """
        self.setGeometry(400, 400, 400, 400)
    
    
    @pyqtSlot()
    def showDialog(self):
 
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                data.show()
    

app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())

