'''Escreva um programa que crie um dicionário relacionando o nome dos estados brasileiros (como chaves) 
às suas siglas. O programa deve solicitar ao usuário o nome de um estado, e chamar uma função que devolve 
a sua sigla.'''

estados_br = {
    "Acre": "AC",
    "Alagoas": "AL",
    "Amapá": "AP",
    "Amazonas": "AM",
    "Bahia": "BA",
    "Ceará": "CE",
    "Distrito Federal": "DF",
    "Espírito Santo": "ES",
    "Goiás": "GO",
    "Maranhão": "MA",
    "Mato Grosso": "MT",
    "Mato Grosso do Sul": "MS",
    "Minas Gerais": "MG",
    "Pará": "PA",
    "Paraíba": "PB",
    "Paraná": "PR",
    "Pernambuco": "PE",
    "Piauí": "PI",
    "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN",
    "Rio Grande do Sul": "RS",
    "Rondônia": "RO",
    "Roraima": "RR",
    "Santa Catarina": "SC",
    "São Paulo": "SP",
    "Sergipe": "SE",
    "Tocantins": "TO"
}

def obter_sigla(estado):
    return estados_br.get(estado, "Estado não encontrado")

estado_final = input("Digite o nome de um estado brasileiro: ")

sigla_do_estado = obter_sigla(estado_final)
print(f"A sigla de {estado_final} é {sigla_do_estado}.")