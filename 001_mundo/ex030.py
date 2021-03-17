'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

# Recebendo valores:
num = int(input('Digite um numero: '))

#Se a divisão com 2 for exata, então o número é positivo.
if num % 2 == 0:
    print('O numero é par')

#Caso contrario:
else:
    print('O numero é impar')
    