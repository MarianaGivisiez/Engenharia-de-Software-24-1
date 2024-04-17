import sqlite3
from datetime import datetime

class DataBase():
    def __init__(self, name='system.db'):
        # Inicialização da classe com o nome do banco de dados
        self.name = name

    def connect(self):
        # Método para conectar ao banco de dados
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        # Método para fechar a conexão com o banco de dados
        try:
            self.connection.close()
        except:
            pass

    def create_tables(self):
        # Método para criar as tabelas necessárias no banco de dados
        try:
            cursor = self.connection.cursor()
            # Criação da tabela 'users' se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                );
            """)
            # Criação da tabela 'expenses' se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    date DATE NOT NULL,  -- Usando tipo de dado DATE para armazenar datas
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                );
            """)
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão")

    def insert_user(self, user, password, password_confirm):
        # Método para inserir um novo usuário no banco de dados
        if(user != "" and password != "" and password_confirm != ""):
            if password == password_confirm:
                try:
                    cursor = self.connection.cursor()
                    cursor.execute(""" 
                                INSERT INTO users(user, password) VALUES(?,?)
                    """, (user, password))
                    self.connection.commit()
                    print("Usuário registrado com sucesso!")
                    return True
                except AttributeError:
                    print("Faça a conexão")
            else:
                print("As senhas não coincidem. Tente novamente.")
                return False
        else:
            print("Algum campo está vazio!")
            return False

    def check_user(self, user, password):
        # Método para verificar se um usuário existe no banco de dados
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           SELECT * FROM users;
                           """)
            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password:
                    return True
                else:
                    continue
            return False
        except:
            pass

    def check_user_name(self, user):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           SELECT * FROM users;
                           """)
            for linha in cursor.fetchall():
                if linha[1].upper() == user.upper():
                    return True
                else:
                    continue
            return False
        except:
            pass

    def check_user_password(self, user, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           SELECT * FROM users;
                           """)
            for linha in cursor.fetchall():
                print(linha[1])
                if linha[1].upper() == user.upper():
                    if linha[2] == password:
                        return True
                    else:
                        return False
                else:
                    continue
            return False
        except:
            pass

    def name_exists(self, user):
        # Método para verificar se um nome de usuário já existe no banco de dados
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + user + '%',))
            results = cursor.fetchall()
            if len(results) == 0:
                return False
            else:
                return True
        except AttributeError:
            print("Faça a conexão")

    def fazer_login(self, user, password):
        # Método para fazer login verificando o nome de usuário e senha no banco de dados
        if self.name_exists(user):
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT password FROM users WHERE name LIKE ?", ('%' + user + '%',))
                results = cursor.fetchall()
                password = results[0][0]
                if password == password:
                    return True
                else:
                    return False
            except AttributeError:
                print("Faça a conexão")
        else:
            return False

    def insert_expense(self, user_id, name, date, amount, category):
        # Método para inserir uma nova despesa no banco de dados
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" 
                INSERT INTO expenses(user_id, name, date, amount, category) VALUES(?,?,?,?,?)
            """, (user_id, name, date, amount, category))
            self.connection.commit()
            print("Despesa registrada com sucesso!")
        except AttributeError:
            print("Faça a conexão")

    def get_expenses(self, user_id):
        # Método para recuperar as despesas de um usuário específico
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM expenses WHERE user_id = ?
            """, (user_id,))
            return cursor.fetchall()
        except AttributeError:
            print("Faça a conexão")

    def edit_expense_name(self, expense_id, name):
        # Método para editar o nome de uma despesa no banco de dados
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE expenses
                SET name = ?
                WHERE id = ?
            """, (name, expense_id))
            self.connection.commit()
            print("Nome da despesa editado com sucesso!")
        except AttributeError:
            print("Faça a conexão")

    def edit_expense_date(self, expense_id, date):
        # Método para editar a data de uma despesa no banco de dados
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE expenses
                SET date = ?
                WHERE id = ?
            """, (date, expense_id))
            self.connection.commit()
            print("Data da despesa editada com sucesso!")
        except AttributeError:
            print("Faça a conexão")

    def edit_expense_amount(self, expense_id, amount):
        # Método para editar o valor de uma despesa no banco de dados
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE expenses
                SET amount = ?
                WHERE id = ?
            """, (amount, expense_id))
            self.connection.commit()
            print("Valor da despesa editado com sucesso!")
        except AttributeError:
            print("Faça a conexão")

    def edit_expense_category(self, expense_id, category):
        # Método para editar a categoria de uma despesa no banco de dados
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE expenses
                SET category = ?
                WHERE id = ?
            """, (category, expense_id))
            self.connection.commit()
            print("Categoria da despesa editada com sucesso!")
        except AttributeError:
            print("Faça a conexão")



