'''10- Escreva uma função celsius(fahrenheit) que receba um valor de uma temperatura Fahrenheit 
e devolva seu equivalente em Celsius. Usando esta função, imprima os valores equivalentes das 
temperaturas Fahrenheit em Celsius entre 0 e 300, com incrementos de 10. Coloque comandos para que 
o usuário escolha os valores de início, fim e os valores de início, fim e passo que serão usados 
passo que serão usados como argumentos da função.'''

def celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

inicio = int(input("Digite o valor de início (Fahrenheit): "))
fim = int(input("Digite o valor de fim (Fahrenheit): "))
passo = int(input("Digite o valor do passo: "))

for fahrenheit in range(inicio, fim + 1, passo):
    celsius_value = celsius(fahrenheit)
    print(f"| {fahrenheit:^10} | {celsius_value:^10.2f} |")