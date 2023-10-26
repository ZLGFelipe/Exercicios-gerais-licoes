'''
Escreva uma função que calcule o fatorial de um número. O fatorial pode ser definido como:


'''
def calc_fatorial(num: int):
    if num == 0:
        return 1
    if num > 0:
        return num * calc_fatorial(num - 1)

    return "Fatorial indefinido para números negativos"


num = 5
result = calc_fatorial(num)
print(f'O fatorial de {num} é {result}')
