'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

#Recebendo valores:
salario = float(input('Digite o salario do funcionario: R$'))


if salario > 1250:

    #Calculando aumento:
    aumento = salario + (salario * 10 / 100)

    #Resultado:
    print('O aumento foi de: R${}'.format(aumento))
    
else:
    aumento = salario + (salario * 15 / 100)
    print('O aumento foi de 15% agora o salario sera de: R${}'.format(aumento))
