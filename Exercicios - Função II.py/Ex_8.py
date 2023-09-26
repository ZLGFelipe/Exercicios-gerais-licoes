'''Crie uma função chamada "calcular_desconto" que
recebe o valor de um produto e uma porcentagem de
desconto como argumentos, e retorna o valor do produto
com o desconto aplicado.'''

def calcular_desconto(produto, porcentagem_desconto):
    desconto = produto * (porcentagem_desconto / 100)
    valor_com_desconto = produto - desconto
    return valor_com_desconto

produto = 100
porcentagem_desconto = 20
valor_com_desconto = calcular_desconto(produto, porcentagem_desconto)
print(f"O produto com desconto fica no valor de R${valor_com_desconto:.2f}")