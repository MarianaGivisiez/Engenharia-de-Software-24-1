# Importação do módulo sqlite3 para interagir com o banco de dados SQLite
import sqlite3

# Definição da classe DataBase para gerenciar o banco de dados
class DataBase():
    def __init__(self, name='system.db'):
        # Inicialização da classe com o nome do banco de dados (padrão: 'system.db')
        self.name = name

    def conecta(self):
        # Método para conectar ao banco de dados
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        # Método para fechar a conexão com o banco de dados
        try:
            self.connection.close()
        except:
            pass

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                );
            """)
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão")


    def insert_user(self, user, password, password_confirm):
        # Método para inserir um novo usuário no banco de dados
        if password == password_confirm:
            try:
                cursor = self.connection.cursor()
                # Inserção de um novo usuário na tabela 'users'
                cursor.execute(""" 
                               INSERT INTO users( user, password) VALUES(?,?)
                """, ( user, password))
                self.connection.commit()
                print("Usuário registrado com sucesso!")
            except AttributeError:
                print("faça a conexão")
        else:
            print("As senhas não coincidem. Tente novamente.")

    def check_user(self, user, password):
        # Método para verificar se um usuário existe no banco de dados
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           SELECT * FROM users;
                           """)
            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password:
                    return "user"
                else:
                    continue
            return "sem acesso"
        except:
            pass
        
    def nome_existe(self, name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
            results = cursor.fetchall()
            if len(results) == 0:
                return False
            else:
                return True
        except AttributeError:
            print("Faça a conexão")

    def fazer_login(self, nome, senha):
        if self.nome_existe(nome):
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT password FROM users WHERE name LIKE ?", ('%' + nome + '%',))
                results = cursor.fetchall()
                password = results[0][0]
                if password == senha:
                    return True
                else:
                    return False
            except AttributeError:
                print("Faça a conexão")
        else:
            return False
        
    
    def insert_expense(self, user_id, description, amount):
        # Método para inserir uma nova despesa no banco de dados
        try:
            cursor = self.connection.cursor()
            # Inserção de uma nova despesa na tabela 'expenses'
            cursor.execute(""" 
                INSERT INTO expenses(user_id, description, amount) VALUES(?,?,?)
            """, (user_id, description, amount))
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
    
# Teste
# db = DataBase()
# db.conecta()
# db.create_tables()  # Criação das tabelas necessárias no banco de dados
# db.insert_user("Jooo", "password123", "password123")  # Inserção de um novo usuário
# db.close_connection()  # Fechamento da conexão com o banco de dados

# Example usage:
# Replace 'example.db' with your database name, 'my_table' with your table name,
# and 'John' with the name you want to search for.

##### result_df = search_name_in_database('example.db', 'my_table', 'John') #####

# Display the search results
