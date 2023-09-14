'''Partindo da lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use os comandos desta seção para 
obter [5, 6, 7, 8, 9, 4, 3, 2, 1, 0].'''

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

primeira_parte = lista[:5] 
segunda_parte = lista[5:]  

primeira_parte = primeira_parte[::-1] 
segunda_parte = segunda_parte[::-1] 

lista = segunda_parte + primeira_parte

print(lista)
