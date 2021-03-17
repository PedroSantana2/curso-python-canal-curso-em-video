'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

#Recebendo valores:
salario = float(input('Digite o salario do funcionario: R$'))

#Calculando aumento:
aumento = salario + (salario * 15 / 100)

#Resultado:
print('O salrio do funcionario passou de {} reais para {} reais.'.format(salario, aumento))
