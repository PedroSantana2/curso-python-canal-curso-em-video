'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

#Recebendo valores:
frase = str(input('Digite um a frase: ')).strip().upper()

#Declarando variaveis:
quantidade = frase.count('A')
primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1

#Resultados:
print('A quantidade de A na sua frase é de: {}'.format(quantidade))
print('O primeiro A aparece na posição: {}'.format(primeira))
print('A ultima letra A apareceu na posição: {}'.format(ultima))
