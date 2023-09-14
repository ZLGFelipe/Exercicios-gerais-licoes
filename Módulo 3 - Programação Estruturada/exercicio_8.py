'''8- Sabendo que um triângulo é dito equilátero quando tem 3 lados iguais, isósceles quando tem 2 
lados iguais e escaleno quando todos os lados têm tamanhos diferentes, escreva um programa que receba 
os valores dos três lados de um triângulo e imprima se ele é equilátero, isósceles ou escaleno.'''

lado1 = float(input('Insira o valor do primeiro lado: '))
lado2 = float(input('Insira o valor do segundo lado: '))
lado3 = float(input('Insira o valor do terceiro lado: '))
if lado1 == lado2 == lado3:
    print('O triângulo é equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')