'''
O teste de palíndromo desta seção tem um grande problema: ele não diferencia maiúsculas de minúsculas.
 Desse modo, "Ovo" não seria identificado como palíndromo. Como se pode consertar isso?
   Pesquise a função de Python "lower()" que transforma maiúsculas em minúsculas.
'''


def e_palindromo(palavra):
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]
    return palavra == palavra_invertida


print(e_palindromo("Ovo"))
print(e_palindromo("banana"))
