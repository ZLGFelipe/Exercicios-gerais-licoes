'''
Crie uma função que multiplique uma matriz por um escalar.
'''

def produto_escalar(matriz: list, escalar: int) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] *= escalar 
    
    return matriz
            

matriz = [
    [1, 2, 4], 
    [2, 5, 6], 
    [4, 6, 7],
]
print(produto_escalar(matriz, 5))