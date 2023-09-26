'''Execute as mesmas operações do exercício 5.17, mas usando o comando extend() no lugar de append() 
com uma lista. O que acontece? Houve alguma diferença? Tente imprimir o elemento primos[4]. 
O que é impresso?'''

primos = [2, 3, 5, 7]
primos.extend([23, 29, 31])

print(primos[4])
#R: agora aparece so o 23, pois o 23 é exatamente o elemento 4.