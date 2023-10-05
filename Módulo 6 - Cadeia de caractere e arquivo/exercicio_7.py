'''
Escreva uma função que receba uma string como parâmetro e diga se se trata de um palíndromo ou não.
Na string devem ser ignorados os espaços em branco e as letras maiúsculas e minúsculas não são diferenciadas.
Por exemplo, a frase "Seco de raiva coloco no colo caviar e doces" deve ser considerada um palíndromo.
'''

def e_palindromo(frase):
    frase = frase.replace(" ", "").lower()

    return frase == frase[::-1]

frase1 = "Seco de raiva coloco no colo caviar e doces"
frase2 = "Olá, mundo!"
frase3 = "Anita lava a tina"

print(e_palindromo(frase1))
print(e_palindromo(frase2))
print(e_palindromo(frase3))
