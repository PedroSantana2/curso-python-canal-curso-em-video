'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
'''
print('=-' * 20)

#Recebendo valores:
nota1 = float(input('Digite a primeira nota do aluno: '))
print('=-' * 20)
nota2 = float(input('Digite a segunda nota do aluno: '))
print('=-' * 20)

#Calculando media:
media = (nota1 + nota2) / 2

#Resultado:
print('A media do aluno foi de: {:.1f}'.format(media))
