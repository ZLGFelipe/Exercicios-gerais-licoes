'''11- Escreva uma função distancia(x1, y1, x2, y2) que devolva a distância entre dois pontos 
cujas coordenadas cartesianas são (x1, y1) e (x2, y2).'''

import math

def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distancia = math.sqrt(dx**2 + dy**2)
    return distancia

x1, y1 = 0, 0
x2, y2 = 3, 4
resultado = distancia(x1, y1, x2, y2)
print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é {resultado:.2f}")