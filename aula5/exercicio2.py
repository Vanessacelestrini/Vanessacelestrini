"""
Escreva um programa que leia dois numeros e que pergunte qual operacao voce deseja realizar voce deve calcular
soma (+) , subtracão (-), multiplicacao(*) e divisao (/)
exiba o resultado da operacao solicitada
"""

# entrada
num1 = int(input("digite o primeiro numero para calculo. "))
num2 = int(input("digite o numero. "))
operacao = input("deseja realizar a soma(+) , subtracão(-), multiplicacao(*) e divisao(/) ")



#processamento
if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2 

elif operacao == "/":
    resultado = num1 / num2

else:
    print("operacao invalida")
    resultado = 0
    print("resultado : ", resultado)        
