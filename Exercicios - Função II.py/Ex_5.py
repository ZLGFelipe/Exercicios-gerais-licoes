'''Crie uma função chamada "calcular_potencia" que recebe
dois números como argumentos: a base e o expoente. A
função deve retornar a base elevada ao expoente.'''

def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado

base = int(input('Insira a Base: '))
expoente = int(input('Insira o expoente: '))
potencia = calcular_potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a {potencia}")