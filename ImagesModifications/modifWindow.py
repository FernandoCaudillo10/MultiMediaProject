


import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from PIL import Image
import modifications


class modif(QWidget):
    
    def __init__(self):
        super().__init__()
    
        vbox = QVBoxLayout()
        
        self.im = Image.open("portrait2.jpg")
        
        self.my_btn1 = QPushButton("grayscale", self)
        self.my_btn2 = QPushButton("negative ", self)
        self.my_btn3 = QPushButton("dark ", self)
        self.my_btn4 = QPushButton("bright ", self)
        self.my_btn5 = QPushButton("contrast ", self)
        self.my_btn6 = QPushButton("binarization ", self)
        self.my_btn7 = QPushButton("edges ", self)
        self.my_btn = QPushButton("SHOW ", self)
                  
        self.my_btn1.clicked.connect(self.on_click1)
        self.my_btn2.clicked.connect(self.on_click2)
        self.my_btn3.clicked.connect(self.on_click3)
        self.my_btn4.clicked.connect(self.on_click4)
        self.my_btn5.clicked.connect(self.on_click5)
        self.my_btn6.clicked.connect(self.on_click6)
        self.my_btn7.clicked.connect(self.on_click7)
        self.my_btn.clicked.connect(self.on_click)
        
        vbox.addWidget(self.my_btn1)
        vbox.addWidget(self.my_btn2)
        vbox.addWidget(self.my_btn3)
        vbox.addWidget(self.my_btn4)
        vbox.addWidget(self.my_btn5)
        vbox.addWidget(self.my_btn6)
        vbox.addWidget(self.my_btn7)
        vbox.addWidget(self.my_btn)
        
        self.setWindowTitle("Modifications Window")
        self.setLayout(vbox)
        self.setGeometry(10,10,640,480)
        self.show()
        
    @pyqtSlot() 
    def on_click1(self):
        self.im = modifications.grayscale("portrait2.jpg")
    def on_click2(self):
        self.im = modifications.negative("portrait2.jpg")
    def on_click3(self):
        self.im = modifications.darkimg("portrait2.jpg")
    def on_click4(self):
        self.im = modifications.bright("portrait2.jpg")
    def on_click5(self):
        self.im = modifications.test("portrait2.jpg")
    def on_click6(self):
        self.im = modifications.binarization("portrait2.jpg")       
    def on_click7(self):
        self.im = modifications.edges("portrait2.jpg")    
    def on_click(self):
        self.im.show()
        

app = QApplication(sys.argv) 
main_win = modif() 
main_win.show() 
sys.exit(app.exec_())