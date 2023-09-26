'''Crie uma função chamada "verificar_palindromo" que
recebe uma string como argumento e retorna True se a
string for um palíndromo (ou seja, pode ser lida da mesma
forma de trás para frente), e False caso contrário.'''

def verificar_palindromo(texto):
    texto = texto.lower()  
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1] 

print(verificar_palindromo("Hello, World!"))
print(verificar_palindromo("Anotaram a data da maratona"))