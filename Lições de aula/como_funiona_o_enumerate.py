def como_funciona_o_enumerate(lista: list):
    '''contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1'''
    
    for item, indice in enumerate(lista):
        print(f'{indice+1} - {item}')

frutas = [
    'laranja',
    'goiaba',
    'pera',
    'maçã',
    'uva',
    'morango'
]

como_funciona_o_enumerate(frutas)
