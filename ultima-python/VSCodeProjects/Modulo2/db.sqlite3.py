import sqlite3

conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()

cursor.execute('CREATE TABLE fornecedor (id INT,nome VARCHAR(100),endereço VARCHAR(250))')

conexao.commit()

conexao.close()

'''
1.Quais tipos de colunas o banco SQLite suporta?

 R: Qualquer tipo que desejar contanto que sejam: INTEGER, REAL,NUMERIC, TEXT e BLOB.

2.Crie uma tabela chamada “cliente”. Nela, é necessário ter as seguintes colunas:
id
nome
cpf
data_de_cadastro
Endereco
R:
import sqlite3

conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()

cursor.execute('CREATE TABLE cliente (id INT,nome VARCHAR(100),cpf VARCHAR(11),data_de_cadastro VARCHAR(20),endereco VARCHAR(250))')

conexao.commit()

conexao.close()

3.Não foi informado o tipo dessas colunas na tabela “cliente”. Qual seria o tipo ideal para cada coluna?
R:
id: INTEGER
nome: TEXT
cpf: TEXT
data_de_cadastro: TEXT
Endereco: TEXT
'''