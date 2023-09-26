'''Modifique o Programa 4.23 que calcula pi para que este não mais solicite o número de pontos a serem 
gerados, mas gere uma tabela com ao menos 10 valores de pi calculados com números diferentes de pontos. 
Sua tabela deve possuir ao menos 10 valores diferentes. Use range() para gerar os diversos valores de 
entrada da função.'''

import random as r
import math as m

def coordenadas_aleatorias():

    x = r.random()

    y = r.random()

    return x, y

def coordenadas_circulo(x, y):

    return m.hypot(x, y) < 1

def calculo_pi(n):
    conta_circulo = 0

    for _ in range(n):
        x, y = coordenadas_aleatorias()

        if coordenadas_circulo(x, y):
            conta_circulo += 1

    pi = 4 * conta_circulo / n
    erro = m.fabs(pi - m.pi)

    return pi, erro

def main():
    valores_pi = 10
    tabela_pi = []

    for num_pontos in range(1, valores_pi + 1):
        pi, erro = calculo_pi(num_pontos)
        tabela_pi.append((num_pontos, pi, erro))

    print("Pontos | Pi | Erro")
    for linha in tabela_pi:
        print(f"{linha[0]:.2f} | {linha[1]:.2f} | {linha[2]:.4f}")

main()