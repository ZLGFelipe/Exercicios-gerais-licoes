'''Use os comandos desta seção para criar uma nova lista com os elementos da primeira metade de uma lista. 
Por exemplo, se temos lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use os comandos para obter [0, 1, 2, 3, 4].'''

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeira_metade = lista[:len(lista)//2]

print(primeira_metade)
