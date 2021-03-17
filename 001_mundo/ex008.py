'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

#Recebendo valores:
metros = float(input('Digite o valor em metros: '))

#Declarando variaveis
centimetros = metros * 100
milimetros = metros * 1000

#Informando resultado:
print('{} metros é: \n{} centímetros\n{} milímetros'.format(metros, centimetros, milimetros))
