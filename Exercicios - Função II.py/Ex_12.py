'''Crie uma função chamada "calcular_raiz_quadrada" que
calcula a raiz quadrada de um número sem utilizar a
função de raiz quadrada embutida do Python (math.sqrt).
A função deve retornar o resultado com uma precisão de
duas casas decimais.'''

def raiz_quadrada(numero):
    raiz=numero**0.5
    print(f"{raiz}.2f")

import math
def raiz_Quadrada(num):
    r=math.sqrt(num)
    print(f"{r}.2f")