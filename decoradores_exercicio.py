def log(func):
    def interna(*args, **kwargs):  # empacota aqui
        print(f"executando {func.__name__}")
        resultado = func(*args, **kwargs)  # desempacota aqui
        print("fim da execução da interna")
        return resultado
    print("fora da interna e agora retornando ela")
    return interna

# mesma coisa que:
# soma = log(soma) # aponta pra interna aqui
@log
def soma(a, b):
    print("entrei na função da soma")
    return a + b

print(soma(3, 4))


# primeiro a ser executado é a decoradora

# fora da interna e agora retornando ela
# executando soma
# entrei na função da soma
# fim da execução da interna
# 7
