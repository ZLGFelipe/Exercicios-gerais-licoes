def fatorial(n: int):
    if n == 1:
        return n
    else:
        return n * fatorial(n-1)


n = 5 

print(fatorial(n))