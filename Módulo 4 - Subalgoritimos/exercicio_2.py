'''2- Escreva um programa que imprima uma tabela das raízes quadradas dos números entre 1 e 100,
 com entre 1 e 100, com incrementos de 10. incrementos de 10.'''

 from math import sqrt

def raiz_de_10_em_10():
    for numero in range(1, 101, 10):
        print(f'{numero} = {sqrt(numero):.3f}')