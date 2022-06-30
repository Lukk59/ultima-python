import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = 'UPDATE selecao SET titulos = 6 WHERE id = 1'
cursor.execute(sql)
conexao.close()
'''
É possível atualizar mais de um campo ao mesmo tempo. Para isso, basta separar os campos por vírgula, assim:

UPDATE selecao SET titulos = 6, nome = ‘BRASIL’ WHERE id = 1

O comando UPDATE aceita ser chamado sem a cláusula WHERE, entretanto, isso deve ser feito com muita prudência 
— normalmente não se deseja atualizar todos os registros de uma tabela, e sim parte deles ou apenas um.

O UPDATE, assim como o SELECT, aceita condições com ''and'' e ''or''.
'''