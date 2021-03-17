'''
Escreva um programa que converta uma temperatura digitada em C para F.
'''

#Recebendo valores:
cel = float(input('Digite a temperatura em celsius: '))

#Convertendo:
fah = (cel * 9/5) + 32

#Resultado:
print('{:.1f} graus celsius equivalem a {:.1f} graus fahrenheit'.format(cel, fah))
