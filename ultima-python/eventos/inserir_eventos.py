import sqlite3

conexao = sqlite3.connect('eventos.sqlite3')

cursor = conexao.cursor()

nome = input('qual o nome do evento? ')
local = input('qual o local do evento? ')
preco = input("qual o preco do evento? ")

sql_categorias = "select id, nome from categoria"
categorias = cursor.execute(sql_categorias)
print(categorias)
for categoria in categorias:
    print('id:', categoria[0], 'nome:', categoria[1])

categoria_id = input('qual a categoria do evento? ')
valores = [nome, local, float(preco), categoria_id]

sql = 'insert into evento (nome, local, preco, categoria_id) values (?, ?, ?, ?)'
cursor.execute(sql, valores)
conexao.commit()
conexao.execute()