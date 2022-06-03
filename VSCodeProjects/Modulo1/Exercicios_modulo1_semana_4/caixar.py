'''
else:
            print("Não foi possivel sacar o resto")
            break
'''
valor = int(input("q valor quer: "))
total = valor
cedulas = 50
totalced = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totalced += 1
    else:
        if totalced > 0:
            print(f'total de {totalced} cedulas de R$ {cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalced = 0
        if total == 0:
            break