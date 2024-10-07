"criar uma função para ler os valores while"
def calcularMedia(n1, n2):
    media = (n1 + n2)/2
    return media

def imprimirAlunos(alunos):
    for aluno in alunos:
            print(aluno['nome'],'(media: ',aluno['media'], ' - ',aluno['resultado'],')')

resposta = int(input('Quantos alunos para calcular? '))

i = 0
alunos = []

while i < resposta: 
    nomeAluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota2: '))
    media = (nota1 + nota2)/2
    resultado = "Aprovado"  if media >= 6.5 else "Reprovado"
  
    alunos.append(
        {
           'nome': nomeAluno,
           'nota1': nota1,
           'nota2': nota2,
           'media': media,
           'resultado': resultado
        }
   )
    
    i = i + 1

imprimirAlunos(alunos)
    
