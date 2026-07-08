def log(func):
    def interna(*args, **kwargs):
        print(f"executando {func.__name__}")
        resultado = func(*args, **kwargs)
        print("fim da execução da interna")
        return resultado
    print("fora da interna e agora retornando ela")
    return interna

@log
def soma(a, b):
    print("entrei na função da soma")
    return a + b

print(soma(3, 4))

# primeiro a ser executado é a decoradora