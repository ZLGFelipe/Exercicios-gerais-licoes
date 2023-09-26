'''3- Escreva um programa em Python que leia um número e imprima a si mesmo, o seu quadrado e o seu cubo.'''

def exercicio_4_3(numero):
    print(f'numero = {numero}')
    print(f'{numero}² = {numero ** 2}')
    print(f'{numero}³ = {numero ** 3}')

valor = int(input('Digite um valor: '))
exercicio_4_3(valor)