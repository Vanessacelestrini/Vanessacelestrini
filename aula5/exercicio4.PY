"""Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O
programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela. """

# Contagem regressiva de 10 a 0
#import time
#time.sleep(10)
#print("esperamos 10 segundos")

import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print("Fogo!")


