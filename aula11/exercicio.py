"Elabore um programa que calcule quantas notas de 50, 10 e 1 são necessárias para se pagar uma conta cujo valor é fornecido"

#Digite o valor da conta
def valor_conta():
    valor = float(input("Digite o valor da conta"))
    return valor

#calcule quantas notas de 50, 10 e 1 sao necessarias

def calcular_notas(valor):
    notas_50 = int(valor / 50)
    valor %= 50

    notas_10 = int(valor / 10)
    valor %= 10
    
    notas_1 = int(valor / 1)
    valor %= 1

    return notas_50, notas_10, notas_1
    
#exibir o resultado

def exibir_resultado(notas_50, notas_10, notas_1):
    print(f"notas 50:{notas_50}")
    print(f"notas 10:{notas_10}")
    print(f"notas 1:{notas_1}")

def obter_valor():
    valor = valor_conta()
    notas_50, notas_10, notas_1 = calcular_notas(valor)
    exibir_resultado(notas_50, notas_10, notas_1)

if __name__ == "__main__":
    obter_valor()