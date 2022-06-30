'''
Em algumas situações, talvez seja necessário realizar uma busca mais refinada em campos do tipo texto — 
por exemplo, consultas em que queremos verificar se uma determinada coluna contém parte de uma palavra 
ou frase. Para esses casos, utilizamos a opção LIKE em conjunto com o caractere “%”. 
Considerando a tabela de categoria da lição anterior, podemos buscar todas as categorias que começam 
com a letra C:

SELECT id, nome FROM categoria WHERE nome LIKE ‘C%’

O resultado da consulta será:

 id	 nome
 1	 Celulares

Na opção LIKE, o caractere “%” indica que a busca pode corresponder a qualquer sequência de caracteres, 
zero ou mais vezes, isto é, depois da letra “C” pode vir qualquer coisa, inclusive nada.

Um outro exemplo, agora na tabela produto, seria buscar todos os produtos que contenham a letra “e” no 
seu nome. O SELECT ficaria assim:

SELECT id, nome, categoria_id FROM produto WHERE nome LIKE ‘%e%’

O resultado seria o seguinte:

 id	 nome	 categoria_id
 2	 iPhone Y	 1
 3	 Lenovo W	 2

 Nesse caso, colocamos duas vezes o caractere “%”, assim indicamos que antes da letra “e” pode 
 vir qualquer texto (inclusive nada), e depois dela também pode vir qualquer texto.

A opção LIKE é muito útil e amplamente utilizada, entretanto, é preciso tomar cuidado para que a 
consulta não seja muito complexa, pois isso a tornará lenta.  Ela pode ser usada tanto na 
cláusula WHERE do SELECT como na do UPDATE e DELETE.

Ex:
DELETE FROM produto where nome = ‘%o%’
'''