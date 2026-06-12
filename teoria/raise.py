print(123)
# raise ValueError('Deu erro')  # ValueError: Deu erro
# da erro de graça
# basicamente criar um erro


# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         raise
#         # print('_____')
#         # return n


def erro_divide_0(d):
    if d == 0:
        raise ZeroDivisionError('Dividiu por zero')
    return True

# def divide(numero, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError('Você está tentanto dividir por zero! ')


def verificador(numero):
    type_numero = type(numero)
    if numero is not isinstance(numero, (int, float)):
        raise TypeError(
            f'{numero} deve ser int ou float '
            f'{type_numero.__name__} enviado! '
        )
    return True


def divide(n, d):
    erro_divide_0(d)
    verificador(n)
    verificador(d)
    return n / d


print(divide(8, 0))
