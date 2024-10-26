import mysql.connector

# (Obs: Opcional o SQLAlchemy já conecta ao banco de dados. by VH)
conexao = mysql.connector.connect(
    host='localhost',
    database='mydb',
    user='root',
    password=''
)

if conexao.is_connected():
    print('Conectado ao banco de dados com sucesso!')
    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES")
    for tabela in cursor.fetchall():
        print(tabela)
    cursor.close()
    conexao.close()
else:
    print('Erro ao conectar ao banco de dados.')