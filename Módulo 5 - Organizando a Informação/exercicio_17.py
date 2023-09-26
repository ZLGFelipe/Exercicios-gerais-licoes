'''O que acontece se você chama o comando append() com outra lista? Considere a lista 
primos = [2, 3, 5, 7] e que você use o comando primos.append([23,29,31]). Tente imprimir o elemento 
primos[4]. O que é impresso?'''

primos = [2, 3, 5, 7]
primos.append([23, 29, 31])

print(primos[4])
#R: aparece os 3 numeros que foram juntados, como se o append inteiro fosse o elemento 4.