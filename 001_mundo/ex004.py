'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela
'''
a = input('Digite algo: ')
print('É alfanumerico?', a.isalnum())
print('É numerico?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É maiusculas?', a.isupper())
print('É minusculas?', a.islower())
print('So tem espaços?', a.isspace())
print('Está captalizada(maiúsculo e minusculo', a.istitle())
