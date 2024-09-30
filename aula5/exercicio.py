lista = []
while True:
    numero = int(input("digite um numero (0 -sai): "))
    if numero ==0:
        break
    lista.append(numero)

print(lista)

#o while nao pode ser convertido em for poque 
#o numero de repeticoes é desconhecido no inicio
for  i in lista:
    print(i)