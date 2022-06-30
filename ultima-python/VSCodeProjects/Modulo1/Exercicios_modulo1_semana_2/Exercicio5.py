'''
Crie um programa que calcule o peso ideal de uma pessoa. Para isso utilize as fórmulas da tabela:
Para Homens: (72.7 * altura) – 58
Para Mulheres: (62.1 * altura) – 44.7 


Sua aplicação deve identificar se a pessoa é Homem ou Mulher e então fazer o cálculo apropriado. Deve ser impresso se a pessoa é homem ou mulher, juntamente com o peso ideal calculado.


'''
'''
altura = float(input("Qual sua altura: "))
sexo = input("Qual o seu sexo: ")
sexo = 'm' or 'f'
while sexo == 'm':
    homens = (72.7 * altura) - 58
    print(f"Seu peso ideal é:{homens} ")
while sexo == 'f':
    mulheres = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {mulheres}")
    break
if sexo == "m":
    homens = (72.7 * altura) - 58
    print(f"Seu peso ideal é:{homens} ")
if sexo == "f":
    mulheres = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {mulheres}")

elif sexo != "m" or "f":
    print("Dados invalidos!!!")
Resultado:
'''



sexo = input("Qual o seu sexo: ")
altura = float(input("Qual sua altura: "))

if sexo == 'M':
    homens = (72.7 * altura) - 58
    print(f"Seu peso ideal é:{homens} ")
elif sexo == 'F':
    mulheres = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {mulheres}")
else:
    print("Dados invalidos!!!")