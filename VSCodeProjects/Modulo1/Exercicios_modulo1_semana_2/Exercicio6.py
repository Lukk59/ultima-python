'''
 Um nutricionista está precisando de uma ajuda para calcular o IMC de seus pacientes. 
Para calcular o IMC ele passou a seguinte fórmula: IMC = peso / ( altura )². Crie um 
programa que faça o cálculo do IMC de uma pessoa (ele deve ser impresso na tela) e classifique o 
IMC dessa pessoa de acordo com a tabela (também deverá ser impresso):


Valor do IMC             Classificação
Abaixo de 18,5           Pessoa abaixo do peso
Entre 18,5 e 25          Pessoa com peso normal
Entre 25 e 30            Pessoa acima do peso
Acima de 30              Pessoa obesa

Resposta:
'''
peso = float(input('Qual seu peso em kg: '))
altura = float(input('Qual sua altura em cm: '))

IMC = peso / (altura**2)
print(f'Seu IMC é: {IMC}')

if IMC >= 30:
    print("Pessoa obesa.")
else:
    if IMC >= 25:
        print('Pessoa acima do peso.')
    elif IMC >= 18.5:
        print('Pessoa com peso normal')
    else:
        print('Pessoa abaixo do peso')