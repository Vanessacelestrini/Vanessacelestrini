"""
r - read
a - append - inserir registro
w - write escrita
x - criar aquivo
rw - leitura de escrita

"""
# open ("caminho", modo de abertura)
#arquivo = open ("texto.txt","r")
arquivo = open("texto.txt","r")

#RETORNA SE O ARQUIVO PODE SER LIDO
print(arquivo.readable())


#IMPRIMI OS DADOS DO ARQUIVO CHAMADO ARQUIVO
print(arquivo.read())
print("bom dia!")
print("bom\n dia!")
