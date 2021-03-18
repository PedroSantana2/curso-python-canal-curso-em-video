'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

#Importando função do modulo datetime:
from datetime import date

#Recebendo ano:
ano = int(input('Digite o ano: | Digite "0" para considerar o ano atual! '))

#Se digitar zero:
if ano == 0:
    ano = date.today().year
    print(ano)

#Calculando se é bissexto:
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano é bissexto!')

else:
    print('O ano não é bissexto')
