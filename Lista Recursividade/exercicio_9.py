'''
9. Escreva uma função recursiva que conte o número de palavras em uma string. Considere que as palavras 
são separadas por espaços em branco.
'''
def cont_palavras(frase):
    frase = frase.strip()

    if not frase:
        return 0
    else:
        posicao_espaco = frase.find(' ')
        if posicao_espaco == -1:
            return 1
        else:
            return 1 + cont_palavras(frase[posicao_espaco+1:])


frase = "Esta é uma frase de exemplo"
num_de_palavras = cont_palavras(frase)
print(f'O número de palavras na frase é: {num_de_palavras}')