def fazer_big_mac(nome):
    print(f'sanduiche Big Mac {nome}')


def fazer_batata(tamanho):
    print(f'batata {tamanho}')

def preparar_refrigerante(tipo,tamanho):
    print(f'{tipo} {tamanho}')


fazer_big_mac("vanessa")    
fazer_batata("grande")
preparar_refrigerante("coca-cola","media")

def combo_bigmac(nome,tamanho_batata,tipo_refrigerante,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refrigerante,tamanho_refri)

combo_bigmac("mauro","media","coca-cola","grande")
