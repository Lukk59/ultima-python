'''
Em um banco de dados é possível também realizar consultas com funções agregadoras, isto é, 
consultas nas quais o resultado final é um cálculo feito em cima de um conjunto de dados. 
Os exemplos mais comuns são:

COUNT: contabiliza o número de linhas numa determinada coluna;

SUM: somar todos os valores de uma determinada coluna;

MIN e MAX: calcula o valor mínimo e máximo de uma determinada coluna;

AVG: calcula a média dos valores de uma determinada coluna.

Ex: Tabela transacoes:


CREATE TABLE transacoes (

id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

descricao TEXT(50),

valor INTEGER NOT NULL

);

 id	 descricao	 valor
 1	 pizzaria italiana	 120
 2	 pix para maria	 250
 3	 NULL	 110
 4	 Boleto energia	 320
A linha com id 3 está com a descrição NULL, isto é, o dado a ser salvo não teve a sua descrição informada — 
nesse caso, essa coluna aceita valores nulos.

Agora vamos aos exemplos de consultas:

1 – Para contar quantos registros existem:

SELECT COUNT(id) FROM transacoes

R: COUNT(id) = 4

Na cláusula SELECT, é indicado apenas o COUNT(id), ou seja, esta é a única informação que deseja-se resgatar. 
Ela é utilizada com parênteses, dentro do do qual insere-se a coluna que deseja-se contar. 
Como a coluna id é a chave primária — e, por isso, uma coluna obrigatória —, temos a certeza de que 
esse campo estará em todas as linhas, e assim temos o total de registros da nossa tabela.

Se, em vez de usar a coluna id, usarmos a coluna descricao, o comando e o resultado seriam os seguintes:

SELECT COUNT(descricao) FROM transacoes

R: COUNT(descricao) = 3

O resultado dessa contagem é 3, pois uma das linhas contém a coluna descricao nula, e assim essa 
linha não é contabilizada.

2 – caso se deseje somar o valor das transações:

SELECT SUM(valor) FROM transacoes

R: SUM(valor) = 800

Bastante similar ao COUNT, o SUM também necessita que se indique com qual coluna a soma deverá ser realizada. 
Para que o resultado da consulta fique mais “elegante” e exiba uma descrição melhor do que “SUM(valor)”, é 
possível utilizar o as (alias) assim:

SELECT SUM(valor) as total_valor FROM transacoes

R: total_valor = 800

Neste exemplo, o cabeçalho que identifica a soma da coluna valor fica com o texto total_valor.

3 – caso se deseje saber o menor e maior valor das transações:

As funções agregadoras também podem ser utilizadas juntas. Por exemplo, caso se queira saber, 
em uma mesma consulta, o menor e maior valor entre as transações:

SELECT MIN(valor) as ‘Menor Valor’, MAX(valor) as ‘Maior Valor’ FROM transacoes

R: Menor Valor = 110; Maior Valor = 320

No exemplo acima, além das duas funções agregadoras em uma mesma consulta (MIN e MAX), utilizamos o as, 
e a descrição do cabeçalho entre aspas simples. O “as” é necessário em cabeçalhos com mais de um palavra, 
ou seja, que contenham espaços em sua nomenclatura.

4 – caso se deseje saber a média do valor das transações:

Por fim, temos a função AVG, que indica a média dos valores de uma coluna. Um exemplo seria:

SELECT AVG(valor) as ‘Média do Valor’ FROM transacoes WHERE valor < 300

R: Média do Valor = 160

Para o exemplo de AVG, acrescentamos a cláusula WHERE, indicando que a aplicação dessas funções agregadoras 
também podem ter filtros, como nas consultas anteriores.

Ex: SELECT SUM(id) as ‘Soma dos IDs’ FROM transacoes
'''