from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtGui
import os

class TelaLogin(QMainWindow):

    def __init__(self):
        super(TelaLogin, self).__init__()
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "../interfaces/tela_login.ui")
        uic.loadUi(file_path, self)

        img_path = os.path.join(base_path, "../images/eye.png")
        self.iconShow = QtGui.QIcon(img_path)
        img_path = os.path.join(base_path, "../images/eye_blind.png")
        self.iconHide = QtGui.QIcon(img_path)

        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_3.setIcon(self.iconShow)
        self.pushButton_3.clicked.connect(self.toggleVisibility)
       
        self.show()
    
    def toggleVisibility(self):
            if self.lineEdit_2.echoMode()==QLineEdit.Normal:
                self.lineEdit_2.setEchoMode(QLineEdit.Password)
                self.pushButton_3.setIcon(self.iconShow)
            else:
                self.lineEdit_2.setEchoMode(QLineEdit.Normal)
                self.pushButton_3.setIcon(self.iconHide)
