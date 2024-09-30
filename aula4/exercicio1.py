""" Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80
km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da
multa, cobrando R$ 5 por km acima de 80 km/h.0 """

velocidade = float(input("digite a velocidade do carro"))
if velocidade  > 80:
    multa = (velocidade - 80)* 5
    print(f'você foi multado! em R$ {multa}')

if velocidade <= 80:
    
    print("Sua velocidade esta ok, boa viagem!")

    