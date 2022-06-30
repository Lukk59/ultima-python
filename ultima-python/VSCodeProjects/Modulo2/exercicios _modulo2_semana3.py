'''
Dada a tabela “Fornecedor” abaixo, realize as seguintes operações:

 id	 nome	                         endereco	               produto
 1	 Empresa de Leite Parmaleite	 Rua dos Leites, 23	       Leite
 2	 Peixaria Abril	                 Rua dos Leites, 26	       Peixe
 3	 Açougue Legal	                 Rua das Carnes, 30	       Carnes
 4	 Açougue Novo	                 Rua das Carnes, 50	       Carnes

A)Utilizando o comando INSERT, insira mais dois novos fornecedores:“Padaria do Pão” e “Marcenaria Martelo”,
com os ids 3 e 4 respectivamente, e crie também os endereços;

B)Atualize o endereço do fornecedor com id = 2 para “Rua dos Peixes, 26” com o comando UPDATE;

C)Selecione todos os registros da tabela fornecedor com o comando SELECT; 

D)Selecione todos os registros da tabela fornecedor que tenham a coluna produto igual a Carnes;

E)Remova o fornecedor que tem o id = 1 com o comando DELETE.
'''
# A)
import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = '''
INSER INTO Fornecedor (id, nome, endereco)
VALUES (?, ?, ?)
'''
valores = [(3, "Padaria do Pão", "Rua do pao, 45"),
(4, "Marcenaria Martelo", "Rua do martelo, 32")]
cursor.executemany(sql, valores)
conexao.commit()
print('dados inseridos com sucesso')
conexao.close()

# B)
import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = 'UPDATE Fornecerdor SET endereco = “Rua dos Peixes, 26” WHERE id = 2'
resultados = cursor.execute(sql)
for resultado in resultados:
    print(resultado)
print('DADOS ATUALIZADOS')
conexao.close()

# C)
import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = 'SELECT * FROM Fornecedor' 
resultados = cursor.execute(sql)
for resultado in resultados:
    print(resultado)
print('FIM DO PROGRAMA')
conexao.close()

# D)
import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = 'SELECT * FROM Fornecedor WHERE produto = carnes' 
resultados = cursor.execute(sql)
for resultado in resultados:
    print(resultado)
print('FIM DO PROGRAMA')
conexao.close()

# E)
import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = 'DELETE FROM Fornecerdor WHERE id = 1'
cursor.execute(sql)
print('DADOS DELETADOS')
conexao.close()