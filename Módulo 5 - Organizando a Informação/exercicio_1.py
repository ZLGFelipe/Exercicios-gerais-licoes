'''Escreva um programa que receba uma lista de temperaturas em Celsius e escreva na tela o resultado 
da conversão dessas temperaturas em Fahrenheit. (Não se esqueça de usar a fórmula correta!)'''

def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def converter(lista_temps: list):
    for celsius in lista_temps:
        fahrenheit = celsius_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")


temperaturas_celsius = [25.5, 30.0, 15.3, 10.8, 0.0]
print("Resultados em Fahrenheit:")
converter(temperaturas_celsius)