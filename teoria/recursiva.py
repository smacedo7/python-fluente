
def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(4))


def fatorial2(n):
    if n == 1 or n == 0:
        print(f'fatoral de {n} é 0')
    else:
        fat = n * fatorial(n - 1)
        print(f'Fazendo faotrial de {n}')
    return fat


print(fatorial2(4))


def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


print(fibonnaci(8))


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


print(mdc(10, 5))


def mmc(a, b):
    if b == 0:
        return a
    return abs(a * b) / mdc(a, b)


print(mmc(10, 5))
