quantidade = int(input('quantidade: '))
preco = float(input('preço: '))

valor_total = quantidade * preco
print(f'valor total: {valor_total:.2f} R$')

if valor_total > 5000.0:
    valor_com_desconto = valor_total * 0.9
    print(f'valor com desconto de 10%: {valor_com_desconto:.2f} R$')
