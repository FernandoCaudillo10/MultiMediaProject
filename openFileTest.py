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
    def initUI(self):      

        self.textEdit = QTextEdit()
        #self.setCentralWidget(self.textEdit)

        #self.statusBar()
        self.openFile = QPushButton("search",self)
        #openFile = QAction(QIcon('open.png'), 'Open', self)
        #openFile.setShortcut('Ctrl+O')
        #openFile.setStatusTip('Open new File')
        #openFile.triggered.connect(self.showDialog)
        self.openFile.clicked.connect(self.showDialog)

        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(openFile)       
        
        
        self.setWindowTitle('File dialog')

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.textEdit)
        hbox1 = QHBoxLayout(self)
        hbox1.addWidget(self.openFile)
        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        self.setLayout(vbox)
        self.setGeometry(400, 300, 350, 400)
    
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

