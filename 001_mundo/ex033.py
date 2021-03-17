'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

#Recebendo valores:
numero1 = int(input('Digite o primeiro valor '))
numero2 = int(input('Digite o segundo valor '))
numero3 = int(input('Digite o terceiro valor '))

#Transformando em uma lista:
lista = [numero1, numero2, numero3]

#Colocando em ordem:
ordenados = sorted(lista)

#Variaveis:
menor = ordenados[0]
maior = ordenados[2]

#Resultado:
print('O menor numero é: {}'.format(menor))
print('O maior numero é: {}'.format(maior))
