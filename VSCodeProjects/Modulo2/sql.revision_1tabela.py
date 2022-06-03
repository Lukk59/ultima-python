'''
Agora que conhecemos as principais operações SQL, vamos praticá-las usando Python em vez do DBeaver. 
Para isso, utilizaremos como base de dados um cadastro de clientes e pedidos, com as seguintes tabelas:

Cliente: irá armazenar as informações dos clientes;
Pedido: irá armazenar as informações gerais de um pedido;
Item: irá armazenar as informações de um item associado a um pedido, ou seja, um pedido poderá ter 1 
ou mais itens.

Para começar a nossa aplicação de exemplo, precisamos fazer a conexão com o banco de dados. 
Como visto anteriormente é bem simples realizar esse tipo de conexão:
'''
import sqlite3

conexao = sqlite3.connect('banco.sqlite3')

#Após abrir a conexão e criar o banco, vamos fazer a rotina que cria as tabelas:

sql_cliente = '''
CREATE TABLE cliente (
    id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100),
    cpf TEXT(14) NOT NULL,
    CONSTRAINT client_UN UNIQUE (cpf)
);
'''
cursor = conexao.cursor()
cursor.execute(sql_cliente)
'''
No código acima, criamos a tabela cliente, que terá 3 campos (id, nome e cpf), sendo que o CPF é um campo com restrição 
de unicidade.
Logo abaixo desse código, vamos fazer a rotina para criar a tabela pedido:
'''
sql_pedido = '''
CREATE TABLE pedido (
    id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "data" TEXT(20) NOT NULL,
    client_id INTERGER NOT NULL,
    CONSTRAINT podido_FK FOREIGN KEY (client_id) REFERENCES client(id)
);
'''
cursor.execute(sql_pedido)
'''
Nesta rotina, além do campo id e data, criamos o campo “cliente_id”,  que é o relacionamento da tabela pedido com a tabela 
cliente — afinal, um pedido sempre será feito por um determinado cliente.

Por fim, vamos criar a tabela item_pedido, que serve para indicar quais itens foram solicitados para cada pedido:
'''
sql_item_pedido = '''
CREATE TABLE item_pedido (
    id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    pedido_id INTERGER NOT NULL,
    produto TEXT(100),
    valor REAL,
    quantidade INTERGER,
    CONSTRAINT item_podido_FK FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);
'''
cursor.execute(sql_item_pedido)
'''
A tabela item_pedido tem um relacionamento com pedido (1 para Muitos ou One to Many) através da coluna 
pedido_id. Nessa tabela, o produto é apenas um campo textual (não existe cadastro do produto), e então 
temos os campos valor e quantidade.

Por fim, é necessário fazer o commit e fechar a conexão com o banco de dados:
'''
conexao.commit()
conexao.close()