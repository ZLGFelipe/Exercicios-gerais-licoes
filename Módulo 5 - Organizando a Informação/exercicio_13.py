'''Dada a lista [10, 2, 32, 14, 35, 46, 17, 58, 199, 19], escreva um programa que imprima:

1.os elementos de índices pares;

2.os elementos de índices ímpares;

3.os elementos entre os índices 2 (inclusive) e 4 (exclusive);

4.o elemento de índice 1 e depois os elementos distantes 3 posições a partir de 1, até o final.'''

lista = [10, 2, 32, 14, 35, 46, 17, 58, 199, 19]

elementos_indices_pares = [lista[i] for i in range(len(lista)) if i % 2 == 0]

elementos_indices_impares = [lista[i] for i in range(len(lista)) if i % 2 != 0]

elementos_entre_indices_2_e_4 = lista[2:4]

elemento_indice_1_e_distantes_3 = [lista[1]] + lista[1::3]

print("1. Elementos de índices pares:", elementos_indices_pares)
print("2. Elementos de índices ímpares:", elementos_indices_impares)
print("3. Elementos entre os índices 2 (inclusive) e 4 (exclusive):", elementos_entre_indices_2_e_4)
print("4. Elemento de índice 1 e elementos distantes 3 posições a partir de 1, até o final:", elemento_indice_1_e_distantes_3)


