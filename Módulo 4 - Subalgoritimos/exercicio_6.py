'''6- Modifique o programa da árvore de natal para usar comandos for in range() 
em vez de escrever explicitamente cada linha. Você vai precisar de 4 laços com for para desenhar 
a mesma árvore.'''

altura = int(input("Digite a altura da árvore: "))

for i in range(1, altura + 1):
    espacos = altura - i
    asteriscos = 2 * i - 1
    print(" " * espacos + "*" * asteriscos)

tronco_altura = altura // 3

for _ in range(tronco_altura):
    espacos = altura - tronco_altura
    print(" " * espacos + "*" * (tronco_altura * 2 - 1))