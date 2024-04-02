import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class AppBase(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplicação base PyQt')
        self.setGeometry(700, 300, 500, 500)

        # A modificar
        self.label = QLabel('Tela inicial', self)
        self.label.setGeometry(50, 50, 300, 100)

def main():
    app = QApplication(sys.argv)
    janela = AppBase()
    janela.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
