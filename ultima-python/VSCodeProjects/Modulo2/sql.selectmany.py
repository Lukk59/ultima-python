'''
CREATE TABLE categoria (

id INTEGER NOT NULL PRIMARY KEY AUTO AUTOINCREMENT,

nome VARCHAR(100)

);


CREATE TABLE produto (

id INTEGER NOT NULL PRIMARY KEY AUTO AUTOINCREMENT,

nome VARCHAR(100),

categoria_id INT NOT NULL,

CONSTRAINT produto_fk FOREIGN KEY (categoria_id) REFERENCES categoria(id)

);
Obs: Lembrando que a opção AUTOINCREMENT indica que a colina id será gerada automaticamente 
sempre que um dado for inserido, isto é, não precisamos indicar o valor dessa coluna ao inserir 
dados com o comando INSERT.
'''
'''
SELECT p.id, p.nome, c.nome as categoria

FROM produto as p, categoria as c

WHERE p.categoria_id = c.id

O “as” — também conhecido como um “alias” —, além de ser útil para a realização de 
consultas em mais de uma tabela, serve também para renomear a descrição da coluna no 
resultado da consulta, como no caso:

c.nome as categoria

Neste caso, utilizamos o “as” para que a coluna contendo o nome da categoria fique com o cabeçalho categoria.
'''
'''
Agora que sabemos fazer consultas em mais de uma tabela, podemos realizar 
condições entre elas, como no caso:

SELECT p.id, p.nome, c.nome as categoria

FROM produto as p, categoria as c

WHERE p.categoria_id = c.id and c.nome = ‘Celulares’

Aqui utilizamos a palavra chave "and" para combinar a condição de ligação entre as 
tabelas e o filtro indicando apenas os produtos com o nome da categoria Celulares.
'''