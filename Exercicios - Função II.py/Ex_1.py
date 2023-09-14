'''Crie uma função chamada "maior_numero" que recebe uma lista de números como argumento 
e retorna o maior número da lista'''
#maior numero com 'max'
def maior_numero(lista_numeros):
    maior= max(lista_numeros) 
    return maior

lista = [4, 7, 1, 2, 10]
x = maior_numero(lista)
print(f'o maior numero é {x}')

#maior numero sem 'max'

def maior_num(lista_num):
    Maior = -1
    for item in lista_num:
        if Maior < item:
            Maior = item

    return Maior

lista = [4, 7, 1, 2, 10]
maiorr = maior_num(lista)
print(f'Maior = {maiorr}')