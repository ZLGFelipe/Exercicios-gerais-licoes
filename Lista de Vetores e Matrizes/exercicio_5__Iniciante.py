'''
Crie um programa que calcule a média dos elementos de uma matriz.
'''

def media_matriz(matriz: list) -> float:
    qtd = 0
    soma = 0
    
    for linha in matriz:
        soma += sum(linha)
        qtd += len(linha)
    
    media = soma / qtd
    return media


matriz = [
    [1, 2, 4], 
    [2, 5, 6], 
    [4, 6, 7]
]

print(media_matriz(matriz))