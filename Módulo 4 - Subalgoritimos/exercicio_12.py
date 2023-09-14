'''12- Modifique o programa que calcula pi para perguntar diversas vezes pelo número de pontos 
a serem sorteados, calculando pi para cada pedido. O programa deve terminar quando for digitado "0".'''

import random

def calcular_pi(num_pontos):
    pontos_dentro_do_circulo = 0

    for _ in range(num_pontos):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distancia = x**2 + y**2
        if distancia <= 1:
            pontos_dentro_do_circulo += 1

    pi_estimado = 4 * (pontos_dentro_do_circulo / num_pontos)
    return pi_estimado

while True:
    num_pontos = int(input("Digite o número de pontos a serem sorteados (ou 0 para sair): "))

    if num_pontos == 0:
        break

    Pi_estimado = calcular_pi(num_pontos)
    print(f"Aproximação de π com {num_pontos} pontos: {Pi_estimado}")