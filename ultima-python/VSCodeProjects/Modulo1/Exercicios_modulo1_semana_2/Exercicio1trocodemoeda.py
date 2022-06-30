'''
 1)O caixa no bar do Sr. João está cheio de diversas moedas. O Sr. João precisa 
fechar o caixa, mas está com dificuldade de fazer os cálculos do tanto de dinheiro que ele possui em moedas.
Enquanto estava organizando ele conseguiu separar as moedas e contar a quantidade delas conforme a tabela:

Moeda:      Quantidade:
5 centavos             35
10 centavos            50
25 centavos            30
50 centavos            15
1 real                 19

 Crie uma aplicação que calcule a quantidade de reais (R$) que o
Sr. João possui moedas no caixa. A aplicação deve imprimir o valor total em reais (R$),
pode-se utilizar ponto flutuante para poder representar o valor com duas casas decimais no momento
que for imprimir na tela o valor.
 Resposta:
 print(f"Moedas de x centavos: {} R$")
'''
centavos_5 = int(input("Informe o numero de moedas de 5 centavos: "))
centavos_10 = int(input("Informe o numero de moedas de 10 centavos: "))
centavos_25 = int(input("Informe o numero de moedas de 25 centavos: "))
centavos_50 = int(input("Informe o numero de moedas de 50 centavos: "))
real_1 = int(input("Informe o numero de moedas de 1 real: "))

resultado1 = (centavos_5 * 0.05)
resultado2 = (centavos_10 * 0.10)
resultado3 = (centavos_25 * 0.25)
resultado4 = (centavos_50 * 0.50)
resultado5 = (real_1 * 1)
total = resultado1 + resultado2 + resultado3 + resultado4 + resultado5

print(f"Moedas de 5 centavos: {resultado1:.2f} R$")
print(f"Moedas de 10 centavos: {resultado2:.2f} R$")
print(f"Moedas de 25 centavos: {resultado3:.2f} R$")
print(f"Moedas de 50 centavos: {resultado4:.2f} R$")
print(f"Moedas de 1 real: {resultado5:.2f} R$") # :05d
print(f"total: {float(total):.2f} R$")