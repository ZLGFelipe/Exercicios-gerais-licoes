'''11- Escreva um programa que receba um número inteiro n e calcule a soma dos quadrados dos números 
até n-1. Exemplo: se n for igual a 3, seu programa deve dar o resultado da soma dar o resultado da 
soma dos números dos números 1 + 2.'''

n = int(input('Insira um número inteiro: '))
soma_quadrados = (n - 1) * (n - 1 + 1) * (2 * (n - 1) + 1) // 6
print(f'A soma dos quadrados dos números até {n-1} é: {soma_quadrados}')