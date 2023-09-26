'''16- Escreva um programa que crie uma lista com 3 elementos e peça ao usuário um índice de um elemento
 a ser impresso. Se o usuário pedir um índice fora da faixa de valores permitidos 
(abaixo de zero ou acima de 2), o programa deve emitir uma mensagem de erro (Use a exceção IndexError).'''

lista = [10, 20, 30]

indice = int(input("Digite o índice do elemento a ser impresso (0 a 2): "))

if 0 <= indice <= 2:
    elemento = lista[indice]
    print(f"O elemento no índice {indice} é {elemento}")
else:
    print("Erro: Índice fora da faixa válida (0 a 2)")