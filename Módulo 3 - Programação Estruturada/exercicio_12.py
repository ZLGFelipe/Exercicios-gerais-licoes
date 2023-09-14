'''12- Escreva um programa que calcule a média dos números digitados pelo usuário. O programa deve 
calcular a média quando o usuário digitar o número zero.'''

def calcular_media(numeros):
  total = sum(numeros)
  quantidade = len(numeros)
  if quantidade == 0:
   return 0
  else:
    media = total / quantidade
    return media

numeros_digitados = []
numero = float(input('Digite um numero (ou 0 pra sair): '))

while numero != 0:
  numeros_digitados.append(numero)
  numero = float(input('Digite um numero (ou 0 pra sair): '))
  break

media = calcular_media(numeros_digitados)
print(f'A média dos numeros digitados é: {media}')