'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
#Recebendo valores:
km = int(input('Digite a distancia em quilometros: '))

#Se for menor ou igual a 200Km
if km <= 200:
    preco = km * 0.50
#Caso contrario:
else:
    preco = km * 0.45

#Resultado:
print('O preço da passagem vai ser de: {:.2f} reais'.format(preco))
