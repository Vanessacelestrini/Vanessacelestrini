'''Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,45 para viagens mais longas.
'''
# Distancia do Percurso do passageiro Km
Percursokm = float(input("Percurso em Km"))

# Verifique o preco da passagem, cobrando R$ 0,50 por Km viajens de ate 200km e 0,45 viagens mais longas

if Percursokm <= 200:
    tarifa = Percursokm * 0.5

if Percursokm > 200:
       tarifa = Percursokm * 0.45 

# calcule a nova tarifa
print(f"sua tarifa é de R$ {tarifa}")

'''
  
km = float(input("Digite a distância percorrida"))

if km <= 200:
    passagem =  0.5 * km
   
else:
    passagem =  0.45 * km
print(f'O valor a pagar por percorrer a distância de {km} é  R${passagem}')    

'''
