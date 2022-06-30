'''
3- Crie uma função de somatório que some todos os números que a mesma receber (usando *args ).
'''

def soma_de_numeros(*args):
    resultado = 0
    for numeros in args:
        resultado += numeros
        print(resultado)

soma_de_numeros(4, 56, 2, 13, 8, 90)