from time import perf_counter

def timer(func):
    def interna(*args, **kwargs):
        print('Dentro da interna!')
        inicio = perf_counter()
        resultado = func(*args, **kwargs)
        fim = perf_counter()
        print(f'o tempo de execução da func {func.__name__} foi de {fim - inicio}')
        return resultado
    return interna

@timer
def contar():
    soma = 0
    for _ in range(5000000):
        soma += _
    return soma

@timer
def potencia(base, expoente):
    return base ** expoente

print(potencia(5, 8))
print(contar())