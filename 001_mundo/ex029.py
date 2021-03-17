'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

#Recebendo informações:
velocidade = int(input('Digite a velocidade do carro(em km): '))

#Se maior que 80:
if velocidade > 80:
    ultrapassou = velocidade - 80
    multa = ultrapassou * 7
    print('Você ultrapassou {:.0f}km do permitido e vai passar uma multa de: {:.2f} reais'.format(ultrapassou, multa))

#Caso contrario:
else:
    print('Voce não ultrapassou a velocidade')
