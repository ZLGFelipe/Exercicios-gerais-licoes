'''14- Escreva um programa que calcule a temperatura equivalente em Fahrenheit para os graus Celsius 
entre 0 e 100 com intervalos de 10 graus.'''

for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}  {fahrenheit}')