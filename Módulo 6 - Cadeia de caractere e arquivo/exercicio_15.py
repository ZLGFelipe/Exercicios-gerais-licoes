'''
Escreva um programa que guarde os pontos gerados pelo Programa 4.16 em um arquivo, um ponto por linha.
Ao final, escreva nesse arquivo o resultado do cálculo para pi.
'''

import math
import random

nome_arquivo = 'pontos.txt'
arquivo = open(nome_arquivo, 'w')


def gera_coordenadas_aleatorias():

    x = random.random()

    y = random.random()

    return x, y


def coordenadas_dentro_circulo(x, y):

    return math.hypot(x, y) < 1


def calcula_pi(n):

    conta_circulo = 0

    for i in range(n):

        x, y = gera_coordenadas_aleatorias()

        if coordenadas_dentro_circulo(x, y):

            conta_circulo += 1

    pi = 4 * conta_circulo / n

    erro = math.fabs(pi - math.pi)

    arquivo.write("\nPonto X:")
    arquivo.write(str(x))
    arquivo.write("\nPonto Y:")
    arquivo.write(str(y))
    arquivo.write("\nCom o Valor de pi sendo: ")
    arquivo.write(str(pi))

    return pi, erro


while True:
    num = int(input('Quantos pontos devem ser sorteados? (Digite 0 para sair): '))

    if num == 0:
        print("Programa encerrado.")
        break

    pi, erro = calcula_pi(num)
    print('Com', num, 'pontos, o valor de pi é', pi, 'com erro', erro)
