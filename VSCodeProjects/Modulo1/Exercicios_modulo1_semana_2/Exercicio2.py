'''
 Um freelancer está com dificuldade para calcular qual o valor cobrar por um projeto que está estimado
em 80 horas. Após pensar e revisitar o preço de alguns projetos que cobrou no passado ele montou a seguinte 
fórmula: valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado. 
 Sua tarefa é criar um programa que faça essa conta para o freelancer. Considere que o valor inicial sempre 
será 1000,00 R$ e o valor da hora cobrada é de 20,45 R$. A aplicação deve imprimir o valor calculado pelo 
projeto considerando duas casas decimais na formatação do valor. Dica: Olhar a ordem como as operações da 
fórmula devem ser realizadas.


Resposta:
'''
valor_inicial = 1000
valor_da_hora = 20.45
quantidade_de_horas = int(input("Quantas horas de trabalho estimadas: "))

formula = (valor_inicial + (valor_da_hora * quantidade_de_horas))
porcentagem = (formula * 0.15)
total = formula + porcentagem

print(f"Horas: {quantidade_de_horas}")
print(f"procentagem calculada: {porcentagem}")
print(f"Valor do projeto {float(total)} R$")