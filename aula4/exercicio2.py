'''Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
'''

# Solicita ao usuário que digite o salário
salario = float(input("Digite o seu salário: R$ "))

# Verifica se o salário é maior que 1.250,00
if salario > 1250.00:
    aumento = salario * 0.10  # Calcula o aumento de 10%
else:
    aumento = salario * 0.15  # Calcula o aumento de 15%

# Calcula o novo salário
novo_salario = salario + aumento

# Exibe o aumento e o novo salário
print(f"Você teve um aumento de R$ {aumento:.2f}")
print(f"Seu novo salário é R$ {novo_salario:.2f}")


 # salario = float(input("digite o valor do salario funcionario"))
#if salario <= 1250 :
  #  salario = salario + (salario * 15) /100
#    salario = salario * 1.15
    #print(f'ovalor do novo salario é R${salario}')

#else:
#    salario = salario 1.1
#    print(f'o valor do novo salario é R$ {salario}') 

