'''
Escreva um programa que copie o conteúdo de um arquivo para um novo arquivo. Seu programa deve testar
se o arquivo de destino já existe e, se afirmativo, deve perguntar ao usuário se ele quer sobrescrevê-lo.
'''

nome_arquivo_origem = input("Digite o nome do arquivo de origem: ")

nome_arquivo_destino = input("Digite o nome do arquivo de destino: ")

try:
    with open(nome_arquivo_origem, 'r') as arquivo_origem:
        arquivo_destino_existe = False
        try:
            with open(nome_arquivo_destino, 'r'):
                arquivo_destino_existe = True
        except FileNotFoundError:
            pass

        if arquivo_destino_existe:
            confirmacao = input(
                "O arquivo de destino já existe. Deseja sobrescrevê-lo? (S/N): ").strip().lower()
            if confirmacao != 's':
                print("Operação cancelada.")
                exit()

        with open(nome_arquivo_destino, 'w') as arquivo_destino:
            conteudo = arquivo_origem.read()
            arquivo_destino.write(conteudo)

    print(
        f"O conteúdo do arquivo '{nome_arquivo_origem}' foi copiado para '{nome_arquivo_destino}'.")

except FileNotFoundError:
    print("Arquivo de origem não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
