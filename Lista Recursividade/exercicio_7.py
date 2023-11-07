'''
7. Escreva uma função recursiva que converta um número inteiro em binário representado como uma string.
'''


def inteiro_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return inteiro_binario(num // 2) + str(num % 2)


num1 = 15
binario = inteiro_binario(num1)
print(f'A representação binária de {num1} é {binario}')
