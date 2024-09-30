"faça um programa que se a idade for maior que 50 anos , a mensagem seja: Fulano tem X anos e é experiente"
"se a idade for menor que 50 anos"
"a mensagem deve ser Fulano tem x anos , está em treinamento"

# Digite a idade

idade = int(input("Digite sua idade:"))

# informe se tem 50 ou +

if idade > 50:
    print(f"Tem {idade} tem experiencia")

else:
      print(f"Tem {idade} está em treinamento")