import sqlite3
conexao = sqlite3.connect('eventos.sqlite3')
cursor = conexao.cursor()

sql = 'select id, nome, local, preco, categoria_id from evento'
eventos = cursor.execute(sql)

for evento in eventos:
    print(
        "id:", evento[0], 'nome', evento[1], 'local', evento[2],
        'preco:', evento[3], 'categoria_id', evento[4]
        )

evento_id = input('qual o evento que deseja remover? ')

sql_delete = 'delete from evento where id = ?'
cursor.execute(sql_delete, [evento_id])

conexao.commit()
conexao.close()