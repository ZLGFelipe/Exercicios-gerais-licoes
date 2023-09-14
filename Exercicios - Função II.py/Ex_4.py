'''Crie uma função chamada "calcular_media" que recebe
uma lista de números como argumento e retorna a média
aritmética dos elementos.'''

def calcular_media(lista_numeros):
    if not lista_numeros:  
        return 0  
    
    soma = sum(lista_numeros)  
    media = soma / len(lista_numeros)  
    return media

numeros = [2.5, 2.5, 4]
media = calcular_media(numeros)
print(f"A média dos números é: {media}")