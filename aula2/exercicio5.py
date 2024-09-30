# Solicita a temperatura em graus Celsius
temperatura_celsius = float(input("Digite a temperatura em ºC: "))

# Converte a temperatura para Fahrenheit usando a fórmula
temperatura_fahrenheit = (9 * temperatura_celsius / 5) + 32

# Exibe a temperatura convertida em Fahrenheit
print(f"A temperatura em ºF é: {temperatura_fahrenheit:.2f}")
