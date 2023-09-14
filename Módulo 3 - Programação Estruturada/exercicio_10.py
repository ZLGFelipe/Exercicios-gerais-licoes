'''10- Este programa irá exigir um pouco mais de testes. É comum que donos de cachorros calculem 
a “idade humana” equivalente de seus cães usando uma simples multiplicação por 7, mas a conta é um pouco
mais complexa que isso. O envelhecimento de um cão depende de sua raça. Até os dois primeiros anos de 
cães de uma raça pequena, cada ano equivale a 12,5 anos humanos. Para os cães médios, esses dois anos 
contam 10,5 por ano e para os cães grandes, cada ano conta 9 anos. Acima de dois anos, temos de contar 
5,2 anos por ano para um beagle (raça pequena), 5,7 para um golden retriever (raça média) e 
7,8 para um pastor alemão (raça grande). Considere que um cão pequeno pesa até 3 quilos, um cão médio 
pesa entre 10 e 23 quilos e um cão grande tem acima de quilos e um cão grande tem acima de 23 quilos. 
23 quilos. Escreva um programa que solicite o peso do cão e a sua idade. Com esses dados, seu programa 
deve calcular a “idade humana” do cão usando como exemplo os cães citados anteriormente.'''

def calcular_idade_humana(peso, idade):
  if peso <= 3:
    if idade <= 2:
      idade_humana = idade * 12.5
    else:
      idade_humana = 2 * 12.5 + (idade - 2) * 5.2
  elif 10 <= peso <= 23:
    if idade <= 2:
      idade_humana = idade * 10.5
    else:
      idade_humana = 2 * 10.5 + (idade - 2) * 5.7
  else:
    if idade <= 2:
      idade_humana = idade * 9
    else:
      idade_humana = 2* 9 +(idade - 2) * 7.8
  return idade_humana

peso = float(input('Digite o peso do cão (em quilos): '))
idade = int(inpu('Digite a idade do cão (em anos): '))

idade_equivalente = calcular _idade_humana(peso, idade)
print(f'A idade humana equivalente do cão é: {idade_equivalente}')