'''9- Escreva uma função fahrenheit(celsius) que receba um valor de uma temperatura Celsius e devolva 
seu equivalente em Fahrenheit. Usando esta função, imprima os valores equivalentes das temperaturas 
Celsius em Fahrenheit entre 0 e 100, com entre 0 e 100, com incrementos de 10. incrementos de 10.'''

def fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

for celsius in range(0, 101, 10):
    fahrenheit_value = fahrenheit(celsius)
    print(f"| {celsius:^7} | {fahrenheit_value:^9.2f} |")