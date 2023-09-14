'''Reescreva o Programa 5.13 usando o comando while.'''

print('Tabela de conversão de Fahrenheit para Celsius')

fahrenheit = 0

while fahrenheit <= 300:
    celsius = (5/9)*(fahrenheit - 32)
    print('{:>5d} -> {:>5.1f}'.format(fahrenheit, celsius))
    fahrenheit += 20