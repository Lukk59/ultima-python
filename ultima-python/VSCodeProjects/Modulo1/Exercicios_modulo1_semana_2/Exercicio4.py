'''
 Crie um programa que possua as variáveis A, B e C. Imprima o resultado de A + B caso ele 
seja menor do que C, caso contrário imprima que o valor é menor. Teste a aplicação com alguns 
valores nas variáveis sugeridas.

a = int(input("Qual o valor de A: "))

Resultado:
'''
a = int(input("Qual o valor de A: "))
b = int(input("Qual o valor de B: "))
c = int(input("Qual o valor de C: "))

total = a + b
if total < c:
    print(f"Valor de A+B: {total}")
else:
    print("O valor é menor")