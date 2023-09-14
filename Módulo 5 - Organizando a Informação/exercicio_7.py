'''Escreva um programa para gerar uma lista com o quadrado dos números pares entre 10 e 20 (inclusive).'''

quadrados_pares = []

for num in range(10, 21):
    if num % 2 == 0:
        quadrado = num ** 2
        quadrados_pares.append(quadrado)

print("Quadrados dos números pares entre 10 e 20 incluidos:")
print(quadrados_pares)
