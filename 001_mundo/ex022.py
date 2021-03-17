'''
 Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

#Recebendo informações:
nome = input('Digite um nome: ')

#Declarando variaveis:
maiusculas = nome.upper()
minusculas = nome.lower()
quantidade_letras = len(nome) - nome.count(' ')
primeiro_nome = len(nome.split()[0])

#Resultado:
print('Seu nome em maiusculas: {}\nSeu nome em minusculas:{}\nSeu nome tem ao todo {} letras\nSeu primeiro nome tem {} letras'.format(maiusculas, minusculas, quantidade_letras, primeiro_nome))
