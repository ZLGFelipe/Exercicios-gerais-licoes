'''Escreva um programa que dada a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] gere a 
lista [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].'''

lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
deslocamento = 5

lista_deslocada = lista_original[deslocamento:] + lista_original[:deslocamento]

print("Lista deslocada:", lista_deslocada)
