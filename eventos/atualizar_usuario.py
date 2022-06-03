import sqlite3
conexao = sqlite3.connect('eventos.sqlite3')
cursor = conexao.cursor()

sql = 'select id, nome, email from usuario'
usuarios = cursor.execute(sql)

for usuario in usuarios:
    print('id:', usuario[0], 'nome', usuario[1], 'email', usuario[2])

usuario_id = input('qual usuario deseja alterar (informar o id)? ')

sql = 'select id, nome, email from usuario where id = ?'
usuarios = cursor.execute(sql, usuario_id)
nome_original = ''
email_original = ''
for usuario in usuarios:
    nome_original = usuario[0]
    email_original = usuario[1]
    break

nome = input('qual o novo nome deste usuario (deixe em branco para nao alterar)? ')
email = input('qual o novo email deste usuario (deixe em branco para nao alterar)? ')

if not nome:
    nome = nome_original
if not email:
    email = email_original

sql_update = 'update usuario set nome = ?, email = ? where id= ?'
cursor.execute(sql_update, [nome, email, usuario_id])

conexao.commit()
conexao.close()