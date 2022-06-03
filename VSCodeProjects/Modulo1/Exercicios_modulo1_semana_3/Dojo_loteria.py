from random import randint


def randomizador_de_loteria():
    resultado = list()
    while len(resultado) < 6:
        numero = randint(1,60)
        if numero not in resultado:
            resultado.append(numero)
    return resultado


def escolha_de_numero():
    numeros = input("escolha 6 numeros: ")
    lista_de_numeros = numeros.split('-')
    if len(lista_de_numeros) != 6:
        print('sai fora zeca urubu')
        exit()
    return lista_de_numeros

def verificaçao_do_resultado():
    resultado_da_loteria = randomizador_de_loteria()
    numeros_escolhidos = escolha_de_numero()
    numeros_acertados = 0 
    for numeros in numeros_escolhidos:
        if int(numeros) in resultado_da_loteria:
            numeros_acertados += 1
    if numeros_acertados == 6:
        print('vc ganhou')
    else:
        print('perdeu')

verificaçao_do_resultado()