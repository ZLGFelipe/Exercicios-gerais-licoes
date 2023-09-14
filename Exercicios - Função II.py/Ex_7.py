'''Crie uma função chamada "contar_ocorrencias" que
recebe uma lista de elementos e um elemento específico
como argumentos, e retorna a quantidade de vezes que o
elemento aparece na lista.'''

def contar_ocorrencias(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador