'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

#Recebendo valor:
nome = str(input('Digite seu nome: ')).strip()

#Variaveis:
#Coloca tudo em maiusculo e dividi a string de acordo com os espaços:
dividir = nome.upper().split()

#Retorna valor boleano:
resultado = bool('SILVA' in dividir)

#Resultado:
print('Você tem Silva no nome? {}'.format(resultado))
