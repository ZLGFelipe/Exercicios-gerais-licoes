'''Os dicionários de Python não são ordenados, pois sua função principal é a busca rápida de uma 
informação baseada em uma chave. Modifique o programa sobre aeroportos desta seção para trabalhar apenas 
com tuplas, eliminando o dicionário e usando o nome da cidade como primeiro elemento da tupla.'''

latitude_g = (22, 48, 34)
longitude_g = (43, 15, 0)
aeroporto_g = ('Galeão', latitude_g , longitude_g)

latitude_gua = (23, 26, 6)
longitude_gua = (46, 28, 22)
aeroporto_gua = ('Guarulhos', latitude_gua, longitude_gua)

aeroportos = [
    aeroporto_g,
    aeroporto_gua
]

for aeroporto in aeroportos:
    cidade = aeroporto[0]
    latitude = f'{aeroporto[1][0]}º{aeroporto[1][1]}"{aeroporto[1][2]}"'
    longitude = f'{aeroporto[2][0]}º{aeroporto[2][1]}"{aeroporto[2][2]}"'

    print(
        f'Aeroporto {cidade}:\n\t{aeroporto[0]}\n\tLatitude: {latitude}\n\tLongitude: {longitude}')