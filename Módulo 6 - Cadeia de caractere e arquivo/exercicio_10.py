'''
Escreva um programa que converta todas as letras de um arquivo em maiúsculas e escreva o resultado na tela.
'''

nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

        conteudo_maiusculo = conteudo.upper()

        print(conteudo_maiusculo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
