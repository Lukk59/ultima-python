altura = float(input("digite a sua altura(m): "))
peso = float(input("digite o seu peso(kg): "))

imc = peso / (altura ** 2)

print(f"o seu imc é: {imc:.2f}")


if imc < 18.5:
    print('abaixo do peso')
elif imc <= 24.9:
    print('peso normal')
elif imc <= 29.9:
    print('pré obesidade')
elif imc <= 34.9:
    print('obesidade grau 1')
elif imc <= 39.9:
    print('obesidade grau 2')
else:
    print('obesidade grau 3')
