'''
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

#Recebendo valor:
num = int(input('Digite o numero: '))

#Declarando variaveis:
antecessor = num - 1
sucessor = num + 1

#Resultado:
print('Seu sucessor é: {}\nNumero digitado: {}\nSeu antecessor é {}'.format(sucessor , num, antecessor))
