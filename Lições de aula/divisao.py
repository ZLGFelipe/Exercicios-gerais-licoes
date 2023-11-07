def divisao(quoci: int, divisor: int):
    if quoci < divisor:
        return 0
    else:
        return 1 + divisao(quoci - divisor, divisor)
    

print(divisao(24, 2))