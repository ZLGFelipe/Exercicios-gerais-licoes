'''
Escreva uma função que receba uma string como parâmetro e escreva-a invertida, usando apenas o fatiamento.
 Ex.: "celacanto provoca maremoto" imprime "otomeram acovorp otnacalec". Dica: o passo pode ser negativo.
'''


def inverter_string(string):
    string_invertida = string[::-1]
    print(string_invertida)


entrada = "celacanto provoca maremoto"
inverter_string(entrada)
