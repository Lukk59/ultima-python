'''
Uma loja de móveis está com dificuldades de calcular algumas condições de pagamento de seus 
móveis. Eles possuem algumas regras e o seu trabalho é implementar uma aplicação que faça os cálculos 
de acordo com as regras:

Regras:

À vista em dinheiro, recebe 15% de desconto

À vista no cartão de crédito, recebe 10% de desconto

Em duas vezes, preço normal de etiqueta sem juros

Mais de duas vezes, preço normal de etiqueta mais juros de 10%

O programa deve ter uma variável com o valor de etiqueta do produto, uma variável 
com forma de pagamento e uma com o preço final após a aplicação de uma das regras.

Resultado:
'''
valor_etiqueta = float(input('Qual o valor do produto em R$: '))
forma_de_pagamento = input('Qual a forma de pagamento: ')

if forma_de_pagamento == "a vista em dinheiro":
    vt1 = valor_etiqueta - (valor_etiqueta * 0.15)
    print(vt1)
elif forma_de_pagamento == 'a vista no cartão de credito':
    vt2 = valor_etiqueta - (valor_etiqueta * 0.10)
    print(vt2)
else:
    if forma_de_pagamento == 'em duas vezes':
        print(valor_etiqueta)
    elif forma_de_pagamento == "mais de duas vezes":
        vt3 = valor_etiqueta * 1.10
        print(vt3)
    else:
        print("error, error, error, self destruct initiated!")
