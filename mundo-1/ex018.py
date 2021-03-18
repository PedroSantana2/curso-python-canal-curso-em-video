'''
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
'''

#Importando math:
import math

#Recebendo informações:
an = float(input('Digite o angulo: '))

#Converter para radianos:
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

#Resultado:
print('Seno: {:.2f}, Cos: {:.2f}, Tang {:.2f}'.format(seno, cos, tan))
