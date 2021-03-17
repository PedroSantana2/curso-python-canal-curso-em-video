'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
'''

#Importando trunc
from math import trunc

#Recebendo valores:
num = float(input('Digite o numero: '))

#Variaveis:
inteiro = trunc(num)

#Resultado:
print('Parte inteira: {}'.format(inteiro))
