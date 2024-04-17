import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QStyledItemDelegate, QHeaderView
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QColor, QFont
import pandas as pd
import datetime
import numpy

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gerenciador de Despesas")
        self.setGeometry(100, 100, 800, 600)

        # Lendo o arquivo Excel com Pandas
        try:
            self.df = pd.read_excel("dados.xlsx")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            sys.exit(1)

        self.df['Data'] = self.df['Data'].dt.date

        self.table_view = QTableView(self)

        self.category_count_label = QLabel("", self)
        self.category_expense_label = QLabel("", self)
        self.count_name_label = QLabel("", self)
        self.count_value_label = QLabel("", self)
        self.expense_value_label = QLabel("", self)

        self.update_metrics()

        self.add_button = QPushButton("Adicionar Despesa", self)
        self.edit_button = QPushButton("Editar Despesa", self)

        self.add_button.clicked.connect(self.add_expense)
        self.edit_button.clicked.connect(self.edit_expense)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)

        metrics_layout = QHBoxLayout()
        metrics_layout.addWidget(self.category_count_label)
        metrics_layout.addWidget(self.category_expense_label)

        expenses_layout = QHBoxLayout()
        expenses_layout.addWidget(self.count_name_label)
        expenses_layout.addWidget(self.count_value_label)
        expenses_layout.addWidget(self.expense_value_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(metrics_layout)
        main_layout.addLayout(expenses_layout)
        main_layout.addWidget(self.table_view)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        model = PandasModel(self.df)
        self.table_view.setModel(model)

        delegate = ColorDelegate(self.df)
        self.table_view.setItemDelegate(delegate)

        # Ajustando o tamanho das colunas ao conteúdo
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.show()

    def add_expense(self):
        # Implemente a função de adicionar despesa aqui
        print("Adicionar Despesa")

    def edit_expense(self):
        # Implemente a função de editar despesa aqui
        print("Editar Despesa")

    def update_metrics(self):
        category_counts = self.df['Categoria'].value_counts()
        names_list = category_counts.index.tolist()
        count_list = category_counts.tolist()
        names_str = 'Categoria:{}'.format(''.join('\n{}'.format(name) for name in names_list))
        counts_str = 'Número de despesas:{}'.format(''.join('\n{}'.format(value) for value in count_list))

        self.count_name_label.setText(names_str)
        self.count_value_label.setText(counts_str)
        
        expenses_list = self.df.groupby('Categoria')['Valor'].sum().tolist()
        expenses_list = ["R$ " + str(value) for value in expenses_list]
        expenses_str = 'Valor total:{}'.format(''.join('\n{}'.format(value) for value in expenses_list))

        self.expense_value_label.setText(expenses_str)
        self.category_count_label.setText("Visão geral das despesas:")

        font = self.category_count_label.font()
        font.setPointSize(9)
        self.category_count_label.setFont(font)
        self.count_name_label.setFont(font)
        self.count_value_label.setFont(font)
        self.expense_value_label.setFont(font)

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                value = self._data.iloc[index.row(), index.column()]

                if isinstance(value, datetime.date):
                    return value.strftime('%d-%m-%Y')
                elif isinstance(value, numpy.int64):
                    return 'R$ {}'.format(value)

                return str(value)
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None

class ColorDelegate(QStyledItemDelegate):
    def __init__(self, df):
        super().__init__()
        self.df = df

    def paint(self, painter, option, index):
        if index.isValid():
            value = str(self.df.iloc[index.row(), 3])
            color = self.get_color(value)
            painter.fillRect(option.rect, QColor(color))
            super().paint(painter, option, index)

    def get_color(self, value):
        if value == "Alimentação":
            return '#ffb1a5'
        elif value == "Transporte":
            return '#a3d9f0'
        elif value == "Saúde":
            return '#a6f1a6'
        elif value == "Lazer":
            return '#ffe970'
        else:
            return '#ffffff'

def main():
    app_principal = QApplication(sys.argv)

    tela_inicial = TelaInicial()
    tela_inicial.show()

    sys.exit(app_principal.exec_())

if __name__ == '__main__':
    # para testar, basta rodar o arquivo
    main()