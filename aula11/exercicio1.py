"tendo como dados de entrada a altura e o sexo de uma pessoa (M masculino e F feminino)"
"construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:"
"para homens (72.7*h) -58"
"para mulheres(62.1*h) -44.7"


#Digite valor da altura
altura = float(input('Qual a sua altura:'))
#Digite o sexo F Feminino M masculino
sexo = input('Qual o seu sexo (F/M:')

#calculo do peso ideal

if (sexo =='M'):
    peso = (72.7*altura)-58

else:
    peso = (62.1*altura)-44.7

print('o seu pedo ideal é', peso)

