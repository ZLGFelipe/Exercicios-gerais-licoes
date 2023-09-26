'''
Crie uma função que receba dois vetores e retorne a soma deles.
'''

#forma basica
def soma_vetores(vetor1: list, vetor2: list) -> list:
    vetor_soma = []
    for i in range(len(vetor1)):
        vetor_soma.append(vetor1[i]+vetor2[i])
    return vetor_soma


l1 = [2, 8, 7]
l2 = [8, 2, 3]

l3 = soma_vetores(l1, l2)
print(l3)

#forma completa
def Soma_vetores(Vetor1: list, Vetor2: list) -> list:
    Vetor_soma = []
    maior = max(len(Vetor1), len(Vetor2))
    for i in range(maior):
        Valor1 = Vetor1[i] if i < len(Vetor1) else 0 
        Valor2 = Vetor2[i] if i < len(Vetor2) else 0 

        Vetor_soma.append(Valor1 +Valor2)
    return Vetor_soma


L1 = [2, 8, 7]
L2 = [8, 2, 3, 6]

L3 = Soma_vetores(L1, L2)
print(L3)
