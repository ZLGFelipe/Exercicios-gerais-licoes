'''Modifique o Programa 4.16 de modo que a função que gera coordenadas aleatórias receba como parâmetro o 
número de coordenadas que precisam ser geradas e devolva uma lista de tuplas com essas coordenadas. 
Deste modo, a função que calcula o valor de pi também precisa ser modificada para tratar essas coordenadas 
em forma de lista de tuplas.'''

import random as r
import math as m


def coordenadas_aleatorias(n):

    coordenadas = [(r.random(), r.random()) for _ in range(n)]

    return tuple(coordenadas)


def coordenadas_circulo(x, y):

    return m.hypot(x, y) < 1


def calcula_pi(coord):

    conta_circulo = 0

    for x, y in coord:
        if coordenadas_circulo(x, y):
            conta_circulo += 1

    pi = 4 * conta_circulo / len(coord)
    erro = m.fabs(pi - m.pi)

    return pi, erro


num = int(input('Quantos pontos devem ser sorteados? '))

coord = coordenadas_aleatorias(num)
pi, erro = calcula_pi(coord)

print('Com', num, 'pontos, o valor de pi é', pi, 'com erro', erro)