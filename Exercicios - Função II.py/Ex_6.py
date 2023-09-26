'''Crie uma função chamada "encontrar_primos" que recebe
um número inteiro positivo como argumento e retorna
uma lista com todos os números primos menores ou iguais
ao número fornecido.'''


def encontrar_primo(numero: int):
    primos = []
    for i in range(1, numero + 1):
        if e_primo(i):
            primos.append(i)
            print(i)
     
    return primos

        
def e_primo(numero: int):
    for i in range(2, numero):
        divide = numero % i == 0
        if divide:
            return False
        
        return True
        
lista_primos=encontrar_primo(9)
print(lista_primos)