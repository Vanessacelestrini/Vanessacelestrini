"Elabore um script que solicite o nome de um aluno e duas notas."
"Em seguida calcule e imprima a media e mostre se o aluno foi aprovado ou reprovado, Para estar aprovado a media tem de ser acima de 6,5"
"Faca isso para quantidade digitadas de  alunos" " pedir todos alunos e notas e no final fazer a listagem "

alunos = []

num_alunos = int(input("Digite o número de alunos: "))

for i in range(num_alunos):
    nome_aluno = input(f"Digite o nome do aluno {i + 1}: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    media = (nota1 + nota2) / 2 
    
    status = "Aprovado" if media >= 6.5 else "Reprovado"
    
    aluno_info = {
        'nome': nome_aluno,
        'nota1': nota1,
        'nota2': nota2,
        'media': media,
        'status': status
    }
    
    alunos.append(aluno_info)

for aluno in alunos:
    print(f"{aluno['nome']}: Média: {aluno['media']:.2f} - {aluno['status']}")