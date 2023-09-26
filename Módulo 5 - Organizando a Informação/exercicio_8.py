'''Escreva um programa para gerar uma lista com o quadrado dos números ímpares de 0 a 9, como no 
Programa 5.16, porém não use filtros. Use apenas o comando range() para controlar a geração da sequência 
de números ímpares.'''

quadrado_impar = []

for num in range(10):
    if num % 2 == 1:
        quad = num ** 2
        quadrado_impar.append(quad)

print(quadrado_impar)