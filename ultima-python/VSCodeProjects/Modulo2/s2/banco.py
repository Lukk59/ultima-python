import sqlite3

conexao = sqlite3.connect('aula2database.sqlite3')

cursor = conexao.cursor()

sql = '''
create table pedido(
    id int nor null,
    cliente varchar(100),
    data varchar(20),
    primary key (id)
)
'''

cursor.execute(sql)
conexao.commit()
conexao.close()
