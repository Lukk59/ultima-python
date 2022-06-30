'''
 Alguns alunos de uma universidade criaram uma “criptografia” para se comunicarem entre eles durante o 
tempo que estão longe da universidade. Essa criptografia é baseada em códigos que, quando convertidos, 
formam as letras de uma palavra. Esses números são informados em uma lista de caracteres e são separados 
pela string ‘-1’ conforme o exemplo abaixo:

 sequencia = {'7', '9', '-1', '7', '3', '-1'}

Nessa sequência teríamos o número 79 representando um caractere e o número 73 representando 
outro caractere da mensagem. Para saber a letra será necessário percorrer essa lista e ir concatenando 
os números antes de identificar um separador (‘-1’) para então identificar qual letra o código numérico 
representa. Por exemplo:
1) A primeira iteração da lista será lido o primeiro número ‘7’, adicionamos ele em uma variável 
(sugestão de nome: codigo_letra),
2) Na segunda interação será lido o número ‘9’ que será concatenado na mesma variável variável 
(usando o += com strings)
3) Na terceira iteração iremos identificar que é o caractere que separa as letras da mensagem, 
converter o código numérico para uma letra usando o código: palavra += chr(int(codigo_letra)) 
(esse código utiliza funções, iremos estudar mais a respeito ao longo do curso). Após converter 
a variável deve ser limpa para que possamos continuar a ler as demais letras.
4) Será repetido todos os passos acima para a segunda letra

Para o exemplo acima, a primeira letra é o caractere “O” e a segunda letra será o caractere “I” 
formando a palavra “OI”.
Sua tarefa será criar uma aplicação que percorra a sequência:
mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', 
'-1', '6', '5', '-1']
Faça a concatenação dos códigos numéricos conforme o exemplo acima e ao final imprima qual a palavra formada. 
Após fazer a aplicação, pesquise por códigos ASCII 😉

Resposta:
chr('o')

ord('o')
'''

sequencia = {'7', '9', '-1', '7', '3', '-1'}

codigo_letra = "o"
# += chr(int(codigo_letra))
for number in sequencia:
    if Number == '-1':
        print(' ')
    elif sequencia == chr(int(codigo_letra)):
        print(chr(int(codigo_letra)))
    else:
        break
