'''
Escreva uma função recursiva que diga se uma palavra é um palíndromo.
Ex: arara, ovo, radar, osso.
'''

def palindromo(palavra: str) -> bool:
    palavra = palavra.lower()
    if len(palavra) <= 1:
        return True
    elif palavra[0] == palavra[-1]:
        return palindromo(palavra[1:-1])
    else:
        return False


palavra1 = "arara"
palavra2 = "ovo"
palavra3 = "radar"
palavra4 = "osso"

print(palindromo(palavra1))
print(palindromo(palavra2))
print(palindromo(palavra3))
print(palindromo(palavra4))