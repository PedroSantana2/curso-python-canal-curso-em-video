'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
#Recebendo valores:
lado1 = float(input('Digite o primeiro lado do triangulo: '))
lado2 = float(input('Digite o segundo lado do triangulo: '))
lado3 = float(input('Digite o terceiro lado do triangulo: '))

#Confereindo se os valores podem formar um triangulo:
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado2 + lado1):
    print('Pode formar um triangulo!')

else:
    print('Não pode formar um triangulo!')
    