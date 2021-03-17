'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um porgrama que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

#Importando random
import random

#Recebendo valores:
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

#Transformando em lista:
lista = [a1, a2, a3, a4]

#Sorteando uma sequencia aleatoria:
random.shuffle(lista)

#Resultado:
print('A ordem de apresentação sera: ')
print(lista)
