import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface_registro import Ui_MainWindow

def main():
    app_principal = QApplication(sys.argv)
    janela = QMainWindow()
    tela_registro = Ui_MainWindow()
    tela_registro.setupUi(janela)
    janela.show()
    sys.exit(app_principal.exec_())

if __name__ == '__main__':
    main()
