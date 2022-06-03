'''
2- Crie de forma recursiva uma função que printe do número recebido até o zero.

'''

def contador(valor_dado=10):
    while valor_dado >= 0:
        print(valor_dado)
        valor_dado -= 1
    print('fim')

contador(11)
