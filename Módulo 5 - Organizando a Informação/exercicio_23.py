'''Use os comandos desta seção para inverter os elementos da primeira metade de uma lista. Por exemplo, 
se a lista é lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use os comandos para 
obter [4, 3, 2, 1, 0, 5, 6, 7, 8, 9].'''

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

primeira_metade = lista[:len(lista)//2]
segunda_metade = lista[len(lista)//2:]

primeira_metade = primeira_metade[::-1]
lista = primeira_metade + segunda_metade

print(lista)
