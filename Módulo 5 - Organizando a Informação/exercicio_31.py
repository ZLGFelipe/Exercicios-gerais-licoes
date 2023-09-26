'''Escreva um programa que crie uma tupla com todos os números entre 100 e 1000 que são divisíveis por 
7 mas não são múltiplos de 3.'''

divisiveis_por_7_nao_multiplos_de_3 = []

for numero in range(100, 1001):
    if numero % 7 == 0 and numero % 3 != 0:
        divisiveis_por_7_nao_multiplos_de_3.append(numero)

tuple_resultante = tuple(divisiveis_por_7_nao_multiplos_de_3)

print(tuple_resultante)
