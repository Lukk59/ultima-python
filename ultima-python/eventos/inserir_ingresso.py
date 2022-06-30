import sqlite3
import datetime

conexao = sqlite3.connect('eventos.sqlite3')

cursor = conexao.cursor()

email = input('qual o email do usuario?: ')
sql_usuario = 'select id from usuario where email = ?'
resultado_usuario = cursor.execute(sql_usuario, [email])
usuario_id = 0
for usuario in resultado_usuario:
    usuario_id = usuario[0]
    break

sql_eventos = '''
select e.id, e.nome, e.local, e.preco, c.nome 
from evento as e,categoria as c
where e.categoria_id = c.id
'''
print('eventos disponiveis')
eventos = cursor.execute(sql_eventos)
for evento in eventos:
    print(
        "id:", evento[0], 'nome', evento[1], 'local', evento[2],
        'preco:', evento[3], 'categoria', evento[4]
        )

evento_id = input('qual o ID do evento?: ')
sql_ingresso = 'insert into ingresso (usuario_id, evento_id, data) values (?, ?, ?)'
hoje = datetime.date.today()
valores = [usuario_id, evento_id, str(hoje)]
cursor.execute(sql_ingresso, valores)
conexao.commit()
conexao.close()