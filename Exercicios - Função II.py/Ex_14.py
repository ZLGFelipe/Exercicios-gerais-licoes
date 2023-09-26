'''Crie uma função chamada quadrado que recebe dois
parâmetros, um para a base e outro para a altura mostre
a borda de uma quadrado feito por asteriscos.
Por exemplo, para os valores 5 e 3 a saída de ser:
* * * * *
*       *
* * * * * '''

def quadrado(base, altura):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            linha = "* " * base 
        else:
            linha = "* " + "  " * (base - 2) + "*"
        print(linha)

base = int(input('Insira a Base: '))
altura = int(input('Insira a Altura: '))
quadrado(base, altura)