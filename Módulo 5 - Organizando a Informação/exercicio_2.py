'''Reescreva o programa 5.13 de modo a imprimir o resultado a partir do último elemento (de 300 para 0).'''

print('Tabela de conversão de Fahrenheit para Celsius')

for fahrenheit in range(300, -1, -20):

    celsius = (5/9)*(fahrenheit - 32)

    print('{:>5d} -> {:>5.1f}'.format(fahrenheit, celsius))