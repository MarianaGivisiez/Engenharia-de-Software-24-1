# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from database import DataBase
from interface_login import TelaLogin

class TelaRegistro():
    def __init__(self, db, janela):
        # Armazena a instância do banco de dados
        self.db = db
        self.janela = janela

    def registrar(self):
        usuario = self.lineEdit.text()
        print(usuario)
        senha = self.lineEdit_2.text()
        confirmacao = self.lineEdit_3.text()

        print(self.db.check_user_name(usuario))
        if(self.db.check_user_name(usuario) == True):
                self.label_5.setText("Nome de usuário indisponível")
                self.label_5.adjustSize()
        else:
                is_user_inserted = self.db.insert_user(usuario,senha,confirmacao)
                if(is_user_inserted):
                        self.mudar_para_login()
                else:
                        self.label_5.setText("As senhas não coincidem")
                        self.label_5.adjustSize()

    def mudar_para_login(self):
          tela_login = TelaLogin(self.db)
          tela_login.setupUi(self.janela)
                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(514, 380)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"\n"
"background-color: rgb(212, 255, 217);\n"
"\n"
"")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 240, 131, 41))
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(185, 300, 180, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1.setFont(font)
        self.pushButton_1.setMouseTracking(False)
        self.pushButton_1.setAutoFillBackground(False)
        self.pushButton_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton.clicked.connect(self.registrar) #colocar nome da função
        self.pushButton_1.clicked.connect(self.mudar_para_login)
            
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 100, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        #label 1
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #label 2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #label 3
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #label 4
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 10, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        #label 5
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 220, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_3")
        self.label_5.setStyleSheet("color: red;")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 140, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 180, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setMouseTracking(True)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de Registro"))
        self.pushButton.setText(_translate("MainWindow", "Registrar-se"))
        self.pushButton_1.setText(_translate("MainWindow", "Já tenho cadastro"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Digite seu nome de usuário"))
        self.label.setText(_translate("MainWindow", "Nome de usuário"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.label_3.setText(_translate("MainWindow", "Repetir senha"))
        self.label_4.setText(_translate("MainWindow", "Registro"))
        self.label_5.setText(_translate("", ""))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Digite sua senha"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Digite novamente a senha"))
