import sys
from filtering import Filters
from movie import Movie
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.edit = QLineEdit("drag and drop", self)
        self.edit.setDragEnabled(True)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.edit)
        self.setLayout(hbox)
        self.setGeometry(200,200,200,200)




app = QApplication(sys.argv)

mw = MainWindow()
f = Filters()
m = Movie()

mw.show()
f.show()
m.show()

sys.exit(app.exec_())
