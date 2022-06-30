import sqlite3
conexao = sqlite3.connect('db.sqlite3')
sql = '''
INSERT INTO fornecedor (id, nome, endereco)
VALUES (1,'empresa tal', 'rua tal, 23');
'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()

id = input('digite o ID do forenecedor: ')
nome = input('digite o nome do fornecedor: ')
endereco = input('digite o endereço do fornecedor: ')

import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = '''
INSERT INTO fornecedor (id, nome, endereco) values (?, ?, ?);
'''
valores = [id, nome, endereco]
cursor.execute(sql, valores)
conexao.commit()
print('dados inseridos com sucesso')
conexao.close()