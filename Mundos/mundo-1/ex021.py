'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

#Importando pygame:
import pygame

#Iniciando pygame:
pygame.init()

#Usando mixer do pygame:
#Selecionando audio:
pygame.mixer.music.load('ex021uepa.mp3')

#Iniciando o audio:
pygame.mixer.music.play()

#Fim do programa:
input()
