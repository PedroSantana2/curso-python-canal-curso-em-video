'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m^2
'''

#Recebendo informações:
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

#Calculando area:
area = largura * altura

#Calculando quantidade de tinta necessária:
tinta = area / 2

#Resultado:
print('Pra pintar a parede de {:.2f} m2 você precisara de {:.2f} litros de tinta!'.format(area, tinta))
