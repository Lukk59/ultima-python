''' SELECIONA TODOS:
SELECT * FROM selecao; 
        OU
SELECT id, nome, titulos, confederacao FROM selecao; 
    SELECIONA ESPECIFICO:
SELECT id, nome, titulos, confederacao FROM selecao WHERE confederacao = ‘uefa’
        TB
SELECT id, nome, titulos, confederacao FROM selecao WHERE id = 1
'''

import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = 'SELECT id, nome, titulos, confederacao FROM selecao WHERE titulos >= 4'
resultados = cursor.execute(sql)
for resultado in resultados:
    print(resultado)
print('FIM DO PROGRAMA')
conexao.close()
'''
''and'': para os casos em que se deseja que o resultado se encaixe em duas
ou mais condições obrigatoriamente; ex:

SELECT id, nome, titulos, confederacao FROM selecao WHERE confederacao = ‘uefa’ and titulos > 3

''or'': para os casos em que o resultado se encaixe em uma ou outra condição,
ou seja, só precisa atender a uma condição. ex:

SELECT id, nome, titulos, confederacao FROM selecao WHERE confederacao = ‘uefa’ or titulos > 3

Por fim, indicamos se é ASC (ascendente/crescente) ou DESC (descendente/decrescente):

SELECT id, nome, titulos, confederacao FROM selecao ORDER BY nome ASC

Um outro exemplo seria ordenar pelo número de títulos, mas indicando uma condição:

SELECT id, nome, titulos, confederacao FROM selecao WHERE titulos > 0 ORDER BY titulos DESC
'''