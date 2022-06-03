'''
Com as tabelas criadas, vamos precisar inserir alguns dados. Para isso, vamos criar um programa 
que possa popular esse banco de dados:
'''
import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
print('insira os dados do cliente: ')
nome = input('qual o nome do cliente: ')
cpf = input('qual o cpf do cliente: ')
valores = [nome, cpf]
sql_inserir = 'INSERT INTO cliente (nome, cpf) values (?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()
'''
Na rotina acima, abrimos novamente a conexão com o banco e em seguida fazemos perguntas para o usuário que 
está executando nosso programa. Solicitamos o nome e o cpf e então inserimos os dados em uma lista chamada 
valores.

Depois, criamos o comando sql para inserção de dados (variável sql_inserir), e por fim executamos o 
comando cursor.execute(sql_inserir, valores). Como discutido anteriormente, a função cursor.execute 
pode receber dois argumentos: o primeiro é o comando sql e o segundo uma lista de valores. Esses valores 
irão substituir as interrogações contidas no comando sql (primeiro argumento). Ou seja, o 
argumento sql_inserir têm duas interrogações e, sendo assim, a lista valores precisa ter duas 
informações — no caso o nome e o cpf.

Perceba que não indicamos o campo id ao inserir o dado, pois na criação da tabela indicamos que esse campo 
é AUTOINCREMENT, assim o id vai ser gerado de forma automática.

Ao executar essa rotina, teremos essa possível visualização (pode ser rodado várias vezes para inserir 
vários dados):

Ex:
insira os dados do cliente:
qual o nome do cliente: Maria da Silva
qual o cpf do cliente: 000.000.000-00
Ao ser perguntado sobre o nome, a resposta foi “Maria da Silva” e o cpf “000.000.000-00”.

Agora que já temos a rotina para inserir clientes, 
vamos fazer a rotina para inserir um pedido:
'''
import sqlite3
import datetime
conexao = sqlite3.connect('banco.sqlite3')
print('insira os dados do pedido: ')
cliente_id = input('qual o ID do cliente?: ')
hoje = datetime.date.today()
valores = [cliente_id, hoje]
sql_pedido = 'INSERT INTO pedido (cliente_id, data) values (?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_inserir, valores)
print('ID do pedido: ', cursor.lastrowid)
'''
Na primeira parte, pedimos o id do cliente e identificamos a data atual. O módulo datetime já vem disponível 
quando instalamos o Python. Nele, é possível identificar a data com a função today(), que está no 
submódulo date dentro do datetime.

Com o id do cliente e a data de hoje, criamos o comando para inserir na tabela pedido (variável sql_pedido), 
e por fim executamos a função cursor.execute(sql_pedido, valores). Após inserir o dado, fazemos um 
print com a opção cursor.lastrowid. Essa variável indica qual foi o último id gerado automaticamente, 
visto que a tabela pedido tem o campo id com a opção AUTOINCREMENT.

Antes de chamar o conexao.commit() e conexao.close() para finalizar o programa, vamos permitir 
que o usuário indique quais e quantos itens ele deseja associar ao pedido. Para isso, usamos a 
seguinte rotina logo abaixo da inserção do pedido:
'''
pedido_id = cursor.lastrowid
quantidade_itens = input('quantos itens deseja adicionar?: ')
quantidade_itens = int(quantidade_itens)
for i in range(quantidade_itens):
    produto = input('qual o produto?: ')
    quantidade = input('qual a quantidade?: ')
    quantidade = int(quantidade)
    valor = input('qual o valor?: ')
    valor = float(valor)
    sql_item = '''
    INSERT INTO item_pedido (pedido_id, produto, valor, quantidade)
    values (?, ?, ?, ?)
    '''
    valores = [pedido_id, produto, valor, quantidade]
    cursor.execute(sql_item, valores)
conexao.commit()
conexao.close()
'''
Para inserir o item, a primeira coisa a ser feita é criar uma variável que irá armazenar o id do 
pedido gerado anteriormente, assim criamos a variável pedido_id.

Em seguida perguntamos ao usuário quantos produtos ele deseja adicionar, e convertemos  a resposta 
para inteiro, pois o que retorna da chamada da função input é sempre texto, mesmo que tenha se 
digitado um valor numérico. Para isso, basta passar a variável dentro da função int.

Com a quantidade de itens definida, vamos fazer um for utilizando a função range: ela recebe um 
valor numérico e retorna uma lista que começa com zero e tem quantidade de números pelo valor indicado, 
como no exemplo:

range(5) – [0, 1, 2, 3, 4]

range(10) – [0, 1, 2, 3, 4, 5,6, 7, 8, 9]

Assim, caso o usuário tenha indicado dois itens, vamos perguntar duas vezes o nome do produto, 
a quantidade e o valor para fazer a inserção de tais itens. Na linha 74 fazemos a conversão da quantidade 
para inteiro também e, na linha 76, convertemos para um número flutuante, que é o valor numérico que aceita 
casas decimais. Por fim fazemos a inserção do item, passando o pedido_id, produto, quantidade e valor.

Após esse código, finalizamos com a chamada do conexao.commit() e o conexao.close().

Ao rodar esse programa iremos encontrar algo assim:

insira os dados do pedido:
qual o ID do cliente?: 1
ID do pedido: 1
quantos itens deseja adicionar?: 2
qual o produto?: penela de pressao
qual a quantidade?: 1
qual o valor?: 50
qual o produto?: faca afiada
qual a quantidade?: 2
qual o valor?: 15.50

Como foi indicado que seriam dois itens, as perguntas sobre o produto, quantidade e valor 
foram realizadas duas vezes. Uma observação interessante é que no valor do segundo item (Faca Afiada) 
o valor está utilizando ponto como separador da casa decimal e não vírgula; isto acontece porque é o 
padrão da linguagem Python.
'''