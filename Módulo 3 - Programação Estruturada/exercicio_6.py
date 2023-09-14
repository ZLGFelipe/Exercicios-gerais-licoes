'''6- Escreva um programa em Python que teste se um número é divisível por 3, 5 ou 7. Seu programa 
deve dizer por qual desses valores o número é divisível.'''

numero = int(input('Insira um número inteiro: '))
if numero % 3 == 0:
    print(f'O número {numero} é divisível por 3.')
elif numero % 5 == 0:
    print(f'O número {numero} é divisível por 5.')
elif numero % 7 == 0:
    print(f'O número {numero} é divisível por 7.')
else:
    print(f'O número {numero} não é divisível por 3, nem por 5 nem por 7.')