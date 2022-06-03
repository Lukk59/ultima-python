import sqlite3

conexao = sqlite3.connect('eventos.sqlite3')

cursor = conexao.cursor()

nome = input("qual o nome da categoria?: ")

sql = 'INSERT INTO categoria (nome) values (?)'

cursor.execute(sql, [nome])

conexao.commit()
conexao.close()