from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtGui
import os

class TelaLogin(QMainWindow):

    def __init__(self):
        super(TelaLogin, self).__init__()
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "../interfaces/tela_registro.ui")
        uic.loadUi(file_path, self)
       
        self.show()
