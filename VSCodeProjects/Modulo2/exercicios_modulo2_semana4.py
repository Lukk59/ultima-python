'''
Para este módulo vamos modelar um banco de dados de aplicação TODO usando SQLite. 

Com esta base de dados, vamos criar a aplicação CLI TODO com as funcionalidades:

A) Criar, atualizar e excluir um TODO;
B) Criar, atualizar e excluir categorias;
C) Listar todos os afazeres de um dia específico;
D) Listar todas as categorias;
E) Marcar uma tarefa como concluída.

Para esta atividade recomenda-se criar o banco de dados e as tabelas utilizando o DBeaver e, 
para cada item da atividade, fazer um programa Python nos moldes dos programas criados nesta semana.

O SQLite vai gerar um arquivo do banco de dados; pedimos que este seja enviado por e-mail para 
giulia@ultima.school juntamente com os arquivos Python.

O assunto do email deve ser:

NOME DO ALUNO PD0222 Modulo2Semana4
'''

# Criar:

import sqlite3
conexao = sqlite3.connect('todo.sqlite3')

sql_todo = '''
CREATE TABLE todo (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100),
    descricao TEXT(100),
    data_inicio TEXT(20),
    data_fim TEXT(20),
    status TEXT(1)
);
'''
cursor = conexao.cursor()
cursor.execute(sql_todo)
conexao.commit()
conexao.close()

# Delete:

import sqlite3
conexao = sqlite3.connect('todo.sqlite3')

sql_todo = '"DELETE * FROM todo'
cursor = conexao.cursor()
consulta = cursor.execute(sql_todo)
for resultado in consulta:
    print(resultado)
    print('deletado')

conexao.commit()
conexao.close()

# Listar todas as categorias;

import sqlite3
conexao = sqlite3.connect('todo.sqlite3')

sql_todo = '"SELECT * FROM todo'
cursor = conexao.cursor()
consulta = cursor.execute(sql_todo)
for resultado in consulta:
    print(resultado)

conexao.commit()
conexao.close()

# Listar todos os afazeres de um dia específico:

import sqlite3
conexao = sqlite3.connect('todo.sqlite3')

data = input('qual data inicial deseja consultar? ')

sql_todo = 'SELECT * FROM todo WHERE data_inicio = ?'
cursor = conexao.cursor()
consulta = cursor.execute(sql_todo, data)
for resultado in consulta:
    print(resultado)

conexao.commit()
conexao.close()

# Marcar uma tarefa como concluída:

import sqlite3
conexao = sqlite3.connect('todo.sqlite3')
cursor = conexao.cursor()
tarefa_id = input('qual o id da tarefa que deseja atualizar?: ')
status = input('informe o novo status da tarefa?: ')
sql_update_status = "UPDATE todo SET status = ? WHERE id = ?"
cursor.execute(sql_update_status, [tarefa_id, status])
conexao.commit()
conexao.close()

# Update:

import sqlite3
conexao = sqlite3.connect('todo.sqlite3')
cursor = conexao.cursor()

sql_select_todo = 'select id, nome, descricao, data_inicio, data_fim, status'
tarefas = cursor.execute(sql_select_todo)

for tarefa in tarefas:
    print(
        "id:", tarefa[0], 'nome', tarefa[1], 'descricao', tarefa[2],
        'data_inicio:', tarefa[3], 'data_fim', tarefa[4], 'status', tarefa[5]
        )

tarefa_id = input('qual tarefa deseja alterar (informar o id)? ')

sql = 'SELECT * FROM todo WHERE id = ?'
tarefas = cursor.execute(sql, tarefa_id)
nome_original = ''
descricao_original = ''
data_inicio_original = ''
data_fim_original = ''
status_original = ''
for tarefa in tarefas:
    nome_original = tarefa[0]
    descricao_original = tarefa[1]
    data_inicio_original = tarefa[2]
    data_fim_original = tarefa[3]
    status_original = tarefa[4]
    break

nome = input('qual o novo nome desta tarefa (deixe em branco para nao alterar)? ')
descricao = input('qual a nova descricao desta tarefa (deixe em branco para nao alterar)? ')
data_inicio = input('qual a nova data_inicio desta tarefa (deixe em branco para nao alterar)? ')
data_fim = input('qual a nova data_fim desta tarefa (deixe em branco para nao alterar)? ')
status= input('qual o novo status desta tarefa (deixe em branco para nao alterar)? ')

if not nome:
    nome = nome_original
if not descricao:
    descricao = descricao_original
if not data_inicio:
    data_inicio = data_inicio_original
if not data_fim:
    data_fim = data_fim_original
if not status:
    status = status_original


sql_update = 'UPDATE todo SET nome = ?, descricao = ?, data_inicio = ?, data fim = ?, status = ? WHERE id = ?'
valores = [nome, descricao, data_inicio, data_fim, status]
cursor.execute(sql_update, valores)

conexao.commit()
conexao.close()

# Excluir especifico:

import sqlite3
conexao = sqlite3.connect('todo.sqlite3')
cursor = conexao.cursor()

sql_select_todo = 'select id, nome, descricao, data_inicio, data_fim, status'
tarefas = cursor.execute(sql_select_todo)

for tarefa in tarefas:
    print(
        "id:", tarefa[0], 'nome', tarefa[1], 'descricao', tarefa[2],
        'data_inicio:', tarefa[3], 'data_fim', tarefa[4], 'status', tarefa[5]
        )

tarefa_id = input('qual a tarefa que deseja remover? ')

sql_delete = 'DELETE FROM todo WHERE id = ?'
cursor.execute(sql_delete, [tarefa_id])

conexao.commit()
conexao.close()