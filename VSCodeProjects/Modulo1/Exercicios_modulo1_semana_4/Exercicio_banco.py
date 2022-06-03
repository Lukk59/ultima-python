'''
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar 
um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
Exemplos:

Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e
 1 nota de R$ 10,00.
'''
def banco_tal():
    o_valor = int(input('informe o valor a ser sacado em R$: '))
    cedulas = 100
    total_de_cedulas = 0
    if o_valor <= 9:
        print('não foi possivel.')
    else:
        while True:
            if o_valor >= cedulas:
                o_valor -= cedulas
                total_de_cedulas += 1
            else:
                if total_de_cedulas > 0:
                    print(f'Dar {total_de_cedulas} cedulas de {cedulas} R$')
                if cedulas == 100:
                    cedulas = 50
                elif cedulas == 50:
                    cedulas = 20
                elif cedulas == 20:
                    cedulas = 10
                total_de_cedulas = 0
                if o_valor == 0:
                    print('Obrigado por escolher o banco tal.')
                    break
                elif o_valor == (1, 2, 3, 4, 5, 6, 7, 8, 9): #nao funciona e nao acho um jeito de escluir
                    print('não foi possivel completar')
                    break
banco_tal()