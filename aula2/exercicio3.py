# Solicita o preço da mercadoria
preco = float(input("Digite o preço da mercadoria: R$ "))

# Solicita o percentual de desconto
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcula o valor do desconto
valor_desconto = preco * (percentual_desconto / 100)

# Calcula o preço a pagar após o desconto
preco_a_pagar = preco - valor_desconto

# Exibe o valor do desconto e o preço a pagar
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")
