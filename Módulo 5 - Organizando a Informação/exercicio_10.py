'''Escreva um programa que crie uma lista com os 10 primeiros múltiplos de 7.'''

multiplos_de_7 = []
numero_atual = 1

while len(multiplos_de_7) < 10:
    if numero_atual % 7 == 0:
        multiplos_de_7.append(numero_atual)
    numero_atual += 1

print("Os 10 primeiros múltiplos de 7:")
print(multiplos_de_7)
