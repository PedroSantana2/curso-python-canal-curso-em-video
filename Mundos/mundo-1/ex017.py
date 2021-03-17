'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

#Importando modulo math
import math

#Recebendo valores:
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

#Declarando variaveis:
hipotenusa = math.hypot(co, ca)

#Resultado:
print('A hipotenusa vai medir: {:.2f}'.format(math.hypot(co, ca)))
