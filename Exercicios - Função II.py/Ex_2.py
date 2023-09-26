'''Crie uma função chamada "contador_vogais" que recebe
uma string como argumento e retorna a quantidade de
vogais na string.'''

def contador_vogais(texto: str):
    formatado =  texto.lower()
    vogais = ('a', 'e', 'i', 'o', 'u')
    contador = 0

    for letra in formatado:
        if letra in vogais:
            contador += 1

    return contador

total = contador_vogais('Felipe Zamariolli')
print(f'total de vogais = {total}')