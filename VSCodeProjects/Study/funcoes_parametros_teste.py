'''meu_nome = input("seu nome: ")
idade = input('idade: ')

def apresentacao(meu_nome, idade):
    meu_nome = input("seu nome: ")
    idade = input('idade: ')
    print('ola', meu_nome, '\nsua idade é:', idade)

def somar_dois_numeros(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def raiz(x, grau=2):
    return x ** (1/grau)
'''
fatorial = 13
numero = 4
def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)