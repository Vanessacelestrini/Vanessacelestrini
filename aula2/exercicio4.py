# Solicita a distância a percorrer em quilômetros
distancia = float(input("Digite a distância a percorrer (em km): "))

# Solicita a velocidade média esperada em quilômetros por hora
velocidade_media = float(input("Digite a velocidade média esperada (em km/h): "))

# Calcula o tempo de viagem
tempo_viagem = distancia / velocidade_media

# Exibe o tempo de viagem em horas
print(f"Tempo estimado de viagem: {tempo_viagem:.2f} horas")
