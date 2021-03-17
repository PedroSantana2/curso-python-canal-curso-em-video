'''
Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada 
'''

#Recebendo informações:
numero = int(input('Digite um numero: '))

#Declarando variaveis:
a = 0

print('-' * 20)

#Iniciando loop de 0 atá 10
while a < 11:
    print('{} x {:2} = {}'.format(numero, a, (numero * a)))
    a += 1
