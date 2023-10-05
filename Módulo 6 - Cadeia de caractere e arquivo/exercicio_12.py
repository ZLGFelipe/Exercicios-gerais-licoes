'''
Escreva um programa que converta a primeira letra de cada palavra de um arquivo em maiúscula e 
escreva o resultado na tela.
'''

nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

        conteudo_capitalizado = " ".join(
            [palavra.capitalize() for palavra in conteudo.split()])

        print(conteudo_capitalizado)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
