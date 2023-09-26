def girar_lista(qtd: int, lista: list) -> list:
    for _ in range(qtd):
        ultimo = lista.pop()
        lista.insert(0, ultimo)
    return lista


Lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(girar_lista(5, Lista))
