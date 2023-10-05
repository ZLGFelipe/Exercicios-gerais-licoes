'''
Escreva um programa que salve uma tabela com a conversão de temperaturas Celsius para Fahrenheit de 0 a 300.
'''

import csv


def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


tabela = [(celsius, celsius_para_fahrenheit(celsius))
          for celsius in range(301)]

nome_arquivo = "tabela_temperaturas.csv"

with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)

    writer.writerow(["Celsius", "Fahrenheit"])

    writer.writerows(tabela)

print(f"A tabela de temperaturas foi salva no arquivo '{nome_arquivo}'.")
