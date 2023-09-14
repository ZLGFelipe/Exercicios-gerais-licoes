'''Escreva um programa que crie uma matriz tridimensional usando o mecanismo de lista por compreensão.'''

dimensão_x = 3
dimensão_y = 3
dimensão_z = 3

matriz = [[[0 for _ in range(dimensão_z)] for _ in range(dimensão_y)] for _ in range(dimensão_x)]

for x in range(dimensão_x):
    for y in range(dimensão_y):
        for z in range(dimensão_z):
            print(f"matriz_3d[{x}][{y}][{z}] = {matriz[x][y][z]}")