'''Crie uma função chamada "verificar_anagrama" que
recebe duas strings como argumentos e retorna True se as
strings forem anagramas (ou seja, possuírem as mesmas
letras, independentemente da ordem), e False caso
contrário.'''

def verificar_anagrama(texto1, texto2):
    texto1 = texto1.replace(" ", "").lower()  
    texto2 = texto2.replace(" ", "").lower()

    if len(texto1) != len(texto2):
        return False
    
    texto1_letras = list(texto1)
    texto2_letras = list(texto2)

    texto1_letras.sort()
    texto2_letras.sort()

    return texto1_letras == texto2_letras
