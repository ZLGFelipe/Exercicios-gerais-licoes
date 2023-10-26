'''
Escreva uma função recursiva que imprima uma string na ordem inversa.
Ex.: “celacanto provoca maremoto” será impressa como “otomeram acovorp otnacalec”.
'''


def string_inversa(string: str) -> str:
    if len(string) == 0:
        return ""

    return string[-1] + string_inversa(string[:-1])


text = "celacanto provoca maremoto"
result = string_inversa(text)
print(result)