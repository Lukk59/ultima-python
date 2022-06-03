'''
Este comando remove um ou mais registros de uma tabela de acordo com as condições especificadas, 
e é o comando mais “perigoso” do DML (seguido do UPDATE). Afinal, se a sintaxe for escrita de maneira errada,
 pode remover os dados da tabela por completo. Por exemplo:
DELETE FROM selecao WHERE id = 3;
'''
import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = 'DELETE FROM selecao WHERE id = 3;'
cursor.execute(sql)
conexao.close()
'''
O DELETE, escrito dessa forma, faz com que apenas a linha do id igual a 3 seja removida da tabela. 
Porém, se o comando for escrito dessa forma:

DELETE FROM selecao;

Todos  os dados serão removidos da tabela, apagando-a por completo e deixando apenas a estrutura. 
É por isso que em algumas ferramentas de acesso a banco de dados é obrigatório utilizar a 
cláusula WHERE para os comandos DELETE e UPDATE.

O DELETE, assim como o SELECT e UPDATE, aceita condições com ''and'' e ''or''.
'''