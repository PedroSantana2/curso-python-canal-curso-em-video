'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

#Importando random:
import random

#Declarando variavel:
numero_aleatorio = random.randint(0, 5)

#Recebendo valor:
numero_jogador = int(input('Digite o numero e veja se você acertou: '))

#Resultado:
if numero_aleatorio == numero_jogador:
    print('Parabens voce acertou!')
    
else:
    print('Voce errou!')
