import sqlite3

##### mudar nome da tabela #####
database_name = 'nome_da_base.db'
table_name = 'tabela'

conn = sqlite3.connect(database_name)

# Verifica se o nome fornecido existe
def nome_existe(name):
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Execute SQL query to search for the name in the table
    query = f"SELECT * FROM {table_name} WHERE name LIKE ?"
    cur.execute(query, ('%' + name + '%',))
    
    # Fetch the results into a list of tuples
    results = cur.fetchall()
    
    # Close the database connection
    conn.close()
    
    # If no results found, return False
    if len(results) == 0:
        return False
    else:
        return True

def fazer_login(nome,senha):
    if nome_existe(nome):
        # Create a curso object
        cursor = conn.cursor()

        # Quero verificar se a senha, que é uma coluna da tabela coincide com a senha dada pelo usuário
        # Primeiro, devo chegar na linha desejada   

        query = f"SELECT * FROM {table_name} WHERE name LIKE ?"
        cursor.execute(query, ('%' + nome + '%',))

        results = cursor.fetchall()

        conn.close()

        password = results[0][1]

        # Confere se a senha está correta
        if password == senha:
            return True
        else:
            return False

        return True
    else:
        return False

# Example usage:
# Replace 'example.db' with your database name, 'my_table' with your table name,
# and 'John' with the name you want to search for.

##### result_df = search_name_in_database('example.db', 'my_table', 'John') #####

# Display the search results
