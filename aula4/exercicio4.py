#solicito o usoario para digitar um numero
numero = float(input("digite um numero para tabuada de 10"))
# inicializo o numero
i = 1

#estrutura de repetição

while i <= 10:
    aux = i * numero
    print(i ,"x" ,numero , "= ",aux)
    i = i + 1
