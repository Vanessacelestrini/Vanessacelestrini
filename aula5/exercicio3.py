"""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para
indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
Tipo	Faixa(Kwh)	Preço
Residencial	Até 500 Acima de 500	R$ 0,40 R$ 0,65  
Comercial	Até 1000 Acima de 1000	R$ 0,55 R$ 0,60 
Industrial	Até 5000 Acima de 5000	R$ 0,70 R$ 0,80
"""

quantidadekw = int(input("Digite a quantidade de KWh Consumida : "))
tipoinstalacao = input("Digite o tipo de Instalação \n I - Industrial \n C - Comercial \n R - Residencial")

if tipoinstalacao == "R" or tipoinstalacao == "r":
    if quantidadekw <= 500:
        precopagar = 0.40        
    else:
        precopagar = 0.65
elif tipoinstalacao == "C" or tipoinstalacao == "c":
    if quantidadekw <= 1000:
        precopagar = 0.55
    else:
        precopagar = 0.60
elif tipoinstalacao == "I" or tipoinstalacao == "i":
    if quantidadekw <= 5000:
        precopagar = 0.70
    else:
        precopagar = 0.80
else:
    precopagar = 0
    print("Erro ! Tipo de Instalação desconhecido")
custo = quantidadekw * precopagar
print(f'O valor a pagar R$ {custo}') 