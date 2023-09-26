'''Gere uma lista com 100 números de 0 a 99, com o comando range() e, usando valores negativos no 
fatiamento, escreva um programa que imprima:

1.o último elemento da lista original e depois, decrescendo, os elementos distantes 3 posições a partir 
do final até o início;

2.os elementos entre o índice 87 (inclusive) e o índice 34 (exclusive), em ordem decrescente de índices;

3.todos os elementos, exceto os dois últimos.'''

lista = list(range(100))

ultimo_elemento_e_distantes = lista[-1::-3]

elementos_entre_indices = lista[87:33:-1]

todos_exceto_os_ultimos_dois = lista[:-2]

print("1. Último elemento e elementos distantes 3 posições a partir do final até o início:", ultimo_elemento_e_distantes)
print("2. Elementos entre o índice 87 (inclusive) e o índice 34 (exclusive) em ordem decrescente:", elementos_entre_indices)
print("3. Todos os elementos, exceto os dois últimos:", todos_exceto_os_ultimos_dois)


