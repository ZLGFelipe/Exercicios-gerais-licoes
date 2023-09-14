'''Escreva um programa que crie uma lista com números digitados pelo usuário e forneça como saída a 
média desses números.'''

numeros = []

while True:
    entrada = input("Digite um número (ou 'parar' para encerrar): ")
  
    if entrada.lower() == 'parar':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

if numeros:
    media = sum(numeros) / len(numeros)
    print("Média dos números:", media)
else:
    print("Nenhum número foi inserido.")
