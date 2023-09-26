'''Reescreva o programa 5.14 validando a entrada de dados do usuário, usando a estrutura try...except.'''

def fahrenheit_celsius(f):
    return (5 / 9) * (f - 32)

def tabela_celsius(fahrenheit):
    celsius = [None] * len(fahrenheit)
    for i, temp in enumerate(fahrenheit):
        celsius[i] = fahrenheit_celsius(fahrenheit[i])
    return celsius

def main():
    try:
        Começo = int(input('Qual o começo das temperaturas Fahrenheit? '))
        fim = int(input('Qual o fim das temperaturas Fahrenheit? '))
        passo = int(input('Qual o passo das temperaturas Fahrenheit? '))

        fahrenheit = list(range(Começo, fim + 1, passo))

        celsius = tabela_celsius(fahrenheit)

        print('Tabela de conversão de Fahrenheit para Celsius')

        for i, temp in enumerate(fahrenheit):
            print('{:>5d} -> {:>5.1f}'.format(temp, celsius[i]))

    except ValueError:
        print('Erro: Certifique-se de inserir valores numéricos válidos.')

main()