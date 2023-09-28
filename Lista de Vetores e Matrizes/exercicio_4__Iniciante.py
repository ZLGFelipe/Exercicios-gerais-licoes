'''
Crie uma função que verifique se uma matriz é simétrica.
'''

def e_simetrica(matriz: list) -> bool:
    tam = len(matriz)
    for i in range(tam):
        for j in range(tam):
            if i != j and matriz[i][j] != matriz[j][i]:
                return False
    
    return True


matriz = [
    [1, 2, 4],
    [2, 5, 6],
    [4, 6, 7],
]

print(e_simetrica(matriz))