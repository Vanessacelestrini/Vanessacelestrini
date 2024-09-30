"""Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até
que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados,
assim como a soma e a média aritmética"""
def atividade_3():
    
    soma = 0
    quantidade = 0

    while True:
        numero = int(input("Digite um número (0 para sair): "))
        if numero == 0:
            break
        soma += numero
        quantidade += 1

    
    if quantidade > 0:
        media = soma / quantidade
        print(f"Você digitou {quantidade} números.")
        print(f"A soma dos números é {soma}.")
        print(f"A média dos números é {media:.2f}.")
    else:
        print("Nenhum número foi digitado.")


atividade_3()
