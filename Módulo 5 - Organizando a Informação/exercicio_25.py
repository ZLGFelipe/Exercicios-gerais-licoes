'''Escreva um programa que crie uma lista com todos os números entre 100 e 1000 que são divisíveis por 
7 mas não são múltiplos de 3.'''

numeros_divisiveis = []

for numero in range(100, 1001):
    if numero % 7 == 0 and numero % 3 != 0:
        numeros_divisiveis.append(numero)

print(numeros_divisiveis)
