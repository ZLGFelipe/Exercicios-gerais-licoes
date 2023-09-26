'''Escreva um programa que crie uma lista com o cubo dos números entre 1 e 10, ambos inclusive.'''

cubos = []

for num in range(1, 11):
    cubo = num ** 3
    cubos.append(cubo)

print("Cubos dos números de 1 a 10 incluidos:")
print(cubos)
