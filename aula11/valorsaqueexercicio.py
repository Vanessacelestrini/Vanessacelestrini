"Elabore um programa que calcule quantas notas de 50, 10 e 1 são necessárias para se pagar uma conta cujo valor é fornecido"

resposta = 'S'
while resposta =='S':

    valor = int(input('Qual valor para saque'))


    n50 = valor // 50
    n10 = (valor % 50) // 10
    n1 = (valor % 50) % 10

    print('notas de 50 ', n50)
    print('Notas de 10 ', n10)
    print('Moedas de 1 ', n1)

    resposta = input('Deseja fazer outro saque(S/N)')

   