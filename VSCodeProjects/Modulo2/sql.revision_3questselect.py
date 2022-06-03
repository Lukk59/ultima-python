'''
Agora que já temos uma rotina para inserir clientes, pedidos e itens, vamos considerar o seguinte banco 
de dados:

Tabela cliente:

 id	 nome	         cpf
 1	 Maria da Silva	 000.000.000-00
 2	 José Santos	 123.456.789-00

Tabela pedido:

 id	 cliente_id	 data
 1	        1	 2022-01-01
 2	        1	 2022-01-11
 3	        2	 2022-02-01

Tabela item_pedido:

 id	 pedido_id	 produto	 valor	 quantidade
 1	        1	 Prato	     10	     4
 2	        1	 Air Fryer	 350	 2
 3	        2	 Cama Box	 1500	 1
 4	        3	 Celular	 2000	 2
 5	        3	 Headset	 200	 3

Considerando os dados acima, podemos realizar algumas perguntas:

1 – Quais as datas dos pedidos da cliente com nome Maria da Silva?
'''
import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
sql = '''SELECT p.data FROM pedido AS p, cliente AS c 
WHERE p.cliente_id = c.id AND c.nome = 'Maria da Silva'
'''
cursor = conexao.cursor()
consulta = cursor.execute(sql)
for resultado in consulta:
    print(resultado)
'''
O código, feito diretamente no terminal do Python, após a conexão ser aberta executa a 
consulta interligando as duas tabelas: pedido e cliente. O comando sql executado é o seguinte:

SELECT p.data FROM pedido as p, cliente as c WHERE p.cliente_id = c.id AND c.nome = ‘Maria da Silva’

Neste exemplo, precisamos unir as duas tabelas, afinal, a pergunta é sobre os pedidos da 
cliente Maria da Silva e nós não sabemos de antemão qual é o seu id. Assim, precisamos fazer a 
pesquisa com base no nome. Por fim, fazemos um for para percorrer os resultados extraídos da 
consulta e um print para exibir as datas.

2 – Quantos clientes tem a letra “M” no início do nome?

Para responder a esta pergunta precisamos utilizar a opção LIKE da cláusula WHERE:
'''
import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
sql = "SELECT * FROM cliente WHERE nome LIKE 'M%'"
cursor = conexao.cursor()
consulta = cursor.execute(sql)
for resultado in consulta:
    print(resultado)
'''
No exemplo acima, combinamos o LIKE com o “%” para indicar ao banco de dados que queremos todas as 
linhas da tabela cliente que tenham como primeira letra “M”, e depois podem vir quaisquer 
caracteres (inclusive nada).

3 – Qual a quantidade de produtos de um determinado pedido?

Para responder a esta pergunta vamos precisar usar uma função de agregação: SUM. Para chegar 
à resposta vamos fazer o seguinte programa:
'''
import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
pedido_id = input('qual o ID do pedido?: ')
sql = "SELECT SUM(quantidade) FROM item_pedido WHERE pedido_id = ?"
cursor = conexao.cursor()
consulta = cursor.execute(sql, [pedido_id])
for resultado in consulta:
    print(resultado)
'''
No código acima, perguntamos ao usuário que está rodando o programa qual o id do pedido. 
Em seguida, criamos o sql responsável pela consulta utilizando o SUM e, assim como fizemos no 
insert, sempre que dentro do comando sql precisar de valores vindos de “fora” (como no caso do id do pedido), 
colocamos uma “?” e passamos o valor que irá substituir a “?” no segundo parâmetro da função 
cursor.execute. Mesmo que o resultado de uma consulta seja apenas 1 valor, sempre será retornada 
uma lista, assim, precisamos percorrê-la para coletar a informação desejada — no caso, a quantidade 
de itens de um pedido.

Como seria uma consulta que retorne a data do pedido mais recente?

 SELECT MAX(data) FROM pedido
'''