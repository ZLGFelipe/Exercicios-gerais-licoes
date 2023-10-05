'''
Tente outras formas de testar se uma palavra é um palíndromo. Tente outro fatiamento.
'''


def e_palindromo(palavra):
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]
    return palavra == palavra_invertida


print(e_palindromo("ana"))
print(e_palindromo("banana"))
