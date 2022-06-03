'''
7- Escreva uma função que, dado o valor da conta de um restaurante, 
calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.

'''
def valor_do_garçon():
    valor = float(input("qual o valor em reais: "))
    if valor >= 0:
        gorjeta = (valor * 0.10)
        total = gorjeta + valor
        print(f'valor pago em reais: {valor}')
        print(f'valor da gorjetaem rais: {gorjeta}')
        print(f'valor total em reais: {total}')
    else:
        print('valor invalido')

valor_do_garçon()