"Elabore um fluxograma que calcule e exiba a media de 500 numeros fornecidos pelo usuario"
soma = 0
contador = 1

while contador <= 500:
    numero = float(input("Digite o número {} de 500: ".format(contador)))
    soma += numero
    contador += 1

media = soma / 500
print("A média dos 500 números é:", media)
