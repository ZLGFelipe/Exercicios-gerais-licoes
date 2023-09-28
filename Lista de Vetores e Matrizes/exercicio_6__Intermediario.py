'''
Implemente uma função que calcule o produto escalar entre dois vetores.
'''


def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho")

    resultado = 0

    for i in range(len(vetor1)):
        resultado += vetor1[i] * vetor2[i]

    return resultado


vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
resultado = produto_escalar(vetor1, vetor2)
print(f"O produto escalar entre {vetor1} e {vetor2} é {resultado}")
