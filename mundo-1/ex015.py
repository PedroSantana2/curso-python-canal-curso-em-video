'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
'''

#Recebendo valores:
dias = int(input('Digite a quantidade de dias que você andou com o carro: '))
km = float(input('Digite quantos km o você andou com o carro: '))

#Calculando valores das variaveis:
valor_dia = dias * 60
valor_km = km * 0.15
valor_total = valor_dia + valor_km

#Resultado:
print('A valor cabrado pelos dias foram de R${:.2f} \nO valor cobrado pelos km rodados foi de: R${:.2f} \nAo total você ira pagar: R${:.2f}'.format(valor_dia, valor_km, valor_total))
