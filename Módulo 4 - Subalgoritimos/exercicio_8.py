'''8- Escreva uma função que receba um valor inteiro e devolva seu quadrado.'''

numero = int(input('Digite um valor: '))
def quadrado(valor):
    return valor ** 2

resultado = quadrado(numero)
print(f"O quadrado de {numero} é {resultado}")