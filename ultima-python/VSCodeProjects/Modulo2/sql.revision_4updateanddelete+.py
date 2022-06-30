import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
cliente_id = input('qual o ID do cliente que deseja atualizar?: ')
nome = input('informe o novo nome do cliente?: ')
cpf = input('informe o novo cpf do cliente?: ')
sql = "UPDATE cliente SET nome = ?, cpf = ? WHERE id = ?"
valores = [nome, cpf, cliente_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()
'''
Considerando a base de dados contida nas tabelas cliente, pedido e item_pedido, vamos fazer um 
programa que possa atualizar os dados de um determinado cliente, fornecendo o id dele.

Para iniciar nosso programa, precisamos antes perguntar o ID do cliente, pois assim poderemos 
realizar o UPDATE em apenas uma linha. Nas linhas 5 e 6 pedimos ao usuário o novo nome e cpf e, 
por fim, na linha 7, o comando UPDATE tem a cláusula WHERE com condição: “id = ?”

Esse “?” da cláusula WHERE vai ser substituído pelo valor da variável cliente_id, o qual será 
fornecido pelo usuário. Rodando este programa, podemos ter o seguinte resultado:
R:
qual o ID do cliente que deseja atualizar?: 2
informe o novo nome do cliente?: Francisco Souza
informe o novo cpf do cliente?: 123.321.123-32

Para finalizar, podemos criar um programa que remova pedidos com base no id da seguinte forma:
'''
import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
pedido_id = input('qual o ID do pedido que deseja remover?: ')
sql = "DELETE FROM pedido WHERE id = ?"
valores = [pedido_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()
'''
Novamente pedimos o ID da linha que desejamos remover. Este é um procedimento muito comum em sistemas. 
Mesmo que possamos remover ou atualizar um dado com quaisquer condições (como uma condição baseada no 
nome para um cliente ou da data para um pedido), geralmente será utilizada a chave primária, no caso o ID.

Executando o programa acima, podemos visualizar o seguinte resultado:
R:
qual o ID do pedido que deseja remover?: 3

Neste caso removemos o pedido com ID 3, para verificar que de fato o pedido foi removido ou, no 
caso anterior, em que o cliente foi atualizado, basta fazer uma consulta ou visualizar a alteração/remoção 
pelo DBeaver.

"TODO" é um tipo de aplicação para gerenciar tarefas a serem executadas. Existem diversos aplicativos 
para isso e é muito comum que alguém que esteja começando a programar ou aprendendo uma nova linguagem 
faça uma aplicação deste tipo.

"CLI" é um acrônimo para "command-line interface", isto é, uma interface baseada no terminal, que fornece 
comandos para a sua execução. As aplicações "CLI" são muito comuns em sistemas baseados no Linux, mas 
também costumam existir em sistemas Windows e Mac OS.
'''