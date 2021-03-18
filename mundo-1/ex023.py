'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

#Recebendo valor:
numero = int(input('Digite um numero entre 0 e 9999: '))

#Declarando variaveis:
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

#Resultado:
print('Analisando o numero {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
