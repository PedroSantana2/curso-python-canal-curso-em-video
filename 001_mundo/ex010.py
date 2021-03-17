'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''
#Recebendo valores:
din = float(input('Digite a quantidade de reais que você tem na carteira: R$'))

#Convertendo:
dol = din / 3.27

#Resultado:
print('Com {:.2f} reais você pode comprar {:.2f} dolares'.format(din, dol))
