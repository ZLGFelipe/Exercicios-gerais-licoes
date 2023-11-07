def binario(n: int)->str:
    if n<2:
        return n
    else:
        quociente = binario(n // 2)
        resto = n % 2
        return f'{quociente}{resto}'

print(binario(15))