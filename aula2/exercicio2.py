# Solicita o valor do salário ao usuário
salario = float(input("Digite o valor do salário: R$ "))

# Solicita a porcentagem de aumento ao usuário
percentual_aumento = float(input("Digite a porcentagem de aumento: "))

# Calcula o valor do aumento
aumento = salario * (percentual_aumento / 100)

# Calcula o novo salário
novo_salario = salario + aumento
# Exibe o valor do aumento e o novo salário
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
