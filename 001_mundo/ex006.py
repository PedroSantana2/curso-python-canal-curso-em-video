'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

#Recebendo numero:
num = int(input('Digite um numero: '))

#Declarando variaveis:
dobro = num * 2
triplo = num * 3
raiz = num ** (1 / 2)

#Resultado:
print('O numero digitado foi: {} \nO dobro é: {} \nO triplo é: {} \nSua raiz quadrada é: {:.2f}'.format(num, dobro, triplo, raiz))
