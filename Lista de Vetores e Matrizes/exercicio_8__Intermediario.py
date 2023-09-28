'''
Implemente uma função que retorne a matriz identidade de ordem n.
'''

def matriz_identidade(n):
    matriz = []
    
    for i in range(n):
        linha = [0] * n
        
        linha[i] = 1
        
        matriz.append(linha)
    
    return matriz

ordem = 3
matriz_identidade_3x3 = matriz_identidade(ordem)

for linha in matriz_identidade_3x3:
    print(linha)
