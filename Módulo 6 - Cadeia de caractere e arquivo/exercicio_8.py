'''
O Programa 6.10 só funciona bem com um nome composto de três partes.
Modifique o programa para que seja possível trabalhar com um número maior de partes.
'''

def format_nome(nome: str) -> str:
    part_nome = nome.split()

    if len(part_nome) >= 2:
        sobrenome = part_nome[-1]
        primeiro_nome = part_nome[0]
        inicial_segundo_nome = part_nome[1][0] if len(
            part_nome) > 2 else ''

        partes_adicionais = " ".join(part_nome[2:])

        nome_formatado = f"{sobrenome}, {primeiro_nome} {inicial_segundo_nome}. {partes_adicionais}"
        return nome_formatado
    else:
        return "Nome inválido"


nome = 'João Carlos da Silva Pereira'
nome_formatado = format_nome(nome)
print(nome_formatado)