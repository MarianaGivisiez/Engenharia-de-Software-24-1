import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import interface_registro
import interface_login
from database import DataBase

db = DataBase()

def main():
    app_principal = QApplication(sys.argv)
    janela = QMainWindow()
    db.connect()
    db.create_tables()
    tela_registro = interface_registro.TelaRegistro(db, janela)
    tela_login = interface_login.TelaLogin(db)

    tela_registro.setupUi(janela)
    # tela_inicial = TelaInicial()
    # tela_inicial.show()

    janela.show()
    # db.close_connection()
    sys.exit(app_principal.exec_())

if __name__ == '__main__':
    main()
