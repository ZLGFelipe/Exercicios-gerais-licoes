'''17- Modifique o programa anterior para que o mesmo capture também a exceção ValueError da entrada 
de dados pelo da entrada de dados pelo usuário.'''

lista = [10, 20, 30]

while True:
    entrada = input("Digite o índice do elemento a ser impresso (0 a 2): ")

    if entrada.isdigit():
        indice = int(entrada)
        if 0 <= indice <= 2:
            elemento = lista[indice]
            print(f"O elemento no índice {indice} é {elemento}")
            break
        else:
            print("Erro: Índice fora da faixa válida (0 a 2)")
    else:
        print("Erro: Entrada inválida. Digite um número inteiro.")