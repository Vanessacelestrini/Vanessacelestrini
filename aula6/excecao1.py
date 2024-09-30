try:
    n1 = int(input("Digite o primeiro numero"))
    print(n1)
    n2 = int(input("Digite o segundo numero"))
    print(n2)

    calculo = n1/n2
    print(calculo)

except valueError:
    print("Digite um valor numerio")

except ZeroDivisionError:
    print("Nao é possivel dividir zero")

except:
    print("Erro Inesperado")
finally:
    print("--------")
    print("Sempre executará ....entrando ou não dentro de uma excessão")




