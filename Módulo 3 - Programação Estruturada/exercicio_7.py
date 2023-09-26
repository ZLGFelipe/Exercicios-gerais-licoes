'''7- Uma empresa vai conceder um aumento diferenciado a seus funcionários, segundo os seguintes 
critérios: quem ganha até 1000 reais (inclusive) terá aumento de 20 %; entre 1000 e 2000 (inclusive), 
aumento de 18 %; entre 2000 e 4000 (inclusive) aumento de 15 % e acima de 4000 aumento de 10 %. 
Escreva um programa que, dado um valor de salário, calcule o novo valor após o aumento.'''

salario = float(input('Digite o valor do salário: '))
if salario <= 1000:
    novo_salario = salario * 1.20
elif salario <= 2000:
    novo_salario = salario * 1.18
elif salario <= 4000:
    novo_salario = salario * 1.15
else:
    novo_salario = salario * 1.10
print(f'O novo valor do salário é {novo_salario} reais.')