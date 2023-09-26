'''5- Escreva um programa que receba dois números inteiros pelo teclado e informe se o segundo é 
um múltiplo do primeiro.'''

numero1 = int(input('Insira um número inteiro: '))
numero2 = int(input('Insira outro número inteiro: '))
if numero2 % numero1 == 0:
    print(f'O número {numero2} é um múltiplo do número {numero1}.')
else:
    print(f'O número {numero2} não é um múltiplo do número {numero1}.')