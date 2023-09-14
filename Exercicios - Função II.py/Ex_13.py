'''Crie uma função chamada quadrado que recebe dois
parâmetros, um para a base e outro para a altura mostre
um quadrado feito por asteriscos.
Por exemplo, para os valores 5 e 3 a saída de ser:
* * * * *
* * * * *
* * * * * '''

def quadrado(base, altura):
    for _ in range(altura):
        linha = " ".join(["*"] * base) 
        print(linha)

base = int(input('Insira a Base: '))
altura = int(input('Insira a Altura: '))
quadrado(base, altura)