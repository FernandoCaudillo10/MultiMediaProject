import sys
#from filtering import Filters
#from movie import Movie
from PIL import Image
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):      

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        hbox = QHBoxLayout()
        #hbox.addWidget(self.textEdit)

        self.statusBar()
        self.but = QPushButton("hi",self)
        self.but.clicked.connect(self.clicked)
        self.hbox.addWidget(self.but)
        self.setLayout(hbox)
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')


    
    """  
    
    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                return data
      """      
    @pyqtSlot()
    def clicked(self):
        self.image = QPixmap(data)
        self.show()


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())

""" 
app = QApplication(sys.argv)
mw = MainWindow()

f = Filters()
m = Movie()
mw.show()

f.show()
m.show()

sys.exit(app.exec_())
"""