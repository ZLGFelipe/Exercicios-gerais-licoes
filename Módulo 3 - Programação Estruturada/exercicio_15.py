'''15- Escreva um programa que gere o Escreva um programa que gere o seguinte padrão usan seguinte 
padrão usando laços encaixados: do laços encaixados:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*'''

tamanho = 5

for i in range(1, tamanho +1):
  print('*' * i)

for i in range(tamanho - 1, 0, -1):
  print('*' * i)