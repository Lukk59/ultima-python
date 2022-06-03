'''
anos_bissextos = {1600, 1732}
anos_nao_bissextos = {1742, 1889}

for ano in anos_bissextos:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'{ano} é bissexto')
    else:
        print('Ano nao é bissexto')


'''



for i in range(2000, 2022, 2): # (star, stop, step):
    ano = i + 1
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'{ano} é bissexto')
    else:
        print(f'{ano} nao é bissexto')