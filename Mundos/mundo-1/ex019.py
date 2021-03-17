'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

#Importando random:
import random

#Recebendo informações:
a1 = input('Digite o primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
a4 = input('Digite o quarto aluno: ')

#Transformando em uma lista:
lista = [a1, a2, a3, a4]

#Escolhendo um objeto aleatorio dentro da lista:
escolhido = random.choice(lista)

#Resultado:
print('O escolhido foi: {}'.format(escolhido))
