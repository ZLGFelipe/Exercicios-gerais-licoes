'''O que acontece se o terceiro parâmetro de uma operação de fatiamento for -1? 
Teste em uma lista qualquer o comando lista[::-1]. Qual a diferença para reverse()?'''

lista = [1, 2, 3, 4, 5]

lista2 = lista[::-1]

print(lista2)

lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista) 

#A diferença é que no -1 ele inverte mas criando uma nova lista, no reverse ele altera a própria.
