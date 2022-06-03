'''
Exercícios:
1- Crie uma função que, ao receber um número inteiro, retorna se um número  é par ou ímpar (utilizando **kwargs).

2- Crie de forma recursiva uma função que printe do número recebido até o zero.

3- Crie uma função de somatório que some todos os números que a mesma receber (usando *args ).

4- Crie um programa com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

5- Faça um programa com uma função que necessite de um argumento. A função deve retornar o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

6- Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.

7- Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.

8-Crie uma função que receba duas palavras e retorne True caso a primeira palavra seja um prefixo da segunda. Exemplo: ’uf’ é prefixo de ’ufabc’. ’ufabc’ não é prefixo de ’uf’.

'''
'''
1- Crie uma função que, ao receber um número inteiro, retorna se um número  
é par ou ímpar (utilizando **kwargs).

def somar_valores_numericos(*args):
    resultado = 0
    for numeros in args:
        resultado += numeros
        print(resultado)

somar_valores_numericos(1, 2, 3, 4)

def par_ou_impar(*args):
    numero = any
    for numero in args:
        if numero % 2 == 0:
            print(f'{numero} é par')
        else:
            print(f'{numero} é impar')

par_ou_impar(6, 9, 2, 3, 4, 0)
'''


def par_ou_impar(**kwargs):
    print(f'\nkwargs = {kwargs}')
    for i, numero in kwargs.items():
        if numero % 2 == 0:
            print(f'{numero} é par')
        else:
            print(f'{numero} é impar')

par_ou_impar(numero = 6, numero1 = 4, numero2= 5, numero3 = 7)