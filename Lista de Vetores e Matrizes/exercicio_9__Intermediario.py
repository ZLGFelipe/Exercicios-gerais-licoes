'''
Crie um programa que calcule o determinante de uma matriz 3x3.
'''

def determinante(matriz: list) -> int:
    dp = 1
    ds = 1
    for i, l in enumerate(matriz):
        for j, v in enumerate(l):
            if i == j:
                dp *= matriz[i][j]
            else:
                ds *= matriz[i][j]
    
    return dp - ds

matriz = [
    [1, 2], 
    [3, 4], 
]
print(determinante(matriz))